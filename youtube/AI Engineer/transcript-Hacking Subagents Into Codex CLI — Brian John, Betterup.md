# Hacking Subagents Into Codex CLI — Brian John, Betterup

**Video URL:** https://www.youtube.com/watch?v=5eJqXtevlXg

---

## Full Transcript

### [00:00 - 01:00]

**[00:05]** Hi everybody, my name is Brian John and

**[00:05]** Hi everybody, my name is Brian John and I'm excited today to talk to you about

**[00:07]** I'm excited today to talk to you about

**[00:07]** I'm excited today to talk to you about hacking sub agents in the codeex CLI. So

**[00:10]** hacking sub agents in the codeex CLI. So

**[00:10]** hacking sub agents in the codeex CLI. So who am I? I'm a principal fullstack

**[00:13]** who am I? I'm a principal fullstack

**[00:13]** who am I? I'm a principal fullstack engineer. My current focus at work is AI

**[00:16]** engineer. My current focus at work is AI

**[00:16]** engineer. My current focus at work is AI enablement for R&D. So think helping our

**[00:19]** enablement for R&D. So think helping our

**[00:19]** enablement for R&D. So think helping our R&D team members get their work done

**[00:22]** R&D team members get their work done

**[00:22]** R&D team members get their work done faster and with higher quality using AI.

**[00:25]** faster and with higher quality using AI.

**[00:25]** faster and with higher quality using AI. The company I work for is BetterUp. It's

**[00:27]** The company I work for is BetterUp. It's

**[00:27]** The company I work for is BetterUp. It's an awesome place to work. We've been

**[00:29]** an awesome place to work. We've been

**[00:29]** an awesome place to work. We've been using AI since the very beginning. I've

**[00:31]** using AI since the very beginning. I've

**[00:31]** using AI since the very beginning. I've been there for over eight years now,

**[00:33]** been there for over eight years now,

**[00:33]** been there for over eight years now, which is longer than any place I've ever

**[00:34]** which is longer than any place I've ever

**[00:34]** which is longer than any place I've ever worked before. And our mission is to

**[00:37]** worked before. And our mission is to

**[00:37]** worked before. And our mission is to help people everywhere live their lives

**[00:39]** help people everywhere live their lives

**[00:39]** help people everywhere live their lives with better purpose, clarity, and

**[00:41]** with better purpose, clarity, and

**[00:41]** with better purpose, clarity, and passion. If that sounds interesting to

**[00:43]** passion. If that sounds interesting to

**[00:43]** passion. If that sounds interesting to you, you work want to work on cool stuff

**[00:45]** you, you work want to work on cool stuff

**[00:45]** you, you work want to work on cool stuff with LLMs,

**[00:47]** with LLMs,

**[00:47]** with LLMs, please hit me up. I'll add my contact

**[00:49]** please hit me up. I'll add my contact

**[00:49]** please hit me up. I'll add my contact info in the last slide.

**[00:52]** info in the last slide.

**[00:52]** info in the last slide. So, why would we want to hack sub agents

**[00:55]** So, why would we want to hack sub agents

**[00:55]** So, why would we want to hack sub agents into Codeex CLI?


### [01:00 - 02:00]

**[01:01]** Well, I've been using Clog Code as my

**[01:01]** Well, I've been using Clog Code as my daily driver since the very beginning.

**[01:04]** daily driver since the very beginning.

**[01:04]** daily driver since the very beginning. It's a great tool. It's got tons of

**[01:06]** It's a great tool. It's got tons of

**[01:06]** It's a great tool. It's got tons of bells and whistles. It's got great

**[01:08]** bells and whistles. It's got great

**[01:08]** bells and whistles. It's got great models,

**[01:09]** models,

**[01:09]** models, and I use sub agents all the time. But I

**[01:12]** and I use sub agents all the time. But I

**[01:12]** and I use sub agents all the time. But I don't want to be locked in to one tool,

**[01:14]** don't want to be locked in to one tool,

**[01:14]** don't want to be locked in to one tool, and I really don't want to be locked in

**[01:16]** and I really don't want to be locked in

**[01:16]** and I really don't want to be locked in to one model family.

**[01:19]** to one model family.

**[01:19]** to one model family. I wanted to be able to use other tools,

**[01:21]** I wanted to be able to use other tools,

**[01:22]** I wanted to be able to use other tools, particularly codec CLI, because the

**[01:24]** particularly codec CLI, because the

**[01:24]** particularly codec CLI, because the models look really good and I want to be

**[01:27]** models look really good and I want to be

**[01:27]** models look really good and I want to be able to still use sub aents with them so

**[01:29]** able to still use sub aents with them so

**[01:29]** able to still use sub aents with them so that I can use my workflows

**[01:31]** that I can use my workflows

**[01:31]** that I can use my workflows with other tools.

**[01:35]** with other tools.

**[01:35]** with other tools. Context management. So, as you all know,

**[01:37]** Context management. So, as you all know,

**[01:38]** Context management. So, as you all know, sub agents are amazing for context

**[01:40]** sub agents are amazing for context

**[01:40]** sub agents are amazing for context management. The main agent can give a

**[01:43]** management. The main agent can give a

**[01:43]** management. The main agent can give a problem to a sub agent. It can go off,

**[01:46]** problem to a sub agent. It can go off,

**[01:46]** problem to a sub agent. It can go off, do its work, use its tokens, and pass

**[01:49]** do its work, use its tokens, and pass

**[01:49]** do its work, use its tokens, and pass just the answer back to the main agent.

**[01:51]** just the answer back to the main agent.

**[01:51]** just the answer back to the main agent. And all that context got used up by the

**[01:53]** And all that context got used up by the

**[01:53]** And all that context got used up by the sub agent doesn't end up in your main

**[01:55]** sub agent doesn't end up in your main

**[01:55]** sub agent doesn't end up in your main context window, which is incredible.


### [02:00 - 03:00]

**[02:02]** And I don't think I have to say any more

**[02:02]** And I don't think I have to say any more about this one. We've all seen this way

**[02:03]** about this one. We've all seen this way

**[02:03]** about this one. We've all seen this way too many times and it gets annoying.

**[02:06]** too many times and it gets annoying.

**[02:06]** too many times and it gets annoying. And I have to give credit where credit

**[02:08]** And I have to give credit where credit

**[02:08]** And I have to give credit where credit is due. This talk by Dex Hory changed

**[02:12]** is due. This talk by Dex Hory changed

**[02:12]** is due. This talk by Dex Hory changed the way that I work with AI.

**[02:15]** the way that I work with AI.

**[02:15]** the way that I work with AI. The workflows he proposes here I found

**[02:18]** The workflows he proposes here I found

**[02:18]** The workflows he proposes here I found to be really effective especially in

**[02:22]** to be really effective especially in

**[02:22]** to be really effective especially in working with large code bases. I'd

**[02:25]** working with large code bases. I'd

**[02:25]** working with large code bases. I'd recommend you check out this talk. He's

**[02:27]** recommend you check out this talk. He's

**[02:27]** recommend you check out this talk. He's also talking at AI engineer code this

**[02:29]** also talking at AI engineer code this

**[02:29]** also talking at AI engineer code this year and I recommend you check out that

**[02:31]** year and I recommend you check out that

**[02:31]** year and I recommend you check out that one too because I'm sure it's going to

**[02:32]** one too because I'm sure it's going to

**[02:32]** one too because I'm sure it's going to be great.

**[02:40]** All right, so let's talk about design.

**[02:40]** All right, so let's talk about design. At the end of the day, a sub aent is

**[02:42]** At the end of the day, a sub aent is

**[02:42]** At the end of the day, a sub aent is really simple. It's just another

**[02:43]** really simple. It's just another

**[02:44]** really simple. It's just another instance of the main agent. So our

**[02:46]** instance of the main agent. So our

**[02:46]** instance of the main agent. So our design can also be really simple.

**[02:49]** design can also be really simple.

**[02:49]** design can also be really simple. In this case, we're going to have our

**[02:50]** In this case, we're going to have our

**[02:50]** In this case, we're going to have our parent codec session.

**[02:52]** parent codec session.

**[02:52]** parent codec session. We're going to have it run a script.

**[02:54]** We're going to have it run a script.

**[02:54]** We're going to have it run a script. It's just going to be a wrapper script

**[02:56]** It's just going to be a wrapper script

**[02:56]** It's just going to be a wrapper script that's going to kind of take care of

**[02:58]** that's going to kind of take care of

**[02:58]** that's going to kind of take care of like figuring out what agent to run.


### [03:00 - 04:00]

**[03:00]** like figuring out what agent to run.

**[03:00]** like figuring out what agent to run. It's going to build the prompt, etc.

**[03:02]** It's going to build the prompt, etc.

**[03:02]** It's going to build the prompt, etc. It's going to kick off codeex exec. So

**[03:05]** It's going to kick off codeex exec. So

**[03:05]** It's going to kick off codeex exec. So that child codeex is going to run as the

**[03:07]** that child codeex is going to run as the

**[03:07]** that child codeex is going to run as the sub aent. It's going to respond to the

**[03:09]** sub aent. It's going to respond to the

**[03:09]** sub aent. It's going to respond to the prompt. It's going to do its work and

**[03:10]** prompt. It's going to do its work and

**[03:10]** prompt. It's going to do its work and it's going to write its answer into a

**[03:12]** it's going to write its answer into a

**[03:12]** it's going to write its answer into a file and then our wrapper script is

**[03:15]** file and then our wrapper script is

**[03:15]** file and then our wrapper script is going to read that file and it's going

**[03:17]** going to read that file and it's going

**[03:17]** going to read that file and it's going to print that result to standard out and

**[03:19]** to print that result to standard out and

**[03:19]** to print that result to standard out and give it back to the parent codec

**[03:20]** give it back to the parent codec

**[03:20]** give it back to the parent codec session.

**[03:22]** session.

**[03:22]** session. Pretty straightforward.

**[03:28]** Well, this is simple, so it should be

**[03:28]** Well, this is simple, so it should be easy, right? Well, that's what I thought

**[03:30]** easy, right? Well, that's what I thought

**[03:30]** easy, right? Well, that's what I thought too. And I started to get all these

**[03:32]** too. And I started to get all these

**[03:32]** too. And I started to get all these errors from Codeex when I tried it.

**[03:36]** errors from Codeex when I tried it.

**[03:36]** errors from Codeex when I tried it. Codex's sandbox really seems to not want

**[03:39]** Codex's sandbox really seems to not want

**[03:39]** Codex's sandbox really seems to not want to let you do this. Now, you can of

**[03:41]** to let you do this. Now, you can of

**[03:41]** to let you do this. Now, you can of course run it with dangerously skip

**[03:42]** course run it with dangerously skip

**[03:42]** course run it with dangerously skip permissions or whatever. I don't do

**[03:45]** permissions or whatever. I don't do

**[03:45]** permissions or whatever. I don't do that,

**[03:47]** that,

**[03:47]** that, but to get it to work with the normal

**[03:49]** but to get it to work with the normal

**[03:49]** but to get it to work with the normal set of permissions actually was really,

**[03:51]** set of permissions actually was really,

**[03:52]** set of permissions actually was really, really hard and I bang my head against

**[03:53]** really hard and I bang my head against

**[03:53]** really hard and I bang my head against the wall a long time trying to get this

**[03:55]** the wall a long time trying to get this

**[03:55]** the wall a long time trying to get this to work.


### [04:00 - 05:00]

**[04:01]** So, figuring out the minimum required

**[04:01]** So, figuring out the minimum required permissions is probably the hardest part

**[04:04]** permissions is probably the hardest part

**[04:04]** permissions is probably the hardest part about this. getting the combination just

**[04:06]** about this. getting the combination just

**[04:06]** about this. getting the combination just right. On the parent, you need at least

**[04:08]** right. On the parent, you need at least

**[04:08]** right. On the parent, you need at least sandbox of workspace, right, to be able

**[04:10]** sandbox of workspace, right, to be able

**[04:10]** sandbox of workspace, right, to be able to run the codeex command. You can

**[04:12]** to run the codeex command. You can

**[04:12]** to run the codeex command. You can always run that dangerously whatever

**[04:15]** always run that dangerously whatever

**[04:15]** always run that dangerously whatever whatever command if you want. Again, I

**[04:17]** whatever command if you want. Again, I

**[04:17]** whatever command if you want. Again, I don't really do that. The child process

**[04:20]** don't really do that. The child process

**[04:20]** don't really do that. The child process is a little bit trickier. The sandbox

**[04:22]** is a little bit trickier. The sandbox

**[04:22]** is a little bit trickier. The sandbox prevents its access to the OpenAI

**[04:25]** prevents its access to the OpenAI

**[04:25]** prevents its access to the OpenAI credentials in your home directory since

**[04:27]** credentials in your home directory since

**[04:27]** credentials in your home directory since it's outside of the workspace.

**[04:30]** it's outside of the workspace.

**[04:30]** it's outside of the workspace. the you need at least sandbox workspace

**[04:32]** the you need at least sandbox workspace

**[04:32]** the you need at least sandbox workspace write again so that it can write the

**[04:35]** write again so that it can write the

**[04:35]** write again so that it can write the file that the uh wrapper script is going

**[04:38]** file that the uh wrapper script is going

**[04:38]** file that the uh wrapper script is going to read and you need to disable this

**[04:41]** to read and you need to disable this

**[04:41]** to read and you need to disable this thing called the rollout recorder

**[04:44]** thing called the rollout recorder

**[04:44]** thing called the rollout recorder which is like a logging thing the just

**[04:46]** which is like a logging thing the just

**[04:46]** which is like a logging thing the just because the parent sandbox again it

**[04:48]** because the parent sandbox again it

**[04:48]** because the parent sandbox again it prevents file system access to any

**[04:51]** prevents file system access to any

**[04:51]** prevents file system access to any subcomands

**[04:52]** subcomands

**[04:52]** subcomands that are outside of the workspace


### [05:00 - 06:00]

**[05:02]** All right, before we go any further, I

**[05:02]** All right, before we go any further, I have to give a quick note about

**[05:03]** have to give a quick note about

**[05:03]** have to give a quick note about security.

**[05:05]** security.

**[05:05]** security. Meta recently wrote a great paper called

**[05:07]** Meta recently wrote a great paper called

**[05:07]** Meta recently wrote a great paper called the agents rule of two that I think

**[05:09]** the agents rule of two that I think

**[05:09]** the agents rule of two that I think explains this really, really well. And

**[05:11]** explains this really, really well. And

**[05:12]** explains this really, really well. And what it says is there's three things you

**[05:13]** what it says is there's three things you

**[05:13]** what it says is there's three things you need to care about with your agent when

**[05:15]** need to care about with your agent when

**[05:15]** need to care about with your agent when it comes to security. whether it's

**[05:17]** it comes to security. whether it's

**[05:17]** it comes to security. whether it's processing untrustworthy input, whether

**[05:20]** processing untrustworthy input, whether

**[05:20]** processing untrustworthy input, whether it has access to sensitive systems or

**[05:22]** it has access to sensitive systems or

**[05:22]** it has access to sensitive systems or private data, and whether it can change

**[05:24]** private data, and whether it can change

**[05:24]** private data, and whether it can change state or communicate externally.

**[05:27]** state or communicate externally.

**[05:27]** state or communicate externally. In our case, we're not processing

**[05:29]** In our case, we're not processing

**[05:29]** In our case, we're not processing untrustworthy inputs.

**[05:31]** untrustworthy inputs.

**[05:31]** untrustworthy inputs. We do have access to sensitive systems

**[05:33]** We do have access to sensitive systems

**[05:33]** We do have access to sensitive systems or private data because we're probably

**[05:35]** or private data because we're probably

**[05:35]** or private data because we're probably working with a proprietary codebase.

**[05:41]** And it can change state and it also can

**[05:41]** And it can change state and it also can can communicate externally. Now the

**[05:44]** can communicate externally. Now the

**[05:44]** can communicate externally. Now the state that it can change is really kind

**[05:45]** state that it can change is really kind

**[05:45]** state that it can change is really kind of dependent on your system. In my case,

**[05:48]** of dependent on your system. In my case,

**[05:48]** of dependent on your system. In my case, it's really not very high risk and the

**[05:51]** it's really not very high risk and the

**[05:51]** it's really not very high risk and the communication it does externally is just

**[05:53]** communication it does externally is just

**[05:53]** communication it does externally is just to OpenAI's API endpoint. So again,

**[05:57]** to OpenAI's API endpoint. So again,

**[05:57]** to OpenAI's API endpoint. So again, not a major risk, I would say. So that

**[05:59]** not a major risk, I would say. So that

**[05:59]** not a major risk, I would say. So that puts us in the lower risk category. But


### [06:00 - 07:00]

**[06:03]** puts us in the lower risk category. But

**[06:03]** puts us in the lower risk category. But importantly,

**[06:04]** importantly,

**[06:04]** importantly, lower risk does not mean no risk. So

**[06:07]** lower risk does not mean no risk. So

**[06:07]** lower risk does not mean no risk. So your mileage may vary here. you need to

**[06:09]** your mileage may vary here. you need to

**[06:09]** your mileage may vary here. you need to make your own determination on if this

**[06:11]** make your own determination on if this

**[06:11]** make your own determination on if this is something you feel comfortable with.

**[06:15]** is something you feel comfortable with.

**[06:15]** is something you feel comfortable with. With that, let's move forward.

**[06:18]** With that, let's move forward.

**[06:18]** With that, let's move forward. All right. So, to get codeex to be able

**[06:20]** All right. So, to get codeex to be able

**[06:20]** All right. So, to get codeex to be able to use sub agents with this wrapper

**[06:23]** to use sub agents with this wrapper

**[06:23]** to use sub agents with this wrapper script and everything, we have to tell

**[06:25]** script and everything, we have to tell

**[06:25]** script and everything, we have to tell it how to run them. So in our agents MD

**[06:28]** it how to run them. So in our agents MD

**[06:28]** it how to run them. So in our agents MD we're going to have just a little bit of

**[06:30]** we're going to have just a little bit of

**[06:30]** we're going to have just a little bit of information here that tells codeex hey

**[06:32]** information here that tells codeex hey

**[06:32]** information here that tells codeex hey when I say use the whatever sub agent go

**[06:38]** when I say use the whatever sub agent go

**[06:38]** when I say use the whatever sub agent go and actually like run this script and

**[06:41]** and actually like run this script and

**[06:41]** and actually like run this script and you know with these commands or whatever

**[06:43]** you know with these commands or whatever

**[06:43]** you know with these commands or whatever and that's how you do it.

**[06:47]** and that's how you do it.

**[06:47]** and that's how you do it. Also we have to tell it when to run sub

**[06:50]** Also we have to tell it when to run sub

**[06:50]** Also we have to tell it when to run sub aents. So that would be you know when

**[06:52]** aents. So that would be you know when

**[06:52]** aents. So that would be you know when the user asks or just when you think

**[06:54]** the user asks or just when you think

**[06:54]** the user asks or just when you think helpful. Then we want to tell it what

**[06:56]** helpful. Then we want to tell it what

**[06:56]** helpful. Then we want to tell it what sub aents are available and what they

**[06:58]** sub aents are available and what they

**[06:58]** sub aents are available and what they do.


### [07:00 - 08:00]

**[07:06]** All right, with that, let's do a quick

**[07:06]** All right, with that, let's do a quick demo.

**[07:13]** I've put together a really quick and

**[07:13]** I've put together a really quick and small proof of concept repository. It's

**[07:16]** small proof of concept repository. It's

**[07:16]** small proof of concept repository. It's open source. You can go and take a look

**[07:18]** open source. You can go and take a look

**[07:18]** open source. You can go and take a look at it yourself. I'll have the URL at the

**[07:20]** at it yourself. I'll have the URL at the

**[07:20]** at it yourself. I'll have the URL at the end of the talk. Let's just take a look

**[07:22]** end of the talk. Let's just take a look

**[07:22]** end of the talk. Let's just take a look at what's in here.

**[07:24]** at what's in here.

**[07:24]** at what's in here. So, first of all, let's take a look at

**[07:26]** So, first of all, let's take a look at

**[07:26]** So, first of all, let's take a look at our agents.

**[07:28]** our agents.

**[07:28]** our agents. I just created a couple of toy agents

**[07:30]** I just created a couple of toy agents

**[07:30]** I just created a couple of toy agents here. Let's go take a look at them how

**[07:32]** here. Let's go take a look at them how

**[07:32]** here. Let's go take a look at them how they're defined.

**[07:35]** they're defined.

**[07:35]** they're defined. You can see here each agent has a name.

**[07:38]** You can see here each agent has a name.

**[07:38]** You can see here each agent has a name. It also has a reasoning effort. So,

**[07:40]** It also has a reasoning effort. So,

**[07:40]** It also has a reasoning effort. So, depending on what kind of work it's

**[07:42]** depending on what kind of work it's

**[07:42]** depending on what kind of work it's doing, you can give it a light, medium,

**[07:44]** doing, you can give it a light, medium,

**[07:44]** doing, you can give it a light, medium, you can give it a high reasoning effort,

**[07:47]** you can give it a high reasoning effort,

**[07:47]** you can give it a high reasoning effort, whatever you think is appropriate. Then

**[07:49]** whatever you think is appropriate. Then

**[07:49]** whatever you think is appropriate. Then you just give it, you know, the prompt

**[07:51]** you just give it, you know, the prompt

**[07:51]** you just give it, you know, the prompt for the agent. So very similar to kind

**[07:53]** for the agent. So very similar to kind

**[07:53]** for the agent. So very similar to kind of how claude code sub aents work. In

**[07:55]** of how claude code sub aents work. In

**[07:55]** of how claude code sub aents work. In this case, it's just counting words. You

**[07:58]** this case, it's just counting words. You

**[07:58]** this case, it's just counting words. You know, this other one is a file writer

**[07:59]** know, this other one is a file writer

**[07:59]** know, this other one is a file writer agent. Just going to take some text and


### [08:00 - 09:00]

**[08:01]** agent. Just going to take some text and

**[08:01]** agent. Just going to take some text and put it in a file. Don't need much

**[08:03]** put it in a file. Don't need much

**[08:03]** put it in a file. Don't need much reasoning for that.

**[08:09]** All right. So now let's look at our

**[08:09]** All right. So now let's look at our wrapper script.

**[08:18]** It's really small, only 72 lines.

**[08:18]** It's really small, only 72 lines. basically just takes in the inputs.

**[08:24]** basically just takes in the inputs.

**[08:24]** basically just takes in the inputs. It's going to call this agent exeutor

**[08:26]** It's going to call this agent exeutor

**[08:26]** It's going to call this agent exeutor Python class, which I'll show in just a

**[08:28]** Python class, which I'll show in just a

**[08:28]** Python class, which I'll show in just a minute. Also very small, and it's going

**[08:29]** minute. Also very small, and it's going

**[08:29]** minute. Also very small, and it's going to return that uh the agent's output to

**[08:34]** to return that uh the agent's output to

**[08:34]** to return that uh the agent's output to standard out so that the main agent can

**[08:37]** standard out so that the main agent can

**[08:37]** standard out so that the main agent can see it. Let's look at that agent

**[08:39]** see it. Let's look at that agent

**[08:39]** see it. Let's look at that agent executive class.

**[08:42]** executive class.

**[08:42]** executive class. Not going to go through this whole

**[08:43]** Not going to go through this whole

**[08:43]** Not going to go through this whole thing. Again, it's pretty small.

**[08:46]** thing. Again, it's pretty small.

**[08:46]** thing. Again, it's pretty small. basically just kicks off the child sub

**[08:48]** basically just kicks off the child sub

**[08:48]** basically just kicks off the child sub agent with the proper permissions and

**[08:50]** agent with the proper permissions and

**[08:50]** agent with the proper permissions and with the right reasoning effort

**[08:53]** with the right reasoning effort

**[08:53]** with the right reasoning effort and it disables the rollout recorder all

**[08:55]** and it disables the rollout recorder all

**[08:55]** and it disables the rollout recorder all that kind of stuff just does all that

**[08:56]** that kind of stuff just does all that

**[08:56]** that kind of stuff just does all that for you. So pretty handy. One thing that


### [09:00 - 10:00]

**[09:00]** for you. So pretty handy. One thing that

**[09:00]** for you. So pretty handy. One thing that I think I didn't cover you look at

**[09:02]** I think I didn't cover you look at

**[09:02]** I think I didn't cover you look at agents MD

**[09:05]** agents MD

**[09:05]** agents MD is it's kind of important here is this

**[09:08]** is it's kind of important here is this

**[09:08]** is it's kind of important here is this part. So when we're telling Codeex how

**[09:13]** part. So when we're telling Codeex how

**[09:13]** part. So when we're telling Codeex how to invoke the sub agent, we're going to

**[09:15]** to invoke the sub agent, we're going to

**[09:15]** to invoke the sub agent, we're going to have it write the agent name to a file.

**[09:17]** have it write the agent name to a file.

**[09:17]** have it write the agent name to a file. We're going to have it write the user's

**[09:19]** We're going to have it write the user's

**[09:19]** We're going to have it write the user's query to a file and then we're going to

**[09:20]** query to a file and then we're going to

**[09:20]** query to a file and then we're going to have it run this command.

**[09:22]** have it run this command.

**[09:22]** have it run this command. You know, another alternative to this

**[09:24]** You know, another alternative to this

**[09:24]** You know, another alternative to this would be to actually pass the agent name

**[09:27]** would be to actually pass the agent name

**[09:27]** would be to actually pass the agent name and the query as command arguments. The

**[09:30]** and the query as command arguments. The

**[09:30]** and the query as command arguments. The reason why we don't want to do that is

**[09:32]** reason why we don't want to do that is

**[09:32]** reason why we don't want to do that is because of Codex's permissioning system.

**[09:36]** because of Codex's permissioning system.

**[09:36]** because of Codex's permissioning system. As long as the command looks exactly the

**[09:38]** As long as the command looks exactly the

**[09:38]** As long as the command looks exactly the same, you only have to grant permission

**[09:42]** same, you only have to grant permission

**[09:42]** same, you only have to grant permission once. But if you have different

**[09:44]** once. But if you have different

**[09:44]** once. But if you have different arguments to the command, you have to

**[09:46]** arguments to the command, you have to

**[09:46]** arguments to the command, you have to approve it every time. So it gets really

**[09:49]** approve it every time. So it gets really

**[09:49]** approve it every time. So it gets really annoying if you have to approve every

**[09:52]** annoying if you have to approve every

**[09:52]** annoying if you have to approve every time that codeex wants to call sub

**[09:55]** time that codeex wants to call sub

**[09:55]** time that codeex wants to call sub agent.

**[09:57]** agent.

**[09:57]** agent. So in this case, we make the command

**[09:58]** So in this case, we make the command

**[09:58]** So in this case, we make the command look exactly the same. Codex is just


### [10:00 - 11:00]

**[10:00]** look exactly the same. Codex is just

**[10:00]** look exactly the same. Codex is just going to run it.

**[10:03]** going to run it.

**[10:03]** going to run it. Now, if you run again with dangerously

**[10:05]** Now, if you run again with dangerously

**[10:05]** Now, if you run again with dangerously skip permissions or whatever, you don't

**[10:06]** skip permissions or whatever, you don't

**[10:06]** skip permissions or whatever, you don't have to worry about this.

**[10:09]** have to worry about this.

**[10:09]** have to worry about this. But all right, let's go in. Oh, then

**[10:10]** But all right, let's go in. Oh, then

**[10:10]** But all right, let's go in. Oh, then we've got this also this wrapper script

**[10:12]** we've got this also this wrapper script

**[10:12]** we've got this also this wrapper script around codeex. So, let's take a look at

**[10:13]** around codeex. So, let's take a look at

**[10:13]** around codeex. So, let's take a look at that real quick. Super simple. Uh, what

**[10:16]** that real quick. Super simple. Uh, what

**[10:16]** that real quick. Super simple. Uh, what it does is it takes the codeex home

**[10:19]** it does is it takes the codeex home

**[10:19]** it does is it takes the codeex home files from your home directory. It's

**[10:20]** files from your home directory. It's

**[10:20]** files from your home directory. It's going to sync them into a subdirectory

**[10:23]** going to sync them into a subdirectory

**[10:23]** going to sync them into a subdirectory so it has access to them and it's going

**[10:25]** so it has access to them and it's going

**[10:25]** so it has access to them and it's going to set codeex home to that directory.

**[10:27]** to set codeex home to that directory.

**[10:27]** to set codeex home to that directory. And it's just going to launch codeex. In

**[10:29]** And it's just going to launch codeex. In

**[10:29]** And it's just going to launch codeex. In this case, I'm launching in full auto

**[10:31]** this case, I'm launching in full auto

**[10:31]** this case, I'm launching in full auto mode, which is just like shorthand for

**[10:33]** mode, which is just like shorthand for

**[10:33]** mode, which is just like shorthand for workspace, write plus, I think, approval

**[10:36]** workspace, write plus, I think, approval

**[10:36]** workspace, write plus, I think, approval on a request or something like that. I

**[10:38]** on a request or something like that. I

**[10:38]** on a request or something like that. I can't remember which one. Um, but pretty

**[10:40]** can't remember which one. Um, but pretty

**[10:40]** can't remember which one. Um, but pretty straightforward. Not much going on here.

**[10:42]** straightforward. Not much going on here.

**[10:42]** straightforward. Not much going on here. Really not much code.

**[10:45]** Really not much code.

**[10:45]** Really not much code. All right, let's go ahead and launch

**[10:46]** All right, let's go ahead and launch

**[10:46]** All right, let's go ahead and launch this.

**[10:51]** Okay,

**[10:51]** Okay, now let's just give it just a quick

**[10:54]** now let's just give it just a quick

**[10:54]** now let's just give it just a quick query.

**[10:56]** query.

**[10:56]** query. I'm going to tell it to use its work

**[10:57]** I'm going to tell it to use its work

**[10:57]** I'm going to tell it to use its work counter sub agent. Have it go off and do


### [11:00 - 12:00]

**[11:00]** counter sub agent. Have it go off and do

**[11:00]** counter sub agent. Have it go off and do that.

**[11:06]** You're going to see it

**[11:06]** You're going to see it figure out that it needs to run this

**[11:08]** figure out that it needs to run this

**[11:08]** figure out that it needs to run this agent exec. It's going to go ahead and

**[11:10]** agent exec. It's going to go ahead and

**[11:10]** agent exec. It's going to go ahead and put the name of the agent in a file.

**[11:12]** put the name of the agent in a file.

**[11:12]** put the name of the agent in a file. It's going to put query in a file. Then

**[11:15]** It's going to put query in a file. Then

**[11:15]** It's going to put query in a file. Then it's going to ask me for permissions to

**[11:16]** it's going to ask me for permissions to

**[11:16]** it's going to ask me for permissions to run it. And it's really important here

**[11:17]** run it. And it's really important here

**[11:17]** run it. And it's really important here that I say yes and don't ask again for

**[11:19]** that I say yes and don't ask again for

**[11:19]** that I say yes and don't ask again for this command. That way it's not going to

**[11:22]** this command. That way it's not going to

**[11:22]** this command. That way it's not going to ask me every time it has to run a sub

**[11:25]** ask me every time it has to run a sub

**[11:25]** ask me every time it has to run a sub agent.

**[11:26]** agent.

**[11:26]** agent. You'll notice that it's running

**[11:28]** You'll notice that it's running

**[11:28]** You'll notice that it's running everything in serial here. Codeex does

**[11:30]** everything in serial here. Codeex does

**[11:30]** everything in serial here. Codeex does not have the ability to run things

**[11:32]** not have the ability to run things

**[11:32]** not have the ability to run things asynchronously like claw does. So, this

**[11:35]** asynchronously like claw does. So, this

**[11:35]** asynchronously like claw does. So, this is slower. And Codeex in general, if

**[11:38]** is slower. And Codeex in general, if

**[11:38]** is slower. And Codeex in general, if you've used it, I think you find it's

**[11:39]** you've used it, I think you find it's

**[11:40]** you've used it, I think you find it's slower overall than than Cloud Code. But

**[11:45]** slower overall than than Cloud Code. But

**[11:45]** slower overall than than Cloud Code. But I think that's really kind of

**[11:46]** I think that's really kind of

**[11:46]** I think that's really kind of intentional. seems like Codex is really

**[11:48]** intentional. seems like Codex is really

**[11:48]** intentional. seems like Codex is really kind of meant to be more of like a

**[11:50]** kind of meant to be more of like a

**[11:50]** kind of meant to be more of like a hands-off unattended type of a tool

**[11:53]** hands-off unattended type of a tool

**[11:53]** hands-off unattended type of a tool versus clog code is meant to be more

**[11:55]** versus clog code is meant to be more

**[11:55]** versus clog code is meant to be more kind of iterative and so you know I

**[11:58]** kind of iterative and so you know I

**[11:58]** kind of iterative and so you know I think that's actually okay. I found this

**[11:59]** think that's actually okay. I found this

**[11:59]** think that's actually okay. I found this okay for me the way that I've used


### [12:00 - 13:00]

**[12:01]** okay for me the way that I've used

**[12:01]** okay for me the way that I've used codeex. All right so we can see we got

**[12:04]** codeex. All right so we can see we got

**[12:04]** codeex. All right so we can see we got that result back printed to standard out

**[12:06]** that result back printed to standard out

**[12:06]** that result back printed to standard out here and then

**[12:09]** here and then

**[12:09]** here and then codeex just gave us back the answer. So,

**[12:10]** codeex just gave us back the answer. So,

**[12:10]** codeex just gave us back the answer. So, let's just do one more with this file

**[12:12]** let's just do one more with this file

**[12:12]** let's just do one more with this file writer sub agent.

**[12:20]** Again, it's going to do the same thing.

**[12:20]** Again, it's going to do the same thing. It's going to write that agent name into

**[12:22]** It's going to write that agent name into

**[12:22]** It's going to write that agent name into a file. It's going to write

**[12:25]** a file. It's going to write

**[12:25]** a file. It's going to write the query into a file. Then, it's going

**[12:28]** the query into a file. Then, it's going

**[12:28]** the query into a file. Then, it's going to call that same command. It will not

**[12:30]** to call that same command. It will not

**[12:30]** to call that same command. It will not ask for permissions this time.

**[12:36]** Oh, and we're using the timeout 600 here

**[12:36]** Oh, and we're using the timeout 600 here because some of these agents can

**[12:38]** because some of these agents can

**[12:38]** because some of these agents can actually take a long time to run. If

**[12:40]** actually take a long time to run. If

**[12:40]** actually take a long time to run. If you're having it do a big task that's

**[12:42]** you're having it do a big task that's

**[12:42]** you're having it do a big task that's going to have it look across a whole

**[12:44]** going to have it look across a whole

**[12:44]** going to have it look across a whole codebase and you have a large codebase,

**[12:46]** codebase and you have a large codebase,

**[12:46]** codebase and you have a large codebase, it can take up to 10 minutes. I've

**[12:48]** it can take up to 10 minutes. I've

**[12:48]** it can take up to 10 minutes. I've actually seen them take longer, up to 20

**[12:49]** actually seen them take longer, up to 20

**[12:49]** actually seen them take longer, up to 20 minutes sometimes. So, you might even

**[12:52]** minutes sometimes. So, you might even

**[12:52]** minutes sometimes. So, you might even want a longer timeout here. This is what

**[12:54]** want a longer timeout here. This is what

**[12:54]** want a longer timeout here. This is what I set for this example. In this case,

**[12:57]** I set for this example. In this case,

**[12:57]** I set for this example. In this case, this is a pretty easy one. So, it only

**[12:59]** this is a pretty easy one. So, it only

**[12:59]** this is a pretty easy one. So, it only took about 40 seconds. All right. So, it


### [13:00 - 14:00]

**[13:01]** took about 40 seconds. All right. So, it

**[13:01]** took about 40 seconds. All right. So, it wrote the file. Just go ahead and verify

**[13:03]** wrote the file. Just go ahead and verify

**[13:03]** wrote the file. Just go ahead and verify that.

**[13:06]** that.

**[13:06]** that. All right.

**[13:08]** All right.

**[13:08]** All right. All right, that's all I have. You can

**[13:11]** All right, that's all I have. You can

**[13:11]** All right, that's all I have. You can find the code at that URL.

**[13:14]** find the code at that URL.

**[13:14]** find the code at that URL. You can find betterup at betterup.com.

**[13:17]** You can find betterup at betterup.com.

**[13:17]** You can find betterup at betterup.com. If you have any questions for me, you

**[13:18]** If you have any questions for me, you

**[13:18]** If you have any questions for me, you can use my email address or you can DM

**[13:21]** can use my email address or you can DM

**[13:21]** can use my email address or you can DM me on X. I don't post anything on X, so

**[13:24]** me on X. I don't post anything on X, so

**[13:24]** me on X. I don't post anything on X, so really no reason to follow me, but go

**[13:26]** really no reason to follow me, but go

**[13:26]** really no reason to follow me, but go ahead if you want. And I hope this was

**[13:29]** ahead if you want. And I hope this was

**[13:29]** ahead if you want. And I hope this was helpful for you. And again, if BetterUp

**[13:32]** helpful for you. And again, if BetterUp

**[13:32]** helpful for you. And again, if BetterUp sounds like an interesting place to you,

**[13:34]** sounds like an interesting place to you,

**[13:34]** sounds like an interesting place to you, please hit me up. Have a great day.


