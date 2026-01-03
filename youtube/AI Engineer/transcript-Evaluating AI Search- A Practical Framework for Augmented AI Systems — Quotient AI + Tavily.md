# Evaluating AI Search- A Practical Framework for Augmented AI Systems — Quotient AI + Tavily

**Video URL:** https://www.youtube.com/watch?v=wRJD0inpmjU

---

## Full Transcript

### [00:00 - 01:00]

**[00:17]** Hi everyone. Uh, thank you so much for

**[00:17]** Hi everyone. Uh, thank you so much for coming. Uh, my name is Julia. I'm CEO

**[00:20]** coming. Uh, my name is Julia. I'm CEO

**[00:20]** coming. Uh, my name is Julia. I'm CEO and co-founder of Quotient AI. Uh, I'm

**[00:23]** and co-founder of Quotient AI. Uh, I'm

**[00:23]** and co-founder of Quotient AI. Uh, I'm Danna Emmery. I am founding AI

**[00:25]** Danna Emmery. I am founding AI

**[00:25]** Danna Emmery. I am founding AI researcher at Quotient AI. My name is

**[00:27]** researcher at Quotient AI. My name is

**[00:27]** researcher at Quotient AI. My name is Mara Sher. I'm head of engineering at

**[00:30]** Mara Sher. I'm head of engineering at

**[00:30]** Mara Sher. I'm head of engineering at and today we are going to talk to you

**[00:32]** and today we are going to talk to you

**[00:32]** and today we are going to talk to you about uh evaluating AI search. So let me

**[00:36]** about uh evaluating AI search. So let me

**[00:36]** about uh evaluating AI search. So let me start with a fundamental challenge we're

**[00:38]** start with a fundamental challenge we're

**[00:38]** start with a fundamental challenge we're all facing in AI today. Traditional

**[00:41]** all facing in AI today. Traditional

**[00:41]** all facing in AI today. Traditional monitoring approaches simply aren't

**[00:42]** monitoring approaches simply aren't

**[00:42]** monitoring approaches simply aren't keeping up with the complexity of modern

**[00:45]** keeping up with the complexity of modern

**[00:45]** keeping up with the complexity of modern AI approaches. First off, these systems

**[00:47]** AI approaches. First off, these systems

**[00:47]** AI approaches. First off, these systems are dynamic. Unlike traditional

**[00:50]** are dynamic. Unlike traditional

**[00:50]** are dynamic. Unlike traditional software, AI agents operate in

**[00:51]** software, AI agents operate in

**[00:51]** software, AI agents operate in constantly changing environments.

**[00:54]** constantly changing environments.

**[00:54]** constantly changing environments. They're not just executing predetermined

**[00:55]** They're not just executing predetermined

**[00:56]** They're not just executing predetermined logic. They're making real-time

**[00:57]** logic. They're making real-time

**[00:57]** logic. They're making real-time decisions based on evolving web content,


### [01:00 - 02:00]

**[01:00]** decisions based on evolving web content,

**[01:00]** decisions based on evolving web content, user interactions, and complex tool

**[01:02]** user interactions, and complex tool

**[01:02]** user interactions, and complex tool chains. The these systems can also have

**[01:05]** chains. The these systems can also have

**[01:05]** chains. The these systems can also have multiple failure modes that happen at

**[01:07]** multiple failure modes that happen at

**[01:07]** multiple failure modes that happen at the same time. They hallucinate,

**[01:09]** the same time. They hallucinate,

**[01:09]** the same time. They hallucinate, retrieval fails, uh they make reasoning

**[01:12]** retrieval fails, uh they make reasoning

**[01:12]** retrieval fails, uh they make reasoning errors and all of these are

**[01:13]** errors and all of these are

**[01:13]** errors and all of these are interconnected.

**[01:15]** interconnected.

**[01:15]** interconnected. A little bit about what we do at

**[01:16]** A little bit about what we do at

**[01:16]** A little bit about what we do at Quotient. We monitor live AI agents. Uh

**[01:19]** Quotient. We monitor live AI agents. Uh

**[01:19]** Quotient. We monitor live AI agents. Uh we have expert evaluators that can

**[01:21]** we have expert evaluators that can

**[01:21]** we have expert evaluators that can detect objective system failures without

**[01:23]** detect objective system failures without

**[01:23]** detect objective system failures without waiting on ground truth data, human

**[01:25]** waiting on ground truth data, human

**[01:25]** waiting on ground truth data, human feedback or benchmarks.

**[01:27]** feedback or benchmarks.

**[01:27]** feedback or benchmarks. A year ago, we met Rom Te's founder and

**[01:30]** A year ago, we met Rom Te's founder and

**[01:30]** A year ago, we met Rom Te's founder and CEO and he posed us with a problem uh

**[01:33]** CEO and he posed us with a problem uh

**[01:33]** CEO and he posed us with a problem uh that really crystallized the core issues

**[01:35]** that really crystallized the core issues

**[01:35]** that really crystallized the core issues we needed to solve.

**[01:37]** we needed to solve.

**[01:37]** we needed to solve. Here's the challenge. How do you build

**[01:39]** Here's the challenge. How do you build

**[01:39]** Here's the challenge. How do you build production readyi search agents when

**[01:41]** production readyi search agents when

**[01:42]** production readyi search agents when your system will be dealing with two

**[01:43]** your system will be dealing with two

**[01:43]** your system will be dealing with two fundamental sources of unpredictability

**[01:45]** fundamental sources of unpredictability

**[01:45]** fundamental sources of unpredictability you cannot proactively control? Under

**[01:48]** you cannot proactively control? Under

**[01:48]** you cannot proactively control? Under the hood, Tavil's agents gathered their

**[01:50]** the hood, Tavil's agents gathered their

**[01:50]** the hood, Tavil's agents gathered their context by searching the web. The web

**[01:52]** context by searching the web. The web

**[01:52]** context by searching the web. The web the web is not static. Traditional

**[01:54]** the web is not static. Traditional

**[01:54]** the web is not static. Traditional benchmarks assume stable ground truth,

**[01:56]** benchmarks assume stable ground truth,

**[01:56]** benchmarks assume stable ground truth, but when you're dealing with real-time

**[01:58]** but when you're dealing with real-time

**[01:58]** but when you're dealing with real-time information, ground through itself is a

**[01:59]** information, ground through itself is a

**[01:59]** information, ground through itself is a moving target. Your users also don't


### [02:00 - 03:00]

**[02:02]** moving target. Your users also don't

**[02:02]** moving target. Your users also don't stick to your test cases. They can ask

**[02:05]** stick to your test cases. They can ask

**[02:05]** stick to your test cases. They can ask odd malformed questions. They have

**[02:07]** odd malformed questions. They have

**[02:07]** odd malformed questions. They have implicit context they don't really share

**[02:09]** implicit context they don't really share

**[02:09]** implicit context they don't really share and you're not aware of. Uh, and this is

**[02:11]** and you're not aware of. Uh, and this is

**[02:11]** and you're not aware of. Uh, and this is not just a theoretical problem. Tavill's

**[02:14]** not just a theoretical problem. Tavill's

**[02:14]** not just a theoretical problem. Tavill's uh Tavilli processes hundreds of

**[02:16]** uh Tavilli processes hundreds of

**[02:16]** uh Tavilli processes hundreds of millions of search requests for its

**[02:18]** millions of search requests for its

**[02:18]** millions of search requests for its agents in production and they need a

**[02:21]** agents in production and they need a

**[02:21]** agents in production and they need a solution that worked at scale in these

**[02:23]** solution that worked at scale in these

**[02:23]** solution that worked at scale in these real world conditions and this is a

**[02:25]** real world conditions and this is a

**[02:25]** real world conditions and this is a story of how we built that.

**[02:33]** Yes. So at Tavilli we're building the

**[02:33]** Yes. So at Tavilli we're building the infrastructure layer for a gent

**[02:35]** infrastructure layer for a gent

**[02:35]** infrastructure layer for a gent interaction at scale essentially

**[02:37]** interaction at scale essentially

**[02:37]** interaction at scale essentially providing language models with real-time

**[02:39]** providing language models with real-time

**[02:39]** providing language models with real-time data from across the web.

**[02:43]** data from across the web.

**[02:43]** data from across the web. There are many use cases where real time

**[02:45]** There are many use cases where real time

**[02:45]** There are many use cases where real time AI search deliver values and this is

**[02:47]** AI search deliver values and this is

**[02:47]** AI search deliver values and this is just a few example of how our clients

**[02:49]** just a few example of how our clients

**[02:49]** just a few example of how our clients are using Tavili to empower their

**[02:51]** are using Tavili to empower their

**[02:51]** are using Tavili to empower their applications. beginning from a CLM

**[02:54]** applications. beginning from a CLM

**[02:54]** applications. beginning from a CLM company that built an AI legal assistant

**[02:56]** company that built an AI legal assistant

**[02:56]** company that built an AI legal assistant to power their legal and business team

**[02:58]** to power their legal and business team

**[02:58]** to power their legal and business team with instant case insight to a sports


### [03:00 - 04:00]

**[03:02]** with instant case insight to a sports

**[03:02]** with instant case insight to a sports news outlet that they created a hybrid

**[03:04]** news outlet that they created a hybrid

**[03:04]** news outlet that they created a hybrid rag chat agent that delivers scores,

**[03:06]** rag chat agent that delivers scores,

**[03:06]** rag chat agent that delivers scores, games, and news updates to a credit card

**[03:10]** games, and news updates to a credit card

**[03:10]** games, and news updates to a credit card company that uses real-time search to uh

**[03:14]** company that uses real-time search to uh

**[03:14]** company that uses real-time search to uh fight fraud by pinpointing merch

**[03:16]** fight fraud by pinpointing merch

**[03:16]** fight fraud by pinpointing merch merchant locations.

**[03:19]** merchant locations.

**[03:19]** merchant locations. So as you can imagine, evaluate a system

**[03:21]** So as you can imagine, evaluate a system

**[03:21]** So as you can imagine, evaluate a system in this kind of vast fastmoving setting

**[03:24]** in this kind of vast fastmoving setting

**[03:24]** in this kind of vast fastmoving setting is quite challenging.

**[03:27]** is quite challenging.

**[03:27]** is quite challenging. We have two principles that guide our

**[03:29]** We have two principles that guide our

**[03:29]** We have two principles that guide our evaluation. First, the web, which is our

**[03:32]** evaluation. First, the web, which is our

**[03:32]** evaluation. First, the web, which is our foundation of our data, is constantly

**[03:34]** foundation of our data, is constantly

**[03:34]** foundation of our data, is constantly changing. This means that our evaluation

**[03:37]** changing. This means that our evaluation

**[03:37]** changing. This means that our evaluation method must keep up with the ongoing

**[03:39]** method must keep up with the ongoing

**[03:39]** method must keep up with the ongoing change.

**[03:41]** change.

**[03:41]** change. Second, that truth is often subjective

**[03:44]** Second, that truth is often subjective

**[03:44]** Second, that truth is often subjective and contextual.

**[03:46]** and contextual.

**[03:46]** and contextual. Evaluating correctness can be tricky

**[03:48]** Evaluating correctness can be tricky

**[03:48]** Evaluating correctness can be tricky because what's right may depend on the

**[03:51]** because what's right may depend on the

**[03:51]** because what's right may depend on the source or the timing or the user needs.

**[03:55]** source or the timing or the user needs.

**[03:55]** source or the timing or the user needs. So we have a responsibility to design

**[03:57]** So we have a responsibility to design

**[03:57]** So we have a responsibility to design our evaluation methods to be as unbiased

**[03:59]** our evaluation methods to be as unbiased

**[03:59]** our evaluation methods to be as unbiased and fair as possible even when absolute


### [04:00 - 05:00]

**[04:02]** and fair as possible even when absolute

**[04:02]** and fair as possible even when absolute truth is hard to pin down.

**[04:05]** truth is hard to pin down.

**[04:05]** truth is hard to pin down. So the first thing to think about in

**[04:07]** So the first thing to think about in

**[04:07]** So the first thing to think about in offline evaluation is which data to use

**[04:10]** offline evaluation is which data to use

**[04:10]** offline evaluation is which data to use to evaluate your system.

**[04:13]** to evaluate your system.

**[04:13]** to evaluate your system. Static data sets are a great start and

**[04:15]** Static data sets are a great start and

**[04:15]** Static data sets are a great start and there are many widely uh open-source

**[04:18]** there are many widely uh open-source

**[04:18]** there are many widely uh open-source data sets available out in the web.

**[04:21]** data sets available out in the web.

**[04:21]** data sets available out in the web. Simple QA is one example. It's a

**[04:23]** Simple QA is one example. It's a

**[04:23]** Simple QA is one example. It's a benchmark and a data sets from open AI

**[04:25]** benchmark and a data sets from open AI

**[04:26]** benchmark and a data sets from open AI that um serve as a standard for

**[04:28]** that um serve as a standard for

**[04:28]** that um serve as a standard for evaluating retrieval accuracy. We have

**[04:31]** evaluating retrieval accuracy. We have

**[04:31]** evaluating retrieval accuracy. We have many many leading AI search providers

**[04:34]** many many leading AI search providers

**[04:34]** many many leading AI search providers that use simple QA to evaluate their

**[04:37]** that use simple QA to evaluate their

**[04:37]** that use simple QA to evaluate their performance. Simple QA is designed to

**[04:39]** performance. Simple QA is designed to

**[04:40]** performance. Simple QA is designed to evaluate a system ability to answer

**[04:42]** evaluate a system ability to answer

**[04:42]** evaluate a system ability to answer short fact-seeking question with a

**[04:45]** short fact-seeking question with a

**[04:45]** short fact-seeking question with a single empirical answer.

**[04:48]** single empirical answer.

**[04:48]** single empirical answer. Another widely uh adopted data set is

**[04:50]** Another widely uh adopted data set is

**[04:50]** Another widely uh adopted data set is hotspot QA which uh tests the which

**[04:53]** hotspot QA which uh tests the which

**[04:53]** hotspot QA which uh tests the which evaluates a system ability to answer

**[04:56]** evaluates a system ability to answer

**[04:56]** evaluates a system ability to answer multihop questions where reasoning

**[04:58]** multihop questions where reasoning

**[04:58]** multihop questions where reasoning across multiple documents is required to


### [05:00 - 06:00]

**[05:01]** across multiple documents is required to

**[05:01]** across multiple documents is required to retrieve the final answer. data set like

**[05:04]** retrieve the final answer. data set like

**[05:04]** retrieve the final answer. data set like simple QA and hotspot QA are a great

**[05:07]** simple QA and hotspot QA are a great

**[05:07]** simple QA and hotspot QA are a great start for evaluating your system. But

**[05:10]** start for evaluating your system. But

**[05:10]** start for evaluating your system. But what happens when you're um when you're

**[05:14]** what happens when you're um when you're

**[05:14]** what happens when you're um when you're evaluating real time um systems that um

**[05:20]** evaluating real time um systems that um

**[05:20]** evaluating real time um systems that um especially when measuring your that your

**[05:22]** especially when measuring your that your

**[05:22]** especially when measuring your that your system keeps up with rapidly evolving

**[05:24]** system keeps up with rapidly evolving

**[05:24]** system keeps up with rapidly evolving information and avoiding regress

**[05:26]** information and avoiding regress

**[05:26]** information and avoiding regress regression like where we operate also

**[05:30]** regression like where we operate also

**[05:30]** regression like where we operate also those kind of static data sets uh don't

**[05:34]** those kind of static data sets uh don't

**[05:34]** those kind of static data sets uh don't address the challenge of benchmarking

**[05:36]** address the challenge of benchmarking

**[05:36]** address the challenge of benchmarking question questions where uh they don't

**[05:39]** question questions where uh they don't

**[05:39]** question questions where uh they don't where there's is no one truth answer or

**[05:42]** where there's is no one truth answer or

**[05:42]** where there's is no one truth answer or subjectivity is involved.

**[05:45]** subjectivity is involved.

**[05:45]** subjectivity is involved. This is what led us to think beyond

**[05:47]** This is what led us to think beyond

**[05:47]** This is what led us to think beyond static data sets towards dynamic

**[05:49]** static data sets towards dynamic

**[05:49]** static data sets towards dynamic evaluation that reflects the changing uh

**[05:55]** evaluation that reflects the changing uh

**[05:55]** evaluation that reflects the changing uh the pace of the of the web. Essentially

**[05:58]** the pace of the of the web. Essentially

**[05:58]** the pace of the of the web. Essentially um dynamic data set are essential for


### [06:00 - 07:00]

**[06:01]** um dynamic data set are essential for

**[06:01]** um dynamic data set are essential for for benchmarking rags in real world

**[06:04]** for benchmarking rags in real world

**[06:04]** for benchmarking rags in real world production system. You can answer

**[06:06]** production system. You can answer

**[06:06]** production system. You can answer today's questions with yesterday data.

**[06:09]** today's questions with yesterday data.

**[06:09]** today's questions with yesterday data. Dynamic data sets have real world

**[06:11]** Dynamic data sets have real world

**[06:11]** Dynamic data sets have real world alignment. They have broad coverage as

**[06:15]** alignment. They have broad coverage as

**[06:15]** alignment. They have broad coverage as you can easily create evil sets for any

**[06:18]** you can easily create evil sets for any

**[06:18]** you can easily create evil sets for any domain or use case that is relevant to

**[06:20]** domain or use case that is relevant to

**[06:20]** domain or use case that is relevant to your specific needs. And they also

**[06:23]** your specific needs. And they also

**[06:23]** your specific needs. And they also ensure continuous relevancy because they

**[06:25]** ensure continuous relevancy because they

**[06:25]** ensure continuous relevancy because they are regularly refresh which means that

**[06:27]** are regularly refresh which means that

**[06:27]** are regularly refresh which means that your system is con is always evaluated

**[06:30]** your system is con is always evaluated

**[06:30]** your system is con is always evaluated against the latest data.

**[06:37]** This led us to build an open-source um

**[06:37]** This led us to build an open-source um agent that basically build dynamic eval

**[06:41]** agent that basically build dynamic eval

**[06:41]** agent that basically build dynamic eval sets for web-based rug system. It's open

**[06:44]** sets for web-based rug system. It's open

**[06:44]** sets for web-based rug system. It's open source and we encourage everyone to

**[06:47]** source and we encourage everyone to

**[06:47]** source and we encourage everyone to check it out and contribute.

**[06:50]** check it out and contribute.

**[06:50]** check it out and contribute. And I also want to acknowledge the work

**[06:51]** And I also want to acknowledge the work

**[06:51]** And I also want to acknowledge the work of Ayal, our head of data at Savili, who

**[06:54]** of Ayal, our head of data at Savili, who

**[06:54]** of Ayal, our head of data at Savili, who initiated this project a couple months

**[06:56]** initiated this project a couple months

**[06:56]** initiated this project a couple months ago.

**[06:57]** ago.

**[06:57]** ago. As you can see here, an example of a

**[06:59]** As you can see here, an example of a


### [07:00 - 08:00]

**[07:00]** As you can see here, an example of a data set generated by the agent. It

**[07:03]** data set generated by the agent. It

**[07:03]** data set generated by the agent. It generates question and answer pairs for

**[07:05]** generates question and answer pairs for

**[07:05]** generates question and answer pairs for targeted domains using information found

**[07:07]** targeted domains using information found

**[07:07]** targeted domains using information found in the web.

**[07:13]** So the agent leverage the langraph

**[07:13]** So the agent leverage the langraph framework and it consists of these key

**[07:16]** framework and it consists of these key

**[07:16]** framework and it consists of these key steps. First it generates broad web

**[07:19]** steps. First it generates broad web

**[07:19]** steps. First it generates broad web search queries for targeted domains

**[07:21]** search queries for targeted domains

**[07:21]** search queries for targeted domains which essentially let you create eval

**[07:24]** which essentially let you create eval

**[07:24]** which essentially let you create eval sets for any uh domain of your choice

**[07:27]** sets for any uh domain of your choice

**[07:27]** sets for any uh domain of your choice and specific need of your application.

**[07:30]** and specific need of your application.

**[07:30]** and specific need of your application. The second step is to aggregorate

**[07:32]** The second step is to aggregorate

**[07:32]** The second step is to aggregorate grounding documents from multiple

**[07:34]** grounding documents from multiple

**[07:34]** grounding documents from multiple real-time AI search providers. We

**[07:37]** real-time AI search providers. We

**[07:37]** real-time AI search providers. We understand that we cannot just use

**[07:39]** understand that we cannot just use

**[07:39]** understand that we cannot just use Tavili to search the web on specific

**[07:41]** Tavili to search the web on specific

**[07:41]** Tavili to search the web on specific domains, find grounding documents, then

**[07:44]** domains, find grounding documents, then

**[07:44]** domains, find grounding documents, then generate question and answer pairs from

**[07:46]** generate question and answer pairs from

**[07:46]** generate question and answer pairs from those documents and then evaluate our

**[07:48]** those documents and then evaluate our

**[07:48]** those documents and then evaluate our performance on those documents. That's

**[07:51]** performance on those documents. That's

**[07:51]** performance on those documents. That's why we use multiple real-time AI search

**[07:54]** why we use multiple real-time AI search

**[07:54]** why we use multiple real-time AI search providers to both maximize coverage and

**[07:56]** providers to both maximize coverage and

**[07:56]** providers to both maximize coverage and minimize bias.

**[07:59]** minimize bias.

**[07:59]** minimize bias. The third step which is the key uh step


### [08:00 - 09:00]

**[08:02]** The third step which is the key uh step

**[08:02]** The third step which is the key uh step in this process is to generate the

**[08:04]** in this process is to generate the

**[08:04]** in this process is to generate the evidencebased question and answer pairs.

**[08:07]** evidencebased question and answer pairs.

**[08:07]** evidencebased question and answer pairs. And we ensure that in the generation

**[08:09]** And we ensure that in the generation

**[08:09]** And we ensure that in the generation process the agent is obliged to to

**[08:12]** process the agent is obliged to to

**[08:12]** process the agent is obliged to to generate answer context which al which

**[08:14]** generate answer context which al which

**[08:14]** generate answer context which al which also increase the reliability of our

**[08:17]** also increase the reliability of our

**[08:17]** also increase the reliability of our question and answer pairs and reduce

**[08:18]** question and answer pairs and reduce

**[08:18]** question and answer pairs and reduce hallucinations.

**[08:20]** hallucinations.

**[08:20]** hallucinations. You can always go back and and check

**[08:23]** You can always go back and and check

**[08:23]** You can always go back and and check which sources were used and which

**[08:24]** which sources were used and which

**[08:24]** which sources were used and which evidence from so those sources were used

**[08:27]** evidence from so those sources were used

**[08:27]** evidence from so those sources were used to generate each question and answer

**[08:29]** to generate each question and answer

**[08:29]** to generate each question and answer pair. And lastly, we use length miss to

**[08:31]** pair. And lastly, we use length miss to

**[08:32]** pair. And lastly, we use length miss to track our experiments which is a great

**[08:34]** track our experiments which is a great

**[08:34]** track our experiments which is a great observability tool to manage these uh

**[08:37]** observability tool to manage these uh

**[08:37]** observability tool to manage these uh offline um evaluation runs and see how

**[08:41]** offline um evaluation runs and see how

**[08:41]** offline um evaluation runs and see how your performance at different time

**[08:43]** your performance at different time

**[08:43]** your performance at different time steps.

**[08:44]** steps.

**[08:44]** steps. The next steps that we want to address

**[08:46]** The next steps that we want to address

**[08:46]** The next steps that we want to address is to support a range of question types

**[08:49]** is to support a range of question types

**[08:49]** is to support a range of question types both simple factbased questions and

**[08:52]** both simple factbased questions and

**[08:52]** both simple factbased questions and multi-hop questions similar to the

**[08:55]** multi-hop questions similar to the

**[08:55]** multi-hop questions similar to the hotspot QA. We also want to ensure

**[08:58]** hotspot QA. We also want to ensure

**[08:58]** hotspot QA. We also want to ensure furnish and fairness and coverage by


### [09:00 - 10:00]

**[09:02]** furnish and fairness and coverage by

**[09:02]** furnish and fairness and coverage by proactively addressing bias and covering

**[09:04]** proactively addressing bias and covering

**[09:04]** proactively addressing bias and covering a wide range of perspective for each

**[09:07]** a wide range of perspective for each

**[09:07]** a wide range of perspective for each subject we generate question and answer

**[09:09]** subject we generate question and answer

**[09:09]** subject we generate question and answer to.

**[09:11]** to.

**[09:11]** to. Additionally, we want to add a

**[09:13]** Additionally, we want to add a

**[09:13]** Additionally, we want to add a supervisor node for coordination which

**[09:15]** supervisor node for coordination which

**[09:15]** supervisor node for coordination which prove itself to be valuable especially

**[09:17]** prove itself to be valuable especially

**[09:18]** prove itself to be valuable especially in these multi- aents uh architectures

**[09:20]** in these multi- aents uh architectures

**[09:20]** in these multi- aents uh architectures and this will increase the quality of

**[09:22]** and this will increase the quality of

**[09:22]** and this will increase the quality of our question and answer pairs.

**[09:26]** our question and answer pairs.

**[09:26]** our question and answer pairs. The next step to think about is uh

**[09:29]** The next step to think about is uh

**[09:29]** The next step to think about is uh benchmarking and we argue that it's

**[09:32]** benchmarking and we argue that it's

**[09:32]** benchmarking and we argue that it's important to measure accuracy but you

**[09:34]** important to measure accuracy but you

**[09:34]** important to measure accuracy but you should not stop there. You should ensure

**[09:36]** should not stop there. You should ensure

**[09:36]** should not stop there. You should ensure an holistic evaluation framework which

**[09:39]** an holistic evaluation framework which

**[09:39]** an holistic evaluation framework which use benchmark like for for our case that

**[09:42]** use benchmark like for for our case that

**[09:42]** use benchmark like for for our case that um measure your your source diversity

**[09:45]** um measure your your source diversity

**[09:46]** um measure your your source diversity your uh source relevancy and hallucation

**[09:49]** your uh source relevancy and hallucation

**[09:49]** your uh source relevancy and hallucation rates. It's also important to leverage

**[09:51]** rates. It's also important to leverage

**[09:51]** rates. It's also important to leverage unsupervised evaluation method that

**[09:53]** unsupervised evaluation method that

**[09:53]** unsupervised evaluation method that remove the need for label for label data

**[09:56]** remove the need for label for label data

**[09:56]** remove the need for label for label data which enable to scale your evaluations

**[09:59]** which enable to scale your evaluations

**[09:59]** which enable to scale your evaluations and address the subjectivity uh issue.


### [10:00 - 11:00]

**[10:03]** and address the subjectivity uh issue.

**[10:03]** and address the subjectivity uh issue. With that, I'll pass it over to Diana

**[10:05]** With that, I'll pass it over to Diana

**[10:05]** With that, I'll pass it over to Diana who who will explain more about this

**[10:07]** who who will explain more about this

**[10:07]** who who will explain more about this reference free benchmarks and also share

**[10:10]** reference free benchmarks and also share

**[10:10]** reference free benchmarks and also share a results from uh an experiment we ran

**[10:13]** a results from uh an experiment we ran

**[10:13]** a results from uh an experiment we ran using a static and a dynamic data set

**[10:15]** using a static and a dynamic data set

**[10:15]** using a static and a dynamic data set that was generated by the agent I

**[10:17]** that was generated by the agent I

**[10:17]** that was generated by the agent I described before.

**[10:21]** described before.

**[10:21]** described before. So, uh we performed a two-part

**[10:23]** So, uh we performed a two-part

**[10:23]** So, uh we performed a two-part evaluation of six different AI search

**[10:26]** evaluation of six different AI search

**[10:26]** evaluation of six different AI search providers. Um the first component of

**[10:29]** providers. Um the first component of

**[10:29]** providers. Um the first component of this experiment was to compare the

**[10:32]** this experiment was to compare the

**[10:32]** this experiment was to compare the accuracy of search providers on a static

**[10:35]** accuracy of search providers on a static

**[10:35]** accuracy of search providers on a static and a dynamic benchmark in order to

**[10:37]** and a dynamic benchmark in order to

**[10:37]** and a dynamic benchmark in order to demonstrate that static benchmarking is

**[10:40]** demonstrate that static benchmarking is

**[10:40]** demonstrate that static benchmarking is not a comprehensive method for

**[10:41]** not a comprehensive method for

**[10:41]** not a comprehensive method for evaluation of AI search. The second

**[10:44]** evaluation of AI search. The second

**[10:44]** evaluation of AI search. The second component was to evaluate the uh dynamic

**[10:48]** component was to evaluate the uh dynamic

**[10:48]** component was to evaluate the uh dynamic data set responses using reference free

**[10:51]** data set responses using reference free

**[10:51]** data set responses using reference free metrics and we compare these results to

**[10:54]** metrics and we compare these results to

**[10:54]** metrics and we compare these results to the uh reference based accuracies that

**[10:57]** the uh reference based accuracies that

**[10:57]** the uh reference based accuracies that we get from the benchmark in order to

**[10:59]** we get from the benchmark in order to

**[10:59]** we get from the benchmark in order to demonstrate that reference reevaluation


### [11:00 - 12:00]

**[11:02]** demonstrate that reference reevaluation

**[11:02]** demonstrate that reference reevaluation can be an effective substitute when

**[11:04]** can be an effective substitute when

**[11:04]** can be an effective substitute when ground truths are not available.

**[11:07]** ground truths are not available.

**[11:07]** ground truths are not available. So jumping right in um for our static

**[11:10]** So jumping right in um for our static

**[11:10]** So jumping right in um for our static versus dynamic benchmarking comparison

**[11:13]** versus dynamic benchmarking comparison

**[11:13]** versus dynamic benchmarking comparison we use simple QA benchmark as the static

**[11:16]** we use simple QA benchmark as the static

**[11:16]** we use simple QA benchmark as the static data set and we're using a dynamic

**[11:18]** data set and we're using a dynamic

**[11:18]** data set and we're using a dynamic benchmark of about a thousand rows

**[11:20]** benchmark of about a thousand rows

**[11:20]** benchmark of about a thousand rows created by Tivi

**[11:23]** created by Tivi

**[11:23]** created by Tivi and as you can see here uh both data

**[11:25]** and as you can see here uh both data

**[11:25]** and as you can see here uh both data sets have roughly similar distributions

**[11:27]** sets have roughly similar distributions

**[11:27]** sets have roughly similar distributions of topics and this helps to ensure a

**[11:29]** of topics and this helps to ensure a

**[11:29]** of topics and this helps to ensure a fair comparison and diversity of

**[11:31]** fair comparison and diversity of

**[11:31]** fair comparison and diversity of questions

**[11:33]** questions

**[11:33]** questions to evaluate the AI search providers.

**[11:36]** to evaluate the AI search providers.

**[11:36]** to evaluate the AI search providers. performance on these two benchmarks.

**[11:38]** performance on these two benchmarks.

**[11:38]** performance on these two benchmarks. We're using the simple QA correctness

**[11:40]** We're using the simple QA correctness

**[11:40]** We're using the simple QA correctness metric and this is an LLM judge which is

**[11:44]** metric and this is an LLM judge which is

**[11:44]** metric and this is an LLM judge which is used on the simple QA benchmark. It

**[11:47]** used on the simple QA benchmark. It

**[11:47]** used on the simple QA benchmark. It compares the model's response against a

**[11:50]** compares the model's response against a

**[11:50]** compares the model's response against a ground truth answer in order to

**[11:51]** ground truth answer in order to

**[11:51]** ground truth answer in order to determine if it's correct, incorrect, or

**[11:54]** determine if it's correct, incorrect, or

**[11:54]** determine if it's correct, incorrect, or not attempted.

**[11:57]** not attempted.

**[11:57]** not attempted. And so here we're showing the

**[11:59]** And so here we're showing the

**[11:59]** And so here we're showing the correctness scores from that simple QA


### [12:00 - 13:00]

**[12:01]** correctness scores from that simple QA

**[12:01]** correctness scores from that simple QA benchmark compared against the dynamic

**[12:03]** benchmark compared against the dynamic

**[12:03]** benchmark compared against the dynamic benchmark. And uh we've anonymized the

**[12:06]** benchmark. And uh we've anonymized the

**[12:06]** benchmark. And uh we've anonymized the search providers for this talk. Um but I

**[12:08]** search providers for this talk. Um but I

**[12:08]** search providers for this talk. Um but I do want to call out that the simple QA

**[12:11]** do want to call out that the simple QA

**[12:11]** do want to call out that the simple QA accuracy scores here are all

**[12:12]** accuracy scores here are all

**[12:12]** accuracy scores here are all self-reported and so they don't all

**[12:14]** self-reported and so they don't all

**[12:14]** self-reported and so they don't all necessarily have clear documentation on

**[12:16]** necessarily have clear documentation on

**[12:16]** necessarily have clear documentation on how they were calculated. But um as you

**[12:19]** how they were calculated. But um as you

**[12:20]** how they were calculated. But um as you can see the correctness scores are for

**[12:22]** can see the correctness scores are for

**[12:22]** can see the correctness scores are for the dynamic benchmark in blue are

**[12:24]** the dynamic benchmark in blue are

**[12:24]** the dynamic benchmark in blue are substantially lower. Um and not only

**[12:27]** substantially lower. Um and not only

**[12:27]** substantially lower. Um and not only that the relative rankings have also

**[12:30]** that the relative rankings have also

**[12:30]** that the relative rankings have also changed pretty considerably. For

**[12:31]** changed pretty considerably. For

**[12:32]** changed pretty considerably. For example, um, provider F all the way on

**[12:34]** example, um, provider F all the way on

**[12:34]** example, um, provider F all the way on the end of this plot here performs the

**[12:36]** the end of this plot here performs the

**[12:36]** the end of this plot here performs the worst on simple QA, but it performs the

**[12:39]** worst on simple QA, but it performs the

**[12:39]** worst on simple QA, but it performs the best on the dynamic benchmark.

**[12:45]** Looking a little closer to the in the

**[12:45]** Looking a little closer to the in the results, um, while this simple QA

**[12:48]** results, um, while this simple QA

**[12:48]** results, um, while this simple QA evaluator is useful, it's certainly far

**[12:51]** evaluator is useful, it's certainly far

**[12:51]** evaluator is useful, it's certainly far from perfect. Um, I have a few examples

**[12:53]** from perfect. Um, I have a few examples

**[12:53]** from perfect. Um, I have a few examples here of, um, model responses that were

**[12:57]** here of, um, model responses that were

**[12:57]** here of, um, model responses that were flagged as incorrect by this LLM judge.


### [13:00 - 14:00]

**[13:00]** flagged as incorrect by this LLM judge.

**[13:00]** flagged as incorrect by this LLM judge. Uh but if you look at the actual text in

**[13:02]** Uh but if you look at the actual text in

**[13:02]** Uh but if you look at the actual text in the model outputs, they do contain the

**[13:04]** the model outputs, they do contain the

**[13:04]** the model outputs, they do contain the correct answer from the ground truth.

**[13:07]** correct answer from the ground truth.

**[13:07]** correct answer from the ground truth. On the flip side of things, um here is

**[13:09]** On the flip side of things, um here is

**[13:09]** On the flip side of things, um here is an example where uh the LLM judge

**[13:12]** an example where uh the LLM judge

**[13:12]** an example where uh the LLM judge classified it as correct. And yes, you

**[13:14]** classified it as correct. And yes, you

**[13:14]** classified it as correct. And yes, you can see that the correct answer is in

**[13:16]** can see that the correct answer is in

**[13:16]** can see that the correct answer is in this response.

**[13:18]** this response.

**[13:18]** this response. But while the correct answer might be

**[13:20]** But while the correct answer might be

**[13:20]** But while the correct answer might be present, that doesn't necessarily mean

**[13:22]** present, that doesn't necessarily mean

**[13:22]** present, that doesn't necessarily mean that the full answer is right. Um this

**[13:25]** that the full answer is right. Um this

**[13:25]** that the full answer is right. Um this evaluation is not accounting for any of

**[13:27]** evaluation is not accounting for any of

**[13:27]** evaluation is not accounting for any of the additional text in this response.

**[13:29]** the additional text in this response.

**[13:29]** the additional text in this response. and there might be hallucinations in

**[13:31]** and there might be hallucinations in

**[13:31]** and there might be hallucinations in there and that would invalidate it. So

**[13:34]** there and that would invalidate it. So

**[13:34]** there and that would invalidate it. So ultimately this evaluation falls short

**[13:37]** ultimately this evaluation falls short

**[13:37]** ultimately this evaluation falls short of identifying when things go wrong in

**[13:39]** of identifying when things go wrong in

**[13:39]** of identifying when things go wrong in AI search.

**[13:41]** AI search.

**[13:41]** AI search. So what are some other ways that we can

**[13:44]** So what are some other ways that we can

**[13:44]** So what are some other ways that we can identify when things go wrong? Up to

**[13:46]** identify when things go wrong? Up to

**[13:46]** identify when things go wrong? Up to this point we have been talking about a

**[13:48]** this point we have been talking about a

**[13:48]** this point we have been talking about a reference-based approach to evaluation.

**[13:50]** reference-based approach to evaluation.

**[13:50]** reference-based approach to evaluation. But what if we don't have ground truths?

**[13:53]** But what if we don't have ground truths?

**[13:53]** But what if we don't have ground truths? In most online and production settings

**[13:55]** In most online and production settings

**[13:55]** In most online and production settings this is typically the case. And as we've

**[13:58]** this is typically the case. And as we've

**[13:58]** this is typically the case. And as we've already discussed, it's especially so in

**[13:59]** already discussed, it's especially so in

**[13:59]** already discussed, it's especially so in AI search. Um, so the question is, can


### [14:00 - 15:00]

**[14:03]** AI search. Um, so the question is, can

**[14:03]** AI search. Um, so the question is, can reference free metrics effectively

**[14:06]** reference free metrics effectively

**[14:06]** reference free metrics effectively identify issues in AI search? For this

**[14:09]** identify issues in AI search? For this

**[14:09]** identify issues in AI search? For this talk, we're going to look at three of

**[14:11]** talk, we're going to look at three of

**[14:11]** talk, we're going to look at three of quotient's reference free metrics. Um,

**[14:14]** quotient's reference free metrics. Um,

**[14:14]** quotient's reference free metrics. Um, we'll look at answer completeness, which

**[14:17]** we'll look at answer completeness, which

**[14:17]** we'll look at answer completeness, which identifies whether all components of the

**[14:19]** identifies whether all components of the

**[14:19]** identifies whether all components of the question were answered. Um, so it

**[14:21]** question were answered. Um, so it

**[14:21]** question were answered. Um, so it classifies model responses as either

**[14:23]** classifies model responses as either

**[14:23]** classifies model responses as either fully addressed, unadressed, or unknown.

**[14:27]** fully addressed, unadressed, or unknown.

**[14:27]** fully addressed, unadressed, or unknown. Uh, if the model says I don't know, then

**[14:29]** Uh, if the model says I don't know, then

**[14:29]** Uh, if the model says I don't know, then we'll look at document relevance, and

**[14:32]** we'll look at document relevance, and

**[14:32]** we'll look at document relevance, and this is the percent of the retrieved

**[14:34]** this is the percent of the retrieved

**[14:34]** this is the percent of the retrieved documents that are actually relevant to

**[14:35]** documents that are actually relevant to

**[14:35]** documents that are actually relevant to addressing the question. Um, and then

**[14:38]** addressing the question. Um, and then

**[14:38]** addressing the question. Um, and then finally, we'll look at hallucination

**[14:40]** finally, we'll look at hallucination

**[14:40]** finally, we'll look at hallucination detection, which identifies whether

**[14:42]** detection, which identifies whether

**[14:42]** detection, which identifies whether there are any facts in the model

**[14:44]** there are any facts in the model

**[14:44]** there are any facts in the model response that are not present in any of

**[14:47]** response that are not present in any of

**[14:47]** response that are not present in any of the retrieved documents. And so we use

**[14:50]** the retrieved documents. And so we use

**[14:50]** the retrieved documents. And so we use these metrics to evaluate the search

**[14:52]** these metrics to evaluate the search

**[14:52]** these metrics to evaluate the search provider's responses on this dynamic

**[14:55]** provider's responses on this dynamic

**[14:55]** provider's responses on this dynamic benchmark.


### [15:00 - 16:00]

**[15:00]** So we've got answer completeness plotted

**[15:00]** So we've got answer completeness plotted here. Um the stacked bar plot shows the

**[15:02]** here. Um the stacked bar plot shows the

**[15:02]** here. Um the stacked bar plot shows the number of responses that were either

**[15:04]** number of responses that were either

**[15:04]** number of responses that were either completely answered uh unressed or

**[15:07]** completely answered uh unressed or

**[15:07]** completely answered uh unressed or marked as unknown.

**[15:09]** marked as unknown.

**[15:09]** marked as unknown. And if we look back at the overall

**[15:12]** And if we look back at the overall

**[15:12]** And if we look back at the overall rankings that we saw earlier on the

**[15:14]** rankings that we saw earlier on the

**[15:14]** rankings that we saw earlier on the dynamic benchmark, um you can see that

**[15:16]** dynamic benchmark, um you can see that

**[15:16]** dynamic benchmark, um you can see that the rankings from answer completeness

**[15:18]** the rankings from answer completeness

**[15:18]** the rankings from answer completeness pretty closely match. Um the average

**[15:20]** pretty closely match. Um the average

**[15:20]** pretty closely match. Um the average performance scores for the two get a

**[15:23]** performance scores for the two get a

**[15:23]** performance scores for the two get a correlation of 0.94.

**[15:25]** correlation of 0.94.

**[15:25]** correlation of 0.94. So this indicates that the reference

**[15:27]** So this indicates that the reference

**[15:27]** So this indicates that the reference free metric can capture relative

**[15:30]** free metric can capture relative

**[15:30]** free metric can capture relative performance pretty well. But

**[15:32]** performance pretty well. But

**[15:32]** performance pretty well. But completeness is still not the same thing

**[15:34]** completeness is still not the same thing

**[15:34]** completeness is still not the same thing as correctness. Um and when we have no

**[15:37]** as correctness. Um and when we have no

**[15:37]** as correctness. Um and when we have no ground truths available then we have to

**[15:39]** ground truths available then we have to

**[15:39]** ground truths available then we have to turn to the next best thing and that is

**[15:42]** turn to the next best thing and that is

**[15:42]** turn to the next best thing and that is the grounding documents.

**[15:44]** the grounding documents.

**[15:44]** the grounding documents. So this is where document relevance and

**[15:47]** So this is where document relevance and

**[15:47]** So this is where document relevance and hallucination detection come in. Uh both

**[15:49]** hallucination detection come in. Uh both

**[15:49]** hallucination detection come in. Uh both of these metrics are going to be looking

**[15:51]** of these metrics are going to be looking

**[15:51]** of these metrics are going to be looking at those grounding documents in order to

**[15:53]** at those grounding documents in order to

**[15:53]** at those grounding documents in order to measure the quality of the model's

**[15:55]** measure the quality of the model's

**[15:55]** measure the quality of the model's response.

**[15:56]** response.

**[15:56]** response. Unfortunately, uh, of all of the search

**[15:59]** Unfortunately, uh, of all of the search

**[15:59]** Unfortunately, uh, of all of the search providers we looked at, only three of


### [16:00 - 17:00]

**[16:01]** providers we looked at, only three of

**[16:01]** providers we looked at, only three of them actually return the retrieved

**[16:02]** them actually return the retrieved

**[16:02]** them actually return the retrieved documents used to generate their

**[16:04]** documents used to generate their

**[16:04]** documents used to generate their answers. Um, the majority of search

**[16:06]** answers. Um, the majority of search

**[16:06]** answers. Um, the majority of search providers typically only provide

**[16:08]** providers typically only provide

**[16:08]** providers typically only provide citations and these are largely

**[16:11]** citations and these are largely

**[16:11]** citations and these are largely unhelpful at scale and also really limit

**[16:13]** unhelpful at scale and also really limit

**[16:14]** unhelpful at scale and also really limit transparency when it comes to debugging.

**[16:21]** So, these are those document relevance

**[16:21]** So, these are those document relevance scores for the three search providers.

**[16:23]** scores for the three search providers.

**[16:23]** scores for the three search providers. Um, and they've been reanomized here. Um

**[16:26]** Um, and they've been reanomized here. Um

**[16:26]** Um, and they've been reanomized here. Um the plot to the left shows the average

**[16:29]** the plot to the left shows the average

**[16:29]** the plot to the left shows the average document relevance, the percent of

**[16:31]** document relevance, the percent of

**[16:31]** document relevance, the percent of retrieved documents that are relevant to

**[16:33]** retrieved documents that are relevant to

**[16:33]** retrieved documents that are relevant to the question. And the plot to the right

**[16:35]** the question. And the plot to the right

**[16:36]** the question. And the plot to the right shows the number of responses that have

**[16:38]** shows the number of responses that have

**[16:38]** shows the number of responses that have no relevant documents.

**[16:40]** no relevant documents.

**[16:40]** no relevant documents. And if we consider these results in

**[16:42]** And if we consider these results in

**[16:42]** And if we consider these results in conjunction with answer completeness, we

**[16:46]** conjunction with answer completeness, we

**[16:46]** conjunction with answer completeness, we find that there's a strong inverse

**[16:47]** find that there's a strong inverse

**[16:47]** find that there's a strong inverse correlation between document relevance

**[16:50]** correlation between document relevance

**[16:50]** correlation between document relevance and the number of unknown answers. And

**[16:52]** and the number of unknown answers. And

**[16:52]** and the number of unknown answers. And this kind of matches intuition. uh if

**[16:55]** this kind of matches intuition. uh if

**[16:55]** this kind of matches intuition. uh if you think about it, if you have no

**[16:57]** you think about it, if you have no

**[16:57]** you think about it, if you have no grounding, no relevant documents for the

**[16:59]** grounding, no relevant documents for the

**[16:59]** grounding, no relevant documents for the question, the model should say I don't


### [17:00 - 18:00]

**[17:00]** question, the model should say I don't

**[17:00]** question, the model should say I don't know rather than trying to answer it.

**[17:04]** know rather than trying to answer it.

**[17:04]** know rather than trying to answer it. And so this brings us to hallucination

**[17:07]** And so this brings us to hallucination

**[17:07]** And so this brings us to hallucination detection. And here we were actually

**[17:09]** detection. And here we were actually

**[17:09]** detection. And here we were actually surprised to see that there was a direct

**[17:12]** surprised to see that there was a direct

**[17:12]** surprised to see that there was a direct relationship with the hallucination rate

**[17:14]** relationship with the hallucination rate

**[17:14]** relationship with the hallucination rate and document relevance. Provider X here

**[17:18]** and document relevance. Provider X here

**[17:18]** and document relevance. Provider X here has the highest hallucination rate, but

**[17:21]** has the highest hallucination rate, but

**[17:21]** has the highest hallucination rate, but it also had the highest overall document

**[17:23]** it also had the highest overall document

**[17:23]** it also had the highest overall document relevance. And this is kind of

**[17:25]** relevance. And this is kind of

**[17:25]** relevance. And this is kind of counterintuitive. Um, but if we think

**[17:27]** counterintuitive. Um, but if we think

**[17:27]** counterintuitive. Um, but if we think about it more, provider X had high

**[17:31]** about it more, provider X had high

**[17:31]** about it more, provider X had high answer completeness, the lowest rate of

**[17:34]** answer completeness, the lowest rate of

**[17:34]** answer completeness, the lowest rate of unknown answers, and it also had the

**[17:37]** unknown answers, and it also had the

**[17:37]** unknown answers, and it also had the highest answer correctness from the

**[17:39]** highest answer correctness from the

**[17:40]** highest answer correctness from the benchmarking earlier of these three

**[17:41]** benchmarking earlier of these three

**[17:41]** benchmarking earlier of these three providers.

**[17:43]** providers.

**[17:43]** providers. So, this probably implies that maybe in

**[17:46]** So, this probably implies that maybe in

**[17:46]** So, this probably implies that maybe in provider X's responses, um, they're more

**[17:50]** provider X's responses, um, they're more

**[17:50]** provider X's responses, um, they're more likely to provide new reasoning or

**[17:51]** likely to provide new reasoning or

**[17:52]** likely to provide new reasoning or interpretations in their response, or

**[17:54]** interpretations in their response, or

**[17:54]** interpretations in their response, or maybe even they're more detailed and

**[17:56]** maybe even they're more detailed and

**[17:56]** maybe even they're more detailed and thorough, and this just creates more

**[17:58]** thorough, and this just creates more

**[17:58]** thorough, and this just creates more opportunity for hallucination in their


### [18:00 - 19:00]

**[18:00]** opportunity for hallucination in their

**[18:00]** opportunity for hallucination in their responses. Um, but the point I want to

**[18:02]** responses. Um, but the point I want to

**[18:02]** responses. Um, but the point I want to make here is that when considering these

**[18:05]** make here is that when considering these

**[18:05]** make here is that when considering these metrics, depending on your use case, you

**[18:08]** metrics, depending on your use case, you

**[18:08]** metrics, depending on your use case, you might index more heavily on one over

**[18:10]** might index more heavily on one over

**[18:10]** might index more heavily on one over another. um they're measuring different

**[18:12]** another. um they're measuring different

**[18:12]** another. um they're measuring different dimensions of response quality and it's

**[18:14]** dimensions of response quality and it's

**[18:14]** dimensions of response quality and it's often a give and take. If you perform

**[18:16]** often a give and take. If you perform

**[18:16]** often a give and take. If you perform really well in one, it might be at the

**[18:18]** really well in one, it might be at the

**[18:18]** really well in one, it might be at the expense of another. Um and as we see

**[18:21]** expense of another. Um and as we see

**[18:21]** expense of another. Um and as we see here, uh there is a trade-off between

**[18:23]** here, uh there is a trade-off between

**[18:23]** here, uh there is a trade-off between complete answer completeness and

**[18:25]** complete answer completeness and

**[18:25]** complete answer completeness and hallucination.

**[18:31]** But also, um if you take these three

**[18:31]** But also, um if you take these three metrics in conjunction, you can use them

**[18:33]** metrics in conjunction, you can use them

**[18:33]** metrics in conjunction, you can use them to understand why things went wrong and

**[18:36]** to understand why things went wrong and

**[18:36]** to understand why things went wrong and uh identify potential strategies for

**[18:39]** uh identify potential strategies for

**[18:39]** uh identify potential strategies for addressing those issues. This diagram

**[18:41]** addressing those issues. This diagram

**[18:41]** addressing those issues. This diagram here shows a few examples on how you can

**[18:44]** here shows a few examples on how you can

**[18:44]** here shows a few examples on how you can interpret your evaluation results. Um

**[18:48]** interpret your evaluation results. Um

**[18:48]** interpret your evaluation results. Um sorry uh how you can interpret your

**[18:50]** sorry uh how you can interpret your

**[18:50]** sorry uh how you can interpret your evaluation results to identify what to

**[18:52]** evaluation results to identify what to

**[18:52]** evaluation results to identify what to do to fix it. So we've got one example

**[18:54]** do to fix it. So we've got one example

**[18:54]** do to fix it. So we've got one example here where um maybe your response is

**[18:57]** here where um maybe your response is

**[18:57]** here where um maybe your response is incomplete um but you have relevant


### [19:00 - 20:00]

**[19:00]** incomplete um but you have relevant

**[19:00]** incomplete um but you have relevant documents, you have no hallucinations.

**[19:02]** documents, you have no hallucinations.

**[19:02]** documents, you have no hallucinations. Uh so this probably means you don't have

**[19:04]** Uh so this probably means you don't have

**[19:04]** Uh so this probably means you don't have all the information you need to answer

**[19:05]** all the information you need to answer

**[19:06]** all the information you need to answer the question. uh and so just retrieving

**[19:08]** the question. uh and so just retrieving

**[19:08]** the question. uh and so just retrieving more documents might solve that. Um but

**[19:11]** more documents might solve that. Um but

**[19:11]** more documents might solve that. Um but the big picture idea is that your

**[19:13]** the big picture idea is that your

**[19:13]** the big picture idea is that your evaluation should do more than just

**[19:15]** evaluation should do more than just

**[19:15]** evaluation should do more than just provide relative rankings. It should

**[19:17]** provide relative rankings. It should

**[19:17]** provide relative rankings. It should help you identify the types of issues

**[19:18]** help you identify the types of issues

**[19:18]** help you identify the types of issues that are present and it should also help

**[19:21]** that are present and it should also help

**[19:21]** that are present and it should also help you understand what strategies to

**[19:22]** you understand what strategies to

**[19:22]** you understand what strategies to implement to solve those issues.

**[19:26]** implement to solve those issues.

**[19:26]** implement to solve those issues. Okay. So uh so in conclusion, let me

**[19:30]** Okay. So uh so in conclusion, let me

**[19:30]** Okay. So uh so in conclusion, let me just quickly paint a picture of where

**[19:32]** just quickly paint a picture of where

**[19:32]** just quickly paint a picture of where we're heading with all this because this

**[19:33]** we're heading with all this because this

**[19:33]** we're heading with all this because this is not just about building the agents

**[19:35]** is not just about building the agents

**[19:35]** is not just about building the agents we've been building for the past couple

**[19:37]** we've been building for the past couple

**[19:37]** we've been building for the past couple years and then slapping evaluation on it

**[19:39]** years and then slapping evaluation on it

**[19:39]** years and then slapping evaluation on it and then continuing to do the same

**[19:40]** and then continuing to do the same

**[19:40]** and then continuing to do the same thing. Uh it's actually it's not about

**[19:43]** thing. Uh it's actually it's not about

**[19:43]** thing. Uh it's actually it's not about building better benchmarking. It's not

**[19:44]** building better benchmarking. It's not

**[19:44]** building better benchmarking. It's not better monitoring. It's not about better

**[19:46]** better monitoring. It's not about better

**[19:46]** better monitoring. It's not about better evaluation. It's about creating AI

**[19:49]** evaluation. It's about creating AI

**[19:49]** evaluation. It's about creating AI systems that can uh continuously improve

**[19:52]** systems that can uh continuously improve

**[19:52]** systems that can uh continuously improve themselves. And imagine for a second

**[19:54]** themselves. And imagine for a second

**[19:54]** themselves. And imagine for a second that agents don't just retrieve

**[19:56]** that agents don't just retrieve

**[19:56]** that agents don't just retrieve information but learn from the patterns

**[19:57]** information but learn from the patterns

**[19:58]** information but learn from the patterns of what information is outdated, what


### [20:00 - 21:00]

**[20:00]** of what information is outdated, what

**[20:00]** of what information is outdated, what sources are unreliable and what users

**[20:02]** sources are unreliable and what users

**[20:02]** sources are unreliable and what users need. Um they can also like maybe detect

**[20:05]** need. Um they can also like maybe detect

**[20:05]** need. Um they can also like maybe detect hallucinations mid conversations and uh

**[20:08]** hallucinations mid conversations and uh

**[20:08]** hallucinations mid conversations and uh correct the course all without human

**[20:10]** correct the course all without human

**[20:10]** correct the course all without human intervention.

**[20:12]** intervention.

**[20:12]** intervention. And this framework that we shared today,

**[20:14]** And this framework that we shared today,

**[20:14]** And this framework that we shared today, dynamic data sets, holistic evaluation,

**[20:17]** dynamic data sets, holistic evaluation,

**[20:17]** dynamic data sets, holistic evaluation, reference free metrics are the building

**[20:19]** reference free metrics are the building

**[20:19]** reference free metrics are the building blocks for getting there. Uh, and this

**[20:22]** blocks for getting there. Uh, and this

**[20:22]** blocks for getting there. Uh, and this this is where we want to get with

**[20:24]** this is where we want to get with

**[20:24]** this is where we want to get with augmented AI. So, thank you so much for

**[20:26]** augmented AI. So, thank you so much for

**[20:26]** augmented AI. So, thank you so much for your time.


