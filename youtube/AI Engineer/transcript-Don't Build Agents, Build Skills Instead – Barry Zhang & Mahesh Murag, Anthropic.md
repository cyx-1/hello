# Don't Build Agents, Build Skills Instead – Barry Zhang & Mahesh Murag, Anthropic

**Video URL:** https://www.youtube.com/watch?v=CEvIs9y1uog

---

## Full Transcript

### [00:00 - 01:00]

**[00:22]** All right, good morning and thank you

**[00:22]** All right, good morning and thank you for having us again. Last time we were

**[00:25]** for having us again. Last time we were

**[00:25]** for having us again. Last time we were here, we're still figuring out what an

**[00:26]** here, we're still figuring out what an

**[00:26]** here, we're still figuring out what an agent even is. Today, many of us are

**[00:29]** agent even is. Today, many of us are

**[00:29]** agent even is. Today, many of us are using agents on a daily basis. But we

**[00:31]** using agents on a daily basis. But we

**[00:32]** using agents on a daily basis. But we still notice gaps. We still have slots,

**[00:34]** still notice gaps. We still have slots,

**[00:34]** still notice gaps. We still have slots, right? Agents have intelligence and

**[00:36]** right? Agents have intelligence and

**[00:36]** right? Agents have intelligence and capabilities, but not always expertise

**[00:38]** capabilities, but not always expertise

**[00:38]** capabilities, but not always expertise that we need for real work. I'm Barry.

**[00:41]** that we need for real work. I'm Barry.

**[00:41]** that we need for real work. I'm Barry. This is Mahes. We created agent skills.

**[00:44]** This is Mahes. We created agent skills.

**[00:44]** This is Mahes. We created agent skills. In this talk, we'll show you why we

**[00:46]** In this talk, we'll show you why we

**[00:46]** In this talk, we'll show you why we stopped building agents and started

**[00:48]** stopped building agents and started

**[00:48]** stopped building agents and started building skills instead.

**[00:51]** building skills instead.

**[00:51]** building skills instead. A lot of things have changed since our

**[00:53]** A lot of things have changed since our

**[00:53]** A lot of things have changed since our last talk. MCP became the standard for

**[00:55]** last talk. MCP became the standard for

**[00:55]** last talk. MCP became the standard for agent connectivity. Cloud Code, our

**[00:57]** agent connectivity. Cloud Code, our

**[00:57]** agent connectivity. Cloud Code, our first coding agent, launched to the

**[00:59]** first coding agent, launched to the

**[00:59]** first coding agent, launched to the world and our cloud agent SDK now


### [01:00 - 02:00]

**[01:01]** world and our cloud agent SDK now

**[01:02]** world and our cloud agent SDK now provides a production ready agent out of

**[01:03]** provides a production ready agent out of

**[01:03]** provides a production ready agent out of the box. We have a more mature ecosystem

**[01:06]** the box. We have a more mature ecosystem

**[01:06]** the box. We have a more mature ecosystem and we're moving towards a new paradigm

**[01:08]** and we're moving towards a new paradigm

**[01:08]** and we're moving towards a new paradigm for agents. That paradigm is a tighter

**[01:11]** for agents. That paradigm is a tighter

**[01:11]** for agents. That paradigm is a tighter coupling between the model and a runtime

**[01:13]** coupling between the model and a runtime

**[01:13]** coupling between the model and a runtime environment.

**[01:15]** environment.

**[01:15]** environment. Put simply, we think code is all we

**[01:17]** Put simply, we think code is all we

**[01:18]** Put simply, we think code is all we need.

**[01:20]** need.

**[01:20]** need. We used to think agents in different

**[01:22]** We used to think agents in different

**[01:22]** We used to think agents in different domains will look very different. Each

**[01:23]** domains will look very different. Each

**[01:23]** domains will look very different. Each one will need its own tools and

**[01:25]** one will need its own tools and

**[01:25]** one will need its own tools and scaffolding and that means we'll have a

**[01:27]** scaffolding and that means we'll have a

**[01:27]** scaffolding and that means we'll have a separate agent for each use case for

**[01:29]** separate agent for each use case for

**[01:29]** separate agent for each use case for each domain. Well, customization is

**[01:31]** each domain. Well, customization is

**[01:31]** each domain. Well, customization is still important for each domain. The

**[01:34]** still important for each domain. The

**[01:34]** still important for each domain. The agent underneath is actually more

**[01:35]** agent underneath is actually more

**[01:35]** agent underneath is actually more universal than we thought.

**[01:38]** universal than we thought.

**[01:38]** universal than we thought. What we realized is that code is not

**[01:40]** What we realized is that code is not

**[01:40]** What we realized is that code is not just a use case but the universal

**[01:42]** just a use case but the universal

**[01:42]** just a use case but the universal interface to the digital world.

**[01:44]** interface to the digital world.

**[01:44]** interface to the digital world. After we built cloud code, we realized

**[01:46]** After we built cloud code, we realized

**[01:46]** After we built cloud code, we realized that cloud code is actually a general

**[01:48]** that cloud code is actually a general

**[01:48]** that cloud code is actually a general purpose agent.

**[01:50]** purpose agent.

**[01:50]** purpose agent. Think about generating a financial

**[01:52]** Think about generating a financial

**[01:52]** Think about generating a financial report. The model can call the API to

**[01:54]** report. The model can call the API to

**[01:54]** report. The model can call the API to pull in data and do research. It can

**[01:56]** pull in data and do research. It can

**[01:56]** pull in data and do research. It can organize that data in the file system.

**[01:58]** organize that data in the file system.

**[01:58]** organize that data in the file system. It can analyze it with Python and then


### [02:00 - 03:00]

**[02:00]** It can analyze it with Python and then

**[02:00]** It can analyze it with Python and then synthesize the insight in old file

**[02:02]** synthesize the insight in old file

**[02:02]** synthesize the insight in old file format all through code. The core

**[02:04]** format all through code. The core

**[02:04]** format all through code. The core scaffolding can suddenly become as thin

**[02:06]** scaffolding can suddenly become as thin

**[02:06]** scaffolding can suddenly become as thin as just bash and file system which is

**[02:09]** as just bash and file system which is

**[02:09]** as just bash and file system which is great and really scalable. But we very

**[02:11]** great and really scalable. But we very

**[02:11]** great and really scalable. But we very quickly run into a different problem

**[02:14]** quickly run into a different problem

**[02:14]** quickly run into a different problem and that problem is domain expertise.

**[02:16]** and that problem is domain expertise.

**[02:16]** and that problem is domain expertise. Who do you want doing your taxes? Is it

**[02:18]** Who do you want doing your taxes? Is it

**[02:18]** Who do you want doing your taxes? Is it going to be Mahesh, the 300 IQ

**[02:20]** going to be Mahesh, the 300 IQ

**[02:20]** going to be Mahesh, the 300 IQ mathematical genius, or is it Barry, an

**[02:22]** mathematical genius, or is it Barry, an

**[02:22]** mathematical genius, or is it Barry, an experienced tax professional, right? I

**[02:24]** experienced tax professional, right? I

**[02:24]** experienced tax professional, right? I would pick Barry every time. I don't

**[02:26]** would pick Barry every time. I don't

**[02:26]** would pick Barry every time. I don't want Mahesh to figure out the 2025 tax

**[02:29]** want Mahesh to figure out the 2025 tax

**[02:29]** want Mahesh to figure out the 2025 tax code from first principles. I need

**[02:30]** code from first principles. I need

**[02:30]** code from first principles. I need consistent execution from from a domain

**[02:33]** consistent execution from from a domain

**[02:33]** consistent execution from from a domain expert. As agents today are a lot like

**[02:35]** expert. As agents today are a lot like

**[02:35]** expert. As agents today are a lot like Mahes. They're brilliant, but they lack

**[02:37]** Mahes. They're brilliant, but they lack

**[02:37]** Mahes. They're brilliant, but they lack expertise.

**[02:44]** They can do no more slow. They can do

**[02:44]** They can do no more slow. They can do amazing things when you really put in

**[02:46]** amazing things when you really put in

**[02:46]** amazing things when you really put in the effort and give proper guidance, but

**[02:48]** the effort and give proper guidance, but

**[02:48]** the effort and give proper guidance, but they're often missing the important

**[02:50]** they're often missing the important

**[02:50]** they're often missing the important context up front. They can't really

**[02:51]** context up front. They can't really

**[02:51]** context up front. They can't really absorb your expertise super well, and

**[02:53]** absorb your expertise super well, and

**[02:53]** absorb your expertise super well, and they don't learn over time.

**[02:56]** they don't learn over time.

**[02:56]** they don't learn over time. That's why we created agent skills.


### [03:00 - 04:00]

**[03:00]** That's why we created agent skills.

**[03:00]** That's why we created agent skills. Skills are organized collections of

**[03:02]** Skills are organized collections of

**[03:02]** Skills are organized collections of files that package composable procedural

**[03:04]** files that package composable procedural

**[03:04]** files that package composable procedural knowledge for agents.

**[03:07]** knowledge for agents.

**[03:07]** knowledge for agents. In other words, they're folders. This

**[03:10]** In other words, they're folders. This

**[03:10]** In other words, they're folders. This simplicity is deliberate. We want

**[03:12]** simplicity is deliberate. We want

**[03:12]** simplicity is deliberate. We want something that anyone human or agent can

**[03:14]** something that anyone human or agent can

**[03:14]** something that anyone human or agent can create and use as long as they have a

**[03:16]** create and use as long as they have a

**[03:16]** create and use as long as they have a computer. These also work with what you

**[03:19]** computer. These also work with what you

**[03:19]** computer. These also work with what you already have. You can version them in

**[03:20]** already have. You can version them in

**[03:20]** already have. You can version them in Git, you can throw them in Google Drive

**[03:22]** Git, you can throw them in Google Drive

**[03:22]** Git, you can throw them in Google Drive and you can zip them up and share with

**[03:24]** and you can zip them up and share with

**[03:24]** and you can zip them up and share with your team. We have used files for uh as

**[03:27]** your team. We have used files for uh as

**[03:27]** your team. We have used files for uh as a primitive for decades and we like

**[03:29]** a primitive for decades and we like

**[03:29]** a primitive for decades and we like them. So why change now?

**[03:33]** them. So why change now?

**[03:33]** them. So why change now? Because of that skills can also include

**[03:35]** Because of that skills can also include

**[03:35]** Because of that skills can also include a lot of scripts as tools. Traditional

**[03:37]** a lot of scripts as tools. Traditional

**[03:37]** a lot of scripts as tools. Traditional tools have pretty obvious problems. Some

**[03:39]** tools have pretty obvious problems. Some

**[03:39]** tools have pretty obvious problems. Some tools have poorly written instructions

**[03:41]** tools have poorly written instructions

**[03:41]** tools have poorly written instructions and are pretty ambiguous and when the

**[03:43]** and are pretty ambiguous and when the

**[03:43]** and are pretty ambiguous and when the model is struggling, it can't really

**[03:45]** model is struggling, it can't really

**[03:45]** model is struggling, it can't really make a change to the tool. So, it's just

**[03:46]** make a change to the tool. So, it's just

**[03:46]** make a change to the tool. So, it's just kind of stuck with a code start problem

**[03:49]** kind of stuck with a code start problem

**[03:49]** kind of stuck with a code start problem and they always live in the context

**[03:50]** and they always live in the context

**[03:50]** and they always live in the context window. Code solves some of these

**[03:52]** window. Code solves some of these

**[03:52]** window. Code solves some of these issues. It's self-documenting. It is

**[03:54]** issues. It's self-documenting. It is

**[03:54]** issues. It's self-documenting. It is modifiable and can live in the file

**[03:56]** modifiable and can live in the file

**[03:56]** modifiable and can live in the file system until they're really needed and

**[03:58]** system until they're really needed and

**[03:58]** system until they're really needed and used. Here's an example of a script


### [04:00 - 05:00]

**[04:02]** used. Here's an example of a script

**[04:02]** used. Here's an example of a script inside of a skill. We kept seeing Claude

**[04:04]** inside of a skill. We kept seeing Claude

**[04:04]** inside of a skill. We kept seeing Claude write the same Python script over and

**[04:06]** write the same Python script over and

**[04:06]** write the same Python script over and over again to apply styling to slides.

**[04:08]** over again to apply styling to slides.

**[04:08]** over again to apply styling to slides. So we just ask cloud to save it inside

**[04:10]** So we just ask cloud to save it inside

**[04:10]** So we just ask cloud to save it inside of the skill as a tool for his version

**[04:12]** of the skill as a tool for his version

**[04:12]** of the skill as a tool for his version for his future self. Now we can just run

**[04:15]** for his future self. Now we can just run

**[04:15]** for his future self. Now we can just run the script and that makes everything a

**[04:17]** the script and that makes everything a

**[04:17]** the script and that makes everything a lot more consistent and a lot more

**[04:18]** lot more consistent and a lot more

**[04:18]** lot more consistent and a lot more efficient.

**[04:23]** At this point skills can contain a lot

**[04:23]** At this point skills can contain a lot of information and we want to protect

**[04:25]** of information and we want to protect

**[04:25]** of information and we want to protect the context window so that we can fit in

**[04:27]** the context window so that we can fit in

**[04:27]** the context window so that we can fit in hundreds of skills and make them truly

**[04:29]** hundreds of skills and make them truly

**[04:29]** hundreds of skills and make them truly composable. That's why skills are

**[04:31]** composable. That's why skills are

**[04:31]** composable. That's why skills are progressively disclosed. At runtime,

**[04:34]** progressively disclosed. At runtime,

**[04:34]** progressively disclosed. At runtime, only this metadata is shown to the model

**[04:36]** only this metadata is shown to the model

**[04:36]** only this metadata is shown to the model just to indicate that he has the skill.

**[04:39]** just to indicate that he has the skill.

**[04:39]** just to indicate that he has the skill. When an agent needs to use a skill, it

**[04:41]** When an agent needs to use a skill, it

**[04:41]** When an agent needs to use a skill, it can read in the rest of the skill.md,

**[04:43]** can read in the rest of the skill.md,

**[04:43]** can read in the rest of the skill.md, which contains the core instruction and

**[04:45]** which contains the core instruction and

**[04:45]** which contains the core instruction and directory for the rest of the folder.

**[04:48]** directory for the rest of the folder.

**[04:48]** directory for the rest of the folder. Everything else is just organized for

**[04:51]** Everything else is just organized for

**[04:51]** Everything else is just organized for ease of access. So that's all skills

**[04:54]** ease of access. So that's all skills

**[04:54]** ease of access. So that's all skills are. They're organized folders with

**[04:56]** are. They're organized folders with

**[04:56]** are. They're organized folders with scripts as tools.

**[04:59]** scripts as tools.

**[04:59]** scripts as tools. Since our launch five weeks ago, this


### [05:00 - 06:00]

**[05:01]** Since our launch five weeks ago, this

**[05:02]** Since our launch five weeks ago, this very simple design has translated into a

**[05:04]** very simple design has translated into a

**[05:04]** very simple design has translated into a very quickly growing ecosystem of

**[05:06]** very quickly growing ecosystem of

**[05:06]** very quickly growing ecosystem of thousands of skills. And we've seen this

**[05:08]** thousands of skills. And we've seen this

**[05:08]** thousands of skills. And we've seen this be split across a couple of different

**[05:10]** be split across a couple of different

**[05:10]** be split across a couple of different types of skills. There are foundational

**[05:12]** types of skills. There are foundational

**[05:12]** types of skills. There are foundational skills, third party skills created by

**[05:15]** skills, third party skills created by

**[05:15]** skills, third party skills created by partners in the ecosystem, and skills

**[05:17]** partners in the ecosystem, and skills

**[05:17]** partners in the ecosystem, and skills built within an enterprise and within

**[05:19]** built within an enterprise and within

**[05:19]** built within an enterprise and within teams.

**[05:21]** teams.

**[05:21]** teams. To start, foundational skills are those

**[05:24]** To start, foundational skills are those

**[05:24]** To start, foundational skills are those that give agents new general

**[05:26]** that give agents new general

**[05:26]** that give agents new general capabilities or domain specific

**[05:28]** capabilities or domain specific

**[05:28]** capabilities or domain specific capabilities that it didn't have before.

**[05:31]** capabilities that it didn't have before.

**[05:31]** capabilities that it didn't have before. We ourselves with our launch built

**[05:33]** We ourselves with our launch built

**[05:33]** We ourselves with our launch built document skills that give Claude the

**[05:35]** document skills that give Claude the

**[05:35]** document skills that give Claude the ability to create and edit professional

**[05:37]** ability to create and edit professional

**[05:37]** ability to create and edit professional quality office documents. We're also

**[05:40]** quality office documents. We're also

**[05:40]** quality office documents. We're also really excited to see people like

**[05:42]** really excited to see people like

**[05:42]** really excited to see people like Cadence build scientific research skills

**[05:45]** Cadence build scientific research skills

**[05:45]** Cadence build scientific research skills that give Claude new capabilities like

**[05:47]** that give Claude new capabilities like

**[05:47]** that give Claude new capabilities like EHR data analysis and using common

**[05:50]** EHR data analysis and using common

**[05:50]** EHR data analysis and using common Python bioinformatics libraries better

**[05:52]** Python bioinformatics libraries better

**[05:52]** Python bioinformatics libraries better than it could before.

**[05:57]** We've also seen partners in the

**[05:57]** We've also seen partners in the ecosystem build skills that help Claude

**[05:59]** ecosystem build skills that help Claude

**[05:59]** ecosystem build skills that help Claude better with their own software and their


### [06:00 - 07:00]

**[06:01]** better with their own software and their

**[06:01]** better with their own software and their own products. Browserbase is a pretty

**[06:04]** own products. Browserbase is a pretty

**[06:04]** own products. Browserbase is a pretty good example of this. They built a skill

**[06:06]** good example of this. They built a skill

**[06:06]** good example of this. They built a skill for their open- source browser

**[06:08]** for their open- source browser

**[06:08]** for their open- source browser automation tooling, stage hand. And now

**[06:10]** automation tooling, stage hand. And now

**[06:10]** automation tooling, stage hand. And now Claude equipped that this skill and with

**[06:13]** Claude equipped that this skill and with

**[06:13]** Claude equipped that this skill and with stage hand can now go navigate the web

**[06:16]** stage hand can now go navigate the web

**[06:16]** stage hand can now go navigate the web and use a browser more effectively to

**[06:17]** and use a browser more effectively to

**[06:18]** and use a browser more effectively to get work done.

**[06:19]** get work done.

**[06:19]** get work done. And notion launched a bunch of skills

**[06:21]** And notion launched a bunch of skills

**[06:21]** And notion launched a bunch of skills that help claude better understand your

**[06:23]** that help claude better understand your

**[06:23]** that help claude better understand your notion workspace and do deep research

**[06:26]** notion workspace and do deep research

**[06:26]** notion workspace and do deep research over your entire workspace.

**[06:31]** And I think where I've seen the most

**[06:31]** And I think where I've seen the most excitement and traction with skills is

**[06:33]** excitement and traction with skills is

**[06:33]** excitement and traction with skills is within large enterprises. These are

**[06:36]** within large enterprises. These are

**[06:36]** within large enterprises. These are company and team specific skills built

**[06:38]** company and team specific skills built

**[06:38]** company and team specific skills built for an organization.

**[06:41]** for an organization.

**[06:41]** for an organization. We've been talking to Fortune 100s that

**[06:43]** We've been talking to Fortune 100s that

**[06:43]** We've been talking to Fortune 100s that are using skills as a way to teach

**[06:45]** are using skills as a way to teach

**[06:45]** are using skills as a way to teach agents about their organizational best

**[06:47]** agents about their organizational best

**[06:47]** agents about their organizational best practices and the weird and unique ways

**[06:49]** practices and the weird and unique ways

**[06:49]** practices and the weird and unique ways that they use this bespoke internal

**[06:51]** that they use this bespoke internal

**[06:51]** that they use this bespoke internal software.

**[06:53]** software.

**[06:53]** software. We're also talking to really large

**[06:55]** We're also talking to really large

**[06:55]** We're also talking to really large developer productivity teams. These are

**[06:57]** developer productivity teams. These are

**[06:57]** developer productivity teams. These are teams serving thousands or even tens of

**[06:59]** teams serving thousands or even tens of

**[06:59]** teams serving thousands or even tens of thousands of developers in an


### [07:00 - 08:00]

**[07:01]** thousands of developers in an

**[07:01]** thousands of developers in an organization that are using skills as a

**[07:03]** organization that are using skills as a

**[07:03]** organization that are using skills as a way to deploy agents like cloud code and

**[07:05]** way to deploy agents like cloud code and

**[07:06]** way to deploy agents like cloud code and teach them about code style best

**[07:07]** teach them about code style best

**[07:07]** teach them about code style best practices and other ways that they want

**[07:09]** practices and other ways that they want

**[07:09]** practices and other ways that they want their developers to work internally.

**[07:12]** their developers to work internally.

**[07:12]** their developers to work internally. So all of these different types of

**[07:13]** So all of these different types of

**[07:13]** So all of these different types of skills are created and consumed by

**[07:15]** skills are created and consumed by

**[07:15]** skills are created and consumed by different people inside of an

**[07:17]** different people inside of an

**[07:17]** different people inside of an organization or in the world. But what

**[07:19]** organization or in the world. But what

**[07:19]** organization or in the world. But what they have in common is anyone can create

**[07:21]** they have in common is anyone can create

**[07:21]** they have in common is anyone can create them and they give agents the new

**[07:23]** them and they give agents the new

**[07:23]** them and they give agents the new capabilities that they didn't have

**[07:25]** capabilities that they didn't have

**[07:25]** capabilities that they didn't have before.

**[07:30]** So, as this ecosystem has grown, we've

**[07:30]** So, as this ecosystem has grown, we've started to observe a couple of

**[07:32]** started to observe a couple of

**[07:32]** started to observe a couple of interesting trends. First, skills are

**[07:34]** interesting trends. First, skills are

**[07:34]** interesting trends. First, skills are starting to get more complex. The most

**[07:37]** starting to get more complex. The most

**[07:37]** starting to get more complex. The most basic skill today can still be a

**[07:39]** basic skill today can still be a

**[07:39]** basic skill today can still be a skill.md markdown file with some prompts

**[07:42]** skill.md markdown file with some prompts

**[07:42]** skill.md markdown file with some prompts and some really basic instructions, but

**[07:44]** and some really basic instructions, but

**[07:44]** and some really basic instructions, but we're starting to see skills that

**[07:45]** we're starting to see skills that

**[07:45]** we're starting to see skills that package software, executables, binaries,

**[07:49]** package software, executables, binaries,

**[07:49]** package software, executables, binaries, files, code, scripts, assets, and a lot

**[07:51]** files, code, scripts, assets, and a lot

**[07:51]** files, code, scripts, assets, and a lot more. And a lot of the skills that are

**[07:53]** more. And a lot of the skills that are

**[07:53]** more. And a lot of the skills that are being built today might take minutes or

**[07:55]** being built today might take minutes or

**[07:55]** being built today might take minutes or hours to build and put into an agent.

**[07:58]** hours to build and put into an agent.

**[07:58]** hours to build and put into an agent. But we think that increasingly much like


### [08:00 - 09:00]

**[08:00]** But we think that increasingly much like

**[08:00]** But we think that increasingly much like a lot of the software we use today,

**[08:02]** a lot of the software we use today,

**[08:02]** a lot of the software we use today, these skills might take weeks or months

**[08:03]** these skills might take weeks or months

**[08:04]** these skills might take weeks or months to build and be maintained.

**[08:10]** We're also seeing that this ecosystem of

**[08:10]** We're also seeing that this ecosystem of skills is complementing the existing

**[08:12]** skills is complementing the existing

**[08:12]** skills is complementing the existing ecosystem of MCP servers that was built

**[08:14]** ecosystem of MCP servers that was built

**[08:14]** ecosystem of MCP servers that was built up over the course of this year.

**[08:16]** up over the course of this year.

**[08:16]** up over the course of this year. Developers are using and building skills

**[08:19]** Developers are using and building skills

**[08:19]** Developers are using and building skills that orchestrate workflows of multiple

**[08:21]** that orchestrate workflows of multiple

**[08:21]** that orchestrate workflows of multiple MCP tools stitched together to do more

**[08:24]** MCP tools stitched together to do more

**[08:24]** MCP tools stitched together to do more complex things with external data and

**[08:26]** complex things with external data and

**[08:26]** complex things with external data and connectivity. And in these cases, MCP

**[08:29]** connectivity. And in these cases, MCP

**[08:29]** connectivity. And in these cases, MCP MCP is providing the connection to the

**[08:31]** MCP is providing the connection to the

**[08:31]** MCP is providing the connection to the outside world while skills are providing

**[08:33]** outside world while skills are providing

**[08:33]** outside world while skills are providing the expertise.

**[08:38]** And finally, and I think most excitingly

**[08:38]** And finally, and I think most excitingly for me personally, is we're seeing

**[08:40]** for me personally, is we're seeing

**[08:40]** for me personally, is we're seeing skills that are being built by people

**[08:42]** skills that are being built by people

**[08:42]** skills that are being built by people that aren't technical. These are people

**[08:44]** that aren't technical. These are people

**[08:44]** that aren't technical. These are people in functions like finance, recruiting,

**[08:46]** in functions like finance, recruiting,

**[08:46]** in functions like finance, recruiting, accounting, legal, and a lot more. Um,

**[08:49]** accounting, legal, and a lot more. Um,

**[08:50]** accounting, legal, and a lot more. Um, and I think this is pretty early

**[08:51]** and I think this is pretty early

**[08:51]** and I think this is pretty early validation of our initial idea that

**[08:54]** validation of our initial idea that

**[08:54]** validation of our initial idea that skills help people that aren't doing

**[08:56]** skills help people that aren't doing

**[08:56]** skills help people that aren't doing coding work extend these general agents

**[08:59]** coding work extend these general agents

**[08:59]** coding work extend these general agents and they make these agents more


### [09:00 - 10:00]

**[09:00]** and they make these agents more

**[09:00]** and they make these agents more accessible for the day-to-day of what

**[09:02]** accessible for the day-to-day of what

**[09:02]** accessible for the day-to-day of what these people are working on.

**[09:08]** So tying this all together, let's talk

**[09:08]** So tying this all together, let's talk about how these all fit into this

**[09:10]** about how these all fit into this

**[09:10]** about how these all fit into this emerging architecture of general agents.

**[09:13]** emerging architecture of general agents.

**[09:13]** emerging architecture of general agents. First, we think this architecture is

**[09:15]** First, we think this architecture is

**[09:15]** First, we think this architecture is converging on a couple of things. The

**[09:17]** converging on a couple of things. The

**[09:17]** converging on a couple of things. The first is this agent loop that helps

**[09:19]** first is this agent loop that helps

**[09:20]** first is this agent loop that helps manage the the model's internal context

**[09:22]** manage the the model's internal context

**[09:22]** manage the the model's internal context and manages what tokens are going in and

**[09:24]** and manages what tokens are going in and

**[09:24]** and manages what tokens are going in and out. And this is coupled with a runtime

**[09:26]** out. And this is coupled with a runtime

**[09:26]** out. And this is coupled with a runtime environment that provides the agent with

**[09:28]** environment that provides the agent with

**[09:28]** environment that provides the agent with a file system and the ability to read

**[09:31]** a file system and the ability to read

**[09:31]** a file system and the ability to read and write code.

**[09:34]** and write code.

**[09:34]** and write code. This agent, as many of us have done

**[09:36]** This agent, as many of us have done

**[09:36]** This agent, as many of us have done throughout this year, can be connected

**[09:37]** throughout this year, can be connected

**[09:37]** throughout this year, can be connected to MCP servers. And these are tools and

**[09:40]** to MCP servers. And these are tools and

**[09:40]** to MCP servers. And these are tools and data from the outside world that make

**[09:42]** data from the outside world that make

**[09:42]** data from the outside world that make the the agent more relevant and more

**[09:44]** the the agent more relevant and more

**[09:44]** the the agent more relevant and more effective.

**[09:46]** effective.

**[09:46]** effective. And now we can give the same agent a

**[09:48]** And now we can give the same agent a

**[09:48]** And now we can give the same agent a library of hundreds or thousands of

**[09:51]** library of hundreds or thousands of

**[09:51]** library of hundreds or thousands of skills that it can decide to pull into

**[09:53]** skills that it can decide to pull into

**[09:53]** skills that it can decide to pull into context only at runtime when it's

**[09:55]** context only at runtime when it's

**[09:55]** context only at runtime when it's deciding to work on a particular task.

**[09:58]** deciding to work on a particular task.

**[09:58]** deciding to work on a particular task. Today, giving an agent a new capability


### [10:00 - 11:00]

**[10:01]** Today, giving an agent a new capability

**[10:01]** Today, giving an agent a new capability in a new domain might just involve

**[10:03]** in a new domain might just involve

**[10:03]** in a new domain might just involve equipping it with the right set of MCP

**[10:05]** equipping it with the right set of MCP

**[10:05]** equipping it with the right set of MCP servers and the right library of skills.

**[10:09]** servers and the right library of skills.

**[10:09]** servers and the right library of skills. And this emerging pattern of an agent

**[10:12]** And this emerging pattern of an agent

**[10:12]** And this emerging pattern of an agent with an MCP server and a set of skills

**[10:14]** with an MCP server and a set of skills

**[10:14]** with an MCP server and a set of skills is something that's already helping us

**[10:16]** is something that's already helping us

**[10:16]** is something that's already helping us at Enthropic deploy Claude to new

**[10:17]** at Enthropic deploy Claude to new

**[10:17]** at Enthropic deploy Claude to new verticals. Just after we launched skills

**[10:20]** verticals. Just after we launched skills

**[10:20]** verticals. Just after we launched skills 5 weeks ago, we immediately launched new

**[10:22]** 5 weeks ago, we immediately launched new

**[10:22]** 5 weeks ago, we immediately launched new offerings in financial services and life

**[10:25]** offerings in financial services and life

**[10:25]** offerings in financial services and life sciences. And each of these came with a

**[10:27]** sciences. And each of these came with a

**[10:27]** sciences. And each of these came with a set of MCP servers and a set of skills

**[10:29]** set of MCP servers and a set of skills

**[10:29]** set of MCP servers and a set of skills that immediately make Claude more

**[10:31]** that immediately make Claude more

**[10:31]** that immediately make Claude more effective for professionals in each of

**[10:33]** effective for professionals in each of

**[10:33]** effective for professionals in each of these domains.

**[10:38]** We're also starting to think about some

**[10:38]** We're also starting to think about some of the other open questions and areas

**[10:40]** of the other open questions and areas

**[10:40]** of the other open questions and areas that we want to focus on for how skills

**[10:42]** that we want to focus on for how skills

**[10:42]** that we want to focus on for how skills evolve in the future as they start to

**[10:45]** evolve in the future as they start to

**[10:45]** evolve in the future as they start to become more complex. We really want to

**[10:47]** become more complex. We really want to

**[10:47]** become more complex. We really want to support developers, enterprises, and

**[10:49]** support developers, enterprises, and

**[10:49]** support developers, enterprises, and other skill builders by starting to

**[10:51]** other skill builders by starting to

**[10:52]** other skill builders by starting to treat skills like we treat software.

**[10:54]** treat skills like we treat software.

**[10:54]** treat skills like we treat software. This means exploring testing and

**[10:56]** This means exploring testing and

**[10:56]** This means exploring testing and evaluation, better tooling to make sure

**[10:59]** evaluation, better tooling to make sure

**[10:59]** evaluation, better tooling to make sure that these agents are loading and


### [11:00 - 12:00]

**[11:01]** that these agents are loading and

**[11:01]** that these agents are loading and triggering skills at the right time and

**[11:03]** triggering skills at the right time and

**[11:03]** triggering skills at the right time and for the right task, and tooling to help

**[11:06]** for the right task, and tooling to help

**[11:06]** for the right task, and tooling to help measure the output quality of an agent

**[11:08]** measure the output quality of an agent

**[11:08]** measure the output quality of an agent equipped with the skill to make sure

**[11:10]** equipped with the skill to make sure

**[11:10]** equipped with the skill to make sure that's on par with what the agent is

**[11:12]** that's on par with what the agent is

**[11:12]** that's on par with what the agent is supposed to be doing.

**[11:14]** supposed to be doing.

**[11:14]** supposed to be doing. We'd also like to focus on versioning.

**[11:16]** We'd also like to focus on versioning.

**[11:16]** We'd also like to focus on versioning. as a skill evolves and the resulting

**[11:18]** as a skill evolves and the resulting

**[11:18]** as a skill evolves and the resulting agent behavior uh evolves, we want this

**[11:21]** agent behavior uh evolves, we want this

**[11:21]** agent behavior uh evolves, we want this to be uh clearly tracked and to have a

**[11:23]** to be uh clearly tracked and to have a

**[11:23]** to be uh clearly tracked and to have a clear lineage over time.

**[11:26]** clear lineage over time.

**[11:26]** clear lineage over time. And finally, we'd also like to explore

**[11:28]** And finally, we'd also like to explore

**[11:28]** And finally, we'd also like to explore skills that can explicitly depend on and

**[11:30]** skills that can explicitly depend on and

**[11:30]** skills that can explicitly depend on and refer to either other skills, MCP

**[11:33]** refer to either other skills, MCP

**[11:33]** refer to either other skills, MCP servers, and dependencies and packages

**[11:35]** servers, and dependencies and packages

**[11:35]** servers, and dependencies and packages within the agents environment. We think

**[11:37]** within the agents environment. We think

**[11:37]** within the agents environment. We think that this is going to make agents a lot

**[11:39]** that this is going to make agents a lot

**[11:39]** that this is going to make agents a lot more predictable in different runtime

**[11:41]** more predictable in different runtime

**[11:41]** more predictable in different runtime environments. and the composability of

**[11:43]** environments. and the composability of

**[11:43]** environments. and the composability of multiple skills together will help

**[11:45]** multiple skills together will help

**[11:45]** multiple skills together will help agents like Claude elicit even more

**[11:47]** agents like Claude elicit even more

**[11:47]** agents like Claude elicit even more complex and relevant behavior from these

**[11:49]** complex and relevant behavior from these

**[11:49]** complex and relevant behavior from these agents.

**[11:51]** agents.

**[11:51]** agents. Overall, these set of things should

**[11:53]** Overall, these set of things should

**[11:53]** Overall, these set of things should hopefully make skills easier to build

**[11:55]** hopefully make skills easier to build

**[11:55]** hopefully make skills easier to build and easier to integrate into agent

**[11:56]** and easier to integrate into agent

**[11:56]** and easier to integrate into agent products, even those besides claude.


### [12:00 - 13:00]

**[12:04]** Finally, a huge part of the value of

**[12:04]** Finally, a huge part of the value of skills we think is going to come from

**[12:06]** skills we think is going to come from

**[12:06]** skills we think is going to come from sharing and distribution. Barry and I

**[12:09]** sharing and distribution. Barry and I

**[12:09]** sharing and distribution. Barry and I think a lot about the future of

**[12:11]** think a lot about the future of

**[12:11]** think a lot about the future of companies that are deploying these

**[12:12]** companies that are deploying these

**[12:12]** companies that are deploying these agents at scale. And the vision that

**[12:15]** agents at scale. And the vision that

**[12:15]** agents at scale. And the vision that excites us most is one of a collecting

**[12:18]** excites us most is one of a collecting

**[12:18]** excites us most is one of a collecting and collective and evolving knowledge

**[12:20]** and collective and evolving knowledge

**[12:20]** and collective and evolving knowledge base of capabilities that's curated by

**[12:23]** base of capabilities that's curated by

**[12:23]** base of capabilities that's curated by people and agents inside of an

**[12:25]** people and agents inside of an

**[12:25]** people and agents inside of an organization. We think skills are a big

**[12:28]** organization. We think skills are a big

**[12:28]** organization. We think skills are a big step towards this vision. They provide

**[12:30]** step towards this vision. They provide

**[12:30]** step towards this vision. They provide the procedural knowledge for your agents

**[12:32]** the procedural knowledge for your agents

**[12:32]** the procedural knowledge for your agents to do useful things. And as you interact

**[12:35]** to do useful things. And as you interact

**[12:35]** to do useful things. And as you interact with an agent and give it feedback and

**[12:38]** with an agent and give it feedback and

**[12:38]** with an agent and give it feedback and more institutional knowledge, it starts

**[12:40]** more institutional knowledge, it starts

**[12:40]** more institutional knowledge, it starts to get better and all of the agents

**[12:42]** to get better and all of the agents

**[12:42]** to get better and all of the agents inside your team and your org get better

**[12:44]** inside your team and your org get better

**[12:44]** inside your team and your org get better as well. And when someone joins your

**[12:47]** as well. And when someone joins your

**[12:47]** as well. And when someone joins your team and starts using Claude for the

**[12:48]** team and starts using Claude for the

**[12:48]** team and starts using Claude for the first time, it already knows what your

**[12:50]** first time, it already knows what your

**[12:50]** first time, it already knows what your team cares about. It knows about your

**[12:52]** team cares about. It knows about your

**[12:52]** team cares about. It knows about your day-to-day and it knows about how to be

**[12:54]** day-to-day and it knows about how to be

**[12:54]** day-to-day and it knows about how to be most effective for the work that you're

**[12:55]** most effective for the work that you're

**[12:55]** most effective for the work that you're doing.

**[12:56]** doing.

**[12:56]** doing. And as this grows and this ecosystem

**[12:58]** And as this grows and this ecosystem

**[12:58]** And as this grows and this ecosystem starts to develop even more, this was


### [13:00 - 14:00]

**[13:00]** starts to develop even more, this was

**[13:00]** starts to develop even more, this was going to this compounding value is going

**[13:02]** going to this compounding value is going

**[13:02]** going to this compounding value is going to extend outside of just your organ

**[13:04]** to extend outside of just your organ

**[13:04]** to extend outside of just your organ into the broader community. So just like

**[13:06]** into the broader community. So just like

**[13:06]** into the broader community. So just like when someone else across the world

**[13:08]** when someone else across the world

**[13:08]** when someone else across the world builds an MCP server that makes your

**[13:09]** builds an MCP server that makes your

**[13:09]** builds an MCP server that makes your agent more useful, a skill built by

**[13:11]** agent more useful, a skill built by

**[13:11]** agent more useful, a skill built by someone else in the community will help

**[13:13]** someone else in the community will help

**[13:13]** someone else in the community will help make your own agents more capable,

**[13:15]** make your own agents more capable,

**[13:15]** make your own agents more capable, reliable, and useful as well.

**[13:20]** reliable, and useful as well.

**[13:20]** reliable, and useful as well. This vision of a evolving knowledge base

**[13:22]** This vision of a evolving knowledge base

**[13:22]** This vision of a evolving knowledge base gets even more powerful when claw starts

**[13:24]** gets even more powerful when claw starts

**[13:24]** gets even more powerful when claw starts to create these skills. We design skills

**[13:27]** to create these skills. We design skills

**[13:27]** to create these skills. We design skills specifically as a concrete steps towards

**[13:29]** specifically as a concrete steps towards

**[13:29]** specifically as a concrete steps towards uh continuous learning.

**[13:31]** uh continuous learning.

**[13:31]** uh continuous learning. When you first start using cloud, this

**[13:33]** When you first start using cloud, this

**[13:33]** When you first start using cloud, this standardized format gives a very

**[13:35]** standardized format gives a very

**[13:35]** standardized format gives a very important guarantee. Anything that cloud

**[13:37]** important guarantee. Anything that cloud

**[13:37]** important guarantee. Anything that cloud writes down can be used efficiently by a

**[13:39]** writes down can be used efficiently by a

**[13:39]** writes down can be used efficiently by a future version of itself. This makes the

**[13:42]** future version of itself. This makes the

**[13:42]** future version of itself. This makes the learning actually transferable.

**[13:44]** learning actually transferable.

**[13:44]** learning actually transferable. As you build up the context skills makes

**[13:46]** As you build up the context skills makes

**[13:46]** As you build up the context skills makes the concept of memory more tangible.

**[13:49]** the concept of memory more tangible.

**[13:49]** the concept of memory more tangible. They don't capture everything. They

**[13:51]** They don't capture everything. They

**[13:51]** They don't capture everything. They don't capture every type of information.

**[13:52]** don't capture every type of information.

**[13:52]** don't capture every type of information. Just procedural knowledge that cloud can

**[13:54]** Just procedural knowledge that cloud can

**[13:54]** Just procedural knowledge that cloud can use on specific tasks.

**[13:57]** use on specific tasks.

**[13:57]** use on specific tasks. When you have worked with cloud for

**[13:59]** When you have worked with cloud for

**[13:59]** When you have worked with cloud for quite a while, the flexibility of skills


### [14:00 - 15:00]

**[14:01]** quite a while, the flexibility of skills

**[14:01]** quite a while, the flexibility of skills matters even more. Cloud can acquire new

**[14:04]** matters even more. Cloud can acquire new

**[14:04]** matters even more. Cloud can acquire new capabilities instantly, evolve them as

**[14:06]** capabilities instantly, evolve them as

**[14:06]** capabilities instantly, evolve them as needed, and then drop the ones that

**[14:08]** needed, and then drop the ones that

**[14:08]** needed, and then drop the ones that become obsolete. This is what we have

**[14:10]** become obsolete. This is what we have

**[14:10]** become obsolete. This is what we have always known. The power of in in context

**[14:12]** always known. The power of in in context

**[14:12]** always known. The power of in in context learning makes this a lot more cost-

**[14:14]** learning makes this a lot more cost-

**[14:14]** learning makes this a lot more cost- effective for information that change on

**[14:16]** effective for information that change on

**[14:16]** effective for information that change on daily basis.

**[14:18]** daily basis.

**[14:18]** daily basis. Our goal is that claude on day 30 of

**[14:20]** Our goal is that claude on day 30 of

**[14:20]** Our goal is that claude on day 30 of working with you is going to be a lot

**[14:22]** working with you is going to be a lot

**[14:22]** working with you is going to be a lot better on cloud on day one. CL can

**[14:24]** better on cloud on day one. CL can

**[14:24]** better on cloud on day one. CL can already create skills for you today

**[14:26]** already create skills for you today

**[14:26]** already create skills for you today using our skill creator skill and we're

**[14:28]** using our skill creator skill and we're

**[14:28]** using our skill creator skill and we're going to continue pushing in that

**[14:29]** going to continue pushing in that

**[14:29]** going to continue pushing in that direction.

**[14:35]** We're going to conclude by comparing the

**[14:35]** We're going to conclude by comparing the agent stack to what we have already seen

**[14:37]** agent stack to what we have already seen

**[14:37]** agent stack to what we have already seen computing.

**[14:38]** computing.

**[14:38]** computing. In a rough analogy, models are like

**[14:41]** In a rough analogy, models are like

**[14:41]** In a rough analogy, models are like processors. Both require massive

**[14:44]** processors. Both require massive

**[14:44]** processors. Both require massive investment and contain immense

**[14:46]** investment and contain immense

**[14:46]** investment and contain immense potential, but only so useful by

**[14:48]** potential, but only so useful by

**[14:48]** potential, but only so useful by themselves.

**[14:50]** themselves.

**[14:50]** themselves. Then we start building operating system.

**[14:52]** Then we start building operating system.

**[14:52]** Then we start building operating system. The OS made processors far more valuable

**[14:54]** The OS made processors far more valuable

**[14:54]** The OS made processors far more valuable by orchestrating the processes,

**[14:56]** by orchestrating the processes,

**[14:56]** by orchestrating the processes, resources, and data around the

**[14:58]** resources, and data around the

**[14:58]** resources, and data around the processor. In AI, we believe that agent


### [15:00 - 16:00]

**[15:00]** processor. In AI, we believe that agent

**[15:00]** processor. In AI, we believe that agent runtime is starting to play this role.

**[15:02]** runtime is starting to play this role.

**[15:02]** runtime is starting to play this role. We're all trying to build the cleanest,

**[15:04]** We're all trying to build the cleanest,

**[15:04]** We're all trying to build the cleanest, most efficient, and most scalable uh

**[15:06]** most efficient, and most scalable uh

**[15:06]** most efficient, and most scalable uh abstractions to get the right tokens in

**[15:09]** abstractions to get the right tokens in

**[15:09]** abstractions to get the right tokens in and out of the model.

**[15:11]** and out of the model.

**[15:11]** and out of the model. But once we have a platform, the real

**[15:13]** But once we have a platform, the real

**[15:13]** But once we have a platform, the real value comes from applications. A few

**[15:16]** value comes from applications. A few

**[15:16]** value comes from applications. A few companies build uh processors and

**[15:18]** companies build uh processors and

**[15:18]** companies build uh processors and operating systems, but millions of

**[15:20]** operating systems, but millions of

**[15:20]** operating systems, but millions of developers like us have built software

**[15:23]** developers like us have built software

**[15:23]** developers like us have built software that encoded domain expertise and our

**[15:25]** that encoded domain expertise and our

**[15:25]** that encoded domain expertise and our unique points of view. We hope that

**[15:27]** unique points of view. We hope that

**[15:27]** unique points of view. We hope that skills can help us open up this layer

**[15:29]** skills can help us open up this layer

**[15:30]** skills can help us open up this layer for everyone. This is where we get

**[15:32]** for everyone. This is where we get

**[15:32]** for everyone. This is where we get creative and solve concrete problem for

**[15:34]** creative and solve concrete problem for

**[15:34]** creative and solve concrete problem for ourselves, for each other, and for the

**[15:35]** ourselves, for each other, and for the

**[15:35]** ourselves, for each other, and for the world just by putting stuff in the

**[15:37]** world just by putting stuff in the

**[15:37]** world just by putting stuff in the folder. So skills are just the starting

**[15:39]** folder. So skills are just the starting

**[15:39]** folder. So skills are just the starting point.

**[15:42]** point.

**[15:42]** point. To close out, we think we're now

**[15:44]** To close out, we think we're now

**[15:44]** To close out, we think we're now converging on this general architecture

**[15:46]** converging on this general architecture

**[15:46]** converging on this general architecture for general agents. We've created skills

**[15:48]** for general agents. We've created skills

**[15:48]** for general agents. We've created skills as a new paradigm for shipping and

**[15:51]** as a new paradigm for shipping and

**[15:51]** as a new paradigm for shipping and sharing new capabilities. So we think

**[15:53]** sharing new capabilities. So we think

**[15:53]** sharing new capabilities. So we think it's time to stop rebuilding agents and

**[15:55]** it's time to stop rebuilding agents and

**[15:55]** it's time to stop rebuilding agents and start building skills instead. And if

**[15:57]** start building skills instead. And if

**[15:57]** start building skills instead. And if you're excited about this, come work

**[15:59]** you're excited about this, come work

**[15:59]** you're excited about this, come work with us and start building some skills


### [16:00 - 17:00]

**[16:01]** with us and start building some skills

**[16:01]** with us and start building some skills today. Thank you.


