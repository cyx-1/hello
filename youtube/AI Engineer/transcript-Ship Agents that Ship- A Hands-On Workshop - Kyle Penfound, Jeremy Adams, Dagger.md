# Ship Agents that Ship- A Hands-On Workshop - Kyle Penfound, Jeremy Adams, Dagger

**Video URL:** https://www.youtube.com/watch?v=Fzb1a24hF-o

---

## Full Transcript

### [00:00 - 01:00]

**[00:16]** Okay, we're going to kick this off. Uh

**[00:16]** Okay, we're going to kick this off. Uh we're trying to sort out some internet

**[00:19]** we're trying to sort out some internet

**[00:19]** we're trying to sort out some internet options here, but uh in the meantime,

**[00:21]** options here, but uh in the meantime,

**[00:21]** options here, but uh in the meantime, I'll uh give us our little intro. Um so,

**[00:24]** I'll uh give us our little intro. Um so,

**[00:24]** I'll uh give us our little intro. Um so, first of all, we're I'm Kyle. This is

**[00:26]** first of all, we're I'm Kyle. This is

**[00:26]** first of all, we're I'm Kyle. This is Jeremy. We're from Dagger. Uh, and

**[00:28]** Jeremy. We're from Dagger. Uh, and

**[00:28]** Jeremy. We're from Dagger. Uh, and you'll see more about what Dagger is

**[00:30]** you'll see more about what Dagger is

**[00:30]** you'll see more about what Dagger is through this workshop where we're going

**[00:32]** through this workshop where we're going

**[00:32]** through this workshop where we're going to build a cool uh, sweet agent and

**[00:35]** to build a cool uh, sweet agent and

**[00:35]** to build a cool uh, sweet agent and we're actually going to deploy it to

**[00:37]** we're actually going to deploy it to

**[00:37]** we're actually going to deploy it to GitHub. And so even like worst case

**[00:39]** GitHub. And so even like worst case

**[00:39]** GitHub. And so even like worst case scenario, if we can't get things running

**[00:41]** scenario, if we can't get things running

**[00:41]** scenario, if we can't get things running locally when we actually push things to

**[00:43]** locally when we actually push things to

**[00:43]** locally when we actually push things to GitHub and see agents running GitHub,

**[00:45]** GitHub and see agents running GitHub,

**[00:45]** GitHub and see agents running GitHub, then that's going to be out of our

**[00:47]** then that's going to be out of our

**[00:47]** then that's going to be out of our internet hands and it's all going to be

**[00:49]** internet hands and it's all going to be

**[00:49]** internet hands and it's all going to be really cool. So, uh, first of all, on

**[00:51]** really cool. So, uh, first of all, on

**[00:51]** really cool. So, uh, first of all, on the left side here, cool. Uh on the left

**[00:55]** the left side here, cool. Uh on the left

**[00:55]** the left side here, cool. Uh on the left side here we have kind of where we're

**[00:57]** side here we have kind of where we're

**[00:57]** side here we have kind of where we're getting started from. So this is the the


### [01:00 - 02:00]

**[01:00]** getting started from. So this is the the

**[01:00]** getting started from. So this is the the documentation site where we have uh

**[01:03]** documentation site where we have uh

**[01:03]** documentation site where we have uh install instructions. So I'll I'll walk

**[01:05]** install instructions. So I'll I'll walk

**[01:05]** install instructions. So I'll I'll walk through those real quick. Um and then

**[01:07]** through those real quick. Um and then

**[01:07]** through those real quick. Um and then our quick starts where we're actually

**[01:09]** our quick starts where we're actually

**[01:09]** our quick starts where we're actually going to walk through these as like the

**[01:10]** going to walk through these as like the

**[01:10]** going to walk through these as like the content of this workshop. Um and then

**[01:13]** content of this workshop. Um and then

**[01:14]** content of this workshop. Um and then also a shout out to uh tomorrow night we

**[01:16]** also a shout out to uh tomorrow night we

**[01:16]** also a shout out to uh tomorrow night we have a a hack night at the Cloudflare

**[01:18]** have a a hack night at the Cloudflare

**[01:18]** have a a hack night at the Cloudflare office. It's on the the um external

**[01:22]** office. It's on the the um external

**[01:22]** office. It's on the the um external events list for uh this conference as

**[01:25]** events list for uh this conference as

**[01:25]** events list for uh this conference as well. Um but here's a QR code for it.

**[01:30]** well. Um but here's a QR code for it.

**[01:30]** well. Um but here's a QR code for it. Um okay, so real quick.

**[01:34]** Um okay, so real quick.

**[01:34]** Um okay, so real quick. So there's a there's a there's a

**[01:36]** So there's a there's a there's a

**[01:36]** So there's a there's a there's a question about whether there's a Slack I

**[01:38]** question about whether there's a Slack I

**[01:38]** question about whether there's a Slack I think Slack for the workshop. Yes,

**[01:41]** think Slack for the workshop. Yes,

**[01:41]** think Slack for the workshop. Yes, absolutely. So, if you go to the Slack,

**[01:43]** absolutely. So, if you go to the Slack,

**[01:43]** absolutely. So, if you go to the Slack, there's it says dagger-workshop

**[01:51]** ship agents that ship is got it. Okay,

**[01:51]** ship agents that ship is got it. Okay, let me pull that up as well. So, if

**[01:53]** let me pull that up as well. So, if

**[01:53]** let me pull that up as well. So, if there's questions, put them in there or

**[01:55]** there's questions, put them in there or

**[01:55]** there's questions, put them in there or raise your hand and Jeremy will get to

**[01:57]** raise your hand and Jeremy will get to

**[01:57]** raise your hand and Jeremy will get to you. Climb over people. I will I will do


### [02:00 - 03:00]

**[02:00]** you. Climb over people. I will I will do

**[02:00]** you. Climb over people. I will I will do make it happen. Yes, I'll do my best.

**[02:03]** make it happen. Yes, I'll do my best.

**[02:03]** make it happen. Yes, I'll do my best. Awesome. So, um yeah, if if everyone if

**[02:06]** Awesome. So, um yeah, if if everyone if

**[02:06]** Awesome. So, um yeah, if if everyone if you're following along, awesome. If if

**[02:09]** you're following along, awesome. If if

**[02:09]** you're following along, awesome. If if you can't like because you don't have

**[02:11]** you can't like because you don't have

**[02:11]** you can't like because you don't have desk room or uh can't get the internet

**[02:13]** desk room or uh can't get the internet

**[02:13]** desk room or uh can't get the internet or whatever, I'm going to walk through

**[02:15]** or whatever, I'm going to walk through

**[02:15]** or whatever, I'm going to walk through it live because I already have

**[02:16]** it live because I already have

**[02:16]** it live because I already have everything on my machine. Um and then

**[02:19]** everything on my machine. Um and then

**[02:19]** everything on my machine. Um and then you can always uh you know check back

**[02:22]** you can always uh you know check back

**[02:22]** you can always uh you know check back with this later on once you have a a

**[02:24]** with this later on once you have a a

**[02:24]** with this later on once you have a a solid connection. Um so if you're not

**[02:26]** solid connection. Um so if you're not

**[02:26]** solid connection. Um so if you're not able to get out your computer or follow

**[02:27]** able to get out your computer or follow

**[02:28]** able to get out your computer or follow along, just watch me and I'll go through

**[02:29]** along, just watch me and I'll go through

**[02:29]** along, just watch me and I'll go through it and it's going to be really neat. Um

**[02:31]** it and it's going to be really neat. Um

**[02:31]** it and it's going to be really neat. Um but if you are following along, uh

**[02:33]** but if you are following along, uh

**[02:33]** but if you are following along, uh here's the installation page on uh

**[02:36]** here's the installation page on uh

**[02:36]** here's the installation page on uh docs.dagger.io IO. So you can install um

**[02:40]** docs.dagger.io IO. So you can install um

**[02:40]** docs.dagger.io IO. So you can install um from the homebrew tap or uh straight

**[02:43]** from the homebrew tap or uh straight

**[02:43]** from the homebrew tap or uh straight from our install script or with windget

**[02:47]** from our install script or with windget

**[02:47]** from our install script or with windget uh you can install the dagger cli. Um

**[02:50]** uh you can install the dagger cli. Um

**[02:50]** uh you can install the dagger cli. Um the only other dependency is that you

**[02:52]** the only other dependency is that you

**[02:52]** the only other dependency is that you need a container runtime such as docker

**[02:54]** need a container runtime such as docker

**[02:54]** need a container runtime such as docker or podman or uh nerdctl. So like

**[02:57]** or podman or uh nerdctl. So like

**[02:57]** or podman or uh nerdctl. So like anything that can run containers uh

**[02:59]** anything that can run containers uh

**[02:59]** anything that can run containers uh because dagger itself runs its engine as


### [03:00 - 04:00]

**[03:02]** because dagger itself runs its engine as

**[03:02]** because dagger itself runs its engine as a container and I'll explain what that

**[03:04]** a container and I'll explain what that

**[03:04]** a container and I'll explain what that means in a second. But, uh, if you're

**[03:05]** means in a second. But, uh, if you're

**[03:05]** means in a second. But, uh, if you're following along, get started on this

**[03:07]** following along, get started on this

**[03:07]** following along, get started on this while I talk through a bunch of stuff

**[03:09]** while I talk through a bunch of stuff

**[03:09]** while I talk through a bunch of stuff about what we're actually doing and

**[03:11]** about what we're actually doing and

**[03:11]** about what we're actually doing and what, um, all these technologies are

**[03:13]** what, um, all these technologies are

**[03:13]** what, um, all these technologies are trying to accomplish. So, I'll take I'll

**[03:15]** trying to accomplish. So, I'll take I'll

**[03:15]** trying to accomplish. So, I'll take I'll take I'll pause you really quick. Yeah,

**[03:17]** take I'll pause you really quick. Yeah,

**[03:17]** take I'll pause you really quick. Yeah, just for the for the folks on the tech

**[03:18]** just for the for the folks on the tech

**[03:18]** just for the for the folks on the tech team. Um, and so for some of you in the

**[03:21]** team. Um, and so for some of you in the

**[03:21]** team. Um, and so for some of you in the room, we're having we we're finding the

**[03:22]** room, we're having we we're finding the

**[03:22]** room, we're having we we're finding the Wi-Fi may or may not work for you. Use a

**[03:25]** Wi-Fi may or may not work for you. Use a

**[03:25]** Wi-Fi may or may not work for you. Use a hotspot if you got one. If that works

**[03:27]** hotspot if you got one. If that works

**[03:27]** hotspot if you got one. If that works down in the basement, you're then you're

**[03:29]** down in the basement, you're then you're

**[03:29]** down in the basement, you're then you're amazing. Also, I'm trying to do a little

**[03:31]** amazing. Also, I'm trying to do a little

**[03:31]** amazing. Also, I'm trying to do a little something through the wired connection

**[03:32]** something through the wired connection

**[03:32]** something through the wired connection here, but for the tech team, it's

**[03:35]** here, but for the tech team, it's

**[03:35]** here, but for the tech team, it's requiring a password for me to use this

**[03:38]** requiring a password for me to use this

**[03:38]** requiring a password for me to use this service. So, um anyway, if you have

**[03:41]** service. So, um anyway, if you have

**[03:41]** service. So, um anyway, if you have that, slip me a note at some point. Um

**[03:43]** that, slip me a note at some point. Um

**[03:43]** that, slip me a note at some point. Um but otherwise, yeah, we're working on

**[03:45]** but otherwise, yeah, we're working on

**[03:45]** but otherwise, yeah, we're working on we're working on getting more

**[03:47]** we're working on getting more

**[03:47]** we're working on getting more connectivity as we speak. Awesome.

**[03:51]** connectivity as we speak. Awesome.

**[03:51]** connectivity as we speak. Awesome. Yep. There we go. Uh so, the QR is

**[03:53]** Yep. There we go. Uh so, the QR is

**[03:53]** Yep. There we go. Uh so, the QR is actually for the the hack night tomorrow

**[03:55]** actually for the the hack night tomorrow

**[03:55]** actually for the the hack night tomorrow night. the um the docs and what we're

**[03:59]** night. the um the docs and what we're

**[03:59]** night. the um the docs and what we're going through are at docs.dagger.io.


### [04:00 - 05:00]

**[04:01]** going through are at docs.dagger.io.

**[04:01]** going through are at docs.dagger.io. Um so that's like the main content for

**[04:04]** Um so that's like the main content for

**[04:04]** Um so that's like the main content for what we're going to walk through. Um and

**[04:06]** what we're going to walk through. Um and

**[04:06]** what we're going to walk through. Um and I guess real quick we can intro as well.

**[04:08]** I guess real quick we can intro as well.

**[04:08]** I guess real quick we can intro as well. If you want to intro yourself first,

**[04:10]** If you want to intro yourself first,

**[04:10]** If you want to intro yourself first, Jeremy. Yeah, sure. I'm Jeremy Adams. I

**[04:12]** Jeremy. Yeah, sure. I'm Jeremy Adams. I

**[04:12]** Jeremy. Yeah, sure. I'm Jeremy Adams. I look after kind of the ecosystem. Uh I'm

**[04:16]** look after kind of the ecosystem. Uh I'm

**[04:16]** look after kind of the ecosystem. Uh I'm part of the ecosystem team that Kyle and

**[04:18]** part of the ecosystem team that Kyle and

**[04:18]** part of the ecosystem team that Kyle and I are both on and uh I've been at Dagger

**[04:23]** I are both on and uh I've been at Dagger

**[04:23]** I are both on and uh I've been at Dagger for a few years. And so I've got to see

**[04:25]** for a few years. And so I've got to see

**[04:25]** for a few years. And so I've got to see already a progression of folks using us

**[04:28]** already a progression of folks using us

**[04:28]** already a progression of folks using us for all sorts of things and most

**[04:30]** for all sorts of things and most

**[04:30]** for all sorts of things and most recently a lot around AI agent kind of

**[04:34]** recently a lot around AI agent kind of

**[04:34]** recently a lot around AI agent kind of workflows. Um but I love in this

**[04:36]** workflows. Um but I love in this

**[04:36]** workflows. Um but I love in this workshop we're going to blend together

**[04:38]** workshop we're going to blend together

**[04:38]** workshop we're going to blend together some of the classic use cases we've seen

**[04:39]** some of the classic use cases we've seen

**[04:39]** some of the classic use cases we've seen with Dagger around CI um and dev

**[04:43]** with Dagger around CI um and dev

**[04:43]** with Dagger around CI um and dev workflows as well as you know giving

**[04:46]** workflows as well as you know giving

**[04:46]** workflows as well as you know giving those to agents. Awesome. Yeah. I'm I'm

**[04:49]** those to agents. Awesome. Yeah. I'm I'm

**[04:49]** those to agents. Awesome. Yeah. I'm I'm Kyle. Um I'm on the same team. Yeah. Um

**[04:51]** Kyle. Um I'm on the same team. Yeah. Um

**[04:52]** Kyle. Um I'm on the same team. Yeah. Um and I have a background in like DevOps

**[04:53]** and I have a background in like DevOps

**[04:54]** and I have a background in like DevOps and platform engineering. Uh so much

**[04:55]** and platform engineering. Uh so much

**[04:56]** and platform engineering. Uh so much more on the the kind of cloud infra side

**[04:59]** more on the the kind of cloud infra side

**[04:59]** more on the the kind of cloud infra side of things versus um that building side.


### [05:00 - 06:00]

**[05:02]** of things versus um that building side.

**[05:02]** of things versus um that building side. So it's cool to come at this from uh

**[05:05]** So it's cool to come at this from uh

**[05:05]** So it's cool to come at this from uh that perspective of you know trying to

**[05:07]** that perspective of you know trying to

**[05:07]** that perspective of you know trying to deploy agents somewhere and and make

**[05:09]** deploy agents somewhere and and make

**[05:09]** deploy agents somewhere and and make things work. And that's why in this

**[05:11]** things work. And that's why in this

**[05:11]** things work. And that's why in this workshop we're going to deploy things to

**[05:13]** workshop we're going to deploy things to

**[05:13]** workshop we're going to deploy things to GitHub because that's uh eventually what

**[05:16]** GitHub because that's uh eventually what

**[05:16]** GitHub because that's uh eventually what you're going to want to do when you

**[05:17]** you're going to want to do when you

**[05:17]** you're going to want to do when you build an agent. You have to put it

**[05:18]** build an agent. You have to put it

**[05:18]** build an agent. You have to put it somewhere to run it. uh can't just live

**[05:20]** somewhere to run it. uh can't just live

**[05:20]** somewhere to run it. uh can't just live on your machine all the time. Uh I guess

**[05:22]** on your machine all the time. Uh I guess

**[05:22]** on your machine all the time. Uh I guess depending on what agent is. Anyway, um

**[05:24]** depending on what agent is. Anyway, um

**[05:24]** depending on what agent is. Anyway, um so if if you made it this far, you've

**[05:26]** so if if you made it this far, you've

**[05:26]** so if if you made it this far, you've made it to the docs, uh then we're going

**[05:29]** made it to the docs, uh then we're going

**[05:30]** made it to the docs, uh then we're going to talk a bit about what Dagger is and

**[05:32]** to talk a bit about what Dagger is and

**[05:32]** to talk a bit about what Dagger is and why we're building agents with it. Um

**[05:34]** why we're building agents with it. Um

**[05:34]** why we're building agents with it. Um and so basically Dagger is like I said,

**[05:37]** and so basically Dagger is like I said,

**[05:37]** and so basically Dagger is like I said, it's a container runtime. It's a

**[05:40]** it's a container runtime. It's a

**[05:40]** it's a container runtime. It's a workflow engine. And so people have

**[05:43]** workflow engine. And so people have

**[05:43]** workflow engine. And so people have historically done things like build

**[05:44]** historically done things like build

**[05:44]** historically done things like build their CI/CD with Dagger because you're

**[05:46]** their CI/CD with Dagger because you're

**[05:46]** their CI/CD with Dagger because you're building these pipelines that

**[05:48]** building these pipelines that

**[05:48]** building these pipelines that orchestrate containers, run all these

**[05:50]** orchestrate containers, run all these

**[05:50]** orchestrate containers, run all these tasks. Uh, and it runs the same on your

**[05:53]** tasks. Uh, and it runs the same on your

**[05:53]** tasks. Uh, and it runs the same on your machine as it runs in any cloud like in

**[05:56]** machine as it runs in any cloud like in

**[05:56]** machine as it runs in any cloud like in um, you know, in your Kubernetes, in

**[05:59]** um, you know, in your Kubernetes, in

**[05:59]** um, you know, in your Kubernetes, in GitHub, wherever your CI might run, but


### [06:00 - 07:00]

**[06:01]** GitHub, wherever your CI might run, but

**[06:01]** GitHub, wherever your CI might run, but it runs the same everywhere. So you're

**[06:03]** it runs the same everywhere. So you're

**[06:03]** it runs the same everywhere. So you're making these workflows. U, and the cool

**[06:05]** making these workflows. U, and the cool

**[06:05]** making these workflows. U, and the cool thing is that's also what agents are,

**[06:07]** thing is that's also what agents are,

**[06:08]** thing is that's also what agents are, right? is that they're they're just

**[06:09]** right? is that they're they're just

**[06:09]** right? is that they're they're just these processes where we have um we have

**[06:15]** these processes where we have um we have

**[06:15]** these processes where we have um we have a bunch of tools we want to give to an

**[06:16]** a bunch of tools we want to give to an

**[06:16]** a bunch of tools we want to give to an agent. Um anyway, okay, we're we're

**[06:18]** agent. Um anyway, okay, we're we're

**[06:18]** agent. Um anyway, okay, we're we're going to see in action. Um and so uh

**[06:22]** going to see in action. Um and so uh

**[06:22]** going to see in action. Um and so uh let's see, we have components, right?

**[06:24]** let's see, we have components, right?

**[06:24]** let's see, we have components, right? So, Dagger itself is made up of uh core

**[06:28]** So, Dagger itself is made up of uh core

**[06:28]** So, Dagger itself is made up of uh core components like containers like I said

**[06:30]** components like containers like I said

**[06:30]** components like containers like I said also repos directories files and now LMS

**[06:34]** also repos directories files and now LMS

**[06:34]** also repos directories files and now LMS are also a component that you have to

**[06:36]** are also a component that you have to

**[06:36]** are also a component that you have to work with uh within this kind of toolbox

**[06:38]** work with uh within this kind of toolbox

**[06:38]** work with uh within this kind of toolbox of Dagger and how we're building things

**[06:41]** of Dagger and how we're building things

**[06:41]** of Dagger and how we're building things and so it's just another building block

**[06:42]** and so it's just another building block

**[06:42]** and so it's just another building block right it's not uh a framework special

**[06:45]** right it's not uh a framework special

**[06:45]** right it's not uh a framework special like just build for making an agent then

**[06:47]** like just build for making an agent then

**[06:47]** like just build for making an agent then you have it living next to your software

**[06:49]** you have it living next to your software

**[06:49]** you have it living next to your software it's another component within your

**[06:51]** it's another component within your

**[06:51]** it's another component within your toolbox and so you're bringing LMS into

**[06:53]** toolbox and so you're bringing LMS into

**[06:53]** toolbox and so you're bringing LMS into these existing workflow those um and

**[06:56]** these existing workflow those um and

**[06:56]** these existing workflow those um and that's why it's a little bit different.

**[06:58]** that's why it's a little bit different.

**[06:58]** that's why it's a little bit different. Yeah, you could think another way of


### [07:00 - 08:00]

**[07:00]** Yeah, you could think another way of

**[07:00]** Yeah, you could think another way of thinking about Dagger in a nutshell is

**[07:02]** thinking about Dagger in a nutshell is

**[07:02]** thinking about Dagger in a nutshell is Dagger's for software engineering

**[07:04]** Dagger's for software engineering

**[07:04]** Dagger's for software engineering workflows and environments. So you're

**[07:07]** workflows and environments. So you're

**[07:07]** workflows and environments. So you're going to see us building some

**[07:09]** going to see us building some

**[07:09]** going to see us building some environments essentially some

**[07:10]** environments essentially some

**[07:10]** environments essentially some containerized environments with some

**[07:12]** containerized environments with some

**[07:12]** containerized environments with some functions and all of these things can

**[07:14]** functions and all of these things can

**[07:14]** functions and all of these things can become tools that you know human

**[07:17]** become tools that you know human

**[07:17]** become tools that you know human software engineers uh AI agents um use

**[07:21]** software engineers uh AI agents um use

**[07:21]** software engineers uh AI agents um use for both development side as well as uh

**[07:25]** for both development side as well as uh

**[07:25]** for both development side as well as uh app delivery side of things. So you'll

**[07:27]** app delivery side of things. So you'll

**[07:27]** app delivery side of things. So you'll see that kind of of course these these

**[07:28]** see that kind of of course these these

**[07:28]** see that kind of of course these these areas are all blending and kind of

**[07:30]** areas are all blending and kind of

**[07:30]** areas are all blending and kind of squishing together right now. We're

**[07:32]** squishing together right now. We're

**[07:32]** squishing together right now. We're seeing all this stuff happen in in real

**[07:33]** seeing all this stuff happen in in real

**[07:33]** seeing all this stuff happen in in real time. So, Dagger is kind of uh gonna be

**[07:36]** time. So, Dagger is kind of uh gonna be

**[07:36]** time. So, Dagger is kind of uh gonna be one tool that you could use for that

**[07:37]** one tool that you could use for that

**[07:38]** one tool that you could use for that whole range. You say you explain Dagger

**[07:40]** whole range. You say you explain Dagger

**[07:40]** whole range. You say you explain Dagger as a tool to build containerized

**[07:42]** as a tool to build containerized

**[07:42]** as a tool to build containerized environments. What's the what's the

**[07:44]** environments. What's the what's the

**[07:44]** environments. What's the what's the distinction between?

**[07:46]** distinction between?

**[07:46]** distinction between? Yeah. So, the question was uh if Dagger

**[07:49]** Yeah. So, the question was uh if Dagger

**[07:49]** Yeah. So, the question was uh if Dagger is a tool to build containerized

**[07:50]** is a tool to build containerized

**[07:50]** is a tool to build containerized environments, what's the distinction

**[07:51]** environments, what's the distinction

**[07:52]** environments, what's the distinction between Dagger and Docker? So, yeah,

**[07:54]** between Dagger and Docker? So, yeah,

**[07:54]** between Dagger and Docker? So, yeah, Docker has been around for a long time

**[07:56]** Docker has been around for a long time

**[07:56]** Docker has been around for a long time and in fact the founders of Docker are

**[07:58]** and in fact the founders of Docker are

**[07:58]** and in fact the founders of Docker are the founders of Dagger. And so we could


### [08:00 - 09:00]

**[08:01]** the founders of Dagger. And so we could

**[08:01]** the founders of Dagger. And so we could think about the scope of the original

**[08:03]** think about the scope of the original

**[08:03]** think about the scope of the original scope of Docker was really about

**[08:04]** scope of Docker was really about

**[08:04]** scope of Docker was really about containerizing an application and making

**[08:06]** containerizing an application and making

**[08:06]** containerizing an application and making that thing portable. So I can run in my

**[08:08]** that thing portable. So I can run in my

**[08:08]** that thing portable. So I can run in my laptop or Kyle's or up in Kubernetes or

**[08:11]** laptop or Kyle's or up in Kubernetes or

**[08:11]** laptop or Kyle's or up in Kubernetes or anywhere. So now what we're doing is

**[08:12]** anywhere. So now what we're doing is

**[08:12]** anywhere. So now what we're doing is we're taking a whole workflow and making

**[08:14]** we're taking a whole workflow and making

**[08:14]** we're taking a whole workflow and making that a portable thing.

**[08:17]** that a portable thing.

**[08:17]** that a portable thing. So yeah, there's definitely multiple

**[08:19]** So yeah, there's definitely multiple

**[08:19]** So yeah, there's definitely multiple containers and other types of objects,

**[08:22]** containers and other types of objects,

**[08:22]** containers and other types of objects, but everything's everything's sandboxed

**[08:24]** but everything's everything's sandboxed

**[08:24]** but everything's everything's sandboxed by default. So you get So yeah, and

**[08:26]** by default. So you get So yeah, and

**[08:26]** by default. So you get So yeah, and we'll see as we get into it. Great

**[08:27]** we'll see as we get into it. Great

**[08:27]** we'll see as we get into it. Great question. Yeah. So we we're we're

**[08:30]** question. Yeah. So we we're we're

**[08:30]** question. Yeah. So we we're we're writing code that is workflows itself.

**[08:32]** writing code that is workflows itself.

**[08:32]** writing code that is workflows itself. So that code can be Go, Python,

**[08:34]** So that code can be Go, Python,

**[08:34]** So that code can be Go, Python, TypeScript, Java, PHP. We have all these

**[08:36]** TypeScript, Java, PHP. We have all these

**[08:36]** TypeScript, Java, PHP. We have all these different languages you can write with.

**[08:38]** different languages you can write with.

**[08:38]** different languages you can write with. Um and the cool thing is that you're not

**[08:41]** Um and the cool thing is that you're not

**[08:41]** Um and the cool thing is that you're not kind of choosing your language for

**[08:43]** kind of choosing your language for

**[08:43]** kind of choosing your language for Dagger and then that's the world you

**[08:45]** Dagger and then that's the world you

**[08:45]** Dagger and then that's the world you live in. Um Dagger has this cross

**[08:47]** live in. Um Dagger has this cross

**[08:47]** live in. Um Dagger has this cross language interop. So if I write a cool

**[08:49]** language interop. So if I write a cool

**[08:49]** language interop. So if I write a cool Dagger module um with Oh, it's it's

**[08:53]** Dagger module um with Oh, it's it's

**[08:53]** Dagger module um with Oh, it's it's going to want to load. That's why I have

**[08:54]** going to want to load. That's why I have

**[08:54]** going to want to load. That's why I have it. Oh, you're amazing. Yeah. Yeah. uh

**[08:57]** it. Oh, you're amazing. Yeah. Yeah. uh

**[08:57]** it. Oh, you're amazing. Yeah. Yeah. uh error occurred. That's Wow. Okay. Um


### [09:00 - 10:00]

**[09:01]** error occurred. That's Wow. Okay. Um

**[09:01]** error occurred. That's Wow. Okay. Um Oh, no. Okay.

**[09:03]** Oh, no. Okay.

**[09:03]** Oh, no. Okay. So, um I broke it. If I write a cool

**[09:06]** So, um I broke it. If I write a cool

**[09:06]** So, um I broke it. If I write a cool module with Dagger that say does like uh

**[09:09]** module with Dagger that say does like uh

**[09:09]** module with Dagger that say does like uh TypeScript build or something, right? Um

**[09:12]** TypeScript build or something, right? Um

**[09:12]** TypeScript build or something, right? Um I I can share this on the Daggerverse

**[09:14]** I I can share this on the Daggerverse

**[09:14]** I I can share this on the Daggerverse and maybe I wrote that module in

**[09:16]** and maybe I wrote that module in

**[09:16]** and maybe I wrote that module in Typescript and you're writing your

**[09:18]** Typescript and you're writing your

**[09:18]** Typescript and you're writing your modules in uh Python. you can just

**[09:22]** modules in uh Python. you can just

**[09:22]** modules in uh Python. you can just install my module and you have these uh

**[09:23]** install my module and you have these uh

**[09:24]** install my module and you have these uh native bindings in your language uh to

**[09:25]** native bindings in your language uh to

**[09:26]** native bindings in your language uh to work with Dagger modules across

**[09:27]** work with Dagger modules across

**[09:27]** work with Dagger modules across language. So anyway, that's that's my

**[09:29]** language. So anyway, that's that's my

**[09:29]** language. So anyway, that's that's my point in that we're not when you pick a

**[09:31]** point in that we're not when you pick a

**[09:31]** point in that we're not when you pick a language, you still get to benefit from

**[09:32]** language, you still get to benefit from

**[09:32]** language, you still get to benefit from the whole Dagger ecosystem.

**[09:35]** the whole Dagger ecosystem.

**[09:35]** the whole Dagger ecosystem. Um and we don't have images on these.

**[09:38]** Um and we don't have images on these.

**[09:38]** Um and we don't have images on these. That's okay. There's some sweet

**[09:39]** That's okay. There's some sweet

**[09:39]** That's okay. There's some sweet animations there of like happening. It's

**[09:42]** animations there of like happening. It's

**[09:42]** animations there of like happening. It's so cool. Yeah, like the coolest

**[09:43]** so cool. Yeah, like the coolest

**[09:43]** so cool. Yeah, like the coolest animation you could think of. Um

**[09:46]** animation you could think of. Um

**[09:46]** animation you could think of. Um awesome. So I think we could probably

**[09:47]** awesome. So I think we could probably

**[09:47]** awesome. So I think we could probably skip forward here. Yeah. Um, and so, uh,

**[09:51]** skip forward here. Yeah. Um, and so, uh,

**[09:52]** skip forward here. Yeah. Um, and so, uh, hopefully we we've installed or we're

**[09:53]** hopefully we we've installed or we're

**[09:53]** hopefully we we've installed or we're downloading or maybe we're still

**[09:54]** downloading or maybe we're still

**[09:54]** downloading or maybe we're still downloading, um, Dagger. Uh, so I'll run

**[09:57]** downloading, um, Dagger. Uh, so I'll run

**[09:57]** downloading, um, Dagger. Uh, so I'll run through real quick, um, kind of the


### [10:00 - 11:00]

**[10:00]** through real quick, um, kind of the

**[10:00]** through real quick, um, kind of the basics of Dagger. So, hopefully that's

**[10:01]** basics of Dagger. So, hopefully that's

**[10:01]** basics of Dagger. So, hopefully that's big enough. Maybe I'll make it a bit

**[10:02]** big enough. Maybe I'll make it a bit

**[10:02]** big enough. Maybe I'll make it a bit bigger. Yeah, that's good.

**[10:05]** bigger. Yeah, that's good.

**[10:05]** bigger. Yeah, that's good. Um, there we go. Yeah. Cool. So, we've

**[10:09]** Um, there we go. Yeah. Cool. So, we've

**[10:09]** Um, there we go. Yeah. Cool. So, we've uh we've installed Dagger. We've got

**[10:11]** uh we've installed Dagger. We've got

**[10:11]** uh we've installed Dagger. We've got these things uh like uh container

**[10:13]** these things uh like uh container

**[10:13]** these things uh like uh container runtime somewhere. Um, and so the first

**[10:15]** runtime somewhere. Um, and so the first

**[10:16]** runtime somewhere. Um, and so the first thing we can do is create containers. So

**[10:17]** thing we can do is create containers. So

**[10:17]** thing we can do is create containers. So if I'm in dagger shell, which I think I

**[10:20]** if I'm in dagger shell, which I think I

**[10:20]** if I'm in dagger shell, which I think I am over here,

**[10:23]** am over here,

**[10:23]** am over here, that's definitely going to get bigger.

**[10:25]** that's definitely going to get bigger.

**[10:25]** that's definitely going to get bigger. Yeah. Yeah.

**[10:31]** So I'm in digger shell and I can say

**[10:31]** So I'm in digger shell and I can say container I think. I don't know.

**[10:42]** Let's go over here.

**[10:42]** Let's go over here. Fighting the internet.

**[10:51]** And so what Kyle's showing is there's

**[10:51]** And so what Kyle's showing is there's like a few different ways of using

**[10:53]** like a few different ways of using

**[10:54]** like a few different ways of using Dagger and you uh on the command line

**[10:56]** Dagger and you uh on the command line

**[10:56]** Dagger and you uh on the command line and um including kind of a

**[10:58]** and um including kind of a

**[10:58]** and um including kind of a non-interactive just fire off a Dagger


### [11:00 - 12:00]

**[11:00]** non-interactive just fire off a Dagger

**[11:00]** non-interactive just fire off a Dagger command to run one of these workflows a

**[11:02]** command to run one of these workflows a

**[11:02]** command to run one of these workflows a function that's one of these workflows

**[11:04]** function that's one of these workflows

**[11:04]** function that's one of these workflows or you can use it in this kind of

**[11:05]** or you can use it in this kind of

**[11:05]** or you can use it in this kind of interactive shell mode that he's showing

**[11:07]** interactive shell mode that he's showing

**[11:07]** interactive shell mode that he's showing here. Yeah. And it's all it's all about

**[11:09]** here. Yeah. And it's all it's all about

**[11:09]** here. Yeah. And it's all it's all about building building blocks right. So like

**[11:10]** building building blocks right. So like

**[11:10]** building building blocks right. So like with the basics of Dagger, you have like

**[11:13]** with the basics of Dagger, you have like

**[11:13]** with the basics of Dagger, you have like I mentioned earlier things like

**[11:14]** I mentioned earlier things like

**[11:14]** I mentioned earlier things like containers, directories, LLMs. Uh but

**[11:17]** containers, directories, LLMs. Uh but

**[11:17]** containers, directories, LLMs. Uh but with our code, we're actually going to

**[11:18]** with our code, we're actually going to

**[11:18]** with our code, we're actually going to be building larger blocks out of those

**[11:20]** be building larger blocks out of those

**[11:20]** be building larger blocks out of those blocks uh to assemble like an actual

**[11:22]** blocks uh to assemble like an actual

**[11:22]** blocks uh to assemble like an actual like part of a workflow and then I'll

**[11:24]** like part of a workflow and then I'll

**[11:24]** like part of a workflow and then I'll take those blocks, build bigger

**[11:26]** take those blocks, build bigger

**[11:26]** take those blocks, build bigger workflows out of those. So as as we're

**[11:27]** workflows out of those. So as as we're

**[11:27]** workflows out of those. So as as we're using shell, we're always going to be

**[11:29]** using shell, we're always going to be

**[11:29]** using shell, we're always going to be interacting with some level of a

**[11:31]** interacting with some level of a

**[11:31]** interacting with some level of a workflow here. about like with container

**[11:33]** workflow here. about like with container

**[11:33]** workflow here. about like with container I can say from uh Alpine and now I've

**[11:36]** I can say from uh Alpine and now I've

**[11:36]** I can say from uh Alpine and now I've got an Alpine container and I can get uh

**[11:41]** got an Alpine container and I can get uh

**[11:41]** got an Alpine container and I can get uh we can do things with that like anything

**[11:43]** we can do things with that like anything

**[11:44]** we can do things with that like anything you might want to do with a container

**[11:46]** you might want to do with a container

**[11:46]** you might want to do with a container right so I could literally say uh give

**[11:48]** right so I could literally say uh give

**[11:48]** right so I could literally say uh give me a terminal and now I've got a

**[11:50]** me a terminal and now I've got a

**[11:50]** me a terminal and now I've got a terminal in a container uh and this is

**[11:52]** terminal in a container uh and this is

**[11:52]** terminal in a container uh and this is the exact kind of tools that we're

**[11:53]** the exact kind of tools that we're

**[11:53]** the exact kind of tools that we're actually giving to our agent as we're

**[11:55]** actually giving to our agent as we're

**[11:55]** actually giving to our agent as we're building these pipelines right so it can

**[11:57]** building these pipelines right so it can

**[11:57]** building these pipelines right so it can you can give it a container but you can

**[11:59]** you can give it a container but you can

**[11:59]** you can give it a container but you can build a specialized workspace


### [12:00 - 13:00]

**[12:01]** build a specialized workspace

**[12:01]** build a specialized workspace for your agent to do things like write

**[12:04]** for your agent to do things like write

**[12:04]** for your agent to do things like write the code. Uh so it's a lot of setup to

**[12:06]** the code. Uh so it's a lot of setup to

**[12:06]** the code. Uh so it's a lot of setup to say that we've got all these these

**[12:08]** say that we've got all these these

**[12:08]** say that we've got all these these primitives that we can give to agents to

**[12:11]** primitives that we can give to agents to

**[12:11]** primitives that we can give to agents to build some really effective software

**[12:13]** build some really effective software

**[12:13]** build some really effective software engineering agents uh by giving them the

**[12:15]** engineering agents uh by giving them the

**[12:15]** engineering agents uh by giving them the exact tools they need to complete the

**[12:17]** exact tools they need to complete the

**[12:17]** exact tools they need to complete the job. Um but also like we mentioned uh

**[12:20]** job. Um but also like we mentioned uh

**[12:20]** job. Um but also like we mentioned uh earlier people use Dagger for CI/CD

**[12:23]** earlier people use Dagger for CI/CD

**[12:23]** earlier people use Dagger for CI/CD because you can create these workflows

**[12:24]** because you can create these workflows

**[12:24]** because you can create these workflows for you know running your tests for your

**[12:26]** for you know running your tests for your

**[12:26]** for you know running your tests for your application or whatever. And the cool

**[12:28]** application or whatever. And the cool

**[12:28]** application or whatever. And the cool thing is that if you've done that, you

**[12:30]** thing is that if you've done that, you

**[12:30]** thing is that if you've done that, you can take that same code that you wrote

**[12:31]** can take that same code that you wrote

**[12:31]** can take that same code that you wrote for running your tests and give that to

**[12:33]** for running your tests and give that to

**[12:33]** for running your tests and give that to your agent. So now your agent isn't just

**[12:35]** your agent. So now your agent isn't just

**[12:35]** your agent. So now your agent isn't just guessing at some code that it's

**[12:36]** guessing at some code that it's

**[12:36]** guessing at some code that it's generating, but it can actually run your

**[12:38]** generating, but it can actually run your

**[12:38]** generating, but it can actually run your actual test the same way that your

**[12:39]** actual test the same way that your

**[12:39]** actual test the same way that your developers and your CI do uh to make

**[12:41]** developers and your CI do uh to make

**[12:41]** developers and your CI do uh to make sure that the code it's generating is

**[12:44]** sure that the code it's generating is

**[12:44]** sure that the code it's generating is valid code and that can it can iterate

**[12:46]** valid code and that can it can iterate

**[12:46]** valid code and that can it can iterate on these things within the agent. So

**[12:48]** on these things within the agent. So

**[12:48]** on these things within the agent. So this is all we're going to build right

**[12:49]** this is all we're going to build right

**[12:49]** this is all we're going to build right now. And we were just talking to

**[12:51]** now. And we were just talking to

**[12:51]** now. And we were just talking to somebody outside before the session uh

**[12:53]** somebody outside before the session uh

**[12:53]** somebody outside before the session uh who was telling us that in in his

**[12:56]** who was telling us that in in his

**[12:56]** who was telling us that in in his organization

**[12:58]** organization

**[12:58]** organization they get uh you know not infrequently


### [13:00 - 14:00]

**[13:01]** they get uh you know not infrequently

**[13:01]** they get uh you know not infrequently now because of people like a product

**[13:03]** now because of people like a product

**[13:03]** now because of people like a product manager who's discovered vibe coding or

**[13:07]** manager who's discovered vibe coding or

**[13:07]** manager who's discovered vibe coding or a team that's using uh you know AI

**[13:10]** a team that's using uh you know AI

**[13:10]** a team that's using uh you know AI powered idees or whatever that people

**[13:13]** powered idees or whatever that people

**[13:13]** powered idees or whatever that people are like cranking out these like massive

**[13:15]** are like cranking out these like massive

**[13:15]** are like cranking out these like massive PRs for him to review like 25,000 line

**[13:19]** PRs for him to review like 25,000 line

**[13:19]** PRs for him to review like 25,000 line PR RS and like and the PRs don't even

**[13:22]** PR RS and like and the PRs don't even

**[13:22]** PR RS and like and the PRs don't even stay static. So he was like he's like oh

**[13:23]** stay static. So he was like he's like oh

**[13:24]** stay static. So he was like he's like oh I just got this PR and I have to review

**[13:26]** I just got this PR and I have to review

**[13:26]** I just got this PR and I have to review it and then like I come back and now

**[13:27]** it and then like I come back and now

**[13:27]** it and then like I come back and now there's five more commits on it that

**[13:29]** there's five more commits on it that

**[13:29]** there's five more commits on it that like you know and so you've got this

**[13:31]** like you know and so you've got this

**[13:32]** like you know and so you've got this thrash happening and so part of what the

**[13:35]** thrash happening and so part of what the

**[13:35]** thrash happening and so part of what the reason why CI and AI bringing that

**[13:38]** reason why CI and AI bringing that

**[13:38]** reason why CI and AI bringing that together makes so much sense is we

**[13:40]** together makes so much sense is we

**[13:40]** together makes so much sense is we actually have to bring some some balance

**[13:42]** actually have to bring some some balance

**[13:42]** actually have to bring some some balance back. you know, we got this fire hose.

**[13:45]** back. you know, we got this fire hose.

**[13:45]** back. you know, we got this fire hose. We can all now just create so much code,

**[13:48]** We can all now just create so much code,

**[13:48]** We can all now just create so much code, but how do we make sure this is actually

**[13:49]** but how do we make sure this is actually

**[13:49]** but how do we make sure this is actually code that we can test and that we can

**[13:52]** code that we can test and that we can

**[13:52]** code that we can test and that we can deploy with some kind of confidence at

**[13:54]** deploy with some kind of confidence at

**[13:54]** deploy with some kind of confidence at some point? So, we need to balance out

**[13:55]** some point? So, we need to balance out

**[13:55]** some point? So, we need to balance out and make sure that there's uh software

**[13:57]** and make sure that there's uh software

**[13:58]** and make sure that there's uh software delivery workflows that are there to to


### [14:00 - 15:00]

**[14:01]** delivery workflows that are there to to

**[14:01]** delivery workflows that are there to to test and build and validate things

**[14:03]** test and build and validate things

**[14:03]** test and build and validate things before we put them out in production.

**[14:05]** before we put them out in production.

**[14:05]** before we put them out in production. So, some of what we'll get into today.

**[14:08]** So, some of what we'll get into today.

**[14:08]** So, some of what we'll get into today. Awesome. So, yeah, let's actually get

**[14:09]** Awesome. So, yeah, let's actually get

**[14:09]** Awesome. So, yeah, let's actually get into writing something. So, zoomed out a

**[14:11]** into writing something. So, zoomed out a

**[14:11]** into writing something. So, zoomed out a bit so you can see where I landed in the

**[14:13]** bit so you can see where I landed in the

**[14:13]** bit so you can see where I landed in the docs. Here on the left side, we have

**[14:14]** docs. Here on the left side, we have

**[14:14]** docs. Here on the left side, we have quick start and I clicked on build a CI

**[14:17]** quick start and I clicked on build a CI

**[14:17]** quick start and I clicked on build a CI pipeline. And that's basically to get us

**[14:20]** pipeline. And that's basically to get us

**[14:20]** pipeline. And that's basically to get us to a point where we have a project or

**[14:22]** to a point where we have a project or

**[14:22]** to a point where we have a project or we're going to make an agent inside of

**[14:24]** we're going to make an agent inside of

**[14:24]** we're going to make an agent inside of that that can build new features for

**[14:25]** that that can build new features for

**[14:25]** that that can build new features for that project. Uh, so it's just going to

**[14:27]** that project. Uh, so it's just going to

**[14:27]** that project. Uh, so it's just going to be a real quick thing where we kind of

**[14:28]** be a real quick thing where we kind of

**[14:28]** be a real quick thing where we kind of set up this uh example project with

**[14:32]** set up this uh example project with

**[14:32]** set up this uh example project with functions that know how to build and

**[14:34]** functions that know how to build and

**[14:34]** functions that know how to build and test the project. Um, so I'm on this

**[14:36]** test the project. Um, so I'm on this

**[14:36]** test the project. Um, so I'm on this page and we've already talked through

**[14:39]** page and we've already talked through

**[14:39]** page and we've already talked through installing Dagger. Uh, and we talked a

**[14:41]** installing Dagger. Uh, and we talked a

**[14:41]** installing Dagger. Uh, and we talked a bit through the basics. Um, so now we

**[14:43]** bit through the basics. Um, so now we

**[14:43]** bit through the basics. Um, so now we have this example application called

**[14:45]** have this example application called

**[14:45]** have this example application called Hello Dagger template. And if you go to

**[14:47]** Hello Dagger template. And if you go to

**[14:47]** Hello Dagger template. And if you go to GitHub and say use this template, uh,

**[14:51]** GitHub and say use this template, uh,

**[14:51]** GitHub and say use this template, uh, you can name it whatever you want like

**[14:52]** you can name it whatever you want like

**[14:52]** you can name it whatever you want like Hello Dagger Workshop or just Hello

**[14:54]** Hello Dagger Workshop or just Hello

**[14:54]** Hello Dagger Workshop or just Hello Dagger, doesn't matter. Uh, you can

**[14:56]** Dagger, doesn't matter. Uh, you can

**[14:56]** Dagger, doesn't matter. Uh, you can create a a repo in your GitHub from this

**[14:59]** create a a repo in your GitHub from this

**[14:59]** create a a repo in your GitHub from this template. And the important reason for


### [15:00 - 16:00]

**[15:01]** template. And the important reason for

**[15:01]** template. And the important reason for that versus cloning it is that that's

**[15:03]** that versus cloning it is that that's

**[15:03]** that versus cloning it is that that's going to make it way easier when we

**[15:04]** going to make it way easier when we

**[15:04]** going to make it way easier when we actually push things to GitHub in a

**[15:06]** actually push things to GitHub in a

**[15:06]** actually push things to GitHub in a little bit uh to make it easier for you

**[15:08]** little bit uh to make it easier for you

**[15:08]** little bit uh to make it easier for you to uh run the GitHub actions that

**[15:10]** to uh run the GitHub actions that

**[15:10]** to uh run the GitHub actions that actually run the agent. Um, so we're

**[15:13]** actually run the agent. Um, so we're

**[15:13]** actually run the agent. Um, so we're going to use that template and I've done

**[15:15]** going to use that template and I've done

**[15:15]** going to use that template and I've done that over here

**[15:18]** that over here

**[15:18]** that over here in this repo where I have my Hello

**[15:21]** in this repo where I have my Hello

**[15:21]** in this repo where I have my Hello Dagger Pi. Uh, because I've done this in

**[15:24]** Dagger Pi. Uh, because I've done this in

**[15:24]** Dagger Pi. Uh, because I've done this in every language. U, you can use whatever

**[15:26]** every language. U, you can use whatever

**[15:26]** every language. U, you can use whatever language you want to use. U, I'll be

**[15:28]** language you want to use. U, I'll be

**[15:28]** language you want to use. U, I'll be walking through Python today because I

**[15:30]** walking through Python today because I

**[15:30]** walking through Python today because I think that's probably what a lot of

**[15:31]** think that's probably what a lot of

**[15:31]** think that's probably what a lot of people uh, here today are most

**[15:33]** people uh, here today are most

**[15:33]** people uh, here today are most comfortable with. Um, but if you're not,

**[15:36]** comfortable with. Um, but if you're not,

**[15:36]** comfortable with. Um, but if you're not, I can switch between languages. Just

**[15:38]** I can switch between languages. Just

**[15:38]** I can switch between languages. Just raise your hand and say, "Show me go."

**[15:40]** raise your hand and say, "Show me go."

**[15:40]** raise your hand and say, "Show me go." Um, that's okay. So

**[15:43]** Um, that's okay. So

**[15:43]** Um, that's okay. So I've got let's see. So I've got this

**[15:46]** I've got let's see. So I've got this

**[15:46]** I've got let's see. So I've got this application in my GitHub now. I've

**[15:49]** application in my GitHub now. I've

**[15:49]** application in my GitHub now. I've cloned it to my machine. So now I can

**[15:51]** cloned it to my machine. So now I can

**[15:51]** cloned it to my machine. So now I can look at the code and it's like this uh

**[15:56]** look at the code and it's like this uh

**[15:56]** look at the code and it's like this uh view app that has a bunch of things in

**[15:59]** view app that has a bunch of things in

**[15:59]** view app that has a bunch of things in it. But the main thing is we want to be


### [16:00 - 17:00]

**[16:01]** it. But the main thing is we want to be

**[16:01]** it. But the main thing is we want to be able to make an agent that develops it,

**[16:03]** able to make an agent that develops it,

**[16:03]** able to make an agent that develops it, right? Um optionally you can configure

**[16:05]** right? Um optionally you can configure

**[16:05]** right? Um optionally you can configure Dagger cloud which is let me just start

**[16:08]** Dagger cloud which is let me just start

**[16:08]** Dagger cloud which is let me just start loading that web page now. Um,

**[16:12]** loading that web page now. Um,

**[16:12]** loading that web page now. Um, it's basically a visualization so you

**[16:14]** it's basically a visualization so you

**[16:14]** it's basically a visualization so you can really easily see what your agent's

**[16:16]** can really easily see what your agent's

**[16:16]** can really easily see what your agent's doing, right? Because that's the hardest

**[16:17]** doing, right? Because that's the hardest

**[16:17]** doing, right? Because that's the hardest part of building agents a lot of the

**[16:19]** part of building agents a lot of the

**[16:19]** part of building agents a lot of the time is understanding like what are they

**[16:22]** time is understanding like what are they

**[16:22]** time is understanding like what are they tripping on, what what's actually going

**[16:23]** tripping on, what what's actually going

**[16:23]** tripping on, what what's actually going on inside the agent, how is it

**[16:25]** on inside the agent, how is it

**[16:25]** on inside the agent, how is it interacting with its tools, what tools

**[16:27]** interacting with its tools, what tools

**[16:27]** interacting with its tools, what tools is it even seeing. Um, so with this

**[16:29]** is it even seeing. Um, so with this

**[16:29]** is it even seeing. Um, so with this visualiz visualization, you're able to

**[16:31]** visualiz visualization, you're able to

**[16:31]** visualiz visualization, you're able to really easily see uh everything that

**[16:34]** really easily see uh everything that

**[16:34]** really easily see uh everything that your agent's doing. And that's helped me

**[16:36]** your agent's doing. And that's helped me

**[16:36]** your agent's doing. And that's helped me a lot like develop my prompts. Like if I

**[16:37]** a lot like develop my prompts. Like if I

**[16:37]** a lot like develop my prompts. Like if I see um the prompts and environments,

**[16:40]** see um the prompts and environments,

**[16:40]** see um the prompts and environments, right? If I see a lot of times that okay

**[16:42]** right? If I see a lot of times that okay

**[16:42]** right? If I see a lot of times that okay that the agent fails because it tries to

**[16:44]** that the agent fails because it tries to

**[16:44]** that the agent fails because it tries to call this tool incorrectly, I can

**[16:46]** call this tool incorrectly, I can

**[16:46]** call this tool incorrectly, I can improve like the description of the tool

**[16:48]** improve like the description of the tool

**[16:48]** improve like the description of the tool or maybe I need to change how the tool

**[16:49]** or maybe I need to change how the tool

**[16:49]** or maybe I need to change how the tool works completely. Um and so being able

**[16:52]** works completely. Um and so being able

**[16:52]** works completely. Um and so being able to see how the agent's behaving is a

**[16:54]** to see how the agent's behaving is a

**[16:54]** to see how the agent's behaving is a huge part of that. Um whether you're

**[16:55]** huge part of that. Um whether you're

**[16:56]** huge part of that. Um whether you're using cloud or or any other thing to

**[16:58]** using cloud or or any other thing to

**[16:58]** using cloud or or any other thing to visualize your agents, that's like the

**[16:59]** visualize your agents, that's like the


### [17:00 - 18:00]

**[17:00]** visualize your agents, that's like the most important part of u making it

**[17:02]** most important part of u making it

**[17:02]** most important part of u making it reliable. Um okay, so we've cloned the

**[17:05]** reliable. Um okay, so we've cloned the

**[17:05]** reliable. Um okay, so we've cloned the project. We now want to create a Dagger

**[17:08]** project. We now want to create a Dagger

**[17:08]** project. We now want to create a Dagger module. So if you've installed Dagger,

**[17:10]** module. So if you've installed Dagger,

**[17:10]** module. So if you've installed Dagger, uh you'll run this command Dagger init

**[17:12]** uh you'll run this command Dagger init

**[17:12]** uh you'll run this command Dagger init uh with whatever SDK you're using. So we

**[17:14]** uh with whatever SDK you're using. So we

**[17:14]** uh with whatever SDK you're using. So we have these tabs here. Um so I'm going to

**[17:16]** have these tabs here. Um so I'm going to

**[17:16]** have these tabs here. Um so I'm going to be using Python. And then the name of

**[17:18]** be using Python. And then the name of

**[17:18]** be using Python. And then the name of the module is going to be hello dagger.

**[17:20]** the module is going to be hello dagger.

**[17:20]** the module is going to be hello dagger. And that's important because that is

**[17:22]** And that's important because that is

**[17:22]** And that's important because that is basically the name of our um object that

**[17:25]** basically the name of our um object that

**[17:25]** basically the name of our um object that gets created. So if I open this up and

**[17:28]** gets created. So if I open this up and

**[17:28]** gets created. So if I open this up and I've run dagger and now I can open in my

**[17:31]** I've run dagger and now I can open in my

**[17:31]** I've run dagger and now I can open in my dagger folder. And sorry that's really

**[17:33]** dagger folder. And sorry that's really

**[17:33]** dagger folder. And sorry that's really small. I don't remember how to make that

**[17:34]** small. I don't remember how to make that

**[17:34]** small. I don't remember how to make that bigger in Zed, but we can. It's in the

**[17:37]** bigger in Zed, but we can. It's in the

**[17:37]** bigger in Zed, but we can. It's in the uh It's in the uh preferences to zoom

**[17:41]** uh It's in the uh preferences to zoom

**[17:41]** uh It's in the uh preferences to zoom the sidebar. Command comma.

**[17:49]** Oh, you command comma and it'll Yeah.

**[17:50]** Oh, you command comma and it'll Yeah. And you just put the there's a the top

**[17:52]** And you just put the there's a the top

**[17:52]** And you just put the there's a the top there's a there's a

**[17:55]** there's a there's a

**[17:55]** there's a there's a Well, I guess you don't have your set,

**[17:56]** Well, I guess you don't have your set,

**[17:56]** Well, I guess you don't have your set, but it's a it's a font size. Font size.


### [18:00 - 19:00]

**[18:01]** but it's a it's a font size. Font size.

**[18:01]** but it's a it's a font size. Font size. that one. UI font size. Change it to

**[18:04]** that one. UI font size. Change it to

**[18:04]** that one. UI font size. Change it to like 25 or something. Watch it. There

**[18:07]** like 25 or something. Watch it. There

**[18:07]** like 25 or something. Watch it. There you go. Save that. Bam. Boom. Okay. So,

**[18:10]** you go. Save that. Bam. Boom. Okay. So,

**[18:10]** you go. Save that. Bam. Boom. Okay. So, now hopefully we can see the sidebar a

**[18:11]** now hopefully we can see the sidebar a

**[18:12]** now hopefully we can see the sidebar a little bit better. Um, so I'm in this

**[18:14]** little bit better. Um, so I'm in this

**[18:14]** little bit better. Um, so I'm in this dagger directory and apparently I've

**[18:17]** dagger directory and apparently I've

**[18:17]** dagger directory and apparently I've written go for this one. Is this Oh,

**[18:19]** written go for this one. Is this Oh,

**[18:19]** written go for this one. Is this Oh, because that's the wrong project. Cool.

**[18:21]** because that's the wrong project. Cool.

**[18:21]** because that's the wrong project. Cool. Uh, let's go to the correct project.

**[18:28]** Me open that up and close all these

**[18:28]** Me open that up and close all these things. Okay. So I'm in the correct

**[18:30]** things. Okay. So I'm in the correct

**[18:30]** things. Okay. So I'm in the correct project and in my dagger I've got this

**[18:33]** project and in my dagger I've got this

**[18:33]** project and in my dagger I've got this source hello dagger mainpi and so we

**[18:36]** source hello dagger mainpi and so we

**[18:36]** source hello dagger mainpi and so we would have generated when we set dagger

**[18:39]** would have generated when we set dagger

**[18:39]** would have generated when we set dagger in it'll have um basically these files

**[18:42]** in it'll have um basically these files

**[18:42]** in it'll have um basically these files but some different content. So it's

**[18:43]** but some different content. So it's

**[18:43]** but some different content. So it's going to have like the the basic

**[18:45]** going to have like the the basic

**[18:45]** going to have like the the basic generated things uh to get you started

**[18:47]** generated things uh to get you started

**[18:48]** generated things uh to get you started building modules but we're going to say

**[18:51]** building modules but we're going to say

**[18:51]** building modules but we're going to say um see dagger functions.

**[18:54]** um see dagger functions.

**[18:54]** um see dagger functions. It'll show us what's available in this

**[18:55]** It'll show us what's available in this

**[18:56]** It'll show us what's available in this Dagger module that just got created. And

**[18:57]** Dagger module that just got created. And

**[18:57]** Dagger module that just got created. And so this is basically how you interact

**[18:58]** so this is basically how you interact

**[18:58]** so this is basically how you interact with daggers with the Dagger CLI and you


### [19:00 - 20:00]

**[19:01]** with daggers with the Dagger CLI and you

**[19:01]** with daggers with the Dagger CLI and you have this code that are just functions

**[19:04]** have this code that are just functions

**[19:04]** have this code that are just functions of how to uh interact with your

**[19:06]** of how to uh interact with your

**[19:06]** of how to uh interact with your application. So for example, this build

**[19:08]** application. So for example, this build

**[19:08]** application. So for example, this build one uh we have a container. If we go

**[19:12]** one uh we have a container. If we go

**[19:12]** one uh we have a container. If we go down to this function and you see we're

**[19:14]** down to this function and you see we're

**[19:14]** down to this function and you see we're just building building blocks. We have a

**[19:15]** just building building blocks. We have a

**[19:15]** just building building blocks. We have a function that gives us a Dagger

**[19:18]** function that gives us a Dagger

**[19:18]** function that gives us a Dagger container that uh is from this base and

**[19:22]** container that uh is from this base and

**[19:22]** container that uh is from this base and we put these files in it and we run this

**[19:24]** we put these files in it and we run this

**[19:24]** we put these files in it and we run this command. And so in that container when

**[19:26]** command. And so in that container when

**[19:26]** command. And so in that container when we want to do a build of our app, uh we

**[19:29]** we want to do a build of our app, uh we

**[19:29]** we want to do a build of our app, uh we can

**[19:31]** can

**[19:31]** can call that other function to get that

**[19:32]** call that other function to get that

**[19:32]** call that other function to get that container with our our code in it, run

**[19:35]** container with our our code in it, run

**[19:35]** container with our our code in it, run another command and then get a directory

**[19:37]** another command and then get a directory

**[19:37]** another command and then get a directory from that. And so this is like really

**[19:38]** from that. And so this is like really

**[19:38]** from that. And so this is like really basic Dagger stuff of how you create

**[19:41]** basic Dagger stuff of how you create

**[19:41]** basic Dagger stuff of how you create your dev tools using Dagger. This is

**[19:43]** your dev tools using Dagger. This is

**[19:43]** your dev tools using Dagger. This is like good to call out here. So

**[19:45]** like good to call out here. So

**[19:45]** like good to call out here. So originally we had this example from Kyle

**[19:47]** originally we had this example from Kyle

**[19:47]** originally we had this example from Kyle where he showed us running like a

**[19:50]** where he showed us running like a

**[19:50]** where he showed us running like a container and then we said give me a a

**[19:53]** container and then we said give me a a

**[19:53]** container and then we said give me a a Scratch container. Oh, wait. Give me an

**[19:54]** Scratch container. Oh, wait. Give me an

**[19:54]** Scratch container. Oh, wait. Give me an im from an image from Alpine or from

**[19:57]** im from an image from Alpine or from

**[19:57]** im from an image from Alpine or from Node or from whatever. And then you can

**[19:59]** Node or from whatever. And then you can

**[19:59]** Node or from whatever. And then you can layer on more things like add a


### [20:00 - 21:00]

**[20:01]** layer on more things like add a

**[20:01]** layer on more things like add a directory a source code to that. Run

**[20:03]** directory a source code to that. Run

**[20:03]** directory a source code to that. Run exec a test command whatever, right?

**[20:05]** exec a test command whatever, right?

**[20:05]** exec a test command whatever, right? Chaining these things together. So you

**[20:07]** Chaining these things together. So you

**[20:07]** Chaining these things together. So you notice I'm using this builder pattern

**[20:09]** notice I'm using this builder pattern

**[20:09]** notice I'm using this builder pattern here in code instead of in like a CLI.

**[20:13]** here in code instead of in like a CLI.

**[20:13]** here in code instead of in like a CLI. So it's all the same API under the hood.

**[20:15]** So it's all the same API under the hood.

**[20:15]** So it's all the same API under the hood. It's just in this in this case he's

**[20:17]** It's just in this in this case he's

**[20:17]** It's just in this in this case he's using a Python SDK into that same API

**[20:21]** using a Python SDK into that same API

**[20:21]** using a Python SDK into that same API but the same things are happening either

**[20:23]** but the same things are happening either

**[20:23]** but the same things are happening either way. Same one unified cache where all

**[20:26]** way. Same one unified cache where all

**[20:26]** way. Same one unified cache where all that stuff is being all those cached

**[20:28]** that stuff is being all those cached

**[20:28]** that stuff is being all those cached operations are at and and one API. So

**[20:30]** operations are at and and one API. So

**[20:30]** operations are at and and one API. So that's why it becomes really easy to use

**[20:33]** that's why it becomes really easy to use

**[20:33]** that's why it becomes really easy to use different languages different language

**[20:35]** different languages different language

**[20:35]** different languages different language SDKs because it's ultimately all one API

**[20:38]** SDKs because it's ultimately all one API

**[20:38]** SDKs because it's ultimately all one API under the hood. And so we got this code

**[20:40]** under the hood. And so we got this code

**[20:40]** under the hood. And so we got this code in this the next step of this where it

**[20:42]** in this the next step of this where it

**[20:42]** in this the next step of this where it says construct a pipeline. We've copied

**[20:44]** says construct a pipeline. We've copied

**[20:44]** says construct a pipeline. We've copied this code into that main file and that

**[20:46]** this code into that main file and that

**[20:46]** this code into that main file and that has all of those functions like publish

**[20:48]** has all of those functions like publish

**[20:48]** has all of those functions like publish build test uh and that build m1 we

**[20:52]** build test uh and that build m1 we

**[20:52]** build test uh and that build m1 we looked at u and build mv as in like your

**[20:55]** looked at u and build mv as in like your

**[20:55]** looked at u and build mv as in like your build environment and so when we run

**[20:56]** build environment and so when we run

**[20:56]** build environment and so when we run dagger functions we'll have those shown

**[20:59]** dagger functions we'll have those shown

**[20:59]** dagger functions we'll have those shown up here with their descriptions and


### [21:00 - 22:00]

**[21:00]** up here with their descriptions and

**[21:00]** up here with their descriptions and everything from the code. So now we've

**[21:03]** everything from the code. So now we've

**[21:03]** everything from the code. So now we've at this point like we we've got the

**[21:04]** at this point like we we've got the

**[21:04]** at this point like we we've got the project that we want to build the agent

**[21:06]** project that we want to build the agent

**[21:06]** project that we want to build the agent in. We've got um some Dagger functions

**[21:09]** in. We've got um some Dagger functions

**[21:09]** in. We've got um some Dagger functions that let us build and test the project.

**[21:11]** that let us build and test the project.

**[21:11]** that let us build and test the project. We've got the project itself. So now

**[21:12]** We've got the project itself. So now

**[21:12]** We've got the project itself. So now let's actually get the agent started.

**[21:15]** let's actually get the agent started.

**[21:15]** let's actually get the agent started. Um, and so now I'll zoom out again so

**[21:17]** Um, and so now I'll zoom out again so

**[21:17]** Um, and so now I'll zoom out again so you can see because I jumped to the next

**[21:19]** you can see because I jumped to the next

**[21:19]** you can see because I jumped to the next page here, which is add an AI agent to

**[21:21]** page here, which is add an AI agent to

**[21:21]** page here, which is add an AI agent to an existing project.

**[21:23]** an existing project.

**[21:23]** an existing project. And so we're starting from exactly where

**[21:26]** And so we're starting from exactly where

**[21:26]** And so we're starting from exactly where we just left off there with that

**[21:27]** we just left off there with that

**[21:27]** we just left off there with that previous guide where we pasted in that

**[21:29]** previous guide where we pasted in that

**[21:29]** previous guide where we pasted in that code. We have our our um build, build a

**[21:34]** code. We have our our um build, build a

**[21:34]** code. We have our our um build, build a publish, test in our Dagger functions.

**[21:36]** publish, test in our Dagger functions.

**[21:36]** publish, test in our Dagger functions. lots of useful functions, but the

**[21:38]** lots of useful functions, but the

**[21:38]** lots of useful functions, but the expectation was the human was probably

**[21:41]** expectation was the human was probably

**[21:41]** expectation was the human was probably running those, right? Or you were having

**[21:44]** running those, right? Or you were having

**[21:44]** running those, right? Or you were having them run in CI. You'd kind of set that

**[21:46]** them run in CI. You'd kind of set that

**[21:46]** them run in CI. You'd kind of set that up, but nothing really agentic yet,

**[21:49]** up, but nothing really agentic yet,

**[21:49]** up, but nothing really agentic yet, right? So, we have, you know, we're just

**[21:50]** right? So, we have, you know, we're just

**[21:50]** right? So, we have, you know, we're just running our unit test or our our build

**[21:52]** running our unit test or our our build

**[21:52]** running our unit test or our our build and creating a production container. And

**[21:54]** and creating a production container. And

**[21:54]** and creating a production container. And this is what uh you as a developer or

**[21:57]** this is what uh you as a developer or

**[21:57]** this is what uh you as a developer or your your CI environment are running

**[21:59]** your your CI environment are running

**[21:59]** your your CI environment are running these functions. But now we want to


### [22:00 - 23:00]

**[22:01]** these functions. But now we want to

**[22:01]** these functions. But now we want to create an agent for developers to

**[22:03]** create an agent for developers to

**[22:03]** create an agent for developers to interact with um or you know to run

**[22:06]** interact with um or you know to run

**[22:06]** interact with um or you know to run anywhere but also our agent should be

**[22:08]** anywhere but also our agent should be

**[22:08]** anywhere but also our agent should be able to use these functions as well. Um

**[22:10]** able to use these functions as well. Um

**[22:10]** able to use these functions as well. Um and so we're in this this next guide and

**[22:12]** and so we're in this this next guide and

**[22:12]** and so we're in this this next guide and we're going to now create a subm module

**[22:15]** we're going to now create a subm module

**[22:15]** we're going to now create a subm module because I mentioned like our agents want

**[22:17]** because I mentioned like our agents want

**[22:17]** because I mentioned like our agents want these uh refined environments where we

**[22:20]** these uh refined environments where we

**[22:20]** these uh refined environments where we give them access to exactly what tools

**[22:22]** give them access to exactly what tools

**[22:22]** give them access to exactly what tools they need to complete their tasks. We

**[22:24]** they need to complete their tasks. We

**[22:24]** they need to complete their tasks. We and nothing more than that. No, no,

**[22:26]** and nothing more than that. No, no,

**[22:26]** and nothing more than that. No, no, wait. I thought you gonna give agents

**[22:27]** wait. I thought you gonna give agents

**[22:27]** wait. I thought you gonna give agents like every possible tool. You want to

**[22:29]** like every possible tool. You want to

**[22:29]** like every possible tool. You want to let them have like a thousand functions

**[22:32]** let them have like a thousand functions

**[22:32]** let them have like a thousand functions that do very powerful things and just

**[22:34]** that do very powerful things and just

**[22:34]** that do very powerful things and just let them run crazy. Is that not the best

**[22:37]** let them run crazy. Is that not the best

**[22:38]** let them run crazy. Is that not the best practice? The uh Yeah, maybe not based

**[22:40]** practice? The uh Yeah, maybe not based

**[22:40]** practice? The uh Yeah, maybe not based on the the smiles across the room. Okay.

**[22:42]** on the the smiles across the room. Okay.

**[22:42]** on the the smiles across the room. Okay. Yes.

**[22:49]** Oh yeah. So the question is what if the

**[22:49]** Oh yeah. So the question is what if the tool needed changes at runtime? How

**[22:51]** tool needed changes at runtime? How

**[22:51]** tool needed changes at runtime? How about dynamic kind of tools, right? So a

**[22:53]** about dynamic kind of tools, right? So a

**[22:53]** about dynamic kind of tools, right? So a lot of cases we're working with MCPs

**[22:55]** lot of cases we're working with MCPs

**[22:55]** lot of cases we're working with MCPs that might we might have a lot of static

**[22:57]** that might we might have a lot of static

**[22:57]** that might we might have a lot of static tool kind of experience you know where

**[22:59]** tool kind of experience you know where

**[22:59]** tool kind of experience you know where things change what what what does happen


### [23:00 - 24:00]

**[23:00]** things change what what what does happen

**[23:00]** things change what what what does happen Kyle? Well so the the main thing is like

**[23:02]** Kyle? Well so the the main thing is like

**[23:02]** Kyle? Well so the the main thing is like you want the right amount of tools to

**[23:05]** you want the right amount of tools to

**[23:05]** you want the right amount of tools to for that agent to solve its task uh

**[23:07]** for that agent to solve its task uh

**[23:07]** for that agent to solve its task uh whatever that task is like it needs the

**[23:09]** whatever that task is like it needs the

**[23:09]** whatever that task is like it needs the flexibility uh to to be able to solve

**[23:12]** flexibility uh to to be able to solve

**[23:12]** flexibility uh to to be able to solve complex problems. Uh so it's not just

**[23:14]** complex problems. Uh so it's not just

**[23:14]** complex problems. Uh so it's not just going straight down a workflow and

**[23:15]** going straight down a workflow and

**[23:15]** going straight down a workflow and saying okay I do this and I do this and

**[23:18]** saying okay I do this and I do this and

**[23:18]** saying okay I do this and I do this and do this because you don't really need an

**[23:19]** do this because you don't really need an

**[23:20]** do this because you don't really need an AI to do that. It needs the amount of

**[23:22]** AI to do that. It needs the amount of

**[23:22]** AI to do that. It needs the amount of tools to select to choose its own path

**[23:24]** tools to select to choose its own path

**[23:24]** tools to select to choose its own path uh to solve whatever task you throw at

**[23:26]** uh to solve whatever task you throw at

**[23:26]** uh to solve whatever task you throw at it. But you don't want so many tools

**[23:28]** it. But you don't want so many tools

**[23:28]** it. But you don't want so many tools that now this is a generalized agent

**[23:30]** that now this is a generalized agent

**[23:30]** that now this is a generalized agent that does anything, right? It needs to

**[23:33]** that does anything, right? It needs to

**[23:33]** that does anything, right? It needs to have some amount of focus so that it can

**[23:35]** have some amount of focus so that it can

**[23:35]** have some amount of focus so that it can solve a specific set of problems really

**[23:38]** solve a specific set of problems really

**[23:38]** solve a specific set of problems really well. But we will see like in the agent

**[23:40]** well. But we will see like in the agent

**[23:40]** well. But we will see like in the agent loop that's going to happen. We will see

**[23:42]** loop that's going to happen. We will see

**[23:42]** loop that's going to happen. We will see the ability for the a for the LLM to see

**[23:45]** the ability for the a for the LLM to see

**[23:45]** the ability for the a for the LLM to see this like menu of tools it has and that

**[23:47]** this like menu of tools it has and that

**[23:47]** this like menu of tools it has and that for it to select the right tool at the

**[23:49]** for it to select the right tool at the

**[23:49]** for it to select the right tool at the right time given the context. Yeah. But

**[23:52]** right time given the context. Yeah. But

**[23:52]** right time given the context. Yeah. But yeah, definitely like a big part of

**[23:54]** yeah, definitely like a big part of

**[23:54]** yeah, definitely like a big part of iterating and building these agents is

**[23:56]** iterating and building these agents is

**[23:56]** iterating and building these agents is determining like the scope of the tools.

**[23:58]** determining like the scope of the tools.

**[23:58]** determining like the scope of the tools. So like um the kind of the balance


### [24:00 - 25:00]

**[24:01]** So like um the kind of the balance

**[24:01]** So like um the kind of the balance between flexibility and reliability

**[24:03]** between flexibility and reliability

**[24:03]** between flexibility and reliability where you want it to be able to solve a

**[24:06]** where you want it to be able to solve a

**[24:06]** where you want it to be able to solve a breadth of problems. Uh, so it needs a

**[24:08]** breadth of problems. Uh, so it needs a

**[24:08]** breadth of problems. Uh, so it needs a variety of tools that it might need. You

**[24:10]** variety of tools that it might need. You

**[24:10]** variety of tools that it might need. You don't know exactly what it's gonna need

**[24:11]** don't know exactly what it's gonna need

**[24:11]** don't know exactly what it's gonna need ahead of time, but you don't want to

**[24:13]** ahead of time, but you don't want to

**[24:13]** ahead of time, but you don't want to give it so many that now it's getting

**[24:15]** give it so many that now it's getting

**[24:15]** give it so many that now it's getting lost and confused and fails half the

**[24:17]** lost and confused and fails half the

**[24:17]** lost and confused and fails half the time, right? And so that's what we're

**[24:18]** time, right? And so that's what we're

**[24:18]** time, right? And so that's what we're going to focus on here with this uh

**[24:20]** going to focus on here with this uh

**[24:20]** going to focus on here with this uh we're going to create a subm module

**[24:22]** we're going to create a subm module

**[24:22]** we're going to create a subm module basically that is kind of it its

**[24:24]** basically that is kind of it its

**[24:24]** basically that is kind of it its playground. It's specific set of tools

**[24:27]** playground. It's specific set of tools

**[24:27]** playground. It's specific set of tools that lets it uh edit our source code.

**[24:29]** that lets it uh edit our source code.

**[24:29]** that lets it uh edit our source code. And so if you've worked with uh maybe

**[24:32]** And so if you've worked with uh maybe

**[24:32]** And so if you've worked with uh maybe agent frameworks in the past that have

**[24:34]** agent frameworks in the past that have

**[24:34]** agent frameworks in the past that have like file system tools, we're actually

**[24:37]** like file system tools, we're actually

**[24:37]** like file system tools, we're actually going to build that in our own code

**[24:38]** going to build that in our own code

**[24:38]** going to build that in our own code right now. Um and that and it's just a

**[24:40]** right now. Um and that and it's just a

**[24:40]** right now. Um and that and it's just a few lines of code. So don't let me scare

**[24:42]** few lines of code. So don't let me scare

**[24:42]** few lines of code. So don't let me scare you with that. But that's the idea is

**[24:44]** you with that. But that's the idea is

**[24:44]** you with that. But that's the idea is like we're we're creating these building

**[24:45]** like we're we're creating these building

**[24:45]** like we're we're creating these building blocks and as you scale this up, uh you

**[24:48]** blocks and as you scale this up, uh you

**[24:48]** blocks and as you scale this up, uh you can consume these from that other people

**[24:50]** can consume these from that other people

**[24:50]** can consume these from that other people have written. You don't have to write it

**[24:51]** have written. You don't have to write it

**[24:51]** have written. You don't have to write it all from scratch. But for the practice

**[24:53]** all from scratch. But for the practice

**[24:53]** all from scratch. But for the practice of building this as a workshop, we're

**[24:55]** of building this as a workshop, we're

**[24:55]** of building this as a workshop, we're going to write it all. And so all right

**[24:57]** going to write it all. And so all right

**[24:57]** going to write it all. And so all right where we going to give the a where we

**[24:58]** where we going to give the a where we

**[24:58]** where we going to give the a where we going to give what we put in this


### [25:00 - 26:00]

**[25:00]** going to give what we put in this

**[25:00]** going to give what we put in this workspace what kind of functions yeah so

**[25:01]** workspace what kind of functions yeah so

**[25:01]** workspace what kind of functions yeah so we do another dagger in it here and we

**[25:03]** we do another dagger in it here and we

**[25:03]** we do another dagger in it here and we say uh daggerworkspace so we've created

**[25:07]** say uh daggerworkspace so we've created

**[25:07]** say uh daggerworkspace so we've created in our file system another subdirectory

**[25:10]** in our file system another subdirectory

**[25:10]** in our file system another subdirectory here uh workspace underdagger and so

**[25:13]** here uh workspace underdagger and so

**[25:13]** here uh workspace underdagger and so this is another dagger module um and

**[25:15]** this is another dagger module um and

**[25:15]** this is another dagger module um and this one's just going to have just the

**[25:17]** this one's just going to have just the

**[25:17]** this one's just going to have just the functions that we want the agent to have

**[25:18]** functions that we want the agent to have

**[25:18]** functions that we want the agent to have access to um so you can imagine it wants

**[25:21]** access to um so you can imagine it wants

**[25:21]** access to um so you can imagine it wants to read the files in your source tree uh

**[25:23]** to read the files in your source tree uh

**[25:23]** to read the files in your source tree uh so we have a function and again a file

**[25:26]** so we have a function and again a file

**[25:26]** so we have a function and again a file is one of those core components of

**[25:27]** is one of those core components of

**[25:27]** is one of those core components of Dagger. And so we just our workspace has

**[25:31]** Dagger. And so we just our workspace has

**[25:31]** Dagger. And so we just our workspace has a Dagger directory which is our source

**[25:33]** a Dagger directory which is our source

**[25:33]** a Dagger directory which is our source code. Um and so we give it a function to

**[25:35]** code. Um and so we give it a function to

**[25:35]** code. Um and so we give it a function to read a file from that. Um so it just

**[25:38]** read a file from that. Um so it just

**[25:38]** read a file from that. Um so it just gets the contents of that file. Um and

**[25:41]** gets the contents of that file. Um and

**[25:41]** gets the contents of that file. Um and that's just the Dagger API to say this

**[25:43]** that's just the Dagger API to say this

**[25:43]** that's just the Dagger API to say this is a path to a file. I can do lots of

**[25:45]** is a path to a file. I can do lots of

**[25:45]** is a path to a file. I can do lots of things with a file. One of those is to

**[25:46]** things with a file. One of those is to

**[25:46]** things with a file. One of those is to look at the contents. Um another

**[25:49]** look at the contents. Um another

**[25:49]** look at the contents. Um another function it needs is to be able to write

**[25:50]** function it needs is to be able to write

**[25:50]** function it needs is to be able to write files to the workspace obviously. Uh and

**[25:53]** files to the workspace obviously. Uh and

**[25:53]** files to the workspace obviously. Uh and so it's very similar API here where we

**[25:55]** so it's very similar API here where we

**[25:55]** so it's very similar API here where we say okay give me the path and also the

**[25:57]** say okay give me the path and also the

**[25:57]** say okay give me the path and also the contents to write to that file. Uh and


### [26:00 - 27:00]

**[26:01]** contents to write to that file. Uh and

**[26:01]** contents to write to that file. Uh and then it needs to be able to know what

**[26:02]** then it needs to be able to know what

**[26:02]** then it needs to be able to know what files are in the workspace. So it needs

**[26:04]** files are in the workspace. So it needs

**[26:04]** files are in the workspace. So it needs to be able to list the files and it's

**[26:06]** to be able to list the files and it's

**[26:06]** to be able to list the files and it's just going to literally do a tree in

**[26:08]** just going to literally do a tree in

**[26:08]** just going to literally do a tree in that workspace so it can quickly see the

**[26:10]** that workspace so it can quickly see the

**[26:10]** that workspace so it can quickly see the the file structure of your code. Um, and

**[26:13]** the file structure of your code. Um, and

**[26:13]** the file structure of your code. Um, and so now basically with those three, we

**[26:15]** so now basically with those three, we

**[26:15]** so now basically with those three, we have another one that we're going to

**[26:16]** have another one that we're going to

**[26:16]** have another one that we're going to look at in a second, but with those

**[26:17]** look at in a second, but with those

**[26:17]** look at in a second, but with those three now can do all the code editing

**[26:19]** three now can do all the code editing

**[26:19]** three now can do all the code editing you might ask it to do within your your

**[26:22]** you might ask it to do within your your

**[26:22]** you might ask it to do within your your file system, right? And with with more

**[26:24]** file system, right? And with with more

**[26:24]** file system, right? And with with more complex um projects, you might need more

**[26:28]** complex um projects, you might need more

**[26:28]** complex um projects, you might need more advanced capabilities of these, like you

**[26:30]** advanced capabilities of these, like you

**[26:30]** advanced capabilities of these, like you might need to be able to read specific

**[26:32]** might need to be able to read specific

**[26:32]** might need to be able to read specific lines from a file or scan files or

**[26:35]** lines from a file or scan files or

**[26:35]** lines from a file or scan files or insert lines into files. But with our

**[26:37]** insert lines into files. But with our

**[26:37]** insert lines into files. But with our kind of demo agent that we're building

**[26:39]** kind of demo agent that we're building

**[26:39]** kind of demo agent that we're building right now, it's like just the most basic

**[26:41]** right now, it's like just the most basic

**[26:41]** right now, it's like just the most basic where we can just read and write files

**[26:43]** where we can just read and write files

**[26:43]** where we can just read and write files and list the files. So if the agent had

**[26:45]** and list the files. So if the agent had

**[26:45]** and list the files. So if the agent had access to this workspace object, it

**[26:48]** access to this workspace object, it

**[26:48]** access to this workspace object, it would see those functions as tools. Read

**[26:52]** would see those functions as tools. Read

**[26:52]** would see those functions as tools. Read file, write file.

**[26:55]** file, write file.

**[26:55]** file, write file. Exactly. It will in a minute. Yeah.

**[26:57]** Exactly. It will in a minute. Yeah.

**[26:57]** Exactly. It will in a minute. Yeah. Yeah. We haven't we haven't plugged the

**[26:58]** Yeah. We haven't we haven't plugged the

**[26:58]** Yeah. We haven't we haven't plugged the the brain into the robot body yet. We


### [27:00 - 28:00]

**[27:00]** the brain into the robot body yet. We

**[27:00]** the brain into the robot body yet. We haven't. Right. So right now we're

**[27:01]** haven't. Right. So right now we're

**[27:01]** haven't. Right. So right now we're building if you think about the agent as

**[27:03]** building if you think about the agent as

**[27:03]** building if you think about the agent as a robot body with a brain plugged into

**[27:05]** a robot body with a brain plugged into

**[27:05]** a robot body with a brain plugged into it. We're building the robot body. Uh,

**[27:07]** it. We're building the robot body. Uh,

**[27:07]** it. We're building the robot body. Uh, and the brain is going to come in just a

**[27:09]** and the brain is going to come in just a

**[27:09]** and the brain is going to come in just a second here, which could be any LLM kind

**[27:11]** second here, which could be any LLM kind

**[27:11]** second here, which could be any LLM kind of a brain in a jar, right? Analogy. So,

**[27:14]** of a brain in a jar, right? Analogy. So,

**[27:14]** of a brain in a jar, right? Analogy. So, our last one finally that I mentioned

**[27:15]** our last one finally that I mentioned

**[27:15]** our last one finally that I mentioned earlier um is test. So, when it

**[27:18]** earlier um is test. So, when it

**[27:18]** earlier um is test. So, when it generates this code in in its uh

**[27:21]** generates this code in in its uh

**[27:21]** generates this code in in its uh workspace, it needs to be able to test

**[27:23]** workspace, it needs to be able to test

**[27:23]** workspace, it needs to be able to test to make sure that the code it generated

**[27:25]** to make sure that the code it generated

**[27:25]** to make sure that the code it generated is correct. And if it didn't, it'll get

**[27:27]** is correct. And if it didn't, it'll get

**[27:27]** is correct. And if it didn't, it'll get the test failures and iterate until it's

**[27:29]** the test failures and iterate until it's

**[27:29]** the test failures and iterate until it's producing good code, right? And so this

**[27:32]** producing good code, right? And so this

**[27:32]** producing good code, right? And so this is kind of the most important part of

**[27:34]** is kind of the most important part of

**[27:34]** is kind of the most important part of building this good agent is some sort of

**[27:36]** building this good agent is some sort of

**[27:36]** building this good agent is some sort of validation tool whether that's like a

**[27:38]** validation tool whether that's like a

**[27:38]** validation tool whether that's like a test or lint or just something to check

**[27:41]** test or lint or just something to check

**[27:41]** test or lint or just something to check that what it's generated uh is correct

**[27:44]** that what it's generated uh is correct

**[27:44]** that what it's generated uh is correct or maybe it's all of these things right

**[27:45]** or maybe it's all of these things right

**[27:46]** or maybe it's all of these things right there could be different levels of

**[27:47]** there could be different levels of

**[27:47]** there could be different levels of complexity but anyway here now we've got

**[27:50]** complexity but anyway here now we've got

**[27:50]** complexity but anyway here now we've got this workspace so if I go in my

**[27:52]** this workspace so if I go in my

**[27:52]** this workspace so if I go in my workspace I have this exact code over

**[27:56]** workspace I have this exact code over

**[27:56]** workspace I have this exact code over here and if I run I think I have the


### [28:00 - 29:00]

**[28:00]** here and if I run I think I have the

**[28:00]** here and if I run I think I have the function down here If I say dagger-m. So

**[28:04]** function down here If I say dagger-m. So

**[28:04]** function down here If I say dagger-m. So now dashm points to a d a specific

**[28:06]** now dashm points to a d a specific

**[28:06]** now dashm points to a d a specific dagger module and I say functions.

**[28:08]** dagger module and I say functions.

**[28:08]** dagger module and I say functions. Remember before we arranged dagger

**[28:09]** Remember before we arranged dagger

**[28:09]** Remember before we arranged dagger functions. If I run dagger-m

**[28:13]** functions. If I run dagger-m

**[28:13]** functions. If I run dagger-m daggerworkspace functions, I'll see uh

**[28:16]** daggerworkspace functions, I'll see uh

**[28:16]** daggerworkspace functions, I'll see uh exactly those functions that we just uh

**[28:18]** exactly those functions that we just uh

**[28:18]** exactly those functions that we just uh created. Okay. So the next step is we

**[28:21]** created. Okay. So the next step is we

**[28:21]** created. Okay. So the next step is we want our main dagger module to have that

**[28:24]** want our main dagger module to have that

**[28:24]** want our main dagger module to have that as a set of tools it can use. And so

**[28:27]** as a set of tools it can use. And so

**[28:27]** as a set of tools it can use. And so we're going to say dagger install that

**[28:30]** we're going to say dagger install that

**[28:30]** we're going to say dagger install that workspace module. So now uh it's

**[28:32]** workspace module. So now uh it's

**[28:32]** workspace module. So now uh it's installed as a dependency of my main

**[28:34]** installed as a dependency of my main

**[28:34]** installed as a dependency of my main module. So it has this object available.

**[28:37]** module. So it has this object available.

**[28:37]** module. So it has this object available. And we'll see why that's really cool in

**[28:40]** And we'll see why that's really cool in

**[28:40]** And we'll see why that's really cool in a second. But basically all all your

**[28:42]** a second. But basically all all your

**[28:42]** a second. But basically all all your dependencies of Dagger like I mentioned

**[28:44]** dependencies of Dagger like I mentioned

**[28:44]** dependencies of Dagger like I mentioned like we have um you know I can look at

**[28:47]** like we have um you know I can look at

**[28:47]** like we have um you know I can look at this real quick. We have a big community

**[28:50]** this real quick. We have a big community

**[28:50]** this real quick. We have a big community of people building things with Dagger.

**[28:52]** of people building things with Dagger.

**[28:52]** of people building things with Dagger. And with that, we have the Daggerverse,

**[28:54]** And with that, we have the Daggerverse,

**[28:54]** And with that, we have the Daggerverse, which is this massive index of like

**[28:56]** which is this massive index of like

**[28:56]** which is this massive index of like thousands of Dagger modules that do

**[28:58]** thousands of Dagger modules that do

**[28:58]** thousands of Dagger modules that do different specialized things. But


### [29:00 - 30:00]

**[29:00]** different specialized things. But

**[29:00]** different specialized things. But whenever you install one of these into a

**[29:02]** whenever you install one of these into a

**[29:02]** whenever you install one of these into a Dagger module, it creates,

**[29:05]** Dagger module, it creates,

**[29:05]** Dagger module, it creates, if we look at my Dagger JSON in this uh

**[29:08]** if we look at my Dagger JSON in this uh

**[29:08]** if we look at my Dagger JSON in this uh project, uh we have this list of

**[29:10]** project, uh we have this list of

**[29:10]** project, uh we have this list of dependencies.

**[29:12]** dependencies.

**[29:12]** dependencies. And so your your um Dagger module has

**[29:16]** And so your your um Dagger module has

**[29:16]** And so your your um Dagger module has basically its own Dagger client that is

**[29:18]** basically its own Dagger client that is

**[29:18]** basically its own Dagger client that is the core Dagger API in addition to all

**[29:20]** the core Dagger API in addition to all

**[29:20]** the core Dagger API in addition to all of your dependencies. And so that when

**[29:22]** of your dependencies. And so that when

**[29:22]** of your dependencies. And so that when you're writing code, you can uh like I

**[29:24]** you're writing code, you can uh like I

**[29:24]** you're writing code, you can uh like I mentioned earlier like native in this

**[29:26]** mentioned earlier like native in this

**[29:26]** mentioned earlier like native in this language. Uh you'll see all of these

**[29:29]** language. Uh you'll see all of these

**[29:29]** language. Uh you'll see all of these things available on the the main Dagger

**[29:31]** things available on the the main Dagger

**[29:31]** things available on the the main Dagger client. So you can do um all these

**[29:33]** client. So you can do um all these

**[29:33]** client. So you can do um all these complex tasks. So basically we've built

**[29:35]** complex tasks. So basically we've built

**[29:35]** complex tasks. So basically we've built two modules already. We've built this

**[29:37]** two modules already. We've built this

**[29:37]** two modules already. We've built this workspace module and the main module

**[29:40]** workspace module and the main module

**[29:40]** workspace module and the main module where we're doing our our tests and

**[29:42]** where we're doing our our tests and

**[29:42]** where we're doing our our tests and builds. Uh and so we want to create the

**[29:44]** builds. Uh and so we want to create the

**[29:44]** builds. Uh and so we want to create the agent now that can take that workspace

**[29:47]** agent now that can take that workspace

**[29:47]** agent now that can take that workspace and our tests and we can actually ask

**[29:48]** and our tests and we can actually ask

**[29:48]** and our tests and we can actually ask for new features uh or modifications or

**[29:51]** for new features uh or modifications or

**[29:52]** for new features uh or modifications or whatever. So that's the next step in

**[29:54]** whatever. So that's the next step in

**[29:54]** whatever. So that's the next step in this guide we're looking at where we

**[29:56]** this guide we're looking at where we

**[29:56]** this guide we're looking at where we want to create an agentic function. So

**[29:58]** want to create an agentic function. So

**[29:58]** want to create an agentic function. So could could we have mixed and matched


### [30:00 - 31:00]

**[30:00]** could could we have mixed and matched

**[30:00]** could could we have mixed and matched like could we have written that

**[30:01]** like could we have written that

**[30:01]** like could we have written that workspace in Typescript or in Go and

**[30:07]** workspace in Typescript or in Go and

**[30:07]** workspace in Typescript or in Go and still installed it into our Python

**[30:09]** still installed it into our Python

**[30:09]** still installed it into our Python module? Yep. Exactly. So like the other

**[30:12]** module? Yep. Exactly. So like the other

**[30:12]** module? Yep. Exactly. So like the other modules any individual module can be

**[30:14]** modules any individual module can be

**[30:14]** modules any individual module can be written in any language and you can mix

**[30:16]** written in any language and you can mix

**[30:16]** written in any language and you can mix and match however you want. I knew the

**[30:18]** and match however you want. I knew the

**[30:18]** and match however you want. I knew the answer to the question. I was just you

**[30:19]** answer to the question. I was just you

**[30:19]** answer to the question. I was just you check just checking but but yeah we see

**[30:21]** check just checking but but yeah we see

**[30:21]** check just checking but but yeah we see people do this a lot where they have

**[30:23]** people do this a lot where they have

**[30:23]** people do this a lot where they have different teams where like you know

**[30:24]** different teams where like you know

**[30:24]** different teams where like you know maybe there's a front-end platform team

**[30:26]** maybe there's a front-end platform team

**[30:26]** maybe there's a front-end platform team and then a backend platform team and

**[30:28]** and then a backend platform team and

**[30:28]** and then a backend platform team and maybe the these folks are typescript

**[30:30]** maybe the these folks are typescript

**[30:30]** maybe the these folks are typescript these folks are go but they can interop

**[30:32]** these folks are go but they can interop

**[30:32]** these folks are go but they can interop and user stuff. So yeah. Yeah. So like

**[30:35]** and user stuff. So yeah. Yeah. So like

**[30:35]** and user stuff. So yeah. Yeah. So like everything everything every task or

**[30:36]** everything everything every task or

**[30:36]** everything everything every task or workflow or whatever that you do with

**[30:38]** workflow or whatever that you do with

**[30:38]** workflow or whatever that you do with Ager is a function in your code. And so

**[30:41]** Ager is a function in your code. And so

**[30:41]** Ager is a function in your code. And so an agent is no different, right? It's

**[30:43]** an agent is no different, right? It's

**[30:43]** an agent is no different, right? It's just going to be another function. Uh

**[30:44]** just going to be another function. Uh

**[30:44]** just going to be another function. Uh and we're going to call this one develop

**[30:46]** and we're going to call this one develop

**[30:46]** and we're going to call this one develop because we're going to ask it we're

**[30:48]** because we're going to ask it we're

**[30:48]** because we're going to ask it we're going to give it an assignment to

**[30:49]** going to give it an assignment to

**[30:49]** going to give it an assignment to complete in our project. Uh and it's

**[30:52]** complete in our project. Uh and it's

**[30:52]** complete in our project. Uh and it's going to complete that assignment. So

**[30:53]** going to complete that assignment. So

**[30:53]** going to complete that assignment. So that the develop function is our agent.

**[30:57]** that the develop function is our agent.

**[30:57]** that the develop function is our agent. Uh, and so this is going to give us the

**[30:59]** Uh, and so this is going to give us the

**[30:59]** Uh, and so this is going to give us the code to copy. And I'll just open in the


### [31:00 - 32:00]

**[31:01]** code to copy. And I'll just open in the

**[31:01]** code to copy. And I'll just open in the editor so that it looks a bit nicer.

**[31:03]** editor so that it looks a bit nicer.

**[31:04]** editor so that it looks a bit nicer. Don't worry, it's only like 500 lines.

**[31:05]** Don't worry, it's only like 500 lines.

**[31:05]** Don't worry, it's only like 500 lines. It's totally fine. And you know what?

**[31:07]** It's totally fine. And you know what?

**[31:08]** It's totally fine. And you know what? It's it's it's really short. And oh,

**[31:10]** It's it's it's really short. And oh,

**[31:10]** It's it's it's really short. And oh, wait, it's not 500 lines. Yeah, this is

**[31:12]** wait, it's not 500 lines. Yeah, this is

**[31:12]** wait, it's not 500 lines. Yeah, this is this is it right here. So, we have a few

**[31:15]** this is it right here. So, we have a few

**[31:15]** this is it right here. So, we have a few lines maybe. You have it all like spaced

**[31:16]** lines maybe. You have it all like spaced

**[31:16]** lines maybe. You have it all like spaced out nicely. Yeah, it's so we have um a

**[31:19]** out nicely. Yeah, it's so we have um a

**[31:19]** out nicely. Yeah, it's so we have um a new function called develop and it takes

**[31:21]** new function called develop and it takes

**[31:22]** new function called develop and it takes in an assignment. And this annotated

**[31:24]** in an assignment. And this annotated

**[31:24]** in an assignment. And this annotated thing is just a Python way of getting us

**[31:26]** thing is just a Python way of getting us

**[31:26]** thing is just a Python way of getting us these these um doc strings for the

**[31:29]** these these um doc strings for the

**[31:30]** these these um doc strings for the parameters. But it in different

**[31:31]** parameters. But it in different

**[31:31]** parameters. But it in different languages like we can see back here if

**[31:33]** languages like we can see back here if

**[31:33]** languages like we can see back here if we go like go your arguments just look

**[31:36]** we go like go your arguments just look

**[31:36]** we go like go your arguments just look like this where this little comment is

**[31:39]** like this where this little comment is

**[31:39]** like this where this little comment is basically the help string when you're

**[31:40]** basically the help string when you're

**[31:40]** basically the help string when you're using the Dagger CLI and say Dagger

**[31:42]** using the Dagger CLI and say Dagger

**[31:42]** using the Dagger CLI and say Dagger functions it'll say the assignment

**[31:44]** functions it'll say the assignment

**[31:44]** functions it'll say the assignment parameter is assignment to complete

**[31:47]** parameter is assignment to complete

**[31:47]** parameter is assignment to complete which is really cool. Uh and we see our

**[31:49]** which is really cool. Uh and we see our

**[31:49]** which is really cool. Uh and we see our source here which is like our project

**[31:51]** source here which is like our project

**[31:51]** source here which is like our project source. Uh but of course we don't want

**[31:52]** source. Uh but of course we don't want

**[31:52]** source. Uh but of course we don't want to have to pass that as a parameter when

**[31:54]** to have to pass that as a parameter when

**[31:54]** to have to pass that as a parameter when we're calling our agent. Uh so there's

**[31:56]** we're calling our agent. Uh so there's

**[31:56]** we're calling our agent. Uh so there's this cool thing with Dagger where you

**[31:57]** this cool thing with Dagger where you

**[31:57]** this cool thing with Dagger where you just say default path is slash and

**[31:59]** just say default path is slash and

**[31:59]** just say default path is slash and that's going to be the root of our git


### [32:00 - 33:00]

**[32:00]** that's going to be the root of our git

**[32:00]** that's going to be the root of our git repo. Uh so if we don't pass in

**[32:04]** repo. Uh so if we don't pass in

**[32:04]** repo. Uh so if we don't pass in explicitly a source parameter, it's just

**[32:06]** explicitly a source parameter, it's just

**[32:06]** explicitly a source parameter, it's just going to pass in our git repo as that

**[32:08]** going to pass in our git repo as that

**[32:08]** going to pass in our git repo as that parameter. And so now we just have to

**[32:09]** parameter. And so now we just have to

**[32:09]** parameter. And so now we just have to say develop build me a cool new feature

**[32:12]** say develop build me a cool new feature

**[32:12]** say develop build me a cool new feature and it's going to kick off our agent. So

**[32:14]** and it's going to kick off our agent. So

**[32:14]** and it's going to kick off our agent. So let's look at the components of the

**[32:16]** let's look at the components of the

**[32:16]** let's look at the components of the agent real quick. So the environment is

**[32:19]** agent real quick. So the environment is

**[32:19]** agent real quick. So the environment is like the main thing, right? And I I've

**[32:21]** like the main thing, right? And I I've

**[32:21]** like the main thing, right? And I I've used that word a lot today and hopefully

**[32:23]** used that word a lot today and hopefully

**[32:23]** used that word a lot today and hopefully a lot of people are using the same word

**[32:26]** a lot of people are using the same word

**[32:26]** a lot of people are using the same word in the same way, but you you have your

**[32:30]** in the same way, but you you have your

**[32:30]** in the same way, but you you have your uh your robot body in the brain like

**[32:32]** uh your robot body in the brain like

**[32:32]** uh your robot body in the brain like Jeremy said where your environment is

**[32:34]** Jeremy said where your environment is

**[32:34]** Jeremy said where your environment is basically not just the tools that it's

**[32:36]** basically not just the tools that it's

**[32:36]** basically not just the tools that it's using to complete the task, but also um

**[32:41]** using to complete the task, but also um

**[32:41]** using to complete the task, but also um your your inputs and outputs for the

**[32:42]** your your inputs and outputs for the

**[32:42]** your your inputs and outputs for the agent um any any objects or state that

**[32:45]** agent um any any objects or state that

**[32:46]** agent um any any objects or state that it's working with. All of this is the

**[32:47]** it's working with. All of this is the

**[32:47]** it's working with. All of this is the environment. And so we want to construct

**[32:49]** environment. And so we want to construct

**[32:49]** environment. And so we want to construct this environment and then plug in the

**[32:52]** this environment and then plug in the

**[32:52]** this environment and then plug in the LLM which is our brain and say here's

**[32:54]** LLM which is our brain and say here's

**[32:54]** LLM which is our brain and say here's your environment here's your task

**[32:56]** your environment here's your task

**[32:56]** your environment here's your task slashprompt

**[32:58]** slashprompt

**[32:58]** slashprompt and complete the task. Um and so this is


### [33:00 - 34:00]

**[33:01]** and complete the task. Um and so this is

**[33:02]** and complete the task. Um and so this is this is the environment we put together

**[33:03]** this is the environment we put together

**[33:03]** this is the environment we put together where the assignment is a string input.

**[33:06]** where the assignment is a string input.

**[33:06]** where the assignment is a string input. Um so we have we have this cool kind of

**[33:09]** Um so we have we have this cool kind of

**[33:09]** Um so we have we have this cool kind of way of um declaratively building your

**[33:12]** way of um declaratively building your

**[33:12]** way of um declaratively building your prompt right where our assignment is the

**[33:14]** prompt right where our assignment is the

**[33:14]** prompt right where our assignment is the assignment to complete. This workspace

**[33:16]** assignment to complete. This workspace

**[33:16]** assignment to complete. This workspace input is a workspace with tools to edit

**[33:19]** input is a workspace with tools to edit

**[33:19]** input is a workspace with tools to edit and test code. So now that our agent

**[33:21]** and test code. So now that our agent

**[33:21]** and test code. So now that our agent when we connect these things we'll we'll

**[33:23]** when we connect these things we'll we'll

**[33:23]** when we connect these things we'll we'll see this as the description of this

**[33:25]** see this as the description of this

**[33:25]** see this as the description of this thing that it can use and say okay we're

**[33:27]** thing that it can use and say okay we're

**[33:27]** thing that it can use and say okay we're we're building out this prompt by uh

**[33:30]** we're building out this prompt by uh

**[33:30]** we're building out this prompt by uh annotating our code basically. And so

**[33:33]** annotating our code basically. And so

**[33:33]** annotating our code basically. And so with this workspace input thing that's

**[33:35]** with this workspace input thing that's

**[33:35]** with this workspace input thing that's referring to the subm module we just

**[33:37]** referring to the subm module we just

**[33:37]** referring to the subm module we just created. So if the workspace exactly so

**[33:40]** created. So if the workspace exactly so

**[33:40]** created. So if the workspace exactly so if we called that something else like fu

**[33:42]** if we called that something else like fu

**[33:42]** if we called that something else like fu workspace and we installed that this

**[33:45]** workspace and we installed that this

**[33:45]** workspace and we installed that this would be with fu workspace input. Right.

**[33:48]** would be with fu workspace input. Right.

**[33:48]** would be with fu workspace input. Right. We're we're dynamically generating all

**[33:50]** We're we're dynamically generating all

**[33:50]** We're we're dynamically generating all of these functions for the environment

**[33:53]** of these functions for the environment

**[33:53]** of these functions for the environment type to say

**[33:55]** type to say

**[33:55]** type to say um

**[33:57]** um

**[33:57]** um any objects in my dependencies I can

**[33:59]** any objects in my dependencies I can

**[33:59]** any objects in my dependencies I can have as an input or an output of uh my


### [34:00 - 35:00]

**[34:01]** have as an input or an output of uh my

**[34:01]** have as an input or an output of uh my environment. And so we notice that we

**[34:04]** environment. And so we notice that we

**[34:04]** environment. And so we notice that we also have a workspace output which is

**[34:06]** also have a workspace output which is

**[34:06]** also have a workspace output which is the completed task. Um because all

**[34:09]** the completed task. Um because all

**[34:09]** the completed task. Um because all objects in Dagger are immutable. And so

**[34:12]** objects in Dagger are immutable. And so

**[34:12]** objects in Dagger are immutable. And so you I give it an object, it's going to

**[34:15]** you I give it an object, it's going to

**[34:15]** you I give it an object, it's going to do a bunch of things and give me back a

**[34:17]** do a bunch of things and give me back a

**[34:17]** do a bunch of things and give me back a different object that's it's completed

**[34:19]** different object that's it's completed

**[34:19]** different object that's it's completed task. Um, and maybe that's like a boring

**[34:21]** task. Um, and maybe that's like a boring

**[34:21]** task. Um, and maybe that's like a boring detail, but the main thing is the thing

**[34:23]** detail, but the main thing is the thing

**[34:23]** detail, but the main thing is the thing I passed in is still going to be the

**[34:25]** I passed in is still going to be the

**[34:25]** I passed in is still going to be the same, but it's going to have a new

**[34:27]** same, but it's going to have a new

**[34:27]** same, but it's going to have a new version that's given me back called

**[34:30]** version that's given me back called

**[34:30]** version that's given me back called completed. I mean, I think a lot of

**[34:32]** completed. I mean, I think a lot of

**[34:32]** completed. I mean, I think a lot of people are dealing with this kind of

**[34:33]** people are dealing with this kind of

**[34:33]** people are dealing with this kind of stuff now, right, with the different

**[34:34]** stuff now, right, with the different

**[34:34]** stuff now, right, with the different APIs and like doing a bunch of JSON

**[34:37]** APIs and like doing a bunch of JSON

**[34:37]** APIs and like doing a bunch of JSON parsing and validation, right? and

**[34:39]** parsing and validation, right? and

**[34:39]** parsing and validation, right? and trying to you know there's different

**[34:40]** trying to you know there's different

**[34:40]** trying to you know there's different frameworks doing it different ways but

**[34:41]** frameworks doing it different ways but

**[34:41]** frameworks doing it different ways but you could just think of it as this is

**[34:43]** you could just think of it as this is

**[34:43]** you could just think of it as this is our way of saying like here are the

**[34:45]** our way of saying like here are the

**[34:45]** our way of saying like here are the typed inputs these are typed inputs

**[34:47]** typed inputs these are typed inputs

**[34:47]** typed inputs these are typed inputs we're expecting a typed output back in

**[34:50]** we're expecting a typed output back in

**[34:50]** we're expecting a typed output back in the end and this gives us a way to

**[34:53]** the end and this gives us a way to

**[34:53]** the end and this gives us a way to ensure that uh we're getting what we

**[34:55]** ensure that uh we're getting what we

**[34:55]** ensure that uh we're getting what we actually asked for right now uh next we

**[34:59]** actually asked for right now uh next we

**[34:59]** actually asked for right now uh next we we need our prompt so we have the


### [35:00 - 36:00]

**[35:00]** we need our prompt so we have the

**[35:00]** we need our prompt so we have the environment and the prompt and we give

**[35:03]** environment and the prompt and we give

**[35:03]** environment and the prompt and we give both of those to the agent basically um

**[35:05]** both of those to the agent basically um

**[35:05]** both of those to the agent basically um so the prompt I believe is just a bit

**[35:08]** so the prompt I believe is just a bit

**[35:08]** so the prompt I believe is just a bit lower here if you're following following

**[35:10]** lower here if you're following following

**[35:10]** lower here if you're following following along here. So it wants you to create a

**[35:12]** along here. So it wants you to create a

**[35:12]** along here. So it wants you to create a dagger/develop

**[35:14]** dagger/develop

**[35:14]** dagger/develop prompt.mmarkdown

**[35:16]** prompt.mmarkdown

**[35:16]** prompt.mmarkdown and it looks like this. So I'll just

**[35:18]** and it looks like this. So I'll just

**[35:18]** and it looks like this. So I'll just open it again over here on my editor.

**[35:22]** open it again over here on my editor.

**[35:22]** open it again over here on my editor. So this is our prompt and so we're

**[35:24]** So this is our prompt and so we're

**[35:24]** So this is our prompt and so we're saying you're a developer on this

**[35:26]** saying you're a developer on this

**[35:26]** saying you're a developer on this project. You're going to give you're

**[35:27]** project. You're going to give you're

**[35:28]** project. You're going to give you're going to get an assignment and the tools

**[35:29]** going to get an assignment and the tools

**[35:29]** going to get an assignment and the tools to complete it. Your assignment is

**[35:31]** to complete it. Your assignment is

**[35:31]** to complete it. Your assignment is dollar sign assignment. And so this is

**[35:33]** dollar sign assignment. And so this is

**[35:33]** dollar sign assignment. And so this is basically it's going to be templated in

**[35:36]** basically it's going to be templated in

**[35:36]** basically it's going to be templated in by

**[35:37]** by

**[35:37]** by the

**[35:39]** the

**[35:39]** the assignment in our environment. So it's

**[35:41]** assignment in our environment. So it's

**[35:41]** assignment in our environment. So it's going to drop that right in that prompt.

**[35:42]** going to drop that right in that prompt.

**[35:42]** going to drop that right in that prompt. So the the agent itself doesn't have to

**[35:44]** So the the agent itself doesn't have to

**[35:44]** So the the agent itself doesn't have to go read this other variable in its

**[35:47]** go read this other variable in its

**[35:47]** go read this other variable in its environment. It knows, okay, my

**[35:49]** environment. It knows, okay, my

**[35:49]** environment. It knows, okay, my assignment is make this cool new

**[35:50]** assignment is make this cool new

**[35:50]** assignment is make this cool new feature. And then we have a bit of

**[35:53]** feature. And then we have a bit of

**[35:53]** feature. And then we have a bit of prompt structure here, right? Where uh

**[35:55]** prompt structure here, right? Where uh

**[35:55]** prompt structure here, right? Where uh if you've built a lot of these agents,

**[35:57]** if you've built a lot of these agents,

**[35:57]** if you've built a lot of these agents, you've probably kind of refined how you

**[35:59]** you've probably kind of refined how you

**[35:59]** you've probably kind of refined how you build your prompts and what those


### [36:00 - 37:00]

**[36:00]** build your prompts and what those

**[36:00]** build your prompts and what those structures look like. Uh this is a

**[36:02]** structures look like. Uh this is a

**[36:02]** structures look like. Uh this is a really simple agent so it doesn't have a

**[36:04]** really simple agent so it doesn't have a

**[36:04]** really simple agent so it doesn't have a ton of structure but we do say uh before

**[36:07]** ton of structure but we do say uh before

**[36:07]** ton of structure but we do say uh before you write code make sure you analyze the

**[36:09]** you write code make sure you analyze the

**[36:09]** you write code make sure you analyze the workspace to understand the project

**[36:11]** workspace to understand the project

**[36:12]** workspace to understand the project structure so it's not just going to

**[36:13]** structure so it's not just going to

**[36:13]** structure so it's not just going to create some garbage or be like cool I

**[36:14]** create some garbage or be like cool I

**[36:14]** create some garbage or be like cool I made this new file uh but I didn't look

**[36:16]** made this new file uh but I didn't look

**[36:16]** made this new file uh but I didn't look at the project first. Um don't make

**[36:18]** at the project first. Um don't make

**[36:18]** at the project first. Um don't make unnecessary changes because sometimes uh

**[36:21]** unnecessary changes because sometimes uh

**[36:21]** unnecessary changes because sometimes uh you'll see especially certain models uh

**[36:23]** you'll see especially certain models uh

**[36:23]** you'll see especially certain models uh without the right constraints will go

**[36:25]** without the right constraints will go

**[36:25]** without the right constraints will go make the change you ask for and then

**[36:27]** make the change you ask for and then

**[36:27]** make the change you ask for and then change four other things and be like

**[36:28]** change four other things and be like

**[36:28]** change four other things and be like cool looks good ship it. um and always

**[36:32]** cool looks good ship it. um and always

**[36:32]** cool looks good ship it. um and always run the test. So, we do have to ask it

**[36:34]** run the test. So, we do have to ask it

**[36:34]** run the test. So, we do have to ask it to run the test once it's made those

**[36:37]** to run the test once it's made those

**[36:37]** to run the test once it's made those changes. So, it's not just going to see

**[36:39]** changes. So, it's not just going to see

**[36:39]** changes. So, it's not just going to see the test function and be like, "Oh, I

**[36:40]** the test function and be like, "Oh, I

**[36:40]** the test function and be like, "Oh, I should probably call that." We want to

**[36:41]** should probably call that." We want to

**[36:41]** should probably call that." We want to make sure to tell the LLM like, "Okay,

**[36:44]** make sure to tell the LLM like, "Okay,

**[36:44]** make sure to tell the LLM like, "Okay, you have a tool that can validate the

**[36:46]** you have a tool that can validate the

**[36:46]** you have a tool that can validate the code you're writing. Make sure you use

**[36:47]** code you're writing. Make sure you use

**[36:47]** code you're writing. Make sure you use that tool." Uh, and then don't stop

**[36:50]** that tool." Uh, and then don't stop

**[36:50]** that tool." Uh, and then don't stop until you've completed the assignment

**[36:51]** until you've completed the assignment

**[36:51]** until you've completed the assignment and the test pass. So, this is telling

**[36:53]** and the test pass. So, this is telling

**[36:53]** and the test pass. So, this is telling it, you know, keep working until you've

**[36:56]** it, you know, keep working until you've

**[36:56]** it, you know, keep working until you've satisfied what I asked it to do and the

**[36:58]** satisfied what I asked it to do and the

**[36:58]** satisfied what I asked it to do and the test pass. some good reinforcement. You


### [37:00 - 38:00]

**[37:00]** test pass. some good reinforcement. You

**[37:00]** test pass. some good reinforcement. You kind of like told it to run the test

**[37:01]** kind of like told it to run the test

**[37:01]** kind of like told it to run the test twice. Yeah, you better. And this is

**[37:03]** twice. Yeah, you better. And this is

**[37:03]** twice. Yeah, you better. And this is comes from experience, right? Maybe a

**[37:05]** comes from experience, right? Maybe a

**[37:05]** comes from experience, right? Maybe a third time will help too. I'll say it

**[37:06]** third time will help too. I'll say it

**[37:06]** third time will help too. I'll say it doesn't hurt at all because Yeah. And

**[37:08]** doesn't hurt at all because Yeah. And

**[37:08]** doesn't hurt at all because Yeah. And maybe in all caps because it's like what

**[37:11]** maybe in all caps because it's like what

**[37:11]** maybe in all caps because it's like what we find we end up running evals on these

**[37:13]** we find we end up running evals on these

**[37:13]** we find we end up running evals on these things, right? Where we'll try different

**[37:15]** things, right? Where we'll try different

**[37:15]** things, right? Where we'll try different LLMs plugged in and then we'll iterate

**[37:17]** LLMs plugged in and then we'll iterate

**[37:17]** LLMs plugged in and then we'll iterate some on the prompts and until we're

**[37:20]** some on the prompts and until we're

**[37:20]** some on the prompts and until we're getting the results, the consistency we

**[37:22]** getting the results, the consistency we

**[37:22]** getting the results, the consistency we want across the different the different

**[37:23]** want across the different the different

**[37:24]** want across the different the different ones. And um and yeah, it comes from

**[37:26]** ones. And um and yeah, it comes from

**[37:26]** ones. And um and yeah, it comes from experience of knowing like how they veer

**[37:28]** experience of knowing like how they veer

**[37:28]** experience of knowing like how they veer off track and etc. How we're writing

**[37:31]** off track and etc. How we're writing

**[37:31]** off track and etc. How we're writing these. Yeah. And that's like what what I

**[37:33]** these. Yeah. And that's like what what I

**[37:33]** these. Yeah. And that's like what what I mentioned earlier like using something

**[37:35]** mentioned earlier like using something

**[37:35]** mentioned earlier like using something like Digger Cloud to be able to visual

**[37:37]** like Digger Cloud to be able to visual

**[37:37]** like Digger Cloud to be able to visual or see the visualization of all the work

**[37:39]** or see the visualization of all the work

**[37:39]** or see the visualization of all the work the agent's doing. If I'm frequently

**[37:41]** the agent's doing. If I'm frequently

**[37:41]** the agent's doing. If I'm frequently seeing like okay that the agent is just

**[37:44]** seeing like okay that the agent is just

**[37:44]** seeing like okay that the agent is just calling write file and then returning I

**[37:46]** calling write file and then returning I

**[37:46]** calling write file and then returning I know that okay I have to tell it to look

**[37:47]** know that okay I have to tell it to look

**[37:47]** know that okay I have to tell it to look at the code. I have to tell it to test

**[37:49]** at the code. I have to tell it to test

**[37:49]** at the code. I have to tell it to test the code. And that's going to be

**[37:50]** the code. And that's going to be

**[37:50]** the code. And that's going to be different for every model and especially

**[37:52]** different for every model and especially

**[37:52]** different for every model and especially like the prompt structure is different

**[37:53]** like the prompt structure is different

**[37:53]** like the prompt structure is different for different models.


### [38:00 - 39:00]

**[38:02]** Yeah. Yeah. So the question is like can

**[38:02]** Yeah. Yeah. So the question is like can you implement like reflection agents to

**[38:04]** you implement like reflection agents to

**[38:04]** you implement like reflection agents to police each other and that's something I

**[38:06]** police each other and that's something I

**[38:06]** police each other and that's something I probably have an example of that I can

**[38:07]** probably have an example of that I can

**[38:07]** probably have an example of that I can show at the end if we have time. Um but

**[38:09]** show at the end if we have time. Um but

**[38:09]** show at the end if we have time. Um but yeah like remember in the with this each

**[38:12]** yeah like remember in the with this each

**[38:12]** yeah like remember in the with this each agent is just a dagger function and so

**[38:15]** agent is just a dagger function and so

**[38:15]** agent is just a dagger function and so you can create all these agents layered

**[38:17]** you can create all these agents layered

**[38:17]** you can create all these agents layered on other agents. Um, and even in your

**[38:20]** on other agents. Um, and even in your

**[38:20]** on other agents. Um, and even in your environment, you could actually put an

**[38:22]** environment, you could actually put an

**[38:22]** environment, you could actually put an agent in the environment and say, "Hey,

**[38:25]** agent in the environment and say, "Hey,

**[38:25]** agent in the environment and say, "Hey, you have this a this agent at your

**[38:27]** you have this a this agent at your

**[38:27]** you have this a this agent at your disposal uh if you needed to do

**[38:29]** disposal uh if you needed to do

**[38:29]** disposal uh if you needed to do something, right?" And I have examples

**[38:30]** something, right?" And I have examples

**[38:30]** something, right?" And I have examples of that, too. But it's like similar to

**[38:33]** of that, too. But it's like similar to

**[38:33]** of that, too. But it's like similar to the the concept of like Google's A2A

**[38:35]** the the concept of like Google's A2A

**[38:35]** the the concept of like Google's A2A where you you say uh if you're not

**[38:37]** where you you say uh if you're not

**[38:37]** where you you say uh if you're not familiar with that, it's basically this

**[38:39]** familiar with that, it's basically this

**[38:39]** familiar with that, it's basically this um structure where you tell an agent,

**[38:42]** um structure where you tell an agent,

**[38:42]** um structure where you tell an agent, listen, you can do these things, but you

**[38:44]** listen, you can do these things, but you

**[38:44]** listen, you can do these things, but you also can talk to these other agents, and

**[38:45]** also can talk to these other agents, and

**[38:45]** also can talk to these other agents, and that's what each of those other agents

**[38:47]** that's what each of those other agents

**[38:47]** that's what each of those other agents do. And so if you need to, you can reach

**[38:49]** do. And so if you need to, you can reach

**[38:49]** do. And so if you need to, you can reach out to them and say, "Hey, other agent,

**[38:51]** out to them and say, "Hey, other agent,

**[38:51]** out to them and say, "Hey, other agent, um, I need you to tell me how to write

**[38:53]** um, I need you to tell me how to write

**[38:53]** um, I need you to tell me how to write TypeScript." And that comes back, right?

**[38:55]** TypeScript." And that comes back, right?

**[38:55]** TypeScript." And that comes back, right? So you can put agents in environments.

**[38:57]** So you can put agents in environments.

**[38:57]** So you can put agents in environments. It's all just piecing functions


### [39:00 - 40:00]

**[39:00]** It's all just piecing functions

**[39:00]** It's all just piecing functions together, right? It's it's just the same

**[39:02]** together, right? It's it's just the same

**[39:02]** together, right? It's it's just the same code we've always been writing, but now

**[39:03]** code we've always been writing, but now

**[39:03]** code we've always been writing, but now there's an LM component. Um, cool. So

**[39:06]** there's an LM component. Um, cool. So

**[39:06]** there's an LM component. Um, cool. So now this line right here, line 94, most

**[39:09]** now this line right here, line 94, most

**[39:09]** now this line right here, line 94, most important line of the workshop because

**[39:10]** important line of the workshop because

**[39:10]** important line of the workshop because this is the agent where we've actually

**[39:12]** this is the agent where we've actually

**[39:12]** this is the agent where we've actually taken our Dagger client and LLM. So this

**[39:15]** taken our Dagger client and LLM. So this

**[39:15]** taken our Dagger client and LLM. So this is another type within the Dagger

**[39:17]** is another type within the Dagger

**[39:18]** is another type within the Dagger client. Make it bigger just for a

**[39:19]** client. Make it bigger just for a

**[39:19]** client. Make it bigger just for a second, you know, just Sure. Yeah. So

**[39:21]** second, you know, just Sure. Yeah. So

**[39:21]** second, you know, just Sure. Yeah. So it's off the screen since it's so

**[39:22]** it's off the screen since it's so

**[39:22]** it's off the screen since it's so important. I feel like it's not even

**[39:24]** important. I feel like it's not even

**[39:24]** important. I feel like it's not even getting that much bigger. It's just so

**[39:26]** getting that much bigger. It's just so

**[39:26]** getting that much bigger. It's just so huge. Yeah. There we go. Yeah. Uh cool.

**[39:28]** huge. Yeah. There we go. Yeah. Uh cool.

**[39:28]** huge. Yeah. There we go. Yeah. Uh cool. So like we we've said, "All right, from

**[39:31]** So like we we've said, "All right, from

**[39:31]** So like we we've said, "All right, from the Dagger client, we need this LLM

**[39:34]** the Dagger client, we need this LLM

**[39:34]** the Dagger client, we need this LLM type. Uh we give it an environment. We

**[39:36]** type. Uh we give it an environment. We

**[39:36]** type. Uh we give it an environment. We give it a prompt. And that's the agent."

**[39:38]** give it a prompt. And that's the agent."

**[39:38]** give it a prompt. And that's the agent." So now we've got this thing work that is

**[39:41]** So now we've got this thing work that is

**[39:41]** So now we've got this thing work that is a Dagger LM. See, people want pictures

**[39:43]** a Dagger LM. See, people want pictures

**[39:43]** a Dagger LM. See, people want pictures of it. You got You got center it. Yeah.

**[39:46]** of it. You got You got center it. Yeah.

**[39:46]** of it. You got You got center it. Yeah. Make it look good. There you go. Boom. I

**[39:48]** Make it look good. There you go. Boom. I

**[39:48]** Make it look good. There you go. Boom. I can If you need your pictures, you can

**[39:50]** can If you need your pictures, you can

**[39:50]** can If you need your pictures, you can get one with Kyle and

**[39:53]** get one with Kyle and

**[39:53]** get one with Kyle and commemorative. We've got like frames

**[39:55]** commemorative. We've got like frames

**[39:55]** commemorative. We've got like frames outside. You can slide it in after. I'll

**[39:57]** outside. You can slide it in after. I'll

**[39:58]** outside. You can slide it in after. I'll autograph it. Um, so that that's the

**[39:59]** autograph it. Um, so that that's the


### [40:00 - 41:00]

**[40:00]** autograph it. Um, so that that's the agent. Like that's literally because

**[40:01]** agent. Like that's literally because

**[40:01]** agent. Like that's literally because we've asked it like we we've said in

**[40:04]** we've asked it like we we've said in

**[40:04]** we've asked it like we we've said in this prompt. We didn't really ask. We

**[40:05]** this prompt. We didn't really ask. We

**[40:05]** this prompt. We didn't really ask. We told it we told it in the prompt. Uh,

**[40:08]** told it we told it in the prompt. Uh,

**[40:08]** told it we told it in the prompt. Uh, this is this is your task. This is how

**[40:10]** this is this is your task. This is how

**[40:10]** this is this is your task. This is how you work. Don't stop until it's done.

**[40:12]** you work. Don't stop until it's done.

**[40:12]** you work. Don't stop until it's done. And so now this work variable in our

**[40:16]** And so now this work variable in our

**[40:16]** And so now this work variable in our code is the completed work. And so from

**[40:19]** code is the completed work. And so from

**[40:19]** code is the completed work. And so from that work we can look back at the

**[40:20]** that work we can look back at the

**[40:20]** that work we can look back at the environment in that and say I have this

**[40:23]** environment in that and say I have this

**[40:23]** environment in that and say I have this output called completed because you

**[40:24]** output called completed because you

**[40:24]** output called completed because you remember in our environment we defined a

**[40:27]** remember in our environment we defined a

**[40:27]** remember in our environment we defined a workspace output called completed and

**[40:29]** workspace output called completed and

**[40:29]** workspace output called completed and this thing should be a workspace. If

**[40:31]** this thing should be a workspace. If

**[40:32]** this thing should be a workspace. If it's not somebody screwed up that

**[40:34]** it's not somebody screwed up that

**[40:34]** it's not somebody screwed up that happens sometimes. Um it's a good final

**[40:36]** happens sometimes. Um it's a good final

**[40:36]** happens sometimes. Um it's a good final check and type check. Yeah. And so from

**[40:39]** check and type check. Yeah. And so from

**[40:39]** check and type check. Yeah. And so from that workspace, we want to grab the

**[40:40]** that workspace, we want to grab the

**[40:40]** that workspace, we want to grab the completed directory which is the source.

**[40:43]** completed directory which is the source.

**[40:43]** completed directory which is the source. So if you remember in our workspace

**[40:48]** So if you remember in our workspace

**[40:48]** So if you remember in our workspace object here, it has an attribute called

**[40:50]** object here, it has an attribute called

**[40:50]** object here, it has an attribute called source which is a directory. And so this

**[40:52]** source which is a directory. And so this

**[40:52]** source which is a directory. And so this is all like a few layers of complexity,

**[40:55]** is all like a few layers of complexity,

**[40:55]** is all like a few layers of complexity, but we've said in that workspace, we

**[40:57]** but we've said in that workspace, we

**[40:57]** but we've said in that workspace, we have a source thing that's a directory.

**[40:59]** have a source thing that's a directory.

**[40:59]** have a source thing that's a directory. And ignore the node modules folder


### [41:00 - 42:00]

**[41:01]** And ignore the node modules folder

**[41:01]** And ignore the node modules folder because maybe that's going to break in

**[41:02]** because maybe that's going to break in

**[41:02]** because maybe that's going to break in my machine. Yeah. Uh and then now that

**[41:05]** my machine. Yeah. Uh and then now that

**[41:05]** my machine. Yeah. Uh and then now that we've got that just to make triple sure

**[41:07]** we've got that just to make triple sure

**[41:07]** we've got that just to make triple sure because remember I mean we we did tell

**[41:09]** because remember I mean we we did tell

**[41:09]** because remember I mean we we did tell it three times to run test but now we

**[41:12]** it three times to run test but now we

**[41:12]** it three times to run test but now we get this back and in our code we're

**[41:13]** get this back and in our code we're

**[41:13]** get this back and in our code we're saying all right now run the test

**[41:15]** saying all right now run the test

**[41:15]** saying all right now run the test because this is all the same code that

**[41:17]** because this is all the same code that

**[41:17]** because this is all the same code that we're using throughout our project to

**[41:19]** we're using throughout our project to

**[41:19]** we're using throughout our project to run tests. So we can say okay completed

**[41:22]** run tests. So we can say okay completed

**[41:22]** run tests. So we can say okay completed now manually run the tests and if that

**[41:24]** now manually run the tests and if that

**[41:24]** now manually run the tests and if that fails you could maybe kick it back into

**[41:26]** fails you could maybe kick it back into

**[41:26]** fails you could maybe kick it back into the LM and say hey this failed try

**[41:28]** the LM and say hey this failed try

**[41:28]** the LM and say hey this failed try harder. That's pretty huge right? So

**[41:29]** harder. That's pretty huge right? So

**[41:29]** harder. That's pretty huge right? So that's like trying to put the agents on

**[41:31]** that's like trying to put the agents on

**[41:32]** that's like trying to put the agents on on rails or give them guard rails,

**[41:33]** on rails or give them guard rails,

**[41:34]** on rails or give them guard rails, whichever metaphor you like better. But

**[41:35]** whichever metaphor you like better. But

**[41:35]** whichever metaphor you like better. But it's like, you know, that's pretty key

**[41:37]** it's like, you know, that's pretty key

**[41:37]** it's like, you know, that's pretty key because we're trying to like let them do

**[41:40]** because we're trying to like let them do

**[41:40]** because we're trying to like let them do the creative stuff they do, the

**[41:41]** the creative stuff they do, the

**[41:41]** the creative stuff they do, the generative stuff they do, like write

**[41:42]** generative stuff they do, like write

**[41:42]** generative stuff they do, like write some code for us, but we need to enforce

**[41:45]** some code for us, but we need to enforce

**[41:45]** some code for us, but we need to enforce certain standards, right? It could be

**[41:47]** certain standards, right? It could be

**[41:47]** certain standards, right? It could be compliance things, could be like you say

**[41:49]** compliance things, could be like you say

**[41:49]** compliance things, could be like you say linting, so we don't just dump that

**[41:51]** linting, so we don't just dump that

**[41:51]** linting, so we don't just dump that garbage garbage back to your machine.

**[41:53]** garbage garbage back to your machine.

**[41:54]** garbage garbage back to your machine. Yeah. Uh, and remember all these changes

**[41:55]** Yeah. Uh, and remember all these changes

**[41:55]** Yeah. Uh, and remember all these changes that it was making as it's iterating on

**[41:57]** that it was making as it's iterating on

**[41:57]** that it was making as it's iterating on these things, that was all done in a

**[41:59]** these things, that was all done in a

**[41:59]** these things, that was all done in a container. It's not just changing your


### [42:00 - 43:00]

**[42:01]** container. It's not just changing your

**[42:01]** container. It's not just changing your file system as it's doing its work. And

**[42:03]** file system as it's doing its work. And

**[42:03]** file system as it's doing its work. And that's a key thing, too, because now

**[42:05]** that's a key thing, too, because now

**[42:05]** that's a key thing, too, because now maybe you have 10 of these agents

**[42:07]** maybe you have 10 of these agents

**[42:07]** maybe you have 10 of these agents running. They all have their own

**[42:08]** running. They all have their own

**[42:08]** running. They all have their own sandboxed workspace where they're

**[42:09]** sandboxed workspace where they're

**[42:10]** sandboxed workspace where they're editing these files. They're not messing

**[42:11]** editing these files. They're not messing

**[42:11]** editing these files. They're not messing up your local state. And before we do

**[42:14]** up your local state. And before we do

**[42:14]** up your local state. And before we do mess up our local state, we triple check

**[42:16]** mess up our local state, we triple check

**[42:16]** mess up our local state, we triple check that the test pass. And then we say,

**[42:19]** that the test pass. And then we say,

**[42:19]** that the test pass. And then we say, okay, return that completed directory.

**[42:20]** okay, return that completed directory.

**[42:20]** okay, return that completed directory. And so now this function

**[42:23]** And so now this function

**[42:23]** And so now this function and we'll just triple check here on the

**[42:25]** and we'll just triple check here on the

**[42:25]** and we'll just triple check here on the guide side. They didn't miss anything.

**[42:27]** guide side. They didn't miss anything.

**[42:27]** guide side. They didn't miss anything. We say dagger functions and we have this

**[42:31]** We say dagger functions and we have this

**[42:31]** We say dagger functions and we have this develop one that shows here. So now if I

**[42:34]** develop one that shows here. So now if I

**[42:34]** develop one that shows here. So now if I go into dagger shell which is hopefully

**[42:36]** go into dagger shell which is hopefully

**[42:36]** go into dagger shell which is hopefully what it asks us to do. It is I say

**[42:38]** what it asks us to do. It is I say

**[42:38]** what it asks us to do. It is I say hopefully I wrote this so you know this

**[42:41]** hopefully I wrote this so you know this

**[42:41]** hopefully I wrote this so you know this we're just checking myself here. Um and

**[42:44]** we're just checking myself here. Um and

**[42:44]** we're just checking myself here. Um and I can go in and say dagger. Now before I

**[42:46]** I can go in and say dagger. Now before I

**[42:46]** I can go in and say dagger. Now before I do that um one thing I don't think I

**[42:49]** do that um one thing I don't think I

**[42:49]** do that um one thing I don't think I called out at the very start here was

**[42:51]** called out at the very start here was

**[42:51]** called out at the very start here was that we had to like configure an LM

**[42:53]** that we had to like configure an LM

**[42:53]** that we had to like configure an LM provider. So with Dagger, you bring your

**[42:55]** provider. So with Dagger, you bring your

**[42:55]** provider. So with Dagger, you bring your own model. You can use OpenAI, Gemini,

**[42:57]** own model. You can use OpenAI, Gemini,

**[42:58]** own model. You can use OpenAI, Gemini, Anthropic, um local models, Olama,


### [43:00 - 44:00]

**[43:01]** Anthropic, um local models, Olama,

**[43:01]** Anthropic, um local models, Olama, Docker model runner, like lit literally

**[43:03]** Docker model runner, like lit literally

**[43:03]** Docker model runner, like lit literally any anything you could hook up to

**[43:04]** any anything you could hook up to

**[43:04]** any anything you could hook up to bedrock. Um so you do have to configure

**[43:09]** bedrock. Um so you do have to configure

**[43:09]** bedrock. Um so you do have to configure some environment variables to be able to

**[43:11]** some environment variables to be able to

**[43:11]** some environment variables to be able to for Dagger to make API calls to that,

**[43:13]** for Dagger to make API calls to that,

**[43:13]** for Dagger to make API calls to that, right? Because we're just we're just the

**[43:16]** right? Because we're just we're just the

**[43:16]** right? Because we're just we're just the agent with the tools. The model is

**[43:18]** agent with the tools. The model is

**[43:18]** agent with the tools. The model is living somewhere else. Um, and so this

**[43:21]** living somewhere else. Um, and so this

**[43:21]** living somewhere else. Um, and so this is this configuration page.

**[43:23]** is this configuration page.

**[43:23]** is this configuration page. Configuration,

**[43:25]** Configuration,

**[43:25]** Configuration, uh, shows all the different options on

**[43:27]** uh, shows all the different options on

**[43:27]** uh, shows all the different options on how to configure things. Um, one really

**[43:29]** how to configure things. Um, one really

**[43:29]** how to configure things. Um, one really cool thing to call out, I'm just going

**[43:31]** cool thing to call out, I'm just going

**[43:31]** cool thing to call out, I'm just going to type something really scary.

**[43:41]** Um, oh my gosh. So, Dagger also has cool

**[43:41]** Um, oh my gosh. So, Dagger also has cool secrets provider integrations. So, I

**[43:43]** secrets provider integrations. So, I

**[43:43]** secrets provider integrations. So, I don't have my actual API key uh echoed

**[43:46]** don't have my actual API key uh echoed

**[43:46]** don't have my actual API key uh echoed there. I just have my one password

**[43:48]** there. I just have my one password

**[43:48]** there. I just have my one password reference and it's just sitting in one

**[43:50]** reference and it's just sitting in one

**[43:50]** reference and it's just sitting in one password somewhere. Um and so let's see.

**[43:55]** password somewhere. Um and so let's see.

**[43:55]** password somewhere. Um and so let's see. Yeah. So it's just pointing at this

**[43:56]** Yeah. So it's just pointing at this

**[43:56]** Yeah. So it's just pointing at this credential. Yeah. And then if I reveal

**[43:58]** credential. Yeah. And then if I reveal

**[43:58]** credential. Yeah. And then if I reveal in plain text,


### [44:00 - 45:00]

**[44:01]** in plain text,

**[44:01]** in plain text, um

**[44:03]** um

**[44:03]** um so I I've configured this in my

**[44:04]** so I I've configured this in my

**[44:04]** so I I've configured this in my environment. So now when I say dagger,

**[44:08]** environment. So now when I say dagger,

**[44:08]** environment. So now when I say dagger, um it's going to take a second to spin

**[44:10]** um it's going to take a second to spin

**[44:10]** um it's going to take a second to spin up. And this is the part where if you're

**[44:12]** up. And this is the part where if you're

**[44:12]** up. And this is the part where if you're struggling a bit with Wi-Fi,

**[44:15]** struggling a bit with Wi-Fi,

**[44:15]** struggling a bit with Wi-Fi, this might be a bit tough, but it's okay

**[44:16]** this might be a bit tough, but it's okay

**[44:16]** this might be a bit tough, but it's okay because if you are following along,

**[44:17]** because if you are following along,

**[44:17]** because if you are following along, we're going to push this to GitHub in a

**[44:19]** we're going to push this to GitHub in a

**[44:19]** we're going to push this to GitHub in a second and it's going to run in GitHub

**[44:20]** second and it's going to run in GitHub

**[44:20]** second and it's going to run in GitHub and it's going to be on GitHub's

**[44:22]** and it's going to be on GitHub's

**[44:22]** and it's going to be on GitHub's network. So, we don't have to be uh

**[44:24]** network. So, we don't have to be uh

**[44:24]** network. So, we don't have to be uh beholden to that. But now, can you run

**[44:26]** beholden to that. But now, can you run

**[44:26]** beholden to that. But now, can you run LLM? Yeah, exactly. So, now if I say LLM

**[44:29]** LLM? Yeah, exactly. So, now if I say LLM

**[44:29]** LLM? Yeah, exactly. So, now if I say LLM pipe model for example, uh where you see

**[44:32]** pipe model for example, uh where you see

**[44:32]** pipe model for example, uh where you see my little one password prompt. Nice. So,

**[44:35]** my little one password prompt. Nice. So,

**[44:35]** my little one password prompt. Nice. So, it's got my key. It's going to take a

**[44:37]** it's got my key. It's going to take a

**[44:37]** it's got my key. It's going to take a second to think about it. Uh, and so

**[44:39]** second to think about it. Uh, and so

**[44:39]** second to think about it. Uh, and so with each model provider, we have a

**[44:40]** with each model provider, we have a

**[44:40]** with each model provider, we have a default model, but you can also specify

**[44:42]** default model, but you can also specify

**[44:42]** default model, but you can also specify one. Um, we can also specify one in

**[44:44]** one. Um, we can also specify one in

**[44:44]** one. Um, we can also specify one in code, but right now by default, it's

**[44:46]** code, but right now by default, it's

**[44:46]** code, but right now by default, it's going to use cloud 35. Uh, so maybe

**[44:49]** going to use cloud 35. Uh, so maybe

**[44:49]** going to use cloud 35. Uh, so maybe we're not going to get the best results,

**[44:50]** we're not going to get the best results,

**[44:50]** we're not going to get the best results, but we'll see. Yes, classic. A classic.

**[44:52]** but we'll see. Yes, classic. A classic.

**[44:52]** but we'll see. Yes, classic. A classic. Yes. Um, cool. So now I have that and I

**[44:55]** Yes. Um, cool. So now I have that and I

**[44:55]** Yes. Um, cool. So now I have that and I can say, and we have that new develop

**[44:58]** can say, and we have that new develop

**[44:58]** can say, and we have that new develop function, right? So I can say help


### [45:00 - 46:00]

**[45:01]** function, right? So I can say help

**[45:01]** function, right? So I can say help develop. And so this is the thing we

**[45:04]** develop. And so this is the thing we

**[45:04]** develop. And so this is the thing we just made where Can you bump that up a

**[45:06]** just made where Can you bump that up a

**[45:06]** just made where Can you bump that up a little bit bigger? For sure. Yeah. Yeah,

**[45:08]** little bit bigger? For sure. Yeah. Yeah,

**[45:08]** little bit bigger? For sure. Yeah. Yeah, perfect. Uh, so we have that required

**[45:10]** perfect. Uh, so we have that required

**[45:10]** perfect. Uh, so we have that required argument of assignment and that was our

**[45:12]** argument of assignment and that was our

**[45:12]** argument of assignment and that was our assignment complete. We have an optional

**[45:14]** assignment complete. We have an optional

**[45:14]** assignment complete. We have an optional argument source which again is just

**[45:15]** argument source which again is just

**[45:16]** argument source which again is just going to be my repo and this is going to

**[45:18]** going to be my repo and this is going to

**[45:18]** going to be my repo and this is going to give us back a directory. Uh, so here's

**[45:21]** give us back a directory. Uh, so here's

**[45:21]** give us back a directory. Uh, so here's how I use it. I just say develop and

**[45:22]** how I use it. I just say develop and

**[45:22]** how I use it. I just say develop and then do the assignment. So let's say

**[45:24]** then do the assignment. So let's say

**[45:24]** then do the assignment. So let's say develop

**[45:26]** develop

**[45:26]** develop and then we didn't actually look at the

**[45:27]** and then we didn't actually look at the

**[45:28]** and then we didn't actually look at the project we're daggerizing yet, but I

**[45:29]** project we're daggerizing yet, but I

**[45:29]** project we're daggerizing yet, but I promise it's like uh viewjs website. So

**[45:33]** promise it's like uh viewjs website. So

**[45:33]** promise it's like uh viewjs website. So let's ask it to I think in here we say

**[45:37]** let's ask it to I think in here we say

**[45:37]** let's ask it to I think in here we say um

**[45:39]** um

**[45:39]** um the example thing is to make the main

**[45:40]** the example thing is to make the main

**[45:40]** the example thing is to make the main page blue and I'll say make the main

**[45:44]** page blue and I'll say make the main

**[45:44]** page blue and I'll say make the main page say hello workshop people. Oh

**[45:48]** page say hello workshop people. Oh

**[45:48]** page say hello workshop people. Oh doesn't say that right now. Um and I've

**[45:50]** doesn't say that right now. Um and I've

**[45:50]** doesn't say that right now. Um and I've never run this so I don't maybe it'll

**[45:52]** never run this so I don't maybe it'll

**[45:52]** never run this so I don't maybe it'll succeed. So now we can see this

**[45:54]** succeed. So now we can see this

**[45:54]** succeed. So now we can see this happening. We see our prompts getting

**[45:56]** happening. We see our prompts getting

**[45:56]** happening. We see our prompts getting passed in. We see the little uh person

**[45:58]** passed in. We see the little uh person

**[45:58]** passed in. We see the little uh person face that's the prompting and the little

**[45:59]** face that's the prompting and the little

**[45:59]** face that's the prompting and the little robot head of the model which is claude


### [46:00 - 47:00]

**[46:02]** robot head of the model which is claude

**[46:02]** robot head of the model which is claude 35 sonet saying cool let me do these

**[46:05]** 35 sonet saying cool let me do these

**[46:05]** 35 sonet saying cool let me do these things and we can actually see it

**[46:07]** things and we can actually see it

**[46:07]** things and we can actually see it calling tools right so it's it's uh

**[46:10]** calling tools right so it's it's uh

**[46:10]** calling tools right so it's it's uh looking at the functions available we

**[46:11]** looking at the functions available we

**[46:11]** looking at the functions available we see that workspace list you said yeah

**[46:14]** see that workspace list you said yeah

**[46:14]** see that workspace list you said yeah list files yeah the ones that we made

**[46:16]** list files yeah the ones that we made

**[46:16]** list files yeah the ones that we made um and so it figured out okay I can look

**[46:18]** um and so it figured out okay I can look

**[46:18]** um and so it figured out okay I can look at my files now here's this specific

**[46:21]** at my files now here's this specific

**[46:21]** at my files now here's this specific file I might need to edit so let me read

**[46:23]** file I might need to edit so let me read

**[46:23]** file I might need to edit so let me read that file and so it it now sees the

**[46:26]** that file and so it it now sees the

**[46:26]** that file and so it it now sees the contents of this. And while this is

**[46:27]** contents of this. And while this is

**[46:27]** contents of this. And while this is running, let me just open up cloud and

**[46:30]** running, let me just open up cloud and

**[46:30]** running, let me just open up cloud and hopefully this will load

**[46:33]** hopefully this will load

**[46:33]** hopefully this will load so we can actually see like the the

**[46:35]** so we can actually see like the the

**[46:35]** so we can actually see like the the cloud visualization of this because it's

**[46:37]** cloud visualization of this because it's

**[46:37]** cloud visualization of this because it's maybe a bit easier to see because we

**[46:39]** maybe a bit easier to see because we

**[46:39]** maybe a bit easier to see because we it's sign in.

**[46:46]** I'm clicking the button. I think my

**[46:46]** I'm clicking the button. I think my Wi-Fi is failing me on this O flow, but

**[46:49]** Wi-Fi is failing me on this O flow, but

**[46:49]** Wi-Fi is failing me on this O flow, but while it's running, we'll just watch

**[46:50]** while it's running, we'll just watch

**[46:50]** while it's running, we'll just watch this. It's the same it's the same open

**[46:52]** this. It's the same it's the same open

**[46:52]** this. It's the same it's the same open telemetry in both places. So that you're

**[46:55]** telemetry in both places. So that you're

**[46:55]** telemetry in both places. So that you're getting streaming to your terminal UI

**[46:57]** getting streaming to your terminal UI

**[46:57]** getting streaming to your terminal UI and the web UI. We see it call write

**[46:59]** and the web UI. We see it call write

**[46:59]** and the web UI. We see it call write file with some new file contents. And


### [47:00 - 48:00]

**[47:02]** file with some new file contents. And

**[47:02]** file with some new file contents. And now says now that we've made the change,

**[47:04]** now says now that we've made the change,

**[47:04]** now says now that we've made the change, let's run the test. And this is the part

**[47:06]** let's run the test. And this is the part

**[47:06]** let's run the test. And this is the part that that really might fail on this

**[47:07]** that that really might fail on this

**[47:07]** that that really might fail on this Wi-Fi because it's inst. It's doing an

**[47:09]** Wi-Fi because it's inst. It's doing an

**[47:09]** Wi-Fi because it's inst. It's doing an npm install and downloading a bunch of

**[47:11]** npm install and downloading a bunch of

**[47:11]** npm install and downloading a bunch of npm modules or node modules. But it's uh

**[47:14]** npm modules or node modules. But it's uh

**[47:14]** npm modules or node modules. But it's uh it should pass in a second. Uh we'll

**[47:16]** it should pass in a second. Uh we'll

**[47:16]** it should pass in a second. Uh we'll just let it go and we'll talk through

**[47:17]** just let it go and we'll talk through

**[47:17]** just let it go and we'll talk through it. But we we can see that our agent is

**[47:21]** it. But we we can see that our agent is

**[47:21]** it. But we we can see that our agent is actually it wrote the files and then

**[47:22]** actually it wrote the files and then

**[47:22]** actually it wrote the files and then it's writing it's running the tests

**[47:24]** it's writing it's running the tests

**[47:24]** it's writing it's running the tests which is really awesome. Uh cool. So

**[47:26]** which is really awesome. Uh cool. So

**[47:26]** which is really awesome. Uh cool. So this opened up over here

**[47:29]** this opened up over here

**[47:29]** this opened up over here with npm installed. Yeah. Was part of

**[47:31]** with npm installed. Yeah. Was part of

**[47:31]** with npm installed. Yeah. Was part of the tool that you gave it or um so this

**[47:34]** the tool that you gave it or um so this

**[47:34]** the tool that you gave it or um so this is Oh yeah. So let's So we see it's

**[47:36]** is Oh yeah. So let's So we see it's

**[47:36]** is Oh yeah. So let's So we see it's saying like with exec npm install with

**[47:38]** saying like with exec npm install with

**[47:38]** saying like with exec npm install with exec npm run test unit. If we go back to

**[47:43]** exec npm run test unit. If we go back to

**[47:43]** exec npm run test unit. If we go back to our workspace

**[47:48]** in our test function, that was part of

**[47:48]** in our test function, that was part of it. So this is like the agent just had

**[47:51]** it. So this is like the agent just had

**[47:51]** it. So this is like the agent just had to call test and we've defined what

**[47:53]** to call test and we've defined what

**[47:53]** to call test and we've defined what happens when you call test and so it's

**[47:56]** happens when you call test and so it's

**[47:56]** happens when you call test and so it's not like the random ones like you know

**[47:57]** not like the random ones like you know

**[47:57]** not like the random ones like you know sometimes you're like you know make sure

**[47:59]** sometimes you're like you know make sure

**[47:59]** sometimes you're like you know make sure test and it's like I'm going to try pi


### [48:00 - 49:00]

**[48:01]** test and it's like I'm going to try pi

**[48:01]** test and it's like I'm going to try pi test with these crazy options and you're

**[48:03]** test with these crazy options and you're

**[48:03]** test with these crazy options and you're like why did you think that was going to

**[48:04]** like why did you think that was going to

**[48:04]** like why did you think that was going to work? Instead you just give it you know

**[48:06]** work? Instead you just give it you know

**[48:06]** work? Instead you just give it you know exactly what it should be. We could give

**[48:07]** exactly what it should be. We could give

**[48:07]** exactly what it should be. We could give it more flexibility in how it runs

**[48:09]** it more flexibility in how it runs

**[48:09]** it more flexibility in how it runs things, but in this case like we already

**[48:11]** things, but in this case like we already

**[48:11]** things, but in this case like we already know like this is how you run tests in

**[48:13]** know like this is how you run tests in

**[48:13]** know like this is how you run tests in the project. So we just give it a test

**[48:15]** the project. So we just give it a test

**[48:15]** the project. So we just give it a test fun. Like that's probably the biggest

**[48:17]** fun. Like that's probably the biggest

**[48:17]** fun. Like that's probably the biggest thing in like creating reliable agents

**[48:19]** thing in like creating reliable agents

**[48:19]** thing in like creating reliable agents with Dagger is like

**[48:22]** with Dagger is like

**[48:22]** with Dagger is like giving flexibility where it's important

**[48:24]** giving flexibility where it's important

**[48:24]** giving flexibility where it's important for completing tasks and removing it

**[48:26]** for completing tasks and removing it

**[48:26]** for completing tasks and removing it where you know exactly how things are

**[48:27]** where you know exactly how things are

**[48:27]** where you know exactly how things are meant to happen. So you know exactly how

**[48:29]** meant to happen. So you know exactly how

**[48:30]** meant to happen. So you know exactly how tests need to run. Uh so it doesn't need

**[48:32]** tests need to run. Uh so it doesn't need

**[48:32]** tests need to run. Uh so it doesn't need the freedom to just run any command in a

**[48:34]** the freedom to just run any command in a

**[48:34]** the freedom to just run any command in a container. we know, okay, all you need

**[48:36]** container. we know, okay, all you need

**[48:36]** container. we know, okay, all you need to do is modify files and run this test

**[48:39]** to do is modify files and run this test

**[48:39]** to do is modify files and run this test function. Um, and for more complex

**[48:42]** function. Um, and for more complex

**[48:42]** function. Um, and for more complex agents, maybe there's some other

**[48:43]** agents, maybe there's some other

**[48:43]** agents, maybe there's some other functions there, too. But for this one,

**[48:45]** functions there, too. But for this one,

**[48:46]** functions there, too. But for this one, like this is the amount of freedom we've

**[48:47]** like this is the amount of freedom we've

**[48:47]** like this is the amount of freedom we've given it. Can we can we like open

**[48:49]** given it. Can we can we like open

**[48:49]** given it. Can we can we like open another uh Well, hold on. So, we got

**[48:51]** another uh Well, hold on. So, we got

**[48:51]** another uh Well, hold on. So, we got cloud. Okay. Okay. We got cloud. So,

**[48:53]** cloud. Okay. Okay. We got cloud. So,

**[48:53]** cloud. Okay. Okay. We got cloud. So, yeah. Well, we'll get back to my pipe

**[48:55]** yeah. Well, we'll get back to my pipe

**[48:55]** yeah. Well, we'll get back to my pipe dream in a second. Okay. So, let me see

**[48:57]** dream in a second. Okay. So, let me see

**[48:57]** dream in a second. Okay. So, let me see if I can expand this. Uh, and so this is


### [49:00 - 50:00]

**[49:00]** if I can expand this. Uh, and so this is

**[49:00]** if I can expand this. Uh, and so this is like the visibility that we want to see

**[49:02]** like the visibility that we want to see

**[49:02]** like the visibility that we want to see when we're running these agents. So we

**[49:03]** when we're running these agents. So we

**[49:04]** when we're running these agents. So we saw the prompt and we saw the assignment

**[49:06]** saw the prompt and we saw the assignment

**[49:06]** saw the prompt and we saw the assignment is to make the main page say hello

**[49:08]** is to make the main page say hello

**[49:08]** is to make the main page say hello workshop people. Cool. And then so this

**[49:10]** workshop people. Cool. And then so this

**[49:10]** workshop people. Cool. And then so this is the prompt we gave it. Now Claude 3.5

**[49:12]** is the prompt we gave it. Now Claude 3.5

**[49:12]** is the prompt we gave it. Now Claude 3.5 is looking at this and saying first

**[49:14]** is looking at this and saying first

**[49:14]** is looking at this and saying first let's look at what objects we have and

**[49:17]** let's look at what objects we have and

**[49:17]** let's look at what objects we have and check out the workspace make the changes

**[49:19]** check out the workspace make the changes

**[49:19]** check out the workspace make the changes and then run the tests. Sounds good. It

**[49:21]** and then run the tests. Sounds good. It

**[49:21]** and then run the tests. Sounds good. It runs list objects which lets it see uh

**[49:25]** runs list objects which lets it see uh

**[49:25]** runs list objects which lets it see uh what it has in its environment which is

**[49:27]** what it has in its environment which is

**[49:27]** what it has in its environment which is like this this workspace tool, right?

**[49:30]** like this this workspace tool, right?

**[49:30]** like this this workspace tool, right? Cool. And then it's going to say list

**[49:31]** Cool. And then it's going to say list

**[49:31]** Cool. And then it's going to say list method. So it's going to see what it can

**[49:33]** method. So it's going to see what it can

**[49:33]** method. So it's going to see what it can do with a workspace. Like what the heck

**[49:35]** do with a workspace. Like what the heck

**[49:35]** do with a workspace. Like what the heck is a workspace? It says it has tools to

**[49:37]** is a workspace? It says it has tools to

**[49:37]** is a workspace? It says it has tools to edit and test code. And then we expand

**[49:40]** edit and test code. And then we expand

**[49:40]** edit and test code. And then we expand that. And so this is like this kind of

**[49:42]** that. And so this is like this kind of

**[49:42]** that. And so this is like this kind of visibility into the agents environment

**[49:44]** visibility into the agents environment

**[49:44]** visibility into the agents environment where we say, "Oh, there's this

**[49:45]** where we say, "Oh, there's this

**[49:45]** where we say, "Oh, there's this workspace write file function that gives

**[49:47]** workspace write file function that gives

**[49:47]** workspace write file function that gives it back a workspace type and these are

**[49:50]** it back a workspace type and these are

**[49:50]** it back a workspace type and these are the arguments." Oh, you mean so we

**[49:51]** the arguments." Oh, you mean so we

**[49:51]** the arguments." Oh, you mean so we didn't have to write any of the JSON

**[49:53]** didn't have to write any of the JSON

**[49:53]** didn't have to write any of the JSON kind of, you know, description of tools.

**[49:55]** kind of, you know, description of tools.

**[49:55]** kind of, you know, description of tools. It just gets generated from the

**[49:56]** It just gets generated from the

**[49:56]** It just gets generated from the functions. Yeah. So we just gave it that

**[49:58]** functions. Yeah. So we just gave it that

**[49:58]** functions. Yeah. So we just gave it that that Dagger module and then it all got


### [50:00 - 51:00]

**[50:00]** that Dagger module and then it all got

**[50:00]** that Dagger module and then it all got wired up into the agents environment.

**[50:03]** wired up into the agents environment.

**[50:03]** wired up into the agents environment. And so that's cool. Let me select these

**[50:04]** And so that's cool. Let me select these

**[50:04]** And so that's cool. Let me select these methods. So now I have these as tools to

**[50:06]** methods. So now I have these as tools to

**[50:06]** methods. So now I have these as tools to call and then let's see what's in the

**[50:08]** call and then let's see what's in the

**[50:08]** call and then let's see what's in the project. So it's going to call workspace

**[50:10]** project. So it's going to call workspace

**[50:10]** project. So it's going to call workspace list files. And remember the the way

**[50:13]** list files. And remember the the way

**[50:13]** list files. And remember the the way that it does that in our workspace code

**[50:15]** that it does that in our workspace code

**[50:15]** that it does that in our workspace code was it creates like an Alpine container

**[50:16]** was it creates like an Alpine container

**[50:16]** was it creates like an Alpine container and runs tree. And so we can see the

**[50:19]** and runs tree. And so we can see the

**[50:19]** and runs tree. And so we can see the tracing of that too which is like the

**[50:21]** tracing of that too which is like the

**[50:21]** tracing of that too which is like the underlying uh actions of the tools being

**[50:24]** underlying uh actions of the tools being

**[50:24]** underlying uh actions of the tools being called. We also see the return of that

**[50:26]** called. We also see the return of that

**[50:26]** called. We also see the return of that which is what the agent sees and it sees

**[50:28]** which is what the agent sees and it sees

**[50:28]** which is what the agent sees and it sees this whole file structure. Cool. And

**[50:30]** this whole file structure. Cool. And

**[50:30]** this whole file structure. Cool. And then we can see says cool sounds to make

**[50:34]** then we can see says cool sounds to make

**[50:34]** then we can see says cool sounds to make it say that we should probably modify

**[50:36]** it say that we should probably modify

**[50:36]** it say that we should probably modify this one or this one. So let's see

**[50:38]** this one or this one. So let's see

**[50:38]** this one or this one. So let's see what's in those files. We can see it

**[50:40]** what's in those files. We can see it

**[50:40]** what's in those files. We can see it read the file and that's uh it's going

**[50:44]** read the file and that's uh it's going

**[50:44]** read the file and that's uh it's going to see this whole file of

**[50:47]** to see this whole file of

**[50:47]** to see this whole file of um the work hello world.view that says

**[50:51]** um the work hello world.view that says

**[50:51]** um the work hello world.view that says okay I don't think that was it. Let's

**[50:52]** okay I don't think that was it. Let's

**[50:52]** okay I don't think that was it. Let's see the app.view view and then it reads

**[50:55]** see the app.view view and then it reads

**[50:55]** see the app.view view and then it reads that file and then eventually it says I

**[50:57]** that file and then eventually it says I

**[50:57]** that file and then eventually it says I see that that world that app.view uses


### [51:00 - 52:00]

**[51:00]** see that that world that app.view uses

**[51:00]** see that that world that app.view uses the hello world component and passes a

**[51:02]** the hello world component and passes a

**[51:02]** the hello world component and passes a message to it. So now it's going to

**[51:04]** message to it. So now it's going to

**[51:04]** message to it. So now it's going to write the file. It's going to change

**[51:06]** write the file. It's going to change

**[51:06]** write the file. It's going to change app.view to pass a different message to

**[51:08]** app.view to pass a different message to

**[51:08]** app.view to pass a different message to it. Um and let's see, we can expand this

**[51:11]** it. Um and let's see, we can expand this

**[51:11]** it. Um and let's see, we can expand this to see the whole thing. Yes. Awesome.

**[51:14]** to see the whole thing. Yes. Awesome.

**[51:14]** to see the whole thing. Yes. Awesome. Nice. So hopefully if this ever if it

**[51:17]** Nice. So hopefully if this ever if it

**[51:17]** Nice. So hopefully if this ever if it doesn't finish, it's fine because we're

**[51:18]** doesn't finish, it's fine because we're

**[51:18]** doesn't finish, it's fine because we're going to push it to GitHub in a second.

**[51:20]** going to push it to GitHub in a second.

**[51:20]** going to push it to GitHub in a second. Um and then GitHub can run it for us.

**[51:23]** Um and then GitHub can run it for us.

**[51:23]** Um and then GitHub can run it for us. But now it's running those tests. So

**[51:24]** But now it's running those tests. So

**[51:24]** But now it's running those tests. So this is the part that it's currently at

**[51:25]** this is the part that it's currently at

**[51:25]** this is the part that it's currently at in my shell where it's been running for

**[51:27]** in my shell where it's been running for

**[51:28]** in my shell where it's been running for like five minutes. Um, so yeah, that

**[51:30]** like five minutes. Um, so yeah, that

**[51:30]** like five minutes. Um, so yeah, that that's the the visibility part I'm

**[51:31]** that's the the visibility part I'm

**[51:31]** that's the the visibility part I'm talking about where we can see exactly

**[51:33]** talking about where we can see exactly

**[51:33]** talking about where we can see exactly what the agent sees and what's happening

**[51:35]** what the agent sees and what's happening

**[51:35]** what the agent sees and what's happening under the hood. Um, so this is to be

**[51:38]** under the hood. Um, so this is to be

**[51:38]** under the hood. Um, so this is to be clear, right? So this is all running on

**[51:40]** clear, right? So this is all running on

**[51:40]** clear, right? So this is all running on your laptop and yet it's all inside that

**[51:44]** your laptop and yet it's all inside that

**[51:44]** your laptop and yet it's all inside that Dagger engine in containers totally

**[51:47]** Dagger engine in containers totally

**[51:47]** Dagger engine in containers totally isolated from your laptop. Dagger cloud

**[51:49]** isolated from your laptop. Dagger cloud

**[51:49]** isolated from your laptop. Dagger cloud is just showing me the visualization.

**[51:52]** is just showing me the visualization.

**[51:52]** is just showing me the visualization. It's not running anything for me. This

**[51:54]** It's not running anything for me. This

**[51:54]** It's not running anything for me. This is on my machine, which is why it's

**[51:55]** is on my machine, which is why it's

**[51:55]** is on my machine, which is why it's still running. Well, right. And and this

**[51:57]** still running. Well, right. And and this

**[51:57]** still running. Well, right. And and this is like because of the connection we

**[51:59]** is like because of the connection we

**[51:59]** is like because of the connection we have and because of, you know, whatever


### [52:00 - 53:00]

**[52:01]** have and because of, you know, whatever

**[52:01]** have and because of, you know, whatever the load we're putting on it. But it's

**[52:03]** the load we're putting on it. But it's

**[52:03]** the load we're putting on it. But it's the other thing to think about is it

**[52:06]** the other thing to think about is it

**[52:06]** the other thing to think about is it could be like uh we're using Python

**[52:08]** could be like uh we're using Python

**[52:08]** could be like uh we're using Python here. We're using Node, right? We're

**[52:10]** here. We're using Node, right? We're

**[52:10]** here. We're using Node, right? We're using a bunch of different tools. So

**[52:11]** using a bunch of different tools. So

**[52:12]** using a bunch of different tools. So like the app is Node, but the the uh the

**[52:15]** like the app is Node, but the the uh the

**[52:15]** like the app is Node, but the the uh the workflows that Kyle's writing are in

**[52:17]** workflows that Kyle's writing are in

**[52:17]** workflows that Kyle's writing are in Python. You could have a laptop say or

**[52:20]** Python. You could have a laptop say or

**[52:20]** Python. You could have a laptop say or any server that just has Dagger and a

**[52:24]** any server that just has Dagger and a

**[52:24]** any server that just has Dagger and a connection to the internet and you don't

**[52:26]** connection to the internet and you don't

**[52:26]** connection to the internet and you don't need any tools installed. So that's why

**[52:28]** need any tools installed. So that's why

**[52:28]** need any tools installed. So that's why the environments environments is not

**[52:30]** the environments environments is not

**[52:30]** the environments environments is not just for the agent developer. I mean it

**[52:32]** just for the agent developer. I mean it

**[52:32]** just for the agent developer. I mean it kind of goes all the way through. So you

**[52:34]** kind of goes all the way through. So you

**[52:34]** kind of goes all the way through. So you could have a brand new laptop with just

**[52:36]** could have a brand new laptop with just

**[52:36]** could have a brand new laptop with just Dagger and it would because it's using a

**[52:40]** Dagger and it would because it's using a

**[52:40]** Dagger and it would because it's using a Python runtime container for the

**[52:42]** Python runtime container for the

**[52:42]** Python runtime container for the workflow he wrote in Python. That's just

**[52:44]** workflow he wrote in Python. That's just

**[52:44]** workflow he wrote in Python. That's just implicitly there. So you don't need to

**[52:46]** implicitly there. So you don't need to

**[52:46]** implicitly there. So you don't need to install Python. You don't need to

**[52:48]** install Python. You don't need to

**[52:48]** install Python. You don't need to struggle with VMs or any other versions

**[52:50]** struggle with VMs or any other versions

**[52:50]** struggle with VMs or any other versions or whatever. It just it's done. And then

**[52:52]** or whatever. It just it's done. And then

**[52:52]** or whatever. It just it's done. And then inside of that somewhere there's node

**[52:54]** inside of that somewhere there's node

**[52:54]** inside of that somewhere there's node container that happened, right? In order

**[52:56]** container that happened, right? In order

**[52:56]** container that happened, right? In order to create this environment, the build

**[52:58]** to create this environment, the build

**[52:58]** to create this environment, the build and the build and all that. And that

**[52:59]** and the build and all that. And that

**[52:59]** and the build and all that. And that again, it's all just nested inside of


### [53:00 - 54:00]

**[53:02]** again, it's all just nested inside of

**[53:02]** again, it's all just nested inside of there and and cached and everything else

**[53:05]** there and and cached and everything else

**[53:05]** there and and cached and everything else automatically. So you can you could kind

**[53:07]** automatically. So you can you could kind

**[53:07]** automatically. So you can you could kind of just do this with a very bare bones

**[53:09]** of just do this with a very bare bones

**[53:09]** of just do this with a very bare bones machine setup and everything will just

**[53:12]** machine setup and everything will just

**[53:12]** machine setup and everything will just work. Yeah. So what we can see that we

**[53:15]** work. Yeah. So what we can see that we

**[53:15]** work. Yeah. So what we can see that we probably won't get to run this part

**[53:17]** probably won't get to run this part

**[53:17]** probably won't get to run this part locally just because um I don't we we'll

**[53:19]** locally just because um I don't we we'll

**[53:20]** locally just because um I don't we we'll come back to it if it finishes but

**[53:21]** come back to it if it finishes but

**[53:21]** come back to it if it finishes but anyway I'll just describe this flow here

**[53:23]** anyway I'll just describe this flow here

**[53:23]** anyway I'll just describe this flow here where we say okay we're in shell that

**[53:25]** where we say okay we're in shell that

**[53:25]** where we say okay we're in shell that happened like we we ran that develop

**[53:28]** happened like we we ran that develop

**[53:28]** happened like we we ran that develop thing and it it gave us back something

**[53:30]** thing and it it gave us back something

**[53:30]** thing and it it gave us back something but now in dagger like I keep saying

**[53:33]** but now in dagger like I keep saying

**[53:33]** but now in dagger like I keep saying we're in shell dagger when you type

**[53:35]** we're in shell dagger when you type

**[53:35]** we're in shell dagger when you type dagger and get into that um this view it

**[53:39]** dagger and get into that um this view it

**[53:39]** dagger and get into that um this view it is a shell just like bash right where we

**[53:42]** is a shell just like bash right where we

**[53:42]** is a shell just like bash right where we can

**[53:43]** can

**[53:43]** can do things like create variables and

**[53:45]** do things like create variables and

**[53:45]** do things like create variables and chain things together. And so what we

**[53:47]** chain things together. And so what we

**[53:47]** chain things together. And so what we could do if this finished is say, okay,

**[53:51]** could do if this finished is say, okay,

**[53:51]** could do if this finished is say, okay, let's actually save that the output of

**[53:53]** let's actually save that the output of

**[53:53]** let's actually save that the output of this thing because remember it returns a

**[53:54]** this thing because remember it returns a

**[53:54]** this thing because remember it returns a directory. Save that to a variable

**[53:56]** directory. Save that to a variable

**[53:56]** directory. Save that to a variable called completed. And then we could pass

**[53:58]** called completed. And then we could pass

**[53:58]** called completed. And then we could pass that to our other functions because


### [54:00 - 55:00]

**[54:00]** that to our other functions because

**[54:00]** that to our other functions because remember they they default to using our

**[54:02]** remember they they default to using our

**[54:02]** remember they they default to using our git source from our machine. But we

**[54:04]** git source from our machine. But we

**[54:04]** git source from our machine. But we could we could pass in that optional

**[54:06]** could we could pass in that optional

**[54:06]** could we could pass in that optional directory to all of our functions to say

**[54:08]** directory to all of our functions to say

**[54:08]** directory to all of our functions to say use this directory instead. So now I

**[54:11]** use this directory instead. So now I

**[54:11]** use this directory instead. So now I could actually run the whole thing uh as

**[54:14]** could actually run the whole thing uh as

**[54:14]** could actually run the whole thing uh as like a local like I could see the

**[54:15]** like a local like I could see the

**[54:15]** like a local like I could see the results of this before even saving it to

**[54:17]** results of this before even saving it to

**[54:17]** results of this before even saving it to my machine. So let me just go over here.

**[54:20]** my machine. So let me just go over here.

**[54:20]** my machine. So let me just go over here. I don't know why I keep ending up in

**[54:21]** I don't know why I keep ending up in

**[54:21]** I don't know why I keep ending up in this folder but we'll go uh to the

**[54:24]** this folder but we'll go uh to the

**[54:24]** this folder but we'll go uh to the correct directory

**[54:31]** and we'll open another shell here and

**[54:31]** and we'll open another shell here and I'll just type in part of this command.

**[54:34]** I'll just type in part of this command.

**[54:34]** I'll just type in part of this command. Um because what what I can do is I can

**[54:37]** Um because what what I can do is I can

**[54:37]** Um because what what I can do is I can run the output from the agent as like I

**[54:40]** run the output from the agent as like I

**[54:40]** run the output from the agent as like I can run the whole site. I can build it

**[54:41]** can run the whole site. I can build it

**[54:41]** can run the whole site. I can build it and serve it to my machine. Uh and I can

**[54:43]** and serve it to my machine. Uh and I can

**[54:44]** and serve it to my machine. Uh and I can see what it's built before I even save

**[54:45]** see what it's built before I even save

**[54:45]** see what it's built before I even save it back to my disk to say yes, this is a

**[54:48]** it back to my disk to say yes, this is a

**[54:48]** it back to my disk to say yes, this is a good solution. Um so once we uh get this

**[54:52]** good solution. Um so once we uh get this

**[54:52]** good solution. Um so once we uh get this connection here,

**[54:54]** connection here,

**[54:54]** connection here, just waiting on pipes to connect to each

**[54:57]** just waiting on pipes to connect to each

**[54:57]** just waiting on pipes to connect to each other. Um


### [55:00 - 56:00]

**[55:00]** other. Um

**[55:00]** other. Um and we'll we'll let that run for a

**[55:01]** and we'll we'll let that run for a

**[55:01]** and we'll we'll let that run for a second. But uh the main thing is we we

**[55:04]** second. But uh the main thing is we we

**[55:04]** second. But uh the main thing is we we can pass this around. We can run all of

**[55:05]** can pass this around. We can run all of

**[55:05]** can pass this around. We can run all of our functions with that completed

**[55:07]** our functions with that completed

**[55:07]** our functions with that completed directory and then finally say all right

**[55:09]** directory and then finally say all right

**[55:09]** directory and then finally say all right we say export that saves it back to your

**[55:11]** we say export that saves it back to your

**[55:12]** we say export that saves it back to your disk and we're done. So the next step is

**[55:14]** disk and we're done. So the next step is

**[55:14]** disk and we're done. So the next step is all right we're good with that. We we

**[55:16]** all right we're good with that. We we

**[55:16]** all right we're good with that. We we know how to use this agent locally to

**[55:18]** know how to use this agent locally to

**[55:18]** know how to use this agent locally to ask it to make cool tasks. That's fine.

**[55:21]** ask it to make cool tasks. That's fine.

**[55:21]** ask it to make cool tasks. That's fine. But my my people requesting features on

**[55:24]** But my my people requesting features on

**[55:24]** But my my people requesting features on my site they don't have this installed.

**[55:26]** my site they don't have this installed.

**[55:26]** my site they don't have this installed. They don't have Docker and Dagger

**[55:28]** They don't have Docker and Dagger

**[55:28]** They don't have Docker and Dagger installed on their machine. They don't

**[55:29]** installed on their machine. They don't

**[55:29]** installed on their machine. They don't want to use Dagger shell. they just want

**[55:31]** want to use Dagger shell. they just want

**[55:31]** want to use Dagger shell. they just want to go to GitHub and say make this new

**[55:33]** to go to GitHub and say make this new

**[55:33]** to go to GitHub and say make this new feature. So that's the next step here

**[55:35]** feature. So that's the next step here

**[55:35]** feature. So that's the next step here and and it sounds ambitious but it's

**[55:38]** and and it sounds ambitious but it's

**[55:38]** and and it sounds ambitious but it's really quick. Um so we've got plenty of

**[55:40]** really quick. Um so we've got plenty of

**[55:40]** really quick. Um so we've got plenty of time to to look at the solution here and

**[55:42]** time to to look at the solution here and

**[55:42]** time to to look at the solution here and we'll look at it in Python once again.

**[55:44]** we'll look at it in Python once again.

**[55:44]** we'll look at it in Python once again. And so the first thing we're going to do

**[55:46]** And so the first thing we're going to do

**[55:46]** And so the first thing we're going to do is actually install another dependency

**[55:48]** is actually install another dependency

**[55:48]** is actually install another dependency from the Daggerverse. And this is my

**[55:51]** from the Daggerverse. And this is my

**[55:51]** from the Daggerverse. And this is my module called GitHub issue. And it's

**[55:54]** module called GitHub issue. And it's

**[55:54]** module called GitHub issue. And it's basically if we go to Daggerverse, we

**[55:56]** basically if we go to Daggerverse, we

**[55:56]** basically if we go to Daggerverse, we saw it installed earlier when you showed

**[55:58]** saw it installed earlier when you showed

**[55:58]** saw it installed earlier when you showed us that Dagger JSON with the Exactly.


### [56:00 - 57:00]

**[56:00]** us that Dagger JSON with the Exactly.

**[56:00]** us that Dagger JSON with the Exactly. But that's because I skipped ahead. Oh,

**[56:01]** But that's because I skipped ahead. Oh,

**[56:01]** But that's because I skipped ahead. Oh, I see. Yeah. Nice.

**[56:05]** I see. Yeah. Nice.

**[56:05]** I see. Yeah. Nice. Um, so if we search for that and we have

**[56:07]** Um, so if we search for that and we have

**[56:07]** Um, so if we search for that and we have this module called GitHub issue, uh,

**[56:10]** this module called GitHub issue, uh,

**[56:10]** this module called GitHub issue, uh, it's got a bunch of functions that let

**[56:12]** it's got a bunch of functions that let

**[56:12]** it's got a bunch of functions that let us do things with GitHub issues like um,

**[56:16]** us do things with GitHub issues like um,

**[56:16]** us do things with GitHub issues like um, we can list GitHub issues in a repo. We

**[56:19]** we can list GitHub issues in a repo. We

**[56:19]** we can list GitHub issues in a repo. We can list the comments on a particular

**[56:20]** can list the comments on a particular

**[56:20]** can list the comments on a particular issue. We can write comments. Uh we can

**[56:24]** issue. We can write comments. Uh we can

**[56:24]** issue. We can write comments. Uh we can create pull request comments. Um all

**[56:26]** create pull request comments. Um all

**[56:26]** create pull request comments. Um all kinds of things with GitHub issues and

**[56:28]** kinds of things with GitHub issues and

**[56:28]** kinds of things with GitHub issues and GitHub pull requests. So with this

**[56:30]** GitHub pull requests. So with this

**[56:30]** GitHub pull requests. So with this module where I've just basically used

**[56:32]** module where I've just basically used

**[56:32]** module where I've just basically used the uh GitHub Go SDK in this Go module

**[56:37]** the uh GitHub Go SDK in this Go module

**[56:37]** the uh GitHub Go SDK in this Go module to connect my Dagger Functions to the

**[56:40]** to connect my Dagger Functions to the

**[56:40]** to connect my Dagger Functions to the API calls. I can install this in my

**[56:42]** API calls. I can install this in my

**[56:42]** API calls. I can install this in my Python project. And now I I can have the

**[56:46]** Python project. And now I I can have the

**[56:46]** Python project. And now I I can have the ability to work with GitHub issues. And

**[56:48]** ability to work with GitHub issues. And

**[56:48]** ability to work with GitHub issues. And so all it needs is a GitHub token. And

**[56:50]** so all it needs is a GitHub token. And

**[56:50]** so all it needs is a GitHub token. And so we create we add another function to

**[56:53]** so we create we add another function to

**[56:53]** so we create we add another function to our code um called develop issue. So

**[56:56]** our code um called develop issue. So

**[56:56]** our code um called develop issue. So remember we created develop now it's

**[56:57]** remember we created develop now it's

**[56:57]** remember we created develop now it's develop issue and all this is going to


### [57:00 - 58:00]

**[57:00]** develop issue and all this is going to

**[57:00]** develop issue and all this is going to do is say we have a GitHub issue out

**[57:02]** do is say we have a GitHub issue out

**[57:02]** do is say we have a GitHub issue out there with our feature request. We want

**[57:04]** there with our feature request. We want

**[57:04]** there with our feature request. We want to read that GitHub issue give it to our

**[57:06]** to read that GitHub issue give it to our

**[57:06]** to read that GitHub issue give it to our agent. The agent's going to do all its

**[57:08]** agent. The agent's going to do all its

**[57:08]** agent. The agent's going to do all its things then give us back a directory.

**[57:10]** things then give us back a directory.

**[57:10]** things then give us back a directory. We're going to take that directory and

**[57:11]** We're going to take that directory and

**[57:11]** We're going to take that directory and make a pull request. Oh, so like really

**[57:13]** make a pull request. Oh, so like really

**[57:13]** make a pull request. Oh, so like really similar to like the assignment that we

**[57:15]** similar to like the assignment that we

**[57:15]** similar to like the assignment that we gave it, instead it's going to be

**[57:17]** gave it, instead it's going to be

**[57:17]** gave it, instead it's going to be reading the GitHub issue and instead of

**[57:19]** reading the GitHub issue and instead of

**[57:19]** reading the GitHub issue and instead of just getting the directory back

**[57:20]** just getting the directory back

**[57:20]** just getting the directory back ourselves, we put the directory into a

**[57:22]** ourselves, we put the directory into a

**[57:22]** ourselves, we put the directory into a PR. So we can see the code here. Um, and

**[57:24]** PR. So we can see the code here. Um, and

**[57:24]** PR. So we can see the code here. Um, and so this is the entire thing here where

**[57:26]** so this is the entire thing here where

**[57:26]** so this is the entire thing here where we're not writing a new agent to do

**[57:28]** we're not writing a new agent to do

**[57:28]** we're not writing a new agent to do this. We're using our other agent. We're

**[57:29]** this. We're using our other agent. We're

**[57:29]** this. We're using our other agent. We're just we're we're wrapping it with some

**[57:32]** just we're we're wrapping it with some

**[57:32]** just we're we're wrapping it with some other pieces to say go here to get the

**[57:34]** other pieces to say go here to get the

**[57:34]** other pieces to say go here to get the assignment. Once it's done, put that

**[57:36]** assignment. Once it's done, put that

**[57:36]** assignment. Once it's done, put that completed work over here. uh which is

**[57:39]** completed work over here. uh which is

**[57:39]** completed work over here. uh which is the from here was like read a get of

**[57:41]** the from here was like read a get of

**[57:42]** the from here was like read a get of issue uh and then we get that assignment

**[57:45]** issue uh and then we get that assignment

**[57:45]** issue uh and then we get that assignment and I can open in the editor so it's

**[57:47]** and I can open in the editor so it's

**[57:47]** and I can open in the editor so it's probably easier to see um

**[57:51]** probably easier to see um

**[57:51]** probably easier to see um okay so we we get that uh get of issue

**[57:54]** okay so we we get that uh get of issue

**[57:54]** okay so we we get that uh get of issue from that issue we get the assignment

**[57:55]** from that issue we get the assignment

**[57:55]** from that issue we get the assignment from the issue body uh we pass that to

**[57:58]** from the issue body uh we pass that to

**[57:58]** from the issue body uh we pass that to our develop function because this is our

**[57:59]** our develop function because this is our

**[57:59]** our develop function because this is our agent and say here's your assignment


### [58:00 - 59:00]

**[58:02]** agent and say here's your assignment

**[58:02]** agent and say here's your assignment here's the source uh which came from

**[58:05]** here's the source uh which came from

**[58:05]** here's the source uh which came from that same defaulted uh input argument.

**[58:09]** that same defaulted uh input argument.

**[58:09]** that same defaulted uh input argument. Uh and then we

**[58:12]** Uh and then we

**[58:12]** Uh and then we uh get the issue title and URL uh which

**[58:15]** uh get the issue title and URL uh which

**[58:15]** uh get the issue title and URL uh which is going to be really cool because then

**[58:17]** is going to be really cool because then

**[58:17]** is going to be really cool because then we can actually in GitHub automatically

**[58:19]** we can actually in GitHub automatically

**[58:19]** we can actually in GitHub automatically have the new pull request linked to the

**[58:21]** have the new pull request linked to the

**[58:21]** have the new pull request linked to the GitHub issue uh just by having this the

**[58:24]** GitHub issue uh just by having this the

**[58:24]** GitHub issue uh just by having this the body say closes this issue and that's

**[58:27]** body say closes this issue and that's

**[58:27]** body say closes this issue and that's going to create a pull request. And so

**[58:29]** going to create a pull request. And so

**[58:29]** going to create a pull request. And so this whole thing like you can run this

**[58:31]** this whole thing like you can run this

**[58:31]** this whole thing like you can run this part locally too. You don't you don't

**[58:32]** part locally too. You don't you don't

**[58:32]** part locally too. You don't you don't have to run this part in GitHub, but it

**[58:34]** have to run this part in GitHub, but it

**[58:34]** have to run this part in GitHub, but it takes the GitHub token and an issue and

**[58:38]** takes the GitHub token and an issue and

**[58:38]** takes the GitHub token and an issue and the repo name so it knows where to put

**[58:39]** the repo name so it knows where to put

**[58:39]** the repo name so it knows where to put the PR and then it

**[58:43]** the PR and then it

**[58:43]** the PR and then it does that whole flow. But we actually

**[58:45]** does that whole flow. But we actually

**[58:45]** does that whole flow. But we actually want that to run in GitHub and that's

**[58:47]** want that to run in GitHub and that's

**[58:47]** want that to run in GitHub and that's super easy. Um, so we've made that

**[58:49]** super easy. Um, so we've made that

**[58:49]** super easy. Um, so we've made that thing. We just saw the code. Uh, now we

**[58:51]** thing. We just saw the code. Uh, now we

**[58:51]** thing. We just saw the code. Uh, now we create a GitHub actions workflow. Uh,

**[58:53]** create a GitHub actions workflow. Uh,

**[58:54]** create a GitHub actions workflow. Uh, the first two things we need to do is in

**[58:57]** the first two things we need to do is in

**[58:57]** the first two things we need to do is in the repo we need to create two repo

**[58:59]** the repo we need to create two repo

**[58:59]** the repo we need to create two repo secrets. one for a cloud token. Again,


### [59:00 - 01:00:00]

**[59:01]** secrets. one for a cloud token. Again,

**[59:02]** secrets. one for a cloud token. Again, that part's optional. Um, but if you

**[59:04]** that part's optional. Um, but if you

**[59:04]** that part's optional. Um, but if you want to see all those things happen in

**[59:05]** want to see all those things happen in

**[59:05]** want to see all those things happen in Dagger Cloud, you just put that token in

**[59:07]** Dagger Cloud, you just put that token in

**[59:07]** Dagger Cloud, you just put that token in the environment. And then whatever LLM

**[59:09]** the environment. And then whatever LLM

**[59:09]** the environment. And then whatever LLM key you're using, so the same one uh I

**[59:12]** key you're using, so the same one uh I

**[59:12]** key you're using, so the same one uh I use locally is going to be in that repo

**[59:14]** use locally is going to be in that repo

**[59:14]** use locally is going to be in that repo secret. So if I go over here in my repo

**[59:16]** secret. So if I go over here in my repo

**[59:16]** secret. So if I go over here in my repo and I say

**[59:19]** and I say

**[59:19]** and I say and I zoom out a bit so I get all the

**[59:20]** and I zoom out a bit so I get all the

**[59:20]** and I zoom out a bit so I get all the buttons, I say settings.

**[59:24]** buttons, I say settings.

**[59:24]** buttons, I say settings. We wait for the page to load. And then

**[59:27]** We wait for the page to load. And then

**[59:28]** We wait for the page to load. And then down here under

**[59:30]** down here under

**[59:30]** down here under secrets and variables

**[59:32]** secrets and variables

**[59:32]** secrets and variables actions,

**[59:34]** actions,

**[59:34]** actions, I have two repo secrets here that we

**[59:36]** I have two repo secrets here that we

**[59:36]** I have two repo secrets here that we just saw from that screenshot. Make it

**[59:38]** just saw from that screenshot. Make it

**[59:38]** just saw from that screenshot. Make it big again. Sure. Um and then there's one

**[59:43]** big again. Sure. Um and then there's one

**[59:43]** big again. Sure. Um and then there's one more thing which is uh let's see that's

**[59:46]** more thing which is uh let's see that's

**[59:46]** more thing which is uh let's see that's how we get our Dagger cloud token and

**[59:47]** how we get our Dagger cloud token and

**[59:47]** how we get our Dagger cloud token and paste in there. Um there's a little

**[59:50]** paste in there. Um there's a little

**[59:50]** paste in there. Um there's a little check box we have to press over here to

**[59:52]** check box we have to press over here to

**[59:52]** check box we have to press over here to let GitHub actions create PRs. Uh

**[59:55]** let GitHub actions create PRs. Uh

**[59:55]** let GitHub actions create PRs. Uh because that's disabled by default. Uh

**[59:58]** because that's disabled by default. Uh

**[59:58]** because that's disabled by default. Uh so if I go under


### [01:00:00 - 01:01:00]

**[01:00:01]** so if I go under

**[01:00:01]** so if I go under um okay under actions

**[01:00:04]** um okay under actions

**[01:00:04]** um okay under actions general

**[01:00:06]** general

**[01:00:06]** general and then at the very bottom there's this

**[01:00:08]** and then at the very bottom there's this

**[01:00:08]** and then at the very bottom there's this checkbox allow GitHub actions to create

**[01:00:10]** checkbox allow GitHub actions to create

**[01:00:10]** checkbox allow GitHub actions to create and approve pull requests. So I've done

**[01:00:12]** and approve pull requests. So I've done

**[01:00:12]** and approve pull requests. So I've done that. Uh now I just need to create a

**[01:00:16]** that. Uh now I just need to create a

**[01:00:16]** that. Uh now I just need to create a workflow and the workflow is super

**[01:00:18]** workflow and the workflow is super

**[01:00:18]** workflow and the workflow is super short. Um this is a thing you can copy

**[01:00:21]** short. Um this is a thing you can copy

**[01:00:21]** short. Um this is a thing you can copy paste and I'll open it up over here.

**[01:00:24]** paste and I'll open it up over here.

**[01:00:24]** paste and I'll open it up over here. Um under GitHub workflows we have

**[01:00:26]** Um under GitHub workflows we have

**[01:00:26]** Um under GitHub workflows we have develop and so now we have this is

**[01:00:29]** develop and so now we have this is

**[01:00:29]** develop and so now we have this is GitHub actions. If you ever haven't used

**[01:00:30]** GitHub actions. If you ever haven't used

**[01:00:30]** GitHub actions. If you ever haven't used GitHub actions, I'll explain this real

**[01:00:32]** GitHub actions, I'll explain this real

**[01:00:32]** GitHub actions, I'll explain this real quick, but it's basically uh a CI

**[01:00:35]** quick, but it's basically uh a CI

**[01:00:35]** quick, but it's basically uh a CI platform and we have with this

**[01:00:37]** platform and we have with this

**[01:00:37]** platform and we have with this configuration we tell it uh when thing

**[01:00:40]** configuration we tell it uh when thing

**[01:00:40]** configuration we tell it uh when thing when events happen uh go do these

**[01:00:43]** when events happen uh go do these

**[01:00:43]** when events happen uh go do these things. So in this case we say when a

**[01:00:46]** things. So in this case we say when a

**[01:00:46]** things. So in this case we say when a github issue is labeled and the label is

**[01:00:49]** github issue is labeled and the label is

**[01:00:49]** github issue is labeled and the label is called develop

**[01:00:51]** called develop

**[01:00:51]** called develop then run this command and this command

**[01:00:53]** then run this command and this command

**[01:00:53]** then run this command and this command is the dagger called develop issue with

**[01:00:55]** is the dagger called develop issue with

**[01:00:56]** is the dagger called develop issue with those arguments like github token the

**[01:00:58]** those arguments like github token the

**[01:00:58]** those arguments like github token the issue ID and the repo and these things


### [01:01:00 - 01:02:00]

**[01:01:00]** issue ID and the repo and these things

**[01:01:00]** issue ID and the repo and these things are all coming from github actions

**[01:01:02]** are all coming from github actions

**[01:01:02]** are all coming from github actions automatically. So like the environment's

**[01:01:04]** automatically. So like the environment's

**[01:01:04]** automatically. So like the environment's GitHub token is created here where we

**[01:01:07]** GitHub token is created here where we

**[01:01:07]** GitHub token is created here where we say this uh this command needs a GitHub

**[01:01:11]** say this uh this command needs a GitHub

**[01:01:11]** say this uh this command needs a GitHub token with permissions to write

**[01:01:14]** token with permissions to write

**[01:01:14]** token with permissions to write contents. Contents are like commits to

**[01:01:16]** contents. Contents are like commits to

**[01:01:16]** contents. Contents are like commits to your project. Uh read the issues and

**[01:01:18]** your project. Uh read the issues and

**[01:01:18]** your project. Uh read the issues and write pull requests. Uh and so we've put

**[01:01:21]** write pull requests. Uh and so we've put

**[01:01:21]** write pull requests. Uh and so we've put that in the environment. We've g it

**[01:01:24]** that in the environment. We've g it

**[01:01:24]** that in the environment. We've g it given it the API key for our LM and the

**[01:01:27]** given it the API key for our LM and the

**[01:01:27]** given it the API key for our LM and the cloud token. Um and so now just by

**[01:01:29]** cloud token. Um and so now just by

**[01:01:30]** cloud token. Um and so now just by running this dagger call that connects

**[01:01:31]** running this dagger call that connects

**[01:01:31]** running this dagger call that connects the dots where github actions whenever

**[01:01:34]** the dots where github actions whenever

**[01:01:34]** the dots where github actions whenever we create that label is going to run

**[01:01:35]** we create that label is going to run

**[01:01:35]** we create that label is going to run that dagger function and that dagger

**[01:01:37]** that dagger function and that dagger

**[01:01:37]** that dagger function and that dagger function has all the capabilities to run

**[01:01:39]** function has all the capabilities to run

**[01:01:39]** function has all the capabilities to run the agent and open a PR. So that's like

**[01:01:41]** the agent and open a PR. So that's like

**[01:01:41]** the agent and open a PR. So that's like us in the dagger shell when we call when

**[01:01:43]** us in the dagger shell when we call when

**[01:01:43]** us in the dagger shell when we call when we are running like the develop function

**[01:01:46]** we are running like the develop function

**[01:01:46]** we are running like the develop function or some other build function or

**[01:01:48]** or some other build function or

**[01:01:48]** or some other build function or whatever. This is just having github

**[01:01:50]** whatever. This is just having github

**[01:01:50]** whatever. This is just having github actions run the develop issue function

**[01:01:52]** actions run the develop issue function

**[01:01:52]** actions run the develop issue function for us. Yep. Why are you having actions

**[01:01:55]** for us. Yep. Why are you having actions

**[01:01:55]** for us. Yep. Why are you having actions do it? So then issues. Um, so we're

**[01:01:58]** do it? So then issues. Um, so we're

**[01:01:58]** do it? So then issues. Um, so we're having GitHub actions do it because we

**[01:01:59]** having GitHub actions do it because we


### [01:02:00 - 01:03:00]

**[01:02:00]** having GitHub actions do it because we want this flow to be automated inside

**[01:02:02]** want this flow to be automated inside

**[01:02:02]** want this flow to be automated inside GitHub. So I'll show the flow real

**[01:02:03]** GitHub. So I'll show the flow real

**[01:02:03]** GitHub. So I'll show the flow real quick, but it can run anywhere. So you

**[01:02:05]** quick, but it can run anywhere. So you

**[01:02:05]** quick, but it can run anywhere. So you can run it as long as it doesn't matter.

**[01:02:07]** can run it as long as it doesn't matter.

**[01:02:07]** can run it as long as it doesn't matter. Doesn't matter where it runs. Yep. Uh,

**[01:02:08]** Doesn't matter where it runs. Yep. Uh,

**[01:02:08]** Doesn't matter where it runs. Yep. Uh, this just happens to be GitHub a GitHub

**[01:02:10]** this just happens to be GitHub a GitHub

**[01:02:10]** this just happens to be GitHub a GitHub actions because we're already in a

**[01:02:12]** actions because we're already in a

**[01:02:12]** actions because we're already in a GitHub repo. It's free because this is

**[01:02:14]** GitHub repo. It's free because this is

**[01:02:14]** GitHub repo. It's free because this is like uh uh we're not using any crazy

**[01:02:18]** like uh uh we're not using any crazy

**[01:02:18]** like uh uh we're not using any crazy compute to run this thing and most of

**[01:02:19]** compute to run this thing and most of

**[01:02:19]** compute to run this thing and most of the hard stuff's happening on your LLM

**[01:02:21]** the hard stuff's happening on your LLM

**[01:02:21]** the hard stuff's happening on your LLM that you're paying for. and they have

**[01:02:22]** that you're paying for. and they have

**[01:02:22]** that you're paying for. and they have better internet connection at GitHub

**[01:02:24]** better internet connection at GitHub

**[01:02:24]** better internet connection at GitHub than today. So let's say let's create a

**[01:02:28]** than today. So let's say let's create a

**[01:02:28]** than today. So let's say let's create a new issue and we'll say change the

**[01:02:31]** new issue and we'll say change the

**[01:02:31]** new issue and we'll say change the greeting and we want to what did we ask

**[01:02:35]** greeting and we want to what did we ask

**[01:02:35]** greeting and we want to what did we ask for before we asked for like make the

**[01:02:38]** for before we asked for like make the

**[01:02:38]** for before we asked for like make the main page say hello workshop something

**[01:02:41]** main page say hello workshop something

**[01:02:41]** main page say hello workshop something like that hello workshop people yes okay

**[01:02:45]** like that hello workshop people yes okay

**[01:02:45]** like that hello workshop people yes okay so we'll create this GitHub issue

**[01:02:48]** so we'll create this GitHub issue

**[01:02:48]** so we'll create this GitHub issue and remember this this whole thing kicks

**[01:02:50]** and remember this this whole thing kicks

**[01:02:50]** and remember this this whole thing kicks off when I add the label develop and so

**[01:02:53]** off when I add the label develop and so

**[01:02:53]** off when I add the label develop and so I've already run this on this repo and

**[01:02:55]** I've already run this on this repo and

**[01:02:55]** I've already run this on this repo and obviously made a typo as well at one

**[01:02:57]** obviously made a typo as well at one

**[01:02:57]** obviously made a typo as well at one point. Um, but if you don't have it

**[01:02:58]** point. Um, but if you don't have it

**[01:02:58]** point. Um, but if you don't have it there, you can just say foo and you'll


### [01:03:00 - 01:04:00]

**[01:03:01]** there, you can just say foo and you'll

**[01:03:01]** there, you can just say foo and you'll have a button to say create a new

**[01:03:03]** have a button to say create a new

**[01:03:03]** have a button to say create a new labeled uh develop. So we want to call

**[01:03:05]** labeled uh develop. So we want to call

**[01:03:05]** labeled uh develop. So we want to call it develop.

**[01:03:07]** it develop.

**[01:03:07]** it develop. Um, so I click that and now my issue has

**[01:03:11]** Um, so I click that and now my issue has

**[01:03:11]** Um, so I click that and now my issue has been labeled and so now that kicks off

**[01:03:14]** been labeled and so now that kicks off

**[01:03:14]** been labeled and so now that kicks off GitHub actions to call my dagger thing.

**[01:03:16]** GitHub actions to call my dagger thing.

**[01:03:16]** GitHub actions to call my dagger thing. So, let's go over here in the actions

**[01:03:18]** So, let's go over here in the actions

**[01:03:18]** So, let's go over here in the actions tab and we should see something running

**[01:03:21]** tab and we should see something running

**[01:03:21]** tab and we should see something running and it says change the greeting and we

**[01:03:23]** and it says change the greeting and we

**[01:03:23]** and it says change the greeting and we can watch this run over here. We can

**[01:03:26]** can watch this run over here. We can

**[01:03:26]** can watch this run over here. We can also pull it up in cloud because

**[01:03:27]** also pull it up in cloud because

**[01:03:27]** also pull it up in cloud because remember I put that cloud token in there

**[01:03:29]** remember I put that cloud token in there

**[01:03:29]** remember I put that cloud token in there because this stuff is all too hard to

**[01:03:31]** because this stuff is all too hard to

**[01:03:31]** because this stuff is all too hard to see uh flying by my screen in real time.

**[01:03:33]** see uh flying by my screen in real time.

**[01:03:34]** see uh flying by my screen in real time. So, let's go back here and this is

**[01:03:36]** So, let's go back here and this is

**[01:03:36]** So, let's go back here and this is GitHub actions, right? But it could be

**[01:03:38]** GitHub actions, right? But it could be

**[01:03:38]** GitHub actions, right? But it could be any kind of you know orchestration or CI

**[01:03:41]** any kind of you know orchestration or CI

**[01:03:41]** any kind of you know orchestration or CI orchestration could be Jenkins could be

**[01:03:42]** orchestration could be Jenkins could be

**[01:03:42]** orchestration could be Jenkins could be Gitlab CI it could be anything Azure

**[01:03:45]** Gitlab CI it could be anything Azure

**[01:03:45]** Gitlab CI it could be anything Azure DevOps you know whatever whatever you

**[01:03:47]** DevOps you know whatever whatever you

**[01:03:47]** DevOps you know whatever whatever you got. Yeah. Question how much if any like

**[01:03:50]** got. Yeah. Question how much if any like

**[01:03:50]** got. Yeah. Question how much if any like Chrome modification for you guys is it

**[01:03:52]** Chrome modification for you guys is it

**[01:03:52]** Chrome modification for you guys is it literally just puts in that one markdown

**[01:03:55]** literally just puts in that one markdown

**[01:03:55]** literally just puts in that one markdown file or do you add like is it aware that

**[01:03:57]** file or do you add like is it aware that

**[01:03:57]** file or do you add like is it aware that it's in Dagger? It is. Yeah. So we have


### [01:04:00 - 01:05:00]

**[01:04:00]** it's in Dagger? It is. Yeah. So we have

**[01:04:00]** it's in Dagger? It is. Yeah. So we have the question is like how much prompt

**[01:04:01]** the question is like how much prompt

**[01:04:01]** the question is like how much prompt modification does the agent have? Uh,

**[01:04:04]** modification does the agent have? Uh,

**[01:04:04]** modification does the agent have? Uh, Dagger has its own system prompt that it

**[01:04:06]** Dagger has its own system prompt that it

**[01:04:06]** Dagger has its own system prompt that it adds that kind of guides it towards like

**[01:04:08]** adds that kind of guides it towards like

**[01:04:08]** adds that kind of guides it towards like how you use uh tools within Dagger. So,

**[01:04:11]** how you use uh tools within Dagger. So,

**[01:04:11]** how you use uh tools within Dagger. So, it knows like call the the select

**[01:04:13]** it knows like call the the select

**[01:04:13]** it knows like call the the select methods and list functions and those

**[01:04:15]** methods and list functions and those

**[01:04:15]** methods and list functions and those those things we saw doing. You can add

**[01:04:17]** those things we saw doing. You can add

**[01:04:17]** those things we saw doing. You can add more to the system prompt. You can get

**[01:04:19]** more to the system prompt. You can get

**[01:04:19]** more to the system prompt. You can get rid of that system prompt if you want

**[01:04:20]** rid of that system prompt if you want

**[01:04:20]** rid of that system prompt if you want to. But yeah, there is a default one.

**[01:04:23]** to. But yeah, there is a default one.

**[01:04:23]** to. But yeah, there is a default one. Yeah, we have to make further edits

**[01:04:26]** Yeah, we have to make further edits

**[01:04:26]** Yeah, we have to make further edits because the agent is not able to develop

**[01:04:28]** because the agent is not able to develop

**[01:04:28]** because the agent is not able to develop the right code or logic. Yeah. How do we

**[01:04:32]** the right code or logic. Yeah. How do we

**[01:04:32]** the right code or logic. Yeah. How do we correct develop but before the rest of

**[01:04:34]** correct develop but before the rest of

**[01:04:34]** correct develop but before the rest of the stuff. Yes. So if the agent does

**[01:04:36]** the stuff. Yes. So if the agent does

**[01:04:36]** the stuff. Yes. So if the agent does some if it calls develop and it runs and

**[01:04:39]** some if it calls develop and it runs and

**[01:04:39]** some if it calls develop and it runs and it produces something that we say okay

**[01:04:40]** it produces something that we say okay

**[01:04:40]** it produces something that we say okay that's not right. How do we go back and

**[01:04:43]** that's not right. How do we go back and

**[01:04:43]** that's not right. How do we go back and say make these changes? Um can we just

**[01:04:47]** say make these changes? Um can we just

**[01:04:47]** say make these changes? Um can we just edit the completed source? Oh yeah. So

**[01:04:50]** edit the completed source? Oh yeah. So

**[01:04:50]** edit the completed source? Oh yeah. So yeah so you you can edit the completed

**[01:04:53]** yeah so you you can edit the completed

**[01:04:53]** yeah so you you can edit the completed source if you want. If you say if you

**[01:04:54]** source if you want. If you say if you

**[01:04:54]** source if you want. If you say if you see the source and say, "Oh, it needs

**[01:04:56]** see the source and say, "Oh, it needs

**[01:04:56]** see the source and say, "Oh, it needs one more change." Or I can show you

**[01:04:58]** one more change." Or I can show you

**[01:04:58]** one more change." Or I can show you another function where we say, uh, we


### [01:05:00 - 01:06:00]

**[01:05:01]** another function where we say, uh, we

**[01:05:01]** another function where we say, uh, we have an ability to give it more feedback

**[01:05:03]** have an ability to give it more feedback

**[01:05:03]** have an ability to give it more feedback to say, "Okay, you've done this so far.

**[01:05:05]** to say, "Okay, you've done this so far.

**[01:05:05]** to say, "Okay, you've done this so far. Here's some more changes to make because

**[01:05:07]** Here's some more changes to make because

**[01:05:07]** Here's some more changes to make because you didn't get it quite right." Um, and

**[01:05:10]** you didn't get it quite right." Um, and

**[01:05:10]** you didn't get it quite right." Um, and so we'll see that happening. Uh, yeah,

**[01:05:12]** so we'll see that happening. Uh, yeah,

**[01:05:12]** so we'll see that happening. Uh, yeah, go ahead. Possible

**[01:05:16]** go ahead. Possible

**[01:05:16]** go ahead. Possible test. So that

**[01:05:19]** test. So that

**[01:05:19]** test. So that doesn't write

**[01:05:23]** doesn't write

**[01:05:23]** doesn't write uh the test directory

**[01:05:26]** uh the test directory

**[01:05:26]** uh the test directory it I think it should um yeah so I the

**[01:05:30]** it I think it should um yeah so I the

**[01:05:30]** it I think it should um yeah so I the question was giving uh the agent access

**[01:05:32]** question was giving uh the agent access

**[01:05:32]** question was giving uh the agent access to the test directory. I think in test

**[01:05:36]** to the test directory. I think in test

**[01:05:36]** to the test directory. I think in test it runs that and I think in our

**[01:05:37]** it runs that and I think in our

**[01:05:37]** it runs that and I think in our workspace we just give it the we give it

**[01:05:40]** workspace we just give it the we give it

**[01:05:40]** workspace we just give it the we give it like the full source full source of the

**[01:05:43]** like the full source full source of the

**[01:05:43]** like the full source full source of the repo so it could get down in there if it

**[01:05:45]** repo so it could get down in there if it

**[01:05:45]** repo so it could get down in there if it wanted to. Yeah. I think it it's kind of

**[01:05:47]** wanted to. Yeah. I think it it's kind of

**[01:05:47]** wanted to. Yeah. I think it it's kind of a funny thing like making sure the test

**[01:05:49]** a funny thing like making sure the test

**[01:05:49]** a funny thing like making sure the test passed because sometimes if the agent

**[01:05:52]** passed because sometimes if the agent

**[01:05:52]** passed because sometimes if the agent broke the test, it'll go change the test

**[01:05:54]** broke the test, it'll go change the test

**[01:05:54]** broke the test, it'll go change the test and sometimes that's correct, right?

**[01:05:56]** and sometimes that's correct, right?

**[01:05:56]** and sometimes that's correct, right? Sometimes we actually change the

**[01:05:57]** Sometimes we actually change the

**[01:05:57]** Sometimes we actually change the behavior and the tests need to be

**[01:05:58]** behavior and the tests need to be

**[01:05:58]** behavior and the tests need to be updated. But maybe more often that's not


### [01:06:00 - 01:07:00]

**[01:06:01]** updated. But maybe more often that's not

**[01:06:01]** updated. But maybe more often that's not correct. So you might want to maybe have

**[01:06:03]** correct. So you might want to maybe have

**[01:06:03]** correct. So you might want to maybe have that as part of your prompting or part

**[01:06:04]** that as part of your prompting or part

**[01:06:04]** that as part of your prompting or part of your validation to say make sure the

**[01:06:06]** of your validation to say make sure the

**[01:06:06]** of your validation to say make sure the agent didn't change the test or or how

**[01:06:10]** agent didn't change the test or or how

**[01:06:10]** agent didn't change the test or or how it kind of tough to decide like whether

**[01:06:12]** it kind of tough to decide like whether

**[01:06:12]** it kind of tough to decide like whether that's correct or not. Yeah.

**[01:06:24]** So in a oneliner. Yeah. Yeah. So in uh

**[01:06:24]** So in a oneliner. Yeah. Yeah. So in uh our workflow we installed Dagger but

**[01:06:28]** our workflow we installed Dagger but

**[01:06:28]** our workflow we installed Dagger but it's it's really just there's a a Dagger

**[01:06:30]** it's it's really just there's a a Dagger

**[01:06:30]** it's it's really just there's a a Dagger for GitHub action and so we just said

**[01:06:33]** for GitHub action and so we just said

**[01:06:33]** for GitHub action and so we just said what threeliner in this threeliner.

**[01:06:34]** what threeliner in this threeliner.

**[01:06:34]** what threeliner in this threeliner. Yeah. So we said this version of Dagger

**[01:06:36]** Yeah. So we said this version of Dagger

**[01:06:36]** Yeah. So we said this version of Dagger but this installs Dagger in your in your

**[01:06:39]** but this installs Dagger in your in your

**[01:06:39]** but this installs Dagger in your in your GitHub actions runtime basically. Uh so

**[01:06:41]** GitHub actions runtime basically. Uh so

**[01:06:41]** GitHub actions runtime basically. Uh so we used checkout to check out a repo and

**[01:06:44]** we used checkout to check out a repo and

**[01:06:44]** we used checkout to check out a repo and then this to install dagger dependencies

**[01:06:47]** then this to install dagger dependencies

**[01:06:47]** then this to install dagger dependencies like you

**[01:06:54]** wouldn't like

**[01:06:54]** wouldn't like Oh yeah.

**[01:06:56]** Oh yeah.

**[01:06:56]** Oh yeah. Yeah. Exactly. So this is um in our

**[01:06:59]** Yeah. Exactly. So this is um in our

**[01:06:59]** Yeah. Exactly. So this is um in our Dagger JSON we have


### [01:07:00 - 01:08:00]

**[01:07:03]** Dagger JSON we have

**[01:07:03]** Dagger JSON we have all all of our dependencies listed and

**[01:07:05]** all all of our dependencies listed and

**[01:07:05]** all all of our dependencies listed and so you don't have to say like Dagger

**[01:07:06]** so you don't have to say like Dagger

**[01:07:06]** so you don't have to say like Dagger install or anything. When we say dagger

**[01:07:08]** install or anything. When we say dagger

**[01:07:08]** install or anything. When we say dagger install, it adds it to this and then we

**[01:07:11]** install, it adds it to this and then we

**[01:07:11]** install, it adds it to this and then we just run it. Um, we don't have to do

**[01:07:13]** just run it. Um, we don't have to do

**[01:07:13]** just run it. Um, we don't have to do anything like npm install like that. It

**[01:07:16]** anything like npm install like that. It

**[01:07:16]** anything like npm install like that. It just it it knows to make sure your

**[01:07:18]** just it it knows to make sure your

**[01:07:18]** just it it knows to make sure your client's generated. But that's that is

**[01:07:20]** client's generated. But that's that is

**[01:07:20]** client's generated. But that's that is the nice thing about having those

**[01:07:22]** the nice thing about having those

**[01:07:22]** the nice thing about having those dependencies,

**[01:07:24]** dependencies,

**[01:07:24]** dependencies, you know, u in a in a file saved in git,

**[01:07:27]** you know, u in a in a file saved in git,

**[01:07:27]** you know, u in a in a file saved in git, you know, alongside the project. So

**[01:07:30]** you know, alongside the project. So

**[01:07:30]** you know, alongside the project. So because like what we've done essentially

**[01:07:32]** because like what we've done essentially

**[01:07:32]** because like what we've done essentially like if when we first got this project

**[01:07:34]** like if when we first got this project

**[01:07:34]** like if when we first got this project this view app project it didn't have any

**[01:07:36]** this view app project it didn't have any

**[01:07:36]** this view app project it didn't have any dagger didn't have anything right it was

**[01:07:38]** dagger didn't have anything right it was

**[01:07:38]** dagger didn't have anything right it was just like an app that you could run and

**[01:07:40]** just like an app that you could run and

**[01:07:40]** just like an app that you could run and then we said oh well it's dagger in it

**[01:07:43]** then we said oh well it's dagger in it

**[01:07:43]** then we said oh well it's dagger in it in this thing and then we got that

**[01:07:44]** in this thing and then we got that

**[01:07:44]** in this thing and then we got that little dagger where we started

**[01:07:46]** little dagger where we started

**[01:07:46]** little dagger where we started developing our build and test functions

**[01:07:48]** developing our build and test functions

**[01:07:48]** developing our build and test functions right kind of like our tools for

**[01:07:50]** right kind of like our tools for

**[01:07:50]** right kind of like our tools for development or for CI just alongside and

**[01:07:53]** development or for CI just alongside and

**[01:07:53]** development or for CI just alongside and then in there is where we've been

**[01:07:55]** then in there is where we've been

**[01:07:55]** then in there is where we've been installing more modules like the the

**[01:07:57]** installing more modules like the the

**[01:07:57]** installing more modules like the the workspace the github the GitHub issues


### [01:08:00 - 01:09:00]

**[01:08:00]** workspace the github the GitHub issues

**[01:08:00]** workspace the github the GitHub issues module like anything else you would

**[01:08:02]** module like anything else you would

**[01:08:02]** module like anything else you would need. So now and that's all in git. So

**[01:08:05]** need. So now and that's all in git. So

**[01:08:05]** need. So now and that's all in git. So the thing's now like this fully loaded

**[01:08:06]** the thing's now like this fully loaded

**[01:08:06]** the thing's now like this fully loaded like daggerized project. So it's kind of

**[01:08:09]** like daggerized project. So it's kind of

**[01:08:09]** like daggerized project. So it's kind of carrying around its own tools on its

**[01:08:11]** carrying around its own tools on its

**[01:08:12]** carrying around its own tools on its back for working you know just for a

**[01:08:15]** back for working you know just for a

**[01:08:15]** back for working you know just for a developer to use or platform engineer to

**[01:08:16]** developer to use or platform engineer to

**[01:08:16]** developer to use or platform engineer to use or for an agent to use.

**[01:08:20]** use or for an agent to use.

**[01:08:20]** use or for an agent to use. Yeah, we're just like waiting for things

**[01:08:21]** Yeah, we're just like waiting for things

**[01:08:21]** Yeah, we're just like waiting for things to load here. Um yeah, go ahead. Have

**[01:08:24]** to load here. Um yeah, go ahead. Have

**[01:08:24]** to load here. Um yeah, go ahead. Have you gotten anything uh like dagger in

**[01:08:27]** you gotten anything uh like dagger in

**[01:08:28]** you gotten anything uh like dagger in dagger where you have it spinning up

**[01:08:29]** dagger where you have it spinning up

**[01:08:29]** dagger where you have it spinning up like agent fleets?

**[01:08:32]** like agent fleets?

**[01:08:32]** like agent fleets? Yeah. Yeah. Yeah. So that's um I mean

**[01:08:36]** Yeah. Yeah. Yeah. So that's um I mean

**[01:08:36]** Yeah. Yeah. Yeah. So that's um I mean myself as someone that builds a lot of

**[01:08:37]** myself as someone that builds a lot of

**[01:08:37]** myself as someone that builds a lot of Dagger code I have agents that need to

**[01:08:39]** Dagger code I have agents that need to

**[01:08:39]** Dagger code I have agents that need to write Dagger code and to to um reliably

**[01:08:43]** write Dagger code and to to um reliably

**[01:08:43]** write Dagger code and to to um reliably uh validate those things they need

**[01:08:45]** uh validate those things they need

**[01:08:45]** uh validate those things they need basically Dagger inside of Dagger. So,

**[01:08:46]** basically Dagger inside of Dagger. So,

**[01:08:46]** basically Dagger inside of Dagger. So, that's exactly like a thing that you can

**[01:08:49]** that's exactly like a thing that you can

**[01:08:49]** that's exactly like a thing that you can do. And I can even uh pull up if we go

**[01:08:52]** do. And I can even uh pull up if we go

**[01:08:52]** do. And I can even uh pull up if we go to And we're a bit short on time, but

**[01:08:54]** to And we're a bit short on time, but

**[01:08:54]** to And we're a bit short on time, but we're basically done with that guide.

**[01:08:56]** we're basically done with that guide.

**[01:08:56]** we're basically done with that guide. Just waiting for it to run. Yeah. Um,

**[01:08:58]** Just waiting for it to run. Yeah. Um,

**[01:08:58]** Just waiting for it to run. Yeah. Um, but we have


### [01:09:00 - 01:10:00]

**[01:09:00]** but we have

**[01:09:00]** but we have uh an examples thing here on the docs.

**[01:09:03]** uh an examples thing here on the docs.

**[01:09:04]** uh an examples thing here on the docs. And there's tons of examples here, but

**[01:09:06]** And there's tons of examples here, but

**[01:09:06]** And there's tons of examples here, but one of the really cool ones that I like

**[01:09:07]** one of the really cool ones that I like

**[01:09:07]** one of the really cool ones that I like the most because I wrote it is I thought

**[01:09:11]** the most because I wrote it is I thought

**[01:09:11]** the most because I wrote it is I thought you were going to show mine, but that's

**[01:09:12]** you were going to show mine, but that's

**[01:09:12]** you were going to show mine, but that's fine. No, it's fine. The

**[01:09:19]** Oh, it's not. Okay. Oh, we're gonna add

**[01:09:19]** Oh, it's not. Okay. Oh, we're gonna add it to the list of examples. Add to the

**[01:09:20]** it to the list of examples. Add to the

**[01:09:20]** it to the list of examples. Add to the list be even cooler list soon. So, we

**[01:09:22]** list be even cooler list soon. So, we

**[01:09:22]** list be even cooler list soon. So, we have your question next. Yeah, there

**[01:09:25]** have your question next. Yeah, there

**[01:09:25]** have your question next. Yeah, there there's this repo under my GitHub

**[01:09:26]** there's this repo under my GitHub

**[01:09:26]** there's this repo under my GitHub kpen/dagger programmer. And this thing

**[01:09:29]** kpen/dagger programmer. And this thing

**[01:09:29]** kpen/dagger programmer. And this thing is something I use to uh like in the

**[01:09:32]** is something I use to uh like in the

**[01:09:32]** is something I use to uh like in the docs we saw those tabs of all the

**[01:09:34]** docs we saw those tabs of all the

**[01:09:34]** docs we saw those tabs of all the different languages. And so, every

**[01:09:35]** different languages. And so, every

**[01:09:35]** different languages. And so, every whenever I write a new guide, I have to

**[01:09:37]** whenever I write a new guide, I have to

**[01:09:37]** whenever I write a new guide, I have to have it in five languages. And so, this

**[01:09:39]** have it in five languages. And so, this

**[01:09:39]** have it in five languages. And so, this agent can take it in one language and

**[01:09:42]** agent can take it in one language and

**[01:09:42]** agent can take it in one language and produce all the languages. Uh, and

**[01:09:44]** produce all the languages. Uh, and

**[01:09:44]** produce all the languages. Uh, and that's just an agent that knows how to

**[01:09:45]** that's just an agent that knows how to

**[01:09:45]** that's just an agent that knows how to write Dagger. And so to do that, it has

**[01:09:48]** write Dagger. And so to do that, it has

**[01:09:48]** write Dagger. And so to do that, it has a lot of cool things in addition to be

**[01:09:50]** a lot of cool things in addition to be

**[01:09:50]** a lot of cool things in addition to be able to like run Dagger and Dagger. So

**[01:09:53]** able to like run Dagger and Dagger. So

**[01:09:53]** able to like run Dagger and Dagger. So if we look at the the code for that,

**[01:09:55]** if we look at the the code for that,

**[01:09:55]** if we look at the the code for that, it's just like this one's in Typescript.

**[01:09:58]** it's just like this one's in Typescript.

**[01:09:58]** it's just like this one's in Typescript. Yeah, this is the TypeScript one. Um,


### [01:10:00 - 01:11:00]

**[01:10:00]** Yeah, this is the TypeScript one. Um,

**[01:10:00]** Yeah, this is the TypeScript one. Um, and when it runs tests, it runs the

**[01:10:03]** and when it runs tests, it runs the

**[01:10:03]** and when it runs tests, it runs the Dagger thing and there's this flag

**[01:10:06]** Dagger thing and there's this flag

**[01:10:06]** Dagger thing and there's this flag privilege nesting so that the inner

**[01:10:08]** privilege nesting so that the inner

**[01:10:08]** privilege nesting so that the inner container can talk to the engine. Um and

**[01:10:11]** container can talk to the engine. Um and

**[01:10:11]** container can talk to the engine. Um and this this is writing Dagger code

**[01:10:13]** this this is writing Dagger code

**[01:10:13]** this this is writing Dagger code basically. Yeah. Question here curious

**[01:10:15]** basically. Yeah. Question here curious

**[01:10:16]** basically. Yeah. Question here curious how does this relate to um MCP and would

**[01:10:19]** how does this relate to um MCP and would

**[01:10:19]** how does this relate to um MCP and would you use Dagger to implement MCP servers

**[01:10:21]** you use Dagger to implement MCP servers

**[01:10:21]** you use Dagger to implement MCP servers and is there some overlap because you

**[01:10:23]** and is there some overlap because you

**[01:10:23]** and is there some overlap because you have all these modules which maybe you

**[01:10:24]** have all these modules which maybe you

**[01:10:24]** have all these modules which maybe you could imagine having multiple MCPS um in

**[01:10:27]** could imagine having multiple MCPS um in

**[01:10:27]** could imagine having multiple MCPS um in as a different mechanism. Yeah,

**[01:10:29]** as a different mechanism. Yeah,

**[01:10:29]** as a different mechanism. Yeah, absolutely. So, one way to think about

**[01:10:31]** absolutely. So, one way to think about

**[01:10:31]** absolutely. So, one way to think about it is um we were we were kind of doing

**[01:10:34]** it is um we were we were kind of doing

**[01:10:34]** it is um we were we were kind of doing this thing with Dagger modules before

**[01:10:36]** this thing with Dagger modules before

**[01:10:36]** this thing with Dagger modules before MCP came on the scene and then obviously

**[01:10:39]** MCP came on the scene and then obviously

**[01:10:39]** MCP came on the scene and then obviously we're like oh this is super aligned with

**[01:10:42]** we're like oh this is super aligned with

**[01:10:42]** we're like oh this is super aligned with the way we think things should be in a

**[01:10:44]** the way we think things should be in a

**[01:10:44]** the way we think things should be in a lot of ways. Um, and so you can today

**[01:10:47]** lot of ways. Um, and so you can today

**[01:10:47]** lot of ways. Um, and so you can today even take a Dagger module and you can

**[01:10:49]** even take a Dagger module and you can

**[01:10:49]** even take a Dagger module and you can say Dagger-m

**[01:10:51]** say Dagger-m

**[01:10:51]** say Dagger-m the name of the module MCP and so you

**[01:10:54]** the name of the module MCP and so you

**[01:10:54]** the name of the module MCP and so you can expose a Dagger module as an MP MCP

**[01:10:57]** can expose a Dagger module as an MP MCP

**[01:10:57]** can expose a Dagger module as an MP MCP server for example and yeah and we've

**[01:10:59]** server for example and yeah and we've

**[01:10:59]** server for example and yeah and we've got some more things that we'll be


### [01:11:00 - 01:12:00]

**[01:11:01]** got some more things that we'll be

**[01:11:01]** got some more things that we'll be probably sharing soon about that kind of

**[01:11:03]** probably sharing soon about that kind of

**[01:11:03]** probably sharing soon about that kind of stuff but yes uh we think it's uh the

**[01:11:06]** stuff but yes uh we think it's uh the

**[01:11:06]** stuff but yes uh we think it's uh the vision is compatible in that way and uh

**[01:11:09]** vision is compatible in that way and uh

**[01:11:09]** vision is compatible in that way and uh yeah you can use you can use the MCP

**[01:11:11]** yeah you can use you can use the MCP

**[01:11:11]** yeah you can use you can use the MCP ecosystem as well. Yeah. So, there's a

**[01:11:13]** ecosystem as well. Yeah. So, there's a

**[01:11:13]** ecosystem as well. Yeah. So, there's a few different layers to it, right?

**[01:11:14]** few different layers to it, right?

**[01:11:14]** few different layers to it, right? There's there's um within our agent that

**[01:11:16]** There's there's um within our agent that

**[01:11:16]** There's there's um within our agent that we just built, we installed modules and

**[01:11:18]** we just built, we installed modules and

**[01:11:18]** we just built, we installed modules and that uses uh basically our internal

**[01:11:21]** that uses uh basically our internal

**[01:11:21]** that uses uh basically our internal implementation of MCP to talk between

**[01:11:23]** implementation of MCP to talk between

**[01:11:23]** implementation of MCP to talk between modules within Dagger. But you can also

**[01:11:25]** modules within Dagger. But you can also

**[01:11:25]** modules within Dagger. But you can also take a Dagger module, expose it as an

**[01:11:27]** take a Dagger module, expose it as an

**[01:11:27]** take a Dagger module, expose it as an MCP server and then um in I don't know

**[01:11:31]** MCP server and then um in I don't know

**[01:11:32]** MCP server and then um in I don't know the near future next week or something

**[01:11:33]** the near future next week or something

**[01:11:33]** the near future next week or something you could connect to external MCP

**[01:11:36]** you could connect to external MCP

**[01:11:36]** you could connect to external MCP servers to bring them into Dagger as

**[01:11:37]** servers to bring them into Dagger as

**[01:11:37]** servers to bring them into Dagger as well. Yeah, I mean it's I wanted to be

**[01:11:39]** well. Yeah, I mean it's I wanted to be

**[01:11:39]** well. Yeah, I mean it's I wanted to be speak clear like the internal the

**[01:11:41]** speak clear like the internal the

**[01:11:41]** speak clear like the internal the internal implementation it's it's before

**[01:11:44]** internal implementation it's it's before

**[01:11:44]** internal implementation it's it's before MCP so it's not MCP per se but it it

**[01:11:47]** MCP so it's not MCP per se but it it

**[01:11:47]** MCP so it's not MCP per se but it it very much logically you can think of it

**[01:11:49]** very much logically you can think of it

**[01:11:49]** very much logically you can think of it in a similar way. Yeah. And because you

**[01:11:52]** in a similar way. Yeah. And because you

**[01:11:52]** in a similar way. Yeah. And because you can expose everything as MCP servers it

**[01:11:55]** can expose everything as MCP servers it

**[01:11:55]** can expose everything as MCP servers it ends up being practically you know very

**[01:11:57]** ends up being practically you know very

**[01:11:57]** ends up being practically you know very very much the same for users. Check it


### [01:12:00 - 01:13:00]

**[01:12:00]** very much the same for users. Check it

**[01:12:00]** very much the same for users. Check it out. We got our PR what finally. Oh we

**[01:12:02]** out. We got our PR what finally. Oh we

**[01:12:02]** out. We got our PR what finally. Oh we got a PR. So we got our PR open. says

**[01:12:05]** got a PR. So we got our PR open. says

**[01:12:05]** got a PR. So we got our PR open. says make the main page say that closes that

**[01:12:07]** make the main page say that closes that

**[01:12:07]** make the main page say that closes that issue we created. We have that commit

**[01:12:09]** issue we created. We have that commit

**[01:12:09]** issue we created. We have that commit pushed up and we see the user is this

**[01:12:11]** pushed up and we see the user is this

**[01:12:11]** pushed up and we see the user is this GitHub action spot and we have on the

**[01:12:15]** GitHub action spot and we have on the

**[01:12:15]** GitHub action spot and we have on the welcome.view

**[01:12:17]** welcome.view

**[01:12:17]** welcome.view it changed from documentation to so

**[01:12:20]** it changed from documentation to so

**[01:12:20]** it changed from documentation to so maybe that's right. Oh, it deleted this

**[01:12:21]** maybe that's right. Oh, it deleted this

**[01:12:21]** maybe that's right. Oh, it deleted this other thing too because it decided

**[01:12:23]** other thing too because it decided

**[01:12:23]** other thing too because it decided that's not needed. Cool. So we have a

**[01:12:25]** that's not needed. Cool. So we have a

**[01:12:25]** that's not needed. Cool. So we have a really cool agent. Yeah, it needs lots

**[01:12:28]** really cool agent. Yeah, it needs lots

**[01:12:28]** really cool agent. Yeah, it needs lots back there.

**[01:12:29]** back there.

**[01:12:29]** back there. agents just like um but yeah the main

**[01:12:32]** agents just like um but yeah the main

**[01:12:32]** agents just like um but yeah the main thing is we were able to get it to run

**[01:12:33]** thing is we were able to get it to run

**[01:12:34]** thing is we were able to get it to run in GitHub so I was able to request that

**[01:12:36]** in GitHub so I was able to request that

**[01:12:36]** in GitHub so I was able to request that feature and it ran handsree and now

**[01:12:41]** feature and it ran handsree and now

**[01:12:41]** feature and it ran handsree and now yeah exactly so right now we we only

**[01:12:43]** yeah exactly so right now we we only

**[01:12:43]** yeah exactly so right now we we only built in the one thing where it says we

**[01:12:44]** built in the one thing where it says we

**[01:12:44]** built in the one thing where it says we create an issue that's a feature request

**[01:12:47]** create an issue that's a feature request

**[01:12:47]** create an issue that's a feature request um but if we look at I think on this

**[01:12:49]** um but if we look at I think on this

**[01:12:49]** um but if we look at I think on this examples list um we have

**[01:12:53]** examples list um we have

**[01:12:53]** examples list um we have uh this one this greetings API which is

**[01:12:55]** uh this one this greetings API which is

**[01:12:55]** uh this one this greetings API which is my main like demo project and it has a

**[01:12:58]** my main like demo project and it has a

**[01:12:58]** my main like demo project and it has a ton stuff in there's like five different


### [01:13:00 - 01:14:00]

**[01:13:00]** ton stuff in there's like five different

**[01:13:00]** ton stuff in there's like five different agents in here and one of them is I want

**[01:13:02]** agents in here and one of them is I want

**[01:13:02]** agents in here and one of them is I want to give feedback on a PR and so we could

**[01:13:05]** to give feedback on a PR and so we could

**[01:13:05]** to give feedback on a PR and so we could probably open one of these

**[01:13:08]** probably open one of these

**[01:13:08]** probably open one of these uh and I say I give it I give it some

**[01:13:12]** uh and I say I give it I give it some

**[01:13:12]** uh and I say I give it I give it some feedback I say slash agent uh add this

**[01:13:15]** feedback I say slash agent uh add this

**[01:13:15]** feedback I say slash agent uh add this other fe so this one the original one is

**[01:13:17]** other fe so this one the original one is

**[01:13:17]** other fe so this one the original one is like make a new endpoint for my API and

**[01:13:20]** like make a new endpoint for my API and

**[01:13:20]** like make a new endpoint for my API and then it did that and then I say okay

**[01:13:23]** then it did that and then I say okay

**[01:13:23]** then it did that and then I say okay here's some feedback the endpoint should

**[01:13:24]** here's some feedback the endpoint should

**[01:13:24]** here's some feedback the endpoint should be authenticated and then it picks up

**[01:13:26]** be authenticated and then it picks up

**[01:13:26]** be authenticated and then it picks up again pushes some new changes and And

**[01:13:28]** again pushes some new changes and And

**[01:13:28]** again pushes some new changes and And then I have another agent where I say

**[01:13:29]** then I have another agent where I say

**[01:13:29]** then I have another agent where I say slashreview and that will create a

**[01:13:32]** slashreview and that will create a

**[01:13:32]** slashreview and that will create a review for my PR with any other changes

**[01:13:33]** review for my PR with any other changes

**[01:13:34]** review for my PR with any other changes that I need. And then I can say okay

**[01:13:35]** that I need. And then I can say okay

**[01:13:35]** that I need. And then I can say okay make those changes and then also please

**[01:13:38]** make those changes and then also please

**[01:13:38]** make those changes and then also please don't delete all the tests. Very

**[01:13:40]** don't delete all the tests. Very

**[01:13:40]** don't delete all the tests. Very important to add and that could be like

**[01:13:42]** important to add and that could be like

**[01:13:42]** important to add and that could be like you don't have to be inserting yourself

**[01:13:44]** you don't have to be inserting yourself

**[01:13:44]** you don't have to be inserting yourself at every one of those points, right? But

**[01:13:46]** at every one of those points, right? But

**[01:13:46]** at every one of those points, right? But in this case it it's great for when

**[01:13:48]** in this case it it's great for when

**[01:13:48]** in this case it it's great for when we're Yeah. If you want an example of

**[01:13:50]** we're Yeah. If you want an example of

**[01:13:50]** we're Yeah. If you want an example of how you could take what that workshop

**[01:13:51]** how you could take what that workshop

**[01:13:51]** how you could take what that workshop just built to the next level where you

**[01:13:53]** just built to the next level where you

**[01:13:53]** just built to the next level where you have all this feedback and more advanced

**[01:13:55]** have all this feedback and more advanced

**[01:13:55]** have all this feedback and more advanced things, this is a great repo to look at

**[01:13:57]** things, this is a great repo to look at

**[01:13:57]** things, this is a great repo to look at this greetings API because it has all of


### [01:14:00 - 01:15:00]

**[01:14:00]** this greetings API because it has all of

**[01:14:00]** this greetings API because it has all of these different agents doing tons of

**[01:14:01]** these different agents doing tons of

**[01:14:01]** these different agents doing tons of things. It even has one where if we look

**[01:14:03]** things. It even has one where if we look

**[01:14:03]** things. It even has one where if we look at uh if I as a human push up a broken

**[01:14:07]** at uh if I as a human push up a broken

**[01:14:07]** at uh if I as a human push up a broken thing because we still have humans

**[01:14:09]** thing because we still have humans

**[01:14:09]** thing because we still have humans developing stuff sometimes, right? Uh,

**[01:14:11]** developing stuff sometimes, right? Uh,

**[01:14:11]** developing stuff sometimes, right? Uh, so I pushed a broken thing and the test

**[01:14:14]** so I pushed a broken thing and the test

**[01:14:14]** so I pushed a broken thing and the test failed, which is super annoying because

**[01:14:17]** failed, which is super annoying because

**[01:14:17]** failed, which is super annoying because I, you know, I skipped running tests

**[01:14:19]** I, you know, I skipped running tests

**[01:14:19]** I, you know, I skipped running tests because I didn't have a good prompt that

**[01:14:20]** because I didn't have a good prompt that

**[01:14:20]** because I didn't have a good prompt that told me to run test three times. Uh,

**[01:14:22]** told me to run test three times. Uh,

**[01:14:22]** told me to run test three times. Uh, this agent can actually look at the test

**[01:14:23]** this agent can actually look at the test

**[01:14:24]** this agent can actually look at the test failure automatically and propose a a

**[01:14:27]** failure automatically and propose a a

**[01:14:27]** failure automatically and propose a a fix for that that I can just click on it

**[01:14:29]** fix for that that I can just click on it

**[01:14:29]** fix for that that I can just click on it and fix that uh, test change. Right? So,

**[01:14:32]** and fix that uh, test change. Right? So,

**[01:14:32]** and fix that uh, test change. Right? So, this is all stuff in this demo repo uh,

**[01:14:35]** this is all stuff in this demo repo uh,

**[01:14:35]** this is all stuff in this demo repo uh, where you can see like how to build all

**[01:14:36]** where you can see like how to build all

**[01:14:36]** where you can see like how to build all these things yourself. A question over

**[01:14:38]** these things yourself. A question over

**[01:14:38]** these things yourself. A question over here. There's a lot I really love here.

**[01:14:41]** here. There's a lot I really love here.

**[01:14:41]** here. There's a lot I really love here. Um, I just had a question almost getting

**[01:14:43]** Um, I just had a question almost getting

**[01:14:43]** Um, I just had a question almost getting at the motivation for some of this

**[01:14:44]** at the motivation for some of this

**[01:14:44]** at the motivation for some of this stuff. Yes. It feels like there's a

**[01:14:46]** stuff. Yes. It feels like there's a

**[01:14:46]** stuff. Yes. It feels like there's a world where Dagger could have really

**[01:14:47]** world where Dagger could have really

**[01:14:47]** world where Dagger could have really prioritized just like the containers,

**[01:14:49]** prioritized just like the containers,

**[01:14:49]** prioritized just like the containers, the workflows and let you just bring

**[01:14:50]** the workflows and let you just bring

**[01:14:50]** the workflows and let you just bring your own AI agent. Like what's the

**[01:14:52]** your own AI agent. Like what's the

**[01:14:52]** your own AI agent. Like what's the motivation behind making it its own

**[01:14:54]** motivation behind making it its own

**[01:14:54]** motivation behind making it its own primitive and going down that path? I

**[01:14:56]** primitive and going down that path? I

**[01:14:56]** primitive and going down that path? I think there there's a lot of levels to

**[01:14:57]** think there there's a lot of levels to

**[01:14:57]** think there there's a lot of levels to it, right? Like if you're already really

**[01:14:59]** it, right? Like if you're already really

**[01:14:59]** it, right? Like if you're already really baked into like Pantic or OpenAI agents


### [01:15:00 - 01:16:00]

**[01:15:02]** baked into like Pantic or OpenAI agents

**[01:15:02]** baked into like Pantic or OpenAI agents SDK, you can still use those container

**[01:15:04]** SDK, you can still use those container

**[01:15:04]** SDK, you can still use those container workflows in that. And I'll show it.

**[01:15:06]** workflows in that. And I'll show it.

**[01:15:06]** workflows in that. And I'll show it. Maybe I shouldn't, but um but I have

**[01:15:09]** Maybe I shouldn't, but um but I have

**[01:15:09]** Maybe I shouldn't, but um but I have crazy. Uh if if you've done the OpenAI

**[01:15:12]** crazy. Uh if if you've done the OpenAI

**[01:15:12]** crazy. Uh if if you've done the OpenAI agents quickart um if it loads here

**[01:15:17]** agents quickart um if it loads here

**[01:15:17]** agents quickart um if it loads here uh or sorry, this is the the agent quick

**[01:15:19]** uh or sorry, this is the the agent quick

**[01:15:19]** uh or sorry, this is the the agent quick start we have but with the agent SDK

**[01:15:21]** start we have but with the agent SDK

**[01:15:21]** start we have but with the agent SDK where I've used the OpenAI agent SDK

**[01:15:23]** where I've used the OpenAI agent SDK

**[01:15:23]** where I've used the OpenAI agent SDK that says like um here's my completions

**[01:15:26]** that says like um here's my completions

**[01:15:26]** that says like um here's my completions model. This is actually using Olama. Uh

**[01:15:29]** model. This is actually using Olama. Uh

**[01:15:29]** model. This is actually using Olama. Uh this is what their SDK looks like. Uh

**[01:15:31]** this is what their SDK looks like. Uh

**[01:15:31]** this is what their SDK looks like. Uh but in that SDK I'm actually still using

**[01:15:34]** but in that SDK I'm actually still using

**[01:15:34]** but in that SDK I'm actually still using Dagger. So I actually recreated that

**[01:15:36]** Dagger. So I actually recreated that

**[01:15:36]** Dagger. So I actually recreated that same workspace where we have read file,

**[01:15:38]** same workspace where we have read file,

**[01:15:38]** same workspace where we have read file, write file, and build u but I've created

**[01:15:41]** write file, and build u but I've created

**[01:15:41]** write file, and build u but I've created that with Dagger inside of the open

**[01:15:44]** that with Dagger inside of the open

**[01:15:44]** that with Dagger inside of the open agents SDK. So I'm I'm using their agent

**[01:15:47]** agents SDK. So I'm I'm using their agent

**[01:15:47]** agents SDK. So I'm I'm using their agent but using Dagger code for the containers

**[01:15:51]** but using Dagger code for the containers

**[01:15:51]** but using Dagger code for the containers like what like why use I guess yeah the

**[01:15:54]** like what like why use I guess yeah the

**[01:15:54]** like what like why use I guess yeah the main thing is like this I had to write

**[01:15:57]** main thing is like this I had to write

**[01:15:57]** main thing is like this I had to write all of these tools and how to use them.

**[01:15:59]** all of these tools and how to use them.

**[01:15:59]** all of these tools and how to use them. If it's all within Dagger, you get that


### [01:16:00 - 01:17:00]

**[01:16:01]** If it's all within Dagger, you get that

**[01:16:01]** If it's all within Dagger, you get that cool thing where we have that whole

**[01:16:02]** cool thing where we have that whole

**[01:16:02]** cool thing where we have that whole Dagger Versa modules. I can just plug

**[01:16:03]** Dagger Versa modules. I can just plug

**[01:16:03]** Dagger Versa modules. I can just plug one in and that's just given to the

**[01:16:05]** one in and that's just given to the

**[01:16:05]** one in and that's just given to the agent, right? Yeah. Your your whole your

**[01:16:07]** agent, right? Yeah. Your your whole your

**[01:16:07]** agent, right? Yeah. Your your whole your whole method signature is instantly

**[01:16:09]** whole method signature is instantly

**[01:16:09]** whole method signature is instantly translated into the right form to work

**[01:16:11]** translated into the right form to work

**[01:16:11]** translated into the right form to work with tools, right? You get tools for

**[01:16:13]** with tools, right? You get tools for

**[01:16:13]** with tools, right? You get tools for free as well as functions and Yeah. And

**[01:16:16]** free as well as functions and Yeah. And

**[01:16:16]** free as well as functions and Yeah. And we do have some people in our community

**[01:16:18]** we do have some people in our community

**[01:16:18]** we do have some people in our community that are using Dagger. they're like with

**[01:16:20]** that are using Dagger. they're like with

**[01:16:20]** that are using Dagger. they're like with paidantic and other things where they're

**[01:16:21]** paidantic and other things where they're

**[01:16:21]** paidantic and other things where they're just like they want the sandbox

**[01:16:23]** just like they want the sandbox

**[01:16:23]** just like they want the sandbox capability because they're like oh I

**[01:16:25]** capability because they're like oh I

**[01:16:25]** capability because they're like oh I don't want to you know I don't want to

**[01:16:27]** don't want to you know I don't want to

**[01:16:27]** don't want to you know I don't want to use another cloud sandbox vendor or

**[01:16:29]** use another cloud sandbox vendor or

**[01:16:29]** use another cloud sandbox vendor or whatever I want to have it locally but I

**[01:16:31]** whatever I want to have it locally but I

**[01:16:31]** whatever I want to have it locally but I don't want it on my computer in my file

**[01:16:32]** don't want it on my computer in my file

**[01:16:32]** don't want it on my computer in my file system either I want containers I want

**[01:16:35]** system either I want containers I want

**[01:16:35]** system either I want containers I want it easy so they're so yeah but I think

**[01:16:38]** it easy so they're so yeah but I think

**[01:16:38]** it easy so they're so yeah but I think yeah the sweet spot is kind of doing it

**[01:16:39]** yeah the sweet spot is kind of doing it

**[01:16:39]** yeah the sweet spot is kind of doing it all because it just harmonizes really

**[01:16:41]** all because it just harmonizes really

**[01:16:41]** all because it just harmonizes really well

**[01:16:42]** well

**[01:16:42]** well question there thanks for the great demo

**[01:16:45]** question there thanks for the great demo

**[01:16:45]** question there thanks for the great demo uh so I had a question let's say if I

**[01:16:47]** uh so I had a question let's say if I

**[01:16:47]** uh so I had a question let's say if I want to build a uh agent for programming

**[01:16:50]** want to build a uh agent for programming

**[01:16:50]** want to build a uh agent for programming HTML games. Yes. Which run in browser.

**[01:16:52]** HTML games. Yes. Which run in browser.

**[01:16:52]** HTML games. Yes. Which run in browser. So for that game building agent, I would

**[01:16:54]** So for that game building agent, I would

**[01:16:54]** So for that game building agent, I would need the testing envir so the running

**[01:16:57]** need the testing envir so the running

**[01:16:57]** need the testing envir so the running and testing environment to be browser.

**[01:16:59]** and testing environment to be browser.

**[01:16:59]** and testing environment to be browser. Yes. So does Dagger has th those sort of


### [01:17:00 - 01:18:00]

**[01:17:01]** Yes. So does Dagger has th those sort of

**[01:17:01]** Yes. So does Dagger has th those sort of constructs like let's say if I want to

**[01:17:03]** constructs like let's say if I want to

**[01:17:03]** constructs like let's say if I want to spin up a browser environment and then

**[01:17:05]** spin up a browser environment and then

**[01:17:05]** spin up a browser environment and then do some kind of automation in that for

**[01:17:07]** do some kind of automation in that for

**[01:17:07]** do some kind of automation in that for testing that game which the LLM might

**[01:17:09]** testing that game which the LLM might

**[01:17:09]** testing that game which the LLM might have written. Yeah, I mean you certainly

**[01:17:11]** have written. Yeah, I mean you certainly

**[01:17:11]** have written. Yeah, I mean you certainly can. I mean I've done I've done some

**[01:17:12]** can. I mean I've done I've done some

**[01:17:12]** can. I mean I've done I've done some headless browser stuff. I've also done

**[01:17:14]** headless browser stuff. I've also done

**[01:17:14]** headless browser stuff. I've also done some browser stuff and then connect over

**[01:17:16]** some browser stuff and then connect over

**[01:17:16]** some browser stuff and then connect over VNC and or different yeah you can do a

**[01:17:19]** VNC and or different yeah you can do a

**[01:17:19]** VNC and or different yeah you can do a lot of you know you can do uh you can do

**[01:17:23]** lot of you know you can do uh you can do

**[01:17:23]** lot of you know you can do uh you can do a lot of stuff u with Linux containers

**[01:17:26]** a lot of stuff u with Linux containers

**[01:17:26]** a lot of stuff u with Linux containers um so yeah we should talk about it you

**[01:17:29]** um so yeah we should talk about it you

**[01:17:29]** um so yeah we should talk about it you should come come in the community let's

**[01:17:31]** should come come in the community let's

**[01:17:31]** should come come in the community let's like do it

**[01:17:36]** great demo and uh thanks for compressing

**[01:17:36]** great demo and uh thanks for compressing a lot of information uh so is my

**[01:17:39]** a lot of information uh so is my

**[01:17:39]** a lot of information uh so is my understanding that you build CI/CD infra

**[01:17:42]** understanding that you build CI/CD infra

**[01:17:42]** understanding that you build CI/CD infra and all these things once and then let

**[01:17:44]** and all these things once and then let

**[01:17:44]** and all these things once and then let Dagger do the asynchronous job of with

**[01:17:46]** Dagger do the asynchronous job of with

**[01:17:46]** Dagger do the asynchronous job of with guardrails and you know uh all the

**[01:17:48]** guardrails and you know uh all the

**[01:17:48]** guardrails and you know uh all the things in place like is it is my

**[01:17:51]** things in place like is it is my

**[01:17:51]** things in place like is it is my understanding that Dagger is sort of

**[01:17:52]** understanding that Dagger is sort of

**[01:17:52]** understanding that Dagger is sort of this asynchronous AI agent that does

**[01:17:54]** this asynchronous AI agent that does

**[01:17:54]** this asynchronous AI agent that does things on its own but with guardrails

**[01:17:57]** things on its own but with guardrails

**[01:17:57]** things on its own but with guardrails not just leaving uh cloud code or

**[01:17:59]** not just leaving uh cloud code or

**[01:17:59]** not just leaving uh cloud code or something uh in a trust all mode and


### [01:18:00 - 01:19:00]

**[01:18:01]** something uh in a trust all mode and

**[01:18:01]** something uh in a trust all mode and then let it do its thing is is that

**[01:18:03]** then let it do its thing is is that

**[01:18:03]** then let it do its thing is is that right I think yeah so the question was

**[01:18:06]** right I think yeah so the question was

**[01:18:06]** right I think yeah so the question was like yeah is what is Dagger in a certain

**[01:18:08]** like yeah is what is Dagger in a certain

**[01:18:08]** like yeah is what is Dagger in a certain sense too but Dagger gives you this

**[01:18:10]** sense too but Dagger gives you this

**[01:18:10]** sense too but Dagger gives you this platform to create these software

**[01:18:12]** platform to create these software

**[01:18:12]** platform to create these software engineering workflows that can be used

**[01:18:14]** engineering workflows that can be used

**[01:18:14]** engineering workflows that can be used for shipping software. They can be used

**[01:18:16]** for shipping software. They can be used

**[01:18:16]** for shipping software. They can be used for developing software, you know, and

**[01:18:17]** for developing software, you know, and

**[01:18:17]** for developing software, you know, and the environments that we saw and then

**[01:18:20]** the environments that we saw and then

**[01:18:20]** the environments that we saw and then you can use them uh as a platform

**[01:18:22]** you can use them uh as a platform

**[01:18:22]** you can use them uh as a platform engineer or as a developer, but then you

**[01:18:24]** engineer or as a developer, but then you

**[01:18:24]** engineer or as a developer, but then you can also hand them off to agents. And so

**[01:18:27]** can also hand them off to agents. And so

**[01:18:27]** can also hand them off to agents. And so we think that's really powerful, the

**[01:18:29]** we think that's really powerful, the

**[01:18:29]** we think that's really powerful, the fact that you can use that same platform

**[01:18:30]** fact that you can use that same platform

**[01:18:30]** fact that you can use that same platform to do all those things and to create

**[01:18:32]** to do all those things and to create

**[01:18:32]** to do all those things and to create those guard rails like you say. Um you

**[01:18:34]** those guard rails like you say. Um you

**[01:18:34]** those guard rails like you say. Um you can the one thing I wanted you to show

**[01:18:36]** can the one thing I wanted you to show

**[01:18:36]** can the one thing I wanted you to show and you got one minute. Can you just

**[01:18:37]** and you got one minute. Can you just

**[01:18:37]** and you got one minute. Can you just show your terminal and just let's get

**[01:18:40]** show your terminal and just let's get

**[01:18:40]** show your terminal and just let's get vibe for just one second. So you're

**[01:18:42]** vibe for just one second. So you're

**[01:18:42]** vibe for just one second. So you're connected to an LLM right now, right? So

**[01:18:45]** connected to an LLM right now, right? So

**[01:18:45]** connected to an LLM right now, right? So um go ahead just like let's talk to this

**[01:18:47]** um go ahead just like let's talk to this

**[01:18:47]** um go ahead just like let's talk to this LLM. So it turns out that we've been

**[01:18:51]** LLM. So it turns out that we've been

**[01:18:51]** LLM. So it turns out that we've been using the shell mode which lets you know

**[01:18:53]** using the shell mode which lets you know

**[01:18:53]** using the shell mode which lets you know kind of like very declaratively say like

**[01:18:54]** kind of like very declaratively say like

**[01:18:54]** kind of like very declaratively say like I want container from Alpine with this

**[01:18:57]** I want container from Alpine with this

**[01:18:57]** I want container from Alpine with this file and give me a terminal into that or

**[01:18:59]** file and give me a terminal into that or

**[01:18:59]** file and give me a terminal into that or whatever. Now what we've done is we just


### [01:19:00 - 01:20:00]

**[01:19:02]** whatever. Now what we've done is we just

**[01:19:02]** whatever. Now what we've done is we just had we're like we're chatting now

**[01:19:04]** had we're like we're chatting now

**[01:19:04]** had we're like we're chatting now directly with the connected LLM and this

**[01:19:07]** directly with the connected LLM and this

**[01:19:07]** directly with the connected LLM and this LLM can see all the Dagger objects you

**[01:19:10]** LLM can see all the Dagger objects you

**[01:19:10]** LLM can see all the Dagger objects you have. So another way you can use Dagger

**[01:19:13]** have. So another way you can use Dagger

**[01:19:13]** have. So another way you can use Dagger is you can just say like all right I'm

**[01:19:14]** is you can just say like all right I'm

**[01:19:14]** is you can just say like all right I'm just going to create this container and

**[01:19:16]** just going to create this container and

**[01:19:16]** just going to create this container and I'm gonna say hey LLM you see that

**[01:19:18]** I'm gonna say hey LLM you see that

**[01:19:18]** I'm gonna say hey LLM you see that container why don't you write some

**[01:19:19]** container why don't you write some

**[01:19:19]** container why don't you write some software in it. So you can get that kind

**[01:19:22]** software in it. So you can get that kind

**[01:19:22]** software in it. So you can get that kind of that kind of workflow going too. So

**[01:19:25]** of that kind of workflow going too. So

**[01:19:25]** of that kind of workflow going too. So he's there you go. So he's actually

**[01:19:26]** he's there you go. So he's actually

**[01:19:26]** he's there you go. So he's actually saying like hey give me a Python

**[01:19:28]** saying like hey give me a Python

**[01:19:28]** saying like hey give me a Python container and so it's going to actually

**[01:19:30]** container and so it's going to actually

**[01:19:30]** container and so it's going to actually look and see what methods exist in the

**[01:19:33]** look and see what methods exist in the

**[01:19:33]** look and see what methods exist in the Dagger API. It's oh there's this

**[01:19:35]** Dagger API. It's oh there's this

**[01:19:36]** Dagger API. It's oh there's this container method in the API which we

**[01:19:37]** container method in the API which we

**[01:19:37]** container method in the API which we were using earlier and then it's going

**[01:19:39]** were using earlier and then it's going

**[01:19:39]** were using earlier and then it's going to like you know decide oh I'm going to

**[01:19:41]** to like you know decide oh I'm going to

**[01:19:41]** to like you know decide oh I'm going to use container maybe from container from

**[01:19:44]** use container maybe from container from

**[01:19:44]** use container maybe from container from container with exec to execute. So these

**[01:19:46]** container with exec to execute. So these

**[01:19:46]** container with exec to execute. So these are just it's exploring the dagger API

**[01:19:49]** are just it's exploring the dagger API

**[01:19:49]** are just it's exploring the dagger API right now. Got it. And now it's going to

**[01:19:51]** right now. Got it. And now it's going to

**[01:19:51]** right now. Got it. And now it's going to like it's actually pulling a Python 3.11

**[01:19:53]** like it's actually pulling a Python 3.11

**[01:19:53]** like it's actually pulling a Python 3.11 container then it can like do things

**[01:19:55]** container then it can like do things

**[01:19:55]** container then it can like do things with that. So you know it's actually

**[01:19:57]** with that. So you know it's actually

**[01:19:57]** with that. So you know it's actually using containers like kind of like

**[01:19:59]** using containers like kind of like

**[01:19:59]** using containers like kind of like computer use or something like that. But


### [01:20:00 - 01:21:00]

**[01:20:01]** computer use or something like that. But

**[01:20:02]** computer use or something like that. But um so yeah, so you can get you can go we

**[01:20:05]** um so yeah, so you can get you can go we

**[01:20:05]** um so yeah, so you can get you can go we didn't even show that side of it because

**[01:20:07]** didn't even show that side of it because

**[01:20:07]** didn't even show that side of it because you know we're trying to show the ver

**[01:20:08]** you know we're trying to show the ver

**[01:20:08]** you know we're trying to show the ver show the guardrails but you can also use

**[01:20:10]** show the guardrails but you can also use

**[01:20:10]** show the guardrails but you can also use it in this kind of a style too. Got it.

**[01:20:13]** it in this kind of a style too. Got it.

**[01:20:13]** it in this kind of a style too. Got it. Uh and one one follow-up question uh

**[01:20:15]** Uh and one one follow-up question uh

**[01:20:15]** Uh and one one follow-up question uh typically LLMs are good at small to

**[01:20:17]** typically LLMs are good at small to

**[01:20:17]** typically LLMs are good at small to medium tasks and that's what we have

**[01:20:19]** medium tasks and that's what we have

**[01:20:19]** medium tasks and that's what we have seen like a small to medium task here.

**[01:20:21]** seen like a small to medium task here.

**[01:20:21]** seen like a small to medium task here. How uh good is Dagger at orchest

**[01:20:23]** How uh good is Dagger at orchest

**[01:20:23]** How uh good is Dagger at orchest orchestrating uh like a large task which

**[01:20:26]** orchestrating uh like a large task which

**[01:20:26]** orchestrating uh like a large task which need which needs design or some user

**[01:20:28]** need which needs design or some user

**[01:20:28]** need which needs design or some user input or you know multi-turn prompt uh

**[01:20:31]** input or you know multi-turn prompt uh

**[01:20:31]** input or you know multi-turn prompt uh like you know not a small medium task

**[01:20:33]** like you know not a small medium task

**[01:20:33]** like you know not a small medium task but a large task. How is dagger with

**[01:20:35]** but a large task. How is dagger with

**[01:20:35]** but a large task. How is dagger with that? Yeah the question is like a size

**[01:20:37]** that? Yeah the question is like a size

**[01:20:37]** that? Yeah the question is like a size of task that dagger is good for. I think

**[01:20:39]** of task that dagger is good for. I think

**[01:20:39]** of task that dagger is good for. I think if you make it if you decompose things

**[01:20:41]** if you make it if you decompose things

**[01:20:41]** if you make it if you decompose things down and you can architect things right

**[01:20:43]** down and you can architect things right

**[01:20:43]** down and you can architect things right it can handle a lot of different sizes

**[01:20:45]** it can handle a lot of different sizes

**[01:20:45]** it can handle a lot of different sizes and we should I know we're at time now

**[01:20:46]** and we should I know we're at time now

**[01:20:46]** and we should I know we're at time now so we're going to like we're going to

**[01:20:47]** so we're going to like we're going to

**[01:20:47]** so we're going to like we're going to end here. We'll take some more questions

**[01:20:49]** end here. We'll take some more questions

**[01:20:49]** end here. We'll take some more questions outside the room, but in the hall for

**[01:20:50]** outside the room, but in the hall for

**[01:20:50]** outside the room, but in the hall for sure. Thank you so much for everybody

**[01:20:52]** sure. Thank you so much for everybody

**[01:20:52]** sure. Thank you so much for everybody that attended. Thank you guys.

**[01:20:54]** that attended. Thank you guys.

**[01:20:54]** that attended. Thank you guys. [Music]


