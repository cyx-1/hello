# Context Engineering- Connecting the Dots with Graphs — Stephen Chin, Neo4j

**Video URL:** https://www.youtube.com/watch?v=LLuKshphGOE

---

## Full Transcript

### [00:00 - 01:00]

**[00:03]** Hello everybody and welcome to my

**[00:03]** Hello everybody and welcome to my session at a engineer code summit and

**[00:06]** session at a engineer code summit and

**[00:06]** session at a engineer code summit and I'm going to talk a bit about how you

**[00:08]** I'm going to talk a bit about how you

**[00:08]** I'm going to talk a bit about how you can connect the dots with graph

**[00:10]** can connect the dots with graph

**[00:10]** can connect the dots with graph technology and solve problems like

**[00:12]** technology and solve problems like

**[00:12]** technology and solve problems like context engineering um improving

**[00:15]** context engineering um improving

**[00:15]** context engineering um improving retrieval patterns and also agentic

**[00:17]** retrieval patterns and also agentic

**[00:17]** retrieval patterns and also agentic memory. So we're going to have a lot of

**[00:18]** memory. So we're going to have a lot of

**[00:18]** memory. So we're going to have a lot of fun. My name is Stephen Chin. I'm VP of

**[00:20]** fun. My name is Stephen Chin. I'm VP of

**[00:20]** fun. My name is Stephen Chin. I'm VP of developer relations at Neo Forj and you

**[00:23]** developer relations at Neo Forj and you

**[00:23]** developer relations at Neo Forj and you can find me at all the different social

**[00:24]** can find me at all the different social

**[00:24]** can find me at all the different social media outlets with my handle Steve on

**[00:26]** media outlets with my handle Steve on

**[00:26]** media outlets with my handle Steve on Java. So excited you're all here to join

**[00:29]** Java. So excited you're all here to join

**[00:29]** Java. So excited you're all here to join for the session today. And I think this

**[00:32]** for the session today. And I think this

**[00:32]** for the session today. And I think this is how a lot of us have felt the past

**[00:35]** is how a lot of us have felt the past

**[00:35]** is how a lot of us have felt the past couple years as AI technology has

**[00:38]** couple years as AI technology has

**[00:38]** couple years as AI technology has basically taken our jobs away. We've

**[00:40]** basically taken our jobs away. We've

**[00:40]** basically taken our jobs away. We've become slaves to um AI programming, to

**[00:43]** become slaves to um AI programming, to

**[00:43]** become slaves to um AI programming, to prompt development, to building things

**[00:45]** prompt development, to building things

**[00:45]** prompt development, to building things off AI models. Now, it's not all bad. I

**[00:48]** off AI models. Now, it's not all bad. I

**[00:48]** off AI models. Now, it's not all bad. I mean, we we have a lot more time to to

**[00:50]** mean, we we have a lot more time to to

**[00:50]** mean, we we have a lot more time to to play games, to hang out in the matrix,

**[00:52]** play games, to hang out in the matrix,

**[00:52]** play games, to hang out in the matrix, but what we really want to be doing is

**[00:54]** but what we really want to be doing is

**[00:54]** but what we really want to be doing is we want to be doing things which are

**[00:55]** we want to be doing things which are

**[00:55]** we want to be doing things which are higher value. So this is where context

**[00:58]** higher value. So this is where context

**[00:58]** higher value. So this is where context engineering comes in the picture and


### [01:00 - 02:00]

**[01:00]** engineering comes in the picture and

**[01:00]** engineering comes in the picture and transforms what we've traditionally been

**[01:02]** transforms what we've traditionally been

**[01:02]** transforms what we've traditionally been doing with kind of oneshot clever

**[01:05]** doing with kind of oneshot clever

**[01:05]** doing with kind of oneshot clever phrasing prompt engineering to get

**[01:07]** phrasing prompt engineering to get

**[01:07]** phrasing prompt engineering to get different results out of the AI and

**[01:09]** different results out of the AI and

**[01:09]** different results out of the AI and we're evolving that to have a more

**[01:11]** we're evolving that to have a more

**[01:11]** we're evolving that to have a more dynamic and and wider scope of things

**[01:14]** dynamic and and wider scope of things

**[01:14]** dynamic and and wider scope of things which we're feeding the AI as context

**[01:17]** which we're feeding the AI as context

**[01:17]** which we're feeding the AI as context which gives us much better results. So

**[01:19]** which gives us much better results. So

**[01:19]** which gives us much better results. So um this allows us to feed the desire of

**[01:23]** um this allows us to feed the desire of

**[01:23]** um this allows us to feed the desire of agents to get even more context and

**[01:25]** agents to get even more context and

**[01:25]** agents to get even more context and information to do things together. Um to

**[01:28]** information to do things together. Um to

**[01:28]** information to do things together. Um to have more dynamic models and

**[01:30]** have more dynamic models and

**[01:30]** have more dynamic models and applications to make our applications

**[01:32]** applications to make our applications

**[01:32]** applications to make our applications goal driven. Um selectively curate the

**[01:34]** goal driven. Um selectively curate the

**[01:34]** goal driven. Um selectively curate the information for the relevancy of the

**[01:37]** information for the relevancy of the

**[01:37]** information for the relevancy of the particular domain which we're working

**[01:38]** particular domain which we're working

**[01:38]** particular domain which we're working in. So if you're working in a um an

**[01:41]** in. So if you're working in a um an

**[01:41]** in. So if you're working in a um an enterprise domain, if you're working

**[01:42]** enterprise domain, if you're working

**[01:42]** enterprise domain, if you're working with a lot of business context, this is

**[01:44]** with a lot of business context, this is

**[01:44]** with a lot of business context, this is particularly important. And then we can

**[01:46]** particularly important. And then we can

**[01:46]** particularly important. And then we can structure the input and get a lot more

**[01:48]** structure the input and get a lot more

**[01:48]** structure the input and get a lot more signal over all the noise of what's

**[01:50]** signal over all the noise of what's

**[01:50]** signal over all the noise of what's being entered into the model which is

**[01:51]** being entered into the model which is

**[01:51]** being entered into the model which is one of the biggest problems with models

**[01:52]** one of the biggest problems with models

**[01:52]** one of the biggest problems with models today. Um huge context windows but very

**[01:56]** today. Um huge context windows but very

**[01:56]** today. Um huge context windows but very little attention focus and simply not

**[01:58]** little attention focus and simply not

**[01:58]** little attention focus and simply not looking at the right parts of the

**[01:59]** looking at the right parts of the

**[01:59]** looking at the right parts of the context to give us good results. And


### [02:00 - 03:00]

**[02:02]** context to give us good results. And

**[02:02]** context to give us good results. And this allows us to think not like prompt

**[02:04]** this allows us to think not like prompt

**[02:04]** this allows us to think not like prompt engineers but like information

**[02:06]** engineers but like information

**[02:06]** engineers but like information architects where we're building the

**[02:09]** architects where we're building the

**[02:09]** architects where we're building the model context which actually gives us

**[02:11]** model context which actually gives us

**[02:11]** model context which actually gives us superior results coming out of the AI.

**[02:14]** superior results coming out of the AI.

**[02:14]** superior results coming out of the AI. And this evolves us from being um you

**[02:17]** And this evolves us from being um you

**[02:17]** And this evolves us from being um you know your traditional trapped to matrix

**[02:19]** know your traditional trapped to matrix

**[02:19]** know your traditional trapped to matrix worker to being superheroes. So this is

**[02:22]** worker to being superheroes. So this is

**[02:22]** worker to being superheroes. So this is this is where we want to be. We want to

**[02:23]** this is where we want to be. We want to

**[02:23]** this is where we want to be. We want to be in control of our destiny. We want to

**[02:26]** be in control of our destiny. We want to

**[02:26]** be in control of our destiny. We want to be able to give the agents all of the

**[02:28]** be able to give the agents all of the

**[02:28]** be able to give the agents all of the information all the context which they

**[02:30]** information all the context which they

**[02:30]** information all the context which they need to perform the task and to do

**[02:31]** need to perform the task and to do

**[02:31]** need to perform the task and to do exactly what we want to get for results

**[02:33]** exactly what we want to get for results

**[02:33]** exactly what we want to get for results out of it. And there's a lot of tools at

**[02:35]** out of it. And there's a lot of tools at

**[02:35]** out of it. And there's a lot of tools at our disposal now which allow us to

**[02:37]** our disposal now which allow us to

**[02:37]** our disposal now which allow us to manipulate, control the context and

**[02:39]** manipulate, control the context and

**[02:39]** manipulate, control the context and really um feed the AIS all the

**[02:41]** really um feed the AIS all the

**[02:41]** really um feed the AIS all the information which they need to be

**[02:43]** information which they need to be

**[02:43]** information which they need to be successful. So in the kind of the scope

**[02:46]** successful. So in the kind of the scope

**[02:46]** successful. So in the kind of the scope of context engineering

**[02:48]** of context engineering

**[02:48]** of context engineering there's a whole bunch of things which

**[02:50]** there's a whole bunch of things which

**[02:50]** there's a whole bunch of things which are clearly um part of the domain that

**[02:53]** are clearly um part of the domain that

**[02:53]** are clearly um part of the domain that this now encompasses. So one is prompt

**[02:56]** this now encompasses. So one is prompt

**[02:56]** this now encompasses. So one is prompt engineering. Of course, we need to

**[02:58]** engineering. Of course, we need to

**[02:58]** engineering. Of course, we need to design engineer good good prompts. Um,


### [03:00 - 04:00]

**[03:01]** design engineer good good prompts. Um,

**[03:01]** design engineer good good prompts. Um, make sure that the AI actually has the

**[03:02]** make sure that the AI actually has the

**[03:02]** make sure that the AI actually has the right instructions, the right

**[03:04]** right instructions, the right

**[03:04]** right instructions, the right information and the right grounding

**[03:05]** information and the right grounding

**[03:05]** information and the right grounding which it needs to do its job well. But

**[03:08]** which it needs to do its job well. But

**[03:08]** which it needs to do its job well. But we also need to pull in from different

**[03:09]** we also need to pull in from different

**[03:09]** we also need to pull in from different data sources by using things like

**[03:11]** data sources by using things like

**[03:11]** data sources by using things like retrieval, augmented generation. So um

**[03:14]** retrieval, augmented generation. So um

**[03:14]** retrieval, augmented generation. So um rag is still very relevant for the

**[03:16]** rag is still very relevant for the

**[03:16]** rag is still very relevant for the ability to pull in data from enterprise

**[03:19]** ability to pull in data from enterprise

**[03:19]** ability to pull in data from enterprise context from different business contexts

**[03:21]** context from different business contexts

**[03:21]** context from different business contexts and then supply that as additional

**[03:24]** and then supply that as additional

**[03:24]** and then supply that as additional information to the AI that it can use to

**[03:25]** information to the AI that it can use to

**[03:26]** information to the AI that it can use to make decisions. Um pulling in state and

**[03:28]** make decisions. Um pulling in state and

**[03:28]** make decisions. Um pulling in state and history as well. So now we actually want

**[03:31]** history as well. So now we actually want

**[03:31]** history as well. So now we actually want our models want memory um both

**[03:34]** our models want memory um both

**[03:34]** our models want memory um both short-term memory so they can

**[03:35]** short-term memory so they can

**[03:35]** short-term memory so they can collaborate with each other and also

**[03:37]** collaborate with each other and also

**[03:37]** collaborate with each other and also long-term memory so they remember the

**[03:39]** long-term memory so they remember the

**[03:39]** long-term memory so they remember the conversation state the history and um

**[03:41]** conversation state the history and um

**[03:41]** conversation state the history and um they can do more effective long-term

**[03:43]** they can do more effective long-term

**[03:43]** they can do more effective long-term operations

**[03:45]** operations

**[03:45]** operations and we also want to be able to structure

**[03:47]** and we also want to be able to structure

**[03:47]** and we also want to be able to structure the output in a meaningful way so we can

**[03:49]** the output in a meaningful way so we can

**[03:49]** the output in a meaningful way so we can actually feed into not only other

**[03:52]** actually feed into not only other

**[03:52]** actually feed into not only other applications but other tools and things

**[03:54]** applications but other tools and things

**[03:54]** applications but other tools and things which we need to collaborate with and

**[03:56]** which we need to collaborate with and

**[03:56]** which we need to collaborate with and integrate our um context with. And when

**[03:58]** integrate our um context with. And when

**[03:58]** integrate our um context with. And when you put this all together, this is kind


### [04:00 - 05:00]

**[04:00]** you put this all together, this is kind

**[04:00]** you put this all together, this is kind of the the scope and domain of context

**[04:03]** of the the scope and domain of context

**[04:03]** of the the scope and domain of context engineering. Now, one of the big focuses

**[04:06]** engineering. Now, one of the big focuses

**[04:06]** engineering. Now, one of the big focuses of this is all about memory. So, it's

**[04:08]** of this is all about memory. So, it's

**[04:08]** of this is all about memory. So, it's all about how we capture the AI memory

**[04:11]** all about how we capture the AI memory

**[04:11]** all about how we capture the AI memory and what we're able to do with it. So,

**[04:13]** and what we're able to do with it. So,

**[04:13]** and what we're able to do with it. So, um there's kind of two main

**[04:15]** um there's kind of two main

**[04:15]** um there's kind of two main categorizations of memory. One is

**[04:17]** categorizations of memory. One is

**[04:17]** categorizations of memory. One is short-term memory. So, this is what the

**[04:19]** short-term memory. So, this is what the

**[04:19]** short-term memory. So, this is what the AI is currently working with on the

**[04:21]** AI is currently working with on the

**[04:21]** AI is currently working with on the current tasks. Um, we want to compress

**[04:24]** current tasks. Um, we want to compress

**[04:24]** current tasks. Um, we want to compress as much information as possible into the

**[04:26]** as much information as possible into the

**[04:26]** as much information as possible into the short-term memory and give it relevant

**[04:28]** short-term memory and give it relevant

**[04:28]** short-term memory and give it relevant results which are high up in the search

**[04:29]** results which are high up in the search

**[04:29]** results which are high up in the search window. Um, be able to integrate tool

**[04:31]** window. Um, be able to integrate tool

**[04:32]** window. Um, be able to integrate tool results into this as well, although you

**[04:34]** results into this as well, although you

**[04:34]** results into this as well, although you know not give it too much information

**[04:36]** know not give it too much information

**[04:36]** know not give it too much information from tools, especially from previous

**[04:37]** from tools, especially from previous

**[04:38]** from tools, especially from previous exchanges where the tools might have

**[04:39]** exchanges where the tools might have

**[04:39]** exchanges where the tools might have dumped a lot of output or information

**[04:41]** dumped a lot of output or information

**[04:41]** dumped a lot of output or information which will fill our context window. Um,

**[04:43]** which will fill our context window. Um,

**[04:43]** which will fill our context window. Um, and in addition to this, we also need to

**[04:45]** and in addition to this, we also need to

**[04:45]** and in addition to this, we also need to mix in long-term memory. So things which

**[04:48]** mix in long-term memory. So things which

**[04:48]** mix in long-term memory. So things which you've learned over a long set of

**[04:50]** you've learned over a long set of

**[04:50]** you've learned over a long set of conversations which might be episodic.

**[04:53]** conversations which might be episodic.

**[04:53]** conversations which might be episodic. Um we need to figure out the semantic

**[04:55]** Um we need to figure out the semantic

**[04:55]** Um we need to figure out the semantic and the structural meaning of past

**[04:57]** and the structural meaning of past

**[04:57]** and the structural meaning of past conversations. Um kind of pull this out


### [05:00 - 06:00]

**[05:00]** conversations. Um kind of pull this out

**[05:00]** conversations. Um kind of pull this out into things which can either be used as

**[05:02]** into things which can either be used as

**[05:02]** into things which can either be used as instructions for the AI and also for

**[05:05]** instructions for the AI and also for

**[05:05]** instructions for the AI and also for procedures and operations which we can

**[05:07]** procedures and operations which we can

**[05:08]** procedures and operations which we can use to to guide and plan the artificial

**[05:10]** use to to guide and plan the artificial

**[05:10]** use to to guide and plan the artificial intelligence. And um when we put this

**[05:13]** intelligence. And um when we put this

**[05:13]** intelligence. And um when we put this together, this helps us pull the more

**[05:16]** together, this helps us pull the more

**[05:16]** together, this helps us pull the more relevant context higher up into the

**[05:18]** relevant context higher up into the

**[05:18]** relevant context higher up into the context window, fill in the gaps, and

**[05:21]** context window, fill in the gaps, and

**[05:21]** context window, fill in the gaps, and then avoid a lot of the noise, which

**[05:22]** then avoid a lot of the noise, which

**[05:22]** then avoid a lot of the noise, which gives us bad results or um

**[05:24]** gives us bad results or um

**[05:24]** gives us bad results or um hallucinations or other problems coming

**[05:26]** hallucinations or other problems coming

**[05:26]** hallucinations or other problems coming from our AI applications.

**[05:30]** from our AI applications.

**[05:30]** from our AI applications. And um memory is really the core of what

**[05:33]** And um memory is really the core of what

**[05:33]** And um memory is really the core of what we need to accomplish. um you know if

**[05:35]** we need to accomplish. um you know if

**[05:35]** we need to accomplish. um you know if you're plugging yourself up to the

**[05:36]** you're plugging yourself up to the

**[05:36]** you're plugging yourself up to the matrix this is where you si synergize

**[05:39]** matrix this is where you si synergize

**[05:39]** matrix this is where you si synergize all of your memories all the things

**[05:41]** all of your memories all the things

**[05:41]** all of your memories all the things which you want to get into the AI

**[05:43]** which you want to get into the AI

**[05:44]** which you want to get into the AI together with um your own own bind your

**[05:46]** together with um your own own bind your

**[05:46]** together with um your own own bind your own neural network that you want to um

**[05:49]** own neural network that you want to um

**[05:49]** own neural network that you want to um express and it's extremely important

**[05:51]** express and it's extremely important

**[05:51]** express and it's extremely important right now because LMS are only as good

**[05:53]** right now because LMS are only as good

**[05:53]** right now because LMS are only as good as the quality of the response that

**[05:55]** as the quality of the response that

**[05:55]** as the quality of the response that they're getting from the data. So if you

**[05:56]** they're getting from the data. So if you

**[05:56]** they're getting from the data. So if you give them bad data if you get them

**[05:58]** give them bad data if you get them

**[05:58]** give them bad data if you get them garbage then you are going to get


### [06:00 - 07:00]

**[06:00]** garbage then you are going to get

**[06:00]** garbage then you are going to get garbage back out again. So, we needed to

**[06:02]** garbage back out again. So, we needed to

**[06:02]** garbage back out again. So, we needed to give them the the right information in

**[06:04]** give them the the right information in

**[06:04]** give them the the right information in the context window and kind of limit and

**[06:06]** the context window and kind of limit and

**[06:06]** the context window and kind of limit and give it um move it up as high as

**[06:08]** give it um move it up as high as

**[06:08]** give it um move it up as high as possible. Be able to do more dynamic

**[06:11]** possible. Be able to do more dynamic

**[06:11]** possible. Be able to do more dynamic prompting with things like DSPY and

**[06:13]** prompting with things like DSPY and

**[06:13]** prompting with things like DSPY and BAML. Um ability to do more reasoning um

**[06:17]** BAML. Um ability to do more reasoning um

**[06:17]** BAML. Um ability to do more reasoning um so we can do internal context

**[06:19]** so we can do internal context

**[06:19]** so we can do internal context engineering on top of our data. This

**[06:22]** engineering on top of our data. This

**[06:22]** engineering on top of our data. This will turn us from human developers into

**[06:25]** will turn us from human developers into

**[06:25]** will turn us from human developers into agents where we're actually using more

**[06:27]** agents where we're actually using more

**[06:27]** agents where we're actually using more agent technology to fuel our

**[06:29]** agent technology to fuel our

**[06:29]** agent technology to fuel our applications to build things. Um, and

**[06:31]** applications to build things. Um, and

**[06:32]** applications to build things. Um, and then this allows us to focus more on the

**[06:35]** then this allows us to focus more on the

**[06:35]** then this allows us to focus more on the time which we're doing our tests rather

**[06:38]** time which we're doing our tests rather

**[06:38]** time which we're doing our tests rather than just focusing on the time which

**[06:39]** than just focusing on the time which

**[06:39]** than just focusing on the time which we're training our models. Um, so

**[06:42]** we're training our models. Um, so

**[06:42]** we're training our models. Um, so together when we have more context now

**[06:45]** together when we have more context now

**[06:45]** together when we have more context now it allows us to do better things but

**[06:47]** it allows us to do better things but

**[06:47]** it allows us to do better things but then it's still important that we really

**[06:49]** then it's still important that we really

**[06:49]** then it's still important that we really have structured information relevant

**[06:52]** have structured information relevant

**[06:52]** have structured information relevant inputs and this improves the reliability

**[06:54]** inputs and this improves the reliability

**[06:54]** inputs and this improves the reliability and the explanability of our models that

**[06:55]** and the explanability of our models that

**[06:56]** and the explanability of our models that come out of it. Um so one of the ways

**[06:59]** come out of it. Um so one of the ways

**[06:59]** come out of it. Um so one of the ways which we can do this is by leveraging


### [07:00 - 08:00]

**[07:01]** which we can do this is by leveraging

**[07:01]** which we can do this is by leveraging knowledge graphs. Knowledge graphs are a

**[07:03]** knowledge graphs. Knowledge graphs are a

**[07:03]** knowledge graphs. Knowledge graphs are a technology which has been around for a

**[07:05]** technology which has been around for a

**[07:05]** technology which has been around for a while but they're very applicable for AI

**[07:07]** while but they're very applicable for AI

**[07:07]** while but they're very applicable for AI because they fill in that gap between

**[07:10]** because they fill in that gap between

**[07:10]** because they fill in that gap between the AI which is very good at um creating

**[07:14]** the AI which is very good at um creating

**[07:14]** the AI which is very good at um creating things building things kind of pulling

**[07:16]** things building things kind of pulling

**[07:16]** things building things kind of pulling from different sources it has but um

**[07:18]** from different sources it has but um

**[07:18]** from different sources it has but um structured information knowledge graphs

**[07:20]** structured information knowledge graphs

**[07:20]** structured information knowledge graphs are a structured representation to

**[07:22]** are a structured representation to

**[07:22]** are a structured representation to understand a bit about how a knowledge

**[07:24]** understand a bit about how a knowledge

**[07:24]** understand a bit about how a knowledge graph is constructed.

**[07:26]** graph is constructed.

**[07:26]** graph is constructed. It's typically built with facts which

**[07:28]** It's typically built with facts which

**[07:28]** It's typically built with facts which are are nodes about people, places,

**[07:30]** are are nodes about people, places,

**[07:30]** are are nodes about people, places, events or things. Those are linked

**[07:32]** events or things. Those are linked

**[07:32]** events or things. Those are linked together by relationships or um um lines

**[07:36]** together by relationships or um um lines

**[07:36]** together by relationships or um um lines between them which reference how those

**[07:38]** between them which reference how those

**[07:38]** between them which reference how those things are related. It's very easy for

**[07:41]** things are related. It's very easy for

**[07:41]** things are related. It's very easy for both humans and LLMs to read knowledge

**[07:44]** both humans and LLMs to read knowledge

**[07:44]** both humans and LLMs to read knowledge graphs. So both acts as a um organizing

**[07:47]** graphs. So both acts as a um organizing

**[07:47]** graphs. So both acts as a um organizing concept, but also a way which you can

**[07:49]** concept, but also a way which you can

**[07:49]** concept, but also a way which you can understand what your AI is doing and

**[07:51]** understand what your AI is doing and

**[07:51]** understand what your AI is doing and actually look at some of the data behind

**[07:52]** actually look at some of the data behind

**[07:52]** actually look at some of the data behind it. And um it can be also very useful as

**[07:55]** it. And um it can be also very useful as

**[07:55]** it. And um it can be also very useful as a digital twin of your organization, of

**[07:57]** a digital twin of your organization, of

**[07:57]** a digital twin of your organization, of your supply chain, of um a whole bunch


### [08:00 - 09:00]

**[08:00]** your supply chain, of um a whole bunch

**[08:00]** your supply chain, of um a whole bunch of different processes in your

**[08:03]** of different processes in your

**[08:03]** of different processes in your organization. And the basic construct of

**[08:05]** organization. And the basic construct of

**[08:06]** organization. And the basic construct of a knowledge graph is um nodes which

**[08:08]** a knowledge graph is um nodes which

**[08:08]** a knowledge graph is um nodes which represent different people in the

**[08:10]** represent different people in the

**[08:10]** represent different people in the situation, relationships, and then you

**[08:12]** situation, relationships, and then you

**[08:12]** situation, relationships, and then you can attach properties to these nodes. So

**[08:13]** can attach properties to these nodes. So

**[08:13]** can attach properties to these nodes. So this is an example of a knowledge graph

**[08:15]** this is an example of a knowledge graph

**[08:15]** this is an example of a knowledge graph where you have two people, they know

**[08:17]** where you have two people, they know

**[08:17]** where you have two people, they know each other, they live with each other.

**[08:20]** each other, they live with each other.

**[08:20]** each other, they live with each other. Well, one person lives with the other.

**[08:21]** Well, one person lives with the other.

**[08:21]** Well, one person lives with the other. So I guess technically it's Ann's house

**[08:23]** So I guess technically it's Ann's house

**[08:23]** So I guess technically it's Ann's house and they both drive a car. Now the car

**[08:26]** and they both drive a car. Now the car

**[08:26]** and they both drive a car. Now the car is owned by Dan or or by an driven by

**[08:31]** is owned by Dan or or by an driven by

**[08:31]** is owned by Dan or or by an driven by Dan as well. So they both have a

**[08:34]** Dan as well. So they both have a

**[08:34]** Dan as well. So they both have a relationship with the car and they have

**[08:36]** relationship with the car and they have

**[08:36]** relationship with the car and they have a relationship with living each other.

**[08:37]** a relationship with living each other.

**[08:37]** a relationship with living each other. And you can see the there's attributes

**[08:39]** And you can see the there's attributes

**[08:39]** And you can see the there's attributes on this. How long has Dan lived or

**[08:42]** on this. How long has Dan lived or

**[08:42]** on this. How long has Dan lived or driven the car, the type of car? So it's

**[08:44]** driven the car, the type of car? So it's

**[08:44]** driven the car, the type of car? So it's a Volvo. Um it's a um model V70. some

**[08:49]** a Volvo. Um it's a um model V70. some

**[08:49]** a Volvo. Um it's a um model V70. some information about it and also some

**[08:51]** information about it and also some

**[08:51]** information about it and also some embeddings. So we can also encapsulate

**[08:53]** embeddings. So we can also encapsulate

**[08:53]** embeddings. So we can also encapsulate embeddings on the graph as well. So we

**[08:56]** embeddings on the graph as well. So we

**[08:56]** embeddings on the graph as well. So we can do vector lookups and this allows us

**[08:59]** can do vector lookups and this allows us

**[08:59]** can do vector lookups and this allows us to do fairly complex things as we build


### [09:00 - 10:00]

**[09:01]** to do fairly complex things as we build

**[09:01]** to do fairly complex things as we build larger knowledge graphs to capture all

**[09:04]** larger knowledge graphs to capture all

**[09:04]** larger knowledge graphs to capture all this information. And what knowledge

**[09:07]** this information. And what knowledge

**[09:07]** this information. And what knowledge graphs gives the benefit of is all of

**[09:08]** graphs gives the benefit of is all of

**[09:08]** graphs gives the benefit of is all of that knowledge context and enrichment

**[09:10]** that knowledge context and enrichment

**[09:10]** that knowledge context and enrichment that we can build into a representation

**[09:13]** that we can build into a representation

**[09:13]** that we can build into a representation of knowledge in addition to LLMs which

**[09:17]** of knowledge in addition to LLMs which

**[09:17]** of knowledge in addition to LLMs which have kind of that language reasoning and

**[09:19]** have kind of that language reasoning and

**[09:19]** have kind of that language reasoning and creativity and when we put them together

**[09:20]** creativity and when we put them together

**[09:20]** creativity and when we put them together we can do really powerful things.

**[09:23]** we can do really powerful things.

**[09:23]** we can do really powerful things. Um so we talked a bit about rag being an

**[09:26]** Um so we talked a bit about rag being an

**[09:26]** Um so we talked a bit about rag being an essential part of context engineering

**[09:29]** essential part of context engineering

**[09:30]** essential part of context engineering and a even better way of doing rag is

**[09:33]** and a even better way of doing rag is

**[09:33]** and a even better way of doing rag is graph rag. Now what is graph rag? So

**[09:35]** graph rag. Now what is graph rag? So

**[09:35]** graph rag. Now what is graph rag? So graph rag is any retrieval pipeline

**[09:39]** graph rag is any retrieval pipeline

**[09:39]** graph rag is any retrieval pipeline which also uses graphs as part of the

**[09:42]** which also uses graphs as part of the

**[09:42]** which also uses graphs as part of the retrieval process. And so um an example

**[09:45]** retrieval process. And so um an example

**[09:45]** retrieval process. And so um an example of this is a user asks a question

**[09:48]** of this is a user asks a question

**[09:48]** of this is a user asks a question um it goes to the LM and it does a

**[09:50]** um it goes to the LM and it does a

**[09:50]** um it goes to the LM and it does a search and it asks for if there's any

**[09:51]** search and it asks for if there's any

**[09:51]** search and it asks for if there's any relevant information which will go as a

**[09:54]** relevant information which will go as a

**[09:54]** relevant information which will go as a query out to a knowledge graph. This

**[09:56]** query out to a knowledge graph. This

**[09:56]** query out to a knowledge graph. This then gets passed in as additional

**[09:58]** then gets passed in as additional

**[09:58]** then gets passed in as additional context to the LLM when it's answering


### [10:00 - 11:00]

**[10:00]** context to the LLM when it's answering

**[10:00]** context to the LLM when it's answering the question and then the LM gives an

**[10:01]** the question and then the LM gives an

**[10:02]** the question and then the LM gives an enriched answer which is more relevant.

**[10:04]** enriched answer which is more relevant.

**[10:04]** enriched answer which is more relevant. So it's it's a will give you more

**[10:07]** So it's it's a will give you more

**[10:07]** So it's it's a will give you more relevant results than just a vector

**[10:09]** relevant results than just a vector

**[10:09]** relevant results than just a vector similarity search because you also have

**[10:11]** similarity search because you also have

**[10:11]** similarity search because you also have information about relationships about

**[10:13]** information about relationships about

**[10:13]** information about relationships about nodes about community grouping more

**[10:15]** nodes about community grouping more

**[10:15]** nodes about community grouping more context. So you can now get domain

**[10:17]** context. So you can now get domain

**[10:18]** context. So you can now get domain information factual information

**[10:20]** information factual information

**[10:20]** information factual information structured knowledge on your subject.

**[10:22]** structured knowledge on your subject.

**[10:22]** structured knowledge on your subject. You can explain what the LM is actually

**[10:25]** You can explain what the LM is actually

**[10:25]** You can explain what the LM is actually doing because you can see the part of

**[10:26]** doing because you can see the part of

**[10:26]** doing because you can see the part of the knowledge graph which got passed to

**[10:27]** the knowledge graph which got passed to

**[10:27]** the knowledge graph which got passed to the LM. And you can also evolve the

**[10:30]** the LM. And you can also evolve the

**[10:30]** the LM. And you can also evolve the knowledge graph over time. And you can

**[10:32]** knowledge graph over time. And you can

**[10:32]** knowledge graph over time. And you can now start to implement overlays like

**[10:34]** now start to implement overlays like

**[10:34]** now start to implement overlays like role-based access. So you can say only

**[10:37]** role-based access. So you can say only

**[10:37]** role-based access. So you can say only these people get access for example in a

**[10:39]** these people get access for example in a

**[10:39]** these people get access for example in a um patient information system only the

**[10:43]** um patient information system only the

**[10:43]** um patient information system only the doctor would have access to the

**[10:45]** doctor would have access to the

**[10:45]** doctor would have access to the diagnosis but only the person who um

**[10:49]** diagnosis but only the person who um

**[10:49]** diagnosis but only the person who um handles the administrative information

**[10:50]** handles the administrative information

**[10:50]** handles the administrative information would have access to phone numbers or

**[10:53]** would have access to phone numbers or

**[10:53]** would have access to phone numbers or addresses or other personal information

**[10:54]** addresses or other personal information

**[10:54]** addresses or other personal information about the patient. So it allows you to

**[10:56]** about the patient. So it allows you to

**[10:56]** about the patient. So it allows you to kind of overload overlay that role based

**[10:58]** kind of overload overlay that role based

**[10:58]** kind of overload overlay that role based access directly on the knowledge graph


### [11:00 - 12:00]

**[11:00]** access directly on the knowledge graph

**[11:00]** access directly on the knowledge graph and then instruct the LM on what

**[11:02]** and then instruct the LM on what

**[11:02]** and then instruct the LM on what information it's allowed to respond with

**[11:05]** information it's allowed to respond with

**[11:05]** information it's allowed to respond with and um knowledge graphs allow this sort

**[11:07]** and um knowledge graphs allow this sort

**[11:07]** and um knowledge graphs allow this sort of explainable AI. So in a in a large

**[11:10]** of explainable AI. So in a in a large

**[11:10]** of explainable AI. So in a in a large graph with a lot of nodes and a lot of

**[11:11]** graph with a lot of nodes and a lot of

**[11:12]** graph with a lot of nodes and a lot of information now you can store the

**[11:13]** information now you can store the

**[11:13]** information now you can store the learnings from the user and agents at

**[11:15]** learnings from the user and agents at

**[11:15]** learnings from the user and agents at the interactions in the graph context.

**[11:18]** the interactions in the graph context.

**[11:18]** the interactions in the graph context. You can start to visualize conversation

**[11:20]** You can start to visualize conversation

**[11:20]** You can start to visualize conversation flows with the addition of reasoning.

**[11:23]** flows with the addition of reasoning.

**[11:24]** flows with the addition of reasoning. You can analyze the context data of

**[11:25]** You can analyze the context data of

**[11:25]** You can analyze the context data of agent systems about performance

**[11:28]** agent systems about performance

**[11:28]** agent systems about performance um identify opportunities for

**[11:30]** um identify opportunities for

**[11:30]** um identify opportunities for improvement over time of the um either

**[11:33]** improvement over time of the um either

**[11:33]** improvement over time of the um either the um the quality of the results which

**[11:35]** the um the quality of the results which

**[11:35]** the um the quality of the results which you're passing in the relationships um

**[11:37]** you're passing in the relationships um

**[11:38]** you're passing in the relationships um removing duplicate nodes so that you get

**[11:39]** removing duplicate nodes so that you get

**[11:40]** removing duplicate nodes so that you get better quality results coming out of it.

**[11:41]** better quality results coming out of it.

**[11:41]** better quality results coming out of it. So it gives you a lot of control over

**[11:43]** So it gives you a lot of control over

**[11:43]** So it gives you a lot of control over the application and the ability to

**[11:45]** the application and the ability to

**[11:45]** the application and the ability to modify and control what the AI is

**[11:47]** modify and control what the AI is

**[11:47]** modify and control what the AI is answering kind of like you're you're

**[11:49]** answering kind of like you're you're

**[11:49]** answering kind of like you're you're training in a in a dojo. So I think you

**[11:52]** training in a in a dojo. So I think you

**[11:52]** training in a in a dojo. So I think you know in the in the film Neo spends a lot

**[11:54]** know in the in the film Neo spends a lot

**[11:54]** know in the in the film Neo spends a lot of time doing virtual training improving

**[11:56]** of time doing virtual training improving

**[11:56]** of time doing virtual training improving his skills with different programs he's

**[11:58]** his skills with different programs he's

**[11:58]** his skills with different programs he's loaded up and um this is how we're able


### [12:00 - 13:00]

**[12:02]** loaded up and um this is how we're able

**[12:02]** loaded up and um this is how we're able to do a lot of amazing things like this

**[12:04]** to do a lot of amazing things like this

**[12:04]** to do a lot of amazing things like this demo which I'm going to show you. So the

**[12:06]** demo which I'm going to show you. So the

**[12:06]** demo which I'm going to show you. So the first demo we're going to show is a um

**[12:09]** first demo we're going to show is a um

**[12:09]** first demo we're going to show is a um graph rack demo using the LLM knowledge

**[12:11]** graph rack demo using the LLM knowledge

**[12:12]** graph rack demo using the LLM knowledge graph builder. So I've already set up a

**[12:14]** graph builder. So I've already set up a

**[12:14]** graph builder. So I've already set up a Neo Forj aura instance. This is the um

**[12:17]** Neo Forj aura instance. This is the um

**[12:17]** Neo Forj aura instance. This is the um um online free version of Neo Forj. You

**[12:19]** um online free version of Neo Forj. You

**[12:19]** um online free version of Neo Forj. You can see I have a a running instance with

**[12:21]** can see I have a a running instance with

**[12:21]** can see I have a a running instance with a bunch of relationships loaded up. And

**[12:23]** a bunch of relationships loaded up. And

**[12:23]** a bunch of relationships loaded up. And to load up those relationships, I use

**[12:26]** to load up those relationships, I use

**[12:26]** to load up those relationships, I use the knowledge graph builder. The

**[12:28]** the knowledge graph builder. The

**[12:28]** the knowledge graph builder. The knowledge graph builder is a very simple

**[12:30]** knowledge graph builder is a very simple

**[12:30]** knowledge graph builder is a very simple web application. It's open source and it

**[12:32]** web application. It's open source and it

**[12:32]** web application. It's open source and it lets you do a couple things. So, it lets

**[12:34]** lets you do a couple things. So, it lets

**[12:34]** lets you do a couple things. So, it lets you upload files. So, you can drag and

**[12:37]** you upload files. So, you can drag and

**[12:37]** you upload files. So, you can drag and drop different files into the user

**[12:38]** drop different files into the user

**[12:38]** drop different files into the user interface. Before the presentation, I

**[12:40]** interface. Before the presentation, I

**[12:40]** interface. Before the presentation, I loaded up a couple representative files

**[12:43]** loaded up a couple representative files

**[12:43]** loaded up a couple representative files of a um supply chain use case. One is a

**[12:46]** of a um supply chain use case. One is a

**[12:46]** of a um supply chain use case. One is a supply chain document and as you can see

**[12:48]** supply chain document and as you can see

**[12:48]** supply chain document and as you can see here it has a whole bunch of information

**[12:50]** here it has a whole bunch of information

**[12:50]** here it has a whole bunch of information about different artifacts

**[12:52]** about different artifacts

**[12:52]** about different artifacts um and the digital signatures of them

**[12:55]** um and the digital signatures of them

**[12:55]** um and the digital signatures of them and the relationship of them. And the

**[12:58]** and the relationship of them. And the

**[12:58]** and the relationship of them. And the second one is the more interesting one.

**[12:59]** second one is the more interesting one.

**[12:59]** second one is the more interesting one. This is a a VEX document which is a


### [13:00 - 14:00]

**[13:01]** This is a a VEX document which is a

**[13:01]** This is a a VEX document which is a security standard and it talks about

**[13:03]** security standard and it talks about

**[13:03]** security standard and it talks about some vulnerabilities

**[13:05]** some vulnerabilities

**[13:05]** some vulnerabilities um in this case inside the Jackson

**[13:07]** um in this case inside the Jackson

**[13:07]** um in this case inside the Jackson library and talks a bit about um how to

**[13:10]** library and talks a bit about um how to

**[13:10]** library and talks a bit about um how to remediate with it, which versions are

**[13:12]** remediate with it, which versions are

**[13:12]** remediate with it, which versions are affected

**[13:13]** affected

**[13:13]** affected um which commits fix it and all that

**[13:16]** um which commits fix it and all that

**[13:16]** um which commits fix it and all that good stuff. So um we have quite a bit of

**[13:18]** good stuff. So um we have quite a bit of

**[13:18]** good stuff. So um we have quite a bit of information which we loaded up and then

**[13:20]** information which we loaded up and then

**[13:20]** information which we loaded up and then what I've done is I've already dropped

**[13:22]** what I've done is I've already dropped

**[13:22]** what I've done is I've already dropped those into the knowledge graph and we

**[13:24]** those into the knowledge graph and we

**[13:24]** those into the knowledge graph and we can take a look at what got generated by

**[13:27]** can take a look at what got generated by

**[13:27]** can take a look at what got generated by the LM. So it takes this through an

**[13:29]** the LM. So it takes this through an

**[13:29]** the LM. So it takes this through an ingest phase um where the LM actually

**[13:32]** ingest phase um where the LM actually

**[13:32]** ingest phase um where the LM actually builds out a knowledge graph and then we

**[13:34]** builds out a knowledge graph and then we

**[13:34]** builds out a knowledge graph and then we can see that some of these nodes

**[13:36]** can see that some of these nodes

**[13:36]** can see that some of these nodes represent different parts of the um VEX

**[13:39]** represent different parts of the um VEX

**[13:39]** represent different parts of the um VEX document. Um here we can see some

**[13:42]** document. Um here we can see some

**[13:42]** document. Um here we can see some information about um um who found the

**[13:46]** information about um um who found the

**[13:46]** information about um um who found the vulnerability, information about the um

**[13:49]** vulnerability, information about the um

**[13:49]** vulnerability, information about the um vulnerability database URL and um all

**[13:52]** vulnerability database URL and um all

**[13:52]** vulnerability database URL and um all this stuff is connected with different

**[13:53]** this stuff is connected with different

**[13:53]** this stuff is connected with different relationships and this allows us to

**[13:55]** relationships and this allows us to

**[13:55]** relationships and this allows us to query, navigate and traverse this

**[13:57]** query, navigate and traverse this

**[13:57]** query, navigate and traverse this information to build better responses

**[13:59]** information to build better responses

**[13:59]** information to build better responses for the LM. So what we're going to do in


### [14:00 - 15:00]

**[14:02]** for the LM. So what we're going to do in

**[14:02]** for the LM. So what we're going to do in this demo is we're going to take this

**[14:04]** this demo is we're going to take this

**[14:04]** this demo is we're going to take this knowledge graph which we built and then

**[14:07]** knowledge graph which we built and then

**[14:07]** knowledge graph which we built and then we're going to run an LLM which does a

**[14:10]** we're going to run an LLM which does a

**[14:10]** we're going to run an LLM which does a two-pass process. The first pass it's

**[14:13]** two-pass process. The first pass it's

**[14:13]** two-pass process. The first pass it's going to do a vector lookup and find a

**[14:16]** going to do a vector lookup and find a

**[14:16]** going to do a vector lookup and find a similarity search to find related nodes

**[14:19]** similarity search to find related nodes

**[14:19]** similarity search to find related nodes in the knowledge graph. And the second

**[14:21]** in the knowledge graph. And the second

**[14:21]** in the knowledge graph. And the second pass it's going to take those nodes

**[14:24]** pass it's going to take those nodes

**[14:24]** pass it's going to take those nodes which are related to the result find

**[14:26]** which are related to the result find

**[14:26]** which are related to the result find related nodes and then pass those in as

**[14:28]** related nodes and then pass those in as

**[14:28]** related nodes and then pass those in as context to the LM. And ideally what we'd

**[14:31]** context to the LM. And ideally what we'd

**[14:31]** context to the LM. And ideally what we'd what we'd like to get from the LM is

**[14:34]** what we'd like to get from the LM is

**[14:34]** what we'd like to get from the LM is that um it will answer questions with

**[14:36]** that um it will answer questions with

**[14:36]** that um it will answer questions with information it has from the knowledge

**[14:38]** information it has from the knowledge

**[14:38]** information it has from the knowledge graph and then it won't be able to

**[14:40]** graph and then it won't be able to

**[14:40]** graph and then it won't be able to answer questions or refuse to answer

**[14:42]** answer questions or refuse to answer

**[14:42]** answer questions or refuse to answer questions with things which are outside

**[14:43]** questions with things which are outside

**[14:43]** questions with things which are outside that knowledge um pool. So let's ask it

**[14:48]** that knowledge um pool. So let's ask it

**[14:48]** that knowledge um pool. So let's ask it [gasps and sighs]

**[14:49]** [gasps and sighs]

**[14:49]** [gasps and sighs] um about vulnerabilities

**[14:53]** um about vulnerabilities

**[14:53]** um about vulnerabilities in the in the Jasper library. So Jasper

**[14:55]** in the in the Jasper library. So Jasper

**[14:55]** in the in the Jasper library. So Jasper is another um Java library that's very

**[14:58]** is another um Java library that's very

**[14:58]** is another um Java library that's very commonly used. It wasn't actually

**[14:59]** commonly used. It wasn't actually

**[14:59]** commonly used. It wasn't actually referenced in the VEX document. So,


### [15:00 - 16:00]

**[15:01]** referenced in the VEX document. So,

**[15:01]** referenced in the VEX document. So, we're in this case, we're hoping to get

**[15:03]** we're in this case, we're hoping to get

**[15:03]** we're in this case, we're hoping to get a no response. Okay, so that's amazing.

**[15:07]** a no response. Okay, so that's amazing.

**[15:07]** a no response. Okay, so that's amazing. I I made a typo. I should have said

**[15:09]** I I made a typo. I should have said

**[15:10]** I I made a typo. I should have said Jackson.

**[15:12]** Jackson.

**[15:12]** Jackson. Let's see what we get when we um ask

**[15:15]** Let's see what we get when we um ask

**[15:15]** Let's see what we get when we um ask about the Jackson library, even with the

**[15:16]** about the Jackson library, even with the

**[15:16]** about the Jackson library, even with the typo, because LMS know that humans are

**[15:19]** typo, because LMS know that humans are

**[15:19]** typo, because LMS know that humans are imperfect and they're very good at

**[15:20]** imperfect and they're very good at

**[15:20]** imperfect and they're very good at fixing our mistakes. And um here we can

**[15:22]** fixing our mistakes. And um here we can

**[15:22]** fixing our mistakes. And um here we can see that it actually pulled out

**[15:23]** see that it actually pulled out

**[15:23]** see that it actually pulled out information about the Jackson databind

**[15:25]** information about the Jackson databind

**[15:25]** information about the Jackson databind library with an XML injection attack. It

**[15:28]** library with an XML injection attack. It

**[15:28]** library with an XML injection attack. It knows a bit about the vulnerability,

**[15:31]** knows a bit about the vulnerability,

**[15:31]** knows a bit about the vulnerability, what version it's in, um whether it's

**[15:34]** what version it's in, um whether it's

**[15:34]** what version it's in, um whether it's fixed and at which version it's fixed

**[15:37]** fixed and at which version it's fixed

**[15:37]** fixed and at which version it's fixed and um all this information is is pulled

**[15:39]** and um all this information is is pulled

**[15:39]** and um all this information is is pulled from and aggregate off the knowledge

**[15:40]** from and aggregate off the knowledge

**[15:40]** from and aggregate off the knowledge graph. So um it gives us quite a lot of

**[15:43]** graph. So um it gives us quite a lot of

**[15:43]** graph. So um it gives us quite a lot of information um very detailed and very

**[15:46]** information um very detailed and very

**[15:46]** information um very detailed and very focused because it's rounded in a um

**[15:50]** focused because it's rounded in a um

**[15:50]** focused because it's rounded in a um data which is um very um complete

**[15:55]** data which is um very um complete

**[15:55]** data which is um very um complete um it's finite and it's something we can

**[15:58]** um it's finite and it's something we can

**[15:58]** um it's finite and it's something we can edit modify and change the response over


### [16:00 - 17:00]

**[16:01]** edit modify and change the response over

**[16:01]** edit modify and change the response over time. So knowledge graphs are a very

**[16:03]** time. So knowledge graphs are a very

**[16:03]** time. So knowledge graphs are a very powerful tool. It allows us to do things

**[16:05]** powerful tool. It allows us to do things

**[16:05]** powerful tool. It allows us to do things like this where we can um get better

**[16:08]** like this where we can um get better

**[16:08]** like this where we can um get better responses and better answers. And now

**[16:11]** responses and better answers. And now

**[16:11]** responses and better answers. And now with knowledge graphs at our disposal,

**[16:13]** with knowledge graphs at our disposal,

**[16:13]** with knowledge graphs at our disposal, now we can we can go and we can fight

**[16:15]** now we can we can go and we can fight

**[16:16]** now we can we can go and we can fight the um the evil agents. Actually, it's

**[16:18]** the um the evil agents. Actually, it's

**[16:18]** the um the evil agents. Actually, it's kind of ironic that the um the agents of

**[16:21]** kind of ironic that the um the agents of

**[16:21]** kind of ironic that the um the agents of the Matrix film were um the bad guys,

**[16:24]** the Matrix film were um the bad guys,

**[16:24]** the Matrix film were um the bad guys, but actually they operated and acted a

**[16:26]** but actually they operated and acted a

**[16:26]** but actually they operated and acted a lot like modern agents where we're

**[16:28]** lot like modern agents where we're

**[16:28]** lot like modern agents where we're having LMS collaborate, pull together,

**[16:31]** having LMS collaborate, pull together,

**[16:31]** having LMS collaborate, pull together, and um cooperate on different

**[16:33]** and um cooperate on different

**[16:33]** and um cooperate on different algorithms. And even the agents in the

**[16:35]** algorithms. And even the agents in the

**[16:35]** algorithms. And even the agents in the film had different personalities and um

**[16:37]** film had different personalities and um

**[16:37]** film had different personalities and um different types um kind of like

**[16:38]** different types um kind of like

**[16:38]** different types um kind of like individual agents. So um we need to

**[16:41]** individual agents. So um we need to

**[16:41]** individual agents. So um we need to power up and and get our um matrix and

**[16:45]** power up and and get our um matrix and

**[16:45]** power up and and get our um matrix and graph skills up to a level where we can

**[16:46]** graph skills up to a level where we can

**[16:46]** graph skills up to a level where we can go tackle the agents with new tools like

**[16:50]** go tackle the agents with new tools like

**[16:50]** go tackle the agents with new tools like memory retrieval. So we we talked a bit

**[16:52]** memory retrieval. So we we talked a bit

**[16:52]** memory retrieval. So we we talked a bit about graph retrieval and um graphs are

**[16:55]** about graph retrieval and um graphs are

**[16:56]** about graph retrieval and um graphs are also a great tool and mechanism which

**[16:58]** also a great tool and mechanism which

**[16:58]** also a great tool and mechanism which you can use to do um memory retrieval as


### [17:00 - 18:00]

**[17:00]** you can use to do um memory retrieval as

**[17:00]** you can use to do um memory retrieval as well. So we can do search

**[17:03]** well. So we can do search

**[17:03]** well. So we can do search um in in memory use graph memory

**[17:05]** um in in memory use graph memory

**[17:05]** um in in memory use graph memory retrieval tools. We have an open- source

**[17:07]** retrieval tools. We have an open- source

**[17:07]** retrieval tools. We have an open- source MCP server which does a lot of this for

**[17:10]** MCP server which does a lot of this for

**[17:10]** MCP server which does a lot of this for graph retrievalss. And now you can query

**[17:13]** graph retrievalss. And now you can query

**[17:13]** graph retrievalss. And now you can query the graph not only for knowledge graphs

**[17:16]** the graph not only for knowledge graphs

**[17:16]** the graph not only for knowledge graphs but also vectors as we did in the last

**[17:18]** but also vectors as we did in the last

**[17:18]** but also vectors as we did in the last um example. And we can also use graph

**[17:20]** um example. And we can also use graph

**[17:20]** um example. And we can also use graph data science algorithms like um

**[17:23]** data science algorithms like um

**[17:23]** data science algorithms like um community groupings or k nearest

**[17:24]** community groupings or k nearest

**[17:24]** community groupings or k nearest neighbors or different graph algorithms

**[17:26]** neighbors or different graph algorithms

**[17:26]** neighbors or different graph algorithms which allow us to get um pull some

**[17:29]** which allow us to get um pull some

**[17:29]** which allow us to get um pull some insights out of the relationship and the

**[17:31]** insights out of the relationship and the

**[17:31]** insights out of the relationship and the structure of the graph. Pull back

**[17:33]** structure of the graph. Pull back

**[17:33]** structure of the graph. Pull back relevant information and then pass this

**[17:35]** relevant information and then pass this

**[17:35]** relevant information and then pass this as additional context um either for

**[17:38]** as additional context um either for

**[17:38]** as additional context um either for short-term or long-term memory into the

**[17:39]** short-term or long-term memory into the

**[17:40]** short-term or long-term memory into the agent loop. um where now we're feeding

**[17:42]** agent loop. um where now we're feeding

**[17:42]** agent loop. um where now we're feeding the agent with additional information

**[17:44]** the agent with additional information

**[17:44]** the agent with additional information and context from either um a short-term

**[17:47]** and context from either um a short-term

**[17:47]** and context from either um a short-term memory source about the current

**[17:49]** memory source about the current

**[17:49]** memory source about the current conversation or knowledge pulled in like

**[17:52]** conversation or knowledge pulled in like

**[17:52]** conversation or knowledge pulled in like kind of what we showed in the previous

**[17:53]** kind of what we showed in the previous

**[17:53]** kind of what we showed in the previous example from a graph or from a long-term

**[17:57]** example from a graph or from a long-term

**[17:57]** example from a graph or from a long-term structure of memory where we memorize um


### [18:00 - 19:00]

**[18:00]** structure of memory where we memorize um

**[18:00]** structure of memory where we memorize um previous conversations give them

**[18:02]** previous conversations give them

**[18:02]** previous conversations give them temporal information and then structure

**[18:04]** temporal information and then structure

**[18:04]** temporal information and then structure those into a memory that can be

**[18:05]** those into a memory that can be

**[18:05]** those into a memory that can be retrieved from the graph. And um now

**[18:08]** retrieved from the graph. And um now

**[18:08]** retrieved from the graph. And um now we're able to use graph memory to

**[18:09]** we're able to use graph memory to

**[18:09]** we're able to use graph memory to capture knowledge in the form of

**[18:11]** capture knowledge in the form of

**[18:11]** capture knowledge in the form of entities and relationships between them

**[18:13]** entities and relationships between them

**[18:13]** entities and relationships between them where some nodes have the relevant

**[18:14]** where some nodes have the relevant

**[18:14]** where some nodes have the relevant properties such as text details

**[18:15]** properties such as text details

**[18:16]** properties such as text details embeddings time and location on top of

**[18:18]** embeddings time and location on top of

**[18:18]** embeddings time and location on top of them. So this is kind of a visual

**[18:19]** them. So this is kind of a visual

**[18:19]** them. So this is kind of a visual representation of our of our graph our

**[18:22]** representation of our of our graph our

**[18:22]** representation of our of our graph our memory graph. Some of these properties

**[18:24]** memory graph. Some of these properties

**[18:24]** memory graph. Some of these properties get vector embedded and this enables us

**[18:26]** get vector embedded and this enables us

**[18:26]** get vector embedded and this enables us to do vector-based semantic search. So

**[18:29]** to do vector-based semantic search. So

**[18:29]** to do vector-based semantic search. So now we can do semantic search on the

**[18:31]** now we can do semantic search on the

**[18:31]** now we can do semantic search on the graphs via projections into vector

**[18:33]** graphs via projections into vector

**[18:33]** graphs via projections into vector space. But then we can also use

**[18:36]** space. But then we can also use

**[18:36]** space. But then we can also use algorithms like K approximate nearest

**[18:38]** algorithms like K approximate nearest

**[18:38]** algorithms like K approximate nearest neighbors, community groupings,

**[18:42]** neighbors, community groupings,

**[18:42]** neighbors, community groupings, um page rank algorithms on top of the

**[18:44]** um page rank algorithms on top of the

**[18:44]** um page rank algorithms on top of the graph to answer different types of

**[18:47]** graph to answer different types of

**[18:47]** graph to answer different types of questions and to kind of bubble up the

**[18:49]** questions and to kind of bubble up the

**[18:49]** questions and to kind of bubble up the most relevant results into the context.

**[18:51]** most relevant results into the context.

**[18:51]** most relevant results into the context. This gives us quite a lot of power

**[18:52]** This gives us quite a lot of power

**[18:52]** This gives us quite a lot of power because we can do both the vector

**[18:54]** because we can do both the vector

**[18:54]** because we can do both the vector embeddings, but we can also

**[18:57]** embeddings, but we can also

**[18:57]** embeddings, but we can also do additional graph algorithms on top of

**[18:59]** do additional graph algorithms on top of

**[18:59]** do additional graph algorithms on top of it.


### [19:00 - 20:00]

**[19:05]** Okay, so now we have our our superpower

**[19:05]** Okay, so now we have our our superpower with our our graph where we're able to

**[19:07]** with our our graph where we're able to

**[19:07]** with our our graph where we're able to do amazing things which aren't possible

**[19:09]** do amazing things which aren't possible

**[19:09]** do amazing things which aren't possible just with um vector embeddings and

**[19:10]** just with um vector embeddings and

**[19:10]** just with um vector embeddings and similarity searches kind of like like

**[19:12]** similarity searches kind of like like

**[19:12]** similarity searches kind of like like the bullet time and the Matrix films. Um

**[19:15]** the bullet time and the Matrix films. Um

**[19:15]** the bullet time and the Matrix films. Um this will allow us to do amazing stunts

**[19:17]** this will allow us to do amazing stunts

**[19:17]** this will allow us to do amazing stunts and to evade the um um the agents. But

**[19:21]** and to evade the um um the agents. But

**[19:21]** and to evade the um um the agents. But let's give a quick example of how this

**[19:23]** let's give a quick example of how this

**[19:23]** let's give a quick example of how this would actually work in practice. So

**[19:25]** would actually work in practice. So

**[19:25]** would actually work in practice. So let's say my question to the LM was

**[19:27]** let's say my question to the LM was

**[19:27]** let's say my question to the LM was let's update this presentation from the

**[19:29]** let's update this presentation from the

**[19:29]** let's update this presentation from the last time I presented with Sid who's my

**[19:31]** last time I presented with Sid who's my

**[19:31]** last time I presented with Sid who's my colleague in India. Um so we can now

**[19:35]** colleague in India. Um so we can now

**[19:35]** colleague in India. Um so we can now search this information in the graph and

**[19:37]** search this information in the graph and

**[19:37]** search this information in the graph and there's two relevant people for this

**[19:39]** there's two relevant people for this

**[19:39]** there's two relevant people for this right so it's it's me um VP of Devril

**[19:42]** right so it's it's me um VP of Devril

**[19:42]** right so it's it's me um VP of Devril it's Sid who's a community manager and

**[19:45]** it's Sid who's a community manager and

**[19:45]** it's Sid who's a community manager and the event and the last time we presented

**[19:48]** the event and the last time we presented

**[19:48]** the event and the last time we presented it was at an event called GIDS um which

**[19:51]** it was at an event called GIDS um which

**[19:51]** it was at an event called GIDS um which is an event in Bangalore awesome

**[19:53]** is an event in Bangalore awesome

**[19:53]** is an event in Bangalore awesome developer conference so um now we have

**[19:56]** developer conference so um now we have

**[19:56]** developer conference so um now we have kind of that temporal relationship with

**[19:59]** kind of that temporal relationship with

**[19:59]** kind of that temporal relationship with the two people and then an event and we


### [20:00 - 21:00]

**[20:02]** the two people and then an event and we

**[20:02]** the two people and then an event and we can add to this the the memory record at

**[20:05]** can add to this the the memory record at

**[20:05]** can add to this the the memory record at a particular time of the presentation.

**[20:08]** a particular time of the presentation.

**[20:08]** a particular time of the presentation. So now we're pulling back information

**[20:10]** So now we're pulling back information

**[20:10]** So now we're pulling back information about this presentation at a specific

**[20:12]** about this presentation at a specific

**[20:12]** about this presentation at a specific point in time and we can pass this in as

**[20:15]** point in time and we can pass this in as

**[20:15]** point in time and we can pass this in as context to the LM. So when we ask it to

**[20:17]** context to the LM. So when we ask it to

**[20:17]** context to the LM. So when we ask it to update the presentation we both have the

**[20:20]** update the presentation we both have the

**[20:20]** update the presentation we both have the context of who presented where they

**[20:22]** context of who presented where they

**[20:22]** context of who presented where they presented and the time period in which

**[20:24]** presented and the time period in which

**[20:24]** presented and the time period in which they presented for the LM to build

**[20:26]** they presented for the LM to build

**[20:26]** they presented for the LM to build additional information on top of it. And

**[20:28]** additional information on top of it. And

**[20:28]** additional information on top of it. And this is only possible because we can do

**[20:30]** this is only possible because we can do

**[20:30]** this is only possible because we can do this um multi-stage query with graphs.

**[20:33]** this um multi-stage query with graphs.

**[20:33]** this um multi-stage query with graphs. Graphs excel in use cases where you are

**[20:37]** Graphs excel in use cases where you are

**[20:37]** Graphs excel in use cases where you are able to pull in multiple facts which are

**[20:39]** able to pull in multiple facts which are

**[20:39]** able to pull in multiple facts which are related um but don't get pulled back in

**[20:42]** related um but don't get pulled back in

**[20:42]** related um but don't get pulled back in a single query. If you can do it in a in

**[20:44]** a single query. If you can do it in a in

**[20:44]** a single query. If you can do it in a in a one shot or you can get a a single

**[20:46]** a one shot or you can get a a single

**[20:46]** a one shot or you can get a a single similarity search um standard vector rag

**[20:50]** similarity search um standard vector rag

**[20:50]** similarity search um standard vector rag is is fine for those sorts of use cases.

**[20:53]** is is fine for those sorts of use cases.

**[20:53]** is is fine for those sorts of use cases. It's where the relationships are two or

**[20:55]** It's where the relationships are two or

**[20:55]** It's where the relationships are two or more where you get the real value from

**[20:57]** more where you get the real value from

**[20:57]** more where you get the real value from doing um graph rag and graph memory.


### [21:00 - 22:00]

**[21:01]** doing um graph rag and graph memory.

**[21:01]** doing um graph rag and graph memory. And um this allows us to do a whole

**[21:02]** And um this allows us to do a whole

**[21:02]** And um this allows us to do a whole bunch of different types of graph

**[21:03]** bunch of different types of graph

**[21:03]** bunch of different types of graph retrievers. So um we could do explicit

**[21:06]** retrievers. So um we could do explicit

**[21:06]** retrievers. So um we could do explicit retrieval queries where we have

**[21:07]** retrieval queries where we have

**[21:07]** retrieval queries where we have pre-anned retrieval queries with

**[21:09]** pre-anned retrieval queries with

**[21:09]** pre-anned retrieval queries with different entry points and retrieving

**[21:10]** different entry points and retrieving

**[21:10]** different entry points and retrieving some context. So this gives us some

**[21:12]** some context. So this gives us some

**[21:12]** some context. So this gives us some great information from the graph but we

**[21:14]** great information from the graph but we

**[21:14]** great information from the graph but we can do better by doing text decipher. So

**[21:17]** can do better by doing text decipher. So

**[21:17]** can do better by doing text decipher. So fine-tuning the LM with schema

**[21:19]** fine-tuning the LM with schema

**[21:19]** fine-tuning the LM with schema generating a query for the question and

**[21:21]** generating a query for the question and

**[21:21]** generating a query for the question and then we can kind of take this to the

**[21:23]** then we can kind of take this to the

**[21:23]** then we can kind of take this to the next level with a genetic traversal

**[21:24]** next level with a genetic traversal

**[21:24]** next level with a genetic traversal where we iteratively navigating over the

**[21:26]** where we iteratively navigating over the

**[21:26]** where we iteratively navigating over the graph collecting information until we

**[21:28]** graph collecting information until we

**[21:28]** graph collecting information until we answer it and using an appropriate set

**[21:30]** answer it and using an appropriate set

**[21:30]** answer it and using an appropriate set of tools. And to show an example of this

**[21:33]** of tools. And to show an example of this

**[21:33]** of tools. And to show an example of this um we're going to use the same knowledge

**[21:35]** um we're going to use the same knowledge

**[21:35]** um we're going to use the same knowledge graph which I loaded up again in our

**[21:38]** graph which I loaded up again in our

**[21:38]** graph which I loaded up again in our demo number two but this time we're

**[21:41]** demo number two but this time we're

**[21:41]** demo number two but this time we're going to query that knowledge graph

**[21:42]** going to query that knowledge graph

**[21:42]** going to query that knowledge graph using clawed code. So what I've done is

**[21:45]** using clawed code. So what I've done is

**[21:45]** using clawed code. So what I've done is I've hooked up claude code using the um

**[21:49]** I've hooked up claude code using the um

**[21:49]** I've hooked up claude code using the um Neoraj MCP cipher um MCP server which is

**[21:53]** Neoraj MCP cipher um MCP server which is

**[21:53]** Neoraj MCP cipher um MCP server which is an open source extension. You can say

**[21:55]** an open source extension. You can say

**[21:55]** an open source extension. You can say new forj cipher mcp server which I've

**[21:57]** new forj cipher mcp server which I've

**[21:57]** new forj cipher mcp server which I've already configured with the database

**[21:59]** already configured with the database

**[21:59]** already configured with the database settings and now when we talk to cloud


### [22:00 - 23:00]

**[22:02]** settings and now when we talk to cloud

**[22:02]** settings and now when we talk to cloud and we ask it a question it can answer

**[22:04]** and we ask it a question it can answer

**[22:04]** and we ask it a question it can answer with that additional graph context that

**[22:06]** with that additional graph context that

**[22:06]** with that additional graph context that it can tell us things. So, I put a few

**[22:07]** it can tell us things. So, I put a few

**[22:07]** it can tell us things. So, I put a few keywords into the MCP server like um

**[22:10]** keywords into the MCP server like um

**[22:10]** keywords into the MCP server like um graph and database and we can ask it um

**[22:13]** graph and database and we can ask it um

**[22:13]** graph and database and we can ask it um what do you know about the Jackson

**[22:15]** what do you know about the Jackson

**[22:16]** what do you know about the Jackson vulnerability

**[22:18]** vulnerability

**[22:18]** vulnerability uh based on your graph database.

**[22:21]** uh based on your graph database.

**[22:21]** uh based on your graph database. And so now in addition to you know

**[22:24]** And so now in addition to you know

**[22:24]** And so now in addition to you know pulling in information from its standard

**[22:26]** pulling in information from its standard

**[22:26]** pulling in information from its standard knowledge sources it's going to use the

**[22:28]** knowledge sources it's going to use the

**[22:28]** knowledge sources it's going to use the NeoRaj MCP server and then query it to

**[22:31]** NeoRaj MCP server and then query it to

**[22:31]** NeoRaj MCP server and then query it to get additional information. And you can

**[22:32]** get additional information. And you can

**[22:32]** get additional information. And you can see that it's doing this multiplestep

**[22:35]** see that it's doing this multiplestep

**[22:35]** see that it's doing this multiplestep plans um search of the graph. So first

**[22:38]** plans um search of the graph. So first

**[22:38]** plans um search of the graph. So first it gets back the schema of the graph so

**[22:40]** it gets back the schema of the graph so

**[22:40]** it gets back the schema of the graph so it can understand the relationships and

**[22:42]** it can understand the relationships and

**[22:42]** it can understand the relationships and how the graph is structured. Now that it

**[22:44]** how the graph is structured. Now that it

**[22:44]** how the graph is structured. Now that it understands the schema of the graph, it

**[22:46]** understands the schema of the graph, it

**[22:46]** understands the schema of the graph, it can go back and it can make a bunch of

**[22:47]** can go back and it can make a bunch of

**[22:47]** can go back and it can make a bunch of queries to get information about the

**[22:49]** queries to get information about the

**[22:49]** queries to get information about the particular vulnerability. So it's firing

**[22:52]** particular vulnerability. So it's firing

**[22:52]** particular vulnerability. So it's firing off a bunch of different cipher queries.

**[22:54]** off a bunch of different cipher queries.

**[22:54]** off a bunch of different cipher queries. Cipher is the um graph query language

**[22:57]** Cipher is the um graph query language

**[22:57]** Cipher is the um graph query language for Neo Forj and most graph databases


### [23:00 - 24:00]

**[23:00]** for Neo Forj and most graph databases

**[23:00]** for Neo Forj and most graph databases support it. It's also now a standard.

**[23:02]** support it. It's also now a standard.

**[23:02]** support it. It's also now a standard. The GQL standard that's ratified by ISO

**[23:05]** The GQL standard that's ratified by ISO

**[23:05]** The GQL standard that's ratified by ISO is um basically a subset of Cipher. And

**[23:09]** is um basically a subset of Cipher. And

**[23:09]** is um basically a subset of Cipher. And now that it got back information about

**[23:11]** now that it got back information about

**[23:11]** now that it got back information about the vulnerabilities, it's pulling back

**[23:13]** the vulnerabilities, it's pulling back

**[23:13]** the vulnerabilities, it's pulling back some of the text chunks to get

**[23:14]** some of the text chunks to get

**[23:14]** some of the text chunks to get additional context which are hanging off

**[23:16]** additional context which are hanging off

**[23:16]** additional context which are hanging off of those nodes. And this way it can give

**[23:19]** of those nodes. And this way it can give

**[23:19]** of those nodes. And this way it can give us a a very complete answer with as much

**[23:22]** us a a very complete answer with as much

**[23:22]** us a a very complete answer with as much information and context as possible from

**[23:24]** information and context as possible from

**[23:24]** information and context as possible from the graph. And the the main difference

**[23:26]** the graph. And the the main difference

**[23:26]** the graph. And the the main difference between this approach where compared to

**[23:29]** between this approach where compared to

**[23:29]** between this approach where compared to the previous one is the previous

**[23:31]** the previous one is the previous

**[23:31]** the previous one is the previous approach was relatively fast but you the

**[23:36]** approach was relatively fast but you the

**[23:36]** approach was relatively fast but you the level of detail it gave us on the CV was

**[23:39]** level of detail it gave us on the CV was

**[23:39]** level of detail it gave us on the CV was limited. When we give a an an agent in

**[23:43]** limited. When we give a an an agent in

**[23:43]** limited. When we give a an an agent in this case we're giving the clawed agent

**[23:44]** this case we're giving the clawed agent

**[23:44]** this case we're giving the clawed agent the ability to kind of have at it for

**[23:47]** the ability to kind of have at it for

**[23:47]** the ability to kind of have at it for the graph do traversals get information

**[23:49]** the graph do traversals get information

**[23:49]** the graph do traversals get information do more traversals you can see that it

**[23:51]** do more traversals you can see that it

**[23:51]** do more traversals you can see that it gives us back very detailed information

**[23:52]** gives us back very detailed information

**[23:52]** gives us back very detailed information about the vulnerability. So it figured

**[23:54]** about the vulnerability. So it figured

**[23:54]** about the vulnerability. So it figured out the CV number, the affected

**[23:56]** out the CV number, the affected

**[23:56]** out the CV number, the affected vulnerability, the type of attack, the

**[23:58]** vulnerability, the type of attack, the

**[23:58]** vulnerability, the type of attack, the severity, and a technical description of


### [24:00 - 25:00]

**[24:00]** severity, and a technical description of

**[24:00]** severity, and a technical description of the attack. So it's a lot more detailed

**[24:02]** the attack. So it's a lot more detailed

**[24:02]** the attack. So it's a lot more detailed than what we got before. And it tells us

**[24:04]** than what we got before. And it tells us

**[24:04]** than what we got before. And it tells us specifically what versions we need to

**[24:06]** specifically what versions we need to

**[24:06]** specifically what versions we need to upgrade to remediate the attack um and

**[24:09]** upgrade to remediate the attack um and

**[24:09]** upgrade to remediate the attack um and gives us some advisory information as

**[24:10]** gives us some advisory information as

**[24:10]** gives us some advisory information as well about this. So um if we were trying

**[24:13]** well about this. So um if we were trying

**[24:13]** well about this. So um if we were trying to develop a um vulnerability report or

**[24:16]** to develop a um vulnerability report or

**[24:16]** to develop a um vulnerability report or something to kind of explain how we

**[24:18]** something to kind of explain how we

**[24:18]** something to kind of explain how we should as an organization um address

**[24:21]** should as an organization um address

**[24:21]** should as an organization um address this vulnerability um using the sort of

**[24:23]** this vulnerability um using the sort of

**[24:23]** this vulnerability um using the sort of agentic multi-step um MCP retrieval

**[24:26]** agentic multi-step um MCP retrieval

**[24:26]** agentic multi-step um MCP retrieval approach is quite powerful because you

**[24:28]** approach is quite powerful because you

**[24:28]** approach is quite powerful because you can see that it gives us um the best

**[24:30]** can see that it gives us um the best

**[24:30]** can see that it gives us um the best possible response since it's able to go

**[24:33]** possible response since it's able to go

**[24:33]** possible response since it's able to go back and keep pulling additional

**[24:34]** back and keep pulling additional

**[24:34]** back and keep pulling additional information from the knowledge graph

**[24:36]** information from the knowledge graph

**[24:36]** information from the knowledge graph that it needs. Okay, so we've seen a few

**[24:39]** that it needs. Okay, so we've seen a few

**[24:39]** that it needs. Okay, so we've seen a few different ways which we can apply

**[24:40]** different ways which we can apply

**[24:40]** different ways which we can apply knowledge graphs to solve and improve

**[24:43]** knowledge graphs to solve and improve

**[24:43]** knowledge graphs to solve and improve the context of our AI applications. So

**[24:47]** the context of our AI applications. So

**[24:47]** the context of our AI applications. So now that we know that we need graphs, we

**[24:48]** now that we know that we need graphs, we

**[24:48]** now that we know that we need graphs, we need we need a lot of graphs. And the

**[24:51]** need we need a lot of graphs. And the

**[24:51]** need we need a lot of graphs. And the best place to find information about

**[24:54]** best place to find information about

**[24:54]** best place to find information about graph technology and getting a lot of

**[24:55]** graph technology and getting a lot of

**[24:55]** graph technology and getting a lot of different use cases for graphs is graph

**[24:57]** different use cases for graphs is graph

**[24:57]** different use cases for graphs is graph academy. It's a entirely free resource

**[24:59]** academy. It's a entirely free resource

**[24:59]** academy. It's a entirely free resource to learn about um both cipher queries.


### [25:00 - 26:00]

**[25:03]** to learn about um both cipher queries.

**[25:03]** to learn about um both cipher queries. It has courses on cypher queries, has

**[25:04]** It has courses on cypher queries, has

**[25:04]** It has courses on cypher queries, has courses on graph rag with examples in

**[25:07]** courses on graph rag with examples in

**[25:07]** courses on graph rag with examples in both Python and TypeScript. Um we have

**[25:09]** both Python and TypeScript. Um we have

**[25:09]** both Python and TypeScript. Um we have some more advanced um graph G gra

**[25:11]** some more advanced um graph G gra

**[25:11]** some more advanced um graph G gra courses coming up as well. So um a lot

**[25:14]** courses coming up as well. So um a lot

**[25:14]** courses coming up as well. So um a lot of information which is all free and

**[25:15]** of information which is all free and

**[25:15]** of information which is all free and very hands-on for you to get started and

**[25:17]** very hands-on for you to get started and

**[25:17]** very hands-on for you to get started and actually build your first application

**[25:18]** actually build your first application

**[25:18]** actually build your first application kind of like the ones which I showed

**[25:20]** kind of like the ones which I showed

**[25:20]** kind of like the ones which I showed here in the presentation. Um now if we

**[25:23]** here in the presentation. Um now if we

**[25:23]** here in the presentation. Um now if we want even more knowledge kind of a wider

**[25:25]** want even more knowledge kind of a wider

**[25:25]** want even more knowledge kind of a wider span we can then go to nodes AI 2026

**[25:29]** span we can then go to nodes AI 2026

**[25:29]** span we can then go to nodes AI 2026 which is our free online virtual

**[25:31]** which is our free online virtual

**[25:31]** which is our free online virtual conference. Um this is following up the

**[25:34]** conference. Um this is following up the

**[25:34]** conference. Um this is following up the amazing nodes conference we had last

**[25:36]** amazing nodes conference we had last

**[25:36]** amazing nodes conference we had last week with um over 13,000 registrants. So

**[25:39]** week with um over 13,000 registrants. So

**[25:39]** week with um over 13,000 registrants. So it was a huge event and Nodes AI is all

**[25:42]** it was a huge event and Nodes AI is all

**[25:42]** it was a huge event and Nodes AI is all about AI for um an entire day with AI

**[25:46]** about AI for um an entire day with AI

**[25:46]** about AI for um an entire day with AI focus sessions. The CFP is open right

**[25:48]** focus sessions. The CFP is open right

**[25:48]** focus sessions. The CFP is open right now if you'd like to submit and it's

**[25:50]** now if you'd like to submit and it's

**[25:50]** now if you'd like to submit and it's free to attend and watch all the

**[25:52]** free to attend and watch all the

**[25:52]** free to attend and watch all the sessions.

**[25:53]** sessions.

**[25:53]** sessions. And if we want to really get down and

**[25:57]** And if we want to really get down and

**[25:57]** And if we want to really get down and you know beat the architect at his own


### [26:00 - 27:00]

**[26:00]** you know beat the architect at his own

**[26:00]** you know beat the architect at his own game, then we need a lot of deep

**[26:03]** game, then we need a lot of deep

**[26:03]** game, then we need a lot of deep research and information. And the best

**[26:05]** research and information. And the best

**[26:05]** research and information. And the best place for that is graphrag.com which is

**[26:07]** place for that is graphrag.com which is

**[26:07]** place for that is graphrag.com which is a community site which we support um

**[26:10]** a community site which we support um

**[26:10]** a community site which we support um where it has all of the latest research

**[26:12]** where it has all of the latest research

**[26:12]** where it has all of the latest research on different graph approaches um how-to

**[26:15]** on different graph approaches um how-to

**[26:15]** on different graph approaches um how-to guides and conceptual information about

**[26:17]** guides and conceptual information about

**[26:18]** guides and conceptual information about how to implement graph rag and just a

**[26:20]** how to implement graph rag and just a

**[26:20]** how to implement graph rag and just a general resource which will help you to

**[26:23]** general resource which will help you to

**[26:23]** general resource which will help you to uplevel your ability to apply graphs to

**[26:26]** uplevel your ability to apply graphs to

**[26:26]** uplevel your ability to apply graphs to different problem domains um with a

**[26:29]** different problem domains um with a

**[26:29]** different problem domains um with a whole bunch of of the cutting edge

**[26:31]** whole bunch of of the cutting edge

**[26:31]** whole bunch of of the cutting edge latest research which is coming out. So,

**[26:33]** latest research which is coming out. So,

**[26:33]** latest research which is coming out. So, um, exciting stuff. Thank you very much

**[26:35]** um, exciting stuff. Thank you very much

**[26:35]** um, exciting stuff. Thank you very much for joining me for the session today.

**[26:38]** for joining me for the session today.

**[26:38]** for joining me for the session today. And I hope you learned a little bit more

**[26:40]** And I hope you learned a little bit more

**[26:40]** And I hope you learned a little bit more about how you can use graphs to connect

**[26:43]** about how you can use graphs to connect

**[26:43]** about how you can use graphs to connect the dots and improve your context

**[26:45]** the dots and improve your context

**[26:45]** the dots and improve your context engineering for your AI applications.


