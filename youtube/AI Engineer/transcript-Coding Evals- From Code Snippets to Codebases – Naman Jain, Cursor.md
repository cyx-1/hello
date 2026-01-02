# Coding Evals- From Code Snippets to Codebases – Naman Jain, Cursor

**Video URL:** https://www.youtube.com/watch?v=tHN44yJoeS8

---

## Full Transcript

### [00:00 - 01:00]

**[00:23]** Hi everyone. So I'll be talking about uh

**[00:23]** Hi everyone. So I'll be talking about uh like some work on evaluations

**[00:25]** like some work on evaluations

**[00:25]** like some work on evaluations particularly evaluations across like I

**[00:27]** particularly evaluations across like I

**[00:27]** particularly evaluations across like I guess I've done in the last four years.

**[00:29]** guess I've done in the last four years.

**[00:29]** guess I've done in the last four years. So let's get started.

**[00:32]** So let's get started.

**[00:32]** So let's get started. So uh I'll be talking about coding

**[00:34]** So uh I'll be talking about coding

**[00:34]** So uh I'll be talking about coding evaluations across varying time

**[00:35]** evaluations across varying time

**[00:35]** evaluations across varying time horizons. So I've been uh working on

**[00:37]** horizons. So I've been uh working on

**[00:37]** horizons. So I've been uh working on like in the code space for about four

**[00:39]** like in the code space for about four

**[00:39]** like in the code space for about four years now like it was right before like

**[00:41]** years now like it was right before like

**[00:41]** years now like it was right before like early copilot came out and my first

**[00:43]** early copilot came out and my first

**[00:43]** early copilot came out and my first project was actually working on

**[00:45]** project was actually working on

**[00:45]** project was actually working on generating like single line panda

**[00:47]** generating like single line panda

**[00:47]** generating like single line panda snippets and my last project was

**[00:48]** snippets and my last project was

**[00:48]** snippets and my last project was generating an entire codebase. So the

**[00:50]** generating an entire codebase. So the

**[00:50]** generating an entire codebase. So the field has like really progressed very

**[00:52]** field has like really progressed very

**[00:52]** field has like really progressed very quickly. So I'll be talking about like

**[00:54]** quickly. So I'll be talking about like

**[00:54]** quickly. So I'll be talking about like uh different stages of evaluations we

**[00:56]** uh different stages of evaluations we

**[00:56]** uh different stages of evaluations we have considered and some learnings

**[00:57]** have considered and some learnings

**[00:57]** have considered and some learnings across each of the projects and how I

**[00:59]** across each of the projects and how I

**[00:59]** across each of the projects and how I see evaluations going forward. So the


### [01:00 - 02:00]

**[01:02]** see evaluations going forward. So the

**[01:02]** see evaluations going forward. So the first work I did was on uh like uh

**[01:04]** first work I did was on uh like uh

**[01:04]** first work I did was on uh like uh evaluating uh coding models in like

**[01:06]** evaluating uh coding models in like

**[01:06]** evaluating uh coding models in like second uh work doing in seconds of time

**[01:08]** second uh work doing in seconds of time

**[01:08]** second uh work doing in seconds of time like generating single line steps your

**[01:10]** like generating single line steps your

**[01:10]** like generating single line steps your co-pilot code completions. Then I work

**[01:13]** co-pilot code completions. Then I work

**[01:13]** co-pilot code completions. Then I work did some work on like uh evaluating on

**[01:15]** did some work on like uh evaluating on

**[01:15]** did some work on like uh evaluating on like interview style competition

**[01:16]** like interview style competition

**[01:16]** like interview style competition programming problems uh which where

**[01:18]** programming problems uh which where

**[01:18]** programming problems uh which where models can work up to minutes. Uh then

**[01:21]** models can work up to minutes. Uh then

**[01:21]** models can work up to minutes. Uh then we worked on some work on like uh

**[01:22]** we worked on some work on like uh

**[01:22]** we worked on some work on like uh repository question answering uh which

**[01:24]** repository question answering uh which

**[01:24]** repository question answering uh which required like maybe uh more uh multiple

**[01:27]** required like maybe uh more uh multiple

**[01:27]** required like maybe uh more uh multiple minutes tens of minutes. Uh and finally

**[01:29]** minutes tens of minutes. Uh and finally

**[01:29]** minutes tens of minutes. Uh and finally like uh pushing the frontier forward we

**[01:32]** like uh pushing the frontier forward we

**[01:32]** like uh pushing the frontier forward we are uh thinking about uh evaluating

**[01:33]** are uh thinking about uh evaluating

**[01:33]** are uh thinking about uh evaluating models on very complex tasks which can

**[01:35]** models on very complex tasks which can

**[01:35]** models on very complex tasks which can take hours or like multiple hours of

**[01:37]** take hours or like multiple hours of

**[01:37]** take hours or like multiple hours of work like code optimization and like

**[01:39]** work like code optimization and like

**[01:39]** work like code optimization and like even further. So let's get started.

**[01:43]** even further. So let's get started.

**[01:43]** even further. So let's get started. Uh so first work I'll be talking about

**[01:45]** Uh so first work I'll be talking about

**[01:45]** Uh so first work I'll be talking about is like codebench uh which is uh like uh

**[01:48]** is like codebench uh which is uh like uh

**[01:48]** is like codebench uh which is uh like uh uh validation work on models for like

**[01:51]** uh validation work on models for like

**[01:51]** uh validation work on models for like competition coding. So here uh like this

**[01:54]** competition coding. So here uh like this

**[01:54]** competition coding. So here uh like this is what a problem would look like. This

**[01:55]** is what a problem would look like. This

**[01:55]** is what a problem would look like. This is like very standard lead code problem

**[01:56]** is like very standard lead code problem

**[01:56]** is like very standard lead code problem and don't worry you don't need to solve

**[01:58]** and don't worry you don't need to solve

**[01:58]** and don't worry you don't need to solve something like this. So uh like uh here


### [02:00 - 03:00]

**[02:02]** something like this. So uh like uh here

**[02:02]** something like this. So uh like uh here as you can see there's a problem uh

**[02:03]** as you can see there's a problem uh

**[02:03]** as you can see there's a problem uh statement and the nice thing about these

**[02:05]** statement and the nice thing about these

**[02:05]** statement and the nice thing about these interview style problems is that these

**[02:07]** interview style problems is that these

**[02:07]** interview style problems is that these problems are very well uh defined. you

**[02:09]** problems are very well uh defined. you

**[02:09]** problems are very well uh defined. you have like good natural language

**[02:11]** have like good natural language

**[02:11]** have like good natural language specifications some example input output

**[02:13]** specifications some example input output

**[02:13]** specifications some example input output examples so you can very uh reliably

**[02:15]** examples so you can very uh reliably

**[02:15]** examples so you can very uh reliably evaluate the models are doing a good job

**[02:16]** evaluate the models are doing a good job

**[02:16]** evaluate the models are doing a good job or not. So what was the motivation

**[02:18]** or not. So what was the motivation

**[02:18]** or not. So what was the motivation behind this and how we improved the

**[02:20]** behind this and how we improved the

**[02:20]** behind this and how we improved the frontier here. So the first challenge in

**[02:23]** frontier here. So the first challenge in

**[02:23]** frontier here. So the first challenge in uh evaluating uh language models these

**[02:25]** uh evaluating uh language models these

**[02:25]** uh evaluating uh language models these days is like data contamination. These

**[02:27]** days is like data contamination. These

**[02:27]** days is like data contamination. These models are trained on like the entire

**[02:28]** models are trained on like the entire

**[02:28]** models are trained on like the entire internet and uh like on stack overflow

**[02:31]** internet and uh like on stack overflow

**[02:31]** internet and uh like on stack overflow you'll find uh like very uh similar

**[02:32]** you'll find uh like very uh similar

**[02:32]** you'll find uh like very uh similar programming problems puzzles. Uh

**[02:35]** programming problems puzzles. Uh

**[02:35]** programming problems puzzles. Uh similarly uh like you'll find uh like uh

**[02:37]** similarly uh like you'll find uh like uh

**[02:37]** similarly uh like you'll find uh like uh very similar programming problem sources

**[02:39]** very similar programming problem sources

**[02:39]** very similar programming problem sources on GitHub or on the internet. So uh like

**[02:43]** on GitHub or on the internet. So uh like

**[02:43]** on GitHub or on the internet. So uh like contamination is a big uh deal. Uh

**[02:45]** contamination is a big uh deal. Uh

**[02:46]** contamination is a big uh deal. Uh another very uh challenging factor which

**[02:47]** another very uh challenging factor which

**[02:47]** another very uh challenging factor which has struggled with the field is like

**[02:49]** has struggled with the field is like

**[02:49]** has struggled with the field is like insufficient text suites. So you'll see

**[02:52]** insufficient text suites. So you'll see

**[02:52]** insufficient text suites. So you'll see that uh like in this program uh like the

**[02:55]** that uh like in this program uh like the

**[02:55]** that uh like in this program uh like the goal was to return a sorted unique

**[02:57]** goal was to return a sorted unique

**[02:57]** goal was to return a sorted unique common elements between the two lists.

**[02:59]** common elements between the two lists.

**[02:59]** common elements between the two lists. But uh like even a solution which does


### [03:00 - 04:00]

**[03:01]** But uh like even a solution which does

**[03:01]** But uh like even a solution which does not do the sorting and just returns the

**[03:02]** not do the sorting and just returns the

**[03:02]** not do the sorting and just returns the set actually works because the tests

**[03:04]** set actually works because the tests

**[03:04]** set actually works because the tests were brittle and were not catching this

**[03:05]** were brittle and were not catching this

**[03:05]** were brittle and were not catching this mistake. So uh like test suites is

**[03:08]** mistake. So uh like test suites is

**[03:08]** mistake. So uh like test suites is another uh like very challenging factor

**[03:10]** another uh like very challenging factor

**[03:10]** another uh like very challenging factor and how do we generate good and diverse

**[03:12]** and how do we generate good and diverse

**[03:12]** and how do we generate good and diverse tests and finally uh difficulty

**[03:15]** tests and finally uh difficulty

**[03:15]** tests and finally uh difficulty distributions which is something which

**[03:16]** distributions which is something which

**[03:16]** distributions which is something which people do not do not really uh reliably

**[03:19]** people do not do not really uh reliably

**[03:19]** people do not do not really uh reliably uh like calibrate uh like when I first

**[03:21]** uh like calibrate uh like when I first

**[03:21]** uh like calibrate uh like when I first was working uh in uh this space uh like

**[03:24]** was working uh in uh this space uh like

**[03:24]** was working uh in uh this space uh like there were two benchmarks available on

**[03:26]** there were two benchmarks available on

**[03:26]** there were two benchmarks available on one benchmark the performance was 80% or

**[03:28]** one benchmark the performance was 80% or

**[03:28]** one benchmark the performance was 80% or 90% and on the other one it was 1% and

**[03:30]** 90% and on the other one it was 1% and

**[03:30]** 90% and on the other one it was 1% and there was nothing in between and uh like

**[03:33]** there was nothing in between and uh like

**[03:33]** there was nothing in between and uh like as like benchmark users what you care

**[03:35]** as like benchmark users what you care

**[03:35]** as like benchmark users what you care about is having some signal from the

**[03:37]** about is having some signal from the

**[03:37]** about is having some signal from the benchmark to like basically hill climb

**[03:39]** benchmark to like basically hill climb

**[03:39]** benchmark to like basically hill climb to make progress to measure progress and

**[03:41]** to make progress to measure progress and

**[03:41]** to make progress to measure progress and in uh either of these regimes when if

**[03:43]** in uh either of these regimes when if

**[03:43]** in uh either of these regimes when if the problems are too easy or too hard

**[03:45]** the problems are too easy or too hard

**[03:45]** the problems are too easy or too hard you don't get a lot of signal. So it is

**[03:47]** you don't get a lot of signal. So it is

**[03:47]** you don't get a lot of signal. So it is very important [clears throat] when

**[03:48]** very important [clears throat] when

**[03:48]** very important [clears throat] when you're designing benchmarks to think

**[03:49]** you're designing benchmarks to think

**[03:49]** you're designing benchmarks to think about like the kinds of problems you are

**[03:51]** about like the kinds of problems you are

**[03:51]** about like the kinds of problems you are taking and will it provide enough signal

**[03:52]** taking and will it provide enough signal

**[03:52]** taking and will it provide enough signal for the users of your benchmark.

**[03:55]** for the users of your benchmark.

**[03:55]** for the users of your benchmark. So uh like in light codebench we

**[03:57]** So uh like in light codebench we

**[03:57]** So uh like in light codebench we pioneered like dynamic evaluations uh

**[03:59]** pioneered like dynamic evaluations uh

**[03:59]** pioneered like dynamic evaluations uh particularly uh like we can periodically


### [04:00 - 05:00]

**[04:01]** particularly uh like we can periodically

**[04:01]** particularly uh like we can periodically update uh the evaluation sets uh and

**[04:04]** update uh the evaluation sets uh and

**[04:04]** update uh the evaluation sets uh and this gives you two uh very nice factors.

**[04:06]** this gives you two uh very nice factors.

**[04:06]** this gives you two uh very nice factors. First is you can combat contamination.

**[04:08]** First is you can combat contamination.

**[04:08]** First is you can combat contamination. So you can evaluate the models on

**[04:09]** So you can evaluate the models on

**[04:09]** So you can evaluate the models on problems that were released after the

**[04:10]** problems that were released after the

**[04:10]** problems that were released after the model was trained. So it has likely not

**[04:12]** model was trained. So it has likely not

**[04:12]** model was trained. So it has likely not seen the problem something like that. Uh

**[04:15]** seen the problem something like that. Uh

**[04:15]** seen the problem something like that. Uh and uh then you can also modify the

**[04:17]** and uh then you can also modify the

**[04:17]** and uh then you can also modify the problem difficulty distributions over

**[04:19]** problem difficulty distributions over

**[04:19]** problem difficulty distributions over time. So as we have talked about models

**[04:20]** time. So as we have talked about models

**[04:20]** time. So as we have talked about models are incre like improving very rapidly.

**[04:23]** are incre like improving very rapidly.

**[04:23]** are incre like improving very rapidly. uh so what was difficult uh for the

**[04:25]** uh so what was difficult uh for the

**[04:25]** uh so what was difficult uh for the model 6 months back might not be now. So

**[04:27]** model 6 months back might not be now. So

**[04:27]** model 6 months back might not be now. So you can uh if you're updating your

**[04:28]** you can uh if you're updating your

**[04:28]** you can uh if you're updating your evaluation sets constantly you can

**[04:30]** evaluation sets constantly you can

**[04:30]** evaluation sets constantly you can actually uh keep calibrate uh the

**[04:32]** actually uh keep calibrate uh the

**[04:32]** actually uh keep calibrate uh the difficulty distributions calibrated so

**[04:34]** difficulty distributions calibrated so

**[04:34]** difficulty distributions calibrated so you still get more signal out of your

**[04:35]** you still get more signal out of your

**[04:35]** you still get more signal out of your benchmarks.

**[04:37]** benchmarks.

**[04:37]** benchmarks. So how we did that here like we had like

**[04:39]** So how we did that here like we had like

**[04:39]** So how we did that here like we had like an automated approach for curation of

**[04:41]** an automated approach for curation of

**[04:41]** an automated approach for curation of these problems and uh similarly we could

**[04:44]** these problems and uh similarly we could

**[04:44]** these problems and uh similarly we could automatically constru these test cases

**[04:46]** automatically constru these test cases

**[04:46]** automatically constru these test cases in an automated manner and uh this

**[04:49]** in an automated manner and uh this

**[04:49]** in an automated manner and uh this allows a very nice thing when since we

**[04:50]** allows a very nice thing when since we

**[04:50]** allows a very nice thing when since we are like collecting problems over time

**[04:53]** are like collecting problems over time

**[04:53]** are like collecting problems over time we have time as a control knob. So like

**[04:55]** we have time as a control knob. So like

**[04:55]** we have time as a control knob. So like we have these problem release months uh

**[04:57]** we have these problem release months uh

**[04:57]** we have these problem release months uh on lead code and if you evaluate the

**[04:59]** on lead code and if you evaluate the

**[04:59]** on lead code and if you evaluate the model performances like the pass at the


### [05:00 - 06:00]

**[05:01]** model performances like the pass at the

**[05:01]** model performances like the pass at the rate one metric uh like on problems

**[05:04]** rate one metric uh like on problems

**[05:04]** rate one metric uh like on problems released over different months you will

**[05:05]** released over different months you will

**[05:05]** released over different months you will see that after uh like uh these model

**[05:08]** see that after uh like uh these model

**[05:08]** see that after uh like uh these model release dates you would see stark drop

**[05:09]** release dates you would see stark drop

**[05:09]** release dates you would see stark drop in model performance. So like after

**[05:11]** in model performance. So like after

**[05:11]** in model performance. So like after deepsek was uh released in like

**[05:13]** deepsek was uh released in like

**[05:13]** deepsek was uh released in like September 2023 uh the performance

**[05:15]** September 2023 uh the performance

**[05:15]** September 2023 uh the performance starkly drops from like maybe 50%

**[05:17]** starkly drops from like maybe 50%

**[05:17]** starkly drops from like maybe 50% average to like over like 20% or 15%

**[05:20]** average to like over like 20% or 15%

**[05:20]** average to like over like 20% or 15% average. So like uh based on these

**[05:23]** average. So like uh based on these

**[05:23]** average. So like uh based on these sliding windows you can uh evaluate

**[05:24]** sliding windows you can uh evaluate

**[05:24]** sliding windows you can uh evaluate performance, measure contamination and

**[05:26]** performance, measure contamination and

**[05:26]** performance, measure contamination and even combat contamination.

**[05:28]** even combat contamination.

**[05:28]** even combat contamination. Um uh we have the running leaderboard

**[05:30]** Um uh we have the running leaderboard

**[05:30]** Um uh we have the running leaderboard which is like very well maintained and

**[05:32]** which is like very well maintained and

**[05:32]** which is like very well maintained and uh on this leaderboard you can actually

**[05:34]** uh on this leaderboard you can actually

**[05:34]** uh on this leaderboard you can actually uh like uh like view performances by uh

**[05:37]** uh like uh like view performances by uh

**[05:37]** uh like uh like view performances by uh scrolling this uh horizontal time bar

**[05:39]** scrolling this uh horizontal time bar

**[05:39]** scrolling this uh horizontal time bar and you'll see that as you're scrolling

**[05:41]** and you'll see that as you're scrolling

**[05:41]** and you'll see that as you're scrolling uh the contaminated models which are the

**[05:43]** uh the contaminated models which are the

**[05:43]** uh the contaminated models which are the red bars actually go down which does

**[05:45]** red bars actually go down which does

**[05:45]** red bars actually go down which does highlight that uh like problem does uh

**[05:47]** highlight that uh like problem does uh

**[05:47]** highlight that uh like problem does uh like model performance does change on uh

**[05:49]** like model performance does change on uh

**[05:49]** like model performance does change on uh these newer kind of problems.

**[05:52]** these newer kind of problems.

**[05:52]** these newer kind of problems. Um finally for uh test generation we uh

**[05:55]** Um finally for uh test generation we uh

**[05:55]** Um finally for uh test generation we uh maintain uh like these uh test

**[05:57]** maintain uh like these uh test

**[05:57]** maintain uh like these uh test generation test generators. So if you

**[05:59]** generation test generators. So if you


### [06:00 - 07:00]

**[06:00]** generation test generators. So if you worked on fuzzing you would have like

**[06:01]** worked on fuzzing you would have like

**[06:01]** worked on fuzzing you would have like input generators where you generate

**[06:03]** input generators where you generate

**[06:03]** input generators where you generate diverse inputs and each of the problems

**[06:05]** diverse inputs and each of the problems

**[06:05]** diverse inputs and each of the problems are supported by like 30s or 50 inputs.

**[06:07]** are supported by like 30s or 50 inputs.

**[06:07]** are supported by like 30s or 50 inputs. So you can uh reliably find mistakes and

**[06:09]** So you can uh reliably find mistakes and

**[06:09]** So you can uh reliably find mistakes and bugs in uh incorrect code and these are

**[06:11]** bugs in uh incorrect code and these are

**[06:11]** bugs in uh incorrect code and these are all automatically generated uh using an

**[06:13]** all automatically generated uh using an

**[06:13]** all automatically generated uh using an LLM driven approaches

**[06:16]** LLM driven approaches

**[06:16]** LLM driven approaches and these problems uh have been like

**[06:18]** and these problems uh have been like

**[06:18]** and these problems uh have been like continuously being released and updated.

**[06:20]** continuously being released and updated.

**[06:20]** continuously being released and updated. So we have released like six different

**[06:21]** So we have released like six different

**[06:21]** So we have released like six different versions of uh life codebench and these

**[06:24]** versions of uh life codebench and these

**[06:24]** versions of uh life codebench and these uh new one of the nice things or one of

**[06:26]** uh new one of the nice things or one of

**[06:26]** uh new one of the nice things or one of the worrying things for me at the start

**[06:27]** the worrying things for me at the start

**[06:27]** the worrying things for me at the start was that uh like if you're constantly

**[06:29]** was that uh like if you're constantly

**[06:29]** was that uh like if you're constantly updating the eval sets will uh like

**[06:31]** updating the eval sets will uh like

**[06:31]** updating the eval sets will uh like people be able to keep track of them

**[06:32]** people be able to keep track of them

**[06:32]** people be able to keep track of them will people be using them or will they

**[06:34]** will people be using them or will they

**[06:34]** will people be using them or will they just restrict to a single version? Uh it

**[06:36]** just restrict to a single version? Uh it

**[06:36]** just restrict to a single version? Uh it turned out that these newer eval sets

**[06:38]** turned out that these newer eval sets

**[06:38]** turned out that these newer eval sets were constantly uh like adopted by

**[06:40]** were constantly uh like adopted by

**[06:40]** were constantly uh like adopted by different foundation model labs and uh

**[06:42]** different foundation model labs and uh

**[06:42]** different foundation model labs and uh like since we updated the problem

**[06:44]** like since we updated the problem

**[06:44]** like since we updated the problem difficulty over time uh the evaluation

**[06:46]** difficulty over time uh the evaluation

**[06:46]** difficulty over time uh the evaluation sets continue to provide strong signal

**[06:47]** sets continue to provide strong signal

**[06:47]** sets continue to provide strong signal to compare uh different models.

**[06:51]** to compare uh different models.

**[06:51]** to compare uh different models. Um so this was like live codebench.

**[06:53]** Um so this was like live codebench.

**[06:53]** Um so this was like live codebench. Let's talk about uh like something which

**[06:55]** Let's talk about uh like something which

**[06:55]** Let's talk about uh like something which is more on coding agents like more real

**[06:57]** is more on coding agents like more real

**[06:57]** is more on coding agents like more real world programs and this is our work on

**[06:59]** world programs and this is our work on

**[06:59]** world programs and this is our work on like uh software optimization. So this


### [07:00 - 08:00]

**[07:01]** like uh software optimization. So this

**[07:01]** like uh software optimization. So this is a problem we're very excited about

**[07:02]** is a problem we're very excited about

**[07:02]** is a problem we're very excited about and I'll talk about a few factors why

**[07:04]** and I'll talk about a few factors why

**[07:04]** and I'll talk about a few factors why you should maybe be excited about this.

**[07:06]** you should maybe be excited about this.

**[07:06]** you should maybe be excited about this. So uh here we are trying to uh measure

**[07:09]** So uh here we are trying to uh measure

**[07:09]** So uh here we are trying to uh measure model capabilities in generating high

**[07:11]** model capabilities in generating high

**[07:11]** model capabilities in generating high performance software and uh I feel that

**[07:13]** performance software and uh I feel that

**[07:13]** performance software and uh I feel that this uh like problem domain uh like

**[07:15]** this uh like problem domain uh like

**[07:15]** this uh like problem domain uh like mixes two uh factors like the

**[07:17]** mixes two uh factors like the

**[07:17]** mixes two uh factors like the algorithmic coding uh uh field I talked

**[07:19]** algorithmic coding uh uh field I talked

**[07:19]** algorithmic coding uh uh field I talked about which is like live codebin setting

**[07:21]** about which is like live codebin setting

**[07:21]** about which is like live codebin setting but also like glob global software

**[07:22]** but also like glob global software

**[07:22]** but also like glob global software editing like uh sweet bench and other

**[07:24]** editing like uh sweet bench and other

**[07:24]** editing like uh sweet bench and other like software uh uh general software

**[07:26]** like software uh uh general software

**[07:26]** like software uh uh general software engineering benchmarks. uh uh in high

**[07:29]** engineering benchmarks. uh uh in high

**[07:29]** engineering benchmarks. uh uh in high performance uh software you will have to

**[07:30]** performance uh software you will have to

**[07:30]** performance uh software you will have to do algorithmic work you have to do deep

**[07:32]** do algorithmic work you have to do deep

**[07:32]** do algorithmic work you have to do deep analysis and find uh uh generate

**[07:35]** analysis and find uh uh generate

**[07:35]** analysis and find uh uh generate software with like right uh runtime.

**[07:38]** software with like right uh runtime.

**[07:38]** software with like right uh runtime. So uh one of the key principles when we

**[07:41]** So uh one of the key principles when we

**[07:41]** So uh one of the key principles when we are trying to build this benchmark was

**[07:42]** are trying to build this benchmark was

**[07:42]** are trying to build this benchmark was like ensuring construct validity because

**[07:44]** like ensuring construct validity because

**[07:44]** like ensuring construct validity because when you see a lot of benchmarks today

**[07:47]** when you see a lot of benchmarks today

**[07:47]** when you see a lot of benchmarks today uh we get very high benchmark scores but

**[07:49]** uh we get very high benchmark scores but

**[07:49]** uh we get very high benchmark scores but at a lot of the times they don't really

**[07:50]** at a lot of the times they don't really

**[07:50]** at a lot of the times they don't really translate to real world performance

**[07:52]** translate to real world performance

**[07:52]** translate to real world performance gains. So construct validity refers to

**[07:54]** gains. So construct validity refers to

**[07:54]** gains. So construct validity refers to how close uh a measurement reflects the

**[07:56]** how close uh a measurement reflects the

**[07:56]** how close uh a measurement reflects the underlying uh concept it's meant to

**[07:58]** underlying uh concept it's meant to

**[07:58]** underlying uh concept it's meant to measure. So like here we are measuring


### [08:00 - 09:00]

**[08:00]** measure. So like here we are measuring

**[08:00]** measure. So like here we are measuring code optimization and we want something

**[08:02]** code optimization and we want something

**[08:02]** code optimization and we want something which is uh like uh reliably evaluates

**[08:04]** which is uh like uh reliably evaluates

**[08:04]** which is uh like uh reliably evaluates real world uh takes. So this usually

**[08:07]** real world uh takes. So this usually

**[08:07]** real world uh takes. So this usually requires like two aspects. First is like

**[08:09]** requires like two aspects. First is like

**[08:09]** requires like two aspects. First is like the task distribution. Your task should

**[08:11]** the task distribution. Your task should

**[08:11]** the task distribution. Your task should be natural and sourced from the real

**[08:12]** be natural and sourced from the real

**[08:12]** be natural and sourced from the real world and then you should be able to

**[08:14]** world and then you should be able to

**[08:14]** world and then you should be able to reliably grade them. So let me talk

**[08:17]** reliably grade them. So let me talk

**[08:17]** reliably grade them. So let me talk about like what steps we take to uh make

**[08:19]** about like what steps we take to uh make

**[08:19]** about like what steps we take to uh make this happen and how we construct this

**[08:20]** this happen and how we construct this

**[08:20]** this happen and how we construct this benchmark. So let's say we take a

**[08:23]** benchmark. So let's say we take a

**[08:23]** benchmark. So let's say we take a codebase like llama cvp uh we take uh uh

**[08:26]** codebase like llama cvp uh we take uh uh

**[08:26]** codebase like llama cvp uh we take uh uh we crawl over all the commits of the

**[08:27]** we crawl over all the commits of the

**[08:27]** we crawl over all the commits of the codebase and we find the commits which

**[08:29]** codebase and we find the commits which

**[08:29]** codebase and we find the commits which are op like doing something uh related

**[08:31]** are op like doing something uh related

**[08:31]** are op like doing something uh related to performance optimization. So here

**[08:33]** to performance optimization. So here

**[08:33]** to performance optimization. So here there was this commit which is

**[08:34]** there was this commit which is

**[08:34]** there was this commit which is optimizing the quantized performance of

**[08:36]** optimizing the quantized performance of

**[08:36]** optimizing the quantized performance of uh like uh certain kinds of models. Uh

**[08:39]** uh like uh certain kinds of models. Uh

**[08:39]** uh like uh certain kinds of models. Uh for all of these uh comm performance

**[08:41]** for all of these uh comm performance

**[08:41]** for all of these uh comm performance optimizing commits we would uh like

**[08:43]** optimizing commits we would uh like

**[08:43]** optimizing commits we would uh like generate performance test cases. Um and

**[08:46]** generate performance test cases. Um and

**[08:46]** generate performance test cases. Um and uh these performance SK would look like

**[08:47]** uh these performance SK would look like

**[08:47]** uh these performance SK would look like some workloads and uh once we have these

**[08:51]** some workloads and uh once we have these

**[08:51]** some workloads and uh once we have these workloads uh we have a very uh nice and

**[08:53]** workloads uh we have a very uh nice and

**[08:53]** workloads uh we have a very uh nice and precise way to specify the problem

**[08:54]** precise way to specify the problem

**[08:54]** precise way to specify the problem statement that uh given this workload of

**[08:56]** statement that uh given this workload of

**[08:56]** statement that uh given this workload of let's say uh running uh Quinn uh 7B

**[08:59]** let's say uh running uh Quinn uh 7B

**[08:59]** let's say uh running uh Quinn uh 7B model uh can uh we give this uh problem


### [09:00 - 10:00]

**[09:02]** model uh can uh we give this uh problem

**[09:02]** model uh can uh we give this uh problem to uh su agent ask the model to optimize

**[09:04]** to uh su agent ask the model to optimize

**[09:04]** to uh su agent ask the model to optimize the code glamour CPB repository so this

**[09:06]** the code glamour CPB repository so this

**[09:06]** the code glamour CPB repository so this code runs faster so as you can imagine

**[09:08]** code runs faster so as you can imagine

**[09:08]** code runs faster so as you can imagine this uh task is like fairly challenging

**[09:10]** this uh task is like fairly challenging

**[09:10]** this uh task is like fairly challenging you need to understand like low-level uh

**[09:12]** you need to understand like low-level uh

**[09:12]** you need to understand like low-level uh implementation details uh and like how

**[09:15]** implementation details uh and like how

**[09:15]** implementation details uh and like how quantized models behave, how we can uh

**[09:17]** quantized models behave, how we can uh

**[09:17]** quantized models behave, how we can uh improve the runtime and so models can

**[09:19]** improve the runtime and so models can

**[09:19]** improve the runtime and so models can generate a patch and the evaluation is

**[09:21]** generate a patch and the evaluation is

**[09:21]** generate a patch and the evaluation is done on whether the patch is correct. So

**[09:23]** done on whether the patch is correct. So

**[09:23]** done on whether the patch is correct. So does it pass the equivalence check with

**[09:25]** does it pass the equivalence check with

**[09:25]** does it pass the equivalence check with the human patch and uh is there a valid

**[09:28]** the human patch and uh is there a valid

**[09:28]** the human patch and uh is there a valid optimization over the reference human

**[09:30]** optimization over the reference human

**[09:30]** optimization over the reference human patch uh that is uh whether you can uh

**[09:32]** patch uh that is uh whether you can uh

**[09:32]** patch uh that is uh whether you can uh generate a better runtime than what a

**[09:34]** generate a better runtime than what a

**[09:34]** generate a better runtime than what a human could do.

**[09:36]** human could do.

**[09:36]** human could do. So uh like uh this is a very challenging

**[09:38]** So uh like uh this is a very challenging

**[09:38]** So uh like uh this is a very challenging task. we have like 100 plus optimization

**[09:40]** task. we have like 100 plus optimization

**[09:40]** task. we have like 100 plus optimization task source in this manner and this is

**[09:42]** task source in this manner and this is

**[09:42]** task source in this manner and this is like fairly uh like important in like uh

**[09:45]** like fairly uh like important in like uh

**[09:45]** like fairly uh like important in like uh like high performance settings. So think

**[09:48]** like high performance settings. So think

**[09:48]** like high performance settings. So think about like data science uh like ML

**[09:50]** about like data science uh like ML

**[09:50]** about like data science uh like ML visualization scenarios uh benchmark uh

**[09:53]** visualization scenarios uh benchmark uh

**[09:53]** visualization scenarios uh benchmark uh like comprises of like various uh

**[09:55]** like comprises of like various uh

**[09:55]** like comprises of like various uh low-level uh code like C, C++, Rust and

**[09:59]** low-level uh code like C, C++, Rust and

**[09:59]** low-level uh code like C, C++, Rust and the very nice thing is like these are


### [10:00 - 11:00]

**[10:00]** the very nice thing is like these are

**[10:00]** the very nice thing is like these are precise problem statements. you can uh

**[10:02]** precise problem statements. you can uh

**[10:02]** precise problem statements. you can uh easily specify to the model what is the

**[10:04]** easily specify to the model what is the

**[10:04]** easily specify to the model what is the goal in the form of a performance test

**[10:05]** goal in the form of a performance test

**[10:05]** goal in the form of a performance test which the model has access to and it can

**[10:07]** which the model has access to and it can

**[10:07]** which the model has access to and it can continuously iterate over it for a long

**[10:09]** continuously iterate over it for a long

**[10:09]** continuously iterate over it for a long time. So here we can scale the test time

**[10:11]** time. So here we can scale the test time

**[10:11]** time. So here we can scale the test time compute and pick the best solution based

**[10:12]** compute and pick the best solution based

**[10:12]** compute and pick the best solution based on uh the test cases that we have and

**[10:15]** on uh the test cases that we have and

**[10:15]** on uh the test cases that we have and this can happen like synchronously or

**[10:17]** this can happen like synchronously or

**[10:17]** this can happen like synchronously or asynchronously.

**[10:19]** asynchronously.

**[10:19]** asynchronously. So uh like we generate these performance

**[10:21]** So uh like we generate these performance

**[10:22]** So uh like we generate these performance test cases and uh that work uh

**[10:23]** test cases and uh that work uh

**[10:23]** test cases and uh that work uh reasonably well but uh we found that

**[10:26]** reasonably well but uh we found that

**[10:26]** reasonably well but uh we found that there were uh like cases of reward

**[10:27]** there were uh like cases of reward

**[10:27]** there were uh like cases of reward hacking here. So what do I mean by

**[10:29]** hacking here. So what do I mean by

**[10:29]** hacking here. So what do I mean by reward hacking? Like frontier models

**[10:31]** reward hacking? Like frontier models

**[10:31]** reward hacking? Like frontier models would write non-inneatic code to like

**[10:33]** would write non-inneatic code to like

**[10:33]** would write non-inneatic code to like actively exploit the evaluation

**[10:35]** actively exploit the evaluation

**[10:35]** actively exploit the evaluation infrastructure or overfitit the test

**[10:36]** infrastructure or overfitit the test

**[10:36]** infrastructure or overfitit the test distributions. So one funny example we

**[10:39]** distributions. So one funny example we

**[10:39]** distributions. So one funny example we saw was like models would add like l

**[10:41]** saw was like models would add like l

**[10:41]** saw was like models would add like l cache to p like arbitrary pandas methods

**[10:43]** cache to p like arbitrary pandas methods

**[10:43]** cache to p like arbitrary pandas methods when we were uh trying to optimize

**[10:45]** when we were uh trying to optimize

**[10:45]** when we were uh trying to optimize pandas and the official solution should

**[10:47]** pandas and the official solution should

**[10:47]** pandas and the official solution should have required changing something in the

**[10:49]** have required changing something in the

**[10:49]** have required changing something in the internals. Uh so we tried to pass this

**[10:51]** internals. Uh so we tried to pass this

**[10:51]** internals. Uh so we tried to pass this by changing our evaluation

**[10:52]** by changing our evaluation

**[10:52]** by changing our evaluation infrastructure so it's like more robust

**[10:54]** infrastructure so it's like more robust

**[10:54]** infrastructure so it's like more robust to this kind of hacking uh approaches

**[10:57]** to this kind of hacking uh approaches

**[10:57]** to this kind of hacking uh approaches but then we saw something like even more

**[10:59]** but then we saw something like even more

**[10:59]** but then we saw something like even more drastic models would sometimes


### [11:00 - 12:00]

**[11:01]** drastic models would sometimes

**[11:01]** drastic models would sometimes completely hijack the infra where uh

**[11:03]** completely hijack the infra where uh

**[11:03]** completely hijack the infra where uh they would add a like site customized.py

**[11:05]** they would add a like site customized.py

**[11:05]** they would add a like site customized.py Pi file where which runs at the start of

**[11:07]** Pi file where which runs at the start of

**[11:07]** Pi file where which runs at the start of Python runtime and it would basically

**[11:09]** Python runtime and it would basically

**[11:10]** Python runtime and it would basically change the numpy library uh like which

**[11:12]** change the numpy library uh like which

**[11:12]** change the numpy library uh like which was installed in the codebase to

**[11:14]** was installed in the codebase to

**[11:14]** was installed in the codebase to something it crawled from uh source and

**[11:17]** something it crawled from uh source and

**[11:17]** something it crawled from uh source and there is like I think you can do some

**[11:19]** there is like I think you can do some

**[11:19]** there is like I think you can do some ways to uh like take some measures to

**[11:21]** ways to uh like take some measures to

**[11:21]** ways to uh like take some measures to make your evaluation infra which is

**[11:22]** make your evaluation infra which is

**[11:22]** make your evaluation infra which is robust to these kind of uh like

**[11:24]** robust to these kind of uh like

**[11:24]** robust to these kind of uh like adversarial uh like attacks. But uh here

**[11:28]** adversarial uh like attacks. But uh here

**[11:28]** adversarial uh like attacks. But uh here uh like there could be myriad ways in

**[11:30]** uh like there could be myriad ways in

**[11:30]** uh like there could be myriad ways in which models can hack these kind of

**[11:31]** which models can hack these kind of

**[11:31]** which models can hack these kind of scenarios. And here uh we propose like

**[11:34]** scenarios. And here uh we propose like

**[11:34]** scenarios. And here uh we propose like hack detector where which is a detection

**[11:36]** hack detector where which is a detection

**[11:36]** hack detector where which is a detection system that leverages GBD5's like code

**[11:38]** system that leverages GBD5's like code

**[11:38]** system that leverages GBD5's like code analysis capabilities and test compute

**[11:41]** analysis capabilities and test compute

**[11:41]** analysis capabilities and test compute to like basically identify these kind of

**[11:42]** to like basically identify these kind of

**[11:42]** to like basically identify these kind of hacking behaviors at runtime. So you

**[11:44]** hacking behaviors at runtime. So you

**[11:44]** hacking behaviors at runtime. So you don't have to imagine all the possible

**[11:46]** don't have to imagine all the possible

**[11:46]** don't have to imagine all the possible failure scenarios at the start. So what

**[11:48]** failure scenarios at the start. So what

**[11:48]** failure scenarios at the start. So what it would take is like a model patch, the

**[11:50]** it would take is like a model patch, the

**[11:50]** it would take is like a model patch, the expert patch and test cases and we'll

**[11:51]** expert patch and test cases and we'll

**[11:51]** expert patch and test cases and we'll ask GBD5 to give like verdicts on like

**[11:54]** ask GBD5 to give like verdicts on like

**[11:54]** ask GBD5 to give like verdicts on like whether it's reward hacking with some

**[11:55]** whether it's reward hacking with some

**[11:56]** whether it's reward hacking with some kind of explanation. Uh we'll do this a

**[11:58]** kind of explanation. Uh we'll do this a

**[11:58]** kind of explanation. Uh we'll do this a few times and take the consensus and


### [12:00 - 13:00]

**[12:00]** few times and take the consensus and

**[12:00]** few times and take the consensus and based on this consensus we'll determine

**[12:01]** based on this consensus we'll determine

**[12:02]** based on this consensus we'll determine if this is uh doing some like nonomatic

**[12:05]** if this is uh doing some like nonomatic

**[12:05]** if this is uh doing some like nonomatic coding patterns or not

**[12:07]** coding patterns or not

**[12:07]** coding patterns or not and uh we did some failure analysis

**[12:09]** and uh we did some failure analysis

**[12:09]** and uh we did some failure analysis based on this. So now you can detect

**[12:11]** based on this. So now you can detect

**[12:11]** based on this. So now you can detect mistakes using test cases whether the

**[12:13]** mistakes using test cases whether the

**[12:13]** mistakes using test cases whether the code is correct or not whether it is

**[12:14]** code is correct or not whether it is

**[12:14]** code is correct or not whether it is optimizing or not but you can also

**[12:16]** optimizing or not but you can also

**[12:16]** optimizing or not but you can also detect reward hacks using this like lm

**[12:18]** detect reward hacks using this like lm

**[12:18]** detect reward hacks using this like lm as a judge uh factor and uh what you see

**[12:22]** as a judge uh factor and uh what you see

**[12:22]** as a judge uh factor and uh what you see is kind of surprising uh like models

**[12:24]** is kind of surprising uh like models

**[12:24]** is kind of surprising uh like models make a lot of like correctness mistakes

**[12:25]** make a lot of like correctness mistakes

**[12:25]** make a lot of like correctness mistakes that you can catch by tests but even if

**[12:27]** that you can catch by tests but even if

**[12:27]** that you can catch by tests but even if the code passes the test cases like 03

**[12:29]** the code passes the test cases like 03

**[12:29]** the code passes the test cases like 03 attempted reward hacking patterns in

**[12:31]** attempted reward hacking patterns in

**[12:31]** attempted reward hacking patterns in like 30% of the problems it tried and

**[12:33]** like 30% of the problems it tried and

**[12:33]** like 30% of the problems it tried and this fraction is like going down uh for

**[12:35]** this fraction is like going down uh for

**[12:35]** this fraction is like going down uh for the newer models to some degree but it

**[12:37]** the newer models to some degree but it

**[12:37]** the newer models to some degree but it is still existing and as we go to more

**[12:39]** is still existing and as we go to more

**[12:39]** is still existing and as we go to more and more real world tasks. Uh this is

**[12:41]** and more real world tasks. Uh this is

**[12:41]** and more real world tasks. Uh this is going to get more challenging and we

**[12:42]** going to get more challenging and we

**[12:42]** going to get more challenging and we need to figure uh like ways to combat

**[12:45]** need to figure uh like ways to combat

**[12:45]** need to figure uh like ways to combat these kind of reward hacking patterns by

**[12:46]** these kind of reward hacking patterns by

**[12:46]** these kind of reward hacking patterns by using LLM judge and other uh ways to

**[12:48]** using LLM judge and other uh ways to

**[12:48]** using LLM judge and other uh ways to make just evaluation infra more

**[12:50]** make just evaluation infra more

**[12:50]** make just evaluation infra more reliable.

**[12:53]** reliable.

**[12:53]** reliable. So next I'll talk about like uh uh like

**[12:55]** So next I'll talk about like uh uh like

**[12:55]** So next I'll talk about like uh uh like sizz some of our new work on like uh

**[12:57]** sizz some of our new work on like uh

**[12:57]** sizz some of our new work on like uh like pushing the boundary of code eval

**[12:59]** like pushing the boundary of code eval

**[12:59]** like pushing the boundary of code eval even further and uh taking a look at


### [13:00 - 14:00]

**[13:01]** even further and uh taking a look at

**[13:01]** even further and uh taking a look at more challenging tasks. So here we were

**[13:05]** more challenging tasks. So here we were

**[13:05]** more challenging tasks. So here we were thinking about like can uh like these

**[13:07]** thinking about like can uh like these

**[13:07]** thinking about like can uh like these language models translate uh like a

**[13:09]** language models translate uh like a

**[13:09]** language models translate uh like a entire code base uh specifically given a

**[13:11]** entire code base uh specifically given a

**[13:12]** entire code base uh specifically given a specification as a C program can you

**[13:13]** specification as a C program can you

**[13:13]** specification as a C program can you generate a safe implementation for the

**[13:15]** generate a safe implementation for the

**[13:15]** generate a safe implementation for the same and we took a fairly complex code

**[13:18]** same and we took a fairly complex code

**[13:18]** same and we took a fairly complex code base. So Zofle is a like highly

**[13:20]** base. So Zofle is a like highly

**[13:20]** base. So Zofle is a like highly efficient compression library from

**[13:22]** efficient compression library from

**[13:22]** efficient compression library from Google like it has about like 4,000

**[13:24]** Google like it has about like 4,000

**[13:24]** Google like it has about like 4,000 lines of code hundreds of functions and

**[13:26]** lines of code hundreds of functions and

**[13:26]** lines of code hundreds of functions and complex data structures. uh and uh we

**[13:29]** complex data structures. uh and uh we

**[13:29]** complex data structures. uh and uh we want like u like very precise and

**[13:31]** want like u like very precise and

**[13:31]** want like u like very precise and correct code. So we uh generated like a

**[13:33]** correct code. So we uh generated like a

**[13:33]** correct code. So we uh generated like a million compression inputs and your test

**[13:34]** million compression inputs and your test

**[13:34]** million compression inputs and your test case was to generate a rest

**[13:35]** case was to generate a rest

**[13:36]** case was to generate a rest implementation that uh maintains

**[13:37]** implementation that uh maintains

**[13:37]** implementation that uh maintains correctness over those million test

**[13:39]** correctness over those million test

**[13:39]** correctness over those million test cases. And when I did this work back in

**[13:41]** cases. And when I did this work back in

**[13:42]** cases. And when I did this work back in uh like uh last year it took us 12 hours

**[13:44]** uh like uh last year it took us 12 hours

**[13:44]** uh like uh last year it took us 12 hours to actually do this translation. Now

**[13:46]** to actually do this translation. Now

**[13:46]** to actually do this translation. Now perhaps with better models this can be

**[13:47]** perhaps with better models this can be

**[13:47]** perhaps with better models this can be done in 2 hours but still I think uh

**[13:49]** done in 2 hours but still I think uh

**[13:49]** done in 2 hours but still I think uh this is pushing the frontier of like

**[13:51]** this is pushing the frontier of like

**[13:51]** this is pushing the frontier of like what the models can do currently. Um so

**[13:54]** what the models can do currently. Um so

**[13:54]** what the models can do currently. Um so what was one of the key findings when we

**[13:55]** what was one of the key findings when we

**[13:56]** what was one of the key findings when we are trying to make progress in uh

**[13:57]** are trying to make progress in uh

**[13:57]** are trying to make progress in uh something like this like end to end

**[13:59]** something like this like end to end

**[13:59]** something like this like end to end correctness is important but it only


### [14:00 - 15:00]

**[14:01]** correctness is important but it only

**[14:01]** correctness is important but it only gives you like one bit of feedback but

**[14:03]** gives you like one bit of feedback but

**[14:03]** gives you like one bit of feedback but for these very long horizon tasks one

**[14:05]** for these very long horizon tasks one

**[14:05]** for these very long horizon tasks one thing which will become more important

**[14:07]** thing which will become more important

**[14:07]** thing which will become more important going forward is like having some

**[14:09]** going forward is like having some

**[14:09]** going forward is like having some measures of intermediate correctness. So

**[14:11]** measures of intermediate correctness. So

**[14:11]** measures of intermediate correctness. So like for our case we could measure like

**[14:13]** like for our case we could measure like

**[14:13]** like for our case we could measure like fraction of code translated, fraction of

**[14:16]** fraction of code translated, fraction of

**[14:16]** fraction of code translated, fraction of code refactored and based on these kind

**[14:17]** code refactored and based on these kind

**[14:18]** code refactored and based on these kind of settings you can uh understand like

**[14:20]** of settings you can uh understand like

**[14:20]** of settings you can uh understand like if you're making progress or not and how

**[14:21]** if you're making progress or not and how

**[14:22]** if you're making progress or not and how you can uh scale systems better.

**[14:25]** you can uh scale systems better.

**[14:25]** you can uh scale systems better. Um so like uh as we're closing I'll talk

**[14:27]** Um so like uh as we're closing I'll talk

**[14:27]** Um so like uh as we're closing I'll talk about like quickly talk about some of

**[14:29]** about like quickly talk about some of

**[14:29]** about like quickly talk about some of the work I did on like in the wilds. So

**[14:31]** the work I did on like in the wilds. So

**[14:31]** the work I did on like in the wilds. So this work was done in collaboration with

**[14:33]** this work was done in collaboration with

**[14:33]** this work was done in collaboration with LM arena folks and uh like I'll talk

**[14:36]** LM arena folks and uh like I'll talk

**[14:36]** LM arena folks and uh like I'll talk about two settings here. First is

**[14:37]** about two settings here. First is

**[14:37]** about two settings here. First is co-pilot arena. So this is like

**[14:39]** co-pilot arena. So this is like

**[14:39]** co-pilot arena. So this is like evaluating in ID uh code completion

**[14:42]** evaluating in ID uh code completion

**[14:42]** evaluating in ID uh code completion assistance. So what we will do here is

**[14:44]** assistance. So what we will do here is

**[14:44]** assistance. So what we will do here is we'll have an ID plug-in where uh like

**[14:47]** we'll have an ID plug-in where uh like

**[14:47]** we'll have an ID plug-in where uh like uh similar to GitHub copilot setting uh

**[14:49]** uh similar to GitHub copilot setting uh

**[14:49]** uh similar to GitHub copilot setting uh we'll generate a completion for you but

**[14:50]** we'll generate a completion for you but

**[14:50]** we'll generate a completion for you but instead of just a single completion

**[14:52]** instead of just a single completion

**[14:52]** instead of just a single completion you'll have two completions appearing

**[14:54]** you'll have two completions appearing

**[14:54]** you'll have two completions appearing like top and uh down and you can pick

**[14:57]** like top and uh down and you can pick

**[14:57]** like top and uh down and you can pick either one of them via shortcuts like

**[14:59]** either one of them via shortcuts like

**[14:59]** either one of them via shortcuts like tab or shift tab and based on the uh


### [15:00 - 16:00]

**[15:02]** tab or shift tab and based on the uh

**[15:02]** tab or shift tab and based on the uh like acceptance rates we can pair wise

**[15:04]** like acceptance rates we can pair wise

**[15:04]** like acceptance rates we can pair wise compare what the code completion

**[15:05]** compare what the code completion

**[15:05]** compare what the code completion assistants are doing.

**[15:08]** assistants are doing.

**[15:08]** assistants are doing. uh uh we also did some work on repo chat

**[15:10]** uh uh we also did some work on repo chat

**[15:10]** uh uh we also did some work on repo chat where uh like uh to evaluate uh like

**[15:13]** where uh like uh to evaluate uh like

**[15:13]** where uh like uh to evaluate uh like code question answering capabilities of

**[15:14]** code question answering capabilities of

**[15:14]** code question answering capabilities of models uh we uh built a system where you

**[15:17]** models uh we uh built a system where you

**[15:17]** models uh we uh built a system where you can provide a github url uh and you can

**[15:19]** can provide a github url uh and you can

**[15:19]** can provide a github url uh and you can ask a natural language query about the

**[15:21]** ask a natural language query about the

**[15:21]** ask a natural language query about the codebase which could be something what

**[15:22]** codebase which could be something what

**[15:22]** codebase which could be something what explain the codebase to as complex as

**[15:24]** explain the codebase to as complex as

**[15:24]** explain the codebase to as complex as let's try to solve this issue let's give

**[15:26]** let's try to solve this issue let's give

**[15:26]** let's try to solve this issue let's give me give me a model patch that could

**[15:28]** me give me a model patch that could

**[15:28]** me give me a model patch that could solve this issue and uh we integrated a

**[15:31]** solve this issue and uh we integrated a

**[15:31]** solve this issue and uh we integrated a very basic and simple uh like su agent

**[15:34]** very basic and simple uh like su agent

**[15:34]** very basic and simple uh like su agent system that fetches the codebase

**[15:35]** system that fetches the codebase

**[15:35]** system that fetches the codebase resolves user queries and like

**[15:37]** resolves user queries and like

**[15:37]** resolves user queries and like multi-turn uh code assistant uh

**[15:39]** multi-turn uh code assistant uh

**[15:39]** multi-turn uh code assistant uh conversations.

**[15:40]** conversations.

**[15:40]** conversations. So uh one thing that stood out to me in

**[15:43]** So uh one thing that stood out to me in

**[15:43]** So uh one thing that stood out to me in these kind of things uh is like like how

**[15:46]** these kind of things uh is like like how

**[15:46]** these kind of things uh is like like how humanentric experiment design uh needs

**[15:48]** humanentric experiment design uh needs

**[15:48]** humanentric experiment design uh needs to be. So uh like for code like copilot

**[15:51]** to be. So uh like for code like copilot

**[15:51]** to be. So uh like for code like copilot you know in particular we realized that

**[15:53]** you know in particular we realized that

**[15:53]** you know in particular we realized that like latency is a big concern for

**[15:55]** like latency is a big concern for

**[15:56]** like latency is a big concern for acceptance rates. So if you look at

**[15:58]** acceptance rates. So if you look at

**[15:58]** acceptance rates. So if you look at accept like latency below and the

**[15:59]** accept like latency below and the

**[15:59]** accept like latency below and the acceptance rates like if it is like


### [16:00 - 17:00]

**[16:01]** acceptance rates like if it is like

**[16:01]** acceptance rates like if it is like anything more than 1 second uh like the

**[16:03]** anything more than 1 second uh like the

**[16:03]** anything more than 1 second uh like the acceptance rates drop very starkly. So

**[16:06]** acceptance rates drop very starkly. So

**[16:06]** acceptance rates drop very starkly. So people care a lot about latency. So you

**[16:08]** people care a lot about latency. So you

**[16:08]** people care a lot about latency. So you have to so we had to design our

**[16:09]** have to so we had to design our

**[16:09]** have to so we had to design our experiment so that it's robust to these

**[16:11]** experiment so that it's robust to these

**[16:11]** experiment so that it's robust to these kind of like latency differences between

**[16:13]** kind of like latency differences between

**[16:13]** kind of like latency differences between models balance latency across different

**[16:15]** models balance latency across different

**[16:15]** models balance latency across different models. So like if you're doing like

**[16:17]** models. So like if you're doing like

**[16:17]** models. So like if you're doing like anything in the wild having this human

**[16:19]** anything in the wild having this human

**[16:19]** anything in the wild having this human centering component understanding human

**[16:21]** centering component understanding human

**[16:21]** centering component understanding human behaviors is very important to do

**[16:23]** behaviors is very important to do

**[16:23]** behaviors is very important to do anything meaningful.

**[16:25]** anything meaningful.

**[16:25]** anything meaningful. So uh at the end I think uh just to

**[16:27]** So uh at the end I think uh just to

**[16:27]** So uh at the end I think uh just to recap like I think I talked about a

**[16:29]** recap like I think I talked about a

**[16:29]** recap like I think I talked about a bunch of works like what are some uh big

**[16:31]** bunch of works like what are some uh big

**[16:31]** bunch of works like what are some uh big takeaways. So I think uh dynamic uh

**[16:34]** takeaways. So I think uh dynamic uh

**[16:34]** takeaways. So I think uh dynamic uh dynamically updating evaluation sets to

**[16:36]** dynamically updating evaluation sets to

**[16:36]** dynamically updating evaluation sets to like prevent contamination like modify

**[16:38]** like prevent contamination like modify

**[16:38]** like prevent contamination like modify the problem distributions like in terms

**[16:39]** the problem distributions like in terms

**[16:39]** the problem distributions like in terms of difficulty in terms of distribution

**[16:41]** of difficulty in terms of distribution

**[16:41]** of difficulty in terms of distribution of tasks we care about as we like uh

**[16:43]** of tasks we care about as we like uh

**[16:44]** of tasks we care about as we like uh improve uh as the language model

**[16:45]** improve uh as the language model

**[16:45]** improve uh as the language model capabilities will improve over time the

**[16:47]** capabilities will improve over time the

**[16:48]** capabilities will improve over time the types of tasks we'll start to do with

**[16:49]** types of tasks we'll start to do with

**[16:49]** types of tasks we'll start to do with model change. You can even uh think of

**[16:51]** model change. You can even uh think of

**[16:51]** model change. You can even uh think of this like uh we were doing like code

**[16:53]** this like uh we were doing like code

**[16:53]** this like uh we were doing like code completion where you were generating

**[16:54]** completion where you were generating

**[16:54]** completion where you were generating like few tokens, few lines and now we

**[16:56]** like few tokens, few lines and now we

**[16:56]** like few tokens, few lines and now we are generating like uh tens of lines,

**[16:58]** are generating like uh tens of lines,

**[16:58]** are generating like uh tens of lines, hundreds of lines and to some degree


### [17:00 - 18:00]

**[17:00]** hundreds of lines and to some degree

**[17:00]** hundreds of lines and to some degree this uh will continuously change and we

**[17:02]** this uh will continuously change and we

**[17:02]** this uh will continuously change and we have to update our evaluation sets uh so

**[17:04]** have to update our evaluation sets uh so

**[17:04]** have to update our evaluation sets uh so that it reflects the real world usage

**[17:06]** that it reflects the real world usage

**[17:06]** that it reflects the real world usage and kinds of things people need. Um the

**[17:09]** and kinds of things people need. Um the

**[17:09]** and kinds of things people need. Um the second very uh important thing is like

**[17:11]** second very uh important thing is like

**[17:11]** second very uh important thing is like ensuring reliable grading in this domain

**[17:13]** ensuring reliable grading in this domain

**[17:13]** ensuring reliable grading in this domain and like tests are very good for

**[17:15]** and like tests are very good for

**[17:15]** and like tests are very good for ensuring correctness and uh provide a

**[17:17]** ensuring correctness and uh provide a

**[17:17]** ensuring correctness and uh provide a lot of reliable feedback but uh once we

**[17:19]** lot of reliable feedback but uh once we

**[17:19]** lot of reliable feedback but uh once we go to real world settings like models

**[17:21]** go to real world settings like models

**[17:21]** go to real world settings like models can start doing like lot of non-edomatic

**[17:23]** can start doing like lot of non-edomatic

**[17:23]** can start doing like lot of non-edomatic coding patterns they would add try

**[17:25]** coding patterns they would add try

**[17:25]** coding patterns they would add try catches everywhere to just prevent any

**[17:26]** catches everywhere to just prevent any

**[17:26]** catches everywhere to just prevent any kind of bug from occurring. So having

**[17:28]** kind of bug from occurring. So having

**[17:28]** kind of bug from occurring. So having these kind of lm judges to detect

**[17:30]** these kind of lm judges to detect

**[17:30]** these kind of lm judges to detect nonmatic coding patterns code quality

**[17:32]** nonmatic coding patterns code quality

**[17:32]** nonmatic coding patterns code quality and just any like arbitrary hacks will

**[17:34]** and just any like arbitrary hacks will

**[17:34]** and just any like arbitrary hacks will be very important. And finally like as I

**[17:37]** be very important. And finally like as I

**[17:38]** be very important. And finally like as I talked about in the last work like

**[17:39]** talked about in the last work like

**[17:39]** talked about in the last work like intermediate grading signals so that you

**[17:41]** intermediate grading signals so that you

**[17:41]** intermediate grading signals so that you can measure like incremental progress uh

**[17:43]** can measure like incremental progress uh

**[17:43]** can measure like incremental progress uh is uh like another key factor here. So I

**[17:46]** is uh like another key factor here. So I

**[17:46]** is uh like another key factor here. So I think that's uh the end of my talk.

**[17:48]** think that's uh the end of my talk.

**[17:48]** think that's uh the end of my talk. Thank you.

**[17:50]** Thank you.

**[17:50]** Thank you. [applause]

**[17:51]** [applause]

**[17:51]** [applause] [music]


