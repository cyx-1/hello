# How to defend your sites from AI bots — David Mytton, Arcjet

**Video URL:** https://www.youtube.com/watch?v=Gi4V8viBGYQ

---

## Full Transcript

### [00:00 - 01:00]

**[00:17]** Hi everyone. So my name is David. I'm

**[00:17]** Hi everyone. So my name is David. I'm the founder of ArtJet. We provide a

**[00:20]** the founder of ArtJet. We provide a

**[00:20]** the founder of ArtJet. We provide a security SDK for developers. So

**[00:22]** security SDK for developers. So

**[00:22]** security SDK for developers. So everything I'm going to be talking to

**[00:23]** everything I'm going to be talking to

**[00:23]** everything I'm going to be talking to you about today is what we've been

**[00:25]** you about today is what we've been

**[00:25]** you about today is what we've been building for the last few years, but how

**[00:27]** building for the last few years, but how

**[00:27]** building for the last few years, but how you can do it yourself.

**[00:29]** you can do it yourself.

**[00:29]** you can do it yourself. So, if you haven't had bots visiting

**[00:32]** So, if you haven't had bots visiting

**[00:32]** So, if you haven't had bots visiting your website and felt the pain, then you

**[00:35]** your website and felt the pain, then you

**[00:35]** your website and felt the pain, then you might be thinking, well, is this really

**[00:36]** might be thinking, well, is this really

**[00:36]** might be thinking, well, is this really a problem? Well, as as you just heard in

**[00:39]** a problem? Well, as as you just heard in

**[00:39]** a problem? Well, as as you just heard in the introduction, almost 50% of web

**[00:42]** the introduction, almost 50% of web

**[00:42]** the introduction, almost 50% of web traffic today is automated clients. And

**[00:45]** traffic today is automated clients. And

**[00:45]** traffic today is automated clients. And that varies depending on the industry.

**[00:47]** that varies depending on the industry.

**[00:47]** that varies depending on the industry. In gaming, that's almost 60% of all

**[00:49]** In gaming, that's almost 60% of all

**[00:49]** In gaming, that's almost 60% of all traffic is automated. And that's before

**[00:52]** traffic is automated. And that's before

**[00:52]** traffic is automated. And that's before the agent revolution has really kicked

**[00:54]** the agent revolution has really kicked

**[00:54]** the agent revolution has really kicked off. This isn't a new problem. It's been

**[00:57]** off. This isn't a new problem. It's been

**[00:57]** off. This isn't a new problem. It's been going on since the invention of the


### [01:00 - 02:00]

**[01:00]** going on since the invention of the

**[01:00]** going on since the invention of the internet and there are bots that you

**[01:02]** internet and there are bots that you

**[01:02]** internet and there are bots that you want to visit your website like Google

**[01:04]** want to visit your website like Google

**[01:04]** want to visit your website like Google bot but there also a lot of malicious

**[01:06]** bot but there also a lot of malicious

**[01:06]** bot but there also a lot of malicious crawlers

**[01:07]** crawlers

**[01:08]** crawlers and this causes a problem.

**[01:10]** and this causes a problem.

**[01:10]** and this causes a problem. The first incident you might experience

**[01:13]** The first incident you might experience

**[01:13]** The first incident you might experience is around expensive requests and think

**[01:16]** is around expensive requests and think

**[01:16]** is around expensive requests and think through what happens on your website. If

**[01:18]** through what happens on your website. If

**[01:18]** through what happens on your website. If it's a static site, then maybe it's not

**[01:20]** it's a static site, then maybe it's not

**[01:20]** it's a static site, then maybe it's not doing much um on your infrastructure.

**[01:22]** doing much um on your infrastructure.

**[01:22]** doing much um on your infrastructure. But if you're generating any content

**[01:24]** But if you're generating any content

**[01:24]** But if you're generating any content from a database or you're reading some

**[01:26]** from a database or you're reading some

**[01:26]** from a database or you're reading some dynamic content in some way, then each

**[01:29]** dynamic content in some way, then each

**[01:29]** dynamic content in some way, then each request is going to cost something.

**[01:31]** request is going to cost something.

**[01:31]** request is going to cost something. Particularly if you're using a

**[01:32]** Particularly if you're using a

**[01:32]** Particularly if you're using a serverless platform, paying per request.

**[01:34]** serverless platform, paying per request.

**[01:34]** serverless platform, paying per request. If you have huge numbers of automated

**[01:36]** If you have huge numbers of automated

**[01:36]** If you have huge numbers of automated clients coming in making requests,

**[01:38]** clients coming in making requests,

**[01:38]** clients coming in making requests, making hundreds of thousands of

**[01:39]** making hundreds of thousands of

**[01:39]** making hundreds of thousands of requests, then this starts to build up

**[01:41]** requests, then this starts to build up

**[01:41]** requests, then this starts to build up as a problem, as a cost problem. Um and

**[01:45]** as a problem, as a cost problem. Um and

**[01:45]** as a problem, as a cost problem. Um and also being able to deal with that on

**[01:46]** also being able to deal with that on

**[01:46]** also being able to deal with that on your infrastructure.

**[01:48]** your infrastructure.

**[01:48]** your infrastructure. And these clients can also be requesting

**[01:50]** And these clients can also be requesting

**[01:50]** And these clients can also be requesting all the assets. So downloading large

**[01:51]** all the assets. So downloading large

**[01:51]** all the assets. So downloading large files, that's going to start eating into

**[01:53]** files, that's going to start eating into

**[01:53]** files, that's going to start eating into your bandwidth costs and eating into the

**[01:56]** your bandwidth costs and eating into the

**[01:56]** your bandwidth costs and eating into the available resources you have to serve

**[01:58]** available resources you have to serve

**[01:58]** available resources you have to serve legitimate users on your site.


### [02:00 - 03:00]

**[02:02]** legitimate users on your site.

**[02:02]** legitimate users on your site. This can show up as a denial of service

**[02:04]** This can show up as a denial of service

**[02:04]** This can show up as a denial of service attack. So your service just might not

**[02:06]** attack. So your service just might not

**[02:06]** attack. So your service just might not be available to others. And even the

**[02:08]** be available to others. And even the

**[02:08]** be available to others. And even the largest website doesn't have infinite

**[02:11]** largest website doesn't have infinite

**[02:11]** largest website doesn't have infinite resources.

**[02:12]** resources.

**[02:12]** resources. Serverless means that you don't have to

**[02:14]** Serverless means that you don't have to

**[02:14]** Serverless means that you don't have to think about that for the most part. But

**[02:16]** think about that for the most part. But

**[02:16]** think about that for the most part. But what where you're actually handling it

**[02:18]** what where you're actually handling it

**[02:18]** what where you're actually handling it is part of the billing.

**[02:25]** This has been a problem for for decades.

**[02:25]** This has been a problem for for decades. And so the real question is well is AI

**[02:28]** And so the real question is well is AI

**[02:28]** And so the real question is well is AI making this worse?

**[02:30]** making this worse?

**[02:30]** making this worse? We see complaints in the media um

**[02:33]** We see complaints in the media um

**[02:33]** We see complaints in the media um websites talking about the traffic that

**[02:35]** websites talking about the traffic that

**[02:35]** websites talking about the traffic that they're getting and there's just an

**[02:36]** they're getting and there's just an

**[02:36]** they're getting and there's just an automatic assumption that this is AI and

**[02:39]** automatic assumption that this is AI and

**[02:39]** automatic assumption that this is AI and on the face of it there's no real

**[02:40]** on the face of it there's no real

**[02:40]** on the face of it there's no real evidence that that is the case. But when

**[02:42]** evidence that that is the case. But when

**[02:42]** evidence that that is the case. But when you start looking into the details about

**[02:43]** you start looking into the details about

**[02:43]** you start looking into the details about the kind of requests that these sites

**[02:45]** the kind of requests that these sites

**[02:45]** the kind of requests that these sites are are seeing, then AI is making it

**[02:48]** are are seeing, then AI is making it

**[02:48]** are are seeing, then AI is making it worse. So for instance, Diaspora, which

**[02:51]** worse. So for instance, Diaspora, which

**[02:51]** worse. So for instance, Diaspora, which is an online um online open source

**[02:53]** is an online um online open source

**[02:53]** is an online um online open source community, they saw that 24% of their

**[02:56]** community, they saw that 24% of their

**[02:56]** community, they saw that 24% of their traffic was from GPTBOT, which is

**[02:58]** traffic was from GPTBOT, which is

**[02:58]** traffic was from GPTBOT, which is OpenAI's crawler.


### [03:00 - 04:00]

**[03:01]** OpenAI's crawler.

**[03:01]** OpenAI's crawler. And then read the docs, which is an

**[03:03]** And then read the docs, which is an

**[03:03]** And then read the docs, which is an online documentation platform for code

**[03:07]** online documentation platform for code

**[03:07]** online documentation platform for code code projects. They found that by

**[03:09]** code projects. They found that by

**[03:09]** code projects. They found that by blocking all AI crawlers, they reduce

**[03:12]** blocking all AI crawlers, they reduce

**[03:12]** blocking all AI crawlers, they reduce their bandwidth from 800 gigabytes a day

**[03:14]** their bandwidth from 800 gigabytes a day

**[03:14]** their bandwidth from 800 gigabytes a day to 200 gigabytes a day. And even

**[03:17]** to 200 gigabytes a day. And even

**[03:17]** to 200 gigabytes a day. And even Wikipedia is having this problem.

**[03:19]** Wikipedia is having this problem.

**[03:19]** Wikipedia is having this problem. They're spending up to 35% of their

**[03:22]** They're spending up to 35% of their

**[03:22]** They're spending up to 35% of their traffic just serving automated clients.

**[03:24]** traffic just serving automated clients.

**[03:24]** traffic just serving automated clients. And they're seeing this increasing

**[03:26]** And they're seeing this increasing

**[03:26]** And they're seeing this increasing significantly and attributing that to AI

**[03:29]** significantly and attributing that to AI

**[03:29]** significantly and attributing that to AI crawlers. So AI is making this worse.

**[03:32]** crawlers. So AI is making this worse.

**[03:32]** crawlers. So AI is making this worse. Scrapers are coming onto sites and

**[03:34]** Scrapers are coming onto sites and

**[03:34]** Scrapers are coming onto sites and pulling down the content and they're not

**[03:37]** pulling down the content and they're not

**[03:37]** pulling down the content and they're not behaving nicely. They're not doing it in

**[03:39]** behaving nicely. They're not doing it in

**[03:39]** behaving nicely. They're not doing it in a gradual way and they're making

**[03:41]** a gradual way and they're making

**[03:41]** a gradual way and they're making hundreds of thousands of requests and

**[03:43]** hundreds of thousands of requests and

**[03:43]** hundreds of thousands of requests and just pulling down content without

**[03:45]** just pulling down content without

**[03:45]** just pulling down content without following the rules.

**[03:50]** In the old days, we had this idea of

**[03:50]** In the old days, we had this idea of good bots and bad bots. And the

**[03:52]** good bots and bad bots. And the

**[03:52]** good bots and bad bots. And the challenge was always distinguishing

**[03:54]** challenge was always distinguishing

**[03:54]** challenge was always distinguishing between them.

**[03:55]** between them.

**[03:56]** between them. If you want your website to show up in a

**[03:57]** If you want your website to show up in a

**[03:57]** If you want your website to show up in a search index like Google, then Google

**[03:59]** search index like Google, then Google

**[03:59]** search index like Google, then Google has to know about your site. has to


### [04:00 - 05:00]

**[04:01]** has to know about your site. has to

**[04:01]** has to know about your site. has to visit and understand your site, but you

**[04:03]** visit and understand your site, but you

**[04:03]** visit and understand your site, but you get a benefit from that because you're

**[04:04]** get a benefit from that because you're

**[04:04]** get a benefit from that because you're going to appear in the search index and

**[04:06]** going to appear in the search index and

**[04:06]** going to appear in the search index and you're going to get traffic as a result.

**[04:08]** you're going to get traffic as a result.

**[04:08]** you're going to get traffic as a result. And so most people consider Google to be

**[04:10]** And so most people consider Google to be

**[04:10]** And so most people consider Google to be a good bot.

**[04:12]** a good bot.

**[04:12]** a good bot. And then there's the bad bots, which are

**[04:14]** And then there's the bad bots, which are

**[04:14]** And then there's the bad bots, which are obviously bad. Scrapers coming to your

**[04:16]** obviously bad. Scrapers coming to your

**[04:16]** obviously bad. Scrapers coming to your site, downloading all the images,

**[04:17]** site, downloading all the images,

**[04:17]** site, downloading all the images, downloading all the content, downloading

**[04:19]** downloading all the content, downloading

**[04:19]** downloading all the content, downloading files. It was very easy to understand

**[04:21]** files. It was very easy to understand

**[04:21]** files. It was very easy to understand that those are the bad bots. But in the

**[04:24]** that those are the bad bots. But in the

**[04:24]** that those are the bad bots. But in the middle, we've got these AI crawlers. And

**[04:27]** middle, we've got these AI crawlers. And

**[04:27]** middle, we've got these AI crawlers. And sometimes they're good, sometimes

**[04:28]** sometimes they're good, sometimes

**[04:28]** sometimes they're good, sometimes they're bad. And it depends on sometimes

**[04:31]** they're bad. And it depends on sometimes

**[04:31]** they're bad. And it depends on sometimes your philosophical approach to AI, but

**[04:33]** your philosophical approach to AI, but

**[04:33]** your philosophical approach to AI, but also what you want from your website

**[04:36]** also what you want from your website

**[04:36]** also what you want from your website because the first kinds of AI bots we

**[04:38]** because the first kinds of AI bots we

**[04:38]** because the first kinds of AI bots we were seeing were for training just to

**[04:40]** were seeing were for training just to

**[04:40]** were seeing were for training just to build up the models and in theory

**[04:43]** build up the models and in theory

**[04:43]** build up the models and in theory there's no benefit to the site owner for

**[04:44]** there's no benefit to the site owner for

**[04:44]** there's no benefit to the site owner for that because it's just being built into

**[04:46]** that because it's just being built into

**[04:46]** that because it's just being built into the model. You're not necessarily

**[04:47]** the model. You're not necessarily

**[04:47]** the model. You're not necessarily getting any traffic. But things have

**[04:50]** getting any traffic. But things have

**[04:50]** getting any traffic. But things have started to change with multiple bots

**[04:52]** started to change with multiple bots

**[04:52]** started to change with multiple bots coming from the different AI providers.

**[04:55]** coming from the different AI providers.

**[04:55]** coming from the different AI providers. So for instance with open AAI they have

**[04:58]** So for instance with open AAI they have

**[04:58]** So for instance with open AAI they have at least four different types of bots.


### [05:00 - 06:00]

**[05:01]** at least four different types of bots.

**[05:01]** at least four different types of bots. So the first one is the open AAI search

**[05:02]** So the first one is the open AAI search

**[05:02]** So the first one is the open AAI search bot. This is kind of classic Google bot

**[05:05]** bot. This is kind of classic Google bot

**[05:05]** bot. This is kind of classic Google bot type um crawler which will come to your

**[05:08]** type um crawler which will come to your

**[05:08]** type um crawler which will come to your site. It will understand what's going on

**[05:10]** site. It will understand what's going on

**[05:10]** site. It will understand what's going on and it will index it so that when

**[05:12]** and it will index it so that when

**[05:12]** and it will index it so that when someone makes a query into chat GPT

**[05:14]** someone makes a query into chat GPT

**[05:14]** someone makes a query into chat GPT using the search functionality you show

**[05:16]** using the search functionality you show

**[05:16]** using the search functionality you show up in OpenAI's index. Now in most cases

**[05:19]** up in OpenAI's index. Now in most cases

**[05:19]** up in OpenAI's index. Now in most cases you're going to want that. It's going to

**[05:20]** you're going to want that. It's going to

**[05:20]** you're going to want that. It's going to do the same thing as Google. You're

**[05:22]** do the same thing as Google. You're

**[05:22]** do the same thing as Google. You're going to appear in a search index.

**[05:24]** going to appear in a search index.

**[05:24]** going to appear in a search index. you're probably going to get citations

**[05:26]** you're probably going to get citations

**[05:26]** you're probably going to get citations and that wasn't the case at the very

**[05:27]** and that wasn't the case at the very

**[05:27]** and that wasn't the case at the very beginning, but now you're getting

**[05:29]** beginning, but now you're getting

**[05:29]** beginning, but now you're getting citations and this is becoming a real

**[05:31]** citations and this is becoming a real

**[05:31]** citations and this is becoming a real source of traffic for sites and for

**[05:33]** source of traffic for sites and for

**[05:33]** source of traffic for sites and for services. People are getting signups as

**[05:35]** services. People are getting signups as

**[05:35]** services. People are getting signups as a result and so there's a win-win. It's

**[05:37]** a result and so there's a win-win. It's

**[05:37]** a result and so there's a win-win. It's it's the same as as the old Google

**[05:39]** it's the same as as the old Google

**[05:39]** it's the same as as the old Google crawlers.

**[05:41]** crawlers.

**[05:41]** crawlers. Then there's chat GPT user and this is a

**[05:43]** Then there's chat GPT user and this is a

**[05:44]** Then there's chat GPT user and this is a little more nuanced. It's where chat GPT

**[05:46]** little more nuanced. It's where chat GPT

**[05:46]** little more nuanced. It's where chat GPT may show up to your website as a result

**[05:48]** may show up to your website as a result

**[05:48]** may show up to your website as a result of a real-time query that a user is

**[05:51]** of a real-time query that a user is

**[05:51]** of a real-time query that a user is making. Maybe you drop the actual URL

**[05:53]** making. Maybe you drop the actual URL

**[05:53]** making. Maybe you drop the actual URL into the chat and ask it to summarize

**[05:55]** into the chat and ask it to summarize

**[05:55]** into the chat and ask it to summarize the content or it's a documentation link

**[05:58]** the content or it's a documentation link

**[05:58]** the content or it's a documentation link and you want to understand how to

**[05:59]** and you want to understand how to

**[05:59]** and you want to understand how to implement something and it's going out


### [06:00 - 07:00]

**[06:00]** implement something and it's going out

**[06:00]** implement something and it's going out and getting that content. It's not used

**[06:03]** and getting that content. It's not used

**[06:03]** and getting that content. It's not used for training, but it may not site the

**[06:07]** for training, but it may not site the

**[06:07]** for training, but it may not site the response. But if you've given it the

**[06:08]** response. But if you've given it the

**[06:08]** response. But if you've given it the URL, then perhaps you're you're a

**[06:10]** URL, then perhaps you're you're a

**[06:10]** URL, then perhaps you're you're a legitimate user. And so maybe you do

**[06:11]** legitimate user. And so maybe you do

**[06:12]** legitimate user. And so maybe you do want that because it's actually your

**[06:13]** want that because it's actually your

**[06:13]** want that because it's actually your users making use of of LLMs.

**[06:16]** users making use of of LLMs.

**[06:16]** users making use of of LLMs. And then there's GPT bot which is the

**[06:18]** And then there's GPT bot which is the

**[06:18]** And then there's GPT bot which is the one that we saw was taking up a huge

**[06:20]** one that we saw was taking up a huge

**[06:20]** one that we saw was taking up a huge amount of um of traffic on Wikipedia and

**[06:23]** amount of um of traffic on Wikipedia and

**[06:23]** amount of um of traffic on Wikipedia and Diaspora and this is the original one

**[06:25]** Diaspora and this is the original one

**[06:25]** Diaspora and this is the original one that is part of the training. It doesn't

**[06:27]** that is part of the training. It doesn't

**[06:27]** that is part of the training. It doesn't benefit you directly. You're being br b

**[06:30]** benefit you directly. You're being br b

**[06:30]** benefit you directly. You're being br b brought into the model and there's often

**[06:32]** brought into the model and there's often

**[06:32]** brought into the model and there's often no citation as a result. These are kind

**[06:35]** no citation as a result. These are kind

**[06:35]** no citation as a result. These are kind of the three crawler bots that you might

**[06:37]** of the three crawler bots that you might

**[06:37]** of the three crawler bots that you might see on your site. And then what we're

**[06:39]** see on your site. And then what we're

**[06:39]** see on your site. And then what we're seeing more of now is the computer use

**[06:41]** seeing more of now is the computer use

**[06:41]** seeing more of now is the computer use operator type bots which are acting on

**[06:45]** operator type bots which are acting on

**[06:45]** operator type bots which are acting on behalf of a real person possibly with a

**[06:47]** behalf of a real person possibly with a

**[06:47]** behalf of a real person possibly with a web browser that's running in a VM that

**[06:50]** web browser that's running in a VM that

**[06:50]** web browser that's running in a VM that is taking an action as an agent an

**[06:52]** is taking an action as an agent an

**[06:52]** is taking an action as an agent an autonomous agent. And this becomes

**[06:55]** autonomous agent. And this becomes

**[06:55]** autonomous agent. And this becomes challenging to understand well do you

**[06:56]** challenging to understand well do you

**[06:56]** challenging to understand well do you want that or not? Maybe it's a

**[06:58]** want that or not? Maybe it's a

**[06:58]** want that or not? Maybe it's a legitimate use case. Maybe the agent is


### [07:00 - 08:00]

**[07:00]** legitimate use case. Maybe the agent is

**[07:00]** legitimate use case. Maybe the agent is doing triage of your inbox. Maybe Google

**[07:02]** doing triage of your inbox. Maybe Google

**[07:02]** doing triage of your inbox. Maybe Google would want that if it's Gmail. But if

**[07:05]** would want that if it's Gmail. But if

**[07:05]** would want that if it's Gmail. But if you've asked an agent to go out and buy

**[07:07]** you've asked an agent to go out and buy

**[07:07]** you've asked an agent to go out and buy 500 concert tickets so you can then go

**[07:08]** 500 concert tickets so you can then go

**[07:08]** 500 concert tickets so you can then go and sell them for a profit, that's

**[07:11]** and sell them for a profit, that's

**[07:11]** and sell them for a profit, that's probably something you don't want to

**[07:12]** probably something you don't want to

**[07:12]** probably something you don't want to allow. And so understanding being able

**[07:14]** allow. And so understanding being able

**[07:14]** allow. And so understanding being able to detect these is really challenging.

**[07:16]** to detect these is really challenging.

**[07:16]** to detect these is really challenging. The OpenAI crawlers identify themselves

**[07:19]** The OpenAI crawlers identify themselves

**[07:19]** The OpenAI crawlers identify themselves as such. You can verify that and so you

**[07:22]** as such. You can verify that and so you

**[07:22]** as such. You can verify that and so you can allow or block them. But something

**[07:24]** can allow or block them. But something

**[07:24]** can allow or block them. But something like operator just shows up as a Chrome

**[07:26]** like operator just shows up as a Chrome

**[07:26]** like operator just shows up as a Chrome browser and it's much more challenging

**[07:28]** browser and it's much more challenging

**[07:28]** browser and it's much more challenging to understand and detect that.

**[07:32]** to understand and detect that.

**[07:32]** to understand and detect that. So let's walk through some of the

**[07:34]** So let's walk through some of the

**[07:34]** So let's walk through some of the defenses that you can implement and to

**[07:36]** defenses that you can implement and to

**[07:36]** defenses that you can implement and to decide as a site owner how you can

**[07:38]** decide as a site owner how you can

**[07:38]** decide as a site owner how you can control the kind of traffic that's

**[07:40]** control the kind of traffic that's

**[07:40]** control the kind of traffic that's coming to your site. So the first one of

**[07:42]** coming to your site. So the first one of

**[07:42]** coming to your site. So the first one of these is it's not really a defense

**[07:44]** these is it's not really a defense

**[07:44]** these is it's not really a defense because it's entirely voluntary.

**[07:45]** because it's entirely voluntary.

**[07:45]** because it's entirely voluntary. Everyone's probably heard of robots.ext.

**[07:47]** Everyone's probably heard of robots.ext.

**[07:47]** Everyone's probably heard of robots.ext. It's how you can describe the structure

**[07:50]** It's how you can describe the structure

**[07:50]** It's how you can describe the structure of your website and tell different

**[07:52]** of your website and tell different

**[07:52]** of your website and tell different crawlers what you want them to do. You

**[07:54]** crawlers what you want them to do. You

**[07:54]** crawlers what you want them to do. You can allow or disallow. You can um

**[07:56]** can allow or disallow. You can um

**[07:56]** can allow or disallow. You can um control particular crawlers. And this


### [08:00 - 09:00]

**[08:00]** control particular crawlers. And this

**[08:00]** control particular crawlers. And this gives you a good understanding of your

**[08:02]** gives you a good understanding of your

**[08:02]** gives you a good understanding of your own site to think through the steps that

**[08:04]** own site to think through the steps that

**[08:04]** own site to think through the steps that you want to take to allow or disallow.

**[08:05]** you want to take to allow or disallow.

**[08:06]** you want to take to allow or disallow. But it's entirely voluntary.

**[08:08]** But it's entirely voluntary.

**[08:08]** But it's entirely voluntary. Crawlers don't have to follow it, but

**[08:09]** Crawlers don't have to follow it, but

**[08:09]** Crawlers don't have to follow it, but the good ones will. Google bot will

**[08:11]** the good ones will. Google bot will

**[08:11]** the good ones will. Google bot will follow this as will all the search

**[08:13]** follow this as will all the search

**[08:13]** follow this as will all the search crawlers. Open AAI claims to follow it

**[08:15]** crawlers. Open AAI claims to follow it

**[08:15]** crawlers. Open AAI claims to follow it and does for the most part as well. But

**[08:17]** and does for the most part as well. But

**[08:17]** and does for the most part as well. But for the types of bots that are causing

**[08:19]** for the types of bots that are causing

**[08:19]** for the types of bots that are causing these problems, they're not following

**[08:21]** these problems, they're not following

**[08:21]** these problems, they're not following this. And in some cases, they're

**[08:23]** this. And in some cases, they're

**[08:23]** this. And in some cases, they're actually using this to find pages on

**[08:25]** actually using this to find pages on

**[08:25]** actually using this to find pages on your site that you've disallowed other

**[08:27]** your site that you've disallowed other

**[08:27]** your site that you've disallowed other bots to go to and deliberately going out

**[08:29]** bots to go to and deliberately going out

**[08:29]** bots to go to and deliberately going out and getting that content.

**[08:31]** and getting that content.

**[08:31]** and getting that content. Even so, this is a good place to start

**[08:33]** Even so, this is a good place to start

**[08:33]** Even so, this is a good place to start because it helps you start to think

**[08:34]** because it helps you start to think

**[08:34]** because it helps you start to think through what you want different bots to

**[08:37]** through what you want different bots to

**[08:37]** through what you want different bots to be doing on your site.

**[08:42]** Every request that comes into your site

**[08:42]** Every request that comes into your site is going to identify itself. This is a

**[08:44]** is going to identify itself. This is a

**[08:44]** is going to identify itself. This is a required HTTP header. Um, and it's just

**[08:47]** required HTTP header. Um, and it's just

**[08:48]** required HTTP header. Um, and it's just a string. It is a name that the crawler

**[08:51]** a string. It is a name that the crawler

**[08:51]** a string. It is a name that the crawler is going to give itself and you'll see

**[08:52]** is going to give itself and you'll see

**[08:52]** is going to give itself and you'll see that in your request logs. It's just a

**[08:55]** that in your request logs. It's just a

**[08:55]** that in your request logs. It's just a string because any any a client can set

**[08:58]** string because any any a client can set

**[08:58]** string because any any a client can set whatever they like for this. But it's


### [09:00 - 10:00]

**[09:00]** whatever they like for this. But it's

**[09:00]** whatever they like for this. But it's surprising how many will actually just

**[09:01]** surprising how many will actually just

**[09:02]** surprising how many will actually just tell you who they are. And you can you

**[09:04]** tell you who they are. And you can you

**[09:04]** tell you who they are. And you can you can use open source libraries um to

**[09:07]** can use open source libraries um to

**[09:07]** can use open source libraries um to detect this and create rules around it.

**[09:10]** detect this and create rules around it.

**[09:10]** detect this and create rules around it. At ArtJet, we've got a open source

**[09:11]** At ArtJet, we've got a open source

**[09:11]** At ArtJet, we've got a open source project with um several thousand

**[09:13]** project with um several thousand

**[09:13]** project with um several thousand different user agents um that you can

**[09:15]** different user agents um that you can

**[09:15]** different user agents um that you can download and use to build your own rules

**[09:17]** download and use to build your own rules

**[09:17]** download and use to build your own rules to identify who you want to access your

**[09:20]** to identify who you want to access your

**[09:20]** to identify who you want to access your site, but it's just a string in a HTTP

**[09:23]** site, but it's just a string in a HTTP

**[09:23]** site, but it's just a string in a HTTP header and you can set it to whatever

**[09:24]** header and you can set it to whatever

**[09:24]** header and you can set it to whatever you want. And so the bad bots will just

**[09:27]** you want. And so the bad bots will just

**[09:27]** you want. And so the bad bots will just change this. They'll pretend to be

**[09:28]** change this. They'll pretend to be

**[09:28]** change this. They'll pretend to be Google or they'll pretend to be Chrome.

**[09:30]** Google or they'll pretend to be Chrome.

**[09:30]** Google or they'll pretend to be Chrome. And so it is not always a good signal

**[09:33]** And so it is not always a good signal

**[09:33]** And so it is not always a good signal about who's actually visiting your site.

**[09:36]** about who's actually visiting your site.

**[09:36]** about who's actually visiting your site. So the next thing you can do is to

**[09:38]** So the next thing you can do is to

**[09:38]** So the next thing you can do is to verify that if a request is made to your

**[09:42]** verify that if a request is made to your

**[09:42]** verify that if a request is made to your site and it claims to be Apple's

**[09:44]** site and it claims to be Apple's

**[09:44]** site and it claims to be Apple's crawler, Bing, Google, OpenAI,

**[09:47]** crawler, Bing, Google, OpenAI,

**[09:48]** crawler, Bing, Google, OpenAI, all of these services support

**[09:49]** all of these services support

**[09:49]** all of these services support verification. So you can look at the

**[09:52]** verification. So you can look at the

**[09:52]** verification. So you can look at the source IP address and you can query

**[09:55]** source IP address and you can query

**[09:55]** source IP address and you can query those services using a reverse DNS

**[09:57]** those services using a reverse DNS

**[09:57]** those services using a reverse DNS lookup to check whether it is actually

**[09:59]** lookup to check whether it is actually

**[09:59]** lookup to check whether it is actually who it claims to be. So if you see a


### [10:00 - 11:00]

**[10:01]** who it claims to be. So if you see a

**[10:02]** who it claims to be. So if you see a request coming from Google, you can ask

**[10:04]** request coming from Google, you can ask

**[10:04]** request coming from Google, you can ask Google is this actually Google and

**[10:06]** Google is this actually Google and

**[10:06]** Google is this actually Google and they'll give you a response back saying

**[10:08]** they'll give you a response back saying

**[10:08]** they'll give you a response back saying whether it is or not. And this makes it

**[10:11]** whether it is or not. And this makes it

**[10:11]** whether it is or not. And this makes it quite straightforward to use the

**[10:12]** quite straightforward to use the

**[10:12]** quite straightforward to use the combination of the user agent string

**[10:15]** combination of the user agent string

**[10:15]** combination of the user agent string plus IP verification to check whether it

**[10:18]** plus IP verification to check whether it

**[10:18]** plus IP verification to check whether it is the good bots are visiting your site

**[10:20]** is the good bots are visiting your site

**[10:20]** is the good bots are visiting your site and to set up some simple rules to allow

**[10:22]** and to set up some simple rules to allow

**[10:22]** and to set up some simple rules to allow those crawlers that you actually want to

**[10:23]** those crawlers that you actually want to

**[10:23]** those crawlers that you actually want to be on the site.

**[10:28]** things start to get a bit more

**[10:28]** things start to get a bit more complicated if those signals don't

**[10:30]** complicated if those signals don't

**[10:30]** complicated if those signals don't provide you with sufficient information.

**[10:33]** provide you with sufficient information.

**[10:33]** provide you with sufficient information. Bot detection is not 100% accurate and

**[10:37]** Bot detection is not 100% accurate and

**[10:37]** Bot detection is not 100% accurate and so you have to build up these layers.

**[10:39]** so you have to build up these layers.

**[10:39]** so you have to build up these layers. And so the next thing you can do is

**[10:40]** And so the next thing you can do is

**[10:40]** And so the next thing you can do is looking at IP addresses.

**[10:43]** looking at IP addresses.

**[10:43]** looking at IP addresses. The idea is to build up a pattern to

**[10:46]** The idea is to build up a pattern to

**[10:46]** The idea is to build up a pattern to understand what is normal from each IP

**[10:49]** understand what is normal from each IP

**[10:49]** understand what is normal from each IP address and not just a single IP address

**[10:51]** address and not just a single IP address

**[10:51]** address and not just a single IP address but the different IP address ranges how

**[10:54]** but the different IP address ranges how

**[10:54]** but the different IP address ranges how they associate with different networks

**[10:56]** they associate with different networks

**[10:56]** they associate with different networks and different network operators whether

**[10:58]** and different network operators whether

**[10:58]** and different network operators whether the request is coming from a data center


### [11:00 - 12:00]

**[11:00]** the request is coming from a data center

**[11:00]** the request is coming from a data center or not and the country level information

**[11:03]** or not and the country level information

**[11:04]** or not and the country level information and you can get this from various

**[11:06]** and you can get this from various

**[11:06]** and you can get this from various databases. um you have to pay for access

**[11:08]** databases. um you have to pay for access

**[11:08]** databases. um you have to pay for access to most of them, but there are also some

**[11:10]** to most of them, but there are also some

**[11:10]** to most of them, but there are also some free APIs you can use to query the

**[11:12]** free APIs you can use to query the

**[11:12]** free APIs you can use to query the metadata associated with a particular IP

**[11:14]** metadata associated with a particular IP

**[11:14]** metadata associated with a particular IP address. MaxMine and IP info are two

**[11:17]** address. MaxMine and IP info are two

**[11:18]** address. MaxMine and IP info are two more popular ones. And you want to be

**[11:20]** more popular ones. And you want to be

**[11:20]** more popular ones. And you want to be looking at things like, well, where's

**[11:21]** looking at things like, well, where's

**[11:22]** looking at things like, well, where's the traffic coming from? And what is the

**[11:24]** the traffic coming from? And what is the

**[11:24]** the traffic coming from? And what is the association with the network? Is this

**[11:25]** association with the network? Is this

**[11:26]** association with the network? Is this coming from a VPN or a proxy? Is it a

**[11:28]** coming from a VPN or a proxy? Is it a

**[11:28]** coming from a VPN or a proxy? Is it a residential or mobile IP address?

**[11:31]** residential or mobile IP address?

**[11:31]** residential or mobile IP address? And last year, 12% of all bot traffic

**[11:36]** And last year, 12% of all bot traffic

**[11:36]** And last year, 12% of all bot traffic that hit the Cloudflare network was from

**[11:38]** that hit the Cloudflare network was from

**[11:38]** that hit the Cloudflare network was from the AWS network. And so you can start to

**[11:41]** the AWS network. And so you can start to

**[11:41]** the AWS network. And so you can start to ask yourself, well, are the normal users

**[11:44]** ask yourself, well, are the normal users

**[11:44]** ask yourself, well, are the normal users of our site and application going to

**[11:46]** of our site and application going to

**[11:46]** of our site and application going to come from a data center. Maybe if you're

**[11:49]** come from a data center. Maybe if you're

**[11:49]** come from a data center. Maybe if you're allowing crawlers on your site, then

**[11:51]** allowing crawlers on your site, then

**[11:51]** allowing crawlers on your site, then that's ex that's expected. But if you

**[11:54]** that's ex that's expected. But if you

**[11:54]** that's ex that's expected. But if you have a signup form that you're expecting

**[11:56]** have a signup form that you're expecting

**[11:56]** have a signup form that you're expecting only humans to submit, then it's

**[11:58]** only humans to submit, then it's

**[11:58]** only humans to submit, then it's unlikely that a request that's coming


### [12:00 - 13:00]

**[12:00]** unlikely that a request that's coming

**[12:00]** unlikely that a request that's coming from a data center IP address is going

**[12:02]** from a data center IP address is going

**[12:02]** from a data center IP address is going to be traffic that you want to accept.

**[12:07]** to be traffic that you want to accept.

**[12:07]** to be traffic that you want to accept. The challenge with looking at geo data

**[12:09]** The challenge with looking at geo data

**[12:09]** The challenge with looking at geo data like blocking a single country for

**[12:10]** like blocking a single country for

**[12:10]** like blocking a single country for instance um is that the geodata is

**[12:13]** instance um is that the geodata is

**[12:13]** instance um is that the geodata is notoriously inaccurate and has become

**[12:16]** notoriously inaccurate and has become

**[12:16]** notoriously inaccurate and has become more inaccurate over time as people are

**[12:17]** more inaccurate over time as people are

**[12:17]** more inaccurate over time as people are using satellite and cell phone

**[12:19]** using satellite and cell phone

**[12:19]** using satellite and cell phone connectivity 5G because the IP address

**[12:23]** connectivity 5G because the IP address

**[12:23]** connectivity 5G because the IP address will be geoloccated to the owner of the

**[12:25]** will be geoloccated to the owner of the

**[12:25]** will be geoloccated to the owner of the IP rather than necessarily the the user

**[12:28]** IP rather than necessarily the the user

**[12:28]** IP rather than necessarily the the user of it. And also even when the database

**[12:32]** of it. And also even when the database

**[12:32]** of it. And also even when the database is saying that the IP address is coming

**[12:34]** is saying that the IP address is coming

**[12:34]** is saying that the IP address is coming from a residential network, there are

**[12:36]** from a residential network, there are

**[12:36]** from a residential network, there are proxy services that you can just buy

**[12:38]** proxy services that you can just buy

**[12:38]** proxy services that you can just buy access to which will route your traffic

**[12:41]** access to which will route your traffic

**[12:41]** access to which will route your traffic through those residential um networks to

**[12:43]** through those residential um networks to

**[12:43]** through those residential um networks to appear like it's coming from a home ISP

**[12:46]** appear like it's coming from a home ISP

**[12:46]** appear like it's coming from a home ISP or a mobile device. So you can't always

**[12:48]** or a mobile device. So you can't always

**[12:48]** or a mobile device. So you can't always trust these and you have to build up

**[12:50]** trust these and you have to build up

**[12:50]** trust these and you have to build up signals and build your own database to

**[12:53]** signals and build your own database to

**[12:53]** signals and build your own database to understand where this traffic is coming

**[12:54]** understand where this traffic is coming

**[12:54]** understand where this traffic is coming from and what the likelihood is that

**[12:56]** from and what the likelihood is that

**[12:56]** from and what the likelihood is that it's an automated client.


### [13:00 - 14:00]

**[13:03]** Captures are the standard thing that

**[13:03]** Captures are the standard thing that we've been using um now for decades to

**[13:06]** we've been using um now for decades to

**[13:06]** we've been using um now for decades to try and distinguish between humans and

**[13:09]** try and distinguish between humans and

**[13:09]** try and distinguish between humans and automated clients, solving puzzles, um

**[13:12]** automated clients, solving puzzles, um

**[13:12]** automated clients, solving puzzles, um moving things around on the screen, but

**[13:13]** moving things around on the screen, but

**[13:13]** moving things around on the screen, but it's becoming increasingly easy for AI

**[13:16]** it's becoming increasingly easy for AI

**[13:16]** it's becoming increasingly easy for AI to solve those. Putting them into an LLM

**[13:19]** to solve those. Putting them into an LLM

**[13:19]** to solve those. Putting them into an LLM or downloading the audio version and

**[13:21]** or downloading the audio version and

**[13:21]** or downloading the audio version and transcribing it can be done in just a

**[13:23]** transcribing it can be done in just a

**[13:23]** transcribing it can be done in just a couple of seconds. and it's trivial and

**[13:25]** couple of seconds. and it's trivial and

**[13:25]** couple of seconds. and it's trivial and cheap to breach these kinds of defenses.

**[13:33]** There are newer approaches to this.

**[13:33]** There are newer approaches to this. Proof of work, which is come from the

**[13:36]** Proof of work, which is come from the

**[13:36]** Proof of work, which is come from the crypto um side of things, means that you

**[13:40]** crypto um side of things, means that you

**[13:40]** crypto um side of things, means that you require a computer to do certain number

**[13:42]** require a computer to do certain number

**[13:42]** require a computer to do certain number of calculations

**[13:43]** of calculations

**[13:43]** of calculations and provide the answer to to a puzzle

**[13:47]** and provide the answer to to a puzzle

**[13:47]** and provide the answer to to a puzzle before they can access the resource. And

**[13:49]** before they can access the resource. And

**[13:49]** before they can access the resource. And this usually takes a certain amount of

**[13:51]** this usually takes a certain amount of

**[13:51]** this usually takes a certain amount of time. It costs CPU time and on an

**[13:54]** time. It costs CPU time and on an

**[13:54]** time. It costs CPU time and on an individual basis on your laptop or on

**[13:56]** individual basis on your laptop or on

**[13:56]** individual basis on your laptop or on your phone, it might take a second or

**[13:58]** your phone, it might take a second or

**[13:58]** your phone, it might take a second or two to calculate it and it makes no real


### [14:00 - 15:00]

**[14:00]** two to calculate it and it makes no real

**[14:00]** two to calculate it and it makes no real difference to an individual. But if you

**[14:02]** difference to an individual. But if you

**[14:02]** difference to an individual. But if you have a crawler that's going to tens of

**[14:04]** have a crawler that's going to tens of

**[14:04]** have a crawler that's going to tens of thousands or millions of websites and is

**[14:06]** thousands or millions of websites and is

**[14:06]** thousands or millions of websites and is having to solve this puzzle every single

**[14:08]** having to solve this puzzle every single

**[14:08]** having to solve this puzzle every single time, it becomes very expensive to do

**[14:10]** time, it becomes very expensive to do

**[14:10]** time, it becomes very expensive to do that. And so deploying these proofof

**[14:13]** that. And so deploying these proofof

**[14:13]** that. And so deploying these proofof work options on your website can be a

**[14:15]** work options on your website can be a

**[14:15]** work options on your website can be a way to um to prevent those crawlers.

**[14:19]** way to um to prevent those crawlers.

**[14:19]** way to um to prevent those crawlers. But then it becomes a question of

**[14:21]** But then it becomes a question of

**[14:21]** But then it becomes a question of incentives. So if you're crawling

**[14:23]** incentives. So if you're crawling

**[14:23]** incentives. So if you're crawling millions of websites, then maybe that is

**[14:25]** millions of websites, then maybe that is

**[14:25]** millions of websites, then maybe that is a good defense. But if we go back to

**[14:27]** a good defense. But if we go back to

**[14:27]** a good defense. But if we go back to that ticket example, if it costs someone

**[14:30]** that ticket example, if it costs someone

**[14:30]** that ticket example, if it costs someone a couple of dollars to solve a capture

**[14:32]** a couple of dollars to solve a capture

**[14:32]** a couple of dollars to solve a capture or to solve a proof of work, but they're

**[14:34]** or to solve a proof of work, but they're

**[14:34]** or to solve a proof of work, but they're then going to sell a ticket for $200 or

**[14:36]** then going to sell a ticket for $200 or

**[14:36]** then going to sell a ticket for $200 or $300,

**[14:38]** $300,

**[14:38]** $300, the profit is still there. And so these

**[14:40]** the profit is still there. And so these

**[14:40]** the profit is still there. And so these may not even be a defense against

**[14:42]** may not even be a defense against

**[14:42]** may not even be a defense against certain types of um of attacks.

**[14:46]** certain types of um of attacks.

**[14:46]** certain types of um of attacks. You can scale the difficulty. So, if you

**[14:48]** You can scale the difficulty. So, if you

**[14:48]** You can scale the difficulty. So, if you bring in all these different signals and

**[14:50]** bring in all these different signals and

**[14:50]** bring in all these different signals and see that something is coming from an

**[14:52]** see that something is coming from an

**[14:52]** see that something is coming from an unverified IP address and has suspicious

**[14:55]** unverified IP address and has suspicious

**[14:55]** unverified IP address and has suspicious um suspicious uh characteristics, then

**[14:57]** um suspicious uh characteristics, then

**[14:57]** um suspicious uh characteristics, then maybe you could give them a harder

**[14:59]** maybe you could give them a harder

**[14:59]** maybe you could give them a harder puzzle. But then you start to have


### [15:00 - 16:00]

**[15:00]** puzzle. But then you start to have

**[15:00]** puzzle. But then you start to have accessibility problems and I'm sure

**[15:02]** accessibility problems and I'm sure

**[15:02]** accessibility problems and I'm sure we've all seen those really annoying

**[15:04]** we've all seen those really annoying

**[15:04]** we've all seen those really annoying captures that you can't solve and you

**[15:06]** captures that you can't solve and you

**[15:06]** captures that you can't solve and you have to keep refreshing. Um that becomes

**[15:08]** have to keep refreshing. Um that becomes

**[15:08]** have to keep refreshing. Um that becomes a problem as well.

**[15:13]** There are a couple of interesting open

**[15:13]** There are a couple of interesting open source projects that implement these.

**[15:15]** source projects that implement these.

**[15:15]** source projects that implement these. Anubis is a good one. Go away and

**[15:17]** Anubis is a good one. Go away and

**[15:17]** Anubis is a good one. Go away and Nepenthees. These are all proxies that

**[15:19]** Nepenthees. These are all proxies that

**[15:20]** Nepenthees. These are all proxies that you can install on the Kubernetes

**[15:21]** you can install on the Kubernetes

**[15:21]** you can install on the Kubernetes cluster um or put them in front of your

**[15:23]** cluster um or put them in front of your

**[15:23]** cluster um or put them in front of your your application. You can run it

**[15:24]** your application. You can run it

**[15:24]** your application. You can run it yourself and it will implement these

**[15:26]** yourself and it will implement these

**[15:26]** yourself and it will implement these proof of work problems and put it in

**[15:28]** proof of work problems and put it in

**[15:28]** proof of work problems and put it in front of the users that it thinks are

**[15:30]** front of the users that it thinks are

**[15:30]** front of the users that it thinks are suspicious.

**[15:35]** And there are also some emerging

**[15:36]** And there are also some emerging standards around introducing signatures

**[15:38]** standards around introducing signatures

**[15:38]** standards around introducing signatures into requests because what we're trying

**[15:40]** into requests because what we're trying

**[15:40]** into requests because what we're trying to do is to prove that a particular

**[15:43]** to do is to prove that a particular

**[15:43]** to do is to prove that a particular client is who they say it is and is who

**[15:46]** client is who they say it is and is who

**[15:46]** client is who they say it is and is who you want to be on the website. Now,

**[15:48]** you want to be on the website. Now,

**[15:48]** you want to be on the website. Now, Cloudflare has suggested this idea of

**[15:51]** Cloudflare has suggested this idea of

**[15:51]** Cloudflare has suggested this idea of HTTP message signatures for automated

**[15:53]** HTTP message signatures for automated

**[15:53]** HTTP message signatures for automated clients where every request will include

**[15:55]** clients where every request will include

**[15:55]** clients where every request will include a cryptographic signature which you can

**[15:57]** a cryptographic signature which you can

**[15:57]** a cryptographic signature which you can then verify very quickly and then you

**[15:59]** then verify very quickly and then you

**[15:59]** then verify very quickly and then you can understand which which client is


### [16:00 - 17:00]

**[16:02]** can understand which which client is

**[16:02]** can understand which which client is coming to your site. This is only just

**[16:05]** coming to your site. This is only just

**[16:05]** coming to your site. This is only just been announced a couple of weeks ago, so

**[16:06]** been announced a couple of weeks ago, so

**[16:06]** been announced a couple of weeks ago, so it's still being developed. There's some

**[16:08]** it's still being developed. There's some

**[16:08]** it's still being developed. There's some questions around whether it's any better

**[16:10]** questions around whether it's any better

**[16:10]** questions around whether it's any better than just verifying the IP address, but

**[16:12]** than just verifying the IP address, but

**[16:12]** than just verifying the IP address, but it's a way of verifying automated

**[16:14]** it's a way of verifying automated

**[16:14]** it's a way of verifying automated clients. And then a couple of years ago,

**[16:16]** clients. And then a couple of years ago,

**[16:16]** clients. And then a couple of years ago, Apple announced private access tokens

**[16:19]** Apple announced private access tokens

**[16:19]** Apple announced private access tokens and what they called a privacy pass,

**[16:22]** and what they called a privacy pass,

**[16:22]** and what they called a privacy pass, which allowed website owners to verify

**[16:25]** which allowed website owners to verify

**[16:25]** which allowed website owners to verify that a request was coming from a browser

**[16:28]** that a request was coming from a browser

**[16:28]** that a request was coming from a browser that was owned by an iCloud subscriber.

**[16:31]** that was owned by an iCloud subscriber.

**[16:31]** that was owned by an iCloud subscriber. This has been implemented across all

**[16:32]** This has been implemented across all

**[16:32]** This has been implemented across all Apple devices. If you're using Safari,

**[16:35]** Apple devices. If you're using Safari,

**[16:35]** Apple devices. If you're using Safari, this is on um and it will reduce the

**[16:37]** this is on um and it will reduce the

**[16:38]** this is on um and it will reduce the number of captures that you might see

**[16:39]** number of captures that you might see

**[16:39]** number of captures that you might see because you can verify that someone's

**[16:41]** because you can verify that someone's

**[16:41]** because you can verify that someone's actually a paying subscriber to iCloud.

**[16:43]** actually a paying subscriber to iCloud.

**[16:43]** actually a paying subscriber to iCloud. but it's had limited adoption elsewhere.

**[16:46]** but it's had limited adoption elsewhere.

**[16:46]** but it's had limited adoption elsewhere. Not many sites are using it and it's

**[16:48]** Not many sites are using it and it's

**[16:48]** Not many sites are using it and it's only on the Apple ecosystem even though

**[16:50]** only on the Apple ecosystem even though

**[16:50]** only on the Apple ecosystem even though it's a it's almost an approved standard.

**[16:58]** And then we have to implement

**[16:58]** And then we have to implement fingerprints as well. So fingerprinting


### [17:00 - 18:00]

**[17:00]** fingerprints as well. So fingerprinting

**[17:00]** fingerprints as well. So fingerprinting is looking at the network requests to

**[17:03]** is looking at the network requests to

**[17:03]** is looking at the network requests to generate a hash to be able to identify

**[17:05]** generate a hash to be able to identify

**[17:05]** generate a hash to be able to identify that client because it's quite trivial

**[17:09]** that client because it's quite trivial

**[17:09]** that client because it's quite trivial to change the IP address that your

**[17:10]** to change the IP address that your

**[17:10]** to change the IP address that your requests are coming from. And you'll

**[17:11]** requests are coming from. And you'll

**[17:12]** requests are coming from. And you'll often see crawlers using banks of tens

**[17:14]** often see crawlers using banks of tens

**[17:14]** often see crawlers using banks of tens or hundreds of thousands of different IP

**[17:16]** or hundreds of thousands of different IP

**[17:16]** or hundreds of thousands of different IP addresses, particularly with IPv6, which

**[17:19]** addresses, particularly with IPv6, which

**[17:19]** addresses, particularly with IPv6, which means implementing

**[17:21]** means implementing

**[17:21]** means implementing um signatures based just on an IP

**[17:23]** um signatures based just on an IP

**[17:23]** um signatures based just on an IP address isn't sufficient, but the client

**[17:26]** address isn't sufficient, but the client

**[17:26]** address isn't sufficient, but the client stays the same. The client

**[17:27]** stays the same. The client

**[17:28]** stays the same. The client characteristics stay the same across

**[17:29]** characteristics stay the same across

**[17:29]** characteristics stay the same across multiple requests and you can build up a

**[17:31]** multiple requests and you can build up a

**[17:31]** multiple requests and you can build up a fingerprint of that. This is the open

**[17:34]** fingerprint of that. This is the open

**[17:34]** fingerprint of that. This is the open source J4 hash which is based on the TLS

**[17:37]** source J4 hash which is based on the TLS

**[17:37]** source J4 hash which is based on the TLS fingerprint looking at the network level

**[17:39]** fingerprint looking at the network level

**[17:39]** fingerprint looking at the network level um and looking at the configuration of

**[17:41]** um and looking at the configuration of

**[17:41]** um and looking at the configuration of SSL

**[17:43]** SSL

**[17:43]** SSL and then there's a proprietary version

**[17:45]** and then there's a proprietary version

**[17:45]** and then there's a proprietary version on HTTP which looking at headers um and

**[17:48]** on HTTP which looking at headers um and

**[17:48]** on HTTP which looking at headers um and the different headers that are sent with

**[17:49]** the different headers that are sent with

**[17:49]** the different headers that are sent with a client and the characteristics of an

**[17:51]** a client and the characteristics of an

**[17:51]** a client and the characteristics of an HTTP request to build up a fingerprint

**[17:54]** HTTP request to build up a fingerprint

**[17:54]** HTTP request to build up a fingerprint and then you can use those fingerprints

**[17:55]** and then you can use those fingerprints

**[17:55]** and then you can use those fingerprints as part of your block rules. So you

**[17:57]** as part of your block rules. So you

**[17:57]** as part of your block rules. So you could look at all the hundreds of

**[17:59]** could look at all the hundreds of

**[17:59]** could look at all the hundreds of thousands of requests coming from a


### [18:00 - 19:00]

**[18:00]** thousands of requests coming from a

**[18:00]** thousands of requests coming from a single fingerprint. You could just block

**[18:02]** single fingerprint. You could just block

**[18:02]** single fingerprint. You could just block that fingerprint regardless of how many

**[18:04]** that fingerprint regardless of how many

**[18:04]** that fingerprint regardless of how many IP addresses it's coming across.

**[18:11]** And then rate limiting is used in

**[18:11]** And then rate limiting is used in conjunction with a fingerprint. Once you

**[18:14]** conjunction with a fingerprint. Once you

**[18:14]** conjunction with a fingerprint. Once you can fingerprint the client, you can

**[18:15]** can fingerprint the client, you can

**[18:15]** can fingerprint the client, you can apply quotas or a limit to it. And the

**[18:18]** apply quotas or a limit to it. And the

**[18:18]** apply quotas or a limit to it. And the key is really important there. You can't

**[18:19]** key is really important there. You can't

**[18:19]** key is really important there. You can't just rate limit on an IP address because

**[18:22]** just rate limit on an IP address because

**[18:22]** just rate limit on an IP address because people have different IPs. It changes

**[18:24]** people have different IPs. It changes

**[18:24]** people have different IPs. It changes all the time. And then for malicious

**[18:25]** all the time. And then for malicious

**[18:26]** all the time. And then for malicious crawlers, they can just change them

**[18:27]** crawlers, they can just change them

**[18:27]** crawlers, they can just change them themselves. And so keying off user

**[18:30]** themselves. And so keying off user

**[18:30]** themselves. And so keying off user session ID is a good way to do it. If

**[18:32]** session ID is a good way to do it. If

**[18:32]** session ID is a good way to do it. If the user is logged in and you want to

**[18:34]** the user is logged in and you want to

**[18:34]** the user is logged in and you want to apply your rate limits or if you've got

**[18:36]** apply your rate limits or if you've got

**[18:36]** apply your rate limits or if you've got the um the fingerprint, the J4 hash, you

**[18:40]** the um the fingerprint, the J4 hash, you

**[18:40]** the um the fingerprint, the J4 hash, you can implement rate limits on that.

**[18:47]** So these are the eight defenses.

**[18:47]** So these are the eight defenses. Robots.ext is where you start. It's not

**[18:50]** Robots.ext is where you start. It's not

**[18:50]** Robots.ext is where you start. It's not where you finish though because it's not

**[18:52]** where you finish though because it's not

**[18:52]** where you finish though because it's not going to prevent all the bots. It's a

**[18:54]** going to prevent all the bots. It's a

**[18:54]** going to prevent all the bots. It's a voluntary standard. It's where you start

**[18:56]** voluntary standard. It's where you start

**[18:56]** voluntary standard. It's where you start because it helps with the the good bots.

**[18:59]** because it helps with the the good bots.

**[18:59]** because it helps with the the good bots. At the very least, you need to be


### [19:00 - 20:00]

**[19:00]** At the very least, you need to be

**[19:00]** At the very least, you need to be looking at user agents. There are

**[19:02]** looking at user agents. There are

**[19:02]** looking at user agents. There are various open source options for looking

**[19:04]** various open source options for looking

**[19:04]** various open source options for looking at that and setting up rules and then

**[19:06]** at that and setting up rules and then

**[19:06]** at that and setting up rules and then verifying that the user agent for

**[19:08]** verifying that the user agent for

**[19:08]** verifying that the user agent for clients that you actually want on your

**[19:10]** clients that you actually want on your

**[19:10]** clients that you actually want on your site are the ones that are actually

**[19:12]** site are the ones that are actually

**[19:12]** site are the ones that are actually making the requests. That gets you most

**[19:15]** making the requests. That gets you most

**[19:15]** making the requests. That gets you most of the way. For most sites, that will

**[19:17]** of the way. For most sites, that will

**[19:17]** of the way. For most sites, that will deal with everything you need. But for

**[19:19]** deal with everything you need. But for

**[19:19]** deal with everything you need. But for the more popular ones or sites with

**[19:21]** the more popular ones or sites with

**[19:21]** the more popular ones or sites with particularly um interesting resources or

**[19:25]** particularly um interesting resources or

**[19:25]** particularly um interesting resources or things that that people might want to

**[19:26]** things that that people might want to

**[19:26]** things that that people might want to buy lots lots of numbers of or they're

**[19:28]** buy lots lots of numbers of or they're

**[19:28]** buy lots lots of numbers of or they're in restricted quantities, you need to go

**[19:30]** in restricted quantities, you need to go

**[19:30]** in restricted quantities, you need to go further looking at the IP reputation,

**[19:33]** further looking at the IP reputation,

**[19:33]** further looking at the IP reputation, setting up proof of work, considering

**[19:35]** setting up proof of work, considering

**[19:35]** setting up proof of work, considering these experimental HTTP signatures and

**[19:38]** these experimental HTTP signatures and

**[19:38]** these experimental HTTP signatures and certainly the fingerprint side of things

**[19:40]** certainly the fingerprint side of things

**[19:40]** certainly the fingerprint side of things is where most people land in combination

**[19:42]** is where most people land in combination

**[19:42]** is where most people land in combination with the rate limits.

**[19:44]** with the rate limits.

**[19:44]** with the rate limits. You can implement all these yourselves

**[19:46]** You can implement all these yourselves

**[19:46]** You can implement all these yourselves in code.

**[19:48]** in code.

**[19:48]** in code. That's what we do at ArtJet. There's a

**[19:50]** That's what we do at ArtJet. There's a

**[19:50]** That's what we do at ArtJet. There's a much more detailed writeup of this talk

**[19:52]** much more detailed writeup of this talk

**[19:52]** much more detailed writeup of this talk on uh the blog that I just published

**[19:54]** on uh the blog that I just published

**[19:54]** on uh the blog that I just published earlier today. So, if you have a look at

**[19:55]** earlier today. So, if you have a look at

**[19:55]** earlier today. So, if you have a look at blog.artjet.com,

**[19:57]** blog.artjet.com,

**[19:57]** blog.artjet.com, there's a full write up of this talk

**[19:58]** there's a full write up of this talk

**[19:58]** there's a full write up of this talk with much more detailed examples. I'm


### [20:00 - 21:00]

**[20:01]** with much more detailed examples. I'm

**[20:01]** with much more detailed examples. I'm happy to answer any questions via email

**[20:02]** happy to answer any questions via email

**[20:02]** happy to answer any questions via email and we also have a booth down in the

**[20:04]** and we also have a booth down in the

**[20:04]** and we also have a booth down in the expo. But, thank you very much.


