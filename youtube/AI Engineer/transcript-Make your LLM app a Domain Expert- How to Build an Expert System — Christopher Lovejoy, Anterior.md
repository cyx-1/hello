# Make your LLM app a Domain Expert- How to Build an Expert System — Christopher Lovejoy, Anterior

**Video URL:** https://www.youtube.com/watch?v=MRM7oA3JsFs

---

## Full Transcript

### [00:00 - 01:00]

**[00:16]** Hi everybody. So I'm Christopher

**[00:16]** Hi everybody. So I'm Christopher Lovejoy. I'm a medical doctor turned AI

**[00:18]** Lovejoy. I'm a medical doctor turned AI

**[00:18]** Lovejoy. I'm a medical doctor turned AI engineer and I'm going to share a

**[00:21]** engineer and I'm going to share a

**[00:21]** engineer and I'm going to share a playbook for building a domain native

**[00:23]** playbook for building a domain native

**[00:23]** playbook for building a domain native LLM application. Uh so I spent about

**[00:26]** LLM application. Uh so I spent about

**[00:26]** LLM application. Uh so I spent about eight years um training and working as a

**[00:28]** eight years um training and working as a

**[00:28]** eight years um training and working as a medical doctor and then I spent the last

**[00:29]** medical doctor and then I spent the last

**[00:30]** medical doctor and then I spent the last seven years building AI systems that

**[00:31]** seven years building AI systems that

**[00:31]** seven years building AI systems that incorporate medical domain expertise. Um

**[00:34]** incorporate medical domain expertise. Um

**[00:34]** incorporate medical domain expertise. Um and I did that at a few different

**[00:36]** and I did that at a few different

**[00:36]** and I did that at a few different startups. So I worked at a a health tech

**[00:38]** startups. So I worked at a a health tech

**[00:38]** startups. So I worked at a a health tech startup called Serakare um doing tech

**[00:40]** startup called Serakare um doing tech

**[00:40]** startup called Serakare um doing tech enabled home care. Uh the startup

**[00:42]** enabled home care. Uh the startup

**[00:42]** enabled home care. Uh the startup recently hit 500 million ARR. Um worked

**[00:45]** recently hit 500 million ARR. Um worked

**[00:45]** recently hit 500 million ARR. Um worked at various other startups and I

**[00:46]** at various other startups and I

**[00:46]** at various other startups and I currently work at Anterior.

**[00:48]** currently work at Anterior.

**[00:48]** currently work at Anterior. And Anterior is a New York based

**[00:51]** And Anterior is a New York based

**[00:51]** And Anterior is a New York based clinicianled uh company. Here we provide

**[00:53]** clinicianled uh company. Here we provide

**[00:53]** clinicianled uh company. Here we provide clinical reasoning tools to automate and

**[00:57]** clinical reasoning tools to automate and

**[00:57]** clinical reasoning tools to automate and accelerate uh health insurance um and

**[00:59]** accelerate uh health insurance um and

**[00:59]** accelerate uh health insurance um and healthcare administration. Uh we serve


### [01:00 - 02:00]

**[01:01]** healthcare administration. Uh we serve

**[01:01]** healthcare administration. Uh we serve about 50 million we serve uh health

**[01:03]** about 50 million we serve uh health

**[01:03]** about 50 million we serve uh health insurance providers that cover about 50

**[01:05]** insurance providers that cover about 50

**[01:05]** insurance providers that cover about 50 million lives uh in the US. And we spend

**[01:08]** million lives uh in the US. And we spend

**[01:08]** million lives uh in the US. And we spend a lot of time thinking about what does

**[01:09]** a lot of time thinking about what does

**[01:09]** a lot of time thinking about what does it mean to build a domain native LLM

**[01:12]** it mean to build a domain native LLM

**[01:12]** it mean to build a domain native LLM application whether it's in healthcare

**[01:14]** application whether it's in healthcare

**[01:14]** application whether it's in healthcare um or otherwise. Uh and that's what I'm

**[01:16]** um or otherwise. Uh and that's what I'm

**[01:16]** um or otherwise. Uh and that's what I'm going to talk about today. And in

**[01:19]** going to talk about today. And in

**[01:19]** going to talk about today. And in particular, our bet really is that when

**[01:21]** particular, our bet really is that when

**[01:21]** particular, our bet really is that when it comes to vertical AI applications,

**[01:23]** it comes to vertical AI applications,

**[01:24]** it comes to vertical AI applications, the system that you build for

**[01:25]** the system that you build for

**[01:25]** the system that you build for incorporating your domain insights is

**[01:27]** incorporating your domain insights is

**[01:27]** incorporating your domain insights is far more important than the

**[01:28]** far more important than the

**[01:28]** far more important than the sophistication of your models and your

**[01:29]** sophistication of your models and your

**[01:29]** sophistication of your models and your pipelines. So the limitation these days

**[01:31]** pipelines. So the limitation these days

**[01:31]** pipelines. So the limitation these days is not like how powerful is your model

**[01:34]** is not like how powerful is your model

**[01:34]** is not like how powerful is your model and whether it can uh reason to the

**[01:36]** and whether it can uh reason to the

**[01:36]** and whether it can uh reason to the level you need it to. It's more can your

**[01:39]** level you need it to. It's more can your

**[01:39]** level you need it to. It's more can your model understand the context um in that

**[01:42]** model understand the context um in that

**[01:42]** model understand the context um in that industry for that particular customer uh

**[01:44]** industry for that particular customer uh

**[01:44]** industry for that particular customer uh and perform perform the reasoning that

**[01:45]** and perform perform the reasoning that

**[01:45]** and perform perform the reasoning that it needs to and the way that you enable

**[01:48]** it needs to and the way that you enable

**[01:48]** it needs to and the way that you enable that and the way that you uh kind of

**[01:49]** that and the way that you uh kind of

**[01:49]** that and the way that you uh kind of iterate quickly with your customers is

**[01:51]** iterate quickly with your customers is

**[01:51]** iterate quickly with your customers is by building the system around it and

**[01:53]** by building the system around it and

**[01:53]** by building the system around it and there's various components to that um

**[01:55]** there's various components to that um

**[01:55]** there's various components to that um that's what I'm going to talk about. So

**[01:57]** that's what I'm going to talk about. So

**[01:57]** that's what I'm going to talk about. So this is the kind of high level schematic

**[01:59]** this is the kind of high level schematic

**[01:59]** this is the kind of high level schematic and we're going to go through each of


### [02:00 - 03:00]

**[02:00]** and we're going to go through each of

**[02:00]** and we're going to go through each of these parts um throughout the talk. Uh

**[02:02]** these parts um throughout the talk. Uh

**[02:02]** these parts um throughout the talk. Uh as you'll see right in the middle

**[02:03]** as you'll see right in the middle

**[02:04]** as you'll see right in the middle there's the the PM um and this is you

**[02:07]** there's the the PM um and this is you

**[02:07]** there's the the PM um and this is you know in our experience it makes sense

**[02:08]** know in our experience it makes sense

**[02:08]** know in our experience it makes sense for this to be a domain um expert um

**[02:10]** for this to be a domain um expert um

**[02:10]** for this to be a domain um expert um product manager. So in our context it's

**[02:12]** product manager. So in our context it's

**[02:12]** product manager. So in our context it's clinical um and I'm going to go through

**[02:14]** clinical um and I'm going to go through

**[02:14]** clinical um and I'm going to go through go through this in more detail shortly.

**[02:17]** go through this in more detail shortly.

**[02:17]** go through this in more detail shortly. But first I think it's worth taking a

**[02:18]** But first I think it's worth taking a

**[02:18]** But first I think it's worth taking a quick step back and asking you know why

**[02:20]** quick step back and asking you know why

**[02:20]** quick step back and asking you know why is it so hard to successfully apply

**[02:22]** is it so hard to successfully apply

**[02:22]** is it so hard to successfully apply large language models to specialized

**[02:24]** large language models to specialized

**[02:24]** large language models to specialized industries.

**[02:25]** industries.

**[02:25]** industries. We think it's because of the last mile

**[02:27]** We think it's because of the last mile

**[02:27]** We think it's because of the last mile problem. And what I mean by the last

**[02:29]** problem. And what I mean by the last

**[02:29]** problem. And what I mean by the last mile problem is is this problem that I I

**[02:30]** mile problem is is this problem that I I

**[02:30]** mile problem is is this problem that I I kind of touched on just now around uh

**[02:33]** kind of touched on just now around uh

**[02:34]** kind of touched on just now around uh giving the model and your your kind of

**[02:35]** giving the model and your your kind of

**[02:36]** giving the model and your your kind of AI system more generally context and

**[02:38]** AI system more generally context and

**[02:38]** AI system more generally context and understanding of the specific workflow

**[02:40]** understanding of the specific workflow

**[02:40]** understanding of the specific workflow for that customer for that industry. Um

**[02:43]** for that customer for that industry. Um

**[02:43]** for that customer for that industry. Um and

**[02:46]** and

**[02:46]** and I'm going to illustrate that with an

**[02:47]** I'm going to illustrate that with an

**[02:47]** I'm going to illustrate that with an example um from a clinical case that

**[02:50]** example um from a clinical case that

**[02:50]** example um from a clinical case that we've processed. Our AI anterior is

**[02:52]** we've processed. Our AI anterior is

**[02:52]** we've processed. Our AI anterior is called Florence and a 78-y old female

**[02:56]** called Florence and a 78-y old female

**[02:56]** called Florence and a 78-y old female patient uh presented with right knee

**[02:58]** patient uh presented with right knee

**[02:58]** patient uh presented with right knee pain. The doctor recommended a knee


### [03:00 - 04:00]

**[03:01]** pain. The doctor recommended a knee

**[03:01]** pain. The doctor recommended a knee arthoscopy and as part of deciding

**[03:04]** arthoscopy and as part of deciding

**[03:04]** arthoscopy and as part of deciding whether this treatment was appropriate,

**[03:05]** whether this treatment was appropriate,

**[03:05]** whether this treatment was appropriate, whether the doctor made an appropriate

**[03:06]** whether the doctor made an appropriate

**[03:06]** whether the doctor made an appropriate decision, Florence needs to answer

**[03:08]** decision, Florence needs to answer

**[03:08]** decision, Florence needs to answer various questions. Uh one of those

**[03:10]** various questions. Uh one of those

**[03:10]** various questions. Uh one of those questions is is there documentation of

**[03:12]** questions is is there documentation of

**[03:12]** questions is is there documentation of unsuccessful conservative therapy for at

**[03:14]** unsuccessful conservative therapy for at

**[03:14]** unsuccessful conservative therapy for at least six weeks. Um and you know on the

**[03:17]** least six weeks. Um and you know on the

**[03:17]** least six weeks. Um and you know on the surface of it that might seem relatively

**[03:19]** surface of it that might seem relatively

**[03:19]** surface of it that might seem relatively simple. I mean, I appreciate maybe not a

**[03:21]** simple. I mean, I appreciate maybe not a

**[03:21]** simple. I mean, I appreciate maybe not a lot of doctors in the room, so you might

**[03:23]** lot of doctors in the room, so you might

**[03:23]** lot of doctors in the room, so you might not know what conservative therapy is,

**[03:25]** not know what conservative therapy is,

**[03:25]** not know what conservative therapy is, but um actually there's a lot of kind of

**[03:28]** but um actually there's a lot of kind of

**[03:28]** but um actually there's a lot of kind of like hidden complexity in answering a

**[03:29]** like hidden complexity in answering a

**[03:29]** like hidden complexity in answering a question like this. So, for example, you

**[03:32]** question like this. So, for example, you

**[03:32]** question like this. So, for example, you know, conservative therapy um typically

**[03:35]** know, conservative therapy um typically

**[03:35]** know, conservative therapy um typically what we mean by conservative therapy is

**[03:36]** what we mean by conservative therapy is

**[03:36]** what we mean by conservative therapy is when there's some kind of option for uh

**[03:39]** when there's some kind of option for uh

**[03:39]** when there's some kind of option for uh you know, a more aggressive treatment,

**[03:40]** you know, a more aggressive treatment,

**[03:40]** you know, a more aggressive treatment, maybe a surgical operation, that's like

**[03:42]** maybe a surgical operation, that's like

**[03:42]** maybe a surgical operation, that's like the the you know, the surgical

**[03:44]** the the you know, the surgical

**[03:44]** the the you know, the surgical treatment. And then if you're deciding

**[03:45]** treatment. And then if you're deciding

**[03:45]** treatment. And then if you're deciding not to operate and you want to try

**[03:47]** not to operate and you want to try

**[03:47]** not to operate and you want to try something conservative first, that's

**[03:48]** something conservative first, that's

**[03:48]** something conservative first, that's like the conservative therapy. So it

**[03:49]** like the conservative therapy. So it

**[03:49]** like the conservative therapy. So it might be, you know, do physiootherapy,

**[03:52]** might be, you know, do physiootherapy,

**[03:52]** might be, you know, do physiootherapy, uh lose weight, um do kind of, you know,

**[03:54]** uh lose weight, um do kind of, you know,

**[03:54]** uh lose weight, um do kind of, you know, non-invasive things that might help

**[03:56]** non-invasive things that might help

**[03:56]** non-invasive things that might help resolve the problem. But actually

**[03:58]** resolve the problem. But actually

**[03:58]** resolve the problem. But actually there's some there's still some

**[03:59]** there's some there's still some

**[03:59]** there's some there's still some ambiguity there because, uh, you know,


### [04:00 - 05:00]

**[04:01]** ambiguity there because, uh, you know,

**[04:01]** ambiguity there because, uh, you know, in some cases, giving medication might

**[04:03]** in some cases, giving medication might

**[04:03]** in some cases, giving medication might be a conservative therapy. In some

**[04:04]** be a conservative therapy. In some

**[04:04]** be a conservative therapy. In some cases, that's actually the more

**[04:05]** cases, that's actually the more

**[04:05]** cases, that's actually the more aggressive treatment and there's

**[04:06]** aggressive treatment and there's

**[04:06]** aggressive treatment and there's something else that's more conservative.

**[04:08]** something else that's more conservative.

**[04:08]** something else that's more conservative. Um, so there's one layer of ambiguity

**[04:09]** Um, so there's one layer of ambiguity

**[04:09]** Um, so there's one layer of ambiguity there. Then when we talk about

**[04:11]** there. Then when we talk about

**[04:11]** there. Then when we talk about unsuccessful um well what is unsu let's

**[04:14]** unsuccessful um well what is unsu let's

**[04:14]** unsuccessful um well what is unsu let's say that somebody has uh some knee pain

**[04:17]** say that somebody has uh some knee pain

**[04:18]** say that somebody has uh some knee pain they do some treatment and their

**[04:19]** they do some treatment and their

**[04:19]** they do some treatment and their symptoms improve significantly but they

**[04:21]** symptoms improve significantly but they

**[04:21]** symptoms improve significantly but they don't like fully resolve. So is that

**[04:23]** don't like fully resolve. So is that

**[04:23]** don't like fully resolve. So is that successful? Do we need like a full

**[04:24]** successful? Do we need like a full

**[04:24]** successful? Do we need like a full resolution of symptoms or is it just

**[04:26]** resolution of symptoms or is it just

**[04:26]** resolution of symptoms or is it just like a partial resolution is enough? If

**[04:28]** like a partial resolution is enough? If

**[04:28]** like a partial resolution is enough? If it's partial like at what point is that

**[04:29]** it's partial like at what point is that

**[04:30]** it's partial like at what point is that enough to be quantified as successful?

**[04:32]** enough to be quantified as successful?

**[04:32]** enough to be quantified as successful? Um so again there's kind of complexity

**[04:34]** Um so again there's kind of complexity

**[04:34]** Um so again there's kind of complexity and nuance with with how that's

**[04:35]** and nuance with with how that's

**[04:35]** and nuance with with how that's interpreted. And then finally

**[04:37]** interpreted. And then finally

**[04:37]** interpreted. And then finally documentation for at least six weeks.

**[04:39]** documentation for at least six weeks.

**[04:39]** documentation for at least six weeks. again, you know, documentation. Are we

**[04:42]** again, you know, documentation. Are we

**[04:42]** again, you know, documentation. Are we saying that the medical record said they

**[04:45]** saying that the medical record said they

**[04:45]** saying that the medical record said they started physical therapy 8 weeks ago,

**[04:46]** started physical therapy 8 weeks ago,

**[04:46]** started physical therapy 8 weeks ago, then it's never mentioned again? We can

**[04:49]** then it's never mentioned again? We can

**[04:49]** then it's never mentioned again? We can therefore assume that they've been doing

**[04:50]** therefore assume that they've been doing

**[04:50]** therefore assume that they've been doing it for for 8 weeks. Uh or do we need

**[04:52]** it for for 8 weeks. Uh or do we need

**[04:52]** it for for 8 weeks. Uh or do we need like explicit documentation that they

**[04:54]** like explicit documentation that they

**[04:54]** like explicit documentation that they started treatment, they did it for 8

**[04:56]** started treatment, they did it for 8

**[04:56]** started treatment, they did it for 8 weeks, and you know, it's completed. Uh


### [05:00 - 06:00]

**[05:00]** weeks, and you know, it's completed. Uh

**[05:00]** weeks, and you know, it's completed. Uh where where do we like draw the line

**[05:01]** where where do we like draw the line

**[05:02]** where where do we like draw the line there in terms of what we can infer?

**[05:07]** Um and yeah, just kind of coming back to

**[05:07]** Um and yeah, just kind of coming back to echo our point. So this is really our

**[05:09]** echo our point. So this is really our

**[05:09]** echo our point. So this is really our bet that the system is more important.

**[05:11]** bet that the system is more important.

**[05:12]** bet that the system is more important. Uh we believe that in every vertical

**[05:14]** Uh we believe that in every vertical

**[05:14]** Uh we believe that in every vertical industry the uh you know the team the

**[05:17]** industry the uh you know the team the

**[05:17]** industry the uh you know the team the company that wins is the one that builds

**[05:18]** company that wins is the one that builds

**[05:18]** company that wins is the one that builds the best system for taking those domain

**[05:20]** the best system for taking those domain

**[05:20]** the best system for taking those domain insights and quickly translating them

**[05:22]** insights and quickly translating them

**[05:22]** insights and quickly translating them into the pipeline giving it that context

**[05:24]** into the pipeline giving it that context

**[05:24]** into the pipeline giving it that context and iterating um to create this

**[05:26]** and iterating um to create this

**[05:26]** and iterating um to create this improvements.

**[05:31]** Um, and we also, you know, found I guess

**[05:31]** Um, and we also, you know, found I guess to talk to this counterpoint, the

**[05:33]** to talk to this counterpoint, the

**[05:33]** to talk to this counterpoint, the models, I mean, models obviously are

**[05:34]** models, I mean, models obviously are

**[05:34]** models, I mean, models obviously are important. Um, and the the progress in

**[05:37]** important. Um, and the the progress in

**[05:37]** important. Um, and the the progress in models makes it easier to have a good

**[05:38]** models makes it easier to have a good

**[05:38]** models makes it easier to have a good starting point, but that's only getting

**[05:41]** starting point, but that's only getting

**[05:41]** starting point, but that's only getting up to a certain baseline. And we found

**[05:42]** up to a certain baseline. And we found

**[05:42]** up to a certain baseline. And we found we kind of hit a saturation around like

**[05:45]** we kind of hit a saturation around like

**[05:45]** we kind of hit a saturation around like 95% uh level. So, we invested a lot of

**[05:47]** 95% uh level. So, we invested a lot of

**[05:47]** 95% uh level. So, we invested a lot of time and effort improving our pipelines.

**[05:49]** time and effort improving our pipelines.

**[05:49]** time and effort improving our pipelines. Um, obviously 95% is stuck, still pretty

**[05:51]** Um, obviously 95% is stuck, still pretty

**[05:51]** Um, obviously 95% is stuck, still pretty reasonable. And this is that performing

**[05:53]** reasonable. And this is that performing

**[05:53]** reasonable. And this is that performing the like primary task that our our AI

**[05:55]** the like primary task that our our AI

**[05:55]** the like primary task that our our AI system does which is approving these

**[05:57]** system does which is approving these

**[05:57]** system does which is approving these care requests um in a health insurance

**[05:59]** care requests um in a health insurance

**[05:59]** care requests um in a health insurance context. Um so we're at 95% and we then


### [06:00 - 07:00]

**[06:03]** context. Um so we're at 95% and we then

**[06:03]** context. Um so we're at 95% and we then iterated based on this system um that

**[06:05]** iterated based on this system um that

**[06:05]** iterated based on this system um that I'm going to walk through and we really

**[06:06]** I'm going to walk through and we really

**[06:06]** I'm going to walk through and we really got to you know kind of almost silly

**[06:08]** got to you know kind of almost silly

**[06:08]** got to you know kind of almost silly accuracy of like 99%. Uh we got this

**[06:11]** accuracy of like 99%. Uh we got this

**[06:11]** accuracy of like 99%. Uh we got this class point of um light award a few

**[06:13]** class point of um light award a few

**[06:13]** class point of um light award a few weeks ago for this. Um and really what

**[06:16]** weeks ago for this. Um and really what

**[06:16]** weeks ago for this. Um and really what we found here and what we observed is

**[06:18]** we found here and what we observed is

**[06:18]** we found here and what we observed is that the the models reason very well.

**[06:21]** that the the models reason very well.

**[06:21]** that the the models reason very well. they get to a great baseline. But if

**[06:22]** they get to a great baseline. But if

**[06:22]** they get to a great baseline. But if you're in in an industry where you

**[06:24]** you're in in an industry where you

**[06:24]** you're in in an industry where you really need to ek out that like final

**[06:25]** really need to ek out that like final

**[06:25]** really need to ek out that like final mile of performance, um you need to be

**[06:28]** mile of performance, um you need to be

**[06:28]** mile of performance, um you need to be able to then kind of give the model give

**[06:29]** able to then kind of give the model give

**[06:29]** able to then kind of give the model give the pipeline that context.

**[06:33]** the pipeline that context.

**[06:33]** the pipeline that context. Uh so how do we do that? Well, we call

**[06:36]** Uh so how do we do that? Well, we call

**[06:36]** Uh so how do we do that? Well, we call this our adaptive domain intelligence

**[06:38]** this our adaptive domain intelligence

**[06:38]** this our adaptive domain intelligence engine. And what this is performing is

**[06:41]** engine. And what this is performing is

**[06:41]** engine. And what this is performing is it's taking customer specific domain

**[06:43]** it's taking customer specific domain

**[06:43]** it's taking customer specific domain insights and it's converting them into

**[06:45]** insights and it's converting them into

**[06:45]** insights and it's converting them into performance improvements um and kind of

**[06:47]** performance improvements um and kind of

**[06:47]** performance improvements um and kind of building a system around that. And

**[06:49]** building a system around that. And

**[06:49]** building a system around that. And there's broadly two main parts to this.

**[06:51]** there's broadly two main parts to this.

**[06:51]** there's broadly two main parts to this. The first part is the measurement side

**[06:53]** The first part is the measurement side

**[06:53]** The first part is the measurement side of things. So, you know, how is how is

**[06:55]** of things. So, you know, how is how is

**[06:55]** of things. So, you know, how is how is our current pipeline doing? Um, and then

**[06:58]** our current pipeline doing? Um, and then

**[06:58]** our current pipeline doing? Um, and then the rest of this is the uh improvement


### [07:00 - 08:00]

**[07:00]** the rest of this is the uh improvement

**[07:00]** the rest of this is the uh improvement side. So, I'm going to talk first a bit

**[07:02]** side. So, I'm going to talk first a bit

**[07:02]** side. So, I'm going to talk first a bit more about measurement in more detail

**[07:03]** more about measurement in more detail

**[07:03]** more about measurement in more detail and then and then a bit about

**[07:04]** and then and then a bit about

**[07:04]** and then and then a bit about improvements.

**[07:06]** improvements.

**[07:06]** improvements. So, measuring domain specific uh

**[07:08]** So, measuring domain specific uh

**[07:08]** So, measuring domain specific uh performance.

**[07:10]** performance.

**[07:10]** performance. The first thing um and I think you know

**[07:12]** The first thing um and I think you know

**[07:12]** The first thing um and I think you know a lot of this is is really just kind of

**[07:13]** a lot of this is is really just kind of

**[07:13]** a lot of this is is really just kind of practice best practice more generally

**[07:15]** practice best practice more generally

**[07:15]** practice best practice more generally but um the first step is to define what

**[07:18]** but um the first step is to define what

**[07:18]** but um the first step is to define what is it that your users really care about

**[07:20]** is it that your users really care about

**[07:20]** is it that your users really care about as metrics. So in a health context

**[07:22]** as metrics. So in a health context

**[07:22]** as metrics. So in a health context obviously I've been talking about

**[07:23]** obviously I've been talking about

**[07:23]** obviously I've been talking about medical necessity reviews um this is our

**[07:25]** medical necessity reviews um this is our

**[07:25]** medical necessity reviews um this is our bread and butter and there the customers

**[07:27]** bread and butter and there the customers

**[07:27]** bread and butter and there the customers really care about false approvals. They

**[07:28]** really care about false approvals. They

**[07:28]** really care about false approvals. They want to minimize false approvals because

**[07:30]** want to minimize false approvals because

**[07:30]** want to minimize false approvals because a false approval where you've approved

**[07:32]** a false approval where you've approved

**[07:32]** a false approval where you've approved care means that you know a patient who

**[07:34]** care means that you know a patient who

**[07:34]** care means that you know a patient who didn't need the care might get given

**[07:35]** didn't need the care might get given

**[07:35]** didn't need the care might get given some care they don't need and obviously

**[07:37]** some care they don't need and obviously

**[07:37]** some care they don't need and obviously from an insurance provider point of view

**[07:38]** from an insurance provider point of view

**[07:38]** from an insurance provider point of view they're then paying for treatment that

**[07:39]** they're then paying for treatment that

**[07:39]** they're then paying for treatment that they don't necessarily want to pay for.

**[07:41]** they don't necessarily want to pay for.

**[07:41]** they don't necessarily want to pay for. Um and often defining these metrics is

**[07:44]** Um and often defining these metrics is

**[07:44]** Um and often defining these metrics is like a collaboration between the domain

**[07:45]** like a collaboration between the domain

**[07:45]** like a collaboration between the domain experts in your company and the

**[07:46]** experts in your company and the

**[07:46]** experts in your company and the customers to kind of like really

**[07:48]** customers to kind of like really

**[07:48]** customers to kind of like really translate what are the metrics that you

**[07:49]** translate what are the metrics that you

**[07:49]** translate what are the metrics that you care about. They might be like one or

**[07:51]** care about. They might be like one or

**[07:51]** care about. They might be like one or two or like usually there's just a few

**[07:53]** two or like usually there's just a few

**[07:53]** two or like usually there's just a few metrics that matter most. So in a few

**[07:55]** metrics that matter most. So in a few

**[07:55]** metrics that matter most. So in a few other industries like legal when you're

**[07:57]** other industries like legal when you're

**[07:57]** other industries like legal when you're analyzing contracts it might be that you

**[07:58]** analyzing contracts it might be that you

**[07:58]** analyzing contracts it might be that you really want to minimize a number of uh


### [08:00 - 09:00]

**[08:00]** really want to minimize a number of uh

**[08:00]** really want to minimize a number of uh missed critical terms when you're when

**[08:01]** missed critical terms when you're when

**[08:01]** missed critical terms when you're when you're identifying these clauses in the

**[08:03]** you're identifying these clauses in the

**[08:03]** you're identifying these clauses in the contract for fraud detection. Your

**[08:04]** contract for fraud detection. Your

**[08:04]** contract for fraud detection. Your topline metric might be something like

**[08:05]** topline metric might be something like

**[08:05]** topline metric might be something like preventing um dollar loss from fraud.

**[08:07]** preventing um dollar loss from fraud.

**[08:07]** preventing um dollar loss from fraud. You know education it might be you want

**[08:09]** You know education it might be you want

**[08:09]** You know education it might be you want to optimize for test score improvements.

**[08:10]** to optimize for test score improvements.

**[08:10]** to optimize for test score improvements. Um I think it's it's definitely a

**[08:12]** Um I think it's it's definitely a

**[08:12]** Um I think it's it's definitely a helpful exercise to push yourself to

**[08:15]** helpful exercise to push yourself to

**[08:15]** helpful exercise to push yourself to think of like really if I'm optimizing

**[08:16]** think of like really if I'm optimizing

**[08:16]** think of like really if I'm optimizing for like one or two metrics what is like

**[08:17]** for like one or two metrics what is like

**[08:18]** for like one or two metrics what is like the metric that is most important. Um

**[08:21]** the metric that is most important. Um

**[08:21]** the metric that is most important. Um and then what you can also do hand

**[08:22]** and then what you can also do hand

**[08:22]** and then what you can also do hand inhand with that um which is very

**[08:24]** inhand with that um which is very

**[08:24]** inhand with that um which is very helpful uh just going off the bottom

**[08:27]** helpful uh just going off the bottom

**[08:27]** helpful uh just going off the bottom there a little bit but uh is designing a

**[08:30]** there a little bit but uh is designing a

**[08:30]** there a little bit but uh is designing a failure mode ontology and what I mean by

**[08:32]** failure mode ontology and what I mean by

**[08:32]** failure mode ontology and what I mean by this is taking the task that you're

**[08:35]** this is taking the task that you're

**[08:35]** this is taking the task that you're performing and identifying what are all

**[08:37]** performing and identifying what are all

**[08:37]** performing and identifying what are all the different ways in which my AI fails

**[08:39]** the different ways in which my AI fails

**[08:39]** the different ways in which my AI fails and it might be at the level of like

**[08:41]** and it might be at the level of like

**[08:41]** and it might be at the level of like higher order categories so for example

**[08:43]** higher order categories so for example

**[08:43]** higher order categories so for example here we've got medical record extraction

**[08:44]** here we've got medical record extraction

**[08:44]** here we've got medical record extraction clinical reasoning and rules

**[08:45]** clinical reasoning and rules

**[08:45]** clinical reasoning and rules interpretation we found that for medical

**[08:47]** interpretation we found that for medical

**[08:47]** interpretation we found that for medical necessity review these are the three

**[08:48]** necessity review these are the three

**[08:48]** necessity review these are the three broad categories these the three board

**[08:50]** broad categories these the three board

**[08:50]** broad categories these the three board ways in which the AI can fail and then

**[08:51]** ways in which the AI can fail and then

**[08:52]** ways in which the AI can fail and then within those there's various like

**[08:53]** within those there's various like

**[08:53]** within those there's various like different subtypes. Um and this is an

**[08:55]** different subtypes. Um and this is an

**[08:55]** different subtypes. Um and this is an iterative process. There's like various

**[08:56]** iterative process. There's like various

**[08:56]** iterative process. There's like various techniques for doing this. Um I think it

**[08:59]** techniques for doing this. Um I think it

**[08:59]** techniques for doing this. Um I think it it's important here to bring in your


### [09:00 - 10:00]

**[09:00]** it's important here to bring in your

**[09:00]** it's important here to bring in your domain experts. I think one failure mode

**[09:02]** domain experts. I think one failure mode

**[09:02]** domain experts. I think one failure mode is that you have somebody kind of

**[09:04]** is that you have somebody kind of

**[09:04]** is that you have somebody kind of looking at your AI traces in isolation

**[09:05]** looking at your AI traces in isolation

**[09:05]** looking at your AI traces in isolation and coming up with these um who don't

**[09:07]** and coming up with these um who don't

**[09:07]** and coming up with these um who don't necessarily have the context on how

**[09:08]** necessarily have the context on how

**[09:08]** necessarily have the context on how things are working. I think this is a a

**[09:10]** things are working. I think this is a a

**[09:10]** things are working. I think this is a a step that's critical to have domain

**[09:11]** step that's critical to have domain

**[09:11]** step that's critical to have domain experts uh leading this process.

**[09:15]** experts uh leading this process.

**[09:15]** experts uh leading this process. Um but really I think the the big value

**[09:18]** Um but really I think the the big value

**[09:18]** Um but really I think the the big value ad is when you do both of these at the

**[09:20]** ad is when you do both of these at the

**[09:20]** ad is when you do both of these at the same time um together because what this

**[09:22]** same time um together because what this

**[09:22]** same time um together because what this gives you uh and and this is a this is a

**[09:24]** gives you uh and and this is a this is a

**[09:24]** gives you uh and and this is a this is a dashboard that we've built internally. I

**[09:26]** dashboard that we've built internally. I

**[09:26]** dashboard that we've built internally. I appreciate the text might be a little

**[09:27]** appreciate the text might be a little

**[09:27]** appreciate the text might be a little bit small um but essentially on the

**[09:29]** bit small um but essentially on the

**[09:29]** bit small um but essentially on the right hand side you have a patient's

**[09:31]** right hand side you have a patient's

**[09:31]** right hand side you have a patient's medical record. You also have the

**[09:32]** medical record. You also have the

**[09:32]** medical record. You also have the guidelines that the record is being

**[09:34]** guidelines that the record is being

**[09:34]** guidelines that the record is being appraised against. On the left hand side

**[09:36]** appraised against. On the left hand side

**[09:36]** appraised against. On the left hand side you have the AI outputs. Um so this is

**[09:39]** you have the AI outputs. Um so this is

**[09:39]** you have the AI outputs. Um so this is the decision that it's made the

**[09:40]** the decision that it's made the

**[09:40]** the decision that it's made the reasoning behind its decision and what

**[09:42]** reasoning behind its decision and what

**[09:42]** reasoning behind its decision and what we enable our domain experts to do here

**[09:44]** we enable our domain experts to do here

**[09:44]** we enable our domain experts to do here enable our clinicians is they can come

**[09:45]** enable our clinicians is they can come

**[09:46]** enable our clinicians is they can come in they can mark whether it's correct or

**[09:47]** in they can mark whether it's correct or

**[09:47]** in they can mark whether it's correct or incorrect and if it's incorrect then

**[09:49]** incorrect and if it's incorrect then

**[09:49]** incorrect and if it's incorrect then this box here is for um defining the

**[09:51]** this box here is for um defining the

**[09:51]** this box here is for um defining the failure mode. So from that ontology we

**[09:53]** failure mode. So from that ontology we

**[09:53]** failure mode. So from that ontology we just saw on the slide before they can

**[09:54]** just saw on the slide before they can

**[09:54]** just saw on the slide before they can say this failed in this way and doing

**[09:58]** say this failed in this way and doing

**[09:58]** say this failed in this way and doing those at the same point and having your

**[09:59]** those at the same point and having your

**[09:59]** those at the same point and having your domain expert sit at that point doing


### [10:00 - 11:00]

**[10:01]** domain expert sit at that point doing

**[10:01]** domain expert sit at that point doing both of these is uh super valuable

**[10:04]** both of these is uh super valuable

**[10:04]** both of these is uh super valuable because it then enables you to

**[10:06]** because it then enables you to

**[10:06]** because it then enables you to understand things like this. So on the

**[10:08]** understand things like this. So on the

**[10:08]** understand things like this. So on the x- axis here we have number of false

**[10:10]** x- axis here we have number of false

**[10:10]** x- axis here we have number of false approvals. That's the metric that we

**[10:11]** approvals. That's the metric that we

**[10:11]** approvals. That's the metric that we really care about in our context. And

**[10:13]** really care about in our context. And

**[10:13]** really care about in our context. And then we have the different failure modes

**[10:15]** then we have the different failure modes

**[10:15]** then we have the different failure modes on on the y- axis. And obviously that

**[10:17]** on on the y- axis. And obviously that

**[10:17]** on on the y- axis. And obviously that tells us that if we want to minimize our

**[10:19]** tells us that if we want to minimize our

**[10:19]** tells us that if we want to minimize our false approvals and we want to like

**[10:20]** false approvals and we want to like

**[10:20]** false approvals and we want to like optimize for this this top northstar

**[10:22]** optimize for this this top northstar

**[10:22]** optimize for this this top northstar metric that we care about, these are

**[10:24]** metric that we care about, these are

**[10:24]** metric that we care about, these are what we want to address first kind of in

**[10:26]** what we want to address first kind of in

**[10:26]** what we want to address first kind of in this order. Um which as a PM is then a

**[10:29]** this order. Um which as a PM is then a

**[10:29]** this order. Um which as a PM is then a useful piece of information to help you

**[10:30]** useful piece of information to help you

**[10:30]** useful piece of information to help you prioritize uh the work that you want to

**[10:32]** prioritize uh the work that you want to

**[10:32]** prioritize uh the work that you want to do.

**[10:35]** do.

**[10:35]** do. So that's the measure side of things.

**[10:37]** So that's the measure side of things.

**[10:37]** So that's the measure side of things. I'm now going to go on to talk about the

**[10:39]** I'm now going to go on to talk about the

**[10:39]** I'm now going to go on to talk about the um the improvements

**[10:41]** um the improvements

**[10:41]** um the improvements um and particularly with this domain

**[10:43]** um and particularly with this domain

**[10:43]** um and particularly with this domain specific context.

**[10:45]** specific context.

**[10:45]** specific context. So

**[10:48]** So

**[10:48]** So what that also gives you this kind of

**[10:50]** what that also gives you this kind of

**[10:50]** what that also gives you this kind of failure mode labeling we talked about

**[10:51]** failure mode labeling we talked about

**[10:51]** failure mode labeling we talked about before is you get these readymade data

**[10:54]** before is you get these readymade data

**[10:54]** before is you get these readymade data sets that you can iterate against. And

**[10:56]** sets that you can iterate against. And

**[10:56]** sets that you can iterate against. And these data sets are super valuable

**[10:57]** these data sets are super valuable

**[10:57]** these data sets are super valuable because they're coming directly from

**[10:59]** because they're coming directly from

**[10:59]** because they're coming directly from production data, which means you know


### [11:00 - 12:00]

**[11:01]** production data, which means you know

**[11:01]** production data, which means you know that they're representative of the kind

**[11:02]** that they're representative of the kind

**[11:02]** that they're representative of the kind of input data distribution that you're

**[11:03]** of input data distribution that you're

**[11:04]** of input data distribution that you're going to see more so than synthetic data

**[11:05]** going to see more so than synthetic data

**[11:06]** going to see more so than synthetic data would be. Uh and you can now you know

**[11:09]** would be. Uh and you can now you know

**[11:09]** would be. Uh and you can now you know when you you had those priorities on the

**[11:11]** when you you had those priorities on the

**[11:11]** when you you had those priorities on the previous slide, we saw which sort of

**[11:12]** previous slide, we saw which sort of

**[11:12]** previous slide, we saw which sort of failure modes were causing the most

**[11:13]** failure modes were causing the most

**[11:13]** failure modes were causing the most false approvals. We can then pick that

**[11:14]** false approvals. We can then pick that

**[11:14]** false approvals. We can then pick that data set of you know 100 cases that came

**[11:17]** data set of you know 100 cases that came

**[11:17]** data set of you know 100 cases that came through prodical

**[11:19]** through prodical

**[11:19]** through prodical failure mode. You can give that to an

**[11:21]** failure mode. You can give that to an

**[11:21]** failure mode. You can give that to an engineer. An engineer can iterate

**[11:22]** engineer. An engineer can iterate

**[11:22]** engineer. An engineer can iterate against it and you can keep on testing.

**[11:23]** against it and you can keep on testing.

**[11:23]** against it and you can keep on testing. Okay, how is my performance against that

**[11:24]** Okay, how is my performance against that

**[11:24]** Okay, how is my performance against that particular failure mode right now?

**[11:30]** And that lets you do something like this

**[11:30]** And that lets you do something like this where on the x-axis here we have the

**[11:32]** where on the x-axis here we have the

**[11:32]** where on the x-axis here we have the pipeline version. On the y axis we have

**[11:34]** pipeline version. On the y axis we have

**[11:34]** pipeline version. On the y axis we have the performance score. Um by definition

**[11:36]** the performance score. Um by definition

**[11:36]** the performance score. Um by definition on these flaws we're starting very low

**[11:38]** on these flaws we're starting very low

**[11:38]** on these flaws we're starting very low for each of these like failure mode data

**[11:39]** for each of these like failure mode data

**[11:40]** for each of these like failure mode data sets but every time you increment your

**[11:41]** sets but every time you increment your

**[11:42]** sets but every time you increment your pipeline version maybe you spent some

**[11:43]** pipeline version maybe you spent some

**[11:43]** pipeline version maybe you spent some time focusing on this particular failure

**[11:45]** time focusing on this particular failure

**[11:45]** time focusing on this particular failure mode and and you were able to get a big

**[11:46]** mode and and you were able to get a big

**[11:46]** mode and and you were able to get a big jump in performance. Um and then you can

**[11:48]** jump in performance. Um and then you can

**[11:48]** jump in performance. Um and then you can see the other ones also jumping up as

**[11:49]** see the other ones also jumping up as

**[11:49]** see the other ones also jumping up as well um on kind of subsequent releases.

**[11:52]** well um on kind of subsequent releases.

**[11:52]** well um on kind of subsequent releases. And you can also use this to then track

**[11:53]** And you can also use this to then track

**[11:53]** And you can also use this to then track that you're not regressing on any

**[11:54]** that you're not regressing on any

**[11:54]** that you're not regressing on any particular failure mode as well. Um so

**[11:57]** particular failure mode as well. Um so

**[11:57]** particular failure mode as well. Um so it's a useful useful uh visualization to

**[11:59]** it's a useful useful uh visualization to

**[11:59]** it's a useful useful uh visualization to be able to make.


### [12:00 - 13:00]

**[12:02]** be able to make.

**[12:02]** be able to make. And you can then go one step further and

**[12:04]** And you can then go one step further and

**[12:04]** And you can then go one step further and actually bring your domain experts into

**[12:06]** actually bring your domain experts into

**[12:06]** actually bring your domain experts into the kind of improvements in the

**[12:08]** the kind of improvements in the

**[12:08]** the kind of improvements in the iteration itself. And what that looks

**[12:10]** iteration itself. And what that looks

**[12:10]** iteration itself. And what that looks like is creating this tooling that

**[12:13]** like is creating this tooling that

**[12:13]** like is creating this tooling that enables a domain expert who's not

**[12:14]** enables a domain expert who's not

**[12:14]** enables a domain expert who's not necessarily technical to come in. They

**[12:16]** necessarily technical to come in. They

**[12:16]** necessarily technical to come in. They can then suggest changes to the

**[12:17]** can then suggest changes to the

**[12:17]** can then suggest changes to the application pipeline. They can also

**[12:19]** application pipeline. They can also

**[12:19]** application pipeline. They can also suggest new domain knowledge that's made

**[12:21]** suggest new domain knowledge that's made

**[12:21]** suggest new domain knowledge that's made available to the pipeline. And obviously

**[12:23]** available to the pipeline. And obviously

**[12:23]** available to the pipeline. And obviously they're the best positioned to be making

**[12:24]** they're the best positioned to be making

**[12:24]** they're the best positioned to be making these kind of um you know opinions of

**[12:27]** these kind of um you know opinions of

**[12:27]** these kind of um you know opinions of what sort of domain knowledge might be

**[12:28]** what sort of domain knowledge might be

**[12:28]** what sort of domain knowledge might be might be relevant. And then you have

**[12:30]** might be relevant. And then you have

**[12:30]** might be relevant. And then you have your pipeline in the middle that's ready

**[12:32]** your pipeline in the middle that's ready

**[12:32]** your pipeline in the middle that's ready to use those if it wants to. And on the

**[12:34]** to use those if it wants to. And on the

**[12:34]** to use those if it wants to. And on the right hand side you have those domain

**[12:35]** right hand side you have those domain

**[12:35]** right hand side you have those domain evals which might be these failure set

**[12:37]** evals which might be these failure set

**[12:37]** evals which might be these failure set evals. You might have more generic eval

**[12:38]** evals. You might have more generic eval

**[12:38]** evals. You might have more generic eval sets as well. and they can then tell you

**[12:41]** sets as well. and they can then tell you

**[12:41]** sets as well. and they can then tell you in a data-driven way, okay, given this

**[12:43]** in a data-driven way, okay, given this

**[12:43]** in a data-driven way, okay, given this domain knowledge suggestion from a

**[12:45]** domain knowledge suggestion from a

**[12:45]** domain knowledge suggestion from a domain expert, should that go live in

**[12:46]** domain expert, should that go live in

**[12:46]** domain expert, should that go live in the platform and now it's in production

**[12:48]** the platform and now it's in production

**[12:48]** the platform and now it's in production and and then um you know it should be

**[12:50]** and and then um you know it should be

**[12:50]** and and then um you know it should be improving the performance for for live

**[12:51]** improving the performance for for live

**[12:51]** improving the performance for for live customers. Um and this whole loop can

**[12:53]** customers. Um and this whole loop can

**[12:53]** customers. Um and this whole loop can happen very quickly. So for example and

**[12:55]** happen very quickly. So for example and

**[12:55]** happen very quickly. So for example and I think actually on the next slide yeah

**[12:57]** I think actually on the next slide yeah

**[12:57]** I think actually on the next slide yeah I'll just show um so this is a dashboard


### [13:00 - 14:00]

**[13:00]** I'll just show um so this is a dashboard

**[13:00]** I'll just show um so this is a dashboard we saw before but this is with this

**[13:02]** we saw before but this is with this

**[13:02]** we saw before but this is with this extra button which is like a domain

**[13:03]** extra button which is like a domain

**[13:03]** extra button which is like a domain knowledge addition button and so again

**[13:05]** knowledge addition button and so again

**[13:05]** knowledge addition button and so again we're keeping the same context we have

**[13:07]** we're keeping the same context we have

**[13:07]** we're keeping the same context we have uh you know a domain expert clinician

**[13:09]** uh you know a domain expert clinician

**[13:09]** uh you know a domain expert clinician coming in here they're reviewing the

**[13:10]** coming in here they're reviewing the

**[13:10]** coming in here they're reviewing the case they're saying is it correct is it

**[13:12]** case they're saying is it correct is it

**[13:12]** case they're saying is it correct is it incorrect they're saying what's the

**[13:13]** incorrect they're saying what's the

**[13:13]** incorrect they're saying what's the failure mode and now they can say I

**[13:15]** failure mode and now they can say I

**[13:15]** failure mode and now they can say I think this domain knowledge would be

**[13:17]** think this domain knowledge would be

**[13:17]** think this domain knowledge would be helpful for the application's

**[13:18]** helpful for the application's

**[13:18]** helpful for the application's performance and uh you know it might be

**[13:21]** performance and uh you know it might be

**[13:21]** performance and uh you know it might be I think in this case appreciate it might

**[13:23]** I think in this case appreciate it might

**[13:23]** I think in this case appreciate it might not be that easy to read But um the

**[13:25]** not be that easy to read But um the

**[13:25]** not be that easy to read But um the model is kind of making some some

**[13:26]** model is kind of making some some

**[13:26]** model is kind of making some some mistake related to understanding

**[13:28]** mistake related to understanding

**[13:28]** mistake related to understanding suspicion of a condition because the

**[13:31]** suspicion of a condition because the

**[13:31]** suspicion of a condition because the patient like has the condition and it

**[13:32]** patient like has the condition and it

**[13:32]** patient like has the condition and it says oh there's no suspicion of the

**[13:34]** says oh there's no suspicion of the

**[13:34]** says oh there's no suspicion of the condition um but actually they they have

**[13:36]** condition um but actually they they have

**[13:36]** condition um but actually they they have it and like there's there's like you

**[13:38]** it and like there's there's like you

**[13:38]** it and like there's there's like you could give some information to the model

**[13:39]** could give some information to the model

**[13:40]** could give some information to the model for the medical context of how we

**[13:41]** for the medical context of how we

**[13:41]** for the medical context of how we interpret suspicious or suspicion as a

**[13:43]** interpret suspicious or suspicion as a

**[13:43]** interpret suspicious or suspicion as a word that would then influence the

**[13:45]** word that would then influence the

**[13:45]** word that would then influence the answer. Um or it could be that maybe the

**[13:47]** answer. Um or it could be that maybe the

**[13:47]** answer. Um or it could be that maybe the reasoning uses some kind of scoring

**[13:48]** reasoning uses some kind of scoring

**[13:48]** reasoning uses some kind of scoring system and you realize actually the

**[13:49]** system and you realize actually the

**[13:50]** system and you realize actually the model doesn't have access to that

**[13:50]** model doesn't have access to that

**[13:50]** model doesn't have access to that scoring system. You could again you

**[13:52]** scoring system. You could again you

**[13:52]** scoring system. You could again you could add that as domain knowledge um to

**[13:54]** could add that as domain knowledge um to

**[13:54]** could add that as domain knowledge um to continually build out what the what the

**[13:56]** continually build out what the what the

**[13:56]** continually build out what the what the model can handle. And what that helps

**[13:59]** model can handle. And what that helps

**[13:59]** model can handle. And what that helps with yeah in ter in terms of kind of


### [14:00 - 15:00]

**[14:01]** with yeah in ter in terms of kind of

**[14:01]** with yeah in ter in terms of kind of iteration speed from that you can do

**[14:03]** iteration speed from that you can do

**[14:03]** iteration speed from that you can do that maybe you want to let your evals

**[14:05]** that maybe you want to let your evals

**[14:05]** that maybe you want to let your evals automatically let that go in or maybe

**[14:07]** automatically let that go in or maybe

**[14:07]** automatically let that go in or maybe you want to um have some kind of human

**[14:08]** you want to um have some kind of human

**[14:08]** you want to um have some kind of human in the loop but it just means that you

**[14:10]** in the loop but it just means that you

**[14:10]** in the loop but it just means that you can have this very quick process. This

**[14:11]** can have this very quick process. This

**[14:11]** can have this very quick process. This prod comes through you analyze it um by

**[14:15]** prod comes through you analyze it um by

**[14:15]** prod comes through you analyze it um by through a clinical lens and then the

**[14:16]** through a clinical lens and then the

**[14:16]** through a clinical lens and then the same day you've essentially fixed it

**[14:18]** same day you've essentially fixed it

**[14:18]** same day you've essentially fixed it because you've added the domain

**[14:18]** because you've added the domain

**[14:18]** because you've added the domain knowledge that should solve it. You can

**[14:20]** knowledge that should solve it. You can

**[14:20]** knowledge that should solve it. You can prove that with the evals and then it's

**[14:21]** prove that with the evals and then it's

**[14:21]** prove that with the evals and then it's live.

**[14:27]** And what this means is that, you know,

**[14:27]** And what this means is that, you know, these domain expert reviews that are

**[14:29]** these domain expert reviews that are

**[14:29]** these domain expert reviews that are really kind of powering a lot of the

**[14:30]** really kind of powering a lot of the

**[14:30]** really kind of powering a lot of the insights you're getting here are giving

**[14:31]** insights you're getting here are giving

**[14:31]** insights you're getting here are giving you three main things. They're giving

**[14:32]** you three main things. They're giving

**[14:32]** you three main things. They're giving you performance metrics, they're giving

**[14:34]** you performance metrics, they're giving

**[14:34]** you performance metrics, they're giving you these failure modes, and they're

**[14:35]** you these failure modes, and they're

**[14:35]** you these failure modes, and they're giving you these suggested improvements

**[14:37]** giving you these suggested improvements

**[14:37]** giving you these suggested improvements um allin one.

**[14:39]** um allin one.

**[14:40]** um allin one. Yep.

**[14:46]** Yeah, good question. So the question is

**[14:46]** Yeah, good question. So the question is um how do you define a domain expert?

**[14:47]** um how do you define a domain expert?

**[14:47]** um how do you define a domain expert? like what level of of expertise do you

**[14:49]** like what level of of expertise do you

**[14:49]** like what level of of expertise do you need here? I think it really depends on

**[14:50]** need here? I think it really depends on

**[14:50]** need here? I think it really depends on the specific like workflow that you're

**[14:53]** the specific like workflow that you're

**[14:53]** the specific like workflow that you're doing um and what you're kind of

**[14:55]** doing um and what you're kind of

**[14:55]** doing um and what you're kind of optimizing for. So in our context, if

**[14:57]** optimizing for. So in our context, if

**[14:57]** optimizing for. So in our context, if you're optimizing for clinical reasoning

**[14:59]** you're optimizing for clinical reasoning

**[14:59]** you're optimizing for clinical reasoning and the quality of the clinical


### [15:00 - 16:00]

**[15:00]** and the quality of the clinical

**[15:00]** and the quality of the clinical reasoning, you therefore want somebody

**[15:01]** reasoning, you therefore want somebody

**[15:01]** reasoning, you therefore want somebody with like as much clinical experience,

**[15:03]** with like as much clinical experience,

**[15:03]** with like as much clinical experience, ideally a doctor, um you know, ideally

**[15:05]** ideally a doctor, um you know, ideally

**[15:05]** ideally a doctor, um you know, ideally they have relevant expertise in the

**[15:07]** they have relevant expertise in the

**[15:07]** they have relevant expertise in the specialtity that you're dealing with. Uh

**[15:09]** specialtity that you're dealing with. Uh

**[15:09]** specialtity that you're dealing with. Uh but it but it kind of really depends on

**[15:10]** but it but it kind of really depends on

**[15:10]** but it but it kind of really depends on your use case. It might be that there's

**[15:12]** your use case. It might be that there's

**[15:12]** your use case. It might be that there's actually simpler things we also um can

**[15:15]** actually simpler things we also um can

**[15:15]** actually simpler things we also um can can do in which case that level of

**[15:16]** can do in which case that level of

**[15:16]** can do in which case that level of expertise is not necessary and you could

**[15:18]** expertise is not necessary and you could

**[15:18]** expertise is not necessary and you could have you know like a more junior

**[15:19]** have you know like a more junior

**[15:19]** have you know like a more junior clinical person but the idea being that

**[15:21]** clinical person but the idea being that

**[15:21]** clinical person but the idea being that it's either like a nurse or a doctor or

**[15:23]** it's either like a nurse or a doctor or

**[15:23]** it's either like a nurse or a doctor or somebody that has experience of doing

**[15:24]** somebody that has experience of doing

**[15:24]** somebody that has experience of doing this workflow in in the real world. Does

**[15:27]** this workflow in in the real world. Does

**[15:27]** this workflow in in the real world. Does that make sense? Yeah. Another question.

**[15:38]** Yeah. This is this is bespoke tooling.

**[15:38]** Yeah. This is this is bespoke tooling. And I think in general my my philosophy

**[15:40]** And I think in general my my philosophy

**[15:40]** And I think in general my my philosophy on this is that if you if you're really

**[15:43]** on this is that if you if you're really

**[15:43]** on this is that if you if you're really placing a lot of weight on what you're

**[15:46]** placing a lot of weight on what you're

**[15:46]** placing a lot of weight on what you're kind of generating and this feeds into

**[15:47]** kind of generating and this feeds into

**[15:47]** kind of generating and this feeds into your system in various other different

**[15:48]** your system in various other different

**[15:48]** your system in various other different ways in the kind of ways I'm describing,

**[15:49]** ways in the kind of ways I'm describing,

**[15:50]** ways in the kind of ways I'm describing, it probably makes most sense to do this

**[15:51]** it probably makes most sense to do this

**[15:51]** it probably makes most sense to do this with bespoke tooling that you build

**[15:52]** with bespoke tooling that you build

**[15:52]** with bespoke tooling that you build yourself because it's you want to

**[15:54]** yourself because it's you want to

**[15:54]** yourself because it's you want to integrate it into the rest of your

**[15:55]** integrate it into the rest of your

**[15:55]** integrate it into the rest of your platform and it's just generally going

**[15:56]** platform and it's just generally going

**[15:56]** platform and it's just generally going to be um you know easier to do that if

**[15:59]** to be um you know easier to do that if

**[15:59]** to be um you know easier to do that if you're if you're kind of like doing


### [16:00 - 17:00]

**[16:00]** you're if you're kind of like doing

**[16:00]** you're if you're kind of like doing everything yourself. Yeah.

**[16:03]** everything yourself. Yeah.

**[16:03]** everything yourself. Yeah. Are these are your domain experts users?

**[16:06]** Are these are your domain experts users?

**[16:06]** Are these are your domain experts users? them to come in.

**[16:08]** them to come in.

**[16:08]** them to come in. Yeah, great question. Um, I think it c

**[16:10]** Yeah, great question. Um, I think it c

**[16:10]** Yeah, great question. Um, I think it c it can be both. Um, we like in our

**[16:13]** it can be both. Um, we like in our

**[16:13]** it can be both. Um, we like in our experience typically we start with we we

**[16:15]** experience typically we start with we we

**[16:15]** experience typically we start with we we will hire some people inhouse who kind

**[16:16]** will hire some people inhouse who kind

**[16:16]** will hire some people inhouse who kind of come and do this for us to give us

**[16:18]** of come and do this for us to give us

**[16:18]** of come and do this for us to give us this initial data so that we can do that

**[16:19]** this initial data so that we can do that

**[16:19]** this initial data so that we can do that iteration. I think there's definitely a

**[16:21]** iteration. I think there's definitely a

**[16:21]** iteration. I think there's definitely a world in which the customer themselves

**[16:24]** world in which the customer themselves

**[16:24]** world in which the customer themselves might also want to do validation of your

**[16:26]** might also want to do validation of your

**[16:26]** might also want to do validation of your AI and they might actually do this kind

**[16:27]** AI and they might actually do this kind

**[16:27]** AI and they might actually do this kind of process themselves in which case this

**[16:29]** of process themselves in which case this

**[16:29]** of process themselves in which case this then becomes a customerf facing product

**[16:30]** then becomes a customerf facing product

**[16:30]** then becomes a customerf facing product for them to to use as well. Um, yeah.

**[16:34]** for them to to use as well. Um, yeah.

**[16:34]** for them to to use as well. Um, yeah. Uh, okay. So, love the questions, but

**[16:37]** Uh, okay. So, love the questions, but

**[16:37]** Uh, okay. So, love the questions, but we're going to reserve time for Chris to

**[16:39]** we're going to reserve time for Chris to

**[16:39]** we're going to reserve time for Chris to keep going. Sounds good. And and I'm

**[16:40]** keep going. Sounds good. And and I'm

**[16:40]** keep going. Sounds good. And and I'm just um these are the last couple slides

**[16:41]** just um these are the last couple slides

**[16:42]** just um these are the last couple slides now as well. So, putting everything

**[16:44]** now as well. So, putting everything

**[16:44]** now as well. So, putting everything together. Uh this is the overall flow

**[16:47]** together. Uh this is the overall flow

**[16:47]** together. Uh this is the overall flow and

**[16:49]** and

**[16:49]** and essentially what this what what this can

**[16:51]** essentially what this what what this can

**[16:51]** essentially what this what what this can look like is you have your production

**[16:52]** look like is you have your production

**[16:52]** look like is you have your production application. It's generating these

**[16:54]** application. It's generating these

**[16:54]** application. It's generating these decisions, these AI outputs. You're

**[16:57]** decisions, these AI outputs. You're

**[16:57]** decisions, these AI outputs. You're having your domain experts review that,

**[16:58]** having your domain experts review that,

**[16:58]** having your domain experts review that, giving these performance insights.

**[16:59]** giving these performance insights.


### [17:00 - 18:00]

**[17:00]** giving these performance insights. That's things like the metrics, the

**[17:01]** That's things like the metrics, the

**[17:01]** That's things like the metrics, the failure modes. uh you then have your PM,

**[17:04]** failure modes. uh you then have your PM,

**[17:04]** failure modes. uh you then have your PM, your kind of domain expert PM who sits

**[17:06]** your kind of domain expert PM who sits

**[17:06]** your kind of domain expert PM who sits in the middle. They then have this rich

**[17:07]** in the middle. They then have this rich

**[17:07]** in the middle. They then have this rich information on okay, what should I

**[17:08]** information on okay, what should I

**[17:08]** information on okay, what should I prioritize based on the failure modes,

**[17:10]** prioritize based on the failure modes,

**[17:10]** prioritize based on the failure modes, based on the metrics. They can then turn

**[17:12]** based on the metrics. They can then turn

**[17:12]** based on the metrics. They can then turn to an engineer and say um I want you to

**[17:14]** to an engineer and say um I want you to

**[17:14]** to an engineer and say um I want you to fix this failure mode because I really

**[17:15]** fix this failure mode because I really

**[17:15]** fix this failure mode because I really care about it and I want you to fix it

**[17:17]** care about it and I want you to fix it

**[17:17]** care about it and I want you to fix it up to this performance threshold. So

**[17:18]** up to this performance threshold. So

**[17:18]** up to this performance threshold. So they can say right now, you know, in

**[17:19]** they can say right now, you know, in

**[17:20]** they can say right now, you know, in production we're getting 0% or 10% on

**[17:22]** production we're getting 0% or 10% on

**[17:22]** production we're getting 0% or 10% on this particular data set. I want you to

**[17:24]** this particular data set. I want you to

**[17:24]** this particular data set. I want you to go away and work on this until you get

**[17:25]** go away and work on this until you get

**[17:25]** go away and work on this until you get to 50%. And then the engineer can go and

**[17:28]** to 50%. And then the engineer can go and

**[17:28]** to 50%. And then the engineer can go and um you know run different experiments,

**[17:29]** um you know run different experiments,

**[17:29]** um you know run different experiments, have different ideas of how they might

**[17:31]** have different ideas of how they might

**[17:31]** have different ideas of how they might improve this, changing prompting,

**[17:32]** improve this, changing prompting,

**[17:32]** improve this, changing prompting, changing models, doing fine-tuning, all

**[17:34]** changing models, doing fine-tuning, all

**[17:34]** changing models, doing fine-tuning, all this kind of thing. They then have a

**[17:36]** this kind of thing. They then have a

**[17:36]** this kind of thing. They then have a very tight iteration loop because they

**[17:37]** very tight iteration loop because they

**[17:37]** very tight iteration loop because they have these ready-made failure mode data

**[17:38]** have these ready-made failure mode data

**[17:38]** have these ready-made failure mode data sets. They can run the eval. They can

**[17:40]** sets. They can run the eval. They can

**[17:40]** sets. They can run the eval. They can see the impact of those um eval. And

**[17:42]** see the impact of those um eval. And

**[17:42]** see the impact of those um eval. And then once they've kind of done that loop

**[17:44]** then once they've kind of done that loop

**[17:44]** then once they've kind of done that loop and they're they're hitting the

**[17:45]** and they're they're hitting the

**[17:45]** and they're they're hitting the percentage that they need, they can then

**[17:46]** percentage that they need, they can then

**[17:46]** percentage that they need, they can then go and give that back to the PM and say,

**[17:48]** go and give that back to the PM and say,

**[17:48]** go and give that back to the PM and say, "Hey, here are the changes I made. This

**[17:49]** "Hey, here are the changes I made. This

**[17:49]** "Hey, here are the changes I made. This is the impact." The PM can then um take

**[17:53]** is the impact." The PM can then um take

**[17:53]** is the impact." The PM can then um take that information and make some decision

**[17:55]** that information and make some decision

**[17:55]** that information and make some decision about going live. they can take the

**[17:56]** about going live. they can take the

**[17:56]** about going live. they can take the those uh email metrics, they can look at

**[17:58]** those uh email metrics, they can look at

**[17:58]** those uh email metrics, they can look at the kind of wider context of what this


### [18:00 - 19:00]

**[18:00]** the kind of wider context of what this

**[18:00]** the kind of wider context of what this change might impact elsewhere in the

**[18:01]** change might impact elsewhere in the

**[18:02]** change might impact elsewhere in the product um and then decide whether to go

**[18:04]** product um and then decide whether to go

**[18:04]** product um and then decide whether to go live uh with that in production.

**[18:07]** live uh with that in production.

**[18:07]** live uh with that in production. So final takeaway just to wrap up um you

**[18:11]** So final takeaway just to wrap up um you

**[18:11]** So final takeaway just to wrap up um you know to build a domain native element

**[18:12]** know to build a domain native element

**[18:12]** know to build a domain native element application you need to solve the the

**[18:14]** application you need to solve the the

**[18:14]** application you need to solve the the last mile problem. This isn't solved by

**[18:16]** last mile problem. This isn't solved by

**[18:16]** last mile problem. This isn't solved by just using more powerful models or more

**[18:17]** just using more powerful models or more

**[18:17]** just using more powerful models or more sophisticated pipelines. Uh you need

**[18:19]** sophisticated pipelines. Uh you need

**[18:19]** sophisticated pipelines. Uh you need what we call an adaptive domain

**[18:21]** what we call an adaptive domain

**[18:21]** what we call an adaptive domain intelligence engine. Domain experts can

**[18:23]** intelligence engine. Domain experts can

**[18:23]** intelligence engine. Domain experts can power this system by reviewing their AI

**[18:25]** power this system by reviewing their AI

**[18:25]** power this system by reviewing their AI outputs to generate metrics to generate

**[18:26]** outputs to generate metrics to generate

**[18:26]** outputs to generate metrics to generate failure modes and to generate suggested

**[18:28]** failure modes and to generate suggested

**[18:28]** failure modes and to generate suggested improvements. And this is really

**[18:29]** improvements. And this is really

**[18:29]** improvements. And this is really powerful because it takes production

**[18:31]** powerful because it takes production

**[18:31]** powerful because it takes production data live from kind of inside your

**[18:33]** data live from kind of inside your

**[18:33]** data live from kind of inside your customer's context and it uses that to

**[18:35]** customer's context and it uses that to

**[18:35]** customer's context and it uses that to give your LM product the nuance

**[18:36]** give your LM product the nuance

**[18:36]** give your LM product the nuance understanding of the customer workflows

**[18:38]** understanding of the customer workflows

**[18:38]** understanding of the customer workflows and continually iterate towards that and

**[18:39]** and continually iterate towards that and

**[18:39]** and continually iterate towards that and eek out the the kind of final

**[18:40]** eek out the the kind of final

**[18:40]** eek out the the kind of final performance um performance level. And

**[18:43]** performance um performance level. And

**[18:43]** performance um performance level. And the end result is you have this

**[18:45]** the end result is you have this

**[18:45]** the end result is you have this self-improving datadriven process that

**[18:47]** self-improving datadriven process that

**[18:47]** self-improving datadriven process that can be managed by a domain expert PM

**[18:49]** can be managed by a domain expert PM

**[18:49]** can be managed by a domain expert PM sitting in the middle.

**[18:51]** sitting in the middle.

**[18:51]** sitting in the middle. Um, so thank you for your attention. Um,

**[18:55]** Um, so thank you for your attention. Um,

**[18:55]** Um, so thank you for your attention. Um, uh, I, if you're interested in kind of

**[18:56]** uh, I, if you're interested in kind of

**[18:56]** uh, I, if you're interested in kind of vertical AI applications or like evals

**[18:58]** vertical AI applications or like evals

**[18:58]** vertical AI applications or like evals and AI product management more

**[18:59]** and AI product management more

**[18:59]** and AI product management more generally, I've written about that at my


### [19:00 - 20:00]

**[19:01]** generally, I've written about that at my

**[19:01]** generally, I've written about that at my website, chris lovejoy.me. Uh, always

**[19:03]** website, chris lovejoy.me. Uh, always

**[19:03]** website, chris lovejoy.me. Uh, always interested to talk about this. So feel

**[19:04]** interested to talk about this. So feel

**[19:04]** interested to talk about this. So feel free to drop an email at chrisanser.com.

**[19:06]** free to drop an email at chrisanser.com.

**[19:06]** free to drop an email at chrisanser.com. And we're also hiring as well at the

**[19:08]** And we're also hiring as well at the

**[19:08]** And we're also hiring as well at the moment. So check out anio.com/comp

**[19:10]** moment. So check out anio.com/comp

**[19:10]** moment. So check out anio.com/comp for open roles. Thank you.


