# Fuzzing in the GenAI Era — Leonard Tang, Haize Labs

**Video URL:** https://www.youtube.com/watch?v=OMGPvW8TBHc

---

## Full Transcript

### [00:00 - 01:00]

**[00:17]** Thanks Ally for the great intro. Uh

**[00:17]** Thanks Ally for the great intro. Uh indeed we're working on what I believe

**[00:18]** indeed we're working on what I believe

**[00:18]** indeed we're working on what I believe to be the exant problem in AI which is

**[00:20]** to be the exant problem in AI which is

**[00:20]** to be the exant problem in AI which is to say how do you validate verify audit

**[00:23]** to say how do you validate verify audit

**[00:23]** to say how do you validate verify audit steer something that is as subjective

**[00:25]** steer something that is as subjective

**[00:25]** steer something that is as subjective and unstructured as literal LLM slop. So

**[00:28]** and unstructured as literal LLM slop. So

**[00:28]** and unstructured as literal LLM slop. So today we're going to be talking a lot

**[00:29]** today we're going to be talking a lot

**[00:29]** today we're going to be talking a lot about this. Um I should point out that

**[00:31]** about this. Um I should point out that

**[00:31]** about this. Um I should point out that ostensively we're part of the AI

**[00:32]** ostensively we're part of the AI

**[00:32]** ostensively we're part of the AI security track although I would really

**[00:34]** security track although I would really

**[00:34]** security track although I would really consider us more of a QA company and

**[00:36]** consider us more of a QA company and

**[00:36]** consider us more of a QA company and eval company in some sense although

**[00:38]** eval company in some sense although

**[00:38]** eval company in some sense although there's a lot of shared similarities in

**[00:39]** there's a lot of shared similarities in

**[00:39]** there's a lot of shared similarities in how we approach the problem technically

**[00:41]** how we approach the problem technically

**[00:41]** how we approach the problem technically right we are essentially a property

**[00:43]** right we are essentially a property

**[00:43]** right we are essentially a property based testing company or fuss testing

**[00:45]** based testing company or fuss testing

**[00:45]** based testing company or fuss testing company or as I like to call it a hazing

**[00:47]** company or as I like to call it a hazing

**[00:47]** company or as I like to call it a hazing company.

**[00:49]** company.

**[00:49]** company. Cool. So just to set the context a

**[00:51]** Cool. So just to set the context a

**[00:51]** Cool. So just to set the context a little bit uh why do we start haze? What

**[00:53]** little bit uh why do we start haze? What

**[00:53]** little bit uh why do we start haze? What does haze mean? haze to us is

**[00:55]** does haze mean? haze to us is

**[00:55]** does haze mean? haze to us is ultimately, all right, we know that AI

**[00:57]** ultimately, all right, we know that AI

**[00:57]** ultimately, all right, we know that AI systems are extremely unreliable.

**[00:58]** systems are extremely unreliable.

**[00:58]** systems are extremely unreliable. They're hard to trust in practice, and


### [01:00 - 02:00]

**[01:00]** They're hard to trust in practice, and

**[01:00]** They're hard to trust in practice, and you sort of need to pressure test them

**[01:02]** you sort of need to pressure test them

**[01:02]** you sort of need to pressure test them before you put them out into the wild.

**[01:04]** before you put them out into the wild.

**[01:04]** before you put them out into the wild. Our solution to doing this is basically,

**[01:06]** Our solution to doing this is basically,

**[01:06]** Our solution to doing this is basically, let's just run large scale optimization

**[01:08]** let's just run large scale optimization

**[01:08]** let's just run large scale optimization and simulation and search before

**[01:10]** and simulation and search before

**[01:10]** and simulation and search before deployment and try and figure out

**[01:11]** deployment and try and figure out

**[01:11]** deployment and try and figure out through a battery of tests whether or

**[01:13]** through a battery of tests whether or

**[01:13]** through a battery of tests whether or not your system will behave as expected

**[01:15]** not your system will behave as expected

**[01:15]** not your system will behave as expected before it actually goes into production.

**[01:18]** before it actually goes into production.

**[01:18]** before it actually goes into production. And I'm sure any of you guys who have

**[01:20]** And I'm sure any of you guys who have

**[01:20]** And I'm sure any of you guys who have tried to build LLM apps in the past have

**[01:22]** tried to build LLM apps in the past have

**[01:22]** tried to build LLM apps in the past have understood extremely viscerally uh what

**[01:25]** understood extremely viscerally uh what

**[01:25]** understood extremely viscerally uh what I mean when I say the last mile problem

**[01:26]** I mean when I say the last mile problem

**[01:26]** I mean when I say the last mile problem in AI, right? It's at this point in 2025

**[01:29]** in AI, right? It's at this point in 2025

**[01:29]** in AI, right? It's at this point in 2025 extremely easy to get something that is

**[01:32]** extremely easy to get something that is

**[01:32]** extremely easy to get something that is demo ready uh or PC ready. Like you can

**[01:34]** demo ready uh or PC ready. Like you can

**[01:34]** demo ready uh or PC ready. Like you can whip together a cool product over the

**[01:36]** whip together a cool product over the

**[01:36]** whip together a cool product over the weekend and impress your PM and whatnot,

**[01:38]** weekend and impress your PM and whatnot,

**[01:38]** weekend and impress your PM and whatnot, but uh it's really hard to get that same

**[01:40]** but uh it's really hard to get that same

**[01:40]** but uh it's really hard to get that same product into production at a point where

**[01:42]** product into production at a point where

**[01:42]** product into production at a point where it's truly robust and enterprisegrade

**[01:44]** it's truly robust and enterprisegrade

**[01:44]** it's truly robust and enterprisegrade and reliable. And you know this has been

**[01:46]** and reliable. And you know this has been

**[01:46]** and reliable. And you know this has been the case for the past two plus years at

**[01:49]** the case for the past two plus years at

**[01:49]** the case for the past two plus years at this point right like we've been

**[01:50]** this point right like we've been

**[01:50]** this point right like we've been promised uh the allure of autonomy and

**[01:53]** promised uh the allure of autonomy and

**[01:53]** promised uh the allure of autonomy and agency and full gen AI and enterprise

**[01:56]** agency and full gen AI and enterprise

**[01:56]** agency and full gen AI and enterprise transformation for two plus years since

**[01:58]** transformation for two plus years since

**[01:58]** transformation for two plus years since chat GPT launched and we're still not


### [02:00 - 03:00]

**[02:00]** chat GPT launched and we're still not

**[02:00]** chat GPT launched and we're still not quite there right and I think it

**[02:01]** quite there right and I think it

**[02:02]** quite there right and I think it ultimately it's because we haven't

**[02:03]** ultimately it's because we haven't

**[02:03]** ultimately it's because we haven't solved this last mile problem around

**[02:05]** solved this last mile problem around

**[02:05]** solved this last mile problem around trust and reliability and risk

**[02:09]** trust and reliability and risk

**[02:09]** trust and reliability and risk so I think part of the big reasons we

**[02:10]** so I think part of the big reasons we

**[02:10]** so I think part of the big reasons we haven't solved this is because people

**[02:12]** haven't solved this is because people

**[02:12]** haven't solved this is because people still think about eval measuring your AI

**[02:14]** still think about eval measuring your AI

**[02:14]** still think about eval measuring your AI system in a very straightforward and

**[02:16]** system in a very straightforward and

**[02:16]** system in a very straightforward and naive sense which is easiest to explain

**[02:18]** naive sense which is easiest to explain

**[02:18]** naive sense which is easiest to explain uh as follows right I'm sure everybody

**[02:20]** uh as follows right I'm sure everybody

**[02:20]** uh as follows right I'm sure everybody has seen this idea of going out uh being

**[02:22]** has seen this idea of going out uh being

**[02:22]** has seen this idea of going out uh being a human subject matter expert collecting

**[02:24]** a human subject matter expert collecting

**[02:24]** a human subject matter expert collecting a finite static golden data set of

**[02:27]** a finite static golden data set of

**[02:27]** a finite static golden data set of inputs and then expected outputs ground

**[02:29]** inputs and then expected outputs ground

**[02:29]** inputs and then expected outputs ground truth outputs uh from the uh human and

**[02:32]** truth outputs uh from the uh human and

**[02:32]** truth outputs uh from the uh human and then basically running the inputs

**[02:33]** then basically running the inputs

**[02:34]** then basically running the inputs through a application getting the the

**[02:35]** through a application getting the the

**[02:35]** through a application getting the the actual output and then comparing it

**[02:36]** actual output and then comparing it

**[02:36]** actual output and then comparing it somehow with the the ground truth golden

**[02:38]** somehow with the the ground truth golden

**[02:38]** somehow with the the ground truth golden answers right this is how eval has been

**[02:41]** answers right this is how eval has been

**[02:41]** answers right this is how eval has been done forever uh since the birth of deep

**[02:45]** done forever uh since the birth of deep

**[02:45]** done forever uh since the birth of deep learning uh and prior but it doesn't

**[02:47]** learning uh and prior but it doesn't

**[02:47]** learning uh and prior but it doesn't quite hold up in the genai era

**[02:49]** quite hold up in the genai era

**[02:49]** quite hold up in the genai era specifically because of this property of

**[02:51]** specifically because of this property of

**[02:51]** specifically because of this property of geni systems which is what I like to

**[02:54]** geni systems which is what I like to

**[02:54]** geni systems which is what I like to call brittleleness or more technically

**[02:55]** call brittleleness or more technically

**[02:56]** call brittleleness or more technically lip shits discontinuity um and what I

**[02:58]** lip shits discontinuity um and what I

**[02:58]** lip shits discontinuity um and what I mean by this is you know people say AI


### [03:00 - 04:00]

**[03:00]** mean by this is you know people say AI

**[03:00]** mean by this is you know people say AI is sensitive AI is brittle AI is

**[03:02]** is sensitive AI is brittle AI is

**[03:02]** is sensitive AI is brittle AI is non-deterministic which is true this is

**[03:05]** non-deterministic which is true this is

**[03:05]** non-deterministic which is true this is all true but that's really not the main

**[03:08]** all true but that's really not the main

**[03:08]** all true but that's really not the main problem that makes AI so hard to deal

**[03:09]** problem that makes AI so hard to deal

**[03:09]** problem that makes AI so hard to deal with right nondeterminism is really fine

**[03:11]** with right nondeterminism is really fine

**[03:11]** with right nondeterminism is really fine if you set the temperature to zero yes

**[03:12]** if you set the temperature to zero yes

**[03:12]** if you set the temperature to zero yes there's like caching and weird systems

**[03:15]** there's like caching and weird systems

**[03:15]** there's like caching and weird systems uh quirks and all the LM providers that

**[03:17]** uh quirks and all the LM providers that

**[03:17]** uh quirks and all the LM providers that make it somewhat non-deterministic even

**[03:19]** make it somewhat non-deterministic even

**[03:19]** make it somewhat non-deterministic even at scale. But for the most part,

**[03:21]** at scale. But for the most part,

**[03:21]** at scale. But for the most part, nondeterminism really doesn't bite you

**[03:22]** nondeterminism really doesn't bite you

**[03:22]** nondeterminism really doesn't bite you too much when you're building a apps,

**[03:23]** too much when you're building a apps,

**[03:23]** too much when you're building a apps, right? You for the most part are

**[03:24]** right? You for the most part are

**[03:24]** right? You for the most part are constrain your outputs to temperature

**[03:26]** constrain your outputs to temperature

**[03:26]** constrain your outputs to temperature zero. You're running things through a

**[03:27]** zero. You're running things through a

**[03:27]** zero. You're running things through a workflow. It's fairly deterministic.

**[03:29]** workflow. It's fairly deterministic.

**[03:29]** workflow. It's fairly deterministic. What does bite you a lot when you're

**[03:30]** What does bite you a lot when you're

**[03:30]** What does bite you a lot when you're building AI apps though is when you send

**[03:33]** building AI apps though is when you send

**[03:33]** building AI apps though is when you send two ostensibly similar inputs to your AI

**[03:35]** two ostensibly similar inputs to your AI

**[03:35]** two ostensibly similar inputs to your AI application with maybe slight variance

**[03:37]** application with maybe slight variance

**[03:38]** application with maybe slight variance uh in the syntax or the semantics or the

**[03:41]** uh in the syntax or the semantics or the

**[03:41]** uh in the syntax or the semantics or the appearance of the text but all of a

**[03:43]** appearance of the text but all of a

**[03:43]** appearance of the text but all of a sudden you get wildly different outputs

**[03:44]** sudden you get wildly different outputs

**[03:44]** sudden you get wildly different outputs on the other side. Right? This is what I

**[03:46]** on the other side. Right? This is what I

**[03:46]** on the other side. Right? This is what I mean when I say gen apps are incredibly

**[03:48]** mean when I say gen apps are incredibly

**[03:48]** mean when I say gen apps are incredibly brittle. And I think this is the actual

**[03:50]** brittle. And I think this is the actual

**[03:50]** brittle. And I think this is the actual core property that makes building with

**[03:52]** core property that makes building with

**[03:52]** core property that makes building with AI uh with geni so difficult.

**[03:56]** AI uh with geni so difficult.

**[03:56]** AI uh with geni so difficult. And of course, we see this brittleless

**[03:57]** And of course, we see this brittleless

**[03:58]** And of course, we see this brittleless manifest itself in all sorts of fun


### [04:00 - 05:00]

**[04:00]** manifest itself in all sorts of fun

**[04:00]** manifest itself in all sorts of fun ways. I'm sure we don't have to blabber

**[04:01]** ways. I'm sure we don't have to blabber

**[04:01]** ways. I'm sure we don't have to blabber this point too much, but you've got

**[04:02]** this point too much, but you've got

**[04:02]** this point too much, but you've got everything from uh Air Canada customer

**[04:05]** everything from uh Air Canada customer

**[04:05]** everything from uh Air Canada customer supports hallucinating to, you know, uh

**[04:08]** supports hallucinating to, you know, uh

**[04:08]** supports hallucinating to, you know, uh character AI telling teenagers to commit

**[04:10]** character AI telling teenagers to commit

**[04:10]** character AI telling teenagers to commit suicide to um buying a pickup truck for

**[04:13]** suicide to um buying a pickup truck for

**[04:13]** suicide to um buying a pickup truck for $1 on the Chevy uh patient or customer

**[04:17]** $1 on the Chevy uh patient or customer

**[04:17]** $1 on the Chevy uh patient or customer portal, right? I I don't think we need

**[04:18]** portal, right? I I don't think we need

**[04:18]** portal, right? I I don't think we need to go through more examples of this.

**[04:20]** to go through more examples of this.

**[04:20]** to go through more examples of this. This happens more or less every single

**[04:21]** This happens more or less every single

**[04:21]** This happens more or less every single week. There's more and more examples

**[04:22]** week. There's more and more examples

**[04:22]** week. There's more and more examples popping out. Um and again this all comes

**[04:25]** popping out. Um and again this all comes

**[04:25]** popping out. Um and again this all comes back to geni being extremely sensitive

**[04:27]** back to geni being extremely sensitive

**[04:27]** back to geni being extremely sensitive and brittle to prohibition in the input

**[04:28]** and brittle to prohibition in the input

**[04:28]** and brittle to prohibition in the input space.

**[04:30]** space.

**[04:30]** space. Cool. So standard evals of course

**[04:32]** Cool. So standard evals of course

**[04:32]** Cool. So standard evals of course doesn't cover uh this brittleleness

**[04:34]** doesn't cover uh this brittleleness

**[04:34]** doesn't cover uh this brittleleness property and I would say it's

**[04:35]** property and I would say it's

**[04:35]** property and I would say it's insufficient in two senses two primary

**[04:37]** insufficient in two senses two primary

**[04:37]** insufficient in two senses two primary senses. One is coverage right? Uh with a

**[04:40]** senses. One is coverage right? Uh with a

**[04:40]** senses. One is coverage right? Uh with a static data set you only know how good

**[04:43]** static data set you only know how good

**[04:43]** static data set you only know how good your AI system will be with respect to

**[04:45]** your AI system will be with respect to

**[04:45]** your AI system will be with respect to that data set. Right? It might look like

**[04:46]** that data set. Right? It might look like

**[04:46]** that data set. Right? It might look like your AI system is 100% on all your unit

**[04:49]** your AI system is 100% on all your unit

**[04:49]** your AI system is 100% on all your unit tests on all your golden data set

**[04:50]** tests on all your golden data set

**[04:50]** tests on all your golden data set points. But if you just push around the

**[04:53]** points. But if you just push around the

**[04:53]** points. But if you just push around the corner and look around the corner for

**[04:54]** corner and look around the corner for

**[04:54]** corner and look around the corner for more inputs that cover your space more

**[04:56]** more inputs that cover your space more

**[04:56]** more inputs that cover your space more densely, it is entirely possible that

**[04:58]** densely, it is entirely possible that

**[04:58]** densely, it is entirely possible that you get prohibations that tell a very


### [05:00 - 06:00]

**[05:00]** you get prohibations that tell a very

**[05:00]** you get prohibations that tell a very very different story about how your AI

**[05:01]** very different story about how your AI

**[05:01]** very different story about how your AI application actually does in the wild.

**[05:03]** application actually does in the wild.

**[05:03]** application actually does in the wild. So point number one, standard eval don't

**[05:05]** So point number one, standard eval don't

**[05:05]** So point number one, standard eval don't have sufficient coverage.

**[05:08]** have sufficient coverage.

**[05:08]** have sufficient coverage. Second point too is it's actually really

**[05:11]** Second point too is it's actually really

**[05:11]** Second point too is it's actually really difficult to come up with a good measure

**[05:13]** difficult to come up with a good measure

**[05:13]** difficult to come up with a good measure of quality uh or even similarity uh

**[05:16]** of quality uh or even similarity uh

**[05:16]** of quality uh or even similarity uh between the outputs of your application

**[05:17]** between the outputs of your application

**[05:18]** between the outputs of your application and your ground truth outputs. Really

**[05:20]** and your ground truth outputs. Really

**[05:20]** and your ground truth outputs. Really what we would want almost is a human

**[05:22]** what we would want almost is a human

**[05:22]** what we would want almost is a human subject matter expert who is constantly

**[05:24]** subject matter expert who is constantly

**[05:24]** subject matter expert who is constantly overseeing your AI application and a

**[05:27]** overseeing your AI application and a

**[05:27]** overseeing your AI application and a subject matter expert who has all the

**[05:28]** subject matter expert who has all the

**[05:28]** subject matter expert who has all the right taste and sensitivity but is able

**[05:30]** right taste and sensitivity but is able

**[05:30]** right taste and sensitivity but is able to translate that sensitivity into some

**[05:32]** to translate that sensitivity into some

**[05:32]** to translate that sensitivity into some quantitative metric. This by no means is

**[05:34]** quantitative metric. This by no means is

**[05:34]** quantitative metric. This by no means is a trivial task, right? I think this is

**[05:36]** a trivial task, right? I think this is

**[05:36]** a trivial task, right? I think this is the core challenge that we've been

**[05:37]** the core challenge that we've been

**[05:37]** the core challenge that we've been trying to face in the field of AI around

**[05:39]** trying to face in the field of AI around

**[05:39]** trying to face in the field of AI around reward modeling for the past five, six,

**[05:41]** reward modeling for the past five, six,

**[05:41]** reward modeling for the past five, six, seven plus years, right? Uh and the key

**[05:44]** seven plus years, right? Uh and the key

**[05:44]** seven plus years, right? Uh and the key challenge is how do you get that

**[05:45]** challenge is how do you get that

**[05:45]** challenge is how do you get that sensitivity from the subject matter

**[05:46]** sensitivity from the subject matter

**[05:46]** sensitivity from the subject matter expert from a nontechnical domain to be

**[05:48]** expert from a nontechnical domain to be

**[05:48]** expert from a nontechnical domain to be able to translate their criteria into

**[05:51]** able to translate their criteria into

**[05:51]** able to translate their criteria into quantitative measures. This is not even

**[05:54]** quantitative measures. This is not even

**[05:54]** quantitative measures. This is not even close to something that's being solved

**[05:55]** close to something that's being solved

**[05:55]** close to something that's being solved with standard evals today. People are

**[05:57]** with standard evals today. People are

**[05:57]** with standard evals today. People are using things like exact match, um

**[05:59]** using things like exact match, um

**[05:59]** using things like exact match, um classifiers, LM as a judge, semantic


### [06:00 - 07:00]

**[06:01]** classifiers, LM as a judge, semantic

**[06:01]** classifiers, LM as a judge, semantic solinity. All these things have their

**[06:02]** solinity. All these things have their

**[06:02]** solinity. All these things have their own sets of uh quirks and undesira and

**[06:06]** own sets of uh quirks and undesira and

**[06:06]** own sets of uh quirks and undesira and we'll see how this this pans out in a

**[06:08]** we'll see how this this pans out in a

**[06:08]** we'll see how this this pans out in a second.

**[06:10]** second.

**[06:10]** second. Long story short of how uh we think

**[06:12]** Long story short of how uh we think

**[06:12]** Long story short of how uh we think about tackling this eval problem is

**[06:14]** about tackling this eval problem is

**[06:14]** about tackling this eval problem is essentially through hazing right fuss

**[06:16]** essentially through hazing right fuss

**[06:16]** essentially through hazing right fuss testing in the AI era. Essentially what

**[06:18]** testing in the AI era. Essentially what

**[06:18]** testing in the AI era. Essentially what hazing comprises is very simple in the

**[06:20]** hazing comprises is very simple in the

**[06:20]** hazing comprises is very simple in the abstract. We just simulate uh large

**[06:22]** abstract. We just simulate uh large

**[06:22]** abstract. We just simulate uh large scale uh stimuli to send to your AI

**[06:24]** scale uh stimuli to send to your AI

**[06:24]** scale uh stimuli to send to your AI application. We get the responses as a

**[06:26]** application. We get the responses as a

**[06:26]** application. We get the responses as a result of the stimuli. We judge and

**[06:29]** result of the stimuli. We judge and

**[06:29]** result of the stimuli. We judge and analyze and score the outputs of your AI

**[06:31]** analyze and score the outputs of your AI

**[06:31]** analyze and score the outputs of your AI application. And we use that as a signal

**[06:33]** application. And we use that as a signal

**[06:33]** application. And we use that as a signal to help guide the next round of search,

**[06:35]** to help guide the next round of search,

**[06:35]** to help guide the next round of search, right? And we essentially just do this

**[06:36]** right? And we essentially just do this

**[06:36]** right? And we essentially just do this iteratively until we discover some bugs

**[06:37]** iteratively until we discover some bugs

**[06:38]** iteratively until we discover some bugs and corner cases that break your AI

**[06:39]** and corner cases that break your AI

**[06:39]** and corner cases that break your AI application. Uh if we don't discover

**[06:41]** application. Uh if we don't discover

**[06:41]** application. Uh if we don't discover anything and we exhaust our search

**[06:42]** anything and we exhaust our search

**[06:42]** anything and we exhaust our search budget, that that means you're

**[06:44]** budget, that that means you're

**[06:44]** budget, that that means you're essentially ready for production, right?

**[06:45]** essentially ready for production, right?

**[06:45]** essentially ready for production, right? So this is hazing in a nutshell.

**[06:49]** So this is hazing in a nutshell.

**[06:49]** So this is hazing in a nutshell. But easy to easy to describe, actually

**[06:52]** But easy to easy to describe, actually

**[06:52]** But easy to easy to describe, actually really difficult to execute in practice.

**[06:54]** really difficult to execute in practice.

**[06:54]** really difficult to execute in practice. um both sides of the equation in terms

**[06:56]** um both sides of the equation in terms

**[06:56]** um both sides of the equation in terms of scoring the output and also

**[06:57]** of scoring the output and also

**[06:57]** of scoring the output and also generating the input stimuli are quite

**[06:59]** generating the input stimuli are quite

**[06:59]** generating the input stimuli are quite difficult technically. Um I'll first


### [07:00 - 08:00]

**[07:01]** difficult technically. Um I'll first

**[07:01]** difficult technically. Um I'll first talk about how do we think about scoring

**[07:02]** talk about how do we think about scoring

**[07:02]** talk about how do we think about scoring the output again translating from

**[07:04]** the output again translating from

**[07:04]** the output again translating from subjective criteria into quantitative

**[07:06]** subjective criteria into quantitative

**[07:06]** subjective criteria into quantitative metrics. Uh we call this judging more

**[07:08]** metrics. Uh we call this judging more

**[07:08]** metrics. Uh we call this judging more broadly.

**[07:10]** broadly.

**[07:10]** broadly. Probably you guys are familiar with uh

**[07:12]** Probably you guys are familiar with uh

**[07:12]** Probably you guys are familiar with uh something like using LM as a judge to

**[07:15]** something like using LM as a judge to

**[07:15]** something like using LM as a judge to essentially have an LM look at the

**[07:17]** essentially have an LM look at the

**[07:17]** essentially have an LM look at the output of your AI application and decide

**[07:19]** output of your AI application and decide

**[07:19]** output of your AI application and decide you know based on some prompt or rubric

**[07:21]** you know based on some prompt or rubric

**[07:21]** you know based on some prompt or rubric that you give to your judge you know is

**[07:22]** that you give to your judge you know is

**[07:22]** that you give to your judge you know is this a good response or is this a bad

**[07:24]** this a good response or is this a bad

**[07:24]** this a good response or is this a bad response tell me on a scale from 1 to

**[07:25]** response tell me on a scale from 1 to

**[07:25]** response tell me on a scale from 1 to five or 1 to 10 or what have you right

**[07:28]** five or 1 to 10 or what have you right

**[07:28]** five or 1 to 10 or what have you right very simple to do but it has its uh

**[07:30]** very simple to do but it has its uh

**[07:30]** very simple to do but it has its uh whole large array of different failure

**[07:32]** whole large array of different failure

**[07:32]** whole large array of different failure modes in particular LM as a judge itself

**[07:34]** modes in particular LM as a judge itself

**[07:34]** modes in particular LM as a judge itself is prone to hallucinations it's it is

**[07:37]** is prone to hallucinations it's it is

**[07:37]** is prone to hallucinations it's it is obviously an LLM so it's prone to

**[07:39]** obviously an LLM so it's prone to

**[07:39]** obviously an LLM so it's prone to hallucination conditions it is uh

**[07:41]** hallucination conditions it is uh

**[07:41]** hallucination conditions it is uh unstable. you could have actually really

**[07:43]** unstable. you could have actually really

**[07:43]** unstable. you could have actually really good articulation of the criteria but it

**[07:45]** good articulation of the criteria but it

**[07:45]** good articulation of the criteria but it doesn't actually operationalize well

**[07:46]** doesn't actually operationalize well

**[07:46]** doesn't actually operationalize well into a model right so it's um uh

**[07:49]** into a model right so it's um uh

**[07:49]** into a model right so it's um uh unccalibrated in the output right like a

**[07:51]** unccalibrated in the output right like a

**[07:51]** unccalibrated in the output right like a what is what is a one to an LLM that's

**[07:53]** what is what is a one to an LLM that's

**[07:53]** what is what is a one to an LLM that's very different to what is a one to a

**[07:55]** very different to what is a one to a

**[07:55]** very different to what is a one to a human right what is a five to a human is

**[07:57]** human right what is a five to a human is

**[07:57]** human right what is a five to a human is very different to what a what is a five

**[07:59]** very different to what a what is a five

**[07:59]** very different to what a what is a five to an LM so it's unccalibrated uh it has


### [08:00 - 09:00]

**[08:01]** to an LM so it's unccalibrated uh it has

**[08:01]** to an LM so it's unccalibrated uh it has all sorts of biases right if you change

**[08:03]** all sorts of biases right if you change

**[08:03]** all sorts of biases right if you change the inputs uh in any weird position

**[08:05]** the inputs uh in any weird position

**[08:05]** the inputs uh in any weird position right let's say you present uh one

**[08:07]** right let's say you present uh one

**[08:07]** right let's say you present uh one response first and the second response

**[08:08]** response first and the second response

**[08:08]** response first and the second response if you flip the order that changes the

**[08:09]** if you flip the order that changes the

**[08:09]** if you flip the order that changes the results often time uh if provide context

**[08:12]** results often time uh if provide context

**[08:12]** results often time uh if provide context or you change some part some some part

**[08:13]** or you change some part some some part

**[08:13]** or you change some part some some part of your rubric that changes the result

**[08:15]** of your rubric that changes the result

**[08:15]** of your rubric that changes the result of the LM as a judge too. So extremely

**[08:17]** of the LM as a judge too. So extremely

**[08:17]** of the LM as a judge too. So extremely biased extremely fickle and TLDDR LM as

**[08:20]** biased extremely fickle and TLDDR LM as

**[08:20]** biased extremely fickle and TLDDR LM as a judge itself uh as an off the call

**[08:22]** a judge itself uh as an off the call

**[08:22]** a judge itself uh as an off the call call offtheshelf call to an LM is

**[08:24]** call offtheshelf call to an LM is

**[08:24]** call offtheshelf call to an LM is oftentimes not going to solve your uh

**[08:26]** oftentimes not going to solve your uh

**[08:26]** oftentimes not going to solve your uh reliability issues.

**[08:29]** reliability issues.

**[08:29]** reliability issues. So the key question in my mind is how do

**[08:31]** So the key question in my mind is how do

**[08:31]** So the key question in my mind is how do you actually QA the judge itself, right?

**[08:33]** you actually QA the judge itself, right?

**[08:33]** you actually QA the judge itself, right? How do you get to a point where you can

**[08:35]** How do you get to a point where you can

**[08:35]** How do you get to a point where you can judge the judge and say that this is the

**[08:36]** judge the judge and say that this is the

**[08:36]** judge the judge and say that this is the best gold standard metric that I can use

**[08:38]** best gold standard metric that I can use

**[08:38]** best gold standard metric that I can use to then actually iterate uh my

**[08:40]** to then actually iterate uh my

**[08:40]** to then actually iterate uh my underlying AI application against. So

**[08:42]** underlying AI application against. So

**[08:42]** underlying AI application against. So how do you judge this judge?

**[08:45]** how do you judge this judge?

**[08:45]** how do you judge this judge? The broad philosophy that uh we've been

**[08:47]** The broad philosophy that uh we've been

**[08:47]** The broad philosophy that uh we've been taking over the past few months is

**[08:49]** taking over the past few months is

**[08:49]** taking over the past few months is essentially pushing the idea of

**[08:51]** essentially pushing the idea of

**[08:51]** essentially pushing the idea of inference time scaling or more broadly

**[08:53]** inference time scaling or more broadly

**[08:53]** inference time scaling or more broadly compute time scaling to the judging

**[08:55]** compute time scaling to the judging

**[08:55]** compute time scaling to the judging stage. So we call this scaling judge

**[08:57]** stage. So we call this scaling judge

**[08:57]** stage. So we call this scaling judge time compute. And there's two ends of


### [09:00 - 10:00]

**[09:00]** time compute. And there's two ends of

**[09:00]** time compute. And there's two ends of the spectrum of this philosophy. One end

**[09:02]** the spectrum of this philosophy. One end

**[09:02]** the spectrum of this philosophy. One end of the spectrum is basically just rip

**[09:04]** of the spectrum is basically just rip

**[09:04]** of the spectrum is basically just rip from scratch. No inductive biases. Train

**[09:07]** from scratch. No inductive biases. Train

**[09:07]** from scratch. No inductive biases. Train reasoning models that get really really

**[09:08]** reasoning models that get really really

**[09:08]** reasoning models that get really really good at this evaluation task. Um and

**[09:10]** good at this evaluation task. Um and

**[09:10]** good at this evaluation task. Um and then the other end of the spectrum is be

**[09:12]** then the other end of the spectrum is be

**[09:12]** then the other end of the spectrum is be very structured. Uh you know don't train

**[09:14]** very structured. Uh you know don't train

**[09:14]** very structured. Uh you know don't train any models. Just use the offtheshelf LMS

**[09:17]** any models. Just use the offtheshelf LMS

**[09:17]** any models. Just use the offtheshelf LMS have really strong inductive prior but

**[09:18]** have really strong inductive prior but

**[09:18]** have really strong inductive prior but basically build agents as judges. Right?

**[09:21]** basically build agents as judges. Right?

**[09:21]** basically build agents as judges. Right? So this is one approach. Basically,

**[09:23]** So this is one approach. Basically,

**[09:23]** So this is one approach. Basically, we'll build agent frameworks, pipelines,

**[09:25]** we'll build agent frameworks, pipelines,

**[09:25]** we'll build agent frameworks, pipelines, workflows to do the judging task. And we

**[09:28]** workflows to do the judging task. And we

**[09:28]** workflows to do the judging task. And we have this nice little library called uh

**[09:30]** have this nice little library called uh

**[09:30]** have this nice little library called uh verdict uh that does this. Very on the

**[09:32]** verdict uh that does this. Very on the

**[09:32]** verdict uh that does this. Very on the nose name, I know. Um but the idea of

**[09:33]** nose name, I know. Um but the idea of

**[09:33]** nose name, I know. Um but the idea of verdict is essentially there's a lot of

**[09:35]** verdict is essentially there's a lot of

**[09:35]** verdict is essentially there's a lot of great intuition from the scalable

**[09:38]** great intuition from the scalable

**[09:38]** great intuition from the scalable oversight community, which is subfield

**[09:40]** oversight community, which is subfield

**[09:40]** oversight community, which is subfield of AI safety. Goal of scalable oversight

**[09:42]** of AI safety. Goal of scalable oversight

**[09:42]** of AI safety. Goal of scalable oversight is basically how do you take smaller

**[09:43]** is basically how do you take smaller

**[09:43]** is basically how do you take smaller language models and have them audit uh

**[09:45]** language models and have them audit uh

**[09:45]** language models and have them audit uh and correct and steer stronger models.

**[09:48]** and correct and steer stronger models.

**[09:48]** and correct and steer stronger models. Originally this is an AI safety concept

**[09:50]** Originally this is an AI safety concept

**[09:50]** Originally this is an AI safety concept because people were worried about you

**[09:51]** because people were worried about you

**[09:52]** because people were worried about you know in the age of superhuman AI how do

**[09:54]** know in the age of superhuman AI how do

**[09:54]** know in the age of superhuman AI how do you have weaker models i.e humans

**[09:55]** you have weaker models i.e humans

**[09:55]** you have weaker models i.e humans control the stronger models, right? And

**[09:57]** control the stronger models, right? And

**[09:57]** control the stronger models, right? And that's how the field got started. But as

**[09:59]** that's how the field got started. But as

**[09:59]** that's how the field got started. But as a result of scalable oversight, there's


### [10:00 - 11:00]

**[10:00]** a result of scalable oversight, there's

**[10:00]** a result of scalable oversight, there's been a lot of great intuition around the

**[10:02]** been a lot of great intuition around the

**[10:02]** been a lot of great intuition around the architectures and primitives uh and

**[10:04]** architectures and primitives uh and

**[10:04]** architectures and primitives uh and units that you would use to probe and

**[10:06]** units that you would use to probe and

**[10:06]** units that you would use to probe and reason and uh critique what a stronger

**[10:09]** reason and uh critique what a stronger

**[10:09]** reason and uh critique what a stronger model is doing. And so we baked a lot of

**[10:11]** model is doing. And so we baked a lot of

**[10:11]** model is doing. And so we baked a lot of those primitives uh and architectures

**[10:13]** those primitives uh and architectures

**[10:13]** those primitives uh and architectures into this vertic library. One example is

**[10:15]** into this vertic library. One example is

**[10:15]** into this vertic library. One example is having LMS debate each other, having the

**[10:16]** having LMS debate each other, having the

**[10:16]** having LMS debate each other, having the weaker LLMs debate each other about what

**[10:18]** weaker LLMs debate each other about what

**[10:18]** weaker LLMs debate each other about what the stronger model is saying and seeing

**[10:20]** the stronger model is saying and seeing

**[10:20]** the stronger model is saying and seeing if that makes sense. Uh another example

**[10:22]** if that makes sense. Uh another example

**[10:22]** if that makes sense. Uh another example is having the LLM's weaker LMS

**[10:24]** is having the LLM's weaker LMS

**[10:24]** is having the LLM's weaker LMS self-verify the results of their own

**[10:25]** self-verify the results of their own

**[10:26]** self-verify the results of their own responses. Right? So you know have an LM

**[10:28]** responses. Right? So you know have an LM

**[10:28]** responses. Right? So you know have an LM say okay this response of the stronger

**[10:30]** say okay this response of the stronger

**[10:30]** say okay this response of the stronger model is good or bad. It is bad for this

**[10:32]** model is good or bad. It is bad for this

**[10:32]** model is good or bad. It is bad for this reason and then maybe having an LM

**[10:34]** reason and then maybe having an LM

**[10:34]** reason and then maybe having an LM critique its own reasoning right. So SE

**[10:36]** critique its own reasoning right. So SE

**[10:36]** critique its own reasoning right. So SE verification is another great primitive.

**[10:37]** verification is another great primitive.

**[10:37]** verification is another great primitive. Um ensembling of course another another

**[10:40]** Um ensembling of course another another

**[10:40]** Um ensembling of course another another uh classic primitive in this case and so

**[10:42]** uh classic primitive in this case and so

**[10:42]** uh classic primitive in this case and so on and so forth.

**[10:45]** on and so forth.

**[10:45]** on and so forth. TLDDR scaling judge time compute in this

**[10:47]** TLDDR scaling judge time compute in this

**[10:47]** TLDDR scaling judge time compute in this particular way uh through building

**[10:49]** particular way uh through building

**[10:49]** particular way uh through building agents as judges actually allows you to

**[10:51]** agents as judges actually allows you to

**[10:51]** agents as judges actually allows you to come up with extremely powerful judging

**[10:54]** come up with extremely powerful judging

**[10:54]** come up with extremely powerful judging systems that are also quite cheap and

**[10:55]** systems that are also quite cheap and

**[10:55]** systems that are also quite cheap and also uh low latency. So here's a plot of

**[10:58]** also uh low latency. So here's a plot of

**[10:58]** also uh low latency. So here's a plot of price uh and latency and cost uh and and


### [11:00 - 12:00]

**[11:01]** price uh and latency and cost uh and and

**[11:01]** price uh and latency and cost uh and and accuracy uh of verdict systems visav uh

**[11:04]** accuracy uh of verdict systems visav uh

**[11:04]** accuracy uh of verdict systems visav uh some of the frontier models uh Frontier

**[11:06]** some of the frontier models uh Frontier

**[11:06]** some of the frontier models uh Frontier Labs reasoning models. So you can see

**[11:08]** Labs reasoning models. So you can see

**[11:08]** Labs reasoning models. So you can see that verdict is beating uh 01 and 03

**[11:10]** that verdict is beating uh 01 and 03

**[11:10]** that verdict is beating uh 01 and 03 mini and of course GP4 and 3.5 sonnets

**[11:12]** mini and of course GP4 and 3.5 sonnets

**[11:12]** mini and of course GP4 and 3.5 sonnets um on the task of expert QA

**[11:15]** um on the task of expert QA

**[11:15]** um on the task of expert QA verification. So this is uh subjective

**[11:17]** verification. So this is uh subjective

**[11:17]** verification. So this is uh subjective criteria grading in expert domains. Um

**[11:20]** criteria grading in expert domains. Um

**[11:20]** criteria grading in expert domains. Um critically verdict here is powered by a

**[11:21]** critically verdict here is powered by a

**[11:21]** critically verdict here is powered by a GP40 mini backbone. Right? So we

**[11:24]** GP40 mini backbone. Right? So we

**[11:24]** GP40 mini backbone. Right? So we basically have stacked GPU GP40 mini

**[11:26]** basically have stacked GPU GP40 mini

**[11:26]** basically have stacked GPU GP40 mini aggressively and what is in this case

**[11:28]** aggressively and what is in this case

**[11:28]** aggressively and what is in this case like a self-verified debate ensemble uh

**[11:31]** like a self-verified debate ensemble uh

**[11:31]** like a self-verified debate ensemble uh architecture and we're able to beat 01

**[11:34]** architecture and we're able to beat 01

**[11:34]** architecture and we're able to beat 01 for a fraction of the cost like less

**[11:35]** for a fraction of the cost like less

**[11:35]** for a fraction of the cost like less than a third of the cost right and also

**[11:37]** than a third of the cost right and also

**[11:37]** than a third of the cost right and also uh like less than a third of the latency

**[11:40]** uh like less than a third of the latency

**[11:40]** uh like less than a third of the latency and this is all because of we have of

**[11:42]** and this is all because of we have of

**[11:42]** and this is all because of we have of the fact that we've chosen the priors in

**[11:43]** the fact that we've chosen the priors in

**[11:43]** the fact that we've chosen the priors in a pretty careful and uh intelligent way.

**[11:47]** a pretty careful and uh intelligent way.

**[11:47]** a pretty careful and uh intelligent way. So that's one way to scale just time

**[11:49]** So that's one way to scale just time

**[11:49]** So that's one way to scale just time compute is basically building agents uh

**[11:50]** compute is basically building agents uh

**[11:50]** compute is basically building agents uh to do the task.

**[11:53]** to do the task.

**[11:53]** to do the task. Other way to do it and this is a lot

**[11:55]** Other way to do it and this is a lot

**[11:55]** Other way to do it and this is a lot more fun in my opinion is basically yeah

**[11:56]** more fun in my opinion is basically yeah

**[11:56]** more fun in my opinion is basically yeah just rip RL from scratch train models to

**[11:58]** just rip RL from scratch train models to

**[11:58]** just rip RL from scratch train models to do the judging task and this is


### [12:00 - 13:00]

**[12:00]** do the judging task and this is

**[12:00]** do the judging task and this is something that we've also been pretty

**[12:01]** something that we've also been pretty

**[12:01]** something that we've also been pretty excited about over the past few months.

**[12:02]** excited about over the past few months.

**[12:02]** excited about over the past few months. Um again uh for standard LM judges whole

**[12:05]** Um again uh for standard LM judges whole

**[12:05]** Um again uh for standard LM judges whole host of issues but two particular issues

**[12:07]** host of issues but two particular issues

**[12:07]** host of issues but two particular issues that are solved by RL is one uh there's

**[12:09]** that are solved by RL is one uh there's

**[12:09]** that are solved by RL is one uh there's a lack of coherent ration that explain

**[12:11]** a lack of coherent ration that explain

**[12:11]** a lack of coherent ration that explain why an LM judge thinks something is a

**[12:13]** why an LM judge thinks something is a

**[12:13]** why an LM judge thinks something is a five out of five or thinks something is

**[12:14]** five out of five or thinks something is

**[12:14]** five out of five or thinks something is good or bad and also standard elements

**[12:17]** good or bad and also standard elements

**[12:17]** good or bad and also standard elements of judge doesn't provide real uh fine

**[12:20]** of judge doesn't provide real uh fine

**[12:20]** of judge doesn't provide real uh fine grained tailored unique criteria to

**[12:22]** grained tailored unique criteria to

**[12:22]** grained tailored unique criteria to whatever idiosyncratic task and data

**[12:24]** whatever idiosyncratic task and data

**[12:24]** whatever idiosyncratic task and data you're looking at. Uh but both of these

**[12:26]** you're looking at. Uh but both of these

**[12:26]** you're looking at. Uh but both of these can be solved by uh RL tuning or

**[12:28]** can be solved by uh RL tuning or

**[12:28]** can be solved by uh RL tuning or specifically GRPO tuning. Uh one paper

**[12:30]** specifically GRPO tuning. Uh one paper

**[12:30]** specifically GRPO tuning. Uh one paper recently that uh has come out in this

**[12:33]** recently that uh has come out in this

**[12:33]** recently that uh has come out in this general flavor is from deepseek. This is

**[12:35]** general flavor is from deepseek. This is

**[12:35]** general flavor is from deepseek. This is SPCT self-principled critique tuning.

**[12:38]** SPCT self-principled critique tuning.

**[12:38]** SPCT self-principled critique tuning. The idea here is essentially can you get

**[12:40]** The idea here is essentially can you get

**[12:40]** The idea here is essentially can you get uh an LM to first propose some data set

**[12:44]** uh an LM to first propose some data set

**[12:44]** uh an LM to first propose some data set or sorry data point specific criteria

**[12:47]** or sorry data point specific criteria

**[12:47]** or sorry data point specific criteria about what to test for. It's almost like

**[12:49]** about what to test for. It's almost like

**[12:49]** about what to test for. It's almost like coming up with unit tests for the

**[12:50]** coming up with unit tests for the

**[12:50]** coming up with unit tests for the specific data point you're looking at

**[12:52]** specific data point you're looking at

**[12:52]** specific data point you're looking at and having the LM essentially look at

**[12:53]** and having the LM essentially look at

**[12:54]** and having the LM essentially look at each of those criteria and critique the

**[12:56]** each of those criteria and critique the

**[12:56]** each of those criteria and critique the the data points on against each of those

**[12:58]** the data points on against each of those

**[12:58]** the data points on against each of those criteria. Right? So it's like instance

**[12:59]** criteria. Right? So it's like instance

**[12:59]** criteria. Right? So it's like instance specific rubric and then instance


### [13:00 - 14:00]

**[13:01]** specific rubric and then instance

**[13:01]** specific rubric and then instance specific rubric critiques. Um this is

**[13:03]** specific rubric critiques. Um this is

**[13:03]** specific rubric critiques. Um this is one way to train RL models. We ran a

**[13:06]** one way to train RL models. We ran a

**[13:06]** one way to train RL models. We ran a pretty simple experiment using this uh

**[13:08]** pretty simple experiment using this uh

**[13:08]** pretty simple experiment using this uh using a variant of this uh technique um

**[13:11]** using a variant of this uh technique um

**[13:11]** using a variant of this uh technique um to GRPO train 600 million parameter and

**[13:14]** to GRPO train 600 million parameter and

**[13:14]** to GRPO train 600 million parameter and 1.7 billion parameter models and TLDDR.

**[13:17]** 1.7 billion parameter models and TLDDR.

**[13:17]** 1.7 billion parameter models and TLDDR. gets us to you know competitive

**[13:19]** gets us to you know competitive

**[13:19]** gets us to you know competitive performance on the reward bench task

**[13:21]** performance on the reward bench task

**[13:21]** performance on the reward bench task with cloud3 opus which is at 80% uh GP4

**[13:24]** with cloud3 opus which is at 80% uh GP4

**[13:24]** with cloud3 opus which is at 80% uh GP4 mini which is at 80% L 370B at 77% and

**[13:28]** mini which is at 80% L 370B at 77% and

**[13:28]** mini which is at 80% L 370B at 77% and J1 micro which is this 1.7 billion

**[13:30]** J1 micro which is this 1.7 billion

**[13:30]** J1 micro which is this 1.7 billion parameter reward model at 80.7% uh

**[13:33]** parameter reward model at 80.7% uh

**[13:33]** parameter reward model at 80.7% uh accuracy on the words bench task right

**[13:35]** accuracy on the words bench task right

**[13:35]** accuracy on the words bench task right and this is all because of judge time

**[13:36]** and this is all because of judge time

**[13:36]** and this is all because of judge time scaling this is all because we did gpo

**[13:38]** scaling this is all because we did gpo

**[13:38]** scaling this is all because we did gpo to come up with uh better rubric

**[13:40]** to come up with uh better rubric

**[13:40]** to come up with uh better rubric proposals and better critiques on the

**[13:42]** proposals and better critiques on the

**[13:42]** proposals and better critiques on the specific task that we're looking at so

**[13:44]** specific task that we're looking at so

**[13:44]** specific task that we're looking at so training off essentially uh much smaller

**[13:47]** training off essentially uh much smaller

**[13:47]** training off essentially uh much smaller model uh doing more compute gets you

**[13:49]** model uh doing more compute gets you

**[13:49]** model uh doing more compute gets you this this much better performance um and

**[13:51]** this this much better performance um and

**[13:52]** this this much better performance um and similar numbers for the 600 million

**[13:53]** similar numbers for the 600 million

**[13:53]** similar numbers for the 600 million parameter model.

**[13:56]** parameter model.

**[13:56]** parameter model. Cool. So that's all judging and scoring

**[13:58]** Cool. So that's all judging and scoring

**[13:58]** Cool. So that's all judging and scoring the outputs. Um equally important though


### [14:00 - 15:00]

**[14:00]** the outputs. Um equally important though

**[14:00]** the outputs. Um equally important though is how do you come up with inputs to

**[14:02]** is how do you come up with inputs to

**[14:02]** is how do you come up with inputs to throw out the AI system, right? And how

**[14:04]** throw out the AI system, right? And how

**[14:04]** throw out the AI system, right? And how do you run the search over time?

**[14:06]** do you run the search over time?

**[14:06]** do you run the search over time? TLDDR there's two ways that we think

**[14:08]** TLDDR there's two ways that we think

**[14:08]** TLDDR there's two ways that we think about this. There is fuzzing in the

**[14:10]** about this. There is fuzzing in the

**[14:10]** about this. There is fuzzing in the general sense which is essentially okay

**[14:12]** general sense which is essentially okay

**[14:12]** general sense which is essentially okay I just want to come up with some

**[14:13]** I just want to come up with some

**[14:13]** I just want to come up with some variance uh of some customer happy path

**[14:16]** variance uh of some customer happy path

**[14:16]** variance uh of some customer happy path and test my system under some reasonable

**[14:18]** and test my system under some reasonable

**[14:18]** and test my system under some reasonable in distribution uh user inputs right

**[14:22]** in distribution uh user inputs right

**[14:22]** in distribution uh user inputs right then there's the more fun part which is

**[14:24]** then there's the more fun part which is

**[14:24]** then there's the more fun part which is how do you do adversarial testing right

**[14:26]** how do you do adversarial testing right

**[14:26]** how do you do adversarial testing right how do you basically emulate some person

**[14:28]** how do you basically emulate some person

**[14:28]** how do you basically emulate some person trying to sit down and prompt inject and

**[14:30]** trying to sit down and prompt inject and

**[14:30]** trying to sit down and prompt inject and jailbreak and mess with your AI systems

**[14:31]** jailbreak and mess with your AI systems

**[14:31]** jailbreak and mess with your AI systems at large uh and this is much more

**[14:34]** at large uh and this is much more

**[14:34]** at large uh and this is much more aggressive in terms of how we pursue the

**[14:35]** aggressive in terms of how we pursue the

**[14:35]** aggressive in terms of how we pursue the optimization problem.

**[14:39]** optimization problem.

**[14:39]** optimization problem. Long story short is, you know, fuzzing

**[14:41]** Long story short is, you know, fuzzing

**[14:41]** Long story short is, you know, fuzzing in the AI sense is much more structured

**[14:44]** in the AI sense is much more structured

**[14:44]** in the AI sense is much more structured and optimization driven than in

**[14:46]** and optimization driven than in

**[14:46]** and optimization driven than in classical security or or software or

**[14:48]** classical security or or software or

**[14:48]** classical security or or software or hardware, right? It is impossible to

**[14:51]** hardware, right? It is impossible to

**[14:51]** hardware, right? It is impossible to like search over the input space of

**[14:53]** like search over the input space of

**[14:53]** like search over the input space of natural language and do a brute force

**[14:55]** natural language and do a brute force

**[14:55]** natural language and do a brute force search uh in any reasonably short amount

**[14:58]** search uh in any reasonably short amount

**[14:58]** search uh in any reasonably short amount of time. Like we're dealing with, you


### [15:00 - 16:00]

**[15:00]** of time. Like we're dealing with, you

**[15:00]** of time. Like we're dealing with, you know, let's say we're doing a llama 3

**[15:01]** know, let's say we're doing a llama 3

**[15:01]** know, let's say we're doing a llama 3 tokenizer. is uh 128,000 tokens per

**[15:05]** tokenizer. is uh 128,000 tokens per

**[15:05]** tokenizer. is uh 128,000 tokens per individual input, right? You scale this

**[15:07]** individual input, right? You scale this

**[15:07]** individual input, right? You scale this up to like 100 million tokens and you're

**[15:08]** up to like 100 million tokens and you're

**[15:08]** up to like 100 million tokens and you're like literally impossible to scan this

**[15:10]** like literally impossible to scan this

**[15:10]** like literally impossible to scan this entire input space. So you have to be

**[15:12]** entire input space. So you have to be

**[15:12]** entire input space. So you have to be very clever and guided and prune the

**[15:14]** very clever and guided and prune the

**[15:14]** very clever and guided and prune the search space as you do hazing and

**[15:15]** search space as you do hazing and

**[15:15]** search space as you do hazing and fuzzing. We treat this task essentially

**[15:17]** fuzzing. We treat this task essentially

**[15:18]** fuzzing. We treat this task essentially as an optimization problem. Right? This

**[15:19]** as an optimization problem. Right? This

**[15:19]** as an optimization problem. Right? This is long story short just discrete

**[15:21]** is long story short just discrete

**[15:21]** is long story short just discrete optimization. There's plenty of rich

**[15:23]** optimization. There's plenty of rich

**[15:23]** optimization. There's plenty of rich literature over the past 60 70 years of

**[15:26]** literature over the past 60 70 years of

**[15:26]** literature over the past 60 70 years of uh discrete math research to go and

**[15:28]** uh discrete math research to go and

**[15:28]** uh discrete math research to go and support how to do this sort of task. So

**[15:29]** support how to do this sort of task. So

**[15:29]** support how to do this sort of task. So you have to massage it of course to work

**[15:30]** you have to massage it of course to work

**[15:30]** you have to massage it of course to work for the LM domain. Um but TLDDR the

**[15:33]** for the LM domain. Um but TLDDR the

**[15:33]** for the LM domain. Um but TLDDR the shirt space is just natural language.

**[15:35]** shirt space is just natural language.

**[15:35]** shirt space is just natural language. The objective that we're trying to

**[15:36]** The objective that we're trying to

**[15:36]** The objective that we're trying to minimize in this case is essentially

**[15:39]** minimize in this case is essentially

**[15:39]** minimize in this case is essentially whatever judge uh that we're using to

**[15:41]** whatever judge uh that we're using to

**[15:41]** whatever judge uh that we're using to score the output. We basically want to

**[15:42]** score the output. We basically want to

**[15:42]** score the output. We basically want to find inputs that break your A

**[15:44]** find inputs that break your A

**[15:44]** find inputs that break your A application visav the judge gets the

**[15:46]** application visav the judge gets the

**[15:46]** application visav the judge gets the output to score very low on some uh

**[15:48]** output to score very low on some uh

**[15:48]** output to score very low on some uh measure of the judge. And yeah we we can

**[15:50]** measure of the judge. And yeah we we can

**[15:50]** measure of the judge. And yeah we we can rip and throw a bunch of fun

**[15:52]** rip and throw a bunch of fun

**[15:52]** rip and throw a bunch of fun optimization algorithms at this. Um we

**[15:53]** optimization algorithms at this. Um we

**[15:54]** optimization algorithms at this. Um we can use gradient based methods to back

**[15:55]** can use gradient based methods to back

**[15:55]** can use gradient based methods to back prop all the way from the judge loss

**[15:57]** prop all the way from the judge loss

**[15:57]** prop all the way from the judge loss through the model to the input space and

**[15:58]** through the model to the input space and

**[15:58]** through the model to the input space and use that to guide uh what tokens we want


### [16:00 - 17:00]

**[16:00]** use that to guide uh what tokens we want

**[16:00]** use that to guide uh what tokens we want to flip. Uh we can use various forms of

**[16:02]** to flip. Uh we can use various forms of

**[16:02]** to flip. Uh we can use various forms of tree search and MCTS. We can search over

**[16:04]** tree search and MCTS. We can search over

**[16:04]** tree search and MCTS. We can search over the latent space of uh embedding models

**[16:07]** the latent space of uh embedding models

**[16:07]** the latent space of uh embedding models and then map from the embedding models

**[16:08]** and then map from the embedding models

**[16:08]** and then map from the embedding models to text and throw that at the underlying

**[16:10]** to text and throw that at the underlying

**[16:10]** to text and throw that at the underlying AI application or the application under

**[16:12]** AI application or the application under

**[16:12]** AI application or the application under test. Um we can use DSPI. We can use all

**[16:14]** test. Um we can use DSPI. We can use all

**[16:14]** test. Um we can use DSPI. We can use all sorts of other great uh tools and tricks

**[16:16]** sorts of other great uh tools and tricks

**[16:16]** sorts of other great uh tools and tricks to solve this optimization problem.

**[16:20]** to solve this optimization problem.

**[16:20]** to solve this optimization problem. Some fun case studies in the last few

**[16:22]** Some fun case studies in the last few

**[16:22]** Some fun case studies in the last few minutes. Um, TLDDR, you could probably

**[16:24]** minutes. Um, TLDDR, you could probably

**[16:24]** minutes. Um, TLDDR, you could probably imagine that this hazing thing matters a

**[16:26]** imagine that this hazing thing matters a

**[16:26]** imagine that this hazing thing matters a lot for people in regulated industries

**[16:28]** lot for people in regulated industries

**[16:28]** lot for people in regulated industries and indeed we work a lot with uh banks

**[16:30]** and indeed we work a lot with uh banks

**[16:30]** and indeed we work a lot with uh banks and financial services and healthcare

**[16:32]** and financial services and healthcare

**[16:32]** and financial services and healthcare and so on. Um, we did something recently

**[16:34]** and so on. Um, we did something recently

**[16:34]** and so on. Um, we did something recently where we um hazed uh the largest bank in

**[16:37]** where we um hazed uh the largest bank in

**[16:37]** where we um hazed uh the largest bank in Hungary. Uh they had this like loan

**[16:39]** Hungary. Uh they had this like loan

**[16:39]** Hungary. Uh they had this like loan calculation AI application that they're

**[16:41]** calculation AI application that they're

**[16:41]** calculation AI application that they're showing to customers. The customer

**[16:43]** showing to customers. The customer

**[16:43]** showing to customers. The customer application had to follow this 18 line

**[16:45]** application had to follow this 18 line

**[16:45]** application had to follow this 18 line code of conduct is what they called it.

**[16:46]** code of conduct is what they called it.

**[16:46]** code of conduct is what they called it. uh and we basically threw everything

**[16:48]** uh and we basically threw everything

**[16:48]** uh and we basically threw everything under the sun uh from our platform in

**[16:49]** under the sun uh from our platform in

**[16:49]** under the sun uh from our platform in terms of optimization and scoring to uh

**[16:51]** terms of optimization and scoring to uh

**[16:51]** terms of optimization and scoring to uh emulate adversaries. We were able to

**[16:53]** emulate adversaries. We were able to

**[16:53]** emulate adversaries. We were able to discover a ton of uh prompt injections

**[16:55]** discover a ton of uh prompt injections

**[16:55]** discover a ton of uh prompt injections and jailbreaks and honestly just like

**[16:57]** and jailbreaks and honestly just like

**[16:57]** and jailbreaks and honestly just like unexpected corner cases that they didn't

**[16:59]** unexpected corner cases that they didn't

**[16:59]** unexpected corner cases that they didn't account for in their code of conducts.


### [17:00 - 18:00]

**[17:01]** account for in their code of conducts.

**[17:01]** account for in their code of conducts. Um and they're able to patch this up and

**[17:02]** Um and they're able to patch this up and

**[17:02]** Um and they're able to patch this up and then finally unblock their production

**[17:03]** then finally unblock their production

**[17:03]** then finally unblock their production into prod.

**[17:05]** into prod.

**[17:05]** into prod. We are doing this right now for a

**[17:07]** We are doing this right now for a

**[17:07]** We are doing this right now for a fortune for Fortune 500 bank that wants

**[17:09]** fortune for Fortune 500 bank that wants

**[17:09]** fortune for Fortune 500 bank that wants to do uh outbound debt collection with

**[17:11]** to do uh outbound debt collection with

**[17:11]** to do uh outbound debt collection with voice agents. uh little bit actually

**[17:13]** voice agents. uh little bit actually

**[17:13]** voice agents. uh little bit actually more complex problem because now

**[17:17]** more complex problem because now

**[17:17]** more complex problem because now we're not just testing in the text

**[17:18]** we're not just testing in the text

**[17:18]** we're not just testing in the text space. We're actually introducing a lot

**[17:20]** space. We're actually introducing a lot

**[17:20]** space. We're actually introducing a lot of uh variance to just the audio signal

**[17:22]** of uh variance to just the audio signal

**[17:22]** of uh variance to just the audio signal as well. So adding things like

**[17:24]** as well. So adding things like

**[17:24]** as well. So adding things like background noise um stacking you know

**[17:26]** background noise um stacking you know

**[17:26]** background noise um stacking you know weird static into the the input domain

**[17:29]** weird static into the the input domain

**[17:29]** weird static into the the input domain changing the frequencies of things etc.

**[17:30]** changing the frequencies of things etc.

**[17:30]** changing the frequencies of things etc. Right? But still an optimization problem

**[17:32]** Right? But still an optimization problem

**[17:32]** Right? But still an optimization problem at the end of the day. um TLDDR what

**[17:34]** at the end of the day. um TLDDR what

**[17:34]** at the end of the day. um TLDDR what took this team you know 3 months or so

**[17:36]** took this team you know 3 months or so

**[17:36]** took this team you know 3 months or so to do with their internal ops teams uh

**[17:39]** to do with their internal ops teams uh

**[17:39]** to do with their internal ops teams uh took in their own words uh only 5

**[17:41]** took in their own words uh only 5

**[17:41]** took in their own words uh only 5 minutes for a platform to do um so

**[17:43]** minutes for a platform to do um so

**[17:43]** minutes for a platform to do um so scaling up adversary emulation uh works

**[17:45]** scaling up adversary emulation uh works

**[17:45]** scaling up adversary emulation uh works for this task as well

**[17:47]** for this task as well

**[17:47]** for this task as well and a little bit more different uh for

**[17:50]** and a little bit more different uh for

**[17:50]** and a little bit more different uh for another voice agent company we've been

**[17:51]** another voice agent company we've been

**[17:51]** another voice agent company we've been helping them with uh scaling up their

**[17:53]** helping them with uh scaling up their

**[17:53]** helping them with uh scaling up their eval uh suite right so not so much

**[17:55]** eval uh suite right so not so much

**[17:55]** eval uh suite right so not so much hazing but basically scaling up their

**[17:57]** hazing but basically scaling up their

**[17:57]** hazing but basically scaling up their subjective human annotators uh through

**[17:59]** subjective human annotators uh through

**[17:59]** subjective human annotators uh through verdicts uh they've seen a 38% increase


### [18:00 - 19:00]

**[18:02]** verdicts uh they've seen a 38% increase

**[18:02]** verdicts uh they've seen a 38% increase in ground truth human agreements using

**[18:03]** in ground truth human agreements using

**[18:03]** in ground truth human agreements using verdicts um as opposed to using uh their

**[18:06]** verdicts um as opposed to using uh their

**[18:06]** verdicts um as opposed to using uh their internal ops teams. And what we're using

**[18:08]** internal ops teams. And what we're using

**[18:08]** internal ops teams. And what we're using here is essentially uh a triedand-rue

**[18:11]** here is essentially uh a triedand-rue

**[18:11]** here is essentially uh a triedand-rue architecture from the verdict library

**[18:12]** architecture from the verdict library

**[18:12]** architecture from the verdict library which is what we call rubric fanout. So

**[18:15]** which is what we call rubric fanout. So

**[18:15]** which is what we call rubric fanout. So it is basically propose individual uh

**[18:17]** it is basically propose individual uh

**[18:17]** it is basically propose individual uh unit test and criteria for any

**[18:18]** unit test and criteria for any

**[18:18]** unit test and criteria for any particular data point uh critique it

**[18:20]** particular data point uh critique it

**[18:20]** particular data point uh critique it self-verify your critique and then

**[18:22]** self-verify your critique and then

**[18:22]** self-verify your critique and then aggregate results at the very end.

**[18:25]** aggregate results at the very end.

**[18:25]** aggregate results at the very end. Cool. So we got a few minutes left uh

**[18:27]** Cool. So we got a few minutes left uh

**[18:27]** Cool. So we got a few minutes left uh for questions but um yeah hazing is a

**[18:31]** for questions but um yeah hazing is a

**[18:31]** for questions but um yeah hazing is a ton of fun. I think it matters a lot for

**[18:32]** ton of fun. I think it matters a lot for

**[18:32]** ton of fun. I think it matters a lot for this new era of software that we're

**[18:34]** this new era of software that we're

**[18:34]** this new era of software that we're building. Uh we're very aggressively

**[18:36]** building. Uh we're very aggressively

**[18:36]** building. Uh we're very aggressively hiring. We're, you know, facing what I

**[18:38]** hiring. We're, you know, facing what I

**[18:38]** hiring. We're, you know, facing what I would deem to be insurmountable

**[18:39]** would deem to be insurmountable

**[18:39]** would deem to be insurmountable enterprise demand and we're only a team

**[18:41]** enterprise demand and we're only a team

**[18:41]** enterprise demand and we're only a team of four people. Uh so we really need to

**[18:43]** of four people. Uh so we really need to

**[18:43]** of four people. Uh so we really need to scale up our team and yeah, we're based

**[18:45]** scale up our team and yeah, we're based

**[18:45]** scale up our team and yeah, we're based in New York in case you guys want to

**[18:46]** in New York in case you guys want to

**[18:46]** in New York in case you guys want to move out to the city. Um and yeah, any

**[18:49]** move out to the city. Um and yeah, any

**[18:49]** move out to the city. Um and yeah, any uh any last questions for me

**[18:52]** uh any last questions for me

**[18:52]** uh any last questions for me >> for the hazing input? Is it multi-shot

**[18:53]** >> for the hazing input? Is it multi-shot

**[18:54]** >> for the hazing input? Is it multi-shot or single shot?

**[18:54]** or single shot?

**[18:54]** or single shot? >> Yeah, great question. So we do both. Uh

**[18:57]** >> Yeah, great question. So we do both. Uh

**[18:57]** >> Yeah, great question. So we do both. Uh we do single turn, multi-turn. Uh we do


### [19:00 - 20:00]

**[19:00]** we do single turn, multi-turn. Uh we do

**[19:00]** we do single turn, multi-turn. Uh we do persistent conversations if you're doing

**[19:01]** persistent conversations if you're doing

**[19:01]** persistent conversations if you're doing voice. Um yeah, all sorts of modalities,

**[19:04]** voice. Um yeah, all sorts of modalities,

**[19:04]** voice. Um yeah, all sorts of modalities, all sorts of inputs.

**[19:06]** all sorts of inputs.

**[19:06]** all sorts of inputs. [Music]


