# Infra that fixes itself, thanks to coding agents — Mahmoud Abdelwahab, Railway

**Video URL:** https://www.youtube.com/watch?v=Q5IVm_CxN2w

---

## Full Transcript

### [00:00 - 01:00]

**[00:01]** your app's infrastructure should fix

**[00:01]** your app's infrastructure should fix itself. Let me show you. So, right now

**[00:03]** itself. Let me show you. So, right now

**[00:03]** itself. Let me show you. So, right now I'm on the Rayway dashboard and I have a

**[00:05]** I'm on the Rayway dashboard and I have a

**[00:05]** I'm on the Rayway dashboard and I have a bunch of services that are deployed and

**[00:07]** bunch of services that are deployed and

**[00:07]** bunch of services that are deployed and all of these services have one thing in

**[00:09]** all of these services have one thing in

**[00:09]** all of these services have one thing in common. They all have bugs and problems.

**[00:11]** common. They all have bugs and problems.

**[00:11]** common. They all have bugs and problems. So, for example, this service has a

**[00:13]** So, for example, this service has a

**[00:13]** So, for example, this service has a memory leak. If I click on it, go to

**[00:15]** memory leak. If I click on it, go to

**[00:16]** memory leak. If I click on it, go to metrics, we can just see memoryization

**[00:19]** metrics, we can just see memoryization

**[00:19]** metrics, we can just see memoryization keeps growing high and very quickly.

**[00:22]** keeps growing high and very quickly.

**[00:22]** keeps growing high and very quickly. This is just a sign of a memory leak and

**[00:24]** This is just a sign of a memory leak and

**[00:24]** This is just a sign of a memory leak and pretty sure the service would eventually

**[00:26]** pretty sure the service would eventually

**[00:26]** pretty sure the service would eventually crash. If I look over at the amount of

**[00:29]** crash. If I look over at the amount of

**[00:29]** crash. If I look over at the amount of requests, we have a high number of 500s.

**[00:32]** requests, we have a high number of 500s.

**[00:32]** requests, we have a high number of 500s. So, the server is failing to respond. We

**[00:35]** So, the server is failing to respond. We

**[00:35]** So, the server is failing to respond. We have a high request error rate of 94%.

**[00:39]** have a high request error rate of 94%.

**[00:39]** have a high request error rate of 94%. And we also have an extremely high

**[00:41]** And we also have an extremely high

**[00:41]** And we also have an extremely high response time of like multiple seconds

**[00:44]** response time of like multiple seconds

**[00:44]** response time of like multiple seconds uh for like the service to respond,

**[00:45]** uh for like the service to respond,

**[00:45]** uh for like the service to respond, which is not ideal. Like if this was a

**[00:48]** which is not ideal. Like if this was a

**[00:48]** which is not ideal. Like if this was a service running in production,

**[00:49]** service running in production,

**[00:50]** service running in production, everything would be on fire. You'd be

**[00:51]** everything would be on fire. You'd be

**[00:51]** everything would be on fire. You'd be getting paged and you just try to bring

**[00:54]** getting paged and you just try to bring

**[00:54]** getting paged and you just try to bring back the service up back quickly. But

**[00:57]** back the service up back quickly. But

**[00:57]** back the service up back quickly. But the thing is not all problems are this


### [01:00 - 02:00]

**[01:00]** the thing is not all problems are this

**[01:00]** the thing is not all problems are this obvious. For example, this service all

**[01:03]** obvious. For example, this service all

**[01:03]** obvious. For example, this service all it does just queries a postcrist

**[01:04]** it does just queries a postcrist

**[01:04]** it does just queries a postcrist database. And if we go to metrics, we'll

**[01:07]** database. And if we go to metrics, we'll

**[01:07]** database. And if we go to metrics, we'll just see that well CPU utilization seems

**[01:10]** just see that well CPU utilization seems

**[01:10]** just see that well CPU utilization seems fine. Memory usage is also fine. Sure,

**[01:13]** fine. Memory usage is also fine. Sure,

**[01:13]** fine. Memory usage is also fine. Sure, it's a bit spiky, but okay, whatever. We

**[01:16]** it's a bit spiky, but okay, whatever. We

**[01:16]** it's a bit spiky, but okay, whatever. We have some fails, but okay, nothing too

**[01:20]** have some fails, but okay, nothing too

**[01:20]** have some fails, but okay, nothing too alarming. request error rate is somewhat

**[01:23]** alarming. request error rate is somewhat

**[01:23]** alarming. request error rate is somewhat high. So that also should make us kind

**[01:26]** high. So that also should make us kind

**[01:26]** high. So that also should make us kind of like want to investigate, but the

**[01:28]** of like want to investigate, but the

**[01:28]** of like want to investigate, but the response time is extremely high. The

**[01:31]** response time is extremely high. The

**[01:31]** response time is extremely high. The thing is this is because the service

**[01:33]** thing is this is because the service

**[01:33]** thing is this is because the service makes queries that are super slow. And

**[01:36]** makes queries that are super slow. And

**[01:36]** makes queries that are super slow. And the thing is if you're an end user

**[01:38]** the thing is if you're an end user

**[01:38]** the thing is if you're an end user that's trying to use this experience,

**[01:40]** that's trying to use this experience,

**[01:40]** that's trying to use this experience, you would just suffer. You would need

**[01:41]** you would just suffer. You would need

**[01:41]** you would just suffer. You would need like 30 seconds for like a page to load,

**[01:44]** like 30 seconds for like a page to load,

**[01:44]** like 30 seconds for like a page to load, which would be a nightmare. So the thing

**[01:47]** which would be a nightmare. So the thing

**[01:47]** which would be a nightmare. So the thing is when you deploy your app to

**[01:49]** is when you deploy your app to

**[01:49]** is when you deploy your app to production maybe some you know bugs or

**[01:52]** production maybe some you know bugs or

**[01:52]** production maybe some you know bugs or issues make their way to production

**[01:54]** issues make their way to production

**[01:54]** issues make their way to production things happen and kind of like the

**[01:57]** things happen and kind of like the

**[01:57]** things happen and kind of like the typical way of dealing with these things

**[01:58]** typical way of dealing with these things

**[01:58]** typical way of dealing with these things is maybe you set up a bunch of


### [02:00 - 03:00]

**[02:00]** is maybe you set up a bunch of

**[02:00]** is maybe you set up a bunch of thresholds and when these thresholds are

**[02:03]** thresholds and when these thresholds are

**[02:03]** thresholds and when these thresholds are met for let's say CPU or memoryization

**[02:07]** met for let's say CPU or memoryization

**[02:07]** met for let's say CPU or memoryization maybe uh you want to have a threshold

**[02:10]** maybe uh you want to have a threshold

**[02:10]** maybe uh you want to have a threshold for the request error rate it shouldn't

**[02:13]** for the request error rate it shouldn't

**[02:13]** for the request error rate it shouldn't exceed a certain amount well what will

**[02:15]** exceed a certain amount well what will

**[02:15]** exceed a certain amount well what will happen is You're going to get alerted

**[02:17]** happen is You're going to get alerted

**[02:17]** happen is You're going to get alerted and you'll be aware that there is an

**[02:18]** and you'll be aware that there is an

**[02:18]** and you'll be aware that there is an issue, but you still have to do the

**[02:20]** issue, but you still have to do the

**[02:20]** issue, but you still have to do the investigation yourself. You have to dig

**[02:22]** investigation yourself. You have to dig

**[02:22]** investigation yourself. You have to dig through logs, metrics, and traces to try

**[02:25]** through logs, metrics, and traces to try

**[02:25]** through logs, metrics, and traces to try to paint a picture in your head and try

**[02:27]** to paint a picture in your head and try

**[02:27]** to paint a picture in your head and try to piece things together so that you can

**[02:29]** to piece things together so that you can

**[02:29]** to piece things together so that you can ship a fix. Now, what I'm proposing is

**[02:33]** ship a fix. Now, what I'm proposing is

**[02:33]** ship a fix. Now, what I'm proposing is you should have a coding agent that

**[02:34]** you should have a coding agent that

**[02:34]** you should have a coding agent that monitors the state of your project and

**[02:38]** monitors the state of your project and

**[02:38]** monitors the state of your project and your application's infrastructure. And

**[02:40]** your application's infrastructure. And

**[02:40]** your application's infrastructure. And if any issue is detected, so you know

**[02:43]** if any issue is detected, so you know

**[02:43]** if any issue is detected, so you know any of the thresholds we define are met,

**[02:45]** any of the thresholds we define are met,

**[02:46]** any of the thresholds we define are met, we should just have a fix shipped,

**[02:48]** we should just have a fix shipped,

**[02:48]** we should just have a fix shipped, right? So like instead of, you know,

**[02:51]** right? So like instead of, you know,

**[02:51]** right? So like instead of, you know, getting the alert and investigating, you

**[02:53]** getting the alert and investigating, you

**[02:53]** getting the alert and investigating, you just review a pull request and you're

**[02:55]** just review a pull request and you're

**[02:55]** just review a pull request and you're like, uh, looks good to me. You ship it

**[02:58]** like, uh, looks good to me. You ship it

**[02:58]** like, uh, looks good to me. You ship it and then everything is good and crisis


### [03:00 - 04:00]

**[03:00]** and then everything is good and crisis

**[03:00]** and then everything is good and crisis averted. So today I'm going to show you

**[03:02]** averted. So today I'm going to show you

**[03:02]** averted. So today I'm going to show you what I have in terms of demo that kind

**[03:06]** what I have in terms of demo that kind

**[03:06]** what I have in terms of demo that kind of paints a picture of how this could be

**[03:09]** of paints a picture of how this could be

**[03:09]** of paints a picture of how this could be achieved. So at a high level I want to

**[03:11]** achieved. So at a high level I want to

**[03:11]** achieved. So at a high level I want to have a series of workflows that will

**[03:13]** have a series of workflows that will

**[03:13]** have a series of workflows that will kick in that will help me go from issue

**[03:16]** kick in that will help me go from issue

**[03:16]** kick in that will help me go from issue detected in on railway my deployment

**[03:18]** detected in on railway my deployment

**[03:18]** detected in on railway my deployment provider to a pull request being open in

**[03:21]** provider to a pull request being open in

**[03:22]** provider to a pull request being open in my GitHub repo. And this is what I have

**[03:24]** my GitHub repo. And this is what I have

**[03:24]** my GitHub repo. And this is what I have in mind. Uh the first workflow that I

**[03:26]** in mind. Uh the first workflow that I

**[03:26]** in mind. Uh the first workflow that I want to have is a workflow that runs on

**[03:28]** want to have is a workflow that runs on

**[03:28]** want to have is a workflow that runs on a schedule. So let's say it runs every

**[03:30]** a schedule. So let's say it runs every

**[03:30]** a schedule. So let's say it runs every 10 minutes, 15 minutes, 30 minutes. And

**[03:32]** 10 minutes, 15 minutes, 30 minutes. And

**[03:32]** 10 minutes, 15 minutes, 30 minutes. And what this workflow will do is one, it

**[03:35]** what this workflow will do is one, it

**[03:35]** what this workflow will do is one, it should fetch the application's

**[03:37]** should fetch the application's

**[03:37]** should fetch the application's architecture. We should have an

**[03:39]** architecture. We should have an

**[03:39]** architecture. We should have an understanding of what services are

**[03:41]** understanding of what services are

**[03:41]** understanding of what services are deployed, which you know like frontends,

**[03:43]** deployed, which you know like frontends,

**[03:43]** deployed, which you know like frontends, backends, crons, cues are live in my

**[03:46]** backends, crons, cues are live in my

**[03:46]** backends, crons, cues are live in my project. And I then want to fetch each

**[03:50]** project. And I then want to fetch each

**[03:50]** project. And I then want to fetch each services resource metrics, so CPU and

**[03:52]** services resource metrics, so CPU and

**[03:52]** services resource metrics, so CPU and memory utilization. And I also want to

**[03:55]** memory utilization. And I also want to

**[03:55]** memory utilization. And I also want to fetch each services HTTP metrics. I want

**[03:57]** fetch each services HTTP metrics. I want

**[03:57]** fetch each services HTTP metrics. I want to see the request error rate, the


### [04:00 - 05:00]

**[04:00]** to see the request error rate, the

**[04:00]** to see the request error rate, the number of failed requests for, you know,

**[04:02]** number of failed requests for, you know,

**[04:02]** number of failed requests for, you know, 500 400 errors. And once that's done, I

**[04:07]** 500 400 errors. And once that's done, I

**[04:07]** 500 400 errors. And once that's done, I will want to then see which services

**[04:10]** will want to then see which services

**[04:10]** will want to then see which services have exceeded which thresholds. And then

**[04:12]** have exceeded which thresholds. And then

**[04:12]** have exceeded which thresholds. And then I just want to return a list of the

**[04:14]** I just want to return a list of the

**[04:14]** I just want to return a list of the affected services. So this would be

**[04:17]** affected services. So this would be

**[04:17]** affected services. So this would be essentially the goal. Now you might be

**[04:19]** essentially the goal. Now you might be

**[04:19]** essentially the goal. Now you might be wondering, well, why not make this an

**[04:21]** wondering, well, why not make this an

**[04:21]** wondering, well, why not make this an alertbased system? So maybe we configure

**[04:23]** alertbased system? So maybe we configure

**[04:24]** alertbased system? So maybe we configure something like web hooks for alerts and

**[04:25]** something like web hooks for alerts and

**[04:26]** something like web hooks for alerts and then that would kick off uh essentially

**[04:28]** then that would kick off uh essentially

**[04:28]** then that would kick off uh essentially this workflow instead. I would argue

**[04:31]** this workflow instead. I would argue

**[04:31]** this workflow instead. I would argue that it's probably better to be able to

**[04:33]** that it's probably better to be able to

**[04:33]** that it's probably better to be able to analyze a slice of time rather than just

**[04:36]** analyze a slice of time rather than just

**[04:36]** analyze a slice of time rather than just having a threshold being met because it

**[04:39]** having a threshold being met because it

**[04:39]** having a threshold being met because it can get pretty noisy. Like imagine you

**[04:41]** can get pretty noisy. Like imagine you

**[04:41]** can get pretty noisy. Like imagine you have a spiky workload uh and you know

**[04:44]** have a spiky workload uh and you know

**[04:44]** have a spiky workload uh and you know you reach the 80% resource utilization

**[04:47]** you reach the 80% resource utilization

**[04:47]** you reach the 80% resource utilization for like your CPU but things are still

**[04:49]** for like your CPU but things are still

**[04:50]** for like your CPU but things are still fine and that's not like in my mind this

**[04:53]** fine and that's not like in my mind this

**[04:53]** fine and that's not like in my mind this is enough to be investigate but it might

**[04:57]** is enough to be investigate but it might

**[04:57]** is enough to be investigate but it might not like it might mean that there just

**[04:59]** not like it might mean that there just

**[04:59]** not like it might mean that there just aren't issues when we try to look at


### [05:00 - 06:00]

**[05:02]** aren't issues when we try to look at

**[05:02]** aren't issues when we try to look at like the bigger picture and all the

**[05:04]** like the bigger picture and all the

**[05:04]** like the bigger picture and all the details.

**[05:06]** details.

**[05:06]** details. Now once we have this list of impact

**[05:09]** Now once we have this list of impact

**[05:09]** Now once we have this list of impact that is impact services we essentially

**[05:11]** that is impact services we essentially

**[05:11]** that is impact services we essentially want to pull in even more context for

**[05:13]** want to pull in even more context for

**[05:13]** want to pull in even more context for them. So like at a high level we want to

**[05:15]** them. So like at a high level we want to

**[05:15]** them. So like at a high level we want to see project health all the services is

**[05:17]** see project health all the services is

**[05:17]** see project health all the services is everything operating as expected. Oh we

**[05:20]** everything operating as expected. Oh we

**[05:20]** everything operating as expected. Oh we have this thing that we're suspicious

**[05:21]** have this thing that we're suspicious

**[05:21]** have this thing that we're suspicious about. Let's actually pull all of you

**[05:24]** about. Let's actually pull all of you

**[05:24]** about. Let's actually pull all of you know additional context for the service

**[05:26]** know additional context for the service

**[05:26]** know additional context for the service because imagine again you have like high

**[05:28]** because imagine again you have like high

**[05:28]** because imagine again you have like high resource utilization. Maybe you're just

**[05:29]** resource utilization. Maybe you're just

**[05:30]** resource utilization. Maybe you're just successful. You have high usage. Uh but

**[05:32]** successful. You have high usage. Uh but

**[05:32]** successful. You have high usage. Uh but then when you pull the logs it's like oh

**[05:33]** then when you pull the logs it's like oh

**[05:33]** then when you pull the logs it's like oh everything seems fine. there aren't any

**[05:36]** everything seems fine. there aren't any

**[05:36]** everything seems fine. there aren't any errors. Well, you're good. And you can

**[05:39]** errors. Well, you're good. And you can

**[05:39]** errors. Well, you're good. And you can imagine that we can even pull even more

**[05:41]** imagine that we can even pull even more

**[05:41]** imagine that we can even pull even more context. Like imagine maybe we scan the

**[05:44]** context. Like imagine maybe we scan the

**[05:44]** context. Like imagine maybe we scan the code in the repo and based on that we

**[05:46]** code in the repo and based on that we

**[05:46]** code in the repo and based on that we infer the upstream providers that the

**[05:49]** infer the upstream providers that the

**[05:49]** infer the upstream providers that the repo relies on and then we can

**[05:51]** repo relies on and then we can

**[05:51]** repo relies on and then we can automatically check the status pages of

**[05:53]** automatically check the status pages of

**[05:53]** automatically check the status pages of these services. Imagine like a payment

**[05:54]** these services. Imagine like a payment

**[05:54]** these services. Imagine like a payment processor goes down. Well, that's kind

**[05:57]** processor goes down. Well, that's kind

**[05:57]** processor goes down. Well, that's kind of how you can know and then the coding


### [06:00 - 07:00]

**[06:00]** of how you can know and then the coding

**[06:00]** of how you can know and then the coding agent will be able to maybe tell you

**[06:02]** agent will be able to maybe tell you

**[06:02]** agent will be able to maybe tell you like, hey, you should just like wait out

**[06:04]** like, hey, you should just like wait out

**[06:04]** like, hey, you should just like wait out this issue.

**[06:05]** this issue.

**[06:06]** this issue. And once we have all this information,

**[06:07]** And once we have all this information,

**[06:07]** And once we have all this information, we can just write a detail plan. So like

**[06:09]** we can just write a detail plan. So like

**[06:09]** we can just write a detail plan. So like we can look at, oh, we have a high

**[06:12]** we can look at, oh, we have a high

**[06:12]** we can look at, oh, we have a high number of 500 requests. We see that we

**[06:16]** number of 500 requests. We see that we

**[06:16]** number of 500 requests. We see that we have very high resource utilization for

**[06:19]** have very high resource utilization for

**[06:19]** have very high resource utilization for memory. and we see that we have you know

**[06:23]** memory. and we see that we have you know

**[06:23]** memory. and we see that we have you know um just errors specifying that a

**[06:26]** um just errors specifying that a

**[06:26]** um just errors specifying that a specific endpoint is failing. Well, this

**[06:29]** specific endpoint is failing. Well, this

**[06:29]** specific endpoint is failing. Well, this is enough information that we can write

**[06:31]** is enough information that we can write

**[06:31]** is enough information that we can write a detailed plan of hey this is my

**[06:33]** a detailed plan of hey this is my

**[06:33]** a detailed plan of hey this is my application's architecture. These are

**[06:35]** application's architecture. These are

**[06:35]** application's architecture. These are the affected services. We just then give

**[06:37]** the affected services. We just then give

**[06:37]** the affected services. We just then give this plan to an agent and then the agent

**[06:40]** this plan to an agent and then the agent

**[06:40]** this plan to an agent and then the agent will just follow the process of hey let

**[06:42]** will just follow the process of hey let

**[06:42]** will just follow the process of hey let me clone this repo. I'll just create a

**[06:44]** me clone this repo. I'll just create a

**[06:44]** me clone this repo. I'll just create a to-do list based on the plan you gave

**[06:45]** to-do list based on the plan you gave

**[06:45]** to-do list based on the plan you gave me. I'll implement all the fixes and

**[06:48]** me. I'll implement all the fixes and

**[06:48]** me. I'll implement all the fixes and I'll just create a pull request. And

**[06:50]** I'll just create a pull request. And

**[06:50]** I'll just create a pull request. And this is kind of how we go from issue

**[06:52]** this is kind of how we go from issue

**[06:52]** this is kind of how we go from issue detected to an open pull request. So

**[06:55]** detected to an open pull request. So

**[06:55]** detected to an open pull request. So let's actually see this in practice. So

**[06:57]** let's actually see this in practice. So

**[06:57]** let's actually see this in practice. So because we have the idea of workflows,


### [07:00 - 08:00]

**[07:00]** because we have the idea of workflows,

**[07:00]** because we have the idea of workflows, what I want to do is actually use what

**[07:02]** what I want to do is actually use what

**[07:02]** what I want to do is actually use what is known as durable execution. So the

**[07:05]** is known as durable execution. So the

**[07:05]** is known as durable execution. So the idea of durable workflows has been

**[07:06]** idea of durable workflows has been

**[07:06]** idea of durable workflows has been around for a while and it's really one

**[07:09]** around for a while and it's really one

**[07:09]** around for a while and it's really one of my favorite abstractions because it

**[07:11]** of my favorite abstractions because it

**[07:11]** of my favorite abstractions because it can help you simplify complex logic

**[07:13]** can help you simplify complex logic

**[07:13]** can help you simplify complex logic while making it more reliable. So for

**[07:16]** while making it more reliable. So for

**[07:16]** while making it more reliable. So for example here we have this workflow. So

**[07:19]** example here we have this workflow. So

**[07:19]** example here we have this workflow. So this actually is ingest but there are

**[07:21]** this actually is ingest but there are

**[07:21]** this actually is ingest but there are lots of solutions out there that pretty

**[07:22]** lots of solutions out there that pretty

**[07:22]** lots of solutions out there that pretty much do the same thing and we have this

**[07:25]** much do the same thing and we have this

**[07:25]** much do the same thing and we have this function that you know called process

**[07:27]** function that you know called process

**[07:27]** function that you know called process video upload. It listens on an event of

**[07:30]** video upload. It listens on an event of

**[07:30]** video upload. It listens on an event of video uploaded and we essentially want

**[07:33]** video uploaded and we essentially want

**[07:33]** video uploaded and we essentially want to do three things. We first want to

**[07:35]** to do three things. We first want to

**[07:35]** to do three things. We first want to generate a transcript and we do this by

**[07:37]** generate a transcript and we do this by

**[07:37]** generate a transcript and we do this by making an API call to a third party API.

**[07:40]** making an API call to a third party API.

**[07:40]** making an API call to a third party API. Once we get that transcript, we want to

**[07:42]** Once we get that transcript, we want to

**[07:42]** Once we get that transcript, we want to generate a summary by also making a

**[07:45]** generate a summary by also making a

**[07:45]** generate a summary by also making a request to an LLM provider. And once we

**[07:47]** request to an LLM provider. And once we

**[07:47]** request to an LLM provider. And once we have the transcript and the summary, we

**[07:48]** have the transcript and the summary, we

**[07:48]** have the transcript and the summary, we want to store them in the database. The

**[07:50]** want to store them in the database. The

**[07:50]** want to store them in the database. The thing is all of these steps, they are

**[07:55]** thing is all of these steps, they are

**[07:55]** thing is all of these steps, they are not 100% guaranteed to work. Uh they are

**[07:58]** not 100% guaranteed to work. Uh they are

**[07:58]** not 100% guaranteed to work. Uh they are prone to failure. And what's neat about


### [08:00 - 09:00]

**[08:00]** prone to failure. And what's neat about

**[08:00]** prone to failure. And what's neat about this pattern is by default, these steps

**[08:03]** this pattern is by default, these steps

**[08:03]** this pattern is by default, these steps will be automatically retried. You don't

**[08:05]** will be automatically retried. You don't

**[08:05]** will be automatically retried. You don't even have to think about it. But if you

**[08:07]** even have to think about it. But if you

**[08:07]** even have to think about it. But if you let's say want to modify this behavior,

**[08:09]** let's say want to modify this behavior,

**[08:09]** let's say want to modify this behavior, maybe you want the retry to happen uh

**[08:12]** maybe you want the retry to happen uh

**[08:12]** maybe you want the retry to happen uh like on a certain schedule like you know

**[08:14]** like on a certain schedule like you know

**[08:14]** like on a certain schedule like you know exponential back off uh maybe you want

**[08:16]** exponential back off uh maybe you want

**[08:16]** exponential back off uh maybe you want to define another thing that should

**[08:20]** to define another thing that should

**[08:20]** to define another thing that should happen in the case of failure you'll be

**[08:22]** happen in the case of failure you'll be

**[08:22]** happen in the case of failure you'll be able to do it. But what's neat is each

**[08:25]** able to do it. But what's neat is each

**[08:25]** able to do it. But what's neat is each step when it succeeds uh the result is

**[08:28]** step when it succeeds uh the result is

**[08:28]** step when it succeeds uh the result is cached. So if for example we are able to

**[08:31]** cached. So if for example we are able to

**[08:31]** cached. So if for example we are able to transcribe the video correctly, we

**[08:32]** transcribe the video correctly, we

**[08:32]** transcribe the video correctly, we summarize the transcript correctly, but

**[08:34]** summarize the transcript correctly, but

**[08:34]** summarize the transcript correctly, but we failed to write to the database. If

**[08:36]** we failed to write to the database. If

**[08:36]** we failed to write to the database. If we were to retry this workflow, we just

**[08:39]** we were to retry this workflow, we just

**[08:39]** we were to retry this workflow, we just continue where we left off. Uh we don't

**[08:41]** continue where we left off. Uh we don't

**[08:41]** continue where we left off. Uh we don't we won't really repeat any work, which

**[08:43]** we won't really repeat any work, which

**[08:43]** we won't really repeat any work, which is one awesome because it's faster, but

**[08:45]** is one awesome because it's faster, but

**[08:45]** is one awesome because it's faster, but also it's more cost effective. So at a

**[08:47]** also it's more cost effective. So at a

**[08:47]** also it's more cost effective. So at a high level, this is the thing that I'll

**[08:49]** high level, this is the thing that I'll

**[08:49]** high level, this is the thing that I'll be relying on in my code because I'll be

**[08:51]** be relying on in my code because I'll be

**[08:51]** be relying on in my code because I'll be making API calls to the railway API to

**[08:54]** making API calls to the railway API to

**[08:54]** making API calls to the railway API to be able to fetch the project

**[08:55]** be able to fetch the project

**[08:55]** be able to fetch the project architecture, all the resource metrics

**[08:58]** architecture, all the resource metrics

**[08:58]** architecture, all the resource metrics um as well as you know the HTTP metrics


### [09:00 - 10:00]

**[09:00]** um as well as you know the HTTP metrics

**[09:00]** um as well as you know the HTTP metrics and whatnot. So yeah, uh this is kind of

**[09:04]** and whatnot. So yeah, uh this is kind of

**[09:04]** and whatnot. So yeah, uh this is kind of like the first thing that um we need to

**[09:07]** like the first thing that um we need to

**[09:07]** like the first thing that um we need to talk about. The second thing is the

**[09:09]** talk about. The second thing is the

**[09:09]** talk about. The second thing is the coding agent. And for the coding agent,

**[09:12]** coding agent. And for the coding agent,

**[09:12]** coding agent. And for the coding agent, I'll be using Open Code. Open code is an

**[09:15]** I'll be using Open Code. Open code is an

**[09:15]** I'll be using Open Code. Open code is an AI agent that's built for the terminal.

**[09:16]** AI agent that's built for the terminal.

**[09:16]** AI agent that's built for the terminal. You can think of it as an alternative to

**[09:18]** You can think of it as an alternative to

**[09:18]** You can think of it as an alternative to something like cloud code, but the main

**[09:20]** something like cloud code, but the main

**[09:20]** something like cloud code, but the main difference is open code is fully open

**[09:22]** difference is open code is fully open

**[09:22]** difference is open code is fully open source and you can choose any LLM

**[09:25]** source and you can choose any LLM

**[09:25]** source and you can choose any LLM provider or uh you know model that you

**[09:28]** provider or uh you know model that you

**[09:28]** provider or uh you know model that you like, which is pretty nice. Uh you have

**[09:30]** like, which is pretty nice. Uh you have

**[09:30]** like, which is pretty nice. Uh you have this nice terminal UI, but honestly

**[09:33]** this nice terminal UI, but honestly

**[09:33]** this nice terminal UI, but honestly what's so cool about the project is how

**[09:35]** what's so cool about the project is how

**[09:35]** what's so cool about the project is how it's architected. So if you go to their

**[09:37]** it's architected. So if you go to their

**[09:37]** it's architected. So if you go to their docs, they actually have a server

**[09:40]** docs, they actually have a server

**[09:40]** docs, they actually have a server implementation. you can have a a a

**[09:44]** implementation. you can have a a a

**[09:44]** implementation. you can have a a a headless server that runs that exposes

**[09:47]** headless server that runs that exposes

**[09:47]** headless server that runs that exposes an API for you to essentially interact

**[09:49]** an API for you to essentially interact

**[09:49]** an API for you to essentially interact with an agent. So the way it works is

**[09:52]** with an agent. So the way it works is

**[09:52]** with an agent. So the way it works is when you run the command open code,

**[09:54]** when you run the command open code,

**[09:54]** when you run the command open code, which is what starts up the agent in

**[09:56]** which is what starts up the agent in

**[09:56]** which is what starts up the agent in your terminal, it doesn't just run a

**[09:58]** your terminal, it doesn't just run a

**[09:58]** your terminal, it doesn't just run a single app. It actually starts a

**[09:59]** single app. It actually starts a

**[09:59]** single app. It actually starts a terminal UI and a server. And because


### [10:00 - 11:00]

**[10:02]** terminal UI and a server. And because

**[10:02]** terminal UI and a server. And because the terminal UI here is the client, we

**[10:05]** the terminal UI here is the client, we

**[10:05]** the terminal UI here is the client, we can essentially bring our own client and

**[10:07]** can essentially bring our own client and

**[10:07]** can essentially bring our own client and talk to the server, which is awesome. uh

**[10:09]** talk to the server, which is awesome. uh

**[10:09]** talk to the server, which is awesome. uh because now we can run open code on a

**[10:12]** because now we can run open code on a

**[10:12]** because now we can run open code on a server in this case would be on railway

**[10:15]** server in this case would be on railway

**[10:15]** server in this case would be on railway and we can just have this server have

**[10:18]** and we can just have this server have

**[10:18]** and we can just have this server have all the tools that the agent would need.

**[10:19]** all the tools that the agent would need.

**[10:20]** all the tools that the agent would need. So we'd install all of the necessary you

**[10:22]** So we'd install all of the necessary you

**[10:22]** So we'd install all of the necessary you know tools we can configure git and then

**[10:25]** know tools we can configure git and then

**[10:25]** know tools we can configure git and then the agent will be able to open pull

**[10:27]** the agent will be able to open pull

**[10:27]** the agent will be able to open pull requests and you know go through the

**[10:30]** requests and you know go through the

**[10:30]** requests and you know go through the file system and do everything. Let me

**[10:32]** file system and do everything. Let me

**[10:32]** file system and do everything. Let me show you what how easy it is to

**[10:34]** show you what how easy it is to

**[10:34]** show you what how easy it is to essentially have this deployed on right

**[10:35]** essentially have this deployed on right

**[10:35]** essentially have this deployed on right away. So if you go to the code uh here

**[10:38]** away. So if you go to the code uh here

**[10:38]** away. So if you go to the code uh here right now this is my project it's called

**[10:40]** right now this is my project it's called

**[10:40]** right now this is my project it's called railway autofix I know great name uh I

**[10:43]** railway autofix I know great name uh I

**[10:43]** railway autofix I know great name uh I have essentially two directories one is

**[10:45]** have essentially two directories one is

**[10:45]** have essentially two directories one is for my API the other one is for open

**[10:48]** for my API the other one is for open

**[10:48]** for my API the other one is for open code and open code really we just have a

**[10:51]** code and open code really we just have a

**[10:51]** code and open code really we just have a single server running using bun and all

**[10:54]** single server running using bun and all

**[10:54]** single server running using bun and all we're doing is we're just calling a

**[10:57]** we're doing is we're just calling a

**[10:57]** we're doing is we're just calling a function uh that is called create open


### [11:00 - 12:00]

**[11:00]** function uh that is called create open

**[11:00]** function uh that is called create open code server so if I actually stop this

**[11:02]** code server so if I actually stop this

**[11:02]** code server so if I actually stop this here you can see it runs on port 4000 9

**[11:06]** here you can see it runs on port 4000 9

**[11:06]** here you can see it runs on port 4000 9 496 and this is pretty much all we need

**[11:11]** 496 and this is pretty much all we need

**[11:11]** 496 and this is pretty much all we need and I have a docker file and in this

**[11:13]** and I have a docker file and in this

**[11:13]** and I have a docker file and in this docker file we're essentially defining

**[11:15]** docker file we're essentially defining

**[11:15]** docker file we're essentially defining that environment. So, we're installing a

**[11:17]** that environment. So, we're installing a

**[11:17]** that environment. So, we're installing a bunch of tools. You can see we're

**[11:18]** bunch of tools. You can see we're

**[11:18]** bunch of tools. You can see we're installing curl, jq, bash, all the other

**[11:20]** installing curl, jq, bash, all the other

**[11:20]** installing curl, jq, bash, all the other tools, even git. Uh, we're installing

**[11:22]** tools, even git. Uh, we're installing

**[11:22]** tools, even git. Uh, we're installing the GitHub CLI, which is what will allow

**[11:25]** the GitHub CLI, which is what will allow

**[11:25]** the GitHub CLI, which is what will allow us to open pull requests against a given

**[11:27]** us to open pull requests against a given

**[11:27]** us to open pull requests against a given repo. We're then installing open code in

**[11:30]** repo. We're then installing open code in

**[11:30]** repo. We're then installing open code in the environment. We're configuring git

**[11:32]** the environment. We're configuring git

**[11:32]** the environment. We're configuring git and at the end, we're just exposing the

**[11:35]** and at the end, we're just exposing the

**[11:35]** and at the end, we're just exposing the port and we're just authenticating the

**[11:37]** port and we're just authenticating the

**[11:37]** port and we're just authenticating the GitHub CLI, which is pretty neat. Uh, by

**[11:39]** GitHub CLI, which is pretty neat. Uh, by

**[11:39]** GitHub CLI, which is pretty neat. Uh, by the way, the code will be linked

**[11:41]** the way, the code will be linked

**[11:41]** the way, the code will be linked somewhere down below. But that's really

**[11:43]** somewhere down below. But that's really

**[11:43]** somewhere down below. But that's really it for open code. And when it comes to

**[11:46]** it for open code. And when it comes to

**[11:46]** it for open code. And when it comes to the actual API, let me actually run it.

**[11:49]** the actual API, let me actually run it.

**[11:49]** the actual API, let me actually run it. So now the this is the open code server

**[11:52]** So now the this is the open code server

**[11:52]** So now the this is the open code server that's running. And if I go here, I have

**[11:55]** that's running. And if I go here, I have

**[11:55]** that's running. And if I go here, I have my actual API running on localhost 3000.

**[11:58]** my actual API running on localhost 3000.

**[11:58]** my actual API running on localhost 3000. And I have a UI that is provided by


### [12:00 - 13:00]

**[12:01]** And I have a UI that is provided by

**[12:01]** And I have a UI that is provided by ingest, which is very useful for

**[12:03]** ingest, which is very useful for

**[12:03]** ingest, which is very useful for debugging. So if I go here and I go to

**[12:07]** debugging. So if I go here and I go to

**[12:07]** debugging. So if I go here and I go to functions, essentially each function

**[12:09]** functions, essentially each function

**[12:09]** functions, essentially each function here is a workflow and it has a bunch of

**[12:12]** here is a workflow and it has a bunch of

**[12:12]** here is a workflow and it has a bunch of steps. So let's actually try to run it

**[12:14]** steps. So let's actually try to run it

**[12:14]** steps. So let's actually try to run it to see what happens. Um now in

**[12:17]** to see what happens. Um now in

**[12:17]** to see what happens. Um now in production when this is live this

**[12:19]** production when this is live this

**[12:20]** production when this is live this monitor project health workflow should

**[12:22]** monitor project health workflow should

**[12:22]** monitor project health workflow should run on a schedule and if an issue is

**[12:25]** run on a schedule and if an issue is

**[12:25]** run on a schedule and if an issue is detected we will call the pool service

**[12:26]** detected we will call the pool service

**[12:26]** detected we will call the pool service context and then pull service context

**[12:30]** context and then pull service context

**[12:30]** context and then pull service context will call the workflow for generating a

**[12:33]** will call the workflow for generating a

**[12:33]** will call the workflow for generating a fix. So if we actually just kick things

**[12:34]** fix. So if we actually just kick things

**[12:34]** fix. So if we actually just kick things off this is how the flow of things will

**[12:38]** off this is how the flow of things will

**[12:38]** off this is how the flow of things will happen. So if I actually have now I have

**[12:40]** happen. So if I actually have now I have

**[12:40]** happen. So if I actually have now I have this function run. We called moderate

**[12:42]** this function run. We called moderate

**[12:42]** this function run. We called moderate project health. Then we called pull

**[12:44]** project health. Then we called pull

**[12:44]** project health. Then we called pull service context and now we're actually

**[12:45]** service context and now we're actually

**[12:45]** service context and now we're actually calling generate fix because we detected

**[12:47]** calling generate fix because we detected

**[12:47]** calling generate fix because we detected an issue and we're just setting um like

**[12:51]** an issue and we're just setting um like

**[12:51]** an issue and we're just setting um like the railway specific variables as

**[12:54]** the railway specific variables as

**[12:54]** the railway specific variables as environment variables. And all of these

**[12:55]** environment variables. And all of these

**[12:55]** environment variables. And all of these are actually available uh on railway.

**[12:58]** are actually available uh on railway.

**[12:58]** are actually available uh on railway. They're just set automatically which is

**[12:59]** They're just set automatically which is

**[12:59]** They're just set automatically which is pretty neat. So if I actually go to


### [13:00 - 14:00]

**[13:01]** pretty neat. So if I actually go to

**[13:01]** pretty neat. So if I actually go to monitor project health you'll see we

**[13:03]** monitor project health you'll see we

**[13:03]** monitor project health you'll see we have a bunch of steps. Uh the first one

**[13:06]** have a bunch of steps. Uh the first one

**[13:06]** have a bunch of steps. Uh the first one is getting the project architecture and

**[13:08]** is getting the project architecture and

**[13:08]** is getting the project architecture and this step right here this is we can

**[13:10]** this step right here this is we can

**[13:10]** this step right here this is we can actually see its output. So we can see

**[13:12]** actually see its output. So we can see

**[13:12]** actually see its output. So we can see all of the databases that I have in my

**[13:14]** all of the databases that I have in my

**[13:14]** all of the databases that I have in my project. I just have one. Uh we can see

**[13:17]** project. I just have one. Uh we can see

**[13:17]** project. I just have one. Uh we can see also a list of all the services as well

**[13:20]** also a list of all the services as well

**[13:20]** also a list of all the services as well as their configuration. We can see which

**[13:23]** as their configuration. We can see which

**[13:23]** as their configuration. We can see which like where's the repo for them and we

**[13:26]** like where's the repo for them and we

**[13:26]** like where's the repo for them and we just now have a highle overview of our

**[13:29]** just now have a highle overview of our

**[13:30]** just now have a highle overview of our applications infrastructure. Uh we also

**[13:32]** applications infrastructure. Uh we also

**[13:32]** applications infrastructure. Uh we also see that we have any kind of like

**[13:33]** see that we have any kind of like

**[13:33]** see that we have any kind of like volumes that are there which is cool.

**[13:36]** volumes that are there which is cool.

**[13:36]** volumes that are there which is cool. And then we have a series of steps that

**[13:38]** And then we have a series of steps that

**[13:38]** And then we have a series of steps that are actually running in parallel. So

**[13:40]** are actually running in parallel. So

**[13:40]** are actually running in parallel. So like you know things are efficient. So

**[13:42]** like you know things are efficient. So

**[13:42]** like you know things are efficient. So we're getting the database resources. We

**[13:44]** we're getting the database resources. We

**[13:44]** we're getting the database resources. We can see on average well what's the max

**[13:46]** can see on average well what's the max

**[13:46]** can see on average well what's the max CPU? Uh and it's like 0.9 CPU. Okay.

**[13:50]** CPU? Uh and it's like 0.9 CPU. Okay.

**[13:50]** CPU? Uh and it's like 0.9 CPU. Okay. Same thing for memory. And we actually

**[13:52]** Same thing for memory. And we actually

**[13:52]** Same thing for memory. And we actually have a summary. And this summary

**[13:54]** have a summary. And this summary

**[13:54]** have a summary. And this summary essentially is us formatting these

**[13:56]** essentially is us formatting these

**[13:56]** essentially is us formatting these results so that we can then pass it to

**[13:58]** results so that we can then pass it to

**[13:58]** results so that we can then pass it to the coding agent. So you can see CPU

**[13:59]** the coding agent. So you can see CPU

**[13:59]** the coding agent. So you can see CPU usage average 0.93 vcpu


### [14:00 - 15:00]

**[14:03]** usage average 0.93 vcpu

**[14:03]** usage average 0.93 vcpu and you know this is the max and memory

**[14:05]** and you know this is the max and memory

**[14:05]** and you know this is the max and memory usage as well. Now this is actually high

**[14:09]** usage as well. Now this is actually high

**[14:09]** usage as well. Now this is actually high uh and we'll be able to kind of

**[14:11]** uh and we'll be able to kind of

**[14:11]** uh and we'll be able to kind of understand that because it's like oh

**[14:13]** understand that because it's like oh

**[14:13]** understand that because it's like oh memory usage here is 31.96 GB out of a

**[14:17]** memory usage here is 31.96 GB out of a

**[14:17]** memory usage here is 31.96 GB out of a max which is 32 gigs. Uh and then we

**[14:19]** max which is 32 gigs. Uh and then we

**[14:19]** max which is 32 gigs. Uh and then we just pull even more um like resources.

**[14:22]** just pull even more um like resources.

**[14:22]** just pull even more um like resources. So like because we have multiple

**[14:24]** So like because we have multiple

**[14:24]** So like because we have multiple services we will call each step for it.

**[14:27]** services we will call each step for it.

**[14:27]** services we will call each step for it. Right? So like we will pull the HTTP

**[14:28]** Right? So like we will pull the HTTP

**[14:28]** Right? So like we will pull the HTTP metrics for each of the three services

**[14:31]** metrics for each of the three services

**[14:31]** metrics for each of the three services that we have deployed for example. But

**[14:33]** that we have deployed for example. But

**[14:33]** that we have deployed for example. But also for this one for the HTTP metrics

**[14:35]** also for this one for the HTTP metrics

**[14:35]** also for this one for the HTTP metrics we can see the error rate percentage for

**[14:37]** we can see the error rate percentage for

**[14:37]** we can see the error rate percentage for 400s for 500s. We see like the latency

**[14:41]** 400s for 500s. We see like the latency

**[14:42]** 400s for 500s. We see like the latency um and we just have like a status count.

**[14:43]** um and we just have like a status count.

**[14:44]** um and we just have like a status count. So we can also have a summary and then

**[14:46]** So we can also have a summary and then

**[14:46]** So we can also have a summary and then we can say hey these this is the rate of

**[14:50]** we can say hey these this is the rate of

**[14:50]** we can say hey these this is the rate of um like request error rates. This these

**[14:52]** um like request error rates. This these

**[14:52]** um like request error rates. This these are the latencies and this way when we

**[14:55]** are the latencies and this way when we

**[14:56]** are the latencies and this way when we actually at the end of like this

**[14:58]** actually at the end of like this

**[14:58]** actually at the end of like this workflow so I go to runs go here again


### [15:00 - 16:00]

**[15:01]** workflow so I go to runs go here again

**[15:01]** workflow so I go to runs go here again towards the end we will actually give

**[15:05]** towards the end we will actually give

**[15:05]** towards the end we will actually give this uh pull service context function

**[15:08]** this uh pull service context function

**[15:08]** this uh pull service context function just all of this information in a nicely

**[15:11]** just all of this information in a nicely

**[15:11]** just all of this information in a nicely formatted way. So if I actually go now

**[15:13]** formatted way. So if I actually go now

**[15:13]** formatted way. So if I actually go now to this function run, we will see here

**[15:16]** to this function run, we will see here

**[15:16]** to this function run, we will see here that we're fetching the HTTP logs, the

**[15:19]** that we're fetching the HTTP logs, the

**[15:19]** that we're fetching the HTTP logs, the build logs, the deployment logs for like

**[15:21]** build logs, the deployment logs for like

**[15:21]** build logs, the deployment logs for like all the services that are affected. And

**[15:23]** all the services that are affected. And

**[15:24]** all the services that are affected. And we can see here like this is the

**[15:25]** we can see here like this is the

**[15:25]** we can see here like this is the function payload. Uh so this is the

**[15:27]** function payload. Uh so this is the

**[15:28]** function payload. Uh so this is the stuff that we passed from the other

**[15:29]** stuff that we passed from the other

**[15:29]** stuff that we passed from the other function. And we can see we just have

**[15:32]** function. And we can see we just have

**[15:32]** function. And we can see we just have all this info. We also have an

**[15:34]** all this info. We also have an

**[15:34]** all this info. We also have an architecture summary. So this actually

**[15:36]** architecture summary. So this actually

**[15:36]** architecture summary. So this actually we can expand this. Uh the architecture

**[15:38]** we can expand this. Uh the architecture

**[15:38]** we can expand this. Uh the architecture summary is just a nicely formatted uh

**[15:41]** summary is just a nicely formatted uh

**[15:41]** summary is just a nicely formatted uh text saying like this is the project

**[15:42]** text saying like this is the project

**[15:42]** text saying like this is the project architecture. We have three services we

**[15:46]** architecture. We have three services we

**[15:46]** architecture. We have three services we are running in the production

**[15:47]** are running in the production

**[15:47]** are running in the production environment. We have one database. We

**[15:49]** environment. We have one database. We

**[15:49]** environment. We have one database. We have all these volumes and we just have

**[15:51]** have all these volumes and we just have

**[15:51]** have all these volumes and we just have all of this information. It's just

**[15:53]** all of this information. It's just

**[15:53]** all of this information. It's just harder to read cuz like in one line but

**[15:55]** harder to read cuz like in one line but

**[15:55]** harder to read cuz like in one line but for the um coding agent we'll just give

**[15:58]** for the um coding agent we'll just give

**[15:58]** for the um coding agent we'll just give it to it as like markdown. So now that


### [16:00 - 17:00]

**[16:01]** it to it as like markdown. So now that

**[16:02]** it to it as like markdown. So now that we have that go to runs again. Now that

**[16:05]** we have that go to runs again. Now that

**[16:05]** we have that go to runs again. Now that we have that, we are just going to make

**[16:07]** we have that, we are just going to make

**[16:07]** we have that, we are just going to make a call to another workflow which is

**[16:09]** a call to another workflow which is

**[16:09]** a call to another workflow which is generate fix. And for this one, what it

**[16:12]** generate fix. And for this one, what it

**[16:12]** generate fix. And for this one, what it does is one, it will analyze with AI. So

**[16:16]** does is one, it will analyze with AI. So

**[16:16]** does is one, it will analyze with AI. So this is the actual output in terms of

**[16:18]** this is the actual output in terms of

**[16:18]** this is the actual output in terms of like the input. It's a bit large to

**[16:21]** like the input. It's a bit large to

**[16:21]** like the input. It's a bit large to render here. Uh but we analyze it with

**[16:23]** render here. Uh but we analyze it with

**[16:23]** render here. Uh but we analyze it with AI. So like you can imagine we give a

**[16:25]** AI. So like you can imagine we give a

**[16:26]** AI. So like you can imagine we give a large language model saying like hey

**[16:28]** large language model saying like hey

**[16:28]** large language model saying like hey this is my project architecture. This is

**[16:30]** this is my project architecture. This is

**[16:30]** this is my project architecture. This is the data. This is how things are

**[16:32]** the data. This is how things are

**[16:32]** the data. This is how things are performing. And then we take all of this

**[16:35]** performing. And then we take all of this

**[16:35]** performing. And then we take all of this information and now we actually come up

**[16:38]** information and now we actually come up

**[16:38]** information and now we actually come up with a plan. So you can see here

**[16:40]** with a plan. So you can see here

**[16:40]** with a plan. So you can see here debugging steps. We want to see

**[16:42]** debugging steps. We want to see

**[16:42]** debugging steps. We want to see reproduce locally with the same load.

**[16:44]** reproduce locally with the same load.

**[16:44]** reproduce locally with the same load. Maybe we want to run it. We want to see

**[16:46]** Maybe we want to run it. We want to see

**[16:46]** Maybe we want to run it. We want to see what will happen if we see that the

**[16:48]** what will happen if we see that the

**[16:48]** what will happen if we see that the agent is like oh I ran into an error.

**[16:50]** agent is like oh I ran into an error.

**[16:50]** agent is like oh I ran into an error. Then it's going to fix it. And then we

**[16:53]** Then it's going to fix it. And then we

**[16:53]** Then it's going to fix it. And then we have like recommendations. So like this

**[16:55]** have like recommendations. So like this

**[16:55]** have like recommendations. So like this is the plan that we'll then just pass to

**[16:57]** is the plan that we'll then just pass to

**[16:57]** is the plan that we'll then just pass to our coding agent. And then we have a

**[16:59]** our coding agent. And then we have a

**[16:59]** our coding agent. And then we have a step to create a session. So on the


### [17:00 - 18:00]

**[17:02]** step to create a session. So on the

**[17:02]** step to create a session. So on the coding agent you can imagine each

**[17:04]** coding agent you can imagine each

**[17:04]** coding agent you can imagine each session being its own chat. So this will

**[17:07]** session being its own chat. So this will

**[17:07]** session being its own chat. So this will run like imagine you have multiple repos

**[17:09]** run like imagine you have multiple repos

**[17:09]** run like imagine you have multiple repos each repo will have its own session. The

**[17:11]** each repo will have its own session. The

**[17:11]** each repo will have its own session. The coding agent will work and then at the

**[17:14]** coding agent will work and then at the

**[17:14]** coding agent will work and then at the end it should you know if as expected it

**[17:17]** end it should you know if as expected it

**[17:17]** end it should you know if as expected it should open a pull request. So yeah

**[17:20]** should open a pull request. So yeah

**[17:20]** should open a pull request. So yeah that's pretty much it. This is how it

**[17:22]** that's pretty much it. This is how it

**[17:22]** that's pretty much it. This is how it works. Now if everything works as

**[17:24]** works. Now if everything works as

**[17:24]** works. Now if everything works as expected we should see a pull request on

**[17:27]** expected we should see a pull request on

**[17:27]** expected we should see a pull request on the project. And here we go. We have a

**[17:30]** the project. And here we go. We have a

**[17:30]** the project. And here we go. We have a pull request that is open with all of

**[17:32]** pull request that is open with all of

**[17:32]** pull request that is open with all of our changes. If we go to the

**[17:34]** our changes. If we go to the

**[17:34]** our changes. If we go to the conversation, we actually be able to see

**[17:36]** conversation, we actually be able to see

**[17:36]** conversation, we actually be able to see that we have a summary of all the

**[17:37]** that we have a summary of all the

**[17:37]** that we have a summary of all the changes, uh, an analysis summary, the

**[17:40]** changes, uh, an analysis summary, the

**[17:40]** changes, uh, an analysis summary, the root causes, what was fixed. So, we

**[17:43]** root causes, what was fixed. So, we

**[17:43]** root causes, what was fixed. So, we should be able to just review this. If

**[17:46]** should be able to just review this. If

**[17:46]** should be able to just review this. If everything looks good, we merge and

**[17:47]** everything looks good, we merge and

**[17:47]** everything looks good, we merge and we're good to go. And that's it. I hope

**[17:49]** we're good to go. And that's it. I hope

**[17:49]** we're good to go. And that's it. I hope you enjoyed this talk as much as I

**[17:51]** you enjoyed this talk as much as I

**[17:51]** you enjoyed this talk as much as I enjoyed making it. If you have any

**[17:52]** enjoyed making it. If you have any

**[17:52]** enjoyed making it. If you have any questions, feel free to reach out to me

**[17:54]** questions, feel free to reach out to me

**[17:54]** questions, feel free to reach out to me on X or Twitter. This is where I mostly

**[17:56]** on X or Twitter. This is where I mostly

**[17:56]** on X or Twitter. This is where I mostly hang out. Also, the repo for this

**[17:59]** hang out. Also, the repo for this

**[17:59]** hang out. Also, the repo for this project will be available somewhere down


### [18:00 - 19:00]

**[18:01]** project will be available somewhere down

**[18:01]** project will be available somewhere down below. So, make sure to check it out.

**[18:03]** below. So, make sure to check it out.

**[18:03]** below. So, make sure to check it out. And with that, thank you so much for

**[18:05]** And with that, thank you so much for

**[18:05]** And with that, thank you so much for watching and I'll see you in the next


