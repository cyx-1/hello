# Wisdom-Driven Knowledge Augmented Generation at Scale - Chin Keong Lam, Patho AI

**Video URL:** https://www.youtube.com/watch?v=9AQOvT8LnMI

---

## Full Transcript

### [00:00 - 01:00]

**[00:17]** So, hi. Hi everybody. Uh, my name is

**[00:17]** So, hi. Hi everybody. Uh, my name is Ching Kyong Lamb. Um, I'm the founder

**[00:19]** Ching Kyong Lamb. Um, I'm the founder

**[00:19]** Ching Kyong Lamb. Um, I'm the founder and CEO of PO.AI.

**[00:22]** and CEO of PO.AI.

**[00:22]** and CEO of PO.AI. Uh, a bit background about my company.

**[00:24]** Uh, a bit background about my company.

**[00:24]** Uh, a bit background about my company. uh PTO AI started two years ago with a

**[00:27]** uh PTO AI started two years ago with a

**[00:27]** uh PTO AI started two years ago with a invitation from National Science

**[00:28]** invitation from National Science

**[00:28]** invitation from National Science Foundation from the SBIR grant funding

**[00:32]** Foundation from the SBIR grant funding

**[00:32]** Foundation from the SBIR grant funding investigating LLM. We did a LMB driven

**[00:36]** investigating LLM. We did a LMB driven

**[00:36]** investigating LLM. We did a LMB driven drug discovery application. Uh since

**[00:38]** drug discovery application. Uh since

**[00:38]** drug discovery application. Uh since then we branch out to leverage what we

**[00:41]** then we branch out to leverage what we

**[00:41]** then we branch out to leverage what we learned about building AI system for

**[00:43]** learned about building AI system for

**[00:43]** learned about building AI system for large corporation. We are currently

**[00:45]** large corporation. We are currently

**[00:45]** large corporation. We are currently building expert AI system for several

**[00:48]** building expert AI system for several

**[00:48]** building expert AI system for several clients. Currently the system we build

**[00:50]** clients. Currently the system we build

**[00:50]** clients. Currently the system we build goes beyond rack system. Um many of our

**[00:53]** goes beyond rack system. Um many of our

**[00:53]** goes beyond rack system. Um many of our client is asking for AI system that

**[00:55]** client is asking for AI system that

**[00:55]** client is asking for AI system that perform task like research and advisory

**[00:58]** perform task like research and advisory

**[00:58]** perform task like research and advisory role based on their area of interest. Uh


### [01:00 - 02:00]

**[01:01]** role based on their area of interest. Uh

**[01:01]** role based on their area of interest. Uh today the talk is about sharing with our

**[01:05]** today the talk is about sharing with our

**[01:05]** today the talk is about sharing with our fellow AI engineer what we learned so

**[01:06]** fellow AI engineer what we learned so

**[01:06]** fellow AI engineer what we learned so far building this kind of system. Okay.

**[01:09]** far building this kind of system. Okay.

**[01:09]** far building this kind of system. Okay. Uh what is knowledge? Okay. Generally

**[01:11]** Uh what is knowledge? Okay. Generally

**[01:11]** Uh what is knowledge? Okay. Generally philosophically I say knowledge is the

**[01:13]** philosophically I say knowledge is the

**[01:13]** philosophically I say knowledge is the understanding and awareness gained

**[01:15]** understanding and awareness gained

**[01:15]** understanding and awareness gained through experience, education and the

**[01:17]** through experience, education and the

**[01:17]** through experience, education and the comprehension of facts and principle.

**[01:20]** comprehension of facts and principle.

**[01:20]** comprehension of facts and principle. And that lead to the next question is

**[01:22]** And that lead to the next question is

**[01:22]** And that lead to the next question is what is knowledge graph? Right? So

**[01:24]** what is knowledge graph? Right? So

**[01:24]** what is knowledge graph? Right? So knowledge graph is a systematic method

**[01:26]** knowledge graph is a systematic method

**[01:26]** knowledge graph is a systematic method of preserving wisdom by connecting them

**[01:29]** of preserving wisdom by connecting them

**[01:29]** of preserving wisdom by connecting them and creating a network or interconnect

**[01:31]** and creating a network or interconnect

**[01:31]** and creating a network or interconnect relationship. That's important. The

**[01:33]** relationship. That's important. The

**[01:33]** relationship. That's important. The graph represent the thought process

**[01:36]** graph represent the thought process

**[01:36]** graph represent the thought process and comprehensive tonomy of a specific

**[01:39]** and comprehensive tonomy of a specific

**[01:39]** and comprehensive tonomy of a specific domain of expertise. That's why this is

**[01:41]** domain of expertise. That's why this is

**[01:41]** domain of expertise. That's why this is is very important for people moving

**[01:44]** is very important for people moving

**[01:44]** is very important for people moving forward is about AI system then think a

**[01:47]** forward is about AI system then think a

**[01:47]** forward is about AI system then think a lot and return uh advice instead of just

**[01:50]** lot and return uh advice instead of just

**[01:50]** lot and return uh advice instead of just retrieve you know data from your

**[01:52]** retrieve you know data from your

**[01:52]** retrieve you know data from your database right so that comes to the

**[01:54]** database right so that comes to the

**[01:54]** database right so that comes to the development of this uh K a okay what is

**[01:57]** development of this uh K a okay what is

**[01:57]** development of this uh K a okay what is K a kag stand for knowledge augment


### [02:00 - 03:00]

**[02:00]** K a kag stand for knowledge augment

**[02:00]** K a kag stand for knowledge augment generations and it's different from rack

**[02:02]** generations and it's different from rack

**[02:02]** generations and it's different from rack okay it is enhanced language model by

**[02:05]** okay it is enhanced language model by

**[02:05]** okay it is enhanced language model by integrating structure knowledge graph

**[02:07]** integrating structure knowledge graph

**[02:07]** integrating structure knowledge graph for more accurate and insightful respond

**[02:09]** for more accurate and insightful respond

**[02:10]** for more accurate and insightful respond making needs smarter more structural

**[02:12]** making needs smarter more structural

**[02:12]** making needs smarter more structural approach than a simple rack. K a doesn't

**[02:16]** approach than a simple rack. K a doesn't

**[02:16]** approach than a simple rack. K a doesn't just retrieve remember it understand

**[02:19]** just retrieve remember it understand

**[02:19]** just retrieve remember it understand this is different

**[02:21]** this is different

**[02:21]** this is different okay after in interviewing a lot of my

**[02:24]** okay after in interviewing a lot of my

**[02:24]** okay after in interviewing a lot of my client okay so or we also expert in a

**[02:27]** client okay so or we also expert in a

**[02:27]** client okay so or we also expert in a certain area of scale I found that there

**[02:29]** certain area of scale I found that there

**[02:29]** certain area of scale I found that there are common ways of their thinking

**[02:32]** are common ways of their thinking

**[02:32]** are common ways of their thinking decision making process the way that

**[02:34]** decision making process the way that

**[02:34]** decision making process the way that make them expert in their area knowledge

**[02:37]** make them expert in their area knowledge

**[02:37]** make them expert in their area knowledge graph seems to be a perfect fit so here

**[02:40]** graph seems to be a perfect fit so here

**[02:40]** graph seems to be a perfect fit so here is the graph or state diagram if you're

**[02:42]** is the graph or state diagram if you're

**[02:42]** is the graph or state diagram if you're a computer engineering grad like So um

**[02:45]** a computer engineering grad like So um

**[02:45]** a computer engineering grad like So um it shows a wisdom the the wisdom note as

**[02:50]** it shows a wisdom the the wisdom note as

**[02:50]** it shows a wisdom the the wisdom note as you can see is the is a core right it's

**[02:53]** you can see is the is a core right it's

**[02:53]** you can see is the is a core right it's wisdom it just isn't static it actively

**[02:57]** wisdom it just isn't static it actively

**[02:57]** wisdom it just isn't static it actively guide decision and fused by other

**[02:59]** guide decision and fused by other

**[02:59]** guide decision and fused by other element


### [03:00 - 04:00]

**[03:02]** element

**[03:02]** element the output from the wisdom actually goes

**[03:05]** the output from the wisdom actually goes

**[03:05]** the output from the wisdom actually goes to decision making in the blue right

**[03:07]** to decision making in the blue right

**[03:07]** to decision making in the blue right wisdom isn't passive it guide decision

**[03:11]** wisdom isn't passive it guide decision

**[03:11]** wisdom isn't passive it guide decision helping us choose wisely Okay. And then

**[03:14]** helping us choose wisely Okay. And then

**[03:14]** helping us choose wisely Okay. And then the decision making analyze the

**[03:16]** the decision making analyze the

**[03:16]** the decision making analyze the situation given in the circle in the uh

**[03:19]** situation given in the circle in the uh

**[03:19]** situation given in the circle in the uh green and decision aren't make you know

**[03:23]** green and decision aren't make you know

**[03:23]** green and decision aren't make you know in a vacuum. Okay. They analyze real

**[03:26]** in a vacuum. Okay. They analyze real

**[03:26]** in a vacuum. Okay. They analyze real world situation. That's the difference.

**[03:27]** world situation. That's the difference.

**[03:27]** world situation. That's the difference. Okay. So look at the wisdom input. Okay.

**[03:30]** Okay. So look at the wisdom input. Okay.

**[03:30]** Okay. So look at the wisdom input. Okay. Look at the relationship feedback from

**[03:32]** Look at the relationship feedback from

**[03:32]** Look at the relationship feedback from the knowledge to wisdom in gold color.

**[03:36]** the knowledge to wisdom in gold color.

**[03:36]** the knowledge to wisdom in gold color. Example of that is knowledge to wisdom

**[03:39]** Example of that is knowledge to wisdom

**[03:39]** Example of that is knowledge to wisdom like all your books smart and

**[03:43]** like all your books smart and

**[03:43]** like all your books smart and encyclopedia Wikipedia whatever you

**[03:45]** encyclopedia Wikipedia whatever you

**[03:45]** encyclopedia Wikipedia whatever you store plus once that data get absorbed

**[03:50]** store plus once that data get absorbed

**[03:50]** store plus once that data get absorbed by whatever model you use up there it

**[03:53]** by whatever model you use up there it

**[03:53]** by whatever model you use up there it need to regurgitate that and understand

**[03:55]** need to regurgitate that and understand

**[03:55]** need to regurgitate that and understand that's why it's very important that

**[03:57]** that's why it's very important that

**[03:57]** that's why it's very important that wisdom is able to synthesize the data

**[03:58]** wisdom is able to synthesize the data

**[03:58]** wisdom is able to synthesize the data after you ingested knowledge okay that's


### [04:00 - 05:00]

**[04:00]** after you ingested knowledge okay that's

**[04:00]** after you ingested knowledge okay that's a kind of abstract but I I'll come come

**[04:02]** a kind of abstract but I I'll come come

**[04:02]** a kind of abstract but I I'll come come to that later what I'm talking about

**[04:04]** to that later what I'm talking about

**[04:04]** to that later what I'm talking about okay from Insight example of that is

**[04:08]** okay from Insight example of that is

**[04:08]** okay from Insight example of that is wisdom derive pattern from chaos like

**[04:11]** wisdom derive pattern from chaos like

**[04:11]** wisdom derive pattern from chaos like some of my client has a lot of social

**[04:13]** some of my client has a lot of social

**[04:13]** some of my client has a lot of social media they their product how do they you

**[04:15]** media they their product how do they you

**[04:16]** media they their product how do they you know track their product sediment from

**[04:17]** know track their product sediment from

**[04:17]** know track their product sediment from from social media right so it's okay

**[04:19]** from social media right so it's okay

**[04:19]** from social media right so it's okay chaotic and from ax tweet right so so

**[04:22]** chaotic and from ax tweet right so so

**[04:22]** chaotic and from ax tweet right so so from that you can see some pattern of

**[04:24]** from that you can see some pattern of

**[04:24]** from that you can see some pattern of their competitor versus uh current what

**[04:26]** their competitor versus uh current what

**[04:26]** their competitor versus uh current what my product is that that's like an

**[04:28]** my product is that that's like an

**[04:28]** my product is that that's like an example of that and I will go to that

**[04:30]** example of that and I will go to that

**[04:30]** example of that and I will go to that later okay when all these connected

**[04:33]** later okay when all these connected

**[04:33]** later okay when all these connected notes matter together why do they matter

**[04:35]** notes matter together why do they matter

**[04:35]** notes matter together why do they matter matter all the notes relate to one

**[04:37]** matter all the notes relate to one

**[04:37]** matter all the notes relate to one another to ever inre um enriching wisdom

**[04:41]** another to ever inre um enriching wisdom

**[04:42]** another to ever inre um enriching wisdom storing system. Okay, this talk is about

**[04:44]** storing system. Okay, this talk is about

**[04:44]** storing system. Okay, this talk is about storing wisdom, right? So knowledge

**[04:46]** storing wisdom, right? So knowledge

**[04:46]** storing wisdom, right? So knowledge tells you what it is, right? And

**[04:51]** tells you what it is, right? And

**[04:51]** tells you what it is, right? And experience tell you what worked before.

**[04:54]** experience tell you what worked before.

**[04:54]** experience tell you what worked before. Insight invent what to try next, right?

**[04:58]** Insight invent what to try next, right?

**[04:58]** Insight invent what to try next, right? Like a pizza knowledge is recipe.


### [05:00 - 06:00]

**[05:01]** Like a pizza knowledge is recipe.

**[05:01]** Like a pizza knowledge is recipe. Experience is knowing your oven burn

**[05:04]** Experience is knowing your oven burn

**[05:04]** Experience is knowing your oven burn crust inside is like hey it is adding

**[05:09]** crust inside is like hey it is adding

**[05:09]** crust inside is like hey it is adding you know honey to the crust you make

**[05:10]** you know honey to the crust you make

**[05:10]** you know honey to the crust you make caramelize perfectly. Right? So the most

**[05:13]** caramelize perfectly. Right? So the most

**[05:13]** caramelize perfectly. Right? So the most important part of the knowledge graph is

**[05:15]** important part of the knowledge graph is

**[05:15]** important part of the knowledge graph is feedback loop. Okay, feedback isn't

**[05:17]** feedback loop. Okay, feedback isn't

**[05:17]** feedback loop. Okay, feedback isn't oneway street. It learn from itself.

**[05:19]** oneway street. It learn from itself.

**[05:20]** oneway street. It learn from itself. Look at the feedback from the uh going

**[05:22]** Look at the feedback from the uh going

**[05:22]** Look at the feedback from the uh going back to all the note from insight to

**[05:24]** back to all the note from insight to

**[05:24]** back to all the note from insight to wisdom. Okay. Um situation inform future

**[05:29]** wisdom. Okay. Um situation inform future

**[05:29]** wisdom. Okay. Um situation inform future wisdom. Experience deepen it insight

**[05:32]** wisdom. Experience deepen it insight

**[05:32]** wisdom. Experience deepen it insight sharpen it. Like a tree growing roots,

**[05:36]** sharpen it. Like a tree growing roots,

**[05:36]** sharpen it. Like a tree growing roots, the more effect the stronger it get. Now

**[05:38]** the more effect the stronger it get. Now

**[05:38]** the more effect the stronger it get. Now I want to ask you a question in general.

**[05:41]** I want to ask you a question in general.

**[05:41]** I want to ask you a question in general. Where do you see this circle in your

**[05:43]** Where do you see this circle in your

**[05:43]** Where do you see this circle in your life? Maybe a tough decision that you

**[05:46]** life? Maybe a tough decision that you

**[05:46]** life? Maybe a tough decision that you know taught you something.

**[05:49]** know taught you something.

**[05:49]** know taught you something. So one practical application for

**[05:51]** So one practical application for

**[05:52]** So one practical application for leadership is wisdom. Avoid knee jack

**[05:55]** leadership is wisdom. Avoid knee jack

**[05:55]** leadership is wisdom. Avoid knee jack reaction by learning from feedback. As

**[05:58]** reaction by learning from feedback. As

**[05:58]** reaction by learning from feedback. As for personal growth, ever notice how


### [06:00 - 07:00]

**[06:01]** for personal growth, ever notice how

**[06:01]** for personal growth, ever notice how past mistake make you wiser? That's the

**[06:03]** past mistake make you wiser? That's the

**[06:04]** past mistake make you wiser? That's the loop in the action. All this. So the

**[06:07]** loop in the action. All this. So the

**[06:07]** loop in the action. All this. So the take away from the slide in this is

**[06:09]** take away from the slide in this is

**[06:09]** take away from the slide in this is wisdom isn't a trophy you learn earn it

**[06:12]** wisdom isn't a trophy you learn earn it

**[06:12]** wisdom isn't a trophy you learn earn it is a muscle you exercise the more you

**[06:15]** is a muscle you exercise the more you

**[06:15]** is a muscle you exercise the more you feed knowledge experience inside the

**[06:18]** feed knowledge experience inside the

**[06:18]** feed knowledge experience inside the more that guide you now I will show you

**[06:21]** more that guide you now I will show you

**[06:21]** more that guide you now I will show you how it being mapped to my current client

**[06:25]** how it being mapped to my current client

**[06:25]** how it being mapped to my current client you know all this is like very abstract

**[06:27]** you know all this is like very abstract

**[06:27]** you know all this is like very abstract right so how I one of my clients

**[06:29]** right so how I one of my clients

**[06:29]** right so how I one of my clients actually doing a competitive analysis uh

**[06:32]** actually doing a competitive analysis uh

**[06:32]** actually doing a competitive analysis uh they used to have a marketing department

**[06:34]** they used to have a marketing department

**[06:34]** they used to have a marketing department doing that but they want AI to do Yeah,

**[06:36]** doing that but they want AI to do Yeah,

**[06:36]** doing that but they want AI to do Yeah, right. They they ask me to build the

**[06:37]** right. They they ask me to build the

**[06:38]** right. They they ask me to build the system. This is exactly what I did with

**[06:40]** system. This is exactly what I did with

**[06:40]** system. This is exactly what I did with the same taxonomy of storing all this.

**[06:43]** the same taxonomy of storing all this.

**[06:43]** the same taxonomy of storing all this. So this taxonomy will be later on I talk

**[06:45]** So this taxonomy will be later on I talk

**[06:45]** So this taxonomy will be later on I talk about how multi- aent is going to handle

**[06:47]** about how multi- aent is going to handle

**[06:47]** about how multi- aent is going to handle all that. Here is one of the chatbot

**[06:50]** all that. Here is one of the chatbot

**[06:50]** all that. Here is one of the chatbot that I build for my client to do you

**[06:52]** that I build for my client to do you

**[06:52]** that I build for my client to do you know not just some uh we not just some

**[06:56]** know not just some uh we not just some

**[06:56]** know not just some uh we not just some chatbot okay it's our wisdom graph power

**[06:58]** chatbot okay it's our wisdom graph power

**[06:58]** chatbot okay it's our wisdom graph power AI designed to turn data into strategy


### [07:00 - 08:00]

**[07:01]** AI designed to turn data into strategy

**[07:01]** AI designed to turn data into strategy right dominant. So what kind of question

**[07:03]** right dominant. So what kind of question

**[07:03]** right dominant. So what kind of question I talk about talk about how do I win my

**[07:05]** I talk about talk about how do I win my

**[07:05]** I talk about talk about how do I win my competitor in this market space that's

**[07:06]** competitor in this market space that's

**[07:06]** competitor in this market space that's kind of very sophisticated question

**[07:07]** kind of very sophisticated question

**[07:08]** kind of very sophisticated question right so without uh if you do simply

**[07:10]** right so without uh if you do simply

**[07:10]** right so without uh if you do simply just right by first speaker talk about

**[07:12]** just right by first speaker talk about

**[07:12]** just right by first speaker talk about right right so it's not going to cut it

**[07:14]** right right so it's not going to cut it

**[07:14]** right right so it's not going to cut it they're not going to able to answer that

**[07:16]** they're not going to able to answer that

**[07:16]** they're not going to able to answer that kind of question okay what I did is this

**[07:18]** kind of question okay what I did is this

**[07:18]** kind of question okay what I did is this uh we retain the same tonomy and uh the

**[07:21]** uh we retain the same tonomy and uh the

**[07:21]** uh we retain the same tonomy and uh the wisdom is then mapped the same engine

**[07:23]** wisdom is then mapped the same engine

**[07:23]** wisdom is then mapped the same engine here the wisdom engine wisdom engine is

**[07:24]** here the wisdom engine wisdom engine is

**[07:24]** here the wisdom engine wisdom engine is like a orchestration agent that does a

**[07:27]** like a orchestration agent that does a

**[07:27]** like a orchestration agent that does a lot of decision making including

**[07:28]** lot of decision making including

**[07:28]** lot of decision making including advising what the ARM is able to see bas

**[07:32]** advising what the ARM is able to see bas

**[07:32]** advising what the ARM is able to see bas on the current situation what to do next

**[07:34]** on the current situation what to do next

**[07:34]** on the current situation what to do next right so um what I did is uh for the uh

**[07:38]** right so um what I did is uh for the uh

**[07:38]** right so um what I did is uh for the uh decision making I map it to a strategy

**[07:40]** decision making I map it to a strategy

**[07:40]** decision making I map it to a strategy generator so these customers are talking

**[07:42]** generator so these customers are talking

**[07:42]** generator so these customers are talking about a competitive analysis right so um

**[07:44]** about a competitive analysis right so um

**[07:44]** about a competitive analysis right so um I map the knowledge in term of knowledge

**[07:47]** I map the knowledge in term of knowledge

**[07:47]** I map the knowledge in term of knowledge what do they have they have market data

**[07:49]** what do they have they have market data

**[07:49]** what do they have they have market data right so I map this experience to HP is

**[07:53]** right so I map this experience to HP is

**[07:53]** right so I map this experience to HP is one of a kind past campaign so they have

**[07:56]** one of a kind past campaign so they have

**[07:56]** one of a kind past campaign so they have a lot of campaign doing a lot of

**[07:58]** a lot of campaign doing a lot of

**[07:58]** a lot of campaign doing a lot of marketing and then um the insight is


### [08:00 - 09:00]

**[08:01]** marketing and then um the insight is

**[08:01]** marketing and then um the insight is actually mapped to uh in industrial

**[08:03]** actually mapped to uh in industrial

**[08:03]** actually mapped to uh in industrial insight they have a database doing

**[08:06]** insight they have a database doing

**[08:06]** insight they have a database doing storing that and then of course the most

**[08:08]** storing that and then of course the most

**[08:08]** storing that and then of course the most important is is the the situation the

**[08:11]** important is is the the situation the

**[08:11]** important is is the the situation the situation is how how am I doing how my

**[08:13]** situation is how how am I doing how my

**[08:13]** situation is how how am I doing how my product selling right so so that that is

**[08:16]** product selling right so so that that is

**[08:16]** product selling right so so that that is like a situation and then I map that to

**[08:18]** like a situation and then I map that to

**[08:18]** like a situation and then I map that to a competitor weakness that means they

**[08:20]** a competitor weakness that means they

**[08:20]** a competitor weakness that means they say if you make the aware of that you

**[08:25]** say if you make the aware of that you

**[08:25]** say if you make the aware of that you probably get a very good answer and then

**[08:27]** probably get a very good answer and then

**[08:27]** probably get a very good answer and then the chatbot will probably be doing the

**[08:29]** the chatbot will probably be doing the

**[08:29]** the chatbot will probably be doing the right thing advising so from here very

**[08:32]** right thing advising so from here very

**[08:32]** right thing advising so from here very high level you know state diagram or

**[08:34]** high level you know state diagram or

**[08:34]** high level you know state diagram or there how do I map it to a system that

**[08:37]** there how do I map it to a system that

**[08:37]** there how do I map it to a system that drive well here comes the trick so

**[08:39]** drive well here comes the trick so

**[08:40]** drive well here comes the trick so anybody here heard of n

**[08:43]** anybody here heard of n

**[08:43]** anybody here heard of n all right all right it's all good so so

**[08:45]** all right all right it's all good so so

**[08:45]** all right all right it's all good so so I I first encounter similar situation

**[08:47]** I I first encounter similar situation

**[08:47]** I I first encounter similar situation when my past IoT project which is not

**[08:50]** when my past IoT project which is not

**[08:50]** when my past IoT project which is not red developed by uh IBM right so it's

**[08:53]** red developed by uh IBM right so it's

**[08:53]** red developed by uh IBM right so it's the same kind of thing it's like no code

**[08:55]** the same kind of thing it's like no code

**[08:55]** the same kind of thing it's like no code but but underneath the hood there's a

**[08:57]** but but underneath the hood there's a

**[08:57]** but but underneath the hood there's a bunch of code okay it's all nodejs code

**[08:59]** bunch of code okay it's all nodejs code

**[08:59]** bunch of code okay it's all nodejs code okay so uh but but for the for for for


### [09:00 - 10:00]

**[09:01]** okay so uh but but for the for for for

**[09:01]** okay so uh but but for the for for for proving your concept and all that it's

**[09:03]** proving your concept and all that it's

**[09:03]** proving your concept and all that it's very very very flexible and I I highly

**[09:06]** very very very flexible and I I highly

**[09:06]** very very very flexible and I I highly recommend that and and and here here you

**[09:08]** recommend that and and and here here you

**[09:08]** recommend that and and and here here you can take a look at the the workflow the

**[09:10]** can take a look at the the workflow the

**[09:10]** can take a look at the the workflow the work from I enable the implementation of

**[09:12]** work from I enable the implementation of

**[09:12]** work from I enable the implementation of this complicated state diagram with um

**[09:15]** this complicated state diagram with um

**[09:15]** this complicated state diagram with um what I say is there is a different

**[09:17]** what I say is there is a different

**[09:17]** what I say is there is a different community note one of the very powerful

**[09:19]** community note one of the very powerful

**[09:19]** community note one of the very powerful node is AI agent well previously N is

**[09:22]** node is AI agent well previously N is

**[09:22]** node is AI agent well previously N is just a workflow automation tool I'm not

**[09:23]** just a workflow automation tool I'm not

**[09:23]** just a workflow automation tool I'm not selling for N here I'm just telling you

**[09:25]** selling for N here I'm just telling you

**[09:25]** selling for N here I'm just telling you I'm using it uh for pro prototyping

**[09:28]** I'm using it uh for pro prototyping

**[09:28]** I'm using it uh for pro prototyping further down the road maybe the client

**[09:30]** further down the road maybe the client

**[09:30]** further down the road maybe the client say too like I I really need to you know

**[09:33]** say too like I I really need to you know

**[09:33]** say too like I I really need to you know go lightweight maybe we will switch over

**[09:35]** go lightweight maybe we will switch over

**[09:35]** go lightweight maybe we will switch over to some other lang chain or whatever but

**[09:37]** to some other lang chain or whatever but

**[09:37]** to some other lang chain or whatever but uh we actually uses like I mapped the

**[09:40]** uh we actually uses like I mapped the

**[09:40]** uh we actually uses like I mapped the previous uh state diagram from the

**[09:42]** previous uh state diagram from the

**[09:42]** previous uh state diagram from the wisdom engine I actually map that to our

**[09:45]** wisdom engine I actually map that to our

**[09:45]** wisdom engine I actually map that to our uh wisdom agent okay wisdom agent is now

**[09:47]** uh wisdom agent okay wisdom agent is now

**[09:47]** uh wisdom agent okay wisdom agent is now have the option to drive uh different

**[09:50]** have the option to drive uh different

**[09:50]** have the option to drive uh different model like openai model entropic model

**[09:52]** model like openai model entropic model

**[09:52]** model like openai model entropic model and even onrem model and then that the

**[09:55]** and even onrem model and then that the

**[09:55]** and even onrem model and then that the key in making the state m the state

**[09:57]** key in making the state m the state

**[09:57]** key in making the state m the state machine work is that my wisdom agent is

**[09:59]** machine work is that my wisdom agent is


### [10:00 - 11:00]

**[10:00]** machine work is that my wisdom agent is now overseeing like a supervisory agent

**[10:02]** now overseeing like a supervisory agent

**[10:02]** now overseeing like a supervisory agent or all these other agent that do uh

**[10:05]** or all these other agent that do uh

**[10:05]** or all these other agent that do uh whatever I say on the state diagram like

**[10:07]** whatever I say on the state diagram like

**[10:07]** whatever I say on the state diagram like um for example the uh state of uh going

**[10:11]** um for example the uh state of uh going

**[10:11]** um for example the uh state of uh going into a note of insight inside agent will

**[10:14]** into a note of insight inside agent will

**[10:14]** into a note of insight inside agent will test to do go to the social media look

**[10:17]** test to do go to the social media look

**[10:17]** test to do go to the social media look for all the settlement of all your

**[10:19]** for all the settlement of all your

**[10:19]** for all the settlement of all your product and then collect that and then

**[10:21]** product and then collect that and then

**[10:21]** product and then collect that and then pump that you can see that at the dot

**[10:23]** pump that you can see that at the dot

**[10:23]** pump that you can see that at the dot bottom that we I connected to a

**[10:27]** bottom that we I connected to a

**[10:27]** bottom that we I connected to a a centralized uh graph left the central

**[10:30]** a centralized uh graph left the central

**[10:30]** a centralized uh graph left the central graph will be able to get updated by

**[10:33]** graph will be able to get updated by

**[10:33]** graph will be able to get updated by different agent uh inside agent will

**[10:35]** different agent uh inside agent will

**[10:35]** different agent uh inside agent will update the their perspective like part

**[10:38]** update the their perspective like part

**[10:38]** update the their perspective like part of that graph for the uh as I say for

**[10:40]** of that graph for the uh as I say for

**[10:40]** of that graph for the uh as I say for this particular uh inside note. So, so

**[10:44]** this particular uh inside note. So, so

**[10:44]** this particular uh inside note. So, so all the unified knowledge graph will

**[10:47]** all the unified knowledge graph will

**[10:47]** all the unified knowledge graph will contain the taxonomy that eventually

**[10:51]** contain the taxonomy that eventually

**[10:51]** contain the taxonomy that eventually just think like the marketing strategies

**[10:54]** just think like the marketing strategies

**[10:54]** just think like the marketing strategies the way that here they will probably if

**[10:56]** the way that here they will probably if

**[10:56]** the way that here they will probably if you are doing manually they probably

**[10:58]** you are doing manually they probably

**[10:58]** you are doing manually they probably would think in your shareepoint will all


### [11:00 - 12:00]

**[11:00]** would think in your shareepoint will all

**[11:00]** would think in your shareepoint will all this you know folder will store the same

**[11:02]** this you know folder will store the same

**[11:02]** this you know folder will store the same kind of uh you know wisdom I call it to

**[11:05]** kind of uh you know wisdom I call it to

**[11:05]** kind of uh you know wisdom I call it to make decision based on that. So the the

**[11:07]** make decision based on that. So the the

**[11:07]** make decision based on that. So the the final decision is LM also depend on the

**[11:10]** final decision is LM also depend on the

**[11:10]** final decision is LM also depend on the model that you use. Uh but I I I I

**[11:12]** model that you use. Uh but I I I I

**[11:12]** model that you use. Uh but I I I I pretty much think that not really the

**[11:15]** pretty much think that not really the

**[11:15]** pretty much think that not really the way that I think the final decision come

**[11:17]** way that I think the final decision come

**[11:17]** way that I think the final decision come when you make a right decision from the

**[11:19]** when you make a right decision from the

**[11:19]** when you make a right decision from the advisor output is basically depend on

**[11:21]** advisor output is basically depend on

**[11:21]** advisor output is basically depend on all the tonomy the graph structure

**[11:24]** all the tonomy the graph structure

**[11:24]** all the tonomy the graph structure that's very important. So come to that I

**[11:26]** that's very important. So come to that I

**[11:26]** that's very important. So come to that I I want to go deep down how I implement

**[11:28]** I want to go deep down how I implement

**[11:28]** I want to go deep down how I implement one of the node uh just to go a bit

**[11:31]** one of the node uh just to go a bit

**[11:31]** one of the node uh just to go a bit technical on this competitive node. How

**[11:33]** technical on this competitive node. How

**[11:33]** technical on this competitive node. How do I implement that? Okay, before I do

**[11:35]** do I implement that? Okay, before I do

**[11:35]** do I implement that? Okay, before I do that, okay, competitive analysis, right?

**[11:38]** that, okay, competitive analysis, right?

**[11:38]** that, okay, competitive analysis, right? Why why you can actually just use rag?

**[11:40]** Why why you can actually just use rag?

**[11:40]** Why why you can actually just use rag? Why do you want to use a knowledge graph

**[11:41]** Why do you want to use a knowledge graph

**[11:41]** Why do you want to use a knowledge graph like new forj? Well, if you ever being

**[11:44]** like new forj? Well, if you ever being

**[11:44]** like new forj? Well, if you ever being asked that question, tell them these

**[11:46]** asked that question, tell them these

**[11:46]** asked that question, tell them these five uh five reason. Okay, first reason

**[11:49]** five uh five reason. Okay, first reason

**[11:49]** five uh five reason. Okay, first reason is knowledge graph you know u system

**[11:52]** is knowledge graph you know u system

**[11:52]** is knowledge graph you know u system excel at capturing and representing

**[11:54]** excel at capturing and representing

**[11:54]** excel at capturing and representing complex relationship between entities

**[11:56]** complex relationship between entities

**[11:56]** complex relationship between entities that is covered by the first speaker but

**[11:58]** that is covered by the first speaker but

**[11:58]** that is covered by the first speaker but I'll just reiterate that this lead to a


### [12:00 - 13:00]

**[12:00]** I'll just reiterate that this lead to a

**[12:00]** I'll just reiterate that this lead to a deeper contextual understanding which is

**[12:02]** deeper contextual understanding which is

**[12:02]** deeper contextual understanding which is crucial for comparative analysis where

**[12:04]** crucial for comparative analysis where

**[12:04]** crucial for comparative analysis where this in this case the insight can be

**[12:07]** this in this case the insight can be

**[12:07]** this in this case the insight can be significant different okay you want to

**[12:10]** significant different okay you want to

**[12:10]** significant different okay you want to find the gap in your computer winners

**[12:12]** find the gap in your computer winners

**[12:12]** find the gap in your computer winners this is very important the second is

**[12:14]** this is very important the second is

**[12:14]** this is very important the second is improve accuracy by leveraging

**[12:16]** improve accuracy by leveraging

**[12:16]** improve accuracy by leveraging structured data and semantics

**[12:17]** structured data and semantics

**[12:17]** structured data and semantics relationship knowledge graph can provide

**[12:20]** relationship knowledge graph can provide

**[12:20]** relationship knowledge graph can provide more accurate and relevant information

**[12:22]** more accurate and relevant information

**[12:22]** more accurate and relevant information compared to traditional vector racks. Um

**[12:25]** compared to traditional vector racks. Um

**[12:25]** compared to traditional vector racks. Um this ensure generated content is not

**[12:27]** this ensure generated content is not

**[12:27]** this ensure generated content is not only relevant but also precise and

**[12:29]** only relevant but also precise and

**[12:29]** only relevant but also precise and reduce the noise and improve decision

**[12:31]** reduce the noise and improve decision

**[12:31]** reduce the noise and improve decision making making this in this case the

**[12:34]** making making this in this case the

**[12:34]** making making this in this case the board is supposed to help the guy that

**[12:35]** board is supposed to help the guy that

**[12:35]** board is supposed to help the guy that is marketing department make decisions.

**[12:37]** is marketing department make decisions.

**[12:37]** is marketing department make decisions. So, so you better make this work improve

**[12:39]** So, so you better make this work improve

**[12:39]** So, so you better make this work improve accuracy. Any inaccurate data, you will

**[12:42]** accuracy. Any inaccurate data, you will

**[12:42]** accuracy. Any inaccurate data, you will be out of the contract, out of the door,

**[12:43]** be out of the contract, out of the door,

**[12:43]** be out of the contract, out of the door, right? So, very important. Okay, you're

**[12:45]** right? So, very important. Okay, you're

**[12:45]** right? So, very important. Okay, you're talking about contract work like me, I

**[12:47]** talking about contract work like me, I

**[12:47]** talking about contract work like me, I have to make the rack as accurate as

**[12:49]** have to make the rack as accurate as

**[12:49]** have to make the rack as accurate as possible. So, the third is scalability

**[12:51]** possible. So, the third is scalability

**[12:51]** possible. So, the third is scalability and flexibility. There graphic you know

**[12:53]** and flexibility. There graphic you know

**[12:54]** and flexibility. There graphic you know graph are incredibly scalable and can

**[12:55]** graph are incredibly scalable and can

**[12:55]** graph are incredibly scalable and can integrate to new data source and

**[12:57]** integrate to new data source and

**[12:57]** integrate to new data source and relationship. The flexibility allow the

**[12:59]** relationship. The flexibility allow the

**[12:59]** relationship. The flexibility allow the continuous improvement. As I say, if


### [13:00 - 14:00]

**[13:01]** continuous improvement. As I say, if

**[13:01]** continuous improvement. As I say, if your taxonomy is correct, you will

**[13:03]** your taxonomy is correct, you will

**[13:03]** your taxonomy is correct, you will continues to improve and and reach,

**[13:05]** continues to improve and and reach,

**[13:05]** continues to improve and and reach, right? So, so that is important and also

**[13:07]** right? So, so that is important and also

**[13:07]** right? So, so that is important and also rich query capability. Knowledge craft

**[13:09]** rich query capability. Knowledge craft

**[13:09]** rich query capability. Knowledge craft support complex query traverse to

**[13:12]** support complex query traverse to

**[13:12]** support complex query traverse to multiple relationship entity provide

**[13:14]** multiple relationship entity provide

**[13:14]** multiple relationship entity provide richer and more detailed insight. This

**[13:16]** richer and more detailed insight. This

**[13:16]** richer and more detailed insight. This is particularly advantage for

**[13:17]** is particularly advantage for

**[13:17]** is particularly advantage for competitive analysis when multifacet

**[13:20]** competitive analysis when multifacet

**[13:20]** competitive analysis when multifacet query like like what the first speaker

**[13:21]** query like like what the first speaker

**[13:21]** query like like what the first speaker say it is super a notoriously good in

**[13:24]** say it is super a notoriously good in

**[13:24]** say it is super a notoriously good in answering things that normal rack will

**[13:28]** answering things that normal rack will

**[13:28]** answering things that normal rack will fail. It's like multihop question. Okay,

**[13:31]** fail. It's like multihop question. Okay,

**[13:31]** fail. It's like multihop question. Okay, this is very important. And then the

**[13:32]** this is very important. And then the

**[13:32]** this is very important. And then the final one is the enhanced data

**[13:34]** final one is the enhanced data

**[13:34]** final one is the enhanced data integration. Uh knowledge graph can

**[13:36]** integration. Uh knowledge graph can

**[13:36]** integration. Uh knowledge graph can seamlessly integrate diverse data source

**[13:39]** seamlessly integrate diverse data source

**[13:39]** seamlessly integrate diverse data source pictures, graphics, videos. Uh however

**[13:42]** pictures, graphics, videos. Uh however

**[13:42]** pictures, graphics, videos. Uh however it is now that LM is so powerful we have

**[13:45]** it is now that LM is so powerful we have

**[13:45]** it is now that LM is so powerful we have OCR capability can do that as long as

**[13:47]** OCR capability can do that as long as

**[13:47]** OCR capability can do that as long as you have a right structure of the graph

**[13:49]** you have a right structure of the graph

**[13:49]** you have a right structure of the graph semistructure unstructured the holistic

**[13:51]** semistructure unstructured the holistic

**[13:51]** semistructure unstructured the holistic approach ensure compressive view of the

**[13:53]** approach ensure compressive view of the

**[13:53]** approach ensure compressive view of the competitive landscape enable more

**[13:55]** competitive landscape enable more

**[13:55]** competitive landscape enable more informed strategic decision making.

**[13:58]** informed strategic decision making.

**[13:58]** informed strategic decision making. Okay. So one of the this is I'm going to


### [14:00 - 15:00]

**[14:00]** Okay. So one of the this is I'm going to

**[14:00]** Okay. So one of the this is I'm going to just very briefly go through this just a

**[14:03]** just very briefly go through this just a

**[14:03]** just very briefly go through this just a uh example of that some of the thing

**[14:05]** uh example of that some of the thing

**[14:05]** uh example of that some of the thing like um problem of a vectors rack you

**[14:07]** like um problem of a vectors rack you

**[14:07]** like um problem of a vectors rack you know vector rack is really really bad in

**[14:09]** know vector rack is really really bad in

**[14:09]** know vector rack is really really bad in answering limited numerical resing

**[14:12]** answering limited numerical resing

**[14:12]** answering limited numerical resing vector store excel you know at sematic

**[14:15]** vector store excel you know at sematic

**[14:15]** vector store excel you know at sematic sim similarity but struggle with complex

**[14:18]** sim similarity but struggle with complex

**[14:18]** sim similarity but struggle with complex numerical calculation this is why uh for

**[14:20]** numerical calculation this is why uh for

**[14:20]** numerical calculation this is why uh for marketing analysis uh that I'm building

**[14:23]** marketing analysis uh that I'm building

**[14:23]** marketing analysis uh that I'm building the chatbot for uh they actually rely on

**[14:26]** the chatbot for uh they actually rely on

**[14:26]** the chatbot for uh they actually rely on number instead of just you know

**[14:28]** number instead of just you know

**[14:28]** number instead of just you know returning

**[14:29]** returning

**[14:29]** returning example like this kind of if you ask

**[14:31]** example like this kind of if you ask

**[14:31]** example like this kind of if you ask like what is the Apple uh revenue uh

**[14:34]** like what is the Apple uh revenue uh

**[14:34]** like what is the Apple uh revenue uh between uh two uh you know what's the

**[14:37]** between uh two uh you know what's the

**[14:37]** between uh two uh you know what's the revenue in 2022 they probably will give

**[14:39]** revenue in 2022 they probably will give

**[14:39]** revenue in 2022 they probably will give you a bunch of this kind of a passage

**[14:41]** you a bunch of this kind of a passage

**[14:41]** you a bunch of this kind of a passage right retrieve a graph instead of uh

**[14:44]** right retrieve a graph instead of uh

**[14:44]** right retrieve a graph instead of uh this kind of a very very precise thing

**[14:46]** this kind of a very very precise thing

**[14:46]** this kind of a very very precise thing like uh the answer is uh you know uh got

**[14:50]** like uh the answer is uh you know uh got

**[14:50]** like uh the answer is uh you know uh got knowledge cross able because the the

**[14:52]** knowledge cross able because the the

**[14:52]** knowledge cross able because the the data is already there in structure form

**[14:54]** data is already there in structure form

**[14:54]** data is already there in structure form the data source assume a knowledge gra

**[14:56]** the data source assume a knowledge gra

**[14:56]** the data source assume a knowledge gra name this particular in this particular

**[14:58]** name this particular in this particular

**[14:58]** name this particular in this particular case Apple financial data the query will


### [15:00 - 16:00]

**[15:01]** case Apple financial data the query will

**[15:01]** case Apple financial data the query will be able the query engine will be able to

**[15:03]** be able the query engine will be able to

**[15:03]** be able the query engine will be able to select the the revenue figure from 2021

**[15:05]** select the the revenue figure from 2021

**[15:05]** select the the revenue figure from 2021 to 2022 and and then do a function call

**[15:09]** to 2022 and and then do a function call

**[15:09]** to 2022 and and then do a function call the function call will eventually give

**[15:10]** the function call will eventually give

**[15:10]** the function call will eventually give come out with 15.23 23 which is exactly

**[15:13]** come out with 15.23 23 which is exactly

**[15:13]** come out with 15.23 23 which is exactly what the marketing guy was looking for a

**[15:15]** what the marketing guy was looking for a

**[15:16]** what the marketing guy was looking for a very quantitative stuff that most of the

**[15:18]** very quantitative stuff that most of the

**[15:18]** very quantitative stuff that most of the decision were based on that because you

**[15:19]** decision were based on that because you

**[15:19]** decision were based on that because you have the evidence not just some passage

**[15:21]** have the evidence not just some passage

**[15:21]** have the evidence not just some passage that you retrieve from the data it's

**[15:23]** that you retrieve from the data it's

**[15:23]** that you retrieve from the data it's basically evidence based decision making

**[15:26]** basically evidence based decision making

**[15:26]** basically evidence based decision making is very important for this kind of uh

**[15:27]** is very important for this kind of uh

**[15:28]** is very important for this kind of uh complicated rack system that you know so

**[15:31]** complicated rack system that you know so

**[15:31]** complicated rack system that you know so um there's a jungle out there right now

**[15:33]** um there's a jungle out there right now

**[15:33]** um there's a jungle out there right now you can use different kind of a uh uh uh

**[15:36]** you can use different kind of a uh uh uh

**[15:36]** you can use different kind of a uh uh uh thing to build your uh you know uh this

**[15:39]** thing to build your uh you know uh this

**[15:39]** thing to build your uh you know uh this is just a snapshot of that you know you

**[15:40]** is just a snapshot of that you know you

**[15:40]** is just a snapshot of that you know you can actually use lang chain plus chroma

**[15:43]** can actually use lang chain plus chroma

**[15:43]** can actually use lang chain plus chroma to to build your own rack and then you

**[15:45]** to to build your own rack and then you

**[15:45]** to to build your own rack and then you also can combine that with your

**[15:47]** also can combine that with your

**[15:47]** also can combine that with your knowledge graph depend on on on your

**[15:49]** knowledge graph depend on on on your

**[15:49]** knowledge graph depend on on on your user case. Okay, if if this this slide

**[15:52]** user case. Okay, if if this this slide

**[15:52]** user case. Okay, if if this this slide show that the rack and the k a can be bu

**[15:54]** show that the rack and the k a can be bu

**[15:54]** show that the rack and the k a can be bu with money. Okay, I adopt that wisdom

**[15:57]** with money. Okay, I adopt that wisdom

**[15:57]** with money. Okay, I adopt that wisdom graph in red color. Normally you will

**[15:59]** graph in red color. Normally you will

**[15:59]** graph in red color. Normally you will see if client is just asking for a


### [16:00 - 17:00]

**[16:02]** see if client is just asking for a

**[16:02]** see if client is just asking for a simple rack that perform product

**[16:04]** simple rack that perform product

**[16:04]** simple rack that perform product information query, you can just use a

**[16:07]** information query, you can just use a

**[16:07]** information query, you can just use a simple chroma DB with LM agent. And if

**[16:09]** simple chroma DB with LM agent. And if

**[16:10]** simple chroma DB with LM agent. And if you start to ask so complicated

**[16:11]** you start to ask so complicated

**[16:11]** you start to ask so complicated questions like how can I beat my

**[16:13]** questions like how can I beat my

**[16:13]** questions like how can I beat my competition based on my current market

**[16:15]** competition based on my current market

**[16:15]** competition based on my current market share. Well, this will be able the the

**[16:18]** share. Well, this will be able the the

**[16:18]** share. Well, this will be able the the the the thing that I will probably be

**[16:20]** the the thing that I will probably be

**[16:20]** the the thing that I will probably be adopting is knowledge graph here with uh

**[16:23]** adopting is knowledge graph here with uh

**[16:23]** adopting is knowledge graph here with uh graph DB plus cipher query and then qua

**[16:26]** graph DB plus cipher query and then qua

**[16:26]** graph DB plus cipher query and then qua and also train my rack to perform

**[16:28]** and also train my rack to perform

**[16:28]** and also train my rack to perform several loop of uh we call multihop

**[16:31]** several loop of uh we call multihop

**[16:31]** several loop of uh we call multihop query and this probably will give you a

**[16:33]** query and this probably will give you a

**[16:33]** query and this probably will give you a very good answer.

**[16:35]** very good answer.

**[16:35]** very good answer. So uh and then it come to the another

**[16:37]** So uh and then it come to the another

**[16:37]** So uh and then it come to the another question when I was trying to extract my

**[16:41]** question when I was trying to extract my

**[16:41]** question when I was trying to extract my uh oh I think my time is uh is almost

**[16:43]** uh oh I think my time is uh is almost

**[16:43]** uh oh I think my time is uh is almost up. Okay. So anyway this is like to say

**[16:46]** up. Okay. So anyway this is like to say

**[16:46]** up. Okay. So anyway this is like to say uh the first speaker talk about the

**[16:48]** uh the first speaker talk about the

**[16:48]** uh the first speaker talk about the extraction right there's a very simple

**[16:50]** extraction right there's a very simple

**[16:50]** extraction right there's a very simple way to extract on the right side is like

**[16:51]** way to extract on the right side is like

**[16:51]** way to extract on the right side is like automated totally automated LM graph

**[16:54]** automated totally automated LM graph

**[16:54]** automated totally automated LM graph transformer on the left is like manual I

**[16:57]** transformer on the left is like manual I

**[16:57]** transformer on the left is like manual I would probably re recommend to send the

**[16:58]** would probably re recommend to send the

**[16:58]** would probably re recommend to send the hybrid model which is like after you use


### [17:00 - 18:00]

**[17:00]** hybrid model which is like after you use

**[17:00]** hybrid model which is like after you use the LM to extract your graph you ask the

**[17:03]** the LM to extract your graph you ask the

**[17:03]** the LM to extract your graph you ask the interview the the expert that you're

**[17:04]** interview the the expert that you're

**[17:04]** interview the the expert that you're going to build uh to to build your

**[17:06]** going to build uh to to build your

**[17:06]** going to build uh to to build your taxonomy right to prone the graph we

**[17:09]** taxonomy right to prone the graph we

**[17:09]** taxonomy right to prone the graph we call it proning your graph remove a lot

**[17:10]** call it proning your graph remove a lot

**[17:10]** call it proning your graph remove a lot of relationship that then that that will

**[17:12]** of relationship that then that that will

**[17:12]** of relationship that then that that will be okay and um I will try to just

**[17:14]** be okay and um I will try to just

**[17:14]** be okay and um I will try to just highlight like this this is the result

**[17:16]** highlight like this this is the result

**[17:16]** highlight like this this is the result of benchmark that we did okay anybody

**[17:18]** of benchmark that we did okay anybody

**[17:18]** of benchmark that we did okay anybody ask you you know why you want to use

**[17:20]** ask you you know why you want to use

**[17:20]** ask you you know why you want to use graph right or k a okay first is

**[17:22]** graph right or k a okay first is

**[17:22]** graph right or k a okay first is accuracy I had achieved 91% because it's

**[17:25]** accuracy I had achieved 91% because it's

**[17:25]** accuracy I had achieved 91% because it's really good in extract structure second

**[17:26]** really good in extract structure second

**[17:26]** really good in extract structure second is flexibility 85% third is repubity

**[17:30]** is flexibility 85% third is repubity

**[17:30]** is flexibility 85% third is repubity reproducibility deterministic and then

**[17:33]** reproducibility deterministic and then

**[17:33]** reproducibility deterministic and then the fourth one traceability and finally

**[17:36]** the fourth one traceability and finally

**[17:36]** the fourth one traceability and finally uh most important is scalability so in

**[17:39]** uh most important is scalability so in

**[17:39]** uh most important is scalability so in conclusion

**[17:41]** conclusion

**[17:41]** conclusion by leveraging structure nature of

**[17:43]** by leveraging structure nature of

**[17:43]** by leveraging structure nature of western knowledge We can significantly

**[17:45]** western knowledge We can significantly

**[17:45]** western knowledge We can significantly enhance the quantitative capability of K

**[17:47]** enhance the quantitative capability of K

**[17:47]** enhance the quantitative capability of K a system and a more accurate and

**[17:50]** a system and a more accurate and

**[17:50]** a system and a more accurate and insightful respond to complex query by

**[17:53]** insightful respond to complex query by

**[17:53]** insightful respond to complex query by using wisdom-driven system as

**[17:54]** using wisdom-driven system as

**[17:54]** using wisdom-driven system as highlighted. Together we can build

**[17:56]** highlighted. Together we can build

**[17:56]** highlighted. Together we can build smarter AI system that can scale and

**[17:58]** smarter AI system that can scale and

**[17:58]** smarter AI system that can scale and store wisdom with the right framing


### [18:00 - 19:00]

**[18:00]** store wisdom with the right framing

**[18:00]** store wisdom with the right framing potentially surpass the intelligent of

**[18:03]** potentially surpass the intelligent of

**[18:03]** potentially surpass the intelligent of the initial expert that we meant to

**[18:05]** the initial expert that we meant to

**[18:05]** the initial expert that we meant to serve. So uh talk to Jesus. You know

**[18:09]** serve. So uh talk to Jesus. You know

**[18:09]** serve. So uh talk to Jesus. You know what do they just do? Talk to Jesus.

**[18:11]** what do they just do? Talk to Jesus.

**[18:11]** what do they just do? Talk to Jesus. He's in our in in a not booth. this my

**[18:14]** He's in our in in a not booth. this my

**[18:14]** He's in our in in a not booth. this my good friend and uh anybody that want to

**[18:16]** good friend and uh anybody that want to

**[18:16]** good friend and uh anybody that want to build graph we have a good uh so-called

**[18:19]** build graph we have a good uh so-called

**[18:19]** build graph we have a good uh so-called LLM graph rack stack on GitHub that is

**[18:23]** LLM graph rack stack on GitHub that is

**[18:23]** LLM graph rack stack on GitHub that is sponsored by new forj and out of the box

**[18:25]** sponsored by new forj and out of the box

**[18:25]** sponsored by new forj and out of the box just spin up your docker the next thing

**[18:28]** just spin up your docker the next thing

**[18:28]** just spin up your docker the next thing you know your text is going to be

**[18:29]** you know your text is going to be

**[18:29]** you know your text is going to be converted to your graph and you can

**[18:31]** converted to your graph and you can

**[18:31]** converted to your graph and you can start happy pruning your graph thank you

**[18:33]** start happy pruning your graph thank you

**[18:33]** start happy pruning your graph thank you thank you so

**[18:34]** thank you so

**[18:34]** thank you so [Applause]

**[18:37]** [Applause]

**[18:37]** [Applause] [Music]


