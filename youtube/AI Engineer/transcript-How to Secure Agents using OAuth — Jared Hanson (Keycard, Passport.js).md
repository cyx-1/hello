# How to Secure Agents using OAuth — Jared Hanson (Keycard, Passport.js)

**Video URL:** https://www.youtube.com/watch?v=blmAkayzE8M

---

## Full Transcript

### [00:00 - 01:00]

**[00:16]** Thanks a lot everyone. Thanks for coming

**[00:16]** Thanks a lot everyone. Thanks for coming out. Uh we're going to talk about a

**[00:18]** out. Uh we're going to talk about a

**[00:18]** out. Uh we're going to talk about a topic that I consider one of the most uh

**[00:19]** topic that I consider one of the most uh

**[00:20]** topic that I consider one of the most uh important topics uh for what we're doing

**[00:22]** important topics uh for what we're doing

**[00:22]** important topics uh for what we're doing with AI and agents, which is how to

**[00:23]** with AI and agents, which is how to

**[00:23]** with AI and agents, which is how to secure agents using OOTH. Um I'm Jared

**[00:27]** secure agents using OOTH. Um I'm Jared

**[00:27]** secure agents using OOTH. Um I'm Jared Hansen. I'm the co-founder of a new

**[00:28]** Hansen. I'm the co-founder of a new

**[00:28]** Hansen. I'm the co-founder of a new company called Keycard where we're

**[00:30]** company called Keycard where we're

**[00:30]** company called Keycard where we're building identity and access management

**[00:32]** building identity and access management

**[00:32]** building identity and access management platform for AI and agents. I'm also the

**[00:36]** platform for AI and agents. I'm also the

**[00:36]** platform for AI and agents. I'm also the creator of Passport.js for any of the

**[00:37]** creator of Passport.js for any of the

**[00:38]** creator of Passport.js for any of the node uh developers in the audience very

**[00:39]** node uh developers in the audience very

**[00:40]** node uh developers in the audience very popular o framework and previously I was

**[00:42]** popular o framework and previously I was

**[00:42]** popular o framework and previously I was at Ozero where I built a lot of their

**[00:44]** at Ozero where I built a lot of their

**[00:44]** at Ozero where I built a lot of their core identity infrastructure and then

**[00:45]** core identity infrastructure and then

**[00:46]** core identity infrastructure and then and then at octa

**[00:48]** and then at octa

**[00:48]** and then at octa uh let's get into it. So I think we're

**[00:50]** uh let's get into it. So I think we're

**[00:50]** uh let's get into it. So I think we're all super excited about what's happening

**[00:52]** all super excited about what's happening

**[00:52]** all super excited about what's happening with LLMs and AI powered applications.

**[00:55]** with LLMs and AI powered applications.

**[00:55]** with LLMs and AI powered applications. uh you know we can bring these things

**[00:56]** uh you know we can bring these things

**[00:56]** uh you know we can bring these things into our daily lives and they automate a

**[00:59]** into our daily lives and they automate a

**[00:59]** into our daily lives and they automate a lot of the tasks for us and and simply


### [01:00 - 02:00]

**[01:00]** lot of the tasks for us and and simply

**[01:00]** lot of the tasks for us and and simply put agents that are more connected are

**[01:02]** put agents that are more connected are

**[01:02]** put agents that are more connected are more useful. Uh so let's connect these

**[01:05]** more useful. Uh so let's connect these

**[01:05]** more useful. Uh so let's connect these agents to more systems. But but hold on

**[01:07]** agents to more systems. But but hold on

**[01:07]** agents to more systems. But but hold on a second because today we face an

**[01:09]** a second because today we face an

**[01:09]** a second because today we face an impossible choice. Uh we can give agents

**[01:11]** impossible choice. Uh we can give agents

**[01:12]** impossible choice. Uh we can give agents broad-based access and accept security

**[01:13]** broad-based access and accept security

**[01:13]** broad-based access and accept security risks or we can limit their capabilities

**[01:16]** risks or we can limit their capabilities

**[01:16]** risks or we can limit their capabilities and sacrifice business value. Uh, and

**[01:19]** and sacrifice business value. Uh, and

**[01:19]** and sacrifice business value. Uh, and this is exemplified pretty well in how

**[01:21]** this is exemplified pretty well in how

**[01:21]** this is exemplified pretty well in how we set up uh, MCP servers today, which

**[01:23]** we set up uh, MCP servers today, which

**[01:23]** we set up uh, MCP servers today, which is we go get API keys that are typically

**[01:26]** is we go get API keys that are typically

**[01:26]** is we go get API keys that are typically longived and broadly scoped. We paste

**[01:28]** longived and broadly scoped. We paste

**[01:28]** longived and broadly scoped. We paste them into some configuration files and

**[01:30]** them into some configuration files and

**[01:30]** them into some configuration files and environment variables and and let our

**[01:32]** environment variables and and let our

**[01:32]** environment variables and and let our agents run with them. Now, if we

**[01:34]** agents run with them. Now, if we

**[01:34]** agents run with them. Now, if we continue this pattern for hundreds or

**[01:35]** continue this pattern for hundreds or

**[01:35]** continue this pattern for hundreds or thousands of agents, we've got a pretty

**[01:37]** thousands of agents, we've got a pretty

**[01:37]** thousands of agents, we've got a pretty big security problem on our hand. Uh,

**[01:39]** big security problem on our hand. Uh,

**[01:39]** big security problem on our hand. Uh, luckily, we we know how to fix this. We

**[01:41]** luckily, we we know how to fix this. We

**[01:41]** luckily, we we know how to fix this. We know how to transition away from static

**[01:43]** know how to transition away from static

**[01:43]** know how to transition away from static secrets uh, to dynamic access using

**[01:46]** secrets uh, to dynamic access using

**[01:46]** secrets uh, to dynamic access using OOTH. Now, show of hands, how many

**[01:48]** OOTH. Now, show of hands, how many

**[01:48]** OOTH. Now, show of hands, how many people are familiar with OOTH in the

**[01:50]** people are familiar with OOTH in the

**[01:50]** people are familiar with OOTH in the crowd? I'll say quite quite a bit. So,

**[01:53]** crowd? I'll say quite quite a bit. So,

**[01:53]** crowd? I'll say quite quite a bit. So, I'll I'll burn through this quickly. Uh,

**[01:55]** I'll I'll burn through this quickly. Uh,

**[01:55]** I'll I'll burn through this quickly. Uh, but just uh as a quick introduction, um

**[01:58]** but just uh as a quick introduction, um

**[01:58]** but just uh as a quick introduction, um I'm not going to lie to anyone like OOTH


### [02:00 - 03:00]

**[02:00]** I'm not going to lie to anyone like OOTH

**[02:00]** I'm not going to lie to anyone like OOTH is a relatively complicated protocol,

**[02:02]** is a relatively complicated protocol,

**[02:02]** is a relatively complicated protocol, especially when you consider all the

**[02:03]** especially when you consider all the

**[02:03]** especially when you consider all the extensions. But the princip principles

**[02:06]** extensions. But the princip principles

**[02:06]** extensions. But the princip principles behind it are fairly straightforward and

**[02:07]** behind it are fairly straightforward and

**[02:07]** behind it are fairly straightforward and easy easy to understand. Uh what it is

**[02:10]** easy easy to understand. Uh what it is

**[02:10]** easy easy to understand. Uh what it is is a protocol for applications which we

**[02:13]** is a protocol for applications which we

**[02:13]** is a protocol for applications which we call clients in OOTH to request access

**[02:15]** call clients in OOTH to request access

**[02:15]** call clients in OOTH to request access to APIs which we call resource servers

**[02:18]** to APIs which we call resource servers

**[02:18]** to APIs which we call resource servers and and these requests are mediated by

**[02:20]** and and these requests are mediated by

**[02:20]** and and these requests are mediated by what's known as an authorization server.

**[02:23]** what's known as an authorization server.

**[02:23]** what's known as an authorization server. If you've ever used anything like

**[02:24]** If you've ever used anything like

**[02:24]** If you've ever used anything like Calendarly and connected it to your

**[02:26]** Calendarly and connected it to your

**[02:26]** Calendarly and connected it to your Google calendar API, you've experienced

**[02:29]** Google calendar API, you've experienced

**[02:29]** Google calendar API, you've experienced OOTH in the real world. Uh what's

**[02:31]** OOTH in the real world. Uh what's

**[02:31]** OOTH in the real world. Uh what's happening there is Calendarly sends a

**[02:33]** happening there is Calendarly sends a

**[02:33]** happening there is Calendarly sends a request over to Google saying, "Hey, I'd

**[02:35]** request over to Google saying, "Hey, I'd

**[02:35]** request over to Google saying, "Hey, I'd like access to this person's Google

**[02:37]** like access to this person's Google

**[02:37]** like access to this person's Google calendar." uh Google C- Google's

**[02:39]** calendar." uh Google C- Google's

**[02:40]** calendar." uh Google C- Google's authorization server then you know

**[02:41]** authorization server then you know

**[02:41]** authorization server then you know ensures that you're logged in prompts

**[02:43]** ensures that you're logged in prompts

**[02:43]** ensures that you're logged in prompts you for consent uh that you want this

**[02:45]** you for consent uh that you want this

**[02:45]** you for consent uh that you want this access to occur and if you agree to it

**[02:47]** access to occur and if you agree to it

**[02:47]** access to occur and if you agree to it uh Google sends what's known as an

**[02:49]** uh Google sends what's known as an

**[02:49]** uh Google sends what's known as an access token over to Calendarly and then

**[02:52]** access token over to Calendarly and then

**[02:52]** access token over to Calendarly and then Kalanley can take that access token and

**[02:53]** Kalanley can take that access token and

**[02:54]** Kalanley can take that access token and go about accessing your calendar. Uh

**[02:56]** go about accessing your calendar. Uh

**[02:56]** go about accessing your calendar. Uh there's a few other interesting bits

**[02:57]** there's a few other interesting bits

**[02:57]** there's a few other interesting bits going on here like refresh tokens which


### [03:00 - 04:00]

**[03:00]** going on here like refresh tokens which

**[03:00]** going on here like refresh tokens which basically allows these access tokens to

**[03:01]** basically allows these access tokens to

**[03:01]** basically allows these access tokens to be shortlived and rotated pretty quickly

**[03:03]** be shortlived and rotated pretty quickly

**[03:03]** be shortlived and rotated pretty quickly while still maintaining the the

**[03:05]** while still maintaining the the

**[03:05]** while still maintaining the the authorized connection. Uh and in OOTH we

**[03:08]** authorized connection. Uh and in OOTH we

**[03:08]** authorized connection. Uh and in OOTH we call these types of flows that involve

**[03:10]** call these types of flows that involve

**[03:10]** call these types of flows that involve user delegation uh authorization code

**[03:12]** user delegation uh authorization code

**[03:12]** user delegation uh authorization code flows and they typically happen via

**[03:14]** flows and they typically happen via

**[03:14]** flows and they typically happen via browser based interfaces that that

**[03:16]** browser based interfaces that that

**[03:16]** browser based interfaces that that you've seen when you've used these types

**[03:17]** you've seen when you've used these types

**[03:18]** you've seen when you've used these types of applications. Now one thing that gets

**[03:21]** of applications. Now one thing that gets

**[03:21]** of applications. Now one thing that gets kind of confusing for people is that

**[03:23]** kind of confusing for people is that

**[03:23]** kind of confusing for people is that OOTH is oftent times used to implement

**[03:26]** OOTH is oftent times used to implement

**[03:26]** OOTH is oftent times used to implement things like signin with Google or signin

**[03:28]** things like signin with Google or signin

**[03:28]** things like signin with Google or signin with uh Facebook. Uh and this is

**[03:30]** with uh Facebook. Uh and this is

**[03:30]** with uh Facebook. Uh and this is confusing because we refer to OOTH as an

**[03:32]** confusing because we refer to OOTH as an

**[03:32]** confusing because we refer to OOTH as an authorization protocol or a delegated

**[03:34]** authorization protocol or a delegated

**[03:34]** authorization protocol or a delegated authorization protocol specifically. So

**[03:36]** authorization protocol specifically. So

**[03:36]** authorization protocol specifically. So what's what's going on here when we use

**[03:37]** what's what's going on here when we use

**[03:38]** what's what's going on here when we use it for signin? Well, this is really just

**[03:39]** it for signin? Well, this is really just

**[03:40]** it for signin? Well, this is really just a special case where the API gets

**[03:42]** a special case where the API gets

**[03:42]** a special case where the API gets replaced with a user info API that just

**[03:44]** replaced with a user info API that just

**[03:44]** replaced with a user info API that just returns claims about the user who logged

**[03:46]** returns claims about the user who logged

**[03:46]** returns claims about the user who logged in. So their ID, their name, their email

**[03:48]** in. So their ID, their name, their email

**[03:48]** in. So their ID, their name, their email address, etc. And we kind of use

**[03:50]** address, etc. And we kind of use

**[03:50]** address, etc. And we kind of use authorization to back our way into

**[03:53]** authorization to back our way into

**[03:53]** authorization to back our way into authentication. Um, and this became like

**[03:55]** authentication. Um, and this became like

**[03:55]** authentication. Um, and this became like such a common pattern that people used

**[03:57]** such a common pattern that people used

**[03:57]** such a common pattern that people used with OOTH that it got formally

**[03:59]** with OOTH that it got formally

**[03:59]** with OOTH that it got formally standardized as open ID connect which is


### [04:00 - 05:00]

**[04:01]** standardized as open ID connect which is

**[04:01]** standardized as open ID connect which is just an identity layer on top of OOTH uh

**[04:03]** just an identity layer on top of OOTH uh

**[04:03]** just an identity layer on top of OOTH uh that standardizes the response format of

**[04:06]** that standardizes the response format of

**[04:06]** that standardizes the response format of that user info API. Uh, it also does a

**[04:08]** that user info API. Uh, it also does a

**[04:08]** that user info API. Uh, it also does a couple things that are kind of confusing

**[04:09]** couple things that are kind of confusing

**[04:10]** couple things that are kind of confusing like introduce more terminology which

**[04:11]** like introduce more terminology which

**[04:11]** like introduce more terminology which identity people are prone to do. Uh, we

**[04:13]** identity people are prone to do. Uh, we

**[04:14]** identity people are prone to do. Uh, we call the authorization server now an

**[04:15]** call the authorization server now an

**[04:15]** call the authorization server now an identity pro identity provider in in the

**[04:18]** identity pro identity provider in in the

**[04:18]** identity pro identity provider in in the scope of open ID connect and

**[04:19]** scope of open ID connect and

**[04:20]** scope of open ID connect and applications are known as relying

**[04:21]** applications are known as relying

**[04:21]** applications are known as relying parties. Don't get hung up on the

**[04:23]** parties. Don't get hung up on the

**[04:23]** parties. Don't get hung up on the terminology. It's it's all the same

**[04:24]** terminology. It's it's all the same

**[04:24]** terminology. It's it's all the same thing.

**[04:26]** thing.

**[04:26]** thing. Uh one other thing that open ID connect

**[04:28]** Uh one other thing that open ID connect

**[04:28]** Uh one other thing that open ID connect does is it introduces an ID token. This

**[04:31]** does is it introduces an ID token. This

**[04:31]** does is it introduces an ID token. This is simply a JSON web token which is a

**[04:33]** is simply a JSON web token which is a

**[04:33]** is simply a JSON web token which is a cryptographically signed statement about

**[04:35]** cryptographically signed statement about

**[04:35]** cryptographically signed statement about who the user is. Uh this overlaps a lot

**[04:37]** who the user is. Uh this overlaps a lot

**[04:37]** who the user is. Uh this overlaps a lot with the user info API. You can think of

**[04:39]** with the user info API. You can think of

**[04:39]** with the user info API. You can think of it as sort of an optimization that the

**[04:41]** it as sort of an optimization that the

**[04:41]** it as sort of an optimization that the application can verify itself without

**[04:43]** application can verify itself without

**[04:43]** application can verify itself without making API requests. It also serves some

**[04:46]** making API requests. It also serves some

**[04:46]** making API requests. It also serves some functions in like ongoing session

**[04:48]** functions in like ongoing session

**[04:48]** functions in like ongoing session management between applications and

**[04:49]** management between applications and

**[04:50]** management between applications and authorization servers, but that's kind

**[04:51]** authorization servers, but that's kind

**[04:51]** authorization servers, but that's kind of beyond the scope of introductory

**[04:53]** of beyond the scope of introductory

**[04:53]** of beyond the scope of introductory material here. Uh in the real world,

**[04:56]** material here. Uh in the real world,

**[04:56]** material here. Uh in the real world, these things get deployed together.

**[04:58]** these things get deployed together.

**[04:58]** these things get deployed together. We'll typically run authorization and


### [05:00 - 06:00]

**[05:00]** We'll typically run authorization and

**[05:00]** We'll typically run authorization and authentication flows uh in line uh so

**[05:03]** authentication flows uh in line uh so

**[05:03]** authentication flows uh in line uh so that you know we know who the user is

**[05:05]** that you know we know who the user is

**[05:05]** that you know we know who the user is who logged in as well as get access to

**[05:07]** who logged in as well as get access to

**[05:07]** who logged in as well as get access to things like their Google calendar.

**[05:10]** things like their Google calendar.

**[05:10]** things like their Google calendar. Uh one thing to call out that is

**[05:12]** Uh one thing to call out that is

**[05:12]** Uh one thing to call out that is important here is that there's three

**[05:13]** important here is that there's three

**[05:14]** important here is that there's three roles in Oath. Uh the client uh and the

**[05:16]** roles in Oath. Uh the client uh and the

**[05:16]** roles in Oath. Uh the client uh and the resource server I think are all

**[05:18]** resource server I think are all

**[05:18]** resource server I think are all relatively straightforward. We

**[05:19]** relatively straightforward. We

**[05:19]** relatively straightforward. We understand that from client server

**[05:20]** understand that from client server

**[05:20]** understand that from client server architectures. The client requests act

**[05:23]** architectures. The client requests act

**[05:23]** architectures. The client requests act uh resources and the resource server

**[05:25]** uh resources and the resource server

**[05:25]** uh resources and the resource server responds with the data. Uh what gets

**[05:27]** responds with the data. Uh what gets

**[05:27]** responds with the data. Uh what gets different is that we introduce this

**[05:29]** different is that we introduce this

**[05:29]** different is that we introduce this authorization server in the middle that

**[05:30]** authorization server in the middle that

**[05:30]** authorization server in the middle that mediates this access. Uh and it mediates

**[05:32]** mediates this access. Uh and it mediates

**[05:32]** mediates this access. Uh and it mediates it by issuing tokens. uh issues tokens

**[05:35]** it by issuing tokens. uh issues tokens

**[05:35]** it by issuing tokens. uh issues tokens back to the client which holds them and

**[05:37]** back to the client which holds them and

**[05:37]** back to the client which holds them and then presents them to a resource server

**[05:39]** then presents them to a resource server

**[05:39]** then presents them to a resource server and the resource server's job is to

**[05:41]** and the resource server's job is to

**[05:41]** and the resource server's job is to verify those tokens. Now what's what's

**[05:44]** verify those tokens. Now what's what's

**[05:44]** verify those tokens. Now what's what's the benefit of this sort of model? Uh

**[05:46]** the benefit of this sort of model? Uh

**[05:46]** the benefit of this sort of model? Uh the main benefit uh flows to the APIs.

**[05:49]** the main benefit uh flows to the APIs.

**[05:49]** the main benefit uh flows to the APIs. They don't have to care about anything

**[05:51]** They don't have to care about anything

**[05:51]** They don't have to care about anything to do with authentication anymore. So

**[05:52]** to do with authentication anymore. So

**[05:52]** to do with authentication anymore. So verifying user password or doing step-up

**[05:55]** verifying user password or doing step-up

**[05:55]** verifying user password or doing step-up authentication, running the consent

**[05:56]** authentication, running the consent

**[05:56]** authentication, running the consent flows, they hand all that job off to the

**[05:58]** flows, they hand all that job off to the

**[05:58]** flows, they hand all that job off to the authorization server and it gets kind of


### [06:00 - 07:00]

**[06:00]** authorization server and it gets kind of

**[06:00]** authorization server and it gets kind of abstracted away by the token uh that the

**[06:03]** abstracted away by the token uh that the

**[06:03]** abstracted away by the token uh that the API can verify what has happened. Um

**[06:06]** API can verify what has happened. Um

**[06:06]** API can verify what has happened. Um there's also some benefits that we can

**[06:07]** there's also some benefits that we can

**[06:07]** there's also some benefits that we can like centralize policy uh and then

**[06:10]** like centralize policy uh and then

**[06:10]** like centralize policy uh and then deploy ecosystems of apps and APIs all

**[06:13]** deploy ecosystems of apps and APIs all

**[06:13]** deploy ecosystems of apps and APIs all kind of protected by a central location

**[06:14]** kind of protected by a central location

**[06:14]** kind of protected by a central location and and build out the the ecosystems

**[06:16]** and and build out the the ecosystems

**[06:16]** and and build out the the ecosystems that we all know today.

**[06:18]** that we all know today.

**[06:18]** that we all know today. Uh how do we apply this to MCP and

**[06:21]** Uh how do we apply this to MCP and

**[06:21]** Uh how do we apply this to MCP and agents in in particular? Well, it it

**[06:23]** agents in in particular? Well, it it

**[06:23]** agents in in particular? Well, it it should be pretty simple. Uh now our

**[06:25]** should be pretty simple. Uh now our

**[06:25]** should be pretty simple. Uh now our applications get replaced by a chatbot

**[06:29]** applications get replaced by a chatbot

**[06:29]** applications get replaced by a chatbot or agent like claude. Uh that we want to

**[06:31]** or agent like claude. Uh that we want to

**[06:32]** or agent like claude. Uh that we want to connect to MCP servers. Uh we the MCP

**[06:35]** connect to MCP servers. Uh we the MCP

**[06:35]** connect to MCP servers. Uh we the MCP clients and the MCP servers should get

**[06:37]** clients and the MCP servers should get

**[06:37]** clients and the MCP servers should get authorized via OOTH by you know the

**[06:39]** authorized via OOTH by you know the

**[06:39]** authorized via OOTH by you know the controlling authorization server in the

**[06:41]** controlling authorization server in the

**[06:41]** controlling authorization server in the middle. This should be pretty simple,

**[06:43]** middle. This should be pretty simple,

**[06:43]** middle. This should be pretty simple, right? Well, nothing with OOTH is ever

**[06:46]** right? Well, nothing with OOTH is ever

**[06:46]** right? Well, nothing with OOTH is ever so simple. So let's take a look at the

**[06:48]** so simple. So let's take a look at the

**[06:48]** so simple. So let's take a look at the state of authorization in MCP. Uh we're

**[06:51]** state of authorization in MCP. Uh we're

**[06:51]** state of authorization in MCP. Uh we're going to look at at where it started,

**[06:52]** going to look at at where it started,

**[06:52]** going to look at at where it started, where it is now, and and then where it's

**[06:54]** where it is now, and and then where it's

**[06:54]** where it is now, and and then where it's going in the future.

**[06:57]** going in the future.

**[06:57]** going in the future. So the first version of MCP, uh it's a

**[06:59]** So the first version of MCP, uh it's a

**[06:59]** So the first version of MCP, uh it's a pretty young protocol. It's like seven


### [07:00 - 08:00]

**[07:01]** pretty young protocol. It's like seven

**[07:01]** pretty young protocol. It's like seven months old to the day, I think. Uh the

**[07:03]** months old to the day, I think. Uh the

**[07:03]** months old to the day, I think. Uh the first version I like to call the NOOTH

**[07:05]** first version I like to call the NOOTH

**[07:05]** first version I like to call the NOOTH version. It didn't have any

**[07:06]** version. It didn't have any

**[07:06]** version. It didn't have any authorization in it at all, uh which

**[07:09]** authorization in it at all, uh which

**[07:09]** authorization in it at all, uh which they admitted in the spec. It was really

**[07:11]** they admitted in the spec. It was really

**[07:11]** they admitted in the spec. It was really a way to get something out there

**[07:12]** a way to get something out there

**[07:12]** a way to get something out there primarily for uh local MCP servers. uh

**[07:15]** primarily for uh local MCP servers. uh

**[07:15]** primarily for uh local MCP servers. uh there was some notion of remote MCP

**[07:17]** there was some notion of remote MCP

**[07:17]** there was some notion of remote MCP servers uh but again no authorization

**[07:20]** servers uh but again no authorization

**[07:20]** servers uh but again no authorization but this kind of spurred discussion

**[07:21]** but this kind of spurred discussion

**[07:21]** but this kind of spurred discussion people saw the promise of MCP and and

**[07:24]** people saw the promise of MCP and and

**[07:24]** people saw the promise of MCP and and started discussing how to add

**[07:25]** started discussing how to add

**[07:25]** started discussing how to add authorization to it. Uh now we have the

**[07:29]** authorization to it. Uh now we have the

**[07:29]** authorization to it. Uh now we have the latest draft of the specification uh

**[07:31]** latest draft of the specification uh

**[07:31]** latest draft of the specification uh which was published in late March. I

**[07:34]** which was published in late March. I

**[07:34]** which was published in late March. I like to refer to this as OOTH the first

**[07:36]** like to refer to this as OOTH the first

**[07:36]** like to refer to this as OOTH the first attempt and for anyone who has ever done

**[07:38]** attempt and for anyone who has ever done

**[07:38]** attempt and for anyone who has ever done OOTH implementations the first attempt

**[07:40]** OOTH implementations the first attempt

**[07:40]** OOTH implementations the first attempt is always pretty poor. Uh, and that is

**[07:43]** is always pretty poor. Uh, and that is

**[07:43]** is always pretty poor. Uh, and that is the case with this version of the

**[07:44]** the case with this version of the

**[07:44]** the case with this version of the specification of MCP. Uh, I don't

**[07:47]** specification of MCP. Uh, I don't

**[07:47]** specification of MCP. Uh, I don't actually recommend anyone read the

**[07:49]** actually recommend anyone read the

**[07:49]** actually recommend anyone read the authorization part of the MCP

**[07:51]** authorization part of the MCP

**[07:51]** authorization part of the MCP specification as it is today because

**[07:52]** specification as it is today because

**[07:52]** specification as it is today because you'll walk away with a pretty

**[07:54]** you'll walk away with a pretty

**[07:54]** you'll walk away with a pretty misinformed view of what OOTH is. But as

**[07:56]** misinformed view of what OOTH is. But as

**[07:56]** misinformed view of what OOTH is. But as a quick recap, what it does, it says,

**[07:58]** a quick recap, what it does, it says,

**[07:58]** a quick recap, what it does, it says, okay, MCP clients got to implement the


### [08:00 - 09:00]

**[08:00]** okay, MCP clients got to implement the

**[08:00]** okay, MCP clients got to implement the client side of of OOTH. That all makes

**[08:03]** client side of of OOTH. That all makes

**[08:03]** client side of of OOTH. That all makes sense. And then it also says MCTP

**[08:06]** sense. And then it also says MCTP

**[08:06]** sense. And then it also says MCTP servers. You need to implement all all

**[08:07]** servers. You need to implement all all

**[08:07]** servers. You need to implement all all of OOTH 2 including authentication,

**[08:10]** of OOTH 2 including authentication,

**[08:10]** of OOTH 2 including authentication, token issuance, etc. Now, OOTH has three

**[08:14]** token issuance, etc. Now, OOTH has three

**[08:14]** token issuance, etc. Now, OOTH has three roles. Where's where's the third role

**[08:16]** roles. Where's where's the third role

**[08:16]** roles. Where's where's the third role here? What happened to the OOTH server?

**[08:17]** here? What happened to the OOTH server?

**[08:17]** here? What happened to the OOTH server? Well, it got collapsed into the MCP

**[08:19]** Well, it got collapsed into the MCP

**[08:19]** Well, it got collapsed into the MCP server, which which is a bit odd. Uh and

**[08:22]** server, which which is a bit odd. Uh and

**[08:22]** server, which which is a bit odd. Uh and people started noticing this. So, 5 days

**[08:25]** people started noticing this. So, 5 days

**[08:25]** people started noticing this. So, 5 days after the specification was released, uh

**[08:27]** after the specification was released, uh

**[08:27]** after the specification was released, uh a blog post went viral. Uh this one from

**[08:30]** a blog post went viral. Uh this one from

**[08:30]** a blog post went viral. Uh this one from Christian Posta saying the MCP

**[08:32]** Christian Posta saying the MCP

**[08:32]** Christian Posta saying the MCP authorization spec is a mess for the

**[08:34]** authorization spec is a mess for the

**[08:34]** authorization spec is a mess for the enterprise. Uh and he states you know

**[08:36]** enterprise. Uh and he states you know

**[08:36]** enterprise. Uh and he states you know the problem here is that it treats the

**[08:38]** the problem here is that it treats the

**[08:38]** the problem here is that it treats the MCP server as both a resource server and

**[08:40]** MCP server as both a resource server and

**[08:40]** MCP server as both a resource server and authorization server. Uh Aaron Perky who

**[08:43]** authorization server. Uh Aaron Perky who

**[08:43]** authorization server. Uh Aaron Perky who does a lot of great OOTH standards work

**[08:45]** does a lot of great OOTH standards work

**[08:45]** does a lot of great OOTH standards work uh followed this up with another blog

**[08:47]** uh followed this up with another blog

**[08:47]** uh followed this up with another blog post that went viral titled let's fix

**[08:49]** post that went viral titled let's fix

**[08:49]** post that went viral titled let's fix OOTH and MCP where he noted that you

**[08:52]** OOTH and MCP where he noted that you

**[08:52]** OOTH and MCP where he noted that you know a bunch of the confusion that was

**[08:54]** know a bunch of the confusion that was

**[08:54]** know a bunch of the confusion that was happening was because the diagram show

**[08:56]** happening was because the diagram show

**[08:56]** happening was because the diagram show that the MCP server itself is handling

**[08:58]** that the MCP server itself is handling

**[08:58]** that the MCP server itself is handling authorization.


### [09:00 - 10:00]

**[09:03]** Now then this kind of culminated in a in

**[09:03]** Now then this kind of culminated in a in a PR to the specification where uh

**[09:06]** a PR to the specification where uh

**[09:06]** a PR to the specification where uh people proposed let's let's fix this

**[09:08]** people proposed let's let's fix this

**[09:08]** people proposed let's let's fix this problem. Let's just shift uh the MCP

**[09:10]** problem. Let's just shift uh the MCP

**[09:10]** problem. Let's just shift uh the MCP server to be an OOTH OOTH resource

**[09:12]** server to be an OOTH OOTH resource

**[09:12]** server to be an OOTH OOTH resource server and everything will be good. This

**[09:14]** server and everything will be good. This

**[09:14]** server and everything will be good. This is a super interesting PR to read.

**[09:16]** is a super interesting PR to read.

**[09:16]** is a super interesting PR to read. There's like 400 some comments on it.

**[09:17]** There's like 400 some comments on it.

**[09:18]** There's like 400 some comments on it. It's not even the only PR there. Uh but

**[09:21]** It's not even the only PR there. Uh but

**[09:21]** It's not even the only PR there. Uh but just kind of a example of how people

**[09:23]** just kind of a example of how people

**[09:23]** just kind of a example of how people just picked up on this problem and ran

**[09:25]** just picked up on this problem and ran

**[09:25]** just picked up on this problem and ran with it. Now, I'm not usually one to say

**[09:28]** with it. Now, I'm not usually one to say

**[09:28]** with it. Now, I'm not usually one to say I told you so, but all the way back in

**[09:30]** I told you so, but all the way back in

**[09:30]** I told you so, but all the way back in January of this year, I commented on the

**[09:33]** January of this year, I commented on the

**[09:33]** January of this year, I commented on the uh as a review for the specification. I

**[09:36]** uh as a review for the specification. I

**[09:36]** uh as a review for the specification. I was like, "Hey, I recommend we model MCP

**[09:39]** was like, "Hey, I recommend we model MCP

**[09:39]** was like, "Hey, I recommend we model MCP servers as as resource servers from an

**[09:41]** servers as as resource servers from an

**[09:41]** servers as as resource servers from an OOTH perspective." I'm not quite sure

**[09:43]** OOTH perspective." I'm not quite sure

**[09:43]** OOTH perspective." I'm not quite sure where where that got lost. It it didn't

**[09:44]** where where that got lost. It it didn't

**[09:44]** where where that got lost. It it didn't get picked up, but in any case, uh we

**[09:47]** get picked up, but in any case, uh we

**[09:47]** get picked up, but in any case, uh we fixed this problem. And one of the

**[09:49]** fixed this problem. And one of the

**[09:49]** fixed this problem. And one of the reasons I'm here is to tell us all more

**[09:50]** reasons I'm here is to tell us all more

**[09:50]** reasons I'm here is to tell us all more about OOTH things that we need to pay

**[09:52]** about OOTH things that we need to pay

**[09:52]** about OOTH things that we need to pay attention to in order to avoid this

**[09:54]** attention to in order to avoid this

**[09:54]** attention to in order to avoid this problem in the future.

**[09:56]** problem in the future.

**[09:56]** problem in the future. Uh so, okay, the next attempt in draft

**[09:58]** Uh so, okay, the next attempt in draft

**[09:58]** Uh so, okay, the next attempt in draft all this feedback has been incorporated


### [10:00 - 11:00]

**[10:00]** all this feedback has been incorporated

**[10:00]** all this feedback has been incorporated and the MCP spec is kind of like fixing

**[10:03]** and the MCP spec is kind of like fixing

**[10:03]** and the MCP spec is kind of like fixing its issues. Um, and the draft version of

**[10:05]** its issues. Um, and the draft version of

**[10:05]** its issues. Um, and the draft version of the specification models o all of OOTH

**[10:08]** the specification models o all of OOTH

**[10:08]** the specification models o all of OOTH pretty cleanly and pretty nicely. Uh,

**[10:10]** pretty cleanly and pretty nicely. Uh,

**[10:10]** pretty cleanly and pretty nicely. Uh, the OOTH authorization server is a

**[10:12]** the OOTH authorization server is a

**[10:12]** the OOTH authorization server is a totally separate entity. And this is

**[10:14]** totally separate entity. And this is

**[10:14]** totally separate entity. And this is really beneficial for all of you

**[10:16]** really beneficial for all of you

**[10:16]** really beneficial for all of you building MCP servers because your job

**[10:18]** building MCP servers because your job

**[10:18]** building MCP servers because your job gets a whole lot easier. All you have to

**[10:20]** gets a whole lot easier. All you have to

**[10:20]** gets a whole lot easier. All you have to do is verify the tokens that come in

**[10:22]** do is verify the tokens that come in

**[10:22]** do is verify the tokens that come in over HTTP and hand off all the other

**[10:25]** over HTTP and hand off all the other

**[10:25]** over HTTP and hand off all the other responsibility to the OA server.

**[10:29]** responsibility to the OA server.

**[10:29]** responsibility to the OA server. So, we're back to a pretty good place uh

**[10:31]** So, we're back to a pretty good place uh

**[10:31]** So, we're back to a pretty good place uh with respect to OOTH and MCP and in

**[10:33]** with respect to OOTH and MCP and in

**[10:33]** with respect to OOTH and MCP and in particular how we authorize connections

**[10:35]** particular how we authorize connections

**[10:35]** particular how we authorize connections between MCP clients and MCP servers.

**[10:39]** between MCP clients and MCP servers.

**[10:39]** between MCP clients and MCP servers. So, let's talk about the future. If if

**[10:42]** So, let's talk about the future. If if

**[10:42]** So, let's talk about the future. If if this is all we do with OOTH, we're not

**[10:44]** this is all we do with OOTH, we're not

**[10:44]** this is all we do with OOTH, we're not even scratching the surface of what we

**[10:45]** even scratching the surface of what we

**[10:45]** even scratching the surface of what we need in order to fully secure AI and AI

**[10:48]** need in order to fully secure AI and AI

**[10:48]** need in order to fully secure AI and AI interactions. So, what else are we going

**[10:50]** interactions. So, what else are we going

**[10:50]** interactions. So, what else are we going to need? Uh we're going to burn through

**[10:52]** to need? Uh we're going to burn through

**[10:52]** to need? Uh we're going to burn through this here pretty quick. The first is

**[10:54]** this here pretty quick. The first is

**[10:54]** this here pretty quick. The first is agentto agent uh communication. So what

**[10:58]** agentto agent uh communication. So what

**[10:58]** agentto agent uh communication. So what we've seen with OAS so far as it's


### [11:00 - 12:00]

**[11:00]** we've seen with OAS so far as it's

**[11:00]** we've seen with OAS so far as it's applied to MCP like I said that's

**[11:01]** applied to MCP like I said that's

**[11:02]** applied to MCP like I said that's referred to as the authorization code

**[11:03]** referred to as the authorization code

**[11:03]** referred to as the authorization code flow and it's particularly relevant for

**[11:05]** flow and it's particularly relevant for

**[11:05]** flow and it's particularly relevant for when we want to do end user delegation.

**[11:07]** when we want to do end user delegation.

**[11:07]** when we want to do end user delegation. Uh but there's a whole bunch of other

**[11:08]** Uh but there's a whole bunch of other

**[11:08]** Uh but there's a whole bunch of other flows in OOTH uh that are relevant in

**[11:11]** flows in OOTH uh that are relevant in

**[11:11]** flows in OOTH uh that are relevant in particular client credentials and this

**[11:13]** particular client credentials and this

**[11:13]** particular client credentials and this applies when we want agents to

**[11:14]** applies when we want agents to

**[11:14]** applies when we want agents to communicate with other agents or other

**[11:16]** communicate with other agents or other

**[11:16]** communicate with other agents or other MCP servers on their own behalf not on

**[11:19]** MCP servers on their own behalf not on

**[11:19]** MCP servers on their own behalf not on behalf of a user. So this is one thing

**[11:21]** behalf of a user. So this is one thing

**[11:21]** behalf of a user. So this is one thing to pay pay attention to. The next, this

**[11:24]** to pay pay attention to. The next, this

**[11:24]** to pay pay attention to. The next, this kind of begs the question, agent

**[11:26]** kind of begs the question, agent

**[11:26]** kind of begs the question, agent identity. Uh, what should we do about

**[11:28]** identity. Uh, what should we do about

**[11:28]** identity. Uh, what should we do about this? Well, if anyone's ever done OOTH

**[11:30]** this? Well, if anyone's ever done OOTH

**[11:30]** this? Well, if anyone's ever done OOTH development, you you're probably

**[11:31]** development, you you're probably

**[11:32]** development, you you're probably familiar with this type of flow is you

**[11:33]** familiar with this type of flow is you

**[11:33]** familiar with this type of flow is you want to build an application. Uh, you

**[11:35]** want to build an application. Uh, you

**[11:35]** want to build an application. Uh, you want to integrate with an API. You go to

**[11:37]** want to integrate with an API. You go to

**[11:37]** want to integrate with an API. You go to some developer portal, create a new

**[11:39]** some developer portal, create a new

**[11:39]** some developer portal, create a new application, get a client ID and secret,

**[11:41]** application, get a client ID and secret,

**[11:41]** application, get a client ID and secret, and then somehow configure your uh

**[11:43]** and then somehow configure your uh

**[11:43]** and then somehow configure your uh application with that those credentials.

**[11:45]** application with that those credentials.

**[11:45]** application with that those credentials. Uh, this is a bunch of friction. This

**[11:48]** Uh, this is a bunch of friction. This

**[11:48]** Uh, this is a bunch of friction. This obviously won't apply well to uh MCP

**[11:50]** obviously won't apply well to uh MCP

**[11:50]** obviously won't apply well to uh MCP which is trying to be a standard pro

**[11:51]** which is trying to be a standard pro

**[11:52]** which is trying to be a standard pro protocol and you want to bring tools and

**[11:53]** protocol and you want to bring tools and

**[11:54]** protocol and you want to bring tools and agents together that that may not be

**[11:55]** agents together that that may not be

**[11:55]** agents together that that may not be aware of each other. Uh you can't do

**[11:57]** aware of each other. Uh you can't do

**[11:57]** aware of each other. Uh you can't do this if you presuppose some sort of

**[11:58]** this if you presuppose some sort of

**[11:58]** this if you presuppose some sort of registration process. So what does MCP


### [12:00 - 13:00]

**[12:02]** registration process. So what does MCP

**[12:02]** registration process. So what does MCP do? Uh well it picks up what is known as

**[12:05]** do? Uh well it picks up what is known as

**[12:06]** do? Uh well it picks up what is known as dynamic client registration. Uh what

**[12:08]** dynamic client registration. Uh what

**[12:08]** dynamic client registration. Uh what this does is allows applications and

**[12:10]** this does is allows applications and

**[12:10]** this does is allows applications and agents to request credentials at runtime

**[12:12]** agents to request credentials at runtime

**[12:12]** agents to request credentials at runtime rather than like ahead of time in manual

**[12:15]** rather than like ahead of time in manual

**[12:15]** rather than like ahead of time in manual registration. Uh so an agent says hey

**[12:18]** registration. Uh so an agent says hey

**[12:18]** registration. Uh so an agent says hey like this is who I am give me a client

**[12:20]** like this is who I am give me a client

**[12:20]** like this is who I am give me a client ID and secret the server does it and the

**[12:22]** ID and secret the server does it and the

**[12:22]** ID and secret the server does it and the agent goes about the rest of its ooth

**[12:23]** agent goes about the rest of its ooth

**[12:23]** agent goes about the rest of its ooth flow. Now this specification has been

**[12:26]** flow. Now this specification has been

**[12:26]** flow. Now this specification has been around for about 10 years and in

**[12:28]** around for about 10 years and in

**[12:28]** around for about 10 years and in practice has seen like no meaningful

**[12:30]** practice has seen like no meaningful

**[12:30]** practice has seen like no meaningful adoption and one of the implications

**[12:33]** adoption and one of the implications

**[12:33]** adoption and one of the implications behind this is it like makes all agents

**[12:36]** behind this is it like makes all agents

**[12:36]** behind this is it like makes all agents anonymous because the registration

**[12:38]** anonymous because the registration

**[12:38]** anonymous because the registration request itself is uncredentialed. This

**[12:41]** request itself is uncredentialed. This

**[12:41]** request itself is uncredentialed. This makes it hard to build trust in agents.

**[12:43]** makes it hard to build trust in agents.

**[12:43]** makes it hard to build trust in agents. It's probably not super viable in my

**[12:45]** It's probably not super viable in my

**[12:45]** It's probably not super viable in my opinion.

**[12:46]** opinion.

**[12:46]** opinion. So what should we be looking at instead?

**[12:49]** So what should we be looking at instead?

**[12:49]** So what should we be looking at instead? Well, there's many cases where we just

**[12:51]** Well, there's many cases where we just

**[12:51]** Well, there's many cases where we just want to use public clients that we don't

**[12:53]** want to use public clients that we don't

**[12:53]** want to use public clients that we don't really care about verifying their

**[12:54]** really care about verifying their

**[12:54]** really care about verifying their identity. In this case, there's an

**[12:56]** identity. In this case, there's an

**[12:56]** identity. In this case, there's an emerging specification called push

**[12:58]** emerging specification called push

**[12:58]** emerging specification called push client registration uh which introduces


### [13:00 - 14:00]

**[13:00]** client registration uh which introduces

**[13:00]** client registration uh which introduces this kind of like well-known string to

**[13:02]** this kind of like well-known string to

**[13:02]** this kind of like well-known string to identify a like public client. Uh we can

**[13:05]** identify a like public client. Uh we can

**[13:05]** identify a like public client. Uh we can just use this well-known string and we

**[13:06]** just use this well-known string and we

**[13:06]** just use this well-known string and we skip the whole registration song and

**[13:08]** skip the whole registration song and

**[13:08]** skip the whole registration song and dance and then the need to store the

**[13:09]** dance and then the need to store the

**[13:09]** dance and then the need to store the resulting state. Uh this is but a lot

**[13:12]** resulting state. Uh this is but a lot

**[13:12]** resulting state. Uh this is but a lot more simpler. It also has the capability

**[13:14]** more simpler. It also has the capability

**[13:14]** more simpler. It also has the capability to carry uh certain client metadata in

**[13:16]** to carry uh certain client metadata in

**[13:16]** to carry uh certain client metadata in the request if if that's necessary. So

**[13:19]** the request if if that's necessary. So

**[13:19]** the request if if that's necessary. So this is something we should look in for

**[13:20]** this is something we should look in for

**[13:20]** this is something we should look in for cases where public clients apply.

**[13:23]** cases where public clients apply.

**[13:23]** cases where public clients apply. Uh but what about clients that we

**[13:25]** Uh but what about clients that we

**[13:25]** Uh but what about clients that we actually want to authenticate and verify

**[13:27]** actually want to authenticate and verify

**[13:27]** actually want to authenticate and verify their identity? Well, my proposal here

**[13:30]** their identity? Well, my proposal here

**[13:30]** their identity? Well, my proposal here is that we should start looking at uh

**[13:32]** is that we should start looking at uh

**[13:32]** is that we should start looking at uh using URLs in PKI for identity. Um, this

**[13:36]** using URLs in PKI for identity. Um, this

**[13:36]** using URLs in PKI for identity. Um, this lets us reuse the existing identifiers

**[13:38]** lets us reuse the existing identifiers

**[13:38]** lets us reuse the existing identifiers that people already associate with the

**[13:40]** that people already associate with the

**[13:40]** that people already associate with the apps they're using and and can repurpose

**[13:41]** apps they're using and and can repurpose

**[13:42]** apps they're using and and can repurpose them into the agent world. This looks

**[13:44]** them into the agent world. This looks

**[13:44]** them into the agent world. This looks like in practice we'd have a URL such as

**[13:47]** like in practice we'd have a URL such as

**[13:47]** like in practice we'd have a URL such as uh, you know, agent.com to be used as a

**[13:49]** uh, you know, agent.com to be used as a

**[13:49]** uh, you know, agent.com to be used as a client identity in OOTH flows and then

**[13:51]** client identity in OOTH flows and then

**[13:51]** client identity in OOTH flows and then through the magic of uh, cryp

**[13:53]** through the magic of uh, cryp

**[13:53]** through the magic of uh, cryp cryptography and key sets, we can

**[13:55]** cryptography and key sets, we can

**[13:55]** cryptography and key sets, we can authenticate these agents by having them

**[13:57]** authenticate these agents by having them

**[13:57]** authenticate these agents by having them sign uh, jot assertions or HTTP message


### [14:00 - 15:00]

**[14:00]** sign uh, jot assertions or HTTP message

**[14:00]** sign uh, jot assertions or HTTP message signatures that we can then verify with

**[14:02]** signatures that we can then verify with

**[14:02]** signatures that we can then verify with with the corresponding public keys.

**[14:09]** All right, this dub dovetales into agent

**[14:09]** All right, this dub dovetales into agent add astation. Uh, we've connected our

**[14:12]** add astation. Uh, we've connected our

**[14:12]** add astation. Uh, we've connected our agents to the resources that we're

**[14:13]** agents to the resources that we're

**[14:13]** agents to the resources that we're using, but then that agent turns around

**[14:15]** using, but then that agent turns around

**[14:15]** using, but then that agent turns around and sends all that information up to an

**[14:16]** and sends all that information up to an

**[14:16]** and sends all that information up to an LLM. This seems like something we should

**[14:18]** LLM. This seems like something we should

**[14:18]** LLM. This seems like something we should probably have some awareness of and

**[14:19]** probably have some awareness of and

**[14:19]** probably have some awareness of and control over. Uh, so in kind of

**[14:21]** control over. Uh, so in kind of

**[14:21]** control over. Uh, so in kind of protected environments, we can sort of

**[14:23]** protected environments, we can sort of

**[14:24]** protected environments, we can sort of get by like treating the LLM as just

**[14:26]** get by like treating the LLM as just

**[14:26]** get by like treating the LLM as just another API, which often it is. uh and

**[14:28]** another API, which often it is. uh and

**[14:28]** another API, which often it is. uh and this is a technique we could apply but

**[14:30]** this is a technique we could apply but

**[14:30]** this is a technique we could apply but it has limited uh capabilities when we

**[14:33]** it has limited uh capabilities when we

**[14:33]** it has limited uh capabilities when we look at like edge deployed agents such

**[14:35]** look at like edge deployed agents such

**[14:35]** look at like edge deployed agents such as on the desktop or mobile devices

**[14:37]** as on the desktop or mobile devices

**[14:37]** as on the desktop or mobile devices where we don't really control their

**[14:39]** where we don't really control their

**[14:39]** where we don't really control their software environment. So there's a bunch

**[14:41]** software environment. So there's a bunch

**[14:41]** software environment. So there's a bunch of interesting work going on in the IET

**[14:42]** of interesting work going on in the IET

**[14:42]** of interesting work going on in the IET app now with respect to like remote

**[14:44]** app now with respect to like remote

**[14:44]** app now with respect to like remote addestation and supply chain uh security

**[14:47]** addestation and supply chain uh security

**[14:47]** addestation and supply chain uh security where we can start to ad attest to the

**[14:49]** where we can start to ad attest to the

**[14:49]** where we can start to ad attest to the state of the device and the software

**[14:50]** state of the device and the software

**[14:50]** state of the device and the software running on it and know what LLM our data

**[14:53]** running on it and know what LLM our data

**[14:53]** running on it and know what LLM our data is going to wind up in and then

**[14:55]** is going to wind up in and then

**[14:55]** is going to wind up in and then incorporate that into OOTH authorization

**[14:57]** incorporate that into OOTH authorization

**[14:57]** incorporate that into OOTH authorization flows.

**[14:59]** flows.

**[14:59]** flows. Next up transactional authorization what


### [15:00 - 16:00]

**[15:01]** Next up transactional authorization what

**[15:01]** Next up transactional authorization what we've done to date in OOTH uh is uh

**[15:05]** we've done to date in OOTH uh is uh

**[15:05]** we've done to date in OOTH uh is uh introduce scopes. This is a whole lot

**[15:07]** introduce scopes. This is a whole lot

**[15:07]** introduce scopes. This is a whole lot better than passwords which OOTH kind of

**[15:09]** better than passwords which OOTH kind of

**[15:09]** better than passwords which OOTH kind of replaced back in the day uh in the sense

**[15:11]** replaced back in the day uh in the sense

**[15:11]** replaced back in the day uh in the sense that now we can do more fine grain

**[15:13]** that now we can do more fine grain

**[15:13]** that now we can do more fine grain permissions such as like read versus

**[15:15]** permissions such as like read versus

**[15:15]** permissions such as like read versus write access. Um but in practice these

**[15:18]** write access. Um but in practice these

**[15:18]** write access. Um but in practice these end up being a little bit too coar

**[15:19]** end up being a little bit too coar

**[15:19]** end up being a little bit too coar grained for a lot of use cases and

**[15:21]** grained for a lot of use cases and

**[15:21]** grained for a lot of use cases and oftentimes a little bit longer lived

**[15:23]** oftentimes a little bit longer lived

**[15:23]** oftentimes a little bit longer lived than than we might like. Uh in in agent

**[15:27]** than than we might like. Uh in in agent

**[15:27]** than than we might like. Uh in in agent interactions we're going to have to be

**[15:28]** interactions we're going to have to be

**[15:28]** interactions we're going to have to be increasingly transactional. So imagine

**[15:30]** increasingly transactional. So imagine

**[15:30]** increasingly transactional. So imagine use cases where you want agents to do

**[15:32]** use cases where you want agents to do

**[15:32]** use cases where you want agents to do financial trans transactions or

**[15:34]** financial trans transactions or

**[15:34]** financial trans transactions or commercial transactions. We're going to

**[15:36]** commercial transactions. We're going to

**[15:36]** commercial transactions. We're going to want to authorize things on a

**[15:38]** want to authorize things on a

**[15:38]** want to authorize things on a transaction basis potentially with uh

**[15:40]** transaction basis potentially with uh

**[15:40]** transaction basis potentially with uh specific amounts or or financial

**[15:42]** specific amounts or or financial

**[15:42]** specific amounts or or financial budgets. So we're going to have to look

**[15:44]** budgets. So we're going to have to look

**[15:44]** budgets. So we're going to have to look at moving to more dynamic access in this

**[15:47]** at moving to more dynamic access in this

**[15:47]** at moving to more dynamic access in this respect. There's a proposal that's

**[15:49]** respect. There's a proposal that's

**[15:49]** respect. There's a proposal that's actually like a specification at this

**[15:50]** actually like a specification at this

**[15:50]** actually like a specification at this point called rich authorization requests

**[15:52]** point called rich authorization requests

**[15:52]** point called rich authorization requests which is which is worth looking into um

**[15:55]** which is which is worth looking into um

**[15:55]** which is which is worth looking into um and something that we can take

**[15:56]** and something that we can take

**[15:56]** and something that we can take inspiration from or either adopt

**[15:58]** inspiration from or either adopt

**[15:58]** inspiration from or either adopt directly for these these use cases.


### [16:00 - 17:00]

**[16:02]** directly for these these use cases.

**[16:02]** directly for these these use cases. Next up we have chain of custody. This

**[16:04]** Next up we have chain of custody. This

**[16:04]** Next up we have chain of custody. This is uh particularly interesting to me. Uh

**[16:07]** is uh particularly interesting to me. Uh

**[16:07]** is uh particularly interesting to me. Uh what we talk about with MCP really

**[16:08]** what we talk about with MCP really

**[16:08]** what we talk about with MCP really covers the first leg of this. On the on

**[16:10]** covers the first leg of this. On the on

**[16:10]** covers the first leg of this. On the on the lefth hand side we have authorized

**[16:12]** the lefth hand side we have authorized

**[16:12]** the lefth hand side we have authorized connections between agents and MCP

**[16:15]** connections between agents and MCP

**[16:15]** connections between agents and MCP servers. But what happens on the right

**[16:16]** servers. But what happens on the right

**[16:16]** servers. But what happens on the right side is completely unspecified in terms

**[16:18]** side is completely unspecified in terms

**[16:18]** side is completely unspecified in terms of like the security pro profile. So how

**[16:21]** of like the security pro profile. So how

**[16:21]** of like the security pro profile. So how do we protect an MCP server that calls

**[16:24]** do we protect an MCP server that calls

**[16:24]** do we protect an MCP server that calls another API within the same domain? In

**[16:26]** another API within the same domain? In

**[16:26]** another API within the same domain? In particular, there's a technique called

**[16:28]** particular, there's a technique called

**[16:28]** particular, there's a technique called OOTH token exchange that I recommend

**[16:30]** OOTH token exchange that I recommend

**[16:30]** OOTH token exchange that I recommend everyone look into. Uh special case of

**[16:33]** everyone look into. Uh special case of

**[16:33]** everyone look into. Uh special case of this is MCP servers to third party APIs.

**[16:38]** this is MCP servers to third party APIs.

**[16:38]** this is MCP servers to third party APIs. In this case, uh we should look into

**[16:40]** In this case, uh we should look into

**[16:40]** In this case, uh we should look into identity chaining across domains. uh and

**[16:43]** identity chaining across domains. uh and

**[16:43]** identity chaining across domains. uh and its corresponding specification the

**[16:44]** its corresponding specification the

**[16:44]** its corresponding specification the identity assertion grant which lets us

**[16:46]** identity assertion grant which lets us

**[16:46]** identity assertion grant which lets us do cross domain authorization in the

**[16:48]** do cross domain authorization in the

**[16:48]** do cross domain authorization in the back end. Somewhat outside the scope of

**[16:50]** back end. Somewhat outside the scope of

**[16:50]** back end. Somewhat outside the scope of OOTH is other internal infrastructure

**[16:52]** OOTH is other internal infrastructure

**[16:52]** OOTH is other internal infrastructure that people should be aware of as they

**[16:54]** that people should be aware of as they

**[16:54]** that people should be aware of as they look to deploy these agents. And then

**[16:56]** look to deploy these agents. And then

**[16:56]** look to deploy these agents. And then the culmination of this is really

**[16:58]** the culmination of this is really

**[16:58]** the culmination of this is really agentto agent flows where uh I don't


### [17:00 - 18:00]

**[17:00]** agentto agent flows where uh I don't

**[17:00]** agentto agent flows where uh I don't know how much of this is happening in

**[17:01]** know how much of this is happening in

**[17:01]** know how much of this is happening in practice today but people see the

**[17:02]** practice today but people see the

**[17:02]** practice today but people see the promise of it. Imagine big graphs of

**[17:05]** promise of it. Imagine big graphs of

**[17:05]** promise of it. Imagine big graphs of agents talking to other agents on other

**[17:06]** agents talking to other agents on other

**[17:06]** agents talking to other agents on other servers. We're going to need endto-end

**[17:08]** servers. We're going to need endto-end

**[17:08]** servers. We're going to need endto-end visibility as the authorization flows

**[17:10]** visibility as the authorization flows

**[17:10]** visibility as the authorization flows along these graphs.

**[17:13]** along these graphs.

**[17:13]** along these graphs. Finally, async interaction. Uh I think

**[17:16]** Finally, async interaction. Uh I think

**[17:16]** Finally, async interaction. Uh I think one of the key things to look at here is

**[17:17]** one of the key things to look at here is

**[17:17]** one of the key things to look at here is like OOTH typically assumes a user is

**[17:19]** like OOTH typically assumes a user is

**[17:19]** like OOTH typically assumes a user is sitting in front of a browser and

**[17:20]** sitting in front of a browser and

**[17:20]** sitting in front of a browser and relatively static, but as we kick off

**[17:23]** relatively static, but as we kick off

**[17:23]** relatively static, but as we kick off flows, users might walk away and agents

**[17:25]** flows, users might walk away and agents

**[17:25]** flows, users might walk away and agents do work in the background. They're going

**[17:26]** do work in the background. They're going

**[17:26]** do work in the background. They're going to need a way to reach out to the user

**[17:28]** to need a way to reach out to the user

**[17:28]** to need a way to reach out to the user and say, "Hey, I need a bit more access

**[17:29]** and say, "Hey, I need a bit more access

**[17:29]** and say, "Hey, I need a bit more access than I've been permissioned." How do we

**[17:31]** than I've been permissioned." How do we

**[17:31]** than I've been permissioned." How do we think about bringing more like real-time

**[17:33]** think about bringing more like real-time

**[17:33]** think about bringing more like real-time interactions via channels like SMS or

**[17:35]** interactions via channels like SMS or

**[17:35]** interactions via channels like SMS or push notifications rather than just

**[17:37]** push notifications rather than just

**[17:37]** push notifications rather than just browser based flows?

**[17:39]** browser based flows?

**[17:39]** browser based flows? And then a hot topic today, uh there's a

**[17:42]** And then a hot topic today, uh there's a

**[17:42]** And then a hot topic today, uh there's a bunch of interesting work going on in

**[17:43]** bunch of interesting work going on in

**[17:43]** bunch of interesting work going on in the voice voice track at at the

**[17:45]** the voice voice track at at the

**[17:45]** the voice voice track at at the conference. Uh as AI starts to interact

**[17:48]** conference. Uh as AI starts to interact

**[17:48]** conference. Uh as AI starts to interact with us via voice and video or

**[17:50]** with us via voice and video or

**[17:50]** with us via voice and video or completely in the background, how do we

**[17:52]** completely in the background, how do we

**[17:52]** completely in the background, how do we think about security in those respects?

**[17:54]** think about security in those respects?

**[17:54]** think about security in those respects? This is really the frontier of of

**[17:55]** This is really the frontier of of

**[17:55]** This is really the frontier of of security and inter interaction. But

**[17:57]** security and inter interaction. But

**[17:57]** security and inter interaction. But there's a lot of prior art in various

**[17:59]** there's a lot of prior art in various

**[17:59]** there's a lot of prior art in various real-time communities around SIP, XMPP,


### [18:00 - 19:00]

**[18:02]** real-time communities around SIP, XMPP,

**[18:02]** real-time communities around SIP, XMPP, XMPPP, WebRTC that uh I think is very

**[18:05]** XMPPP, WebRTC that uh I think is very

**[18:05]** XMPPP, WebRTC that uh I think is very interesting for us to all look at.

**[18:08]** interesting for us to all look at.

**[18:08]** interesting for us to all look at. So there's a lot here. Let's let's go

**[18:11]** So there's a lot here. Let's let's go

**[18:11]** So there's a lot here. Let's let's go build this stuff. It's all important for

**[18:12]** build this stuff. It's all important for

**[18:12]** build this stuff. It's all important for us uh to to achieve a safe and secure AI

**[18:17]** us uh to to achieve a safe and secure AI

**[18:17]** us uh to to achieve a safe and secure AI future. Uh this is what we're building

**[18:18]** future. Uh this is what we're building

**[18:18]** future. Uh this is what we're building at Keycard. Uh we're building an

**[18:20]** at Keycard. Uh we're building an

**[18:20]** at Keycard. Uh we're building an identity access management platform that

**[18:22]** identity access management platform that

**[18:22]** identity access management platform that lets you connect your co-pilots, custom

**[18:24]** lets you connect your co-pilots, custom

**[18:24]** lets you connect your co-pilots, custom agents, and thirdarty agents to all your

**[18:26]** agents, and thirdarty agents to all your

**[18:26]** agents, and thirdarty agents to all your apps, services, and infrastructure all

**[18:28]** apps, services, and infrastructure all

**[18:28]** apps, services, and infrastructure all using standards compliant protocols,

**[18:30]** using standards compliant protocols,

**[18:30]** using standards compliant protocols, ADA, MCP, and OOTH.

**[18:33]** ADA, MCP, and OOTH.

**[18:33]** ADA, MCP, and OOTH. If building this stuff is interesting to

**[18:34]** If building this stuff is interesting to

**[18:34]** If building this stuff is interesting to you, we are hiring hiring. So get in

**[18:36]** you, we are hiring hiring. So get in

**[18:36]** you, we are hiring hiring. So get in touch with me. And if you're if it's not

**[18:38]** touch with me. And if you're if it's not

**[18:38]** touch with me. And if you're if it's not interesting to you, but you know you

**[18:39]** interesting to you, but you know you

**[18:39]** interesting to you, but you know you want to secure your agents, get in touch

**[18:41]** want to secure your agents, get in touch

**[18:41]** want to secure your agents, get in touch with us, too. We're looking for partners

**[18:43]** with us, too. We're looking for partners

**[18:43]** with us, too. We're looking for partners that are building uh so that we can work

**[18:45]** that are building uh so that we can work

**[18:45]** that are building uh so that we can work with you to secure secure your agents.

**[18:47]** with you to secure secure your agents.

**[18:47]** with you to secure secure your agents. Uh the website site is keycard.ai and I

**[18:50]** Uh the website site is keycard.ai and I

**[18:50]** Uh the website site is keycard.ai and I will be around the rest of the

**[18:51]** will be around the rest of the

**[18:51]** will be around the rest of the conference. Thanks.


