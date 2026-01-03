# A2A & MCP Workshop- Automating Business Processes with LLMs — Damien Murphy, Bench

**Video URL:** https://www.youtube.com/watch?v=wXVvfFMTyzY

---

## Full Transcript

### [00:00 - 01:00]

**[00:17]** Hey everybody. Uh yeah, thanks for

**[00:17]** Hey everybody. Uh yeah, thanks for coming. Uh great to see a full room. Uh

**[00:19]** coming. Uh great to see a full room. Uh

**[00:19]** coming. Uh great to see a full room. Uh always good when you're doing a workshop

**[00:20]** always good when you're doing a workshop

**[00:20]** always good when you're doing a workshop to have a a lot of people here. Um so

**[00:23]** to have a a lot of people here. Um so

**[00:23]** to have a a lot of people here. Um so yeah, I'm I'm Damian Murphy. I'm going

**[00:25]** yeah, I'm I'm Damian Murphy. I'm going

**[00:25]** yeah, I'm I'm Damian Murphy. I'm going to be presenting A2A and MCP. uh two

**[00:29]** to be presenting A2A and MCP. uh two

**[00:29]** to be presenting A2A and MCP. uh two pretty hot topics these days in AI um

**[00:31]** pretty hot topics these days in AI um

**[00:31]** pretty hot topics these days in AI um and how you can use them to automate

**[00:33]** and how you can use them to automate

**[00:33]** and how you can use them to automate business processes. Um

**[00:36]** business processes. Um

**[00:36]** business processes. Um so yeah a little bit about me um about

**[00:40]** so yeah a little bit about me um about

**[00:40]** so yeah a little bit about me um about 15 years full-time uh full stack

**[00:42]** 15 years full-time uh full stack

**[00:42]** 15 years full-time uh full stack developer uh five years doing solutions

**[00:45]** developer uh five years doing solutions

**[00:45]** developer uh five years doing solutions engineering so customerf facing kind of

**[00:47]** engineering so customerf facing kind of

**[00:48]** engineering so customerf facing kind of uh forward deployed engineer and uh

**[00:50]** uh forward deployed engineer and uh

**[00:50]** uh forward deployed engineer and uh spent the last three years or so uh

**[00:52]** spent the last three years or so uh

**[00:52]** spent the last three years or so uh working on voice AI and AI agents. Um I

**[00:56]** working on voice AI and AI agents. Um I

**[00:56]** working on voice AI and AI agents. Um I did a workshop last year as well um AI

**[00:59]** did a workshop last year as well um AI

**[00:59]** did a workshop last year as well um AI voice agent swarms and uh yeah pretty


### [01:00 - 02:00]

**[01:02]** voice agent swarms and uh yeah pretty

**[01:02]** voice agent swarms and uh yeah pretty pretty hot topic. I think it's now

**[01:04]** pretty hot topic. I think it's now

**[01:04]** pretty hot topic. I think it's now pretty much standard that everybody can

**[01:05]** pretty much standard that everybody can

**[01:05]** pretty much standard that everybody can build a voice agent in in 5 minutes. Um

**[01:09]** build a voice agent in in 5 minutes. Um

**[01:09]** build a voice agent in in 5 minutes. Um so now the the hard part becomes

**[01:11]** so now the the hard part becomes

**[01:11]** so now the the hard part becomes building autonomous agents that actually

**[01:13]** building autonomous agents that actually

**[01:13]** building autonomous agents that actually can do complex tasks. Um, so I joined

**[01:16]** can do complex tasks. Um, so I joined

**[01:16]** can do complex tasks. Um, so I joined Bench Computing uh about two months ago

**[01:18]** Bench Computing uh about two months ago

**[01:18]** Bench Computing uh about two months ago uh pre-revenue startup u backed by

**[01:21]** uh pre-revenue startup u backed by

**[01:21]** uh pre-revenue startup u backed by Sutter Hill Ventures and we're building

**[01:24]** Sutter Hill Ventures and we're building

**[01:24]** Sutter Hill Ventures and we're building um what I would imagine to be a better

**[01:26]** um what I would imagine to be a better

**[01:26]** um what I would imagine to be a better Manis uh that's more focused on teams

**[01:28]** Manis uh that's more focused on teams

**[01:28]** Manis uh that's more focused on teams and enterprises.

**[01:30]** and enterprises.

**[01:30]** and enterprises. If you're not familiar with what Manis

**[01:32]** If you're not familiar with what Manis

**[01:32]** If you're not familiar with what Manis is, it's kind of like a autonomous AI

**[01:34]** is, it's kind of like a autonomous AI

**[01:34]** is, it's kind of like a autonomous AI agent. And Bench is essentially an

**[01:37]** agent. And Bench is essentially an

**[01:37]** agent. And Bench is essentially an autonomous AI agent that can do uh sub

**[01:40]** autonomous AI agent that can do uh sub

**[01:40]** autonomous AI agent that can do uh sub subp parallel task um automation.

**[01:46]** subp parallel task um automation.

**[01:46]** subp parallel task um automation. All right. So the workshop that we're

**[01:47]** All right. So the workshop that we're

**[01:47]** All right. So the workshop that we're doing today, we're going to build a

**[01:48]** doing today, we're going to build a

**[01:48]** doing today, we're going to build a multi- aent system um using A2A agents.

**[01:52]** multi- aent system um using A2A agents.

**[01:52]** multi- aent system um using A2A agents. Uh if you're not familiar with A2A, uh

**[01:54]** Uh if you're not familiar with A2A, uh

**[01:54]** Uh if you're not familiar with A2A, uh Google released essentially um a

**[01:57]** Google released essentially um a

**[01:57]** Google released essentially um a protocol that allows agents to

**[01:59]** protocol that allows agents to

**[01:59]** protocol that allows agents to communicate over the web.


### [02:00 - 03:00]

**[02:02]** communicate over the web.

**[02:02]** communicate over the web. Uh we're going to integrate these agents

**[02:04]** Uh we're going to integrate these agents

**[02:04]** Uh we're going to integrate these agents with uh MCP, which is the model context

**[02:07]** with uh MCP, which is the model context

**[02:07]** with uh MCP, which is the model context protocol. Uh MCP is like a USBC for, you

**[02:12]** protocol. Uh MCP is like a USBC for, you

**[02:12]** protocol. Uh MCP is like a USBC for, you know, uh all of your agents to be able

**[02:15]** know, uh all of your agents to be able

**[02:15]** know, uh all of your agents to be able to consume um context and tools uh and

**[02:19]** to consume um context and tools uh and

**[02:19]** to consume um context and tools uh and resources uh very easily.

**[02:22]** resources uh very easily.

**[02:22]** resources uh very easily. uh we're going to get these agents to

**[02:24]** uh we're going to get these agents to

**[02:24]** uh we're going to get these agents to work together and we're going to trigger

**[02:26]** work together and we're going to trigger

**[02:26]** work together and we're going to trigger uh the the agent with a web hook and

**[02:29]** uh the the agent with a web hook and

**[02:30]** uh the the agent with a web hook and then uh I'm going to cover a little bit

**[02:31]** then uh I'm going to cover a little bit

**[02:31]** then uh I'm going to cover a little bit about when to use A2A MCP and I'll also

**[02:35]** about when to use A2A MCP and I'll also

**[02:35]** about when to use A2A MCP and I'll also go into uh prompt caching and context

**[02:37]** go into uh prompt caching and context

**[02:37]** go into uh prompt caching and context management as well.

**[02:45]** All right, so A2A, right? Um it's it's

**[02:45]** All right, so A2A, right? Um it's it's not exactly clear what it's for and why

**[02:47]** not exactly clear what it's for and why

**[02:47]** not exactly clear what it's for and why it exists, right? Uh if you ask

**[02:49]** it exists, right? Uh if you ask

**[02:49]** it exists, right? Uh if you ask everybody in the room what they think it

**[02:51]** everybody in the room what they think it

**[02:51]** everybody in the room what they think it does or why it exists, you'll probably

**[02:53]** does or why it exists, you'll probably

**[02:53]** does or why it exists, you'll probably get a different answer. Um but the key

**[02:55]** get a different answer. Um but the key

**[02:55]** get a different answer. Um but the key benefits are you can have agent

**[02:57]** benefits are you can have agent

**[02:57]** benefits are you can have agent specialization, right? So rather than

**[02:59]** specialization, right? So rather than

**[02:59]** specialization, right? So rather than trying to make one agent do 100 things,


### [03:00 - 04:00]

**[03:02]** trying to make one agent do 100 things,

**[03:02]** trying to make one agent do 100 things, you can have a 100 agents do one thing

**[03:05]** you can have a 100 agents do one thing

**[03:05]** you can have a 100 agents do one thing and do that one thing very well. Um Away

**[03:08]** and do that one thing very well. Um Away

**[03:08]** and do that one thing very well. Um Away allows you to handle task delegation.

**[03:11]** allows you to handle task delegation.

**[03:11]** allows you to handle task delegation. So, you know, imagine you had a

**[03:13]** So, you know, imagine you had a

**[03:13]** So, you know, imagine you had a Salesforce agent um and you wanted it to

**[03:16]** Salesforce agent um and you wanted it to

**[03:16]** Salesforce agent um and you wanted it to interact with all the Salesforce MCP um

**[03:20]** interact with all the Salesforce MCP um

**[03:20]** interact with all the Salesforce MCP um uh tools. Uh you could do that. Um

**[03:22]** uh tools. Uh you could do that. Um

**[03:22]** uh tools. Uh you could do that. Um you've also got the ability to do

**[03:24]** you've also got the ability to do

**[03:24]** you've also got the ability to do parallel processing. Uh and this will

**[03:26]** parallel processing. Uh and this will

**[03:26]** parallel processing. Uh and this will become very important when it uh comes

**[03:28]** become very important when it uh comes

**[03:28]** become very important when it uh comes to speed and context management. Uh you

**[03:31]** to speed and context management. Uh you

**[03:31]** to speed and context management. Uh you can then use those A2A agents to have uh

**[03:34]** can then use those A2A agents to have uh

**[03:34]** can then use those A2A agents to have uh complex workflows and and help uh keep

**[03:37]** complex workflows and and help uh keep

**[03:37]** complex workflows and and help uh keep your main agents context size down.

**[03:42]** your main agents context size down.

**[03:42]** your main agents context size down. Uh MCP again really hot topic right now.

**[03:45]** Uh MCP again really hot topic right now.

**[03:45]** Uh MCP again really hot topic right now. Uh it's been kind of coined as the USBC

**[03:47]** Uh it's been kind of coined as the USBC

**[03:47]** Uh it's been kind of coined as the USBC for AI. Um and there's definitely some

**[03:50]** for AI. Um and there's definitely some

**[03:50]** for AI. Um and there's definitely some benefits in just having a standard

**[03:53]** benefits in just having a standard

**[03:53]** benefits in just having a standard interface, right? You know, there's

**[03:54]** interface, right? You know, there's

**[03:54]** interface, right? You know, there's something like 10,000 MCP uh tools that

**[03:57]** something like 10,000 MCP uh tools that

**[03:57]** something like 10,000 MCP uh tools that you can use today. Um about 7,000 of


### [04:00 - 05:00]

**[04:00]** you can use today. Um about 7,000 of

**[04:00]** you can use today. Um about 7,000 of those come through the Zapier MCP. Uh if

**[04:03]** those come through the Zapier MCP. Uh if

**[04:03]** those come through the Zapier MCP. Uh if you're not familiar with Zapier, it's

**[04:05]** you're not familiar with Zapier, it's

**[04:05]** you're not familiar with Zapier, it's essentially a way to connect disparate

**[04:09]** essentially a way to connect disparate

**[04:09]** essentially a way to connect disparate systems together. And they've now

**[04:11]** systems together. And they've now

**[04:11]** systems together. And they've now released all of their uh zaps they're

**[04:13]** released all of their uh zaps they're

**[04:13]** released all of their uh zaps they're called as MCP uh servers and tools.

**[04:17]** called as MCP uh servers and tools.

**[04:17]** called as MCP uh servers and tools. Uh one of the great things about MCP, no

**[04:19]** Uh one of the great things about MCP, no

**[04:19]** Uh one of the great things about MCP, no integration with APIs. So you don't have

**[04:22]** integration with APIs. So you don't have

**[04:22]** integration with APIs. So you don't have to do any sort of you know different

**[04:24]** to do any sort of you know different

**[04:24]** to do any sort of you know different handling of different APIs. Uh it's a

**[04:27]** handling of different APIs. Uh it's a

**[04:27]** handling of different APIs. Uh it's a plug-in architecture uh an industry

**[04:29]** plug-in architecture uh an industry

**[04:29]** plug-in architecture uh an industry standard. Um and it's really based on

**[04:31]** standard. Um and it's really based on

**[04:31]** standard. Um and it's really based on LSP. So LSP was a way for you know idees

**[04:35]** LSP. So LSP was a way for you know idees

**[04:35]** LSP. So LSP was a way for you know idees to actually uh figure out how different

**[04:37]** to actually uh figure out how different

**[04:38]** to actually uh figure out how different code languages worked. Um and it was a

**[04:40]** code languages worked. Um and it was a

**[04:40]** code languages worked. Um and it was a great kind of um transfer uh of of ideas

**[04:44]** great kind of um transfer uh of of ideas

**[04:44]** great kind of um transfer uh of of ideas over to the MCP protocol.

**[04:51]** All right. So when should you use A2A

**[04:51]** All right. So when should you use A2A versus MCP? Anybody?

**[04:58]** MC if you want to resource the

**[04:58]** MC if you want to resource the infrastructure


### [05:00 - 06:00]

**[05:00]** infrastructure

**[05:00]** infrastructure then you go for MCP

**[05:03]** then you go for MCP

**[05:03]** then you go for MCP but I don't know and and and that's kind

**[05:06]** but I don't know and and and that's kind

**[05:06]** but I don't know and and and that's kind of the the challenge right it's like

**[05:09]** of the the challenge right it's like

**[05:09]** of the the challenge right it's like what exactly um you know these protocols

**[05:12]** what exactly um you know these protocols

**[05:12]** what exactly um you know these protocols for and should I be using them and and

**[05:15]** for and should I be using them and and

**[05:15]** for and should I be using them and and things like that. So if you want to

**[05:17]** things like that. So if you want to

**[05:17]** things like that. So if you want to have, you know, two agents, right? And

**[05:20]** have, you know, two agents, right? And

**[05:20]** have, you know, two agents, right? And typically two agents that are completely

**[05:22]** typically two agents that are completely

**[05:22]** typically two agents that are completely unrelated, right? So it's not two agents

**[05:25]** unrelated, right? So it's not two agents

**[05:25]** unrelated, right? So it's not two agents you necessarily control. It's more

**[05:26]** you necessarily control. It's more

**[05:26]** you necessarily control. It's more likely going to be an agent of a third

**[05:28]** likely going to be an agent of a third

**[05:28]** likely going to be an agent of a third party or, you know, their first party

**[05:30]** party or, you know, their first party

**[05:30]** party or, you know, their first party agent and your agent. Yeah.

**[05:32]** agent and your agent. Yeah.

**[05:32]** agent and your agent. Yeah. What's the difference between agent

**[05:36]** What's the difference between agent

**[05:36]** What's the difference between agent and A2A? So I work a lot on the agent

**[05:41]** and A2A? So I work a lot on the agent

**[05:41]** and A2A? So I work a lot on the agent where we have multiple agents and doing

**[05:44]** where we have multiple agents and doing

**[05:44]** where we have multiple agents and doing the same. The you are saying describing

**[05:47]** the same. The you are saying describing

**[05:47]** the same. The you are saying describing A2A is a lot similar to a care.

**[05:51]** A2A is a lot similar to a care.

**[05:51]** A2A is a lot similar to a care. Yeah. So like autogen and and frameworks

**[05:54]** Yeah. So like autogen and and frameworks

**[05:54]** Yeah. So like autogen and and frameworks like that that allow you to kind of uh

**[05:56]** like that that allow you to kind of uh

**[05:56]** like that that allow you to kind of uh manage multiple agents kind of locally.

**[05:59]** manage multiple agents kind of locally.

**[05:59]** manage multiple agents kind of locally. H A2A is more about remote agents,


### [06:00 - 07:00]

**[06:01]** H A2A is more about remote agents,

**[06:01]** H A2A is more about remote agents, right? So agents you have no knowledge

**[06:03]** right? So agents you have no knowledge

**[06:04]** right? So agents you have no knowledge of. Um so you can think of A2A as a way

**[06:06]** of. Um so you can think of A2A as a way

**[06:06]** of. Um so you can think of A2A as a way for you to have service discoverability

**[06:08]** for you to have service discoverability

**[06:08]** for you to have service discoverability and once you have the endpoint to the

**[06:10]** and once you have the endpoint to the

**[06:10]** and once you have the endpoint to the agent, you can then learn everything

**[06:11]** agent, you can then learn everything

**[06:12]** agent, you can then learn everything that that agent's capable of. Um with

**[06:14]** that that agent's capable of. Um with

**[06:14]** that that agent's capable of. Um with things like autogen it's like you know

**[06:16]** things like autogen it's like you know

**[06:16]** things like autogen it's like you know descriptive so you describe what it's

**[06:18]** descriptive so you describe what it's

**[06:18]** descriptive so you describe what it's capable of it's in your control.

**[06:21]** capable of it's in your control.

**[06:21]** capable of it's in your control. So to summarize agent AI is kind of

**[06:26]** So to summarize agent AI is kind of

**[06:26]** So to summarize agent AI is kind of define the role of each agent and A2 is

**[06:32]** define the role of each agent and A2 is

**[06:32]** define the role of each agent and A2 is kind of working on remotely and its role

**[06:36]** kind of working on remotely and its role

**[06:36]** kind of working on remotely and its role is not defined or defined.

**[06:41]** is not defined or defined.

**[06:41]** is not defined or defined. So each of the A2A agents will have a a

**[06:44]** So each of the A2A agents will have a a

**[06:44]** So each of the A2A agents will have a a definition and we'll kind of get into

**[06:45]** definition and we'll kind of get into

**[06:45]** definition and we'll kind of get into that a little bit later. Um but yeah,

**[06:47]** that a little bit later. Um but yeah,

**[06:47]** that a little bit later. Um but yeah, think think of agentic AI kind of as a

**[06:49]** think think of agentic AI kind of as a

**[06:49]** think think of agentic AI kind of as a superset of everything, right? Um A2A

**[06:52]** superset of everything, right? Um A2A

**[06:52]** superset of everything, right? Um A2A and MCP are just kind of subsets of

**[06:54]** and MCP are just kind of subsets of

**[06:54]** and MCP are just kind of subsets of that, right? Different modalities. Um

**[06:58]** that, right? Different modalities. Um

**[06:58]** that, right? Different modalities. Um yeah, so for MCP, you're you're going to


### [07:00 - 08:00]

**[07:00]** yeah, so for MCP, you're you're going to

**[07:00]** yeah, so for MCP, you're you're going to connect to external context and tools.

**[07:02]** connect to external context and tools.

**[07:02]** connect to external context and tools. Um a lot of people don't use most of the

**[07:04]** Um a lot of people don't use most of the

**[07:04]** Um a lot of people don't use most of the features of MCP, right? They're just

**[07:05]** features of MCP, right? They're just

**[07:05]** features of MCP, right? They're just using the tools. Um but there's a lot of

**[07:08]** using the tools. Um but there's a lot of

**[07:08]** using the tools. Um but there's a lot of stuff around prompt templates resources

**[07:11]** stuff around prompt templates resources

**[07:11]** stuff around prompt templates resources um and a thing called um sampling

**[07:15]** um and a thing called um sampling

**[07:15]** um and a thing called um sampling sampling is actually going to be a

**[07:16]** sampling is actually going to be a

**[07:16]** sampling is actually going to be a really interesting thing I think that

**[07:17]** really interesting thing I think that

**[07:17]** really interesting thing I think that we'll see a lot more of as well uh where

**[07:19]** we'll see a lot more of as well uh where

**[07:20]** we'll see a lot more of as well uh where it allows these MCPs uh to sample the

**[07:23]** it allows these MCPs uh to sample the

**[07:23]** it allows these MCPs uh to sample the host LLM right so if you're using you

**[07:26]** host LLM right so if you're using you

**[07:26]** host LLM right so if you're using you know claude and you're hitting an MCP

**[07:28]** know claude and you're hitting an MCP

**[07:28]** know claude and you're hitting an MCP server um that MCP server may want to

**[07:31]** server um that MCP server may want to

**[07:31]** server um that MCP server may want to also use the same model of cloud that

**[07:33]** also use the same model of cloud that

**[07:33]** also use the same model of cloud that you're using and it can use sampling to

**[07:35]** you're using and it can use sampling to

**[07:35]** you're using and it can use sampling to actually achieve that Um, so when you

**[07:37]** actually achieve that Um, so when you

**[07:37]** actually achieve that Um, so when you bring those two together, you you kind

**[07:39]** bring those two together, you you kind

**[07:39]** bring those two together, you you kind of get the benefit of both, right? So

**[07:40]** of get the benefit of both, right? So

**[07:40]** of get the benefit of both, right? So you have A2A is the the remote

**[07:43]** you have A2A is the the remote

**[07:43]** you have A2A is the the remote interface. Uh, and MCP is then giving

**[07:46]** interface. Uh, and MCP is then giving

**[07:46]** interface. Uh, and MCP is then giving you the actual um tool use and and

**[07:49]** you the actual um tool use and and

**[07:49]** you the actual um tool use and and context management.

**[07:55]** Okay, so when not to use MCP. Um, and

**[07:55]** Okay, so when not to use MCP. Um, and and you'll notice a lot of like memes

**[07:57]** and you'll notice a lot of like memes

**[07:57]** and you'll notice a lot of like memes here. Uh, and just to give you a heads

**[07:59]** here. Uh, and just to give you a heads

**[07:59]** here. Uh, and just to give you a heads up, all memes were generated by Bench.


### [08:00 - 09:00]

**[08:01]** up, all memes were generated by Bench.

**[08:01]** up, all memes were generated by Bench. Uh, actually the whole slide deck was

**[08:03]** Uh, actually the whole slide deck was

**[08:03]** Uh, actually the whole slide deck was generated by Bench. um I just gave it a

**[08:05]** generated by Bench. um I just gave it a

**[08:05]** generated by Bench. um I just gave it a markdown file and it and it outputed it.

**[08:08]** markdown file and it and it outputed it.

**[08:08]** markdown file and it and it outputed it. So um when you use A to A or MCP um if

**[08:12]** So um when you use A to A or MCP um if

**[08:12]** So um when you use A to A or MCP um if you have full control of the tools then

**[08:13]** you have full control of the tools then

**[08:13]** you have full control of the tools then you probably don't need it right like if

**[08:15]** you probably don't need it right like if

**[08:15]** you probably don't need it right like if if your function is local to your

**[08:18]** if your function is local to your

**[08:18]** if your function is local to your codebase you know why do you need to

**[08:21]** codebase you know why do you need to

**[08:21]** codebase you know why do you need to create you know a USBC it's kind of like

**[08:23]** create you know a USBC it's kind of like

**[08:23]** create you know a USBC it's kind of like me plugging in my hard drive with a USB

**[08:26]** me plugging in my hard drive with a USB

**[08:26]** me plugging in my hard drive with a USB cable you know like shouldn't I just use

**[08:28]** cable you know like shouldn't I just use

**[08:28]** cable you know like shouldn't I just use the hard drive that's in my machine

**[08:30]** the hard drive that's in my machine

**[08:30]** the hard drive that's in my machine right um so calling functions directly

**[08:33]** right um so calling functions directly

**[08:33]** right um so calling functions directly in your codebase super easy easy to

**[08:35]** in your codebase super easy easy to

**[08:35]** in your codebase super easy easy to maintain faster to develop um and then

**[08:38]** maintain faster to develop um and then

**[08:38]** maintain faster to develop um and then If you have full control of your agents,

**[08:41]** If you have full control of your agents,

**[08:41]** If you have full control of your agents, you probably don't need A2A either,

**[08:42]** you probably don't need A2A either,

**[08:42]** you probably don't need A2A either, right? Um like if they're your agents,

**[08:45]** right? Um like if they're your agents,

**[08:45]** right? Um like if they're your agents, you can use, you know, some sort of

**[08:47]** you can use, you know, some sort of

**[08:47]** you can use, you know, some sort of local uh function call for them to

**[08:48]** local uh function call for them to

**[08:48]** local uh function call for them to communicate. And and I I've built multi-

**[08:51]** communicate. And and I I've built multi-

**[08:51]** communicate. And and I I've built multi- aent systems using MCP and using just

**[08:54]** aent systems using MCP and using just

**[08:54]** aent systems using MCP and using just local function calls. It's a lot easier

**[08:56]** local function calls. It's a lot easier

**[08:56]** local function calls. It's a lot easier to just use the code you have. Uh it's

**[08:59]** to just use the code you have. Uh it's

**[08:59]** to just use the code you have. Uh it's going to be faster. There's no protocol


### [09:00 - 10:00]

**[09:01]** going to be faster. There's no protocol

**[09:01]** going to be faster. There's no protocol overheads and and things like that. A

**[09:03]** overheads and and things like that. A

**[09:03]** overheads and and things like that. A lot easier to debug as well.

**[09:07]** lot easier to debug as well.

**[09:07]** lot easier to debug as well. Okay. So, why do you need A2A and MCP at

**[09:10]** Okay. So, why do you need A2A and MCP at

**[09:10]** Okay. So, why do you need A2A and MCP at all? Right. Um, third party tools is

**[09:13]** all? Right. Um, third party tools is

**[09:13]** all? Right. Um, third party tools is probably the number one reason uh to use

**[09:15]** probably the number one reason uh to use

**[09:15]** probably the number one reason uh to use MCP. Um, you can just get access to such

**[09:19]** MCP. Um, you can just get access to such

**[09:19]** MCP. Um, you can just get access to such a large array of tools um that you know

**[09:22]** a large array of tools um that you know

**[09:22]** a large array of tools um that you know you're never going to be able to uh

**[09:24]** you're never going to be able to uh

**[09:24]** you're never going to be able to uh let's say you're building a product,

**[09:26]** let's say you're building a product,

**[09:26]** let's say you're building a product, right? And and you're like, "Okay, we're

**[09:27]** right? And and you're like, "Okay, we're

**[09:27]** right? And and you're like, "Okay, we're going to build first class integrations

**[09:29]** going to build first class integrations

**[09:29]** going to build first class integrations with Salesforce and Slack and but what

**[09:31]** with Salesforce and Slack and but what

**[09:31]** with Salesforce and Slack and but what about the other 10,000 tools?" I was

**[09:33]** about the other 10,000 tools?" I was

**[09:33]** about the other 10,000 tools?" I was like, "Okay, we'll just allow people to

**[09:35]** like, "Okay, we'll just allow people to

**[09:35]** like, "Okay, we'll just allow people to add their own MCP server." Um, so that

**[09:38]** add their own MCP server." Um, so that

**[09:38]** add their own MCP server." Um, so that gives you great extensibility. Um, but

**[09:40]** gives you great extensibility. Um, but

**[09:40]** gives you great extensibility. Um, but there's a lot of drawbacks with MCP,

**[09:41]** there's a lot of drawbacks with MCP,

**[09:42]** there's a lot of drawbacks with MCP, right? Um, you only get what you're

**[09:44]** right? Um, you only get what you're

**[09:44]** right? Um, you only get what you're given. Um, and a lot of time that's not

**[09:46]** given. Um, and a lot of time that's not

**[09:46]** given. Um, and a lot of time that's not exactly what you want. Um, so you may go

**[09:49]** exactly what you want. Um, so you may go

**[09:49]** exactly what you want. Um, so you may go down the route of saying, you know what,

**[09:50]** down the route of saying, you know what,

**[09:50]** down the route of saying, you know what, I need a a way to actually index this

**[09:53]** I need a a way to actually index this

**[09:53]** I need a a way to actually index this data so that I'm not calling like, you

**[09:55]** data so that I'm not calling like, you

**[09:55]** data so that I'm not calling like, you know, list Slack channels every time I

**[09:58]** know, list Slack channels every time I

**[09:58]** know, list Slack channels every time I want to post a channel, right? Or post a


### [10:00 - 11:00]

**[10:00]** want to post a channel, right? Or post a

**[10:00]** want to post a channel, right? Or post a message.

**[10:01]** message.

**[10:01]** message. Um, and then with A2A, uh, the com

**[10:04]** Um, and then with A2A, uh, the com

**[10:04]** Um, and then with A2A, uh, the com complexity is hidden from you, right?

**[10:05]** complexity is hidden from you, right?

**[10:05]** complexity is hidden from you, right? And that's one of the kind of the key

**[10:07]** And that's one of the kind of the key

**[10:07]** And that's one of the kind of the key tenants of of A2A is that you don't know

**[10:10]** tenants of of A2A is that you don't know

**[10:10]** tenants of of A2A is that you don't know anything about this agent until you

**[10:12]** anything about this agent until you

**[10:12]** anything about this agent until you connect. Um, and all of its complexity

**[10:15]** connect. Um, and all of its complexity

**[10:15]** connect. Um, and all of its complexity is is completely opaque.

**[10:17]** is is completely opaque.

**[10:17]** is is completely opaque. Um, and then you you can essentially

**[10:20]** Um, and then you you can essentially

**[10:20]** Um, and then you you can essentially connect to, you know, any sort of uh

**[10:23]** connect to, you know, any sort of uh

**[10:23]** connect to, you know, any sort of uh remote A2A agent. Um, so long as you

**[10:26]** remote A2A agent. Um, so long as you

**[10:26]** remote A2A agent. Um, so long as you have, you know, the credentials and

**[10:27]** have, you know, the credentials and

**[10:27]** have, you know, the credentials and things like that. Um, we haven't seen

**[10:29]** things like that. Um, we haven't seen

**[10:29]** things like that. Um, we haven't seen any firstparty A2A agents released yet.

**[10:32]** any firstparty A2A agents released yet.

**[10:32]** any firstparty A2A agents released yet. Um, but Google has about I think 50 uh

**[10:34]** Um, but Google has about I think 50 uh

**[10:34]** Um, but Google has about I think 50 uh partners they're going to launch with.

**[10:36]** partners they're going to launch with.

**[10:36]** partners they're going to launch with. So, I I'd imagine there's going to be

**[10:38]** So, I I'd imagine there's going to be

**[10:38]** So, I I'd imagine there's going to be like a Salesforce A2A agent. Um, it'll

**[10:41]** like a Salesforce A2A agent. Um, it'll

**[10:41]** like a Salesforce A2A agent. Um, it'll probably only come with a paid account,

**[10:43]** probably only come with a paid account,

**[10:43]** probably only come with a paid account, right? Because it's going to use LLM

**[10:45]** right? Because it's going to use LLM

**[10:45]** right? Because it's going to use LLM compute. Uh, versus things like MCP

**[10:48]** compute. Uh, versus things like MCP

**[10:48]** compute. Uh, versus things like MCP typically don't actually use an LLM,

**[10:50]** typically don't actually use an LLM,

**[10:50]** typically don't actually use an LLM, right? They use the host LLM.

**[10:54]** right? They use the host LLM.

**[10:54]** right? They use the host LLM. All righty. So, we're going to get into

**[10:55]** All righty. So, we're going to get into

**[10:55]** All righty. So, we're going to get into the code now. Um

**[10:58]** the code now. Um

**[10:58]** the code now. Um yeah, so uh if you haven't already


### [11:00 - 12:00]

**[11:00]** yeah, so uh if you haven't already

**[11:00]** yeah, so uh if you haven't already grabbed the repo, uh we also have a

**[11:02]** grabbed the repo, uh we also have a

**[11:02]** grabbed the repo, uh we also have a Slack channel, um workshop A2A-mcp,

**[11:08]** Slack channel, um workshop A2A-mcp,

**[11:08]** Slack channel, um workshop A2A-mcp, uh-2025.

**[11:09]** uh-2025.

**[11:10]** uh-2025. Um and in this repo, there's basically

**[11:12]** Um and in this repo, there's basically

**[11:12]** Um and in this repo, there's basically every everything you need to get going.

**[11:14]** every everything you need to get going.

**[11:14]** every everything you need to get going. Um

**[11:17]** Um

**[11:17]** Um yeah, so the the code structure, uh

**[11:19]** yeah, so the the code structure, uh

**[11:19]** yeah, so the the code structure, uh we've got a host agent, um and then

**[11:21]** we've got a host agent, um and then

**[11:21]** we've got a host agent, um and then we've got some sub agents, right? And

**[11:23]** we've got some sub agents, right? And

**[11:24]** we've got some sub agents, right? And the whole concept here is to

**[11:25]** the whole concept here is to

**[11:25]** the whole concept here is to demonstrate, you know, ATA and MCP. Um,

**[11:28]** demonstrate, you know, ATA and MCP. Um,

**[11:28]** demonstrate, you know, ATA and MCP. Um, but in reality, these sub agents will

**[11:30]** but in reality, these sub agents will

**[11:30]** but in reality, these sub agents will probably live in a different repo, you

**[11:33]** probably live in a different repo, you

**[11:33]** probably live in a different repo, you know, run on a different server. Um,

**[11:36]** know, run on a different server. Um,

**[11:36]** know, run on a different server. Um, yeah. And then we've also got the uh A2A

**[11:38]** yeah. And then we've also got the uh A2A

**[11:38]** yeah. And then we've also got the uh A2A implementation. Uh, the server and the

**[11:40]** implementation. Uh, the server and the

**[11:40]** implementation. Uh, the server and the client in uh the repo. Uh, these are

**[11:43]** client in uh the repo. Uh, these are

**[11:43]** client in uh the repo. Uh, these are taken directly from the ATA uh repo.

**[11:46]** taken directly from the ATA uh repo.

**[11:46]** taken directly from the ATA uh repo. We've also got the MCP integration. So,

**[11:48]** We've also got the MCP integration. So,

**[11:48]** We've also got the MCP integration. So, this is just a client. Um, we're not

**[11:50]** this is just a client. Um, we're not

**[11:50]** this is just a client. Um, we're not creating a a server here. Uh we also

**[11:54]** creating a a server here. Uh we also

**[11:54]** creating a a server here. Uh we also have a CLI interface. You're not going

**[11:56]** have a CLI interface. You're not going

**[11:56]** have a CLI interface. You're not going to need the CLI interface. That's kind

**[11:57]** to need the CLI interface. That's kind

**[11:57]** to need the CLI interface. That's kind of internally how it's being used. Um


### [12:00 - 13:00]

**[12:02]** of internally how it's being used. Um

**[12:02]** of internally how it's being used. Um yeah, so once you've cloned a repo,

**[12:04]** yeah, so once you've cloned a repo,

**[12:04]** yeah, so once you've cloned a repo, you're going to want an MPM install. Um

**[12:06]** you're going to want an MPM install. Um

**[12:06]** you're going to want an MPM install. Um and you're going to need a MCP server

**[12:08]** and you're going to need a MCP server

**[12:08]** and you're going to need a MCP server URL. Uh this is going to be a Zapier uh

**[12:12]** URL. Uh this is going to be a Zapier uh

**[12:12]** URL. Uh this is going to be a Zapier uh URL and a Gemini API key. Uh you can get

**[12:14]** URL and a Gemini API key. Uh you can get

**[12:14]** URL and a Gemini API key. Uh you can get both of these for free. Uh there's no

**[12:16]** both of these for free. Uh there's no

**[12:16]** both of these for free. Uh there's no need to to sign up for a paid account to

**[12:18]** need to to sign up for a paid account to

**[12:18]** need to to sign up for a paid account to get them. Um and you'll want to rename

**[12:20]** get them. Um and you'll want to rename

**[12:20]** get them. Um and you'll want to rename your mv.ample example uh to

**[12:31]** all right so setting up the Zapier MCP

**[12:31]** all right so setting up the Zapier MCP um when you go to uh zapier.com/mcp

**[12:35]** um when you go to uh zapier.com/mcp

**[12:35]** um when you go to uh zapier.com/mcp uh you'll have the option to create a

**[12:36]** uh you'll have the option to create a

**[12:36]** uh you'll have the option to create a new server um and when you go to connect

**[12:39]** new server um and when you go to connect

**[12:39]** new server um and when you go to connect you're going to have a couple of uh

**[12:40]** you're going to have a couple of uh

**[12:40]** you're going to have a couple of uh options here we're going to use SSE um

**[12:44]** options here we're going to use SSE um

**[12:44]** options here we're going to use SSE um they recently released uh streamable

**[12:46]** they recently released uh streamable

**[12:46]** they recently released uh streamable HTTP which uh is making SSE deprecated

**[12:49]** HTTP which uh is making SSE deprecated

**[12:50]** HTTP which uh is making SSE deprecated and it's going to replace it um but

**[12:51]** and it's going to replace it um but

**[12:51]** and it's going to replace it um but there's There's still a litany of SSE

**[12:53]** there's There's still a litany of SSE

**[12:54]** there's There's still a litany of SSE servers out there. So, um I just used

**[12:57]** servers out there. So, um I just used

**[12:57]** servers out there. So, um I just used SSE for this one. Um once you do that,


### [13:00 - 14:00]

**[13:00]** SSE for this one. Um once you do that,

**[13:00]** SSE for this one. Um once you do that, you're going to get this server URL at

**[13:01]** you're going to get this server URL at

**[13:02]** you're going to get this server URL at the bottom. You can copy that URL.

**[13:03]** the bottom. You can copy that URL.

**[13:03]** the bottom. You can copy that URL. That's going to be the URL that goes

**[13:04]** That's going to be the URL that goes

**[13:04]** That's going to be the URL that goes into your

**[13:07]** into your

**[13:07]** into your and then uh you're going to set up a

**[13:09]** and then uh you're going to set up a

**[13:09]** and then uh you're going to set up a Slack and a GitHub integration. Um so,

**[13:11]** Slack and a GitHub integration. Um so,

**[13:12]** Slack and a GitHub integration. Um so, you're going to want the ability to

**[13:13]** you're going to want the ability to

**[13:13]** you're going to want the ability to create an issue. Um you can put in uh

**[13:16]** create an issue. Um you can put in uh

**[13:16]** create an issue. Um you can put in uh the repository URL for the workshop if

**[13:18]** the repository URL for the workshop if

**[13:18]** the repository URL for the workshop if you want. Uh you can use your own uh as

**[13:20]** you want. Uh you can use your own uh as

**[13:20]** you want. Uh you can use your own uh as well. um you can let AI choose uh these,

**[13:25]** well. um you can let AI choose uh these,

**[13:25]** well. um you can let AI choose uh these, but what I found with AI is that it will

**[13:27]** but what I found with AI is that it will

**[13:28]** but what I found with AI is that it will choose something else, right? Um so a

**[13:30]** choose something else, right? Um so a

**[13:30]** choose something else, right? Um so a lot of time with these MCPs, you're

**[13:32]** lot of time with these MCPs, you're

**[13:32]** lot of time with these MCPs, you're going to want to kind of say, hey, you

**[13:33]** going to want to kind of say, hey, you

**[13:33]** going to want to kind of say, hey, you know, this is the thing I want to do, so

**[13:35]** know, this is the thing I want to do, so

**[13:36]** know, this is the thing I want to do, so let's just kind of hardcode that. Um but

**[13:38]** let's just kind of hardcode that. Um but

**[13:38]** let's just kind of hardcode that. Um but if if you do let it kind of go wild into

**[13:40]** if if you do let it kind of go wild into

**[13:40]** if if you do let it kind of go wild into your Slack, uh it's going to start

**[13:42]** your Slack, uh it's going to start

**[13:42]** your Slack, uh it's going to start posting in general and random and sales

**[13:45]** posting in general and random and sales

**[13:45]** posting in general and random and sales and uh yeah, a few of my bots have kind

**[13:47]** and uh yeah, a few of my bots have kind

**[13:47]** and uh yeah, a few of my bots have kind of gone rogue.

**[13:50]** of gone rogue.

**[13:50]** of gone rogue. All right. So, the Gemini setup. Yeah.

**[13:53]** All right. So, the Gemini setup. Yeah.

**[13:53]** All right. So, the Gemini setup. Yeah. So, you can get the uh API key here, the

**[13:55]** So, you can get the uh API key here, the

**[13:55]** So, you can get the uh API key here, the AI studio. Um, and there's a a link in

**[13:59]** AI studio. Um, and there's a a link in

**[13:59]** AI studio. Um, and there's a a link in the uh slide deck as well if you need to


### [14:00 - 15:00]

**[14:01]** the uh slide deck as well if you need to

**[14:01]** the uh slide deck as well if you need to click it. Um, you can get a free

**[14:03]** click it. Um, you can get a free

**[14:03]** click it. Um, you can get a free account, generate an API key, uh, drop

**[14:06]** account, generate an API key, uh, drop

**[14:06]** account, generate an API key, uh, drop that into your M as well.

**[14:09]** that into your M as well.

**[14:09]** that into your M as well. Excuse me.

**[14:12]** Excuse me.

**[14:12]** Excuse me. And there's also a remote uh, bench A2A

**[14:14]** And there's also a remote uh, bench A2A

**[14:14]** And there's also a remote uh, bench A2A agent. Um, so the code for it actually

**[14:17]** agent. Um, so the code for it actually

**[14:17]** agent. Um, so the code for it actually in the repo. Um, but we haven't

**[14:19]** in the repo. Um, but we haven't

**[14:19]** in the repo. Um, but we haven't officially released our API yet. So, I'm

**[14:22]** officially released our API yet. So, I'm

**[14:22]** officially released our API yet. So, I'm just hosting that remotely. Um, but it's

**[14:23]** just hosting that remotely. Um, but it's

**[14:23]** just hosting that remotely. Um, but it's a nice kind of way to show how you would

**[14:26]** a nice kind of way to show how you would

**[14:26]** a nice kind of way to show how you would use A2A remotely as well.

**[14:29]** use A2A remotely as well.

**[14:29]** use A2A remotely as well. Um, so what is Bench? Uh, Bench is

**[14:32]** Um, so what is Bench? Uh, Bench is

**[14:32]** Um, so what is Bench? Uh, Bench is essentially a kind of LLM aggregator uh

**[14:35]** essentially a kind of LLM aggregator uh

**[14:35]** essentially a kind of LLM aggregator uh with autonomous AI agents. Um, so you

**[14:38]** with autonomous AI agents. Um, so you

**[14:38]** with autonomous AI agents. Um, so you get access to cloud, Gemini, OpenAI, XAI

**[14:40]** get access to cloud, Gemini, OpenAI, XAI

**[14:40]** get access to cloud, Gemini, OpenAI, XAI and loads more models. Uh, it has I

**[14:43]** and loads more models. Uh, it has I

**[14:43]** and loads more models. Uh, it has I think about 30 tools now um and

**[14:45]** think about 30 tools now um and

**[14:45]** think about 30 tools now um and integrations. So um we actually started

**[14:47]** integrations. So um we actually started

**[14:48]** integrations. So um we actually started out with MCP integrations to Slack and

**[14:50]** out with MCP integrations to Slack and

**[14:50]** out with MCP integrations to Slack and Salesforce. They didn't meet our needs.

**[14:52]** Salesforce. They didn't meet our needs.

**[14:52]** Salesforce. They didn't meet our needs. We built firstparty integrations, you

**[14:54]** We built firstparty integrations, you

**[14:54]** We built firstparty integrations, you know, data caching and indexing. Um and

**[14:56]** know, data caching and indexing. Um and

**[14:56]** know, data caching and indexing. Um and and that kind of gives you an idea of

**[14:58]** and that kind of gives you an idea of

**[14:58]** and that kind of gives you an idea of like how far is MCP going to get you,


### [15:00 - 16:00]

**[15:00]** like how far is MCP going to get you,

**[15:00]** like how far is MCP going to get you, right? Uh eventually at some point

**[15:02]** right? Uh eventually at some point

**[15:02]** right? Uh eventually at some point you're going to realize that it doesn't

**[15:03]** you're going to realize that it doesn't

**[15:04]** you're going to realize that it doesn't do the you know the specific thing you

**[15:05]** do the you know the specific thing you

**[15:06]** do the you know the specific thing you need to do.

**[15:08]** need to do.

**[15:08]** need to do. All right. So running the application

**[15:11]** All right. So running the application

**[15:11]** All right. So running the application um you're going to run mpm run start all

**[15:14]** um you're going to run mpm run start all

**[15:14]** um you're going to run mpm run start all um and that's going to kick off all the

**[15:17]** um and that's going to kick off all the

**[15:17]** um and that's going to kick off all the agents right so the slack agent the

**[15:20]** agents right so the slack agent the

**[15:20]** agents right so the slack agent the github agent uh the host agent and uh

**[15:23]** github agent uh the host agent and uh

**[15:23]** github agent uh the host agent and uh it'll also start the web hook server and

**[15:25]** it'll also start the web hook server and

**[15:25]** it'll also start the web hook server and the web hook uh admin panel uh you can

**[15:28]** the web hook uh admin panel uh you can

**[15:28]** the web hook uh admin panel uh you can access net then through localhost port

**[15:30]** access net then through localhost port

**[15:30]** access net then through localhost port 3000

**[15:33]** 3000

**[15:33]** 3000 and um yeah so let's just kind of go

**[15:36]** and um yeah so let's just kind of go

**[15:36]** and um yeah so let's just kind of go into what each of the actual

**[15:38]** into what each of the actual

**[15:38]** into what each of the actual uh agents do. Um so the host agent is

**[15:41]** uh agents do. Um so the host agent is

**[15:41]** uh agents do. Um so the host agent is essentially your central coordinator,

**[15:43]** essentially your central coordinator,

**[15:43]** essentially your central coordinator, right? Um and this this may be the only

**[15:46]** right? Um and this this may be the only

**[15:46]** right? Um and this this may be the only agent that you have in your application.

**[15:48]** agent that you have in your application.

**[15:48]** agent that you have in your application. It may be using external uh A2A agents.

**[15:52]** It may be using external uh A2A agents.

**[15:52]** It may be using external uh A2A agents. Uh and if that's the case, then you know

**[15:55]** Uh and if that's the case, then you know

**[15:55]** Uh and if that's the case, then you know everything that your host does is going

**[15:57]** everything that your host does is going

**[15:57]** everything that your host does is going to be delegated um you know to sub


### [16:00 - 17:00]

**[16:00]** to be delegated um you know to sub

**[16:00]** to be delegated um you know to sub agents.

**[16:03]** agents.

**[16:03]** agents. Um, so that handles all the agent

**[16:04]** Um, so that handles all the agent

**[16:04]** Um, so that handles all the agent discovery and and kind of bringing

**[16:06]** discovery and and kind of bringing

**[16:06]** discovery and and kind of bringing everything together.

**[16:09]** everything together.

**[16:09]** everything together. Yeah. So the the code for that's going

**[16:10]** Yeah. So the the code for that's going

**[16:10]** Yeah. So the the code for that's going to be in source agents host

**[16:13]** to be in source agents host

**[16:13]** to be in source agents host and um you'll notice there's a couple of

**[16:15]** and um you'll notice there's a couple of

**[16:15]** and um you'll notice there's a couple of files in there. One of them is uh the

**[16:17]** files in there. One of them is uh the

**[16:17]** files in there. One of them is uh the host agent prompt, right? So that's just

**[16:19]** host agent prompt, right? So that's just

**[16:19]** host agent prompt, right? So that's just a plain text uh system prompt uh genkit.

**[16:23]** a plain text uh system prompt uh genkit.

**[16:23]** a plain text uh system prompt uh genkit. That's going to be uh essentially how

**[16:25]** That's going to be uh essentially how

**[16:25]** That's going to be uh essentially how you hook all of your A2A code up with

**[16:28]** you hook all of your A2A code up with

**[16:28]** you hook all of your A2A code up with Gemini. Um and there there's also a

**[16:32]** Gemini. Um and there there's also a

**[16:32]** Gemini. Um and there there's also a genkit MCP plugin that um the sub agents

**[16:35]** genkit MCP plugin that um the sub agents

**[16:35]** genkit MCP plugin that um the sub agents use.

**[16:41]** Uh so then the Slack agent um so this is

**[16:41]** Uh so then the Slack agent um so this is going to send a Slack message in

**[16:43]** going to send a Slack message in

**[16:43]** going to send a Slack message in response to the web hook transcript and

**[16:45]** response to the web hook transcript and

**[16:45]** response to the web hook transcript and yeah the the the kind of sample web hook

**[16:48]** yeah the the the kind of sample web hook

**[16:48]** yeah the the the kind of sample web hook that we have in this is essentially you

**[16:49]** that we have in this is essentially you

**[16:49]** that we have in this is essentially you know your meeting end and you're going

**[16:52]** know your meeting end and you're going

**[16:52]** know your meeting end and you're going to receive a transcript of that meeting

**[16:54]** to receive a transcript of that meeting

**[16:54]** to receive a transcript of that meeting right um and with that you're going to

**[16:57]** right um and with that you're going to

**[16:57]** right um and with that you're going to decide what to do. So, it's going to,

**[16:59]** decide what to do. So, it's going to,

**[16:59]** decide what to do. So, it's going to, you know, if it detects any bugs, it's


### [17:00 - 18:00]

**[17:01]** you know, if it detects any bugs, it's

**[17:01]** you know, if it detects any bugs, it's going to create a GitHub issue. If it

**[17:03]** going to create a GitHub issue. If it

**[17:03]** going to create a GitHub issue. If it detects any, you know, feature requests

**[17:05]** detects any, you know, feature requests

**[17:05]** detects any, you know, feature requests or or anything of interest, it's going

**[17:06]** or or anything of interest, it's going

**[17:06]** or or anything of interest, it's going to post that into Slack. Um, and you can

**[17:09]** to post that into Slack. Um, and you can

**[17:09]** to post that into Slack. Um, and you can think of the kind of automations that

**[17:11]** think of the kind of automations that

**[17:11]** think of the kind of automations that you can build with this sort of, uh,

**[17:12]** you can build with this sort of, uh,

**[17:12]** you can build with this sort of, uh, scenario, right? So, um, you could even

**[17:15]** scenario, right? So, um, you could even

**[17:15]** scenario, right? So, um, you could even I had a version here that was hooked up

**[17:17]** I had a version here that was hooked up

**[17:17]** I had a version here that was hooked up to Salesforce, but um, there's actually

**[17:19]** to Salesforce, but um, there's actually

**[17:19]** to Salesforce, but um, there's actually a limitation on the host agent on how

**[17:22]** a limitation on the host agent on how

**[17:22]** a limitation on the host agent on how many sub agents it can call. Um, so I I

**[17:25]** many sub agents it can call. Um, so I I

**[17:25]** many sub agents it can call. Um, so I I figured, right, if one of them's going

**[17:26]** figured, right, if one of them's going

**[17:26]** figured, right, if one of them's going to go, it's going to be Salesforce

**[17:27]** to go, it's going to be Salesforce

**[17:28]** to go, it's going to be Salesforce because it's it's probably the hardest

**[17:29]** because it's it's probably the hardest

**[17:29]** because it's it's probably the hardest to get an account on. Um, but you could

**[17:31]** to get an account on. Um, but you could

**[17:31]** to get an account on. Um, but you could actually update an opportunity based on

**[17:34]** actually update an opportunity based on

**[17:34]** actually update an opportunity based on a sales call, right? So you could have a

**[17:35]** a sales call, right? So you could have a

**[17:35]** a sales call, right? So you could have a sales call and you, you know, you're

**[17:37]** sales call and you, you know, you're

**[17:37]** sales call and you, you know, you're talking to them, you're doing your

**[17:38]** talking to them, you're doing your

**[17:38]** talking to them, you're doing your discovery and you're able to update

**[17:40]** discovery and you're able to update

**[17:40]** discovery and you're able to update those Salesforce fields automatically.

**[17:43]** those Salesforce fields automatically.

**[17:43]** those Salesforce fields automatically. Um, and like the time saving for account

**[17:45]** Um, and like the time saving for account

**[17:45]** Um, and like the time saving for account executives because, you know, they're

**[17:46]** executives because, you know, they're

**[17:46]** executives because, you know, they're probably on backtoback calls is actually

**[17:49]** probably on backtoback calls is actually

**[17:49]** probably on backtoback calls is actually pretty big.

**[17:55]** Yeah. This was an interesting um issue I

**[17:56]** Yeah. This was an interesting um issue I ran into. So I asked one of my

**[17:57]** ran into. So I asked one of my

**[17:57]** ran into. So I asked one of my colleagues um to test the repo out,


### [18:00 - 19:00]

**[18:00]** colleagues um to test the repo out,

**[18:00]** colleagues um to test the repo out, right? Um and he was getting this weird

**[18:02]** right? Um and he was getting this weird

**[18:02]** right? Um and he was getting this weird error where it was saying, you know, the

**[18:04]** error where it was saying, you know, the

**[18:04]** error where it was saying, you know, the Slack MCP succeeded. Um so I asked him

**[18:08]** Slack MCP succeeded. Um so I asked him

**[18:08]** Slack MCP succeeded. Um so I asked him to send me the logs and he sent me this

**[18:11]** to send me the logs and he sent me this

**[18:11]** to send me the logs and he sent me this and it was like is error false?

**[18:14]** and it was like is error false?

**[18:14]** and it was like is error false? And I'm like okay that's that's great.

**[18:17]** And I'm like okay that's that's great.

**[18:17]** And I'm like okay that's that's great. So yeah, it turns out that you know not

**[18:19]** So yeah, it turns out that you know not

**[18:20]** So yeah, it turns out that you know not all MCPs are created equally and the

**[18:22]** all MCPs are created equally and the

**[18:22]** all MCPs are created equally and the Zapier Slack MCP uh fails silently. Um

**[18:26]** Zapier Slack MCP uh fails silently. Um

**[18:26]** Zapier Slack MCP uh fails silently. Um so the the reason it failed was he he

**[18:28]** so the the reason it failed was he he

**[18:28]** so the the reason it failed was he he had um the default Slack channel name uh

**[18:32]** had um the default Slack channel name uh

**[18:32]** had um the default Slack channel name uh which was like test uh Damian Slack and

**[18:36]** which was like test uh Damian Slack and

**[18:36]** which was like test uh Damian Slack and he was in a different workspace where

**[18:37]** he was in a different workspace where

**[18:37]** he was in a different workspace where that channel didn't exist. So it just

**[18:39]** that channel didn't exist. So it just

**[18:39]** that channel didn't exist. So it just failed silently. Uh so I added a bit of

**[18:41]** failed silently. Uh so I added a bit of

**[18:41]** failed silently. Uh so I added a bit of code to detect this kind of empty text

**[18:43]** code to detect this kind of empty text

**[18:43]** code to detect this kind of empty text array. Um so it will fail now. Um, but

**[18:46]** array. Um so it will fail now. Um, but

**[18:46]** array. Um so it will fail now. Um, but it kind of goes to show you just kind of

**[18:49]** it kind of goes to show you just kind of

**[18:49]** it kind of goes to show you just kind of the limitations of MCP.

**[18:53]** the limitations of MCP.

**[18:53]** the limitations of MCP. Yeah. So, the GitHub agent, uh, pretty

**[18:54]** Yeah. So, the GitHub agent, uh, pretty

**[18:54]** Yeah. So, the GitHub agent, uh, pretty straightforward. It's it's it's probably

**[18:56]** straightforward. It's it's it's probably

**[18:56]** straightforward. It's it's it's probably the the most basic of of of the the

**[18:59]** the the most basic of of of the the

**[18:59]** the the most basic of of of the the three or four. Um, so it it just creates


### [19:00 - 20:00]

**[19:02]** three or four. Um, so it it just creates

**[19:02]** three or four. Um, so it it just creates a GitHub issue. Um, super simple. Um,

**[19:05]** a GitHub issue. Um, super simple. Um,

**[19:05]** a GitHub issue. Um, super simple. Um, but you could imagine, you know, how you

**[19:07]** but you could imagine, you know, how you

**[19:07]** but you could imagine, you know, how you would extend this, right? Maybe it's

**[19:08]** would extend this, right? Maybe it's

**[19:08]** would extend this, right? Maybe it's going to open a PR, right? maybe it's

**[19:11]** going to open a PR, right? maybe it's

**[19:11]** going to open a PR, right? maybe it's actually going to implement uh the fix

**[19:13]** actually going to implement uh the fix

**[19:13]** actually going to implement uh the fix for the bug that was reported uh in the

**[19:15]** for the bug that was reported uh in the

**[19:15]** for the bug that was reported uh in the meeting. Um and you can see how down the

**[19:17]** meeting. Um and you can see how down the

**[19:17]** meeting. Um and you can see how down the line as you know AI gets better and and

**[19:20]** line as you know AI gets better and and

**[19:20]** line as you know AI gets better and and and things really improve that a lot of

**[19:22]** and things really improve that a lot of

**[19:22]** and things really improve that a lot of this automation is going to be driven by

**[19:25]** this automation is going to be driven by

**[19:25]** this automation is going to be driven by human interaction, right? So you know

**[19:27]** human interaction, right? So you know

**[19:27]** human interaction, right? So you know speaking with people and posting

**[19:29]** speaking with people and posting

**[19:29]** speaking with people and posting messages in Slack and talking and GitHub

**[19:31]** messages in Slack and talking and GitHub

**[19:31]** messages in Slack and talking and GitHub discussions um is going to trigger AI to

**[19:34]** discussions um is going to trigger AI to

**[19:34]** discussions um is going to trigger AI to take action.

**[19:37]** take action.

**[19:37]** take action. Yeah. So the bench agent um it can it

**[19:40]** Yeah. So the bench agent um it can it

**[19:40]** Yeah. So the bench agent um it can it can do a lot. Uh and that was actually

**[19:41]** can do a lot. Uh and that was actually

**[19:42]** can do a lot. Uh and that was actually one of the problems that I found with

**[19:43]** one of the problems that I found with

**[19:43]** one of the problems that I found with A2A is that like the more functions and

**[19:47]** A2A is that like the more functions and

**[19:47]** A2A is that like the more functions and capabilities an agent has and the harder

**[19:50]** capabilities an agent has and the harder

**[19:50]** capabilities an agent has and the harder it is to describe the agents

**[19:52]** it is to describe the agents

**[19:52]** it is to describe the agents capabilities um in the agent card. Um so

**[19:55]** capabilities um in the agent card. Um so

**[19:55]** capabilities um in the agent card. Um so the agent card is essentially like the

**[19:57]** the agent card is essentially like the

**[19:57]** the agent card is essentially like the public um information to any other agent


### [20:00 - 21:00]

**[20:01]** public um information to any other agent

**[20:01]** public um information to any other agent of what that agent's capable of. Um, so

**[20:03]** of what that agent's capable of. Um, so

**[20:03]** of what that agent's capable of. Um, so I had to really just pair it back and I

**[20:05]** I had to really just pair it back and I

**[20:05]** I had to really just pair it back and I said, "Look, you know, you can do a

**[20:06]** said, "Look, you know, you can do a

**[20:06]** said, "Look, you know, you can do a handful of things. I know you can do

**[20:08]** handful of things. I know you can do

**[20:08]** handful of things. I know you can do more, but like for now, these are the

**[20:10]** more, but like for now, these are the

**[20:10]** more, but like for now, these are the few things that you can do." Um, and

**[20:12]** few things that you can do." Um, and

**[20:12]** few things that you can do." Um, and it's able to go off and like, you know,

**[20:13]** it's able to go off and like, you know,

**[20:14]** it's able to go off and like, you know, browse the web, do research, uh, data

**[20:16]** browse the web, do research, uh, data

**[20:16]** browse the web, do research, uh, data science, all sorts of things. Um, so

**[20:18]** science, all sorts of things. Um, so

**[20:18]** science, all sorts of things. Um, so we're just going to use it for, uh,

**[20:20]** we're just going to use it for, uh,

**[20:20]** we're just going to use it for, uh, researching the company and the people,

**[20:22]** researching the company and the people,

**[20:22]** researching the company and the people, uh, in the meeting transcript.

**[20:26]** uh, in the meeting transcript.

**[20:26]** uh, in the meeting transcript. All right, here we go. Demo gods.

**[20:29]** All right, here we go. Demo gods.

**[20:29]** All right, here we go. Demo gods. Uh, before I start, any questions?

**[20:32]** Uh, before I start, any questions?

**[20:32]** Uh, before I start, any questions? Yeah, you

**[20:33]** Yeah, you

**[20:33]** Yeah, you mentioned some limitation on the number

**[20:34]** mentioned some limitation on the number

**[20:34]** mentioned some limitation on the number of agents.

**[20:37]** of agents.

**[20:37]** of agents. Yeah, so the the Genkit implementation

**[20:39]** Yeah, so the the Genkit implementation

**[20:39]** Yeah, so the the Genkit implementation that Google provide uh limits you to

**[20:42]** that Google provide uh limits you to

**[20:42]** that Google provide uh limits you to five maximum kind of sub agent calls uh

**[20:45]** five maximum kind of sub agent calls uh

**[20:45]** five maximum kind of sub agent calls uh per turn.

**[20:47]** per turn.

**[20:47]** per turn. Is that a hard?

**[20:49]** Is that a hard?

**[20:49]** Is that a hard? Yeah, I I couldn't get around it. The

**[20:52]** Yeah, I I couldn't get around it. The

**[20:52]** Yeah, I I couldn't get around it. The like there was this max like setting but

**[20:55]** like there was this max like setting but

**[20:56]** like there was this max like setting but it didn't work. Yeah. Yeah. So, it's

**[20:58]** it didn't work. Yeah. Yeah. So, it's

**[20:58]** it didn't work. Yeah. Yeah. So, it's something I'm sure they'll fix

**[20:59]** something I'm sure they'll fix

**[20:59]** something I'm sure they'll fix eventually. But, um, it it was an


### [21:00 - 22:00]

**[21:02]** eventually. But, um, it it was an

**[21:02]** eventually. But, um, it it was an interesting issue.

**[21:08]** All right. Let me see if my uh my code

**[21:08]** All right. Let me see if my uh my code is running.

**[21:11]** is running.

**[21:11]** is running. Yeah, I think it is. Yeah. So,

**[21:15]** Yeah, I think it is. Yeah. So,

**[21:15]** Yeah, I think it is. Yeah. So, it should be here. And actually, I'll

**[21:17]** it should be here. And actually, I'll

**[21:17]** it should be here. And actually, I'll show you the the MCP server as well

**[21:19]** show you the the MCP server as well

**[21:19]** show you the the MCP server as well while while I'm here.

**[21:23]** while while I'm here.

**[21:23]** while while I'm here. Yeah. So, this is the MCP inspector.

**[21:25]** Yeah. So, this is the MCP inspector.

**[21:25]** Yeah. So, this is the MCP inspector. It's um an open-source repo as part of

**[21:28]** It's um an open-source repo as part of

**[21:28]** It's um an open-source repo as part of the model. Sorry. Yeah. At the back.

**[21:39]** Yeah, that's actually in the agent card.

**[21:39]** Yeah, that's actually in the agent card. So that'll be in the index.ts of the of

**[21:42]** So that'll be in the index.ts of the of

**[21:42]** So that'll be in the index.ts of the of the sub agent. Yeah, I'll be going

**[21:44]** the sub agent. Yeah, I'll be going

**[21:44]** the sub agent. Yeah, I'll be going through the code in a little bit as well

**[21:45]** through the code in a little bit as well

**[21:45]** through the code in a little bit as well so you can see it. Um yeah, so I'm

**[21:48]** so you can see it. Um yeah, so I'm

**[21:48]** so you can see it. Um yeah, so I'm connecting to my Zapier MCP URL that I

**[21:51]** connecting to my Zapier MCP URL that I

**[21:51]** connecting to my Zapier MCP URL that I got. Um, so I just copied this one,

**[21:53]** got. Um, so I just copied this one,

**[21:53]** got. Um, so I just copied this one, dropped it in. Um, going to connect over

**[21:56]** dropped it in. Um, going to connect over

**[21:56]** dropped it in. Um, going to connect over SSE. Um, and this allows you to, you

**[21:59]** SSE. Um, and this allows you to, you

**[21:59]** SSE. Um, and this allows you to, you know, list the tools, call the tools.


### [22:00 - 23:00]

**[22:01]** know, list the tools, call the tools.

**[22:01]** know, list the tools, call the tools. Um, and it's quite interesting now that

**[22:03]** Um, and it's quite interesting now that

**[22:03]** Um, and it's quite interesting now that Zapier has added instructions, um, as a

**[22:06]** Zapier has added instructions, um, as a

**[22:06]** Zapier has added instructions, um, as a mandatory field on actually all of

**[22:08]** mandatory field on actually all of

**[22:08]** mandatory field on actually all of their, uh, MCP tools. Um, so you don't

**[22:12]** their, uh, MCP tools. Um, so you don't

**[22:12]** their, uh, MCP tools. Um, so you don't actually need to fill out the, uh, the

**[22:15]** actually need to fill out the, uh, the

**[22:15]** actually need to fill out the, uh, the fields anymore. So you can just give it

**[22:17]** fields anymore. So you can just give it

**[22:17]** fields anymore. So you can just give it natural language. So, this kind of

**[22:18]** natural language. So, this kind of

**[22:18]** natural language. So, this kind of suggests to me that they're using an LLM

**[22:21]** suggests to me that they're using an LLM

**[22:21]** suggests to me that they're using an LLM on their side to figure out how to

**[22:23]** on their side to figure out how to

**[22:23]** on their side to figure out how to populate the fields on your behalf. Um,

**[22:26]** populate the fields on your behalf. Um,

**[22:26]** populate the fields on your behalf. Um, which is interesting because it's going

**[22:27]** which is interesting because it's going

**[22:27]** which is interesting because it's going to cost them a fortune, right, as more

**[22:28]** to cost them a fortune, right, as more

**[22:28]** to cost them a fortune, right, as more people adopt it.

**[22:31]** people adopt it.

**[22:31]** people adopt it. All right, so this is the uh the agent

**[22:33]** All right, so this is the uh the agent

**[22:33]** All right, so this is the uh the agent dashboard. Let's just make sure

**[22:35]** dashboard. Let's just make sure

**[22:35]** dashboard. Let's just make sure everything's working. Yeah. Uh, you can

**[22:36]** everything's working. Yeah. Uh, you can

**[22:36]** everything's working. Yeah. Uh, you can see of a couple of previous ones that I

**[22:38]** see of a couple of previous ones that I

**[22:38]** see of a couple of previous ones that I ran. Um, this one is actually the one

**[22:41]** ran. Um, this one is actually the one

**[22:41]** ran. Um, this one is actually the one where the Slack uh thing wasn't found.

**[22:44]** where the Slack uh thing wasn't found.

**[22:44]** where the Slack uh thing wasn't found. So, when I was testing that, my mouse

**[22:47]** So, when I was testing that, my mouse

**[22:47]** So, when I was testing that, my mouse isn't moving. There we go. Um, yeah. So,

**[22:50]** isn't moving. There we go. Um, yeah. So,

**[22:50]** isn't moving. There we go. Um, yeah. So, I put in like a, you know, typical

**[22:53]** I put in like a, you know, typical

**[22:53]** I put in like a, you know, typical unknown uh Slack channel. Um, and then

**[22:55]** unknown uh Slack channel. Um, and then

**[22:55]** unknown uh Slack channel. Um, and then it it detected that it couldn't find it

**[22:58]** it it detected that it couldn't find it

**[22:58]** it it detected that it couldn't find it um based on the heristics.


### [23:00 - 24:00]

**[23:00]** um based on the heristics.

**[23:00]** um based on the heristics. Not sure why my mouse isn't moving.

**[23:02]** Not sure why my mouse isn't moving.

**[23:02]** Not sure why my mouse isn't moving. There we go.

**[23:07]** Yeah.

**[23:07]** Yeah. So, you have defined four agents here.

**[23:11]** So, you have defined four agents here.

**[23:11]** So, you have defined four agents here. Mhm.

**[23:12]** Mhm.

**[23:12]** Mhm. So,

**[23:14]** So,

**[23:14]** So, All 82A agents.

**[23:16]** All 82A agents.

**[23:16]** All 82A agents. Yeah, correct.

**[23:17]** Yeah, correct.

**[23:17]** Yeah, correct. Okay. So, maximum you can go for A2A

**[23:20]** Okay. So, maximum you can go for A2A

**[23:20]** Okay. So, maximum you can go for A2A agents is five.

**[23:22]** agents is five.

**[23:22]** agents is five. Yeah. Uh when when I got to five, that's

**[23:24]** Yeah. Uh when when I got to five, that's

**[23:24]** Yeah. Uh when when I got to five, that's when I got the error. Yeah. So, I think

**[23:26]** when I got the error. Yeah. So, I think

**[23:26]** when I got the error. Yeah. So, I think four. Um

**[23:28]** four. Um

**[23:28]** four. Um um Yeah. And the the host agent here.

**[23:30]** um Yeah. And the the host agent here.

**[23:30]** um Yeah. And the the host agent here. So, these are the host agent logs. Uh

**[23:33]** So, these are the host agent logs. Uh

**[23:33]** So, these are the host agent logs. Uh you can see it connecting to the the

**[23:35]** you can see it connecting to the the

**[23:35]** you can see it connecting to the the different agents. Uh this agent's just

**[23:37]** different agents. Uh this agent's just

**[23:37]** different agents. Uh this agent's just running on a little dinky uh EC2

**[23:40]** running on a little dinky uh EC2

**[23:40]** running on a little dinky uh EC2 instance that I spun up. Um, and it goes

**[23:42]** instance that I spun up. Um, and it goes

**[23:42]** instance that I spun up. Um, and it goes through, learns about the agents, you

**[23:44]** through, learns about the agents, you

**[23:44]** through, learns about the agents, you know, processes, web hooks, like you

**[23:47]** know, processes, web hooks, like you

**[23:47]** know, processes, web hooks, like you don't necessarily need to go in here

**[23:48]** don't necessarily need to go in here

**[23:48]** don't necessarily need to go in here unless you you get a failure. Um, Slack

**[23:51]** unless you you get a failure. Um, Slack

**[23:51]** unless you you get a failure. Um, Slack agent, pretty similar. Um, it's it's

**[23:54]** agent, pretty similar. Um, it's it's

**[23:54]** agent, pretty similar. Um, it's it's basically just sitting there waiting for

**[23:57]** basically just sitting there waiting for

**[23:57]** basically just sitting there waiting for another agent to connect. Uh, when the

**[23:59]** another agent to connect. Uh, when the

**[23:59]** another agent to connect. Uh, when the agent connects, it it uh communicates


### [24:00 - 25:00]

**[24:01]** agent connects, it it uh communicates

**[24:02]** agent connects, it it uh communicates with it. Uh, and you can see here the

**[24:03]** with it. Uh, and you can see here the

**[24:03]** with it. Uh, and you can see here the the bench agents running remotely. Um,

**[24:06]** the bench agents running remotely. Um,

**[24:06]** the bench agents running remotely. Um, the reason I don't have uh verbose logs

**[24:09]** the reason I don't have uh verbose logs

**[24:09]** the reason I don't have uh verbose logs here is because it's remote. it's not

**[24:11]** here is because it's remote. it's not

**[24:11]** here is because it's remote. it's not under my control, right? Um, so the A2A

**[24:13]** under my control, right? Um, so the A2A

**[24:13]** under my control, right? Um, so the A2A logs for that agent are actually on the

**[24:16]** logs for that agent are actually on the

**[24:16]** logs for that agent are actually on the EC2 server. Um, which kind of brings up

**[24:19]** EC2 server. Um, which kind of brings up

**[24:19]** EC2 server. Um, which kind of brings up another question about how do you debug

**[24:21]** another question about how do you debug

**[24:21]** another question about how do you debug when an A2 agent fails, right? Um, yeah.

**[24:25]** when an A2 agent fails, right? Um, yeah.

**[24:25]** when an A2 agent fails, right? Um, yeah. So then on the web hooks page, um, so

**[24:27]** So then on the web hooks page, um, so

**[24:27]** So then on the web hooks page, um, so this is the the only web hook that's

**[24:29]** this is the the only web hook that's

**[24:29]** this is the the only web hook that's preconfigured. Um, and this basically

**[24:32]** preconfigured. Um, and this basically

**[24:32]** preconfigured. Um, and this basically explains, you know, to the agent what

**[24:35]** explains, you know, to the agent what

**[24:35]** explains, you know, to the agent what it's actually going to do when this web

**[24:36]** it's actually going to do when this web

**[24:36]** it's actually going to do when this web hook arrives, right? Um, so it's going

**[24:38]** hook arrives, right? Um, so it's going

**[24:38]** hook arrives, right? Um, so it's going to process the incoming web hook. Um, we

**[24:41]** to process the incoming web hook. Um, we

**[24:41]** to process the incoming web hook. Um, we have a little prompt template here,

**[24:42]** have a little prompt template here,

**[24:42]** have a little prompt template here, right? So it, uh, tells it what the

**[24:44]** right? So it, uh, tells it what the

**[24:44]** right? So it, uh, tells it what the agent capabilities are, how to analyze

**[24:47]** agent capabilities are, how to analyze

**[24:47]** agent capabilities are, how to analyze it, right? Um, and then we have the

**[24:50]** it, right? Um, and then we have the

**[24:50]** it, right? Um, and then we have the processor config, right? And, and this

**[24:52]** processor config, right? And, and this

**[24:52]** processor config, right? And, and this just kind of tells, hey, these are the

**[24:54]** just kind of tells, hey, these are the

**[24:54]** just kind of tells, hey, these are the agents that you have access to as part

**[24:56]** agents that you have access to as part

**[24:56]** agents that you have access to as part of this uh, web hook. Um, this will

**[24:59]** of this uh, web hook. Um, this will

**[24:59]** of this uh, web hook. Um, this will become important when you've got, say, a


### [25:00 - 26:00]

**[25:01]** become important when you've got, say, a

**[25:01]** become important when you've got, say, a 100 A2A agents and you only want like

**[25:04]** 100 A2A agents and you only want like

**[25:04]** 100 A2A agents and you only want like two of them to to interact. Um, and then

**[25:08]** two of them to to interact. Um, and then

**[25:08]** two of them to to interact. Um, and then here we have a test. Um, so this is just

**[25:10]** here we have a test. Um, so this is just

**[25:10]** here we have a test. Um, so this is just a fake transcript that generated with a

**[25:13]** a fake transcript that generated with a

**[25:13]** a fake transcript that generated with a with an LMM. Um, and when we send the

**[25:16]** with an LMM. Um, and when we send the

**[25:16]** with an LMM. Um, and when we send the web hook, you can see here it's

**[25:18]** web hook, you can see here it's

**[25:18]** web hook, you can see here it's processing and hopefully the demo gods

**[25:20]** processing and hopefully the demo gods

**[25:20]** processing and hopefully the demo gods will will do me good here.

**[25:24]** will will do me good here.

**[25:24]** will will do me good here. And it does take a little bit of time,

**[25:25]** And it does take a little bit of time,

**[25:25]** And it does take a little bit of time, right? So the host agent has to process

**[25:27]** right? So the host agent has to process

**[25:27]** right? So the host agent has to process it, then has to reach out to the sub

**[25:29]** it, then has to reach out to the sub

**[25:29]** it, then has to reach out to the sub agents, you know, get all the

**[25:30]** agents, you know, get all the

**[25:30]** agents, you know, get all the information. Um, I think the the bench

**[25:33]** information. Um, I think the the bench

**[25:33]** information. Um, I think the the bench agent probably takes the longest because

**[25:35]** agent probably takes the longest because

**[25:35]** agent probably takes the longest because it's actually doing its own subtasks as

**[25:37]** it's actually doing its own subtasks as

**[25:37]** it's actually doing its own subtasks as well. Okay, we got a we got a Slack

**[25:39]** well. Okay, we got a we got a Slack

**[25:39]** well. Okay, we got a we got a Slack message. That's a good sign. Okay, so

**[25:41]** message. That's a good sign. Okay, so

**[25:42]** message. That's a good sign. Okay, so Snowflake is interested in Slack and

**[25:43]** Snowflake is interested in Slack and

**[25:43]** Snowflake is interested in Slack and GitHub integrations.

**[25:45]** GitHub integrations.

**[25:45]** GitHub integrations. Very cool. Um, we have the GitHub. So, I

**[25:50]** Very cool. Um, we have the GitHub. So, I

**[25:50]** Very cool. Um, we have the GitHub. So, I don't know why my mouse keeps freezing.

**[25:52]** don't know why my mouse keeps freezing.

**[25:52]** don't know why my mouse keeps freezing. There we go. Yes. So, we should have a

**[25:55]** There we go. Yes. So, we should have a

**[25:55]** There we go. Yes. So, we should have a GitHub issue.

**[25:58]** GitHub issue.

**[25:58]** GitHub issue. Here we go.


### [26:00 - 27:00]

**[26:00]** Here we go.

**[26:00]** Here we go. Yeah. So during the trial, the AI

**[26:02]** Yeah. So during the trial, the AI

**[26:02]** Yeah. So during the trial, the AI mclassified the severity of the bugs.

**[26:04]** mclassified the severity of the bugs.

**[26:04]** mclassified the severity of the bugs. Engineers need to investigate and fix

**[26:06]** Engineers need to investigate and fix

**[26:06]** Engineers need to investigate and fix the issue, right? So it's re really

**[26:08]** the issue, right? So it's re really

**[26:08]** the issue, right? So it's re really simple use case, but you can imagine

**[26:10]** simple use case, but you can imagine

**[26:10]** simple use case, but you can imagine that that transcript is probably going

**[26:12]** that that transcript is probably going

**[26:12]** that that transcript is probably going to be 10 times longer. You know, a lot

**[26:13]** to be 10 times longer. You know, a lot

**[26:13]** to be 10 times longer. You know, a lot more information in it. Um and and it

**[26:16]** more information in it. Um and and it

**[26:16]** more information in it. Um and and it will just work, right? Um and then we

**[26:19]** will just work, right? Um and then we

**[26:19]** will just work, right? Um and then we also have the bench agent. So um oh,

**[26:22]** also have the bench agent. So um oh,

**[26:22]** also have the bench agent. So um oh, looks like it's waiting for results. Um

**[26:24]** looks like it's waiting for results. Um

**[26:24]** looks like it's waiting for results. Um so it's going to research uh the

**[26:26]** so it's going to research uh the

**[26:26]** so it's going to research uh the company. Uh I think I did one before

**[26:28]** company. Uh I think I did one before

**[26:28]** company. Uh I think I did one before where it just returned a result. Let me

**[26:30]** where it just returned a result. Let me

**[26:30]** where it just returned a result. Let me see. Yeah. So it basically goes off does

**[26:34]** see. Yeah. So it basically goes off does

**[26:34]** see. Yeah. So it basically goes off does a research into Snowflake and all the

**[26:36]** a research into Snowflake and all the

**[26:36]** a research into Snowflake and all the participants of the call um and returns

**[26:39]** participants of the call um and returns

**[26:39]** participants of the call um and returns that information. Um and this can kind

**[26:41]** that information. Um and this can kind

**[26:41]** that information. Um and this can kind of get as complex or as simple as as you

**[26:43]** of get as complex or as simple as as you

**[26:43]** of get as complex or as simple as as you want it to be. Um and yeah, so when

**[26:47]** want it to be. Um and yeah, so when

**[26:47]** want it to be. Um and yeah, so when you're using the application and you

**[26:49]** you're using the application and you

**[26:49]** you're using the application and you have it up and running and has anybody

**[26:51]** have it up and running and has anybody

**[26:51]** have it up and running and has anybody managed to get it up and running?

**[26:54]** managed to get it up and running?

**[26:54]** managed to get it up and running? Wow, impressive.


### [27:00 - 28:00]

**[27:01]** Yeah question you're using bench agent

**[27:01]** Yeah question you're using bench agent to do the orchestration that's why

**[27:03]** to do the orchestration that's why

**[27:03]** to do the orchestration that's why you're having it right

**[27:05]** you're having it right

**[27:05]** you're having it right uh no so the bench agent is just like

**[27:07]** uh no so the bench agent is just like

**[27:07]** uh no so the bench agent is just like think of it as a third party agent that

**[27:09]** think of it as a third party agent that

**[27:09]** think of it as a third party agent that we can leverage so that the host agent

**[27:11]** we can leverage so that the host agent

**[27:11]** we can leverage so that the host agent is doing all the orchestration

**[27:14]** is doing all the orchestration

**[27:14]** is doing all the orchestration okay so like what is the actual role

**[27:17]** okay so like what is the actual role

**[27:17]** okay so like what is the actual role that agent is playing like what is it

**[27:18]** that agent is playing like what is it

**[27:18]** that agent is playing like what is it actually doing

**[27:20]** actually doing

**[27:20]** actually doing it's doing research on companies and

**[27:22]** it's doing research on companies and

**[27:22]** it's doing research on companies and people

**[27:25]** people

**[27:25]** people just another agent.

**[27:26]** just another agent.

**[27:26]** just another agent. Yeah. So, it's an agent with a load of

**[27:28]** Yeah. So, it's an agent with a load of

**[27:28]** Yeah. So, it's an agent with a load of different capabilities and it's it's

**[27:30]** different capabilities and it's it's

**[27:30]** different capabilities and it's it's basically just um

**[27:31]** basically just um

**[27:31]** basically just um orchestrator isn't local.

**[27:35]** orchestrator isn't local.

**[27:35]** orchestrator isn't local. Yeah. Theo so the these three hosts

**[27:37]** Yeah. Theo so the these three hosts

**[27:37]** Yeah. Theo so the these three hosts Slack and GitHub are all local.

**[27:39]** Slack and GitHub are all local.

**[27:39]** Slack and GitHub are all local. Yeah. I was like I think I thought

**[27:42]** Yeah. I was like I think I thought

**[27:42]** Yeah. I was like I think I thought orchestration.

**[27:45]** orchestration.

**[27:45]** orchestration. Yeah. No, Bench is just a um like it's

**[27:48]** Yeah. No, Bench is just a um like it's

**[27:48]** Yeah. No, Bench is just a um like it's in the repo but um you need an API key

**[27:50]** in the repo but um you need an API key

**[27:50]** in the repo but um you need an API key for it and um we're we're launching in

**[27:52]** for it and um we're we're launching in

**[27:52]** for it and um we're we're launching in about two weeks. So uh I just made it

**[27:54]** about two weeks. So uh I just made it

**[27:54]** about two weeks. So uh I just made it remote for the for the purposes of the

**[27:56]** remote for the for the purposes of the

**[27:56]** remote for the for the purposes of the demo. Um

**[27:58]** demo. Um

**[27:58]** demo. Um so what about the host agent though?


### [28:00 - 29:00]

**[28:00]** so what about the host agent though?

**[28:00]** so what about the host agent though? Sorry,

**[28:01]** Sorry,

**[28:01]** Sorry, the host agent is it uh the zap year

**[28:03]** the host agent is it uh the zap year

**[28:03]** the host agent is it uh the zap year agent or

**[28:04]** agent or

**[28:04]** agent or no? So the the so all of these agents

**[28:07]** no? So the the so all of these agents

**[28:07]** no? So the the so all of these agents are A2A agents. Um the Slack agent and

**[28:10]** are A2A agents. Um the Slack agent and

**[28:10]** are A2A agents. Um the Slack agent and the GitHub agent have MCP tools to Slack

**[28:13]** the GitHub agent have MCP tools to Slack

**[28:13]** the GitHub agent have MCP tools to Slack and GitHub through Zapier. Yeah. Um I

**[28:17]** and GitHub through Zapier. Yeah. Um I

**[28:17]** and GitHub through Zapier. Yeah. Um I can actually show you a diagram that

**[28:20]** can actually show you a diagram that

**[28:20]** can actually show you a diagram that might might explain it a bit better.

**[28:30]** Yeah. I don't know if that explains it

**[28:30]** Yeah. I don't know if that explains it better, but

**[28:32]** better, but

**[28:32]** better, but but the orchestration does happen on

**[28:33]** but the orchestration does happen on

**[28:33]** but the orchestration does happen on your local.

**[28:34]** your local.

**[28:34]** your local. Yeah. Yeah. Everything's happening on my

**[28:36]** Yeah. Yeah. Everything's happening on my

**[28:36]** Yeah. Yeah. Everything's happening on my local. So, if I go into the into the

**[28:38]** local. So, if I go into the into the

**[28:38]** local. So, if I go into the into the codebase, uh have the agent logs.

**[28:42]** codebase, uh have the agent logs.

**[28:42]** codebase, uh have the agent logs. Um so, this is all happening here,

**[28:44]** Um so, this is all happening here,

**[28:44]** Um so, this is all happening here, right? So, it's sent to Slack to T or

**[28:47]** right? So, it's sent to Slack to T or

**[28:47]** right? So, it's sent to Slack to T or is that readable? I go one more.


### [29:00 - 30:00]

**[29:00]** Yeah. Yeah. So you can see here the

**[29:00]** Yeah. Yeah. So you can see here the transcript came in um and then it got a

**[29:03]** transcript came in um and then it got a

**[29:03]** transcript came in um and then it got a response from each of the sub agents and

**[29:05]** response from each of the sub agents and

**[29:05]** response from each of the sub agents and then completed them and it did all of

**[29:07]** then completed them and it did all of

**[29:07]** then completed them and it did all of this in parallel as well, right? Um

**[29:10]** this in parallel as well, right? Um

**[29:10]** this in parallel as well, right? Um sorry, is that a question?

**[29:11]** sorry, is that a question?

**[29:11]** sorry, is that a question? Yes.

**[29:12]** Yes.

**[29:12]** Yes. So in your example here, which agent

**[29:15]** So in your example here, which agent

**[29:15]** So in your example here, which agent would handle human confirmation? Let's

**[29:17]** would handle human confirmation? Let's

**[29:17]** would handle human confirmation? Let's say we want to have a create the test

**[29:21]** say we want to have a create the test

**[29:21]** say we want to have a create the test button in spec here. Which agent would

**[29:23]** button in spec here. Which agent would

**[29:23]** button in spec here. Which agent would handle that part? Do you create a new

**[29:26]** handle that part? Do you create a new

**[29:26]** handle that part? Do you create a new agent for human confirmations? Do you

**[29:28]** agent for human confirmations? Do you

**[29:28]** agent for human confirmations? Do you keep the old one?

**[29:29]** keep the old one?

**[29:30]** keep the old one? Yes, you need a staging area for for

**[29:32]** Yes, you need a staging area for for

**[29:32]** Yes, you need a staging area for for actions. Um, so it's not something I've

**[29:34]** actions. Um, so it's not something I've

**[29:34]** actions. Um, so it's not something I've built into this. Um, there's a lot more

**[29:36]** built into this. Um, there's a lot more

**[29:36]** built into this. Um, there's a lot more you could do here. Um, but human

**[29:38]** you could do here. Um, but human

**[29:38]** you could do here. Um, but human confirmation would typ typically be done

**[29:41]** confirmation would typ typically be done

**[29:41]** confirmation would typ typically be done through like a draft, right? So you

**[29:43]** through like a draft, right? So you

**[29:43]** through like a draft, right? So you would maybe pop up a Slack message with

**[29:45]** would maybe pop up a Slack message with

**[29:45]** would maybe pop up a Slack message with some actions. Um, and then when somebody

**[29:47]** some actions. Um, and then when somebody

**[29:48]** some actions. Um, and then when somebody clicks that, it would communicate back

**[29:49]** clicks that, it would communicate back

**[29:49]** clicks that, it would communicate back kind of like a secondary pass web hook.

**[29:52]** kind of like a secondary pass web hook.

**[29:52]** kind of like a secondary pass web hook. Uh, you might need to persist state

**[29:53]** Uh, you might need to persist state

**[29:53]** Uh, you might need to persist state though. Yeah.

**[29:55]** though. Yeah.

**[29:55]** though. Yeah. Yeah. How do you consider the security

**[29:58]** Yeah. How do you consider the security

**[29:58]** Yeah. How do you consider the security of this endpoint controls of different


### [30:00 - 31:00]

**[30:02]** of this endpoint controls of different

**[30:02]** of this endpoint controls of different vendors communicating from endpoint?

**[30:05]** vendors communicating from endpoint?

**[30:05]** vendors communicating from endpoint? How do you manage the security?

**[30:08]** How do you manage the security?

**[30:08]** How do you manage the security? Yeah. So, as a part of the A2A spec,

**[30:09]** Yeah. So, as a part of the A2A spec,

**[30:09]** Yeah. So, as a part of the A2A spec, you're going to have some sort of

**[30:11]** you're going to have some sort of

**[30:11]** you're going to have some sort of authentication, right? Um I've just

**[30:13]** authentication, right? Um I've just

**[30:13]** authentication, right? Um I've just exposed everything, right? Like it won't

**[30:15]** exposed everything, right? Like it won't

**[30:15]** exposed everything, right? Like it won't exist tomorrow. So, there there's no

**[30:16]** exist tomorrow. So, there there's no

**[30:16]** exist tomorrow. So, there there's no security implic implications. Um, but

**[30:19]** security implic implications. Um, but

**[30:19]** security implic implications. Um, but essentially you're going to you probably

**[30:21]** essentially you're going to you probably

**[30:21]** essentially you're going to you probably have to have a subscription with the

**[30:23]** have to have a subscription with the

**[30:23]** have to have a subscription with the company that's providing that A2A agent.

**[30:25]** company that's providing that A2A agent.

**[30:25]** company that's providing that A2A agent. Uh, because it is consuming tokens,

**[30:27]** Uh, because it is consuming tokens,

**[30:27]** Uh, because it is consuming tokens, right?

**[30:30]** right?

**[30:30]** right? Um, I'm I'm not sure exactly what A2A

**[30:32]** Um, I'm I'm not sure exactly what A2A

**[30:32]** Um, I'm I'm not sure exactly what A2A have in plan. Uh, it's still pretty

**[30:34]** have in plan. Uh, it's still pretty

**[30:34]** have in plan. Uh, it's still pretty early days, but um, with MCP, it's a

**[30:37]** early days, but um, with MCP, it's a

**[30:37]** early days, but um, with MCP, it's a little bit further ahead. It has OT uh,

**[30:39]** little bit further ahead. It has OT uh,

**[30:39]** little bit further ahead. It has OT uh, header authentication, things like that.

**[30:41]** header authentication, things like that.

**[30:41]** header authentication, things like that. So, imagine something similar. And how

**[30:43]** So, imagine something similar. And how

**[30:43]** So, imagine something similar. And how about CISA governance like LM firewall

**[30:47]** about CISA governance like LM firewall

**[30:47]** about CISA governance like LM firewall all those uh benchmarking

**[30:50]** all those uh benchmarking

**[30:50]** all those uh benchmarking autobenchmarking

**[30:52]** autobenchmarking

**[30:52]** autobenchmarking and u also the guard rails etc you do

**[30:57]** and u also the guard rails etc you do

**[30:57]** and u also the guard rails etc you do you have a separate agent or everything

**[30:59]** you have a separate agent or everything

**[30:59]** you have a separate agent or everything is being


### [31:00 - 32:00]

**[31:00]** is being

**[31:00]** is being you you'd probably manage that on like

**[31:02]** you you'd probably manage that on like

**[31:02]** you you'd probably manage that on like an Amazon bedrock or something like that

**[31:04]** an Amazon bedrock or something like that

**[31:04]** an Amazon bedrock or something like that right and you would just you know use

**[31:06]** right and you would just you know use

**[31:06]** right and you would just you know use that guardrailed LLM um from behind

**[31:09]** that guardrailed LLM um from behind

**[31:09]** that guardrailed LLM um from behind there you don't have to use Gemini here

**[31:11]** there you don't have to use Gemini here

**[31:11]** there you don't have to use Gemini here either

**[31:13]** either

**[31:13]** either Yeah.

**[31:24]** And then that host agent is kind of like

**[31:24]** And then that host agent is kind of like the planner and each um do you see like

**[31:30]** the planner and each um do you see like

**[31:30]** the planner and each um do you see like becoming like a talking to each other?

**[31:33]** becoming like a talking to each other?

**[31:33]** becoming like a talking to each other? Um

**[31:34]** Um

**[31:34]** Um um I guess you could but I I don't know

**[31:37]** um I guess you could but I I don't know

**[31:37]** um I guess you could but I I don't know if that's the intention, right? like um

**[31:40]** if that's the intention, right? like um

**[31:40]** if that's the intention, right? like um then they just become hosts, right? When

**[31:42]** then they just become hosts, right? When

**[31:42]** then they just become hosts, right? When they talk to each other, um like if you

**[31:46]** they talk to each other, um like if you

**[31:46]** they talk to each other, um like if you think about it, like if you have no

**[31:48]** think about it, like if you have no

**[31:48]** think about it, like if you have no knowledge of sub agents, um how would

**[31:52]** knowledge of sub agents, um how would

**[31:52]** knowledge of sub agents, um how would you how would you know to talk to them,

**[31:54]** you how would you know to talk to them,

**[31:54]** you how would you know to talk to them, right? You would have to then become a

**[31:55]** right? You would have to then become a

**[31:56]** right? You would have to then become a host agent yourself, connect to that

**[31:58]** host agent yourself, connect to that

**[31:58]** host agent yourself, connect to that other sub agent to to do that. So I I


### [32:00 - 33:00]

**[32:01]** other sub agent to to do that. So I I

**[32:01]** other sub agent to to do that. So I I don't know if that's intended in the A2A

**[32:03]** don't know if that's intended in the A2A

**[32:03]** don't know if that's intended in the A2A spec for sub agents to communicate.

**[32:06]** spec for sub agents to communicate.

**[32:06]** spec for sub agents to communicate. Yeah. So with the host agent um and the

**[32:09]** Yeah. So with the host agent um and the

**[32:09]** Yeah. So with the host agent um and the orchestration that it's doing is it

**[32:11]** orchestration that it's doing is it

**[32:11]** orchestration that it's doing is it actually managing a combination of all

**[32:13]** actually managing a combination of all

**[32:13]** actually managing a combination of all the context windows or like do you hit a

**[32:17]** the context windows or like do you hit a

**[32:17]** the context windows or like do you hit a limit quickly?

**[32:18]** limit quickly?

**[32:18]** limit quickly? Yeah, so all of the context windows and

**[32:20]** Yeah, so all of the context windows and

**[32:20]** Yeah, so all of the context windows and this kind of uh is something I'm going

**[32:22]** this kind of uh is something I'm going

**[32:22]** this kind of uh is something I'm going to cover now in a second as well. Let me

**[32:24]** to cover now in a second as well. Let me

**[32:24]** to cover now in a second as well. Let me uh just go back to the slides

**[32:27]** uh just go back to the slides

**[32:27]** uh just go back to the slides um which is a good it's a good segue.

**[32:31]** um which is a good it's a good segue.

**[32:31]** um which is a good it's a good segue. Um so yeah, one one of the benefits of

**[32:35]** Um so yeah, one one of the benefits of

**[32:35]** Um so yeah, one one of the benefits of like A2A or or any sort of sub agent uh

**[32:38]** like A2A or or any sort of sub agent uh

**[32:38]** like A2A or or any sort of sub agent uh framework is that you're you're not

**[32:41]** framework is that you're you're not

**[32:41]** framework is that you're you're not consuming um the tool results into your

**[32:43]** consuming um the tool results into your

**[32:44]** consuming um the tool results into your context, right? So like when you say hey

**[32:46]** context, right? So like when you say hey

**[32:46]** context, right? So like when you say hey you know um and I think of an example

**[32:49]** you know um and I think of an example

**[32:49]** you know um and I think of an example later on but if if you have a load of uh

**[32:51]** later on but if if you have a load of uh

**[32:51]** later on but if if you have a load of uh Slack messages or GitHub issues or

**[32:53]** Slack messages or GitHub issues or

**[32:53]** Slack messages or GitHub issues or Salesforce opportunities and you want to

**[32:56]** Salesforce opportunities and you want to

**[32:56]** Salesforce opportunities and you want to analyze them and maybe produce like you

**[32:58]** analyze them and maybe produce like you

**[32:58]** analyze them and maybe produce like you know summary of categories and counts


### [33:00 - 34:00]

**[33:01]** know summary of categories and counts

**[33:01]** know summary of categories and counts and the only thing your host agent cares

**[33:03]** and the only thing your host agent cares

**[33:03]** and the only thing your host agent cares about is the summary of categories and

**[33:05]** about is the summary of categories and

**[33:05]** about is the summary of categories and accounts. It doesn't care about the like

**[33:08]** accounts. It doesn't care about the like

**[33:08]** accounts. It doesn't care about the like individual details right because those

**[33:10]** individual details right because those

**[33:10]** individual details right because those have already been processed by the sub

**[33:11]** have already been processed by the sub

**[33:11]** have already been processed by the sub agent. So the sub agents context gets

**[33:14]** agent. So the sub agents context gets

**[33:14]** agent. So the sub agents context gets big, not very big, but like as big as

**[33:16]** big, not very big, but like as big as

**[33:16]** big, not very big, but like as big as the task demands and the host agent only

**[33:19]** the task demands and the host agent only

**[33:19]** the task demands and the host agent only incrementally grows by the the business

**[33:21]** incrementally grows by the the business

**[33:21]** incrementally grows by the the business value it got from that agent. Um like

**[33:25]** value it got from that agent. Um like

**[33:25]** value it got from that agent. Um like one of the challenges at bench is you

**[33:26]** one of the challenges at bench is you

**[33:26]** one of the challenges at bench is you know we have so many tools right like

**[33:28]** know we have so many tools right like

**[33:28]** know we have so many tools right like the context can blow up very quick. Um

**[33:31]** the context can blow up very quick. Um

**[33:31]** the context can blow up very quick. Um so you know very early on we decided

**[33:33]** so you know very early on we decided

**[33:33]** so you know very early on we decided okay we need to have composability. Um

**[33:35]** okay we need to have composability. Um

**[33:35]** okay we need to have composability. Um so that means that bench can create its

**[33:38]** so that means that bench can create its

**[33:38]** so that means that bench can create its own internal bench agent um to avoid

**[33:41]** own internal bench agent um to avoid

**[33:41]** own internal bench agent um to avoid that context growth problem. Um and

**[33:43]** that context growth problem. Um and

**[33:43]** that context growth problem. Um and we're even thinking of going one step

**[33:44]** we're even thinking of going one step

**[33:44]** we're even thinking of going one step further whereas like you know should we

**[33:46]** further whereas like you know should we

**[33:46]** further whereas like you know should we have an agent for every single tool um

**[33:48]** have an agent for every single tool um

**[33:48]** have an agent for every single tool um so that every single tool is protected

**[33:50]** so that every single tool is protected

**[33:50]** so that every single tool is protected from the primary uh prompt. Um so you

**[33:54]** from the primary uh prompt. Um so you

**[33:54]** from the primary uh prompt. Um so you know as you add more tools like the tool

**[33:57]** know as you add more tools like the tool

**[33:57]** know as you add more tools like the tool definitions themselves I think we're up

**[33:58]** definitions themselves I think we're up

**[33:58]** definitions themselves I think we're up to like you know 10,000 tokens just for


### [34:00 - 35:00]

**[34:01]** to like you know 10,000 tokens just for

**[34:01]** to like you know 10,000 tokens just for tool definitions alone. Um, I added the

**[34:04]** tool definitions alone. Um, I added the

**[34:04]** tool definitions alone. Um, I added the Asana MCP. It added 11,000 more tokens,

**[34:07]** Asana MCP. It added 11,000 more tokens,

**[34:07]** Asana MCP. It added 11,000 more tokens, right? So, like, you know, a lot of

**[34:09]** right? So, like, you know, a lot of

**[34:09]** right? So, like, you know, a lot of these MCP servers like they're, you

**[34:10]** these MCP servers like they're, you

**[34:10]** these MCP servers like they're, you know, they're giving you a lot of

**[34:12]** know, they're giving you a lot of

**[34:12]** know, they're giving you a lot of information. Um, and you may not

**[34:14]** information. Um, and you may not

**[34:14]** information. Um, and you may not actually want that. Uh, and that's

**[34:16]** actually want that. Uh, and that's

**[34:16]** actually want that. Uh, and that's actually one of the challenges with

**[34:17]** actually one of the challenges with

**[34:17]** actually one of the challenges with firstparty MCPs is they expose all their

**[34:20]** firstparty MCPs is they expose all their

**[34:20]** firstparty MCPs is they expose all their tools and that's one of the benefits of

**[34:22]** tools and that's one of the benefits of

**[34:22]** tools and that's one of the benefits of Zapier where you can pick and choose

**[34:23]** Zapier where you can pick and choose

**[34:23]** Zapier where you can pick and choose which tool you want to use.

**[34:26]** which tool you want to use.

**[34:26]** which tool you want to use. Yeah.

**[34:26]** Yeah.

**[34:26]** Yeah. Yeah. I was just going to ask why do we

**[34:28]** Yeah. I was just going to ask why do we

**[34:28]** Yeah. I was just going to ask why do we need Zapier?

**[34:30]** need Zapier?

**[34:30]** need Zapier? Zapier is just a really easy way to to

**[34:33]** Zapier is just a really easy way to to

**[34:33]** Zapier is just a really easy way to to use uh MCP right now. Um I think like

**[34:37]** use uh MCP right now. Um I think like

**[34:37]** use uh MCP right now. Um I think like Linear uh Asana um um a few others have

**[34:42]** Linear uh Asana um um a few others have

**[34:42]** Linear uh Asana um um a few others have added like first party MCP servers that

**[34:44]** added like first party MCP servers that

**[34:44]** added like first party MCP servers that are much better than what Zapier

**[34:46]** are much better than what Zapier

**[34:46]** are much better than what Zapier exposes.

**[34:52]** Yeah. So, so why does context size

**[34:52]** Yeah. So, so why does context size matter? Um, so AI agents accumulate

**[34:55]** matter? Um, so AI agents accumulate

**[34:56]** matter? Um, so AI agents accumulate context like as they work and you're

**[34:59]** context like as they work and you're

**[34:59]** context like as they work and you're supposed to keep like all of your tool


### [35:00 - 36:00]

**[35:01]** supposed to keep like all of your tool

**[35:01]** supposed to keep like all of your tool calls, right? What you sent to the to

**[35:04]** calls, right? What you sent to the to

**[35:04]** calls, right? What you sent to the to the tool and what you got back, you're

**[35:05]** the tool and what you got back, you're

**[35:06]** the tool and what you got back, you're supposed to keep that in your context so

**[35:07]** supposed to keep that in your context so

**[35:07]** supposed to keep that in your context so that later on if you, you know, ask a

**[35:10]** that later on if you, you know, ask a

**[35:10]** that later on if you, you know, ask a follow-up question, it still has access

**[35:12]** follow-up question, it still has access

**[35:12]** follow-up question, it still has access to that data. Um, and that becomes very

**[35:15]** to that data. Um, and that becomes very

**[35:15]** to that data. Um, and that becomes very challenging, right? So you've kind of

**[35:16]** challenging, right? So you've kind of

**[35:16]** challenging, right? So you've kind of got two options. is like, okay, do I

**[35:18]** got two options. is like, okay, do I

**[35:18]** got two options. is like, okay, do I just prune, you know, old tool calls and

**[35:20]** just prune, you know, old tool calls and

**[35:20]** just prune, you know, old tool calls and now the the agent gets dumb or, you

**[35:23]** now the the agent gets dumb or, you

**[35:23]** now the the agent gets dumb or, you know, do I figure out some other way to

**[35:24]** know, do I figure out some other way to

**[35:24]** know, do I figure out some other way to do it? Um, and cost is a big challenge,

**[35:28]** do it? Um, and cost is a big challenge,

**[35:28]** do it? Um, and cost is a big challenge, especially when you're doing prompt

**[35:30]** especially when you're doing prompt

**[35:30]** especially when you're doing prompt caching. Um, so with prompt caching, it

**[35:32]** caching. Um, so with prompt caching, it

**[35:32]** caching. Um, so with prompt caching, it it enables you to essentially put a

**[35:35]** it enables you to essentially put a

**[35:35]** it enables you to essentially put a marker in your context and say, hey,

**[35:37]** marker in your context and say, hey,

**[35:37]** marker in your context and say, hey, look, when I make my next request, I

**[35:39]** look, when I make my next request, I

**[35:39]** look, when I make my next request, I want everything in my in my context so

**[35:41]** want everything in my in my context so

**[35:41]** want everything in my in my context so far uh to be cached so that I'm not

**[35:43]** far uh to be cached so that I'm not

**[35:44]** far uh to be cached so that I'm not going to get charged for it. Um but the

**[35:46]** going to get charged for it. Um but the

**[35:46]** going to get charged for it. Um but the cost to actually push that into the

**[35:48]** cost to actually push that into the

**[35:48]** cost to actually push that into the cache uh is about threex the cost of of

**[35:51]** cache uh is about threex the cost of of

**[35:51]** cache uh is about threex the cost of of making a single request with that

**[35:52]** making a single request with that

**[35:52]** making a single request with that context. Um so that means that you have

**[35:54]** context. Um so that means that you have

**[35:54]** context. Um so that means that you have to be very you know diligent in what

**[35:56]** to be very you know diligent in what

**[35:56]** to be very you know diligent in what sort of uh context management strategies

**[35:59]** sort of uh context management strategies

**[35:59]** sort of uh context management strategies you use. Um you know I was running


### [36:00 - 37:00]

**[36:01]** you use. Um you know I was running

**[36:01]** you use. Um you know I was running simulations cuz I I couldn't really

**[36:03]** simulations cuz I I couldn't really

**[36:03]** simulations cuz I I couldn't really figure out like what is the optimal um

**[36:07]** figure out like what is the optimal um

**[36:07]** figure out like what is the optimal um you know caching uh strategy. Uh so I

**[36:09]** you know caching uh strategy. Uh so I

**[36:09]** you know caching uh strategy. Uh so I ran simulations based on usage data um

**[36:12]** ran simulations based on usage data um

**[36:12]** ran simulations based on usage data um of like you know what's the typical

**[36:14]** of like you know what's the typical

**[36:14]** of like you know what's the typical context growth how many turns you know

**[36:16]** context growth how many turns you know

**[36:16]** context growth how many turns you know on average like what percentage of of

**[36:18]** on average like what percentage of of

**[36:18]** on average like what percentage of of users only send one turn right should we

**[36:21]** users only send one turn right should we

**[36:21]** users only send one turn right should we should we cach that one turn if they

**[36:23]** should we cach that one turn if they

**[36:23]** should we cach that one turn if they never ask another question right

**[36:24]** never ask another question right

**[36:24]** never ask another question right probably not. Um so you know it probably

**[36:27]** probably not. Um so you know it probably

**[36:28]** probably not. Um so you know it probably gets down to the actual you user level.

**[36:30]** gets down to the actual you user level.

**[36:30]** gets down to the actual you user level. So, if you have a user that always like

**[36:33]** So, if you have a user that always like

**[36:33]** So, if you have a user that always like puts in new prompts into the same chat

**[36:35]** puts in new prompts into the same chat

**[36:35]** puts in new prompts into the same chat and never opens a new session, um you're

**[36:38]** and never opens a new session, um you're

**[36:38]** and never opens a new session, um you're probably going to want to, you know,

**[36:39]** probably going to want to, you know,

**[36:39]** probably going to want to, you know, continuously uh cache their context. Uh

**[36:41]** continuously uh cache their context. Uh

**[36:41]** continuously uh cache their context. Uh but you might have another user who

**[36:43]** but you might have another user who

**[36:43]** but you might have another user who always creates a new session for every

**[36:45]** always creates a new session for every

**[36:45]** always creates a new session for every question. Um and then just figuring out

**[36:47]** question. Um and then just figuring out

**[36:47]** question. Um and then just figuring out like, you know, what is the context

**[36:49]** like, you know, what is the context

**[36:49]** like, you know, what is the context growth? Uh I think we figured out was

**[36:51]** growth? Uh I think we figured out was

**[36:51]** growth? Uh I think we figured out was around 30,000 tokens was the optimal um

**[36:55]** around 30,000 tokens was the optimal um

**[36:55]** around 30,000 tokens was the optimal um kind of across the board for everybody.

**[36:57]** kind of across the board for everybody.

**[36:57]** kind of across the board for everybody. Um, but that also comes up with false


### [37:00 - 38:00]

**[37:00]** Um, but that also comes up with false

**[37:00]** Um, but that also comes up with false positives. So sometimes you can end up

**[37:02]** positives. So sometimes you can end up

**[37:02]** positives. So sometimes you can end up caching the last turn of of a

**[37:04]** caching the last turn of of a

**[37:04]** caching the last turn of of a conversation. Um, and and that's going

**[37:06]** conversation. Um, and and that's going

**[37:06]** conversation. Um, and and that's going to, you know, cost you a lot more than

**[37:08]** to, you know, cost you a lot more than

**[37:08]** to, you know, cost you a lot more than it than it should naturally.

**[37:14]** Yeah. So the the great thing about the

**[37:14]** Yeah. So the the great thing about the sub agents, right, it protects them. And

**[37:16]** sub agents, right, it protects them. And

**[37:16]** sub agents, right, it protects them. And this was the GitHub kind of example I

**[37:18]** this was the GitHub kind of example I

**[37:18]** this was the GitHub kind of example I was giving you. Um, but this applies to

**[37:19]** was giving you. Um, but this applies to

**[37:19]** was giving you. Um, but this applies to pretty much every uh tool. So, like if

**[37:22]** pretty much every uh tool. So, like if

**[37:22]** pretty much every uh tool. So, like if you're ever integrating with a system,

**[37:25]** you're ever integrating with a system,

**[37:25]** you're ever integrating with a system, you're probably going to run into issues

**[37:26]** you're probably going to run into issues

**[37:26]** you're probably going to run into issues like why do I have to call, you know,

**[37:28]** like why do I have to call, you know,

**[37:28]** like why do I have to call, you know, list Slack channels every time to get

**[37:31]** list Slack channels every time to get

**[37:31]** list Slack channels every time to get the channel ID for the channel name that

**[37:33]** the channel ID for the channel name that

**[37:33]** the channel ID for the channel name that was provided, right? Cuz like nobody's

**[37:35]** was provided, right? Cuz like nobody's

**[37:35]** was provided, right? Cuz like nobody's going to provide like in a chat the

**[37:37]** going to provide like in a chat the

**[37:37]** going to provide like in a chat the channel ID that they want to post,

**[37:38]** channel ID that they want to post,

**[37:38]** channel ID that they want to post, right? It's a it's a UID. It's it's not

**[37:41]** right? It's a it's a UID. It's it's not

**[37:41]** right? It's a it's a UID. It's it's not memorable. Um, so then you get into the

**[37:43]** memorable. Um, so then you get into the

**[37:43]** memorable. Um, so then you get into the question of, okay, well, do I just cache

**[37:45]** question of, okay, well, do I just cache

**[37:45]** question of, okay, well, do I just cache the list of channels and and when do I

**[37:47]** the list of channels and and when do I

**[37:48]** the list of channels and and when do I update that list of channels, right?

**[37:49]** update that list of channels, right?

**[37:49]** update that list of channels, right? like what if the channel was deleted,

**[37:51]** like what if the channel was deleted,

**[37:51]** like what if the channel was deleted, renamed or a new channel was added. Um

**[37:55]** renamed or a new channel was added. Um

**[37:55]** renamed or a new channel was added. Um yeah, and then the the cost is is really

**[37:58]** yeah, and then the the cost is is really

**[37:58]** yeah, and then the the cost is is really probably the biggest one. Um yeah, so


### [38:00 - 39:00]

**[38:01]** probably the biggest one. Um yeah, so

**[38:01]** probably the biggest one. Um yeah, so the the benefits of this lean context,

**[38:03]** the the benefits of this lean context,

**[38:03]** the the benefits of this lean context, right? So your sub agents have that

**[38:05]** right? So your sub agents have that

**[38:05]** right? So your sub agents have that isolated context and and that really

**[38:08]** isolated context and and that really

**[38:08]** isolated context and and that really just allows you to um be be super like

**[38:11]** just allows you to um be be super like

**[38:12]** just allows you to um be be super like fast, low latency, low cost. Um, and if

**[38:15]** fast, low latency, low cost. Um, and if

**[38:15]** fast, low latency, low cost. Um, and if you ever need to go back to ask another

**[38:19]** you ever need to go back to ask another

**[38:19]** you ever need to go back to ask another question, you know, you're going to like

**[38:21]** question, you know, you're going to like

**[38:21]** question, you know, you're going to like spawn that uh process again, right? Um,

**[38:24]** spawn that uh process again, right? Um,

**[38:24]** spawn that uh process again, right? Um, so maybe if you're in control of these

**[38:26]** so maybe if you're in control of these

**[38:26]** so maybe if you're in control of these other agents, you you might want to have

**[38:28]** other agents, you you might want to have

**[38:28]** other agents, you you might want to have some sort of like uh I don't know five

**[38:31]** some sort of like uh I don't know five

**[38:31]** some sort of like uh I don't know five minute TTL on previous questions, right?

**[38:34]** minute TTL on previous questions, right?

**[38:34]** minute TTL on previous questions, right? Um, and then yeah, the host agent only

**[38:38]** Um, and then yeah, the host agent only

**[38:38]** Um, and then yeah, the host agent only processes the summaries. Um, and the raw

**[38:40]** processes the summaries. Um, and the raw

**[38:40]** processes the summaries. Um, and the raw data is discarded after processing.

**[38:43]** data is discarded after processing.

**[38:43]** data is discarded after processing. Um, yeah. So, I'm going to jump back

**[38:46]** Um, yeah. So, I'm going to jump back

**[38:46]** Um, yeah. So, I'm going to jump back into the code here. Uh,

**[38:49]** into the code here. Uh,

**[38:49]** into the code here. Uh, just kind of walk you through

**[38:52]** just kind of walk you through

**[38:52]** just kind of walk you through uh how it all works.


### [39:00 - 40:00]

**[39:01]** All right, we'll start with the host

**[39:01]** All right, we'll start with the host agent and and you notice a few other

**[39:03]** agent and and you notice a few other

**[39:04]** agent and and you notice a few other things, right? So, there's MCP. This is

**[39:05]** things, right? So, there's MCP. This is

**[39:06]** things, right? So, there's MCP. This is just your standard.

**[39:09]** just your standard.

**[39:09]** just your standard. Sorry,

**[39:14]** I thought something. Um, yeah. So, this

**[39:14]** I thought something. Um, yeah. So, this is kind of your standard MCP client uh

**[39:17]** is kind of your standard MCP client uh

**[39:17]** is kind of your standard MCP client uh code. Uh, just just allows you to

**[39:19]** code. Uh, just just allows you to

**[39:19]** code. Uh, just just allows you to consume um the MCP uh calls coming from

**[39:23]** consume um the MCP uh calls coming from

**[39:23]** consume um the MCP uh calls coming from the LLM. Um, we have the the GitHub,

**[39:26]** the LLM. Um, we have the the GitHub,

**[39:26]** the LLM. Um, we have the the GitHub, right? So, this is going to be um what

**[39:28]** right? So, this is going to be um what

**[39:28]** right? So, this is going to be um what it sends to that Zapier endpoint. Uh,

**[39:31]** it sends to that Zapier endpoint. Uh,

**[39:31]** it sends to that Zapier endpoint. Uh, it's going to call GitHub create issue.

**[39:33]** it's going to call GitHub create issue.

**[39:33]** it's going to call GitHub create issue. Uh, and then the Slack agent is going to

**[39:36]** Uh, and then the Slack agent is going to

**[39:36]** Uh, and then the Slack agent is going to do send slack channel message. Um so

**[39:38]** do send slack channel message. Um so

**[39:38]** do send slack channel message. Um so these are just kind of like the MCP

**[39:41]** these are just kind of like the MCP

**[39:41]** these are just kind of like the MCP client tools that the uh individual

**[39:44]** client tools that the uh individual

**[39:44]** client tools that the uh individual agents will use. Um yeah so this genkit

**[39:48]** agents will use. Um yeah so this genkit

**[39:48]** agents will use. Um yeah so this genkit um this is based on on what they provide

**[39:51]** um this is based on on what they provide

**[39:51]** um this is based on on what they provide in their in their sample repo. Um

**[39:55]** in their in their sample repo. Um

**[39:55]** in their in their sample repo. Um you you can use a different model if you

**[39:56]** you you can use a different model if you

**[39:56]** you you can use a different model if you want right you can change you know the

**[39:58]** want right you can change you know the

**[39:58]** want right you can change you know the the settings on it. Um but this


### [40:00 - 41:00]

**[40:00]** the settings on it. Um but this

**[40:00]** the settings on it. Um but this essentially uh spawns you a new instance

**[40:03]** essentially uh spawns you a new instance

**[40:03]** essentially uh spawns you a new instance of what's going to communicate. Um, this

**[40:06]** of what's going to communicate. Um, this

**[40:06]** of what's going to communicate. Um, this just loads the system prompt. Um, I can

**[40:09]** just loads the system prompt. Um, I can

**[40:09]** just loads the system prompt. Um, I can open up the system prompt here. Um, so

**[40:11]** open up the system prompt here. Um, so

**[40:11]** open up the system prompt here. Um, so right, it's got a critical workflow.

**[40:13]** right, it's got a critical workflow.

**[40:13]** right, it's got a critical workflow. It's going to do these things in this

**[40:14]** It's going to do these things in this

**[40:14]** It's going to do these things in this order. It's got a few steps, you know,

**[40:17]** order. It's got a few steps, you know,

**[40:17]** order. It's got a few steps, you know, discovery. Uh, uh, this is actually

**[40:19]** discovery. Uh, uh, this is actually

**[40:19]** discovery. Uh, uh, this is actually something I noticed like if you don't

**[40:21]** something I noticed like if you don't

**[40:21]** something I noticed like if you don't tell the A2A agent to call list remote

**[40:23]** tell the A2A agent to call list remote

**[40:23]** tell the A2A agent to call list remote agents, it just won't, right? And it'll

**[40:26]** agents, it just won't, right? And it'll

**[40:26]** agents, it just won't, right? And it'll try to answer everything on itself. Um,

**[40:28]** try to answer everything on itself. Um,

**[40:28]** try to answer everything on itself. Um, you know, it can very easily fake

**[40:30]** you know, it can very easily fake

**[40:30]** you know, it can very easily fake sending a Slack channel message and be

**[40:32]** sending a Slack channel message and be

**[40:32]** sending a Slack channel message and be like, "Oh, I just sent it for you." I

**[40:33]** like, "Oh, I just sent it for you." I

**[40:33]** like, "Oh, I just sent it for you." I say, "No, you didn't.

**[40:35]** say, "No, you didn't.

**[40:35]** say, "No, you didn't. Um, you know, one of the things I've

**[40:37]** Um, you know, one of the things I've

**[40:37]** Um, you know, one of the things I've noticed, uh, using cursor is like every

**[40:39]** noticed, uh, using cursor is like every

**[40:39]** noticed, uh, using cursor is like every time I catch it doing something wrong,

**[40:41]** time I catch it doing something wrong,

**[40:41]** time I catch it doing something wrong, it says you're absolutely right.

**[40:50]** Um, I even tried to prompt that out of

**[40:50]** Um, I even tried to prompt that out of it. Um, and it's not promptable to get

**[40:52]** it. Um, and it's not promptable to get

**[40:52]** it. Um, and it's not promptable to get to get it to not say that. Um, cool.

**[40:55]** to get it to not say that. Um, cool.

**[40:55]** to get it to not say that. Um, cool. Yeah. And then the the index. So, this

**[40:57]** Yeah. And then the the index. So, this

**[40:57]** Yeah. And then the the index. So, this is actually where the agent card is.

**[40:59]** is actually where the agent card is.

**[40:59]** is actually where the agent card is. It's a little bit long.


### [41:00 - 42:00]

**[41:01]** It's a little bit long.

**[41:02]** It's a little bit long. Let me see.

**[41:04]** Let me see.

**[41:04]** Let me see. I think it's up here near the start.

**[41:19]** There we go. That was line 1200. So, I'm

**[41:19]** There we go. That was line 1200. So, I'm not near the start at all. Um, yeah. So,

**[41:21]** not near the start at all. Um, yeah. So,

**[41:21]** not near the start at all. Um, yeah. So, this this is what the host agent exposes

**[41:24]** this this is what the host agent exposes

**[41:24]** this this is what the host agent exposes if somebody else wanted to call it. Um,

**[41:27]** if somebody else wanted to call it. Um,

**[41:27]** if somebody else wanted to call it. Um, so it has these abilities to list remote

**[41:29]** so it has these abilities to list remote

**[41:29]** so it has these abilities to list remote agents and send tasks, right? And then

**[41:31]** agents and send tasks, right? And then

**[41:31]** agents and send tasks, right? And then if we compare that to the to the GitHub

**[41:33]** if we compare that to the to the GitHub

**[41:33]** if we compare that to the to the GitHub which is uh a lot smaller. Um

**[41:45]** there we go. Yeah. So the GitHub agent

**[41:45]** there we go. Yeah. So the GitHub agent can create GitHub issues, right? Um it's

**[41:47]** can create GitHub issues, right? Um it's

**[41:48]** can create GitHub issues, right? Um it's got the ability uh to do various things

**[41:51]** got the ability uh to do various things

**[41:51]** got the ability uh to do various things and um it has a list of skills. Um and

**[41:54]** and um it has a list of skills. Um and

**[41:54]** and um it has a list of skills. Um and this is all that the the host agent

**[41:57]** this is all that the the host agent

**[41:57]** this is all that the the host agent really knows about this agent. Um, so

**[41:59]** really knows about this agent. Um, so

**[41:59]** really knows about this agent. Um, so you could imagine how big this might get


### [42:00 - 43:00]

**[42:01]** you could imagine how big this might get

**[42:01]** you could imagine how big this might get if you were to, you know, implement

**[42:03]** if you were to, you know, implement

**[42:03]** if you were to, you know, implement every single API that say Salesforce has

**[42:05]** every single API that say Salesforce has

**[42:05]** every single API that say Salesforce has or something like that. Um, and in a lot

**[42:08]** or something like that. Um, and in a lot

**[42:08]** or something like that. Um, and in a lot of cases, um, at least with Salesforce,

**[42:10]** of cases, um, at least with Salesforce,

**[42:10]** of cases, um, at least with Salesforce, rather than implementing, you know,

**[42:13]** rather than implementing, you know,

**[42:13]** rather than implementing, you know, wrappers around the APIs, you're

**[42:14]** wrappers around the APIs, you're

**[42:14]** wrappers around the APIs, you're probably just going to want to use like

**[42:16]** probably just going to want to use like

**[42:16]** probably just going to want to use like the SQL or the so-called directly and

**[42:19]** the SQL or the so-called directly and

**[42:19]** the SQL or the so-called directly and let the agent actually write the

**[42:20]** let the agent actually write the

**[42:20]** let the agent actually write the queries. Um, there's a lot of

**[42:22]** queries. Um, there's a lot of

**[42:22]** queries. Um, there's a lot of flexibility when you have, you know,

**[42:24]** flexibility when you have, you know,

**[42:24]** flexibility when you have, you know, direct database access essentially. um

**[42:26]** direct database access essentially. um

**[42:26]** direct database access essentially. um because the the LLM can, you know,

**[42:28]** because the the LLM can, you know,

**[42:28]** because the the LLM can, you know, bypass, you know, the API layer and just

**[42:31]** bypass, you know, the API layer and just

**[42:31]** bypass, you know, the API layer and just go directly to the to the database.

**[42:34]** go directly to the to the database.

**[42:34]** go directly to the to the database. Um and then the um GitHub agent prompt,

**[42:38]** Um and then the um GitHub agent prompt,

**[42:38]** Um and then the um GitHub agent prompt, right? So, it's got some uh things. Um

**[42:40]** right? So, it's got some uh things. Um

**[42:40]** right? So, it's got some uh things. Um this is something I had to add because

**[42:41]** this is something I had to add because

**[42:41]** this is something I had to add because it it insisted on um mentioning who

**[42:45]** it it insisted on um mentioning who

**[42:45]** it it insisted on um mentioning who submitted the bug report, right? So,

**[42:47]** submitted the bug report, right? So,

**[42:47]** submitted the bug report, right? So, there there's definitely concerns

**[42:48]** there there's definitely concerns

**[42:48]** there there's definitely concerns around, you know, PII uh leaking from

**[42:51]** around, you know, PII uh leaking from

**[42:51]** around, you know, PII uh leaking from your, you know, internal meeting

**[42:53]** your, you know, internal meeting

**[42:53]** your, you know, internal meeting transcripts and ending up in GitHub,

**[42:54]** transcripts and ending up in GitHub,

**[42:54]** transcripts and ending up in GitHub, right? Um, and that kind of goes back to

**[42:57]** right? Um, and that kind of goes back to

**[42:57]** right? Um, and that kind of goes back to your uh your question about, you know,

**[42:59]** your uh your question about, you know,

**[42:59]** your uh your question about, you know, how do you audit what's coming out of


### [43:00 - 44:00]

**[43:01]** how do you audit what's coming out of

**[43:01]** how do you audit what's coming out of these LLMs, right? Uh, and you can do

**[43:03]** these LLMs, right? Uh, and you can do

**[43:03]** these LLMs, right? Uh, and you can do that in a number of ways, but it it

**[43:05]** that in a number of ways, but it it

**[43:05]** that in a number of ways, but it it wouldn't be a part of the A2A spec. I

**[43:07]** wouldn't be a part of the A2A spec. I

**[43:07]** wouldn't be a part of the A2A spec. I think it would just be the LLM you

**[43:09]** think it would just be the LLM you

**[43:09]** think it would just be the LLM you connect to has those guard rails in

**[43:11]** connect to has those guard rails in

**[43:11]** connect to has those guard rails in front of it. Uh, and you you're just

**[43:13]** front of it. Uh, and you you're just

**[43:13]** front of it. Uh, and you you're just using that LLM that has the guard rails.

**[43:16]** using that LLM that has the guard rails.

**[43:16]** using that LLM that has the guard rails. um similar Slack um excuse me has a a

**[43:22]** um similar Slack um excuse me has a a

**[43:22]** um similar Slack um excuse me has a a very simple um

**[43:26]** very simple um

**[43:26]** very simple um uh agent card that I can't seem to find.

**[43:29]** uh agent card that I can't seem to find.

**[43:29]** uh agent card that I can't seem to find. Um and then if we jump over now to

**[43:34]** Um and then if we jump over now to

**[43:34]** Um and then if we jump over now to uh the host config. Um so this is

**[43:37]** uh the host config. Um so this is

**[43:37]** uh the host config. Um so this is essentially what configures um the web

**[43:41]** essentially what configures um the web

**[43:41]** essentially what configures um the web hook, right? So the web hook has

**[43:43]** hook, right? So the web hook has

**[43:43]** hook, right? So the web hook has essentially a config that tells it like

**[43:45]** essentially a config that tells it like

**[43:45]** essentially a config that tells it like what it's doing and and you can see that

**[43:47]** what it's doing and and you can see that

**[43:47]** what it's doing and and you can see that in the UI as well. Um and then uh within

**[43:51]** in the UI as well. Um and then uh within

**[43:51]** in the UI as well. Um and then uh within the A2A folder we've got the client and

**[43:53]** the A2A folder we've got the client and

**[43:53]** the A2A folder we've got the client and the server. Again the these are just

**[43:55]** the server. Again the these are just

**[43:55]** the server. Again the these are just pulled directly from uh the A2A repo. Um

**[43:59]** pulled directly from uh the A2A repo. Um

**[43:59]** pulled directly from uh the A2A repo. Um I don't think they've actually exposed


### [44:00 - 45:00]

**[44:01]** I don't think they've actually exposed

**[44:01]** I don't think they've actually exposed uh types or packages yet. Uh which is

**[44:03]** uh types or packages yet. Uh which is

**[44:03]** uh types or packages yet. Uh which is kind of confusing. Um but essentially

**[44:05]** kind of confusing. Um but essentially

**[44:05]** kind of confusing. Um but essentially you can bring that stuff in there. And

**[44:08]** you can bring that stuff in there. And

**[44:08]** you can bring that stuff in there. And uh then the web hook server. Uh so this

**[44:10]** uh then the web hook server. Uh so this

**[44:10]** uh then the web hook server. Uh so this is just a web UI. Uh initially I had

**[44:13]** is just a web UI. Uh initially I had

**[44:13]** is just a web UI. Uh initially I had this whole thing done through the CLI.

**[44:15]** this whole thing done through the CLI.

**[44:16]** this whole thing done through the CLI. Um you know coding with you know tools

**[44:19]** Um you know coding with you know tools

**[44:19]** Um you know coding with you know tools like cursor or augment code. Um CLIs are

**[44:23]** like cursor or augment code. Um CLIs are

**[44:23]** like cursor or augment code. Um CLIs are way easier for AIS to actually write

**[44:25]** way easier for AIS to actually write

**[44:25]** way easier for AIS to actually write they're going to be able to test it uh

**[44:27]** they're going to be able to test it uh

**[44:27]** they're going to be able to test it uh interact with it much better and and be

**[44:29]** interact with it much better and and be

**[44:30]** interact with it much better and and be able to uh produce those outputs.

**[44:36]** Awesome. Uh so yeah I'm gonna going to

**[44:36]** Awesome. Uh so yeah I'm gonna going to shift over to kind of Q&A now. Um so

**[44:39]** shift over to kind of Q&A now. Um so

**[44:39]** shift over to kind of Q&A now. Um so yeah, anybody any questions? Yeah.

**[44:42]** yeah, anybody any questions? Yeah.

**[44:42]** yeah, anybody any questions? Yeah. So um I want to talk evals for a second.

**[44:46]** So um I want to talk evals for a second.

**[44:46]** So um I want to talk evals for a second. So like um I assume that you manage or I

**[44:49]** So like um I assume that you manage or I

**[44:49]** So like um I assume that you manage or I don't know. I mean you manage them

**[44:50]** don't know. I mean you manage them

**[44:50]** don't know. I mean you manage them probably at the at the agent level. Is

**[44:52]** probably at the at the agent level. Is

**[44:52]** probably at the at the agent level. Is there any type of like distributed

**[44:53]** there any type of like distributed

**[44:54]** there any type of like distributed evalu?


### [45:00 - 46:00]

**[45:02]** Yeah, I I haven't done much evals on

**[45:02]** Yeah, I I haven't done much evals on A2A. Um I still think A2A is a bit too

**[45:05]** A2A. Um I still think A2A is a bit too

**[45:05]** A2A. Um I still think A2A is a bit too early to go into production. um like

**[45:08]** early to go into production. um like

**[45:08]** early to go into production. um like even MCP is is kind of borderline. Um

**[45:12]** even MCP is is kind of borderline. Um

**[45:12]** even MCP is is kind of borderline. Um like there there's a lot of rough edges.

**[45:14]** like there there's a lot of rough edges.

**[45:14]** like there there's a lot of rough edges. Um I think you can achieve like much

**[45:17]** Um I think you can achieve like much

**[45:17]** Um I think you can achieve like much better uh things if if you're in

**[45:19]** better uh things if if you're in

**[45:19]** better uh things if if you're in complete control of everything, you can

**[45:21]** complete control of everything, you can

**[45:21]** complete control of everything, you can achieve much better results, you know,

**[45:23]** achieve much better results, you know,

**[45:23]** achieve much better results, you know, with your own local uh function calls.

**[45:27]** with your own local uh function calls.

**[45:28]** with your own local uh function calls. Yeah.

**[45:28]** Yeah.

**[45:28]** Yeah. Any reason instead of Python?

**[45:32]** Any reason instead of Python?

**[45:32]** Any reason instead of Python? Yeah, you can use any language. I think

**[45:34]** Yeah, you can use any language. I think

**[45:34]** Yeah, you can use any language. I think actually uh the 82A framework is better

**[45:36]** actually uh the 82A framework is better

**[45:36]** actually uh the 82A framework is better in Python. Um I just prefer uh

**[45:39]** in Python. Um I just prefer uh

**[45:39]** in Python. Um I just prefer uh TypeScript myself.

**[45:42]** TypeScript myself.

**[45:42]** TypeScript myself. Yeah.

**[45:43]** Yeah.

**[45:43]** Yeah. Can you tell more about the caching? Is

**[45:45]** Can you tell more about the caching? Is

**[45:45]** Can you tell more about the caching? Is caching provided by the model providers

**[45:47]** caching provided by the model providers

**[45:47]** caching provided by the model providers or we implement our own caching?

**[45:49]** or we implement our own caching?

**[45:50]** or we implement our own caching? Yeah. So you implement your own caching.

**[45:51]** Yeah. So you implement your own caching.

**[45:51]** Yeah. So you implement your own caching. Um so you decide you know when to move

**[45:54]** Um so you decide you know when to move

**[45:54]** Um so you decide you know when to move that cache marker uh how to manage it.

**[45:57]** that cache marker uh how to manage it.

**[45:57]** that cache marker uh how to manage it. Um it can be tricky and and I don't

**[45:59]** Um it can be tricky and and I don't

**[45:59]** Um it can be tricky and and I don't think there's very good information


### [46:00 - 47:00]

**[46:01]** think there's very good information

**[46:01]** think there's very good information available online on on what the best

**[46:03]** available online on on what the best

**[46:03]** available online on on what the best strategies are. Um when I was doing the

**[46:06]** strategies are. Um when I was doing the

**[46:06]** strategies are. Um when I was doing the simulations I I used like linear growth,

**[46:09]** simulations I I used like linear growth,

**[46:09]** simulations I I used like linear growth, exponential growth, um you know fixed

**[46:11]** exponential growth, um you know fixed

**[46:11]** exponential growth, um you know fixed size and and kind of compared them all.

**[46:13]** size and and kind of compared them all.

**[46:13]** size and and kind of compared them all. Uh they all worked out between 25 and

**[46:15]** Uh they all worked out between 25 and

**[46:15]** Uh they all worked out between 25 and 35% cost savings. Um but like in

**[46:19]** 35% cost savings. Um but like in

**[46:19]** 35% cost savings. Um but like in practice what you'll find is you're

**[46:21]** practice what you'll find is you're

**[46:21]** practice what you'll find is you're going to have outliers where you know

**[46:23]** going to have outliers where you know

**[46:23]** going to have outliers where you know the cost of a session kind of balloons

**[46:26]** the cost of a session kind of balloons

**[46:26]** the cost of a session kind of balloons because of you know you you cashed at

**[46:28]** because of you know you you cashed at

**[46:28]** because of you know you you cashed at the wrong point.

**[46:30]** the wrong point.

**[46:30]** the wrong point. Yeah. Yeah.

**[46:31]** Yeah. Yeah.

**[46:31]** Yeah. Yeah. So each of the agent can be talking to

**[46:34]** So each of the agent can be talking to

**[46:34]** So each of the agent can be talking to their own like finer.

**[46:43]** Yeah. Yeah. So they they all have their

**[46:43]** Yeah. Yeah. So they they all have their own um which is kind of in contrast to

**[46:45]** own um which is kind of in contrast to

**[46:45]** own um which is kind of in contrast to MCP where the MCP wants to use your LLM,

**[46:48]** MCP where the MCP wants to use your LLM,

**[46:48]** MCP where the MCP wants to use your LLM, right? Because it doesn't want to

**[46:50]** right? Because it doesn't want to

**[46:50]** right? Because it doesn't want to generate its own tokens. So yeah.

**[46:53]** generate its own tokens. So yeah.

**[46:53]** generate its own tokens. So yeah. Um about the authentication and

**[46:55]** Um about the authentication and

**[46:55]** Um about the authentication and authorization

**[46:57]** authorization

**[46:57]** authorization to MCP or agent agent


### [47:00 - 48:00]

**[47:01]** to MCP or agent agent

**[47:01]** to MCP or agent agent authentication

**[47:03]** authentication

**[47:03]** authentication or

**[47:06]** or

**[47:06]** or Yeah. So there there's a couple of

**[47:07]** Yeah. So there there's a couple of

**[47:07]** Yeah. So there there's a couple of different ways. Um, so, uh, within the

**[47:10]** different ways. Um, so, uh, within the

**[47:10]** different ways. Um, so, uh, within the authentication, you can have, uh,

**[47:12]** authentication, you can have, uh,

**[47:12]** authentication, you can have, uh, headers that do the authentication. Um,

**[47:15]** headers that do the authentication. Um,

**[47:15]** headers that do the authentication. Um, I believe if you drop in an OOTH, uh,

**[47:18]** I believe if you drop in an OOTH, uh,

**[47:18]** I believe if you drop in an OOTH, uh, URL, you'll also get an OOTH popup. Um,

**[47:21]** URL, you'll also get an OOTH popup. Um,

**[47:21]** URL, you'll also get an OOTH popup. Um, I really like the OOTH authentication

**[47:23]** I really like the OOTH authentication

**[47:23]** I really like the OOTH authentication because you're getting the user's, you

**[47:25]** because you're getting the user's, you

**[47:25]** because you're getting the user's, you know, ACL, right? Um, and that means

**[47:27]** know, ACL, right? Um, and that means

**[47:27]** know, ACL, right? Um, and that means that, you know, what that user can

**[47:29]** that, you know, what that user can

**[47:29]** that, you know, what that user can access um, is specific to them.

**[47:38]** you have to

**[47:38]** you have to Yes. So, it's going to be dictated by

**[47:40]** Yes. So, it's going to be dictated by

**[47:40]** Yes. So, it's going to be dictated by the the remote uh server. So, either A2A

**[47:44]** the the remote uh server. So, either A2A

**[47:44]** the the remote uh server. So, either A2A or MCP. Um if you're running your own,

**[47:46]** or MCP. Um if you're running your own,

**[47:46]** or MCP. Um if you're running your own, you can choose what you want to run. Um

**[47:48]** you can choose what you want to run. Um

**[47:48]** you can choose what you want to run. Um there's different transport types as

**[47:50]** there's different transport types as

**[47:50]** there's different transport types as well. So, standard IO is something that

**[47:52]** well. So, standard IO is something that

**[47:52]** well. So, standard IO is something that you would use locally. So, like imagine

**[47:54]** you would use locally. So, like imagine

**[47:54]** you would use locally. So, like imagine you wanted to create like a file on your

**[47:57]** you wanted to create like a file on your

**[47:57]** you wanted to create like a file on your desktop. Um you're going to use standard

**[47:59]** desktop. Um you're going to use standard

**[47:59]** desktop. Um you're going to use standard IO typically to interact with local. Uh


### [48:00 - 49:00]

**[48:01]** IO typically to interact with local. Uh

**[48:02]** IO typically to interact with local. Uh and then SSE was serverside events that

**[48:04]** and then SSE was serverside events that

**[48:04]** and then SSE was serverside events that got deprecated in favor of streamable

**[48:06]** got deprecated in favor of streamable

**[48:06]** got deprecated in favor of streamable HTTP.

**[48:08]** HTTP.

**[48:08]** HTTP. So sorry. So for example

**[48:12]** So sorry. So for example

**[48:12]** So sorry. So for example we are interacting with a Salesforce

**[48:13]** we are interacting with a Salesforce

**[48:14]** we are interacting with a Salesforce agency let's say and each user has

**[48:17]** agency let's say and each user has

**[48:17]** agency let's say and each user has different authorization for example

**[48:19]** different authorization for example

**[48:19]** different authorization for example which

**[48:21]** which

**[48:21]** which employee A probably have access to the

**[48:23]** employee A probably have access to the

**[48:23]** employee A probably have access to the some sort of tables employ

**[48:37]** yeah that will typically be handled uh

**[48:37]** yeah that will typically be handled uh through an OAT MCP server right So

**[48:40]** through an OAT MCP server right So

**[48:40]** through an OAT MCP server right So they're going to essentially log in as

**[48:42]** they're going to essentially log in as

**[48:42]** they're going to essentially log in as themselves as part of the connection and

**[48:45]** themselves as part of the connection and

**[48:45]** themselves as part of the connection and then they're going to save that refresh

**[48:46]** then they're going to save that refresh

**[48:46]** then they're going to save that refresh token for later use.

**[48:49]** token for later use.

**[48:49]** token for later use. Yeah.

**[48:50]** Yeah.

**[48:50]** Yeah. How would you describe the performance

**[48:53]** How would you describe the performance

**[48:54]** How would you describe the performance um for security especially you explained

**[48:56]** um for security especially you explained

**[48:56]** um for security especially you explained very well about authentication etc. But

**[48:59]** very well about authentication etc. But


### [49:00 - 50:00]

**[49:00]** very well about authentication etc. But I'm looking for more explanation towards

**[49:02]** I'm looking for more explanation towards

**[49:02]** I'm looking for more explanation towards encryption asymmetric encryption and

**[49:06]** encryption asymmetric encryption and

**[49:06]** encryption asymmetric encryption and also there is a possibility of

**[49:07]** also there is a possibility of

**[49:08]** also there is a possibility of certificate manager and all the way to

**[49:10]** certificate manager and all the way to

**[49:10]** certificate manager and all the way to the end of the entire architecture. So

**[49:13]** the end of the entire architecture. So

**[49:13]** the end of the entire architecture. So how would you describe the performance

**[49:16]** how would you describe the performance

**[49:16]** how would you describe the performance and see I'm looking for some financial

**[49:19]** and see I'm looking for some financial

**[49:19]** and see I'm looking for some financial application this architecture what you

**[49:21]** application this architecture what you

**[49:21]** application this architecture what you have described is pretty good but uh

**[49:24]** have described is pretty good but uh

**[49:24]** have described is pretty good but uh similar on the financial applications as

**[49:27]** similar on the financial applications as

**[49:27]** similar on the financial applications as well as uh some department of defense or

**[49:31]** well as uh some department of defense or

**[49:31]** well as uh some department of defense or some kind of applications highly in

**[49:34]** some kind of applications highly in

**[49:34]** some kind of applications highly in highly secured environment where it's

**[49:36]** highly secured environment where it's

**[49:36]** highly secured environment where it's all both combination of asymmetric and

**[49:40]** all both combination of asymmetric and

**[49:40]** all both combination of asymmetric and symmetric

**[49:41]** symmetric

**[49:41]** symmetric yeah you're you're probably going want

**[49:42]** yeah you're you're probably going want

**[49:42]** yeah you're you're probably going want to run like the LLM yourself and you're

**[49:46]** to run like the LLM yourself and you're

**[49:46]** to run like the LLM yourself and you're more than likely not going to want to

**[49:48]** more than likely not going to want to

**[49:48]** more than likely not going to want to interact with anybody outside your VPC,

**[49:50]** interact with anybody outside your VPC,

**[49:50]** interact with anybody outside your VPC, right? In those cases, um I I don't know

**[49:53]** right? In those cases, um I I don't know

**[49:53]** right? In those cases, um I I don't know if you would want to consume a third

**[49:55]** if you would want to consume a third

**[49:55]** if you would want to consume a third party MCP server or A2A agent uh in a

**[49:58]** party MCP server or A2A agent uh in a

**[49:58]** party MCP server or A2A agent uh in a highly regulated environment, right?

**[49:59]** highly regulated environment, right?

**[49:59]** highly regulated environment, right? Like, you know, HIPPA compliance,


### [50:00 - 51:00]

**[50:01]** Like, you know, HIPPA compliance,

**[50:01]** Like, you know, HIPPA compliance, financial stuff. Um if you do have the

**[50:04]** financial stuff. Um if you do have the

**[50:04]** financial stuff. Um if you do have the ability to do that, right, you're going

**[50:05]** ability to do that, right, you're going

**[50:05]** ability to do that, right, you're going to have some sort of agreement with the

**[50:07]** to have some sort of agreement with the

**[50:07]** to have some sort of agreement with the service provider that provides those

**[50:09]** service provider that provides those

**[50:09]** service provider that provides those tools. Um, and you're going to, you

**[50:11]** tools. Um, and you're going to, you

**[50:11]** tools. Um, and you're going to, you know, do transport over HTTPS, you're

**[50:13]** know, do transport over HTTPS, you're

**[50:13]** know, do transport over HTTPS, you're going to have maybe mutual TLS both on

**[50:16]** going to have maybe mutual TLS both on

**[50:16]** going to have maybe mutual TLS both on the A2A agent and the remote agent. Uh,

**[50:19]** the A2A agent and the remote agent. Uh,

**[50:19]** the A2A agent and the remote agent. Uh, and similar with the MCP server, you're

**[50:21]** and similar with the MCP server, you're

**[50:21]** and similar with the MCP server, you're probably going to have some sort of IP

**[50:22]** probably going to have some sort of IP

**[50:22]** probably going to have some sort of IP whitelisting, right? Like there's

**[50:24]** whitelisting, right? Like there's

**[50:24]** whitelisting, right? Like there's there's a ton of things you can do

**[50:25]** there's a ton of things you can do

**[50:25]** there's a ton of things you can do around that. I think they're out of

**[50:26]** around that. I think they're out of

**[50:26]** around that. I think they're out of scope of of the actual protocols

**[50:28]** scope of of the actual protocols

**[50:28]** scope of of the actual protocols themselves because, you know,

**[50:30]** themselves because, you know,

**[50:30]** themselves because, you know, essentially you're over an encrypted

**[50:31]** essentially you're over an encrypted

**[50:31]** essentially you're over an encrypted line, but uh, typically there's there's

**[50:33]** line, but uh, typically there's there's

**[50:33]** line, but uh, typically there's there's more to it than than just that, right?

**[50:35]** more to it than than just that, right?

**[50:36]** more to it than than just that, right? So you're playing around the end point

**[50:38]** So you're playing around the end point

**[50:38]** So you're playing around the end point controls on this and that's really scary

**[50:42]** controls on this and that's really scary

**[50:42]** controls on this and that's really scary when dealing with

**[50:44]** when dealing with

**[50:44]** when dealing with Yeah.

**[50:45]** Yeah.

**[50:45]** Yeah. Yeah. And like if if these are your own

**[50:46]** Yeah. And like if if these are your own

**[50:46]** Yeah. And like if if these are your own internal MCP servers and your own

**[50:49]** internal MCP servers and your own

**[50:49]** internal MCP servers and your own internal A2A agents maybe from different

**[50:51]** internal A2A agents maybe from different

**[50:51]** internal A2A agents maybe from different parts of the organization um you know

**[50:53]** parts of the organization um you know

**[50:53]** parts of the organization um you know they'll all live inside your VPC and

**[50:56]** they'll all live inside your VPC and

**[50:56]** they'll all live inside your VPC and they're probably never going to talk to

**[50:58]** they're probably never going to talk to

**[50:58]** they're probably never going to talk to the to public internet. So your the sol


### [51:00 - 52:00]

**[51:02]** the to public internet. So your the sol

**[51:02]** the to public internet. So your the sol the answer I get from you is stay with

**[51:05]** the answer I get from you is stay with

**[51:05]** the answer I get from you is stay with BPC and stay away from uh in that case

**[51:09]** BPC and stay away from uh in that case

**[51:09]** BPC and stay away from uh in that case stay away from endpoint

**[51:11]** stay away from endpoint

**[51:11]** stay away from endpoint um security which means stay away from

**[51:14]** um security which means stay away from

**[51:14]** um security which means stay away from MCP or A2A.

**[51:16]** MCP or A2A.

**[51:16]** MCP or A2A. It's so the these are just protocols. Um

**[51:19]** It's so the these are just protocols. Um

**[51:19]** It's so the these are just protocols. Um it's really up to you whether you want

**[51:21]** it's really up to you whether you want

**[51:21]** it's really up to you whether you want to connect to an external third party

**[51:24]** to connect to an external third party

**[51:24]** to connect to an external third party and that's going to be your own security

**[51:26]** and that's going to be your own security

**[51:26]** and that's going to be your own security posture. Uh it's not really going to be

**[51:27]** posture. Uh it's not really going to be

**[51:27]** posture. Uh it's not really going to be defined by the protocol itself.

**[51:29]** defined by the protocol itself.

**[51:29]** defined by the protocol itself. Yeah. Keep them away from the subet or

**[51:32]** Yeah. Keep them away from the subet or

**[51:32]** Yeah. Keep them away from the subet or bring them inside the subet.

**[51:34]** bring them inside the subet.

**[51:34]** bring them inside the subet. Which one would you prefer?

**[51:36]** Which one would you prefer?

**[51:36]** Which one would you prefer? I I I would liken it to like I found a

**[51:38]** I I I would liken it to like I found a

**[51:38]** I I I would liken it to like I found a USB cable. Will I plug it into my

**[51:40]** USB cable. Will I plug it into my

**[51:40]** USB cable. Will I plug it into my laptop? Right. So the USB it's not its

**[51:44]** laptop? Right. So the USB it's not its

**[51:44]** laptop? Right. So the USB it's not its fault, right? Like USB is just a a

**[51:46]** fault, right? Like USB is just a a

**[51:46]** fault, right? Like USB is just a a standard. Um it's what that USB is

**[51:49]** standard. Um it's what that USB is

**[51:49]** standard. Um it's what that USB is connected to is the risk, right? So like

**[51:52]** connected to is the risk, right? So like

**[51:52]** connected to is the risk, right? So like if you're willing to find a dongle on

**[51:54]** if you're willing to find a dongle on

**[51:54]** if you're willing to find a dongle on the street and plug it in, you know that

**[51:57]** the street and plug it in, you know that

**[51:57]** the street and plug it in, you know that that that's really going to be your

**[51:58]** that that's really going to be your

**[51:58]** that that's really going to be your security posture, right?


### [52:00 - 53:00]

**[52:01]** security posture, right?

**[52:01]** security posture, right? Yeah.

**[52:01]** Yeah.

**[52:01]** Yeah. Okay. So um how much heavy lifting do

**[52:04]** Okay. So um how much heavy lifting do

**[52:04]** Okay. So um how much heavy lifting do you have the orchestrator do? Like you

**[52:06]** you have the orchestrator do? Like you

**[52:06]** you have the orchestrator do? Like you ever hit the scenarios where uh you have

**[52:08]** ever hit the scenarios where uh you have

**[52:08]** ever hit the scenarios where uh you have the orchestrator interprets the response

**[52:11]** the orchestrator interprets the response

**[52:11]** the orchestrator interprets the response from a sub agent and then maybe does a

**[52:13]** from a sub agent and then maybe does a

**[52:13]** from a sub agent and then maybe does a retry with a better prompt.

**[52:17]** retry with a better prompt.

**[52:17]** retry with a better prompt. Loose or anything?

**[52:18]** Loose or anything?

**[52:18]** Loose or anything? Yeah. So, so one of the things and I I

**[52:20]** Yeah. So, so one of the things and I I

**[52:20]** Yeah. So, so one of the things and I I kind of prompted it out of this uh

**[52:23]** kind of prompted it out of this uh

**[52:23]** kind of prompted it out of this uh workshop just to keep it simple is um

**[52:25]** workshop just to keep it simple is um

**[52:25]** workshop just to keep it simple is um like the the bench agent wants to have a

**[52:28]** like the the bench agent wants to have a

**[52:28]** like the the bench agent wants to have a conversation with the host agent. Um but

**[52:31]** conversation with the host agent. Um but

**[52:31]** conversation with the host agent. Um but I I didn't want to kind of implement

**[52:32]** I I didn't want to kind of implement

**[52:32]** I I didn't want to kind of implement that back and forth because it was going

**[52:34]** that back and forth because it was going

**[52:34]** that back and forth because it was going to delay the uh the web hook processing.

**[52:37]** to delay the uh the web hook processing.

**[52:37]** to delay the uh the web hook processing. Um but you can have backs and forths

**[52:39]** Um but you can have backs and forths

**[52:39]** Um but you can have backs and forths between the agents. Um and it's probably

**[52:41]** between the agents. Um and it's probably

**[52:42]** between the agents. Um and it's probably desirable as well, right? like if if for

**[52:44]** desirable as well, right? like if if for

**[52:44]** desirable as well, right? like if if for whatever reason the host agent doesn't

**[52:46]** whatever reason the host agent doesn't

**[52:46]** whatever reason the host agent doesn't give sufficient information, you know,

**[52:48]** give sufficient information, you know,

**[52:48]** give sufficient information, you know, the the remote agent is going to be

**[52:49]** the the remote agent is going to be

**[52:49]** the the remote agent is going to be like, "Okay, you know, I know you want

**[52:51]** like, "Okay, you know, I know you want

**[52:51]** like, "Okay, you know, I know you want to update an opportunity, but you didn't

**[52:53]** to update an opportunity, but you didn't

**[52:53]** to update an opportunity, but you didn't tell me which opportunity." Right? Um

**[52:55]** tell me which opportunity." Right? Um

**[52:55]** tell me which opportunity." Right? Um I mean, I could even see scenarios where

**[52:57]** I mean, I could even see scenarios where

**[52:57]** I mean, I could even see scenarios where you have uh an expensive LM that you


### [53:00 - 54:00]

**[53:00]** you have uh an expensive LM that you

**[53:00]** you have uh an expensive LM that you have on reserve that you go to with a

**[53:03]** have on reserve that you go to with a

**[53:03]** have on reserve that you go to with a cheaper LLM, agents aren't giving you

**[53:05]** cheaper LLM, agents aren't giving you

**[53:05]** cheaper LLM, agents aren't giving you what you want. Like, sorry, just

**[53:06]** what you want. Like, sorry, just

**[53:06]** what you want. Like, sorry, just thinking through stuff.

**[53:08]** thinking through stuff.

**[53:08]** thinking through stuff. Yeah. And I I I think like LLM cost and

**[53:12]** Yeah. And I I I think like LLM cost and

**[53:12]** Yeah. And I I I think like LLM cost and capability is is a big challenge with a

**[53:14]** capability is is a big challenge with a

**[53:14]** capability is is a big challenge with a lot of these things because you know if

**[53:16]** lot of these things because you know if

**[53:16]** lot of these things because you know if if you're running say cloud for opus and

**[53:19]** if you're running say cloud for opus and

**[53:19]** if you're running say cloud for opus and somebody for whatever reason asks you to

**[53:21]** somebody for whatever reason asks you to

**[53:21]** somebody for whatever reason asks you to summarize like you know five sentences h

**[53:24]** summarize like you know five sentences h

**[53:24]** summarize like you know five sentences h it's going to cost you a fortune right

**[53:25]** it's going to cost you a fortune right

**[53:25]** it's going to cost you a fortune right so you need uh intelligent rooting logic

**[53:28]** so you need uh intelligent rooting logic

**[53:28]** so you need uh intelligent rooting logic on like does this task need the entire

**[53:31]** on like does this task need the entire

**[53:31]** on like does this task need the entire context right does it need 20,000 tokens

**[53:33]** context right does it need 20,000 tokens

**[53:33]** context right does it need 20,000 tokens of a system prompt to summarize you know

**[53:36]** of a system prompt to summarize you know

**[53:36]** of a system prompt to summarize you know a short bit of text And that's one of

**[53:38]** a short bit of text And that's one of

**[53:38]** a short bit of text And that's one of the challenges that you you'll run into

**[53:40]** the challenges that you you'll run into

**[53:40]** the challenges that you you'll run into where you you kind of need a like a

**[53:43]** where you you kind of need a like a

**[53:43]** where you you kind of need a like a rooting LLM in front of these complex

**[53:46]** rooting LLM in front of these complex

**[53:46]** rooting LLM in front of these complex agents so that they can actually figure

**[53:47]** agents so that they can actually figure

**[53:47]** agents so that they can actually figure out you know how deep do I go.

**[53:50]** out you know how deep do I go.

**[53:50]** out you know how deep do I go. Yeah. Similar to the routing

**[53:53]** Yeah. Similar to the routing

**[53:53]** Yeah. Similar to the routing orchestration question, I was wondering

**[53:54]** orchestration question, I was wondering

**[53:54]** orchestration question, I was wondering like if you wanted to post a Slack

**[53:56]** like if you wanted to post a Slack

**[53:56]** like if you wanted to post a Slack message that linked the GitHub issue,

**[53:59]** message that linked the GitHub issue,

**[53:59]** message that linked the GitHub issue, for example, I think you'd probably


### [54:00 - 55:00]

**[54:01]** for example, I think you'd probably

**[54:01]** for example, I think you'd probably prefer your architecture to go back

**[54:03]** prefer your architecture to go back

**[54:03]** prefer your architecture to go back through the host to make that decision

**[54:04]** through the host to make that decision

**[54:04]** through the host to make that decision rather than let the GitHub agent

**[54:06]** rather than let the GitHub agent

**[54:06]** rather than let the GitHub agent directly.

**[54:08]** directly.

**[54:08]** directly. Yeah. So the the host agent wouldn't run

**[54:10]** Yeah. So the the host agent wouldn't run

**[54:10]** Yeah. So the the host agent wouldn't run the uh the calls in parallel, right? So

**[54:13]** the uh the calls in parallel, right? So

**[54:13]** the uh the calls in parallel, right? So there there's actually a flag whether

**[54:14]** there there's actually a flag whether

**[54:14]** there there's actually a flag whether you want it to go in parallel or not.

**[54:16]** you want it to go in parallel or not.

**[54:16]** you want it to go in parallel or not. Um, so it would have to say, "Oh, I need

**[54:18]** Um, so it would have to say, "Oh, I need

**[54:18]** Um, so it would have to say, "Oh, I need to create the GitHub issue first um

**[54:20]** to create the GitHub issue first um

**[54:20]** to create the GitHub issue first um before I talk to the Slack agent, right?

**[54:22]** before I talk to the Slack agent, right?

**[54:22]** before I talk to the Slack agent, right? Since I need that URL."

**[54:25]** Since I need that URL."

**[54:25]** Since I need that URL." But in general, you'd prefer to have

**[54:26]** But in general, you'd prefer to have

**[54:26]** But in general, you'd prefer to have those decisions go through the host

**[54:28]** those decisions go through the host

**[54:28]** those decisions go through the host rather than even allow.

**[54:31]** rather than even allow.

**[54:31]** rather than even allow. Yeah, absolutely. Yeah. Yeah.

**[54:34]** Yeah, absolutely. Yeah. Yeah.

**[54:34]** Yeah, absolutely. Yeah. Yeah. Yeah.

**[54:35]** Yeah.

**[54:35]** Yeah. I want to ask that the context slicing

**[54:37]** I want to ask that the context slicing

**[54:37]** I want to ask that the context slicing for the sub aents that is entirely

**[54:39]** for the sub aents that is entirely

**[54:39]** for the sub aents that is entirely happening through prompt engineering or

**[54:41]** happening through prompt engineering or

**[54:41]** happening through prompt engineering or are there other frameworks to like slice

**[54:43]** are there other frameworks to like slice

**[54:43]** are there other frameworks to like slice the context that will be going for

**[54:44]** the context that will be going for

**[54:44]** the context that will be going for different

**[54:46]** different

**[54:46]** different Yeah. So, so typically context

**[54:48]** Yeah. So, so typically context

**[54:48]** Yeah. So, so typically context management is going to be implemented in

**[54:49]** management is going to be implemented in

**[54:49]** management is going to be implemented in your own codebase. Uh the sub agents

**[54:52]** your own codebase. Uh the sub agents

**[54:52]** your own codebase. Uh the sub agents context management is more than likely

**[54:54]** context management is more than likely

**[54:54]** context management is more than likely going to be a third party's codebase. Um

**[54:56]** going to be a third party's codebase. Um

**[54:56]** going to be a third party's codebase. Um if it's one of your own agents, right,

**[54:58]** if it's one of your own agents, right,

**[54:58]** if it's one of your own agents, right, you can manage it as well there. Um but


### [55:00 - 56:00]

**[55:00]** you can manage it as well there. Um but

**[55:00]** you can manage it as well there. Um but yeah, you're you're going to want to

**[55:01]** yeah, you're you're going to want to

**[55:01]** yeah, you're you're going to want to figure out like what's optimal for your

**[55:03]** figure out like what's optimal for your

**[55:04]** figure out like what's optimal for your actual like production usage. Um yeah

**[55:08]** actual like production usage. Um yeah

**[55:08]** actual like production usage. Um yeah but so you you will be using prompts in

**[55:10]** but so you you will be using prompts in

**[55:10]** but so you you will be using prompts in the host agent to to kind of guide what

**[55:13]** the host agent to to kind of guide what

**[55:13]** the host agent to to kind of guide what context to send to each sub aent, right?

**[55:15]** context to send to each sub aent, right?

**[55:15]** context to send to each sub aent, right? Yeah. Yeah. So so what you what you send

**[55:17]** Yeah. Yeah. So so what you what you send

**[55:17]** Yeah. Yeah. So so what you what you send is typically like a question or a task.

**[55:20]** is typically like a question or a task.

**[55:20]** is typically like a question or a task. Um it's usually very small, right? Like

**[55:23]** Um it's usually very small, right? Like

**[55:23]** Um it's usually very small, right? Like you you don't you don't send the full

**[55:24]** you you don't you don't send the full

**[55:24]** you you don't you don't send the full meeting transcript to the Slack agent to

**[55:28]** meeting transcript to the Slack agent to

**[55:28]** meeting transcript to the Slack agent to to do what it's doing. The host agent

**[55:30]** to do what it's doing. The host agent

**[55:30]** to do what it's doing. The host agent processes the transcript and then

**[55:32]** processes the transcript and then

**[55:32]** processes the transcript and then decides what the tasks are. Um, so like

**[55:34]** decides what the tasks are. Um, so like

**[55:34]** decides what the tasks are. Um, so like if I look down here uh and actually I

**[55:37]** if I look down here uh and actually I

**[55:37]** if I look down here uh and actually I think I can see it in the dashboard.

**[55:39]** think I can see it in the dashboard.

**[55:39]** think I can see it in the dashboard. Um, yeah. So this is actually what the

**[55:42]** Um, yeah. So this is actually what the

**[55:42]** Um, yeah. So this is actually what the the host agent sent uh to the GitHub

**[55:45]** the host agent sent uh to the GitHub

**[55:45]** the host agent sent uh to the GitHub agent, right? It said create an issue in

**[55:47]** agent, right? It said create an issue in

**[55:47]** agent, right? It said create an issue in this repo title this, you know, with

**[55:50]** this repo title this, you know, with

**[55:50]** this repo title this, you know, with this description and title. Um, and then

**[55:52]** this description and title. Um, and then

**[55:52]** this description and title. Um, and then the the GitHub agent its task is to

**[55:55]** the the GitHub agent its task is to

**[55:55]** the the GitHub agent its task is to extract uh three bits of information,

**[55:58]** extract uh three bits of information,

**[55:58]** extract uh three bits of information, right? So what's the instructions to


### [56:00 - 57:00]

**[56:00]** right? So what's the instructions to

**[56:00]** right? So what's the instructions to give the MCP server? What's the body and

**[56:02]** give the MCP server? What's the body and

**[56:02]** give the MCP server? What's the body and what's the title?

**[56:05]** what's the title?

**[56:05]** what's the title? Yeah.

**[56:11]** context

**[56:11]** context which we want to send

**[56:14]** which we want to send

**[56:14]** which we want to send for each and every so you show earlier

**[56:18]** for each and every so you show earlier

**[56:18]** for each and every so you show earlier that's pretty much

**[56:21]** that's pretty much

**[56:21]** that's pretty much the understandation

**[56:38]** Yeah. So, so Zapier, uh, the SSE

**[56:38]** Yeah. So, so Zapier, uh, the SSE implementation doesn't actually require

**[56:40]** implementation doesn't actually require

**[56:40]** implementation doesn't actually require headers. Um, I think these are just left

**[56:42]** headers. Um, I think these are just left

**[56:42]** headers. Um, I think these are just left over from from something else. Um, so

**[56:46]** over from from something else. Um, so

**[56:46]** over from from something else. Um, so there's actually no authentication and

**[56:47]** there's actually no authentication and

**[56:47]** there's actually no authentication and the URL itself is kind of like a secret

**[56:51]** the URL itself is kind of like a secret

**[56:51]** the URL itself is kind of like a secret key, right? Um, so like if I disconnect

**[56:54]** key, right? Um, so like if I disconnect

**[56:54]** key, right? Um, so like if I disconnect and and reconnect without the headers, I

**[56:56]** and and reconnect without the headers, I

**[56:56]** and and reconnect without the headers, I should be able to uh Yeah. So I can I

**[56:59]** should be able to uh Yeah. So I can I

**[56:59]** should be able to uh Yeah. So I can I can still query it. um they they've


### [57:00 - 58:00]

**[57:02]** can still query it. um they they've

**[57:02]** can still query it. um they they've moved away from this approach right now

**[57:04]** moved away from this approach right now

**[57:04]** moved away from this approach right now with with with more secure kind of uh

**[57:06]** with with with more secure kind of uh

**[57:06]** with with with more secure kind of uh setups and you you'll notice in their

**[57:08]** setups and you you'll notice in their

**[57:08]** setups and you you'll notice in their thing right um they've kind of

**[57:11]** thing right um they've kind of

**[57:11]** thing right um they've kind of deprecated that and you know treat this

**[57:14]** deprecated that and you know treat this

**[57:14]** deprecated that and you know treat this URL like a password right um

**[57:19]** URL like a password right um

**[57:19]** URL like a password right um what's your experience in using

**[57:21]** what's your experience in using

**[57:21]** what's your experience in using different

**[57:23]** different

**[57:23]** different workflows like for example

**[57:27]** workflows like for example

**[57:27]** workflows like for example Gemini and also did you use

**[57:31]** Gemini and also did you use

**[57:31]** Gemini and also did you use for this kind of work.

**[57:33]** for this kind of work.

**[57:33]** for this kind of work. Yeah. So, so we we typically lean

**[57:35]** Yeah. So, so we we typically lean

**[57:36]** Yeah. So, so we we typically lean towards Gemini for large context um and

**[57:40]** towards Gemini for large context um and

**[57:40]** towards Gemini for large context um and um Claude Sonnet 4 uh for tool calling.

**[57:44]** um Claude Sonnet 4 uh for tool calling.

**[57:44]** um Claude Sonnet 4 uh for tool calling. Um Claude Opus is better, but it's not

**[57:47]** Um Claude Opus is better, but it's not

**[57:47]** Um Claude Opus is better, but it's not like 4x better. Um you know, and when

**[57:50]** like 4x better. Um you know, and when

**[57:50]** like 4x better. Um you know, and when you compare price to performance, right,

**[57:52]** you compare price to performance, right,

**[57:52]** you compare price to performance, right, like you know, 5% better doesn't equate

**[57:55]** like you know, 5% better doesn't equate

**[57:55]** like you know, 5% better doesn't equate to 4x to cost. you talking about Gemini

**[57:57]** to 4x to cost. you talking about Gemini

**[57:58]** to 4x to cost. you talking about Gemini Flash or or Pro?

**[57:59]** Flash or or Pro?

**[57:59]** Flash or or Pro? Yeah, so we'll use Gemini Flash for


### [58:00 - 59:00]

**[58:01]** Yeah, so we'll use Gemini Flash for

**[58:01]** Yeah, so we'll use Gemini Flash for simple things like summarization, right?

**[58:04]** simple things like summarization, right?

**[58:04]** simple things like summarization, right? Um you could use Claude Haiku as well,

**[58:06]** Um you could use Claude Haiku as well,

**[58:06]** Um you could use Claude Haiku as well, but I think I think Google's kind of

**[58:08]** but I think I think Google's kind of

**[58:08]** but I think I think Google's kind of taken the lead in in price performance,

**[58:10]** taken the lead in in price performance,

**[58:10]** taken the lead in in price performance, you know, from an economic standpoint.

**[58:13]** you know, from an economic standpoint.

**[58:13]** you know, from an economic standpoint. Uh but Claude is still the kind of king

**[58:15]** Uh but Claude is still the kind of king

**[58:15]** Uh but Claude is still the kind of king of tools. Uh they they created MCP, so

**[58:18]** of tools. Uh they they created MCP, so

**[58:18]** of tools. Uh they they created MCP, so they kind of had a head start, right?

**[58:21]** they kind of had a head start, right?

**[58:21]** they kind of had a head start, right? What about the hospital?

**[58:23]** What about the hospital?

**[58:23]** What about the hospital? Yeah, we we have Deep Seek hosted in the

**[58:26]** Yeah, we we have Deep Seek hosted in the

**[58:26]** Yeah, we we have Deep Seek hosted in the US. Um, so we've been trying that out.

**[58:28]** US. Um, so we've been trying that out.

**[58:28]** US. Um, so we've been trying that out. Um, I I think Llama has kind of fallen

**[58:31]** Um, I I think Llama has kind of fallen

**[58:31]** Um, I I think Llama has kind of fallen by the wayside a little bit. Um, and

**[58:33]** by the wayside a little bit. Um, and

**[58:33]** by the wayside a little bit. Um, and yeah, Deepseek is just, you know, the

**[58:35]** yeah, Deepseek is just, you know, the

**[58:35]** yeah, Deepseek is just, you know, the clear winner right now. Uh, they also

**[58:37]** clear winner right now. Uh, they also

**[58:37]** clear winner right now. Uh, they also released a new version there, I think,

**[58:38]** released a new version there, I think,

**[58:38]** released a new version there, I think, on the 28. Um, that's kind of up there

**[58:41]** on the 28. Um, that's kind of up there

**[58:41]** on the 28. Um, that's kind of up there with 03 level models. Um, we we actually

**[58:44]** with 03 level models. Um, we we actually

**[58:44]** with 03 level models. Um, we we actually don't use reasoning models uh for our

**[58:47]** don't use reasoning models uh for our

**[58:47]** don't use reasoning models uh for our agents. Um, a lot of the time when

**[58:49]** agents. Um, a lot of the time when

**[58:49]** agents. Um, a lot of the time when you're when you're building, you know,

**[58:51]** you're when you're building, you know,

**[58:51]** you're when you're building, you know, agentic agents, um, a reasoning model

**[58:54]** agentic agents, um, a reasoning model

**[58:54]** agentic agents, um, a reasoning model isn't really needed. Um, like unless you

**[58:57]** isn't really needed. Um, like unless you

**[58:58]** isn't really needed. Um, like unless you want to, you know, pay a fortune for


### [59:00 - 01:00:00]

**[59:00]** want to, you know, pay a fortune for

**[59:00]** want to, you know, pay a fortune for some long tiging task. Um, you know, we

**[59:03]** some long tiging task. Um, you know, we

**[59:03]** some long tiging task. Um, you know, we we we can achieve kind of that reasoning

**[59:06]** we we can achieve kind of that reasoning

**[59:06]** we we can achieve kind of that reasoning level uh, with just the standard models

**[59:08]** level uh, with just the standard models

**[59:08]** level uh, with just the standard models and and browse and a few other tools.

**[59:12]** and and browse and a few other tools.

**[59:12]** and and browse and a few other tools. Yeah.

**[59:12]** Yeah.

**[59:12]** Yeah. So, um, like a third party assume like

**[59:18]** So, um, like a third party assume like

**[59:18]** So, um, like a third party assume like if Stripe has an agent card and stuff,

**[59:21]** if Stripe has an agent card and stuff,

**[59:21]** if Stripe has an agent card and stuff, do you pass instructions for like what

**[59:25]** do you pass instructions for like what

**[59:26]** do you pass instructions for like what like exactly what you want back in terms

**[59:27]** like exactly what you want back in terms

**[59:27]** like exactly what you want back in terms of like I'm just imagining another third

**[59:30]** of like I'm just imagining another third

**[59:30]** of like I'm just imagining another third party agent blowing up your contact

**[59:31]** party agent blowing up your contact

**[59:31]** party agent blowing up your contact window because they're flooding you with

**[59:34]** window because they're flooding you with

**[59:34]** window because they're flooding you with information you don't care about. Do you

**[59:36]** information you don't care about. Do you

**[59:36]** information you don't care about. Do you handle that through the prompt? Are

**[59:37]** handle that through the prompt? Are

**[59:37]** handle that through the prompt? Are there other tools to do that issue?

**[59:40]** there other tools to do that issue?

**[59:40]** there other tools to do that issue? Yeah. So, uh, one of the solutions to

**[59:43]** Yeah. So, uh, one of the solutions to

**[59:43]** Yeah. So, uh, one of the solutions to that is you actually just spawn another

**[59:45]** that is you actually just spawn another

**[59:45]** that is you actually just spawn another agent, um, to communicate with either

**[59:47]** agent, um, to communicate with either

**[59:48]** agent, um, to communicate with either the tool or the agent, right? And that's

**[59:50]** the tool or the agent, right? And that's

**[59:50]** the tool or the agent, right? And that's one of the things we we have in in

**[59:52]** one of the things we we have in in

**[59:52]** one of the things we we have in in bench. Here's some of the slides that so

**[59:54]** bench. Here's some of the slides that so

**[59:54]** bench. Here's some of the slides that so I don't know uh, generate uh, five

**[59:59]** I don't know uh, generate uh, five

**[59:59]** I don't know uh, generate uh, five images


### [01:00:00 - 01:01:00]

**[01:00:08]** So you spawn a sub aent to sort of like

**[01:00:08]** So you spawn a sub aent to sort of like absorb the context flood for lack of a

**[01:00:10]** absorb the context flood for lack of a

**[01:00:10]** absorb the context flood for lack of a better term.

**[01:00:12]** better term.

**[01:00:12]** better term. Yeah. So the the sub aents just kind of

**[01:00:14]** Yeah. So the the sub aents just kind of

**[01:00:14]** Yeah. So the the sub aents just kind of protect you, right? Um and you know like

**[01:00:18]** protect you, right? Um and you know like

**[01:00:18]** protect you, right? Um and you know like when when you're spawning these things

**[01:00:19]** when when you're spawning these things

**[01:00:20]** when when you're spawning these things you can do things in parallel. Um

**[01:00:22]** you can do things in parallel. Um

**[01:00:22]** you can do things in parallel. Um actually if I expand you can see the

**[01:00:24]** actually if I expand you can see the

**[01:00:24]** actually if I expand you can see the thinking as well. So you can see like as

**[01:00:26]** thinking as well. So you can see like as

**[01:00:26]** thinking as well. So you can see like as it's going down through it, right? It's

**[01:00:28]** it's going down through it, right? It's

**[01:00:28]** it's going down through it, right? It's it's doing a lot of work um that you

**[01:00:30]** it's doing a lot of work um that you

**[01:00:30]** it's doing a lot of work um that you don't want in your context, right? like

**[01:00:32]** don't want in your context, right? like

**[01:00:32]** don't want in your context, right? like you you don't want all of your thoughts

**[01:00:34]** you you don't want all of your thoughts

**[01:00:34]** you you don't want all of your thoughts bloating your your context. Um but you

**[01:00:37]** bloating your your context. Um but you

**[01:00:37]** bloating your your context. Um but you also don't want all of your tools

**[01:00:38]** also don't want all of your tools

**[01:00:38]** also don't want all of your tools bloating your context either. Uh you

**[01:00:40]** bloating your context either. Uh you

**[01:00:40]** bloating your context either. Uh you don't want images bloating your context.

**[01:00:42]** don't want images bloating your context.

**[01:00:42]** don't want images bloating your context. You want the ability to analyze an image

**[01:00:44]** You want the ability to analyze an image

**[01:00:44]** You want the ability to analyze an image but you don't want like you know 100,000

**[01:00:47]** but you don't want like you know 100,000

**[01:00:47]** but you don't want like you know 100,000 characters B 64 in your context. So

**[01:00:50]** characters B 64 in your context. So

**[01:00:50]** characters B 64 in your context. So there's there's a lot of kind of

**[01:00:52]** there's there's a lot of kind of

**[01:00:52]** there's there's a lot of kind of optimizations that you can do there. Um

**[01:00:55]** optimizations that you can do there. Um

**[01:00:55]** optimizations that you can do there. Um but yeah did that kind of answer your

**[01:00:57]** but yeah did that kind of answer your

**[01:00:57]** but yeah did that kind of answer your question? Yeah.


### [01:01:00 - 01:02:00]

**[01:01:01]** If you to troubleshoot something like

**[01:01:02]** If you to troubleshoot something like this, it's probably

**[01:01:04]** this, it's probably

**[01:01:04]** this, it's probably Yeah. Yeah. So you can see here now it's

**[01:01:05]** Yeah. Yeah. So you can see here now it's

**[01:01:05]** Yeah. Yeah. So you can see here now it's spawning these subtasks. So these are

**[01:01:07]** spawning these subtasks. So these are

**[01:01:07]** spawning these subtasks. So these are all essentially like instances of bench

**[01:01:11]** all essentially like instances of bench

**[01:01:11]** all essentially like instances of bench that will keep that context out of out

**[01:01:13]** that will keep that context out of out

**[01:01:14]** that will keep that context out of out of my way, right? Yeah.

**[01:01:16]** of my way, right? Yeah.

**[01:01:16]** of my way, right? Yeah. Yeah.

**[01:01:16]** Yeah.

**[01:01:16]** Yeah. What have what you have been using for

**[01:01:19]** What have what you have been using for

**[01:01:19]** What have what you have been using for observability on your agents?

**[01:01:21]** observability on your agents?

**[01:01:22]** observability on your agents? Um we we just kind of roll our own right

**[01:01:24]** Um we we just kind of roll our own right

**[01:01:24]** Um we we just kind of roll our own right now. Uh there's a lot out there that you

**[01:01:26]** now. Uh there's a lot out there that you

**[01:01:26]** now. Uh there's a lot out there that you can use like uh agent ops is a pretty

**[01:01:28]** can use like uh agent ops is a pretty

**[01:01:28]** can use like uh agent ops is a pretty popular one. Um but yeah like if if you

**[01:01:31]** popular one. Um but yeah like if if you

**[01:01:31]** popular one. Um but yeah like if if you really want to build your own uh kind of

**[01:01:34]** really want to build your own uh kind of

**[01:01:34]** really want to build your own uh kind of custom observability layer um you know

**[01:01:37]** custom observability layer um you know

**[01:01:37]** custom observability layer um you know you're like like agent ops doesn't

**[01:01:38]** you're like like agent ops doesn't

**[01:01:38]** you're like like agent ops doesn't really support this concept of

**[01:01:40]** really support this concept of

**[01:01:40]** really support this concept of composable sub aents. Um so it's not

**[01:01:43]** composable sub aents. Um so it's not

**[01:01:43]** composable sub aents. Um so it's not really something that it could model uh

**[01:01:44]** really something that it could model uh

**[01:01:44]** really something that it could model uh correctly. Uh, but we've got some nice

**[01:01:46]** correctly. Uh, but we've got some nice

**[01:01:46]** correctly. Uh, but we've got some nice pictures of cats.

**[01:01:49]** pictures of cats.

**[01:01:50]** pictures of cats. Uh, and yeah, I know we have a few

**[01:01:51]** Uh, and yeah, I know we have a few

**[01:01:51]** Uh, and yeah, I know we have a few minutes left, but if if anybody's

**[01:01:53]** minutes left, but if if anybody's

**[01:01:53]** minutes left, but if if anybody's interested, um, I have $50 in free

**[01:01:56]** interested, um, I have $50 in free

**[01:01:56]** interested, um, I have $50 in free credits. Um, this hasn't launched yet,

**[01:01:59]** credits. Um, this hasn't launched yet,

**[01:01:59]** credits. Um, this hasn't launched yet, so you're getting kind of early access


### [01:02:00 - 01:03:00]

**[01:02:00]** so you're getting kind of early access

**[01:02:00]** so you're getting kind of early access to it. Um, and yeah, we'll I think we'll

**[01:02:04]** to it. Um, and yeah, we'll I think we'll

**[01:02:04]** to it. Um, and yeah, we'll I think we'll be in public beta in about two weeks.

**[01:02:07]** be in public beta in about two weeks.

**[01:02:07]** be in public beta in about two weeks. Um, so yeah, try it out. Like, hit me up

**[01:02:09]** Um, so yeah, try it out. Like, hit me up

**[01:02:09]** Um, so yeah, try it out. Like, hit me up on LinkedIn. I I'd love uh feedback from

**[01:02:11]** on LinkedIn. I I'd love uh feedback from

**[01:02:11]** on LinkedIn. I I'd love uh feedback from you all. you're you're all probably, you

**[01:02:13]** you all. you're you're all probably, you

**[01:02:13]** you all. you're you're all probably, you know, at the forefront of this uh AI

**[01:02:15]** know, at the forefront of this uh AI

**[01:02:15]** know, at the forefront of this uh AI stuff and um it's changing every day. So

**[01:02:18]** stuff and um it's changing every day. So

**[01:02:18]** stuff and um it's changing every day. So if you log in one day and it looks

**[01:02:20]** if you log in one day and it looks

**[01:02:20]** if you log in one day and it looks completely different, don't be

**[01:02:21]** completely different, don't be

**[01:02:21]** completely different, don't be surprised. Happens mid demo for me.

**[01:02:24]** surprised. Happens mid demo for me.

**[01:02:24]** surprised. Happens mid demo for me. Yeah.

**[01:02:25]** Yeah.

**[01:02:25]** Yeah. So you mentioned a lot how hiding

**[01:02:26]** So you mentioned a lot how hiding

**[01:02:26]** So you mentioned a lot how hiding context and sub agents is a good thing,

**[01:02:28]** context and sub agents is a good thing,

**[01:02:28]** context and sub agents is a good thing, but haven't you had cases where you

**[01:02:30]** but haven't you had cases where you

**[01:02:30]** but haven't you had cases where you actually then end up missing something

**[01:02:32]** actually then end up missing something

**[01:02:32]** actually then end up missing something important, some small detail, and then

**[01:02:35]** important, some small detail, and then

**[01:02:35]** important, some small detail, and then how do you resolve that? Does the agent

**[01:02:36]** how do you resolve that? Does the agent

**[01:02:36]** how do you resolve that? Does the agent actually go back and ask for that or do

**[01:02:38]** actually go back and ask for that or do

**[01:02:38]** actually go back and ask for that or do you

**[01:02:39]** you

**[01:02:39]** you Yeah. So you can keep references uh in

**[01:02:41]** Yeah. So you can keep references uh in

**[01:02:42]** Yeah. So you can keep references uh in your context. So you you might say

**[01:02:44]** your context. So you you might say

**[01:02:44]** your context. So you you might say subtask ID123

**[01:02:47]** subtask ID123

**[01:02:47]** subtask ID123 and then when the agent's like, "Oh, I

**[01:02:49]** and then when the agent's like, "Oh, I

**[01:02:49]** and then when the agent's like, "Oh, I wonder I wonder if I have this

**[01:02:51]** wonder I wonder if I have this

**[01:02:51]** wonder I wonder if I have this information. It's just not in my

**[01:02:52]** information. It's just not in my

**[01:02:52]** information. It's just not in my context." Right? And so it has to be

**[01:02:54]** context." Right? And so it has to be

**[01:02:54]** context." Right? And so it has to be smart enough to know when to actually go

**[01:02:57]** smart enough to know when to actually go

**[01:02:57]** smart enough to know when to actually go in and look at that. Um and it can be a

**[01:02:59]** in and look at that. Um and it can be a

**[01:02:59]** in and look at that. Um and it can be a sub agent that does that analysis,


### [01:03:00 - 01:04:00]

**[01:03:01]** sub agent that does that analysis,

**[01:03:01]** sub agent that does that analysis, right? So you could say, "Hey, sub

**[01:03:03]** right? So you could say, "Hey, sub

**[01:03:03]** right? So you could say, "Hey, sub agent, can you just look at all of these

**[01:03:05]** agent, can you just look at all of these

**[01:03:05]** agent, can you just look at all of these IDs and tell me if you can answer this

**[01:03:07]** IDs and tell me if you can answer this

**[01:03:08]** IDs and tell me if you can answer this question?"

**[01:03:10]** question?"

**[01:03:10]** question?" Yeah.

**[01:03:11]** Yeah.

**[01:03:11]** Yeah. there are a lot of

**[01:03:21]** right so you mentioned in the beginning

**[01:03:21]** right so you mentioned in the beginning about right so there are a lot of

**[01:03:24]** about right so there are a lot of

**[01:03:24]** about right so there are a lot of discussions saying that it's a way for

**[01:03:27]** discussions saying that it's a way for

**[01:03:27]** discussions saying that it's a way for using MCP for agent to agent

**[01:03:30]** using MCP for agent to agent

**[01:03:30]** using MCP for agent to agent communication right because the agent

**[01:03:32]** communication right because the agent

**[01:03:32]** communication right because the agent can be a service the client at the same

**[01:03:34]** can be a service the client at the same

**[01:03:34]** can be a service the client at the same time right

**[01:03:35]** time right

**[01:03:35]** time right so what is your opinion

**[01:03:38]** so what is your opinion

**[01:03:38]** so what is your opinion about that you know

**[01:03:41]** about that you know

**[01:03:41]** about that you know It's the million-dollar question, isn't

**[01:03:43]** It's the million-dollar question, isn't

**[01:03:43]** It's the million-dollar question, isn't it?

**[01:03:43]** it?

**[01:03:43]** it? Yes, that's that's why I asked.

**[01:03:45]** Yes, that's that's why I asked.

**[01:03:45]** Yes, that's that's why I asked. Yeah. And I I do think you can achieve

**[01:03:49]** Yeah. And I I do think you can achieve

**[01:03:49]** Yeah. And I I do think you can achieve easier agent agent communication with

**[01:03:53]** easier agent agent communication with

**[01:03:53]** easier agent agent communication with MCP. Um but if it's a remote MCP server,

**[01:03:57]** MCP. Um but if it's a remote MCP server,

**[01:03:57]** MCP. Um but if it's a remote MCP server, I think A2A actually is a little bit


### [01:04:00 - 01:05:00]

**[01:04:01]** I think A2A actually is a little bit

**[01:04:01]** I think A2A actually is a little bit better. Um because you have somebody

**[01:04:03]** better. Um because you have somebody

**[01:04:03]** better. Um because you have somebody else paying the the tokens and building

**[01:04:06]** else paying the the tokens and building

**[01:04:06]** else paying the the tokens and building the agent. Um, like if if all you're

**[01:04:08]** the agent. Um, like if if all you're

**[01:04:08]** the agent. Um, like if if all you're getting from a third party is a list of

**[01:04:11]** getting from a third party is a list of

**[01:04:11]** getting from a third party is a list of tools, um, those tools may not meet your

**[01:04:13]** tools, um, those tools may not meet your

**[01:04:14]** tools, um, those tools may not meet your needs. Um, but if you're getting a

**[01:04:16]** needs. Um, but if you're getting a

**[01:04:16]** needs. Um, but if you're getting a fullyfledged agent from that third

**[01:04:18]** fullyfledged agent from that third

**[01:04:18]** fullyfledged agent from that third party, then it might be able to figure

**[01:04:20]** party, then it might be able to figure

**[01:04:20]** party, then it might be able to figure out like what it can do with with even

**[01:04:23]** out like what it can do with with even

**[01:04:23]** out like what it can do with with even private APIs, right? Maybe maybe that

**[01:04:25]** private APIs, right? Maybe maybe that

**[01:04:25]** private APIs, right? Maybe maybe that agent has direct database base access

**[01:04:27]** agent has direct database base access

**[01:04:27]** agent has direct database base access and it's able to actually on the fly,

**[01:04:30]** and it's able to actually on the fly,

**[01:04:30]** and it's able to actually on the fly, you know, create the API you need,

**[01:04:33]** you know, create the API you need,

**[01:04:33]** you know, create the API you need, right? So, so the tradeoffs basically

**[01:04:35]** right? So, so the tradeoffs basically

**[01:04:35]** right? So, so the tradeoffs basically about

**[01:04:37]** about

**[01:04:37]** about which is important about cost and who

**[01:04:39]** which is important about cost and who

**[01:04:39]** which is important about cost and who going to pay the for the tokens and

**[01:04:41]** going to pay the for the tokens and

**[01:04:42]** going to pay the for the tokens and whatever something like that can be like

**[01:04:44]** whatever something like that can be like

**[01:04:44]** whatever something like that can be like you're running the server maybe using

**[01:04:47]** you're running the server maybe using

**[01:04:47]** you're running the server maybe using MCP going to be easier but am I correct

**[01:04:52]** MCP going to be easier but am I correct

**[01:04:52]** MCP going to be easier but am I correct I don't know if I know at the end of the

**[01:04:55]** I don't know if I know at the end of the

**[01:04:55]** I don't know if I know at the end of the day who's going to pay for the tokens

**[01:04:58]** day who's going to pay for the tokens

**[01:04:58]** day who's going to pay for the tokens right

**[01:04:59]** right


### [01:05:00 - 01:06:00]

**[01:05:00]** right yeah and I think who pays for the tokens

**[01:05:01]** yeah and I think who pays for the tokens

**[01:05:02]** yeah and I think who pays for the tokens is kind of secondary Right? Like at the

**[01:05:03]** is kind of secondary Right? Like at the

**[01:05:03]** is kind of secondary Right? Like at the end of the day, it's about business

**[01:05:04]** end of the day, it's about business

**[01:05:04]** end of the day, it's about business value. And if you can get the business

**[01:05:06]** value. And if you can get the business

**[01:05:06]** value. And if you can get the business value from a tool, right, like send

**[01:05:09]** value from a tool, right, like send

**[01:05:09]** value from a tool, right, like send Slack message, um like that's great,

**[01:05:11]** Slack message, um like that's great,

**[01:05:12]** Slack message, um like that's great, right? Like sending a Slack message

**[01:05:13]** right? Like sending a Slack message

**[01:05:13]** right? Like sending a Slack message isn't hard. Um but the implementation of

**[01:05:16]** isn't hard. Um but the implementation of

**[01:05:16]** isn't hard. Um but the implementation of the search function of Slack is is

**[01:05:18]** the search function of Slack is is

**[01:05:18]** the search function of Slack is is actually not great, right? Um whereas

**[01:05:20]** actually not great, right? Um whereas

**[01:05:20]** actually not great, right? Um whereas compare that to some of the other uh MCB

**[01:05:22]** compare that to some of the other uh MCB

**[01:05:22]** compare that to some of the other uh MCB tools like Linear, uh the search

**[01:05:24]** tools like Linear, uh the search

**[01:05:24]** tools like Linear, uh the search function is actually pretty good, right?

**[01:05:26]** function is actually pretty good, right?

**[01:05:26]** function is actually pretty good, right? Um but then you you start to run into

**[01:05:28]** Um but then you you start to run into

**[01:05:28]** Um but then you you start to run into performance uh challenges as well. So

**[01:05:31]** performance uh challenges as well. So

**[01:05:31]** performance uh challenges as well. So like if I want to search 100,000

**[01:05:33]** like if I want to search 100,000

**[01:05:33]** like if I want to search 100,000 opportunities in Salesforce um and

**[01:05:35]** opportunities in Salesforce um and

**[01:05:35]** opportunities in Salesforce um and figure out like what's the close loss

**[01:05:37]** figure out like what's the close loss

**[01:05:37]** figure out like what's the close loss reason counts and categorize them and do

**[01:05:39]** reason counts and categorize them and do

**[01:05:39]** reason counts and categorize them and do all of that like that that's a huge data

**[01:05:42]** all of that like that that's a huge data

**[01:05:42]** all of that like that that's a huge data processing challenge. MCP is not going

**[01:05:44]** processing challenge. MCP is not going

**[01:05:44]** processing challenge. MCP is not going to be the right uh tool for that because

**[01:05:46]** to be the right uh tool for that because

**[01:05:46]** to be the right uh tool for that because you're you're essentially going to say

**[01:05:47]** you're you're essentially going to say

**[01:05:47]** you're you're essentially going to say okay list opportunities now get the

**[01:05:50]** okay list opportunities now get the

**[01:05:50]** okay list opportunities now get the details of each opportunity right and

**[01:05:52]** details of each opportunity right and

**[01:05:52]** details of each opportunity right and you're going to make like 100,000

**[01:05:53]** you're going to make like 100,000

**[01:05:53]** you're going to make like 100,000 network calls. Um, at that point you're

**[01:05:55]** network calls. Um, at that point you're

**[01:05:55]** network calls. Um, at that point you're really going to want to actually, you

**[01:05:57]** really going to want to actually, you

**[01:05:57]** really going to want to actually, you know, ingest that data, you know, build

**[01:05:59]** know, ingest that data, you know, build

**[01:05:59]** know, ingest that data, you know, build an index, right? And I think, and this


### [01:06:00 - 01:07:00]

**[01:06:02]** an index, right? And I think, and this

**[01:06:02]** an index, right? And I think, and this is kind of like an idea, is like we we

**[01:06:05]** is kind of like an idea, is like we we

**[01:06:05]** is kind of like an idea, is like we we may see a lot of these third party

**[01:06:08]** may see a lot of these third party

**[01:06:08]** may see a lot of these third party software providers essentially just

**[01:06:10]** software providers essentially just

**[01:06:10]** software providers essentially just allow you to access the data lake

**[01:06:13]** allow you to access the data lake

**[01:06:13]** allow you to access the data lake through an agent, right? Um, so like

**[01:06:15]** through an agent, right? Um, so like

**[01:06:16]** through an agent, right? Um, so like scoped data access, you know, just

**[01:06:17]** scoped data access, you know, just

**[01:06:18]** scoped data access, you know, just running complex queries super fast, you

**[01:06:20]** running complex queries super fast, you

**[01:06:20]** running complex queries super fast, you know, no no real like tool calls per se,

**[01:06:23]** know, no no real like tool calls per se,

**[01:06:23]** know, no no real like tool calls per se, but just like ask me a question and I'll

**[01:06:26]** but just like ask me a question and I'll

**[01:06:26]** but just like ask me a question and I'll go figure out how to get the answer.

**[01:06:29]** go figure out how to get the answer.

**[01:06:29]** go figure out how to get the answer. Yeah.

**[01:06:31]** Yeah.

**[01:06:31]** Yeah. Yeah.

**[01:06:56]** Yeah. So, you can achieve the same with

**[01:06:56]** Yeah. So, you can achieve the same with at or with MCP. So, you could just have

**[01:06:59]** at or with MCP. So, you could just have

**[01:06:59]** at or with MCP. So, you could just have a a tool that's called talk to sub


### [01:07:00 - 01:08:00]

**[01:07:02]** a a tool that's called talk to sub

**[01:07:02]** a a tool that's called talk to sub agent, right? Um and and it can work as

**[01:07:05]** agent, right? Um and and it can work as

**[01:07:05]** agent, right? Um and and it can work as the communication protocol. Um I

**[01:07:08]** the communication protocol. Um I

**[01:07:08]** the communication protocol. Um I actually built another uh application

**[01:07:10]** actually built another uh application

**[01:07:10]** actually built another uh application where I had an LLM uh claude 4 um just

**[01:07:14]** where I had an LLM uh claude 4 um just

**[01:07:14]** where I had an LLM uh claude 4 um just talk to its predecessor um just to see

**[01:07:16]** talk to its predecessor um just to see

**[01:07:16]** talk to its predecessor um just to see what would happen. Uh and then I did it

**[01:07:17]** what would happen. Uh and then I did it

**[01:07:17]** what would happen. Uh and then I did it for all the Frontier models. I was like

**[01:07:19]** for all the Frontier models. I was like

**[01:07:19]** for all the Frontier models. I was like hey look just have have 50 chat turns

**[01:07:21]** hey look just have have 50 chat turns

**[01:07:21]** hey look just have have 50 chat turns with your predecessor. Um and it was all

**[01:07:23]** with your predecessor. Um and it was all

**[01:07:23]** with your predecessor. Um and it was all done through uh MCP. Um Claude was the

**[01:07:27]** done through uh MCP. Um Claude was the

**[01:07:27]** done through uh MCP. Um Claude was the only one that taught it became

**[01:07:28]** only one that taught it became

**[01:07:28]** only one that taught it became conscious. Uh Claude Opus actually

**[01:07:30]** conscious. Uh Claude Opus actually

**[01:07:30]** conscious. Uh Claude Opus actually didn't which was strange.

**[01:07:34]** didn't which was strange.

**[01:07:34]** didn't which was strange. Yeah. as a developer right like how much

**[01:07:36]** Yeah. as a developer right like how much

**[01:07:36]** Yeah. as a developer right like how much control do you have over the

**[01:07:37]** control do you have over the

**[01:07:37]** control do you have over the orchestration

**[01:07:39]** orchestration

**[01:07:39]** orchestration so is the orchestration done by the LLM

**[01:07:41]** so is the orchestration done by the LLM

**[01:07:41]** so is the orchestration done by the LLM or do you have some control over

**[01:07:43]** or do you have some control over

**[01:07:43]** or do you have some control over yes so you're prompting the host on how

**[01:07:46]** yes so you're prompting the host on how

**[01:07:46]** yes so you're prompting the host on how to run the orchestration and that's

**[01:07:49]** to run the orchestration and that's

**[01:07:49]** to run the orchestration and that's probably one of the limitations I think

**[01:07:50]** probably one of the limitations I think

**[01:07:50]** probably one of the limitations I think as well of the the system is that like

**[01:07:53]** as well of the the system is that like

**[01:07:53]** as well of the the system is that like you're you're leaving it up to an LLM to

**[01:07:55]** you're you're leaving it up to an LLM to

**[01:07:55]** you're you're leaving it up to an LLM to make decisions um and a lot of the time

**[01:07:58]** make decisions um and a lot of the time

**[01:07:58]** make decisions um and a lot of the time like you know if you run that that same


### [01:08:00 - 01:09:00]

**[01:08:01]** like you know if you run that that same

**[01:08:01]** like you know if you run that that same uh query multiple times you you'll get

**[01:08:03]** uh query multiple times you you'll get

**[01:08:03]** uh query multiple times you you'll get different results right? Like you know

**[01:08:05]** different results right? Like you know

**[01:08:05]** different results right? Like you know it's the exact same thing but it's like

**[01:08:08]** it's the exact same thing but it's like

**[01:08:08]** it's the exact same thing but it's like producing

**[01:08:10]** producing

**[01:08:10]** producing uh different outputs right like uh if I

**[01:08:13]** uh different outputs right like uh if I

**[01:08:13]** uh different outputs right like uh if I go into the uh GitHub issues uh I've al

**[01:08:17]** go into the uh GitHub issues uh I've al

**[01:08:17]** go into the uh GitHub issues uh I've al obviously been testing this a lot of 151

**[01:08:20]** obviously been testing this a lot of 151

**[01:08:20]** obviously been testing this a lot of 151 like it submits different issues right

**[01:08:23]** like it submits different issues right

**[01:08:23]** like it submits different issues right um and I think that non-determinism is

**[01:08:26]** um and I think that non-determinism is

**[01:08:26]** um and I think that non-determinism is is a challenge like maybe with changing

**[01:08:28]** is a challenge like maybe with changing

**[01:08:28]** is a challenge like maybe with changing the temperature you could kind of beat

**[01:08:29]** the temperature you could kind of beat

**[01:08:29]** the temperature you could kind of beat it out of it but you know the

**[01:08:31]** it out of it but you know the

**[01:08:31]** it out of it but you know the temperature is kind of the the beauty of

**[01:08:33]** temperature is kind of the the beauty of

**[01:08:33]** temperature is kind of the the beauty of LLMs

**[01:08:35]** LLMs

**[01:08:35]** LLMs And also on the context right like who

**[01:08:37]** And also on the context right like who

**[01:08:37]** And also on the context right like who is managing the context is the

**[01:08:39]** is managing the context is the

**[01:08:39]** is managing the context is the orchestration engine managing the

**[01:08:40]** orchestration engine managing the

**[01:08:40]** orchestration engine managing the context or are you managing the

**[01:08:43]** context or are you managing the

**[01:08:43]** context or are you managing the developer? Yeah. So, so in this

**[01:08:45]** developer? Yeah. So, so in this

**[01:08:45]** developer? Yeah. So, so in this codebase, I didn't do any prompt

**[01:08:46]** codebase, I didn't do any prompt

**[01:08:46]** codebase, I didn't do any prompt caching. I just and it's a very small

**[01:08:48]** caching. I just and it's a very small

**[01:08:48]** caching. I just and it's a very small system prompt. It's a very small kind of

**[01:08:50]** system prompt. It's a very small kind of

**[01:08:50]** system prompt. It's a very small kind of turn taking. Um, every time you restart,

**[01:08:54]** turn taking. Um, every time you restart,

**[01:08:54]** turn taking. Um, every time you restart, uh, the system, it basically just wipes

**[01:08:56]** uh, the system, it basically just wipes

**[01:08:56]** uh, the system, it basically just wipes everything anyways. So, uh, it's super

**[01:08:58]** everything anyways. So, uh, it's super

**[01:08:58]** everything anyways. So, uh, it's super lean. But as you build out more complex


### [01:09:00 - 01:10:00]

**[01:09:00]** lean. But as you build out more complex

**[01:09:00]** lean. But as you build out more complex systems, uh, you know, context growth is

**[01:09:03]** systems, uh, you know, context growth is

**[01:09:03]** systems, uh, you know, context growth is probably the number one challenge

**[01:09:05]** probably the number one challenge

**[01:09:05]** probably the number one challenge because, you know, context growth

**[01:09:07]** because, you know, context growth

**[01:09:07]** because, you know, context growth becomes cost and cost becomes

**[01:09:09]** becomes cost and cost becomes

**[01:09:09]** becomes cost and cost becomes profitability, right?

**[01:09:11]** profitability, right?

**[01:09:11]** profitability, right? Yeah. And also like when you have like

**[01:09:13]** Yeah. And also like when you have like

**[01:09:13]** Yeah. And also like when you have like multiple users using the same

**[01:09:14]** multiple users using the same

**[01:09:14]** multiple users using the same application, right? So let's say like

**[01:09:16]** application, right? So let's say like

**[01:09:16]** application, right? So let's say like the Salesforce agent behind the scenes

**[01:09:18]** the Salesforce agent behind the scenes

**[01:09:18]** the Salesforce agent behind the scenes as an employee a I might have access to

**[01:09:20]** as an employee a I might have access to

**[01:09:20]** as an employee a I might have access to like one set of like context and the

**[01:09:23]** like one set of like context and the

**[01:09:23]** like one set of like context and the other user they might have like they

**[01:09:26]** other user they might have like they

**[01:09:26]** other user they might have like they might be from a different department and

**[01:09:27]** might be from a different department and

**[01:09:27]** might be from a different department and they can only query their department's

**[01:09:29]** they can only query their department's

**[01:09:29]** they can only query their department's data.

**[01:09:29]** data.

**[01:09:30]** data. Mhm.

**[01:09:30]** Mhm.

**[01:09:30]** Mhm. So how do you control that?

**[01:09:32]** So how do you control that?

**[01:09:32]** So how do you control that? Yeah. That would typically be oat,

**[01:09:34]** Yeah. That would typically be oat,

**[01:09:34]** Yeah. That would typically be oat, right? So so when you go in and you log

**[01:09:36]** right? So so when you go in and you log

**[01:09:36]** right? So so when you go in and you log in with Google

**[01:09:37]** in with Google

**[01:09:37]** in with Google based on my token.

**[01:09:38]** based on my token.

**[01:09:38]** based on my token. Yeah. Yeah. So based on your token and

**[01:09:40]** Yeah. Yeah. So based on your token and

**[01:09:40]** Yeah. Yeah. So based on your token and the the context would only get populated

**[01:09:43]** the the context would only get populated

**[01:09:43]** the the context would only get populated when you ask a question. So it's when

**[01:09:45]** when you ask a question. So it's when

**[01:09:45]** when you ask a question. So it's when you ask that question, it's then going

**[01:09:47]** you ask that question, it's then going

**[01:09:47]** you ask that question, it's then going off to get the data with your OA token

**[01:09:50]** off to get the data with your OA token

**[01:09:50]** off to get the data with your OA token and then bringing back your your kind of

**[01:09:52]** and then bringing back your your kind of

**[01:09:52]** and then bringing back your your kind of scoped data.

**[01:09:53]** scoped data.

**[01:09:53]** scoped data. I see.

**[01:09:53]** I see.

**[01:09:53]** I see. Yeah.

**[01:09:55]** Yeah.

**[01:09:55]** Yeah. Yeah.

**[01:09:56]** Yeah.

**[01:09:56]** Yeah. Yeah. I was curious about your thoughts

**[01:09:58]** Yeah. I was curious about your thoughts

**[01:09:58]** Yeah. I was curious about your thoughts on you touched on it briefly about


### [01:10:00 - 01:11:00]

**[01:10:00]** on you touched on it briefly about

**[01:10:00]** on you touched on it briefly about exposing let's say like the agent as

**[01:10:03]** exposing let's say like the agent as

**[01:10:03]** exposing let's say like the agent as like an MTP server as one of an

**[01:10:05]** like an MTP server as one of an

**[01:10:05]** like an MTP server as one of an alternate interface to that. So there

**[01:10:08]** alternate interface to that. So there

**[01:10:08]** alternate interface to that. So there isn't a lot of great integrations for

**[01:10:10]** isn't a lot of great integrations for

**[01:10:10]** isn't a lot of great integrations for things like desktop and other things to

**[01:10:12]** things like desktop and other things to

**[01:10:12]** things like desktop and other things to use that. Is that something you've been

**[01:10:14]** use that. Is that something you've been

**[01:10:14]** use that. Is that something you've been thinking about? Like

**[01:10:15]** thinking about? Like

**[01:10:15]** thinking about? Like yeah, we're we're probably going to do

**[01:10:17]** yeah, we're we're probably going to do

**[01:10:17]** yeah, we're we're probably going to do MCP uh first. Um I I just built the A2A

**[01:10:21]** MCP uh first. Um I I just built the A2A

**[01:10:21]** MCP uh first. Um I I just built the A2A wrapper uh for this, but yeah, I think

**[01:10:23]** wrapper uh for this, but yeah, I think

**[01:10:23]** wrapper uh for this, but yeah, I think just being able to drop it into cloud

**[01:10:25]** just being able to drop it into cloud

**[01:10:25]** just being able to drop it into cloud desktop or open AI or whatever and then

**[01:10:28]** desktop or open AI or whatever and then

**[01:10:28]** desktop or open AI or whatever and then you have access to that kind of agent

**[01:10:30]** you have access to that kind of agent

**[01:10:30]** you have access to that kind of agent that has access to, you know, all your

**[01:10:32]** that has access to, you know, all your

**[01:10:32]** that has access to, you know, all your sub tools. Uh, one of the cool things

**[01:10:34]** sub tools. Uh, one of the cool things

**[01:10:34]** sub tools. Uh, one of the cool things about uh, Bench actually is that you can

**[01:10:36]** about uh, Bench actually is that you can

**[01:10:36]** about uh, Bench actually is that you can connect it to um, your uh, Slack, your

**[01:10:41]** connect it to um, your uh, Slack, your

**[01:10:42]** connect it to um, your uh, Slack, your GitHub, your Salesforce, right? Uh,

**[01:10:43]** GitHub, your Salesforce, right? Uh,

**[01:10:44]** GitHub, your Salesforce, right? Uh, we've even got this experimental meme

**[01:10:45]** we've even got this experimental meme

**[01:10:45]** we've even got this experimental meme server. Um, this is like a remote uh, VM

**[01:10:50]** server. Um, this is like a remote uh, VM

**[01:10:50]** server. Um, this is like a remote uh, VM uh, MCP that I wrote around the morph

**[01:10:52]** uh, MCP that I wrote around the morph

**[01:10:52]** uh, MCP that I wrote around the morph cloud. Um, and this is really cool

**[01:10:54]** cloud. Um, and this is really cool

**[01:10:54]** cloud. Um, and this is really cool because then you can ask like super

**[01:10:55]** because then you can ask like super

**[01:10:56]** because then you can ask like super complex stuff, right? Like you can ask

**[01:10:57]** complex stuff, right? Like you can ask

**[01:10:57]** complex stuff, right? Like you can ask like, hey, give me a daily briefing of


### [01:11:00 - 01:12:00]

**[01:11:00]** like, hey, give me a daily briefing of

**[01:11:00]** like, hey, give me a daily briefing of my email, of my calendar, of my Slack,

**[01:11:02]** my email, of my calendar, of my Slack,

**[01:11:02]** my email, of my calendar, of my Slack, right? you know, uh, what do I need to

**[01:11:04]** right? you know, uh, what do I need to

**[01:11:04]** right? you know, uh, what do I need to do today? Um, and then it's all built

**[01:11:06]** do today? Um, and then it's all built

**[01:11:06]** do today? Um, and then it's all built around a team as well. So, we have, uh,

**[01:11:08]** around a team as well. So, we have, uh,

**[01:11:08]** around a team as well. So, we have, uh, teams integrations. Um, yeah.

**[01:11:11]** teams integrations. Um, yeah.

**[01:11:11]** teams integrations. Um, yeah. And is that like delegating to your

**[01:11:15]** And is that like delegating to your

**[01:11:15]** And is that like delegating to your So, there's no A2A today in bench. It's

**[01:11:17]** So, there's no A2A today in bench. It's

**[01:11:17]** So, there's no A2A today in bench. It's it's all MCP.

**[01:11:18]** it's all MCP.

**[01:11:18]** it's all MCP. Got it.

**[01:11:18]** Got it.

**[01:11:18]** Got it. Yeah. Yeah. And I think the big takeaway

**[01:11:21]** Yeah. Yeah. And I think the big takeaway

**[01:11:21]** Yeah. Yeah. And I think the big takeaway from this is like, you know, A2A is very

**[01:11:24]** from this is like, you know, A2A is very

**[01:11:24]** from this is like, you know, A2A is very early. It's it's kind of where MCP was,

**[01:11:27]** early. It's it's kind of where MCP was,

**[01:11:27]** early. It's it's kind of where MCP was, you know, four or five months ago, which

**[01:11:28]** you know, four or five months ago, which

**[01:11:28]** you know, four or five months ago, which is like, you know, forever in AI. Um, so

**[01:11:31]** is like, you know, forever in AI. Um, so

**[01:11:31]** is like, you know, forever in AI. Um, so it's it's going to take a bit of time.

**[01:11:33]** it's it's going to take a bit of time.

**[01:11:33]** it's it's going to take a bit of time. Um, I'm really excited though to see

**[01:11:34]** Um, I'm really excited though to see

**[01:11:34]** Um, I'm really excited though to see what, you know, Salesforce release and

**[01:11:36]** what, you know, Salesforce release and

**[01:11:36]** what, you know, Salesforce release and and all the partners that they partnered

**[01:11:38]** and all the partners that they partnered

**[01:11:38]** and all the partners that they partnered with. Um, I don't know if it was just a,

**[01:11:41]** with. Um, I don't know if it was just a,

**[01:11:41]** with. Um, I don't know if it was just a, you know, a flashy like we're partnering

**[01:11:42]** you know, a flashy like we're partnering

**[01:11:42]** you know, a flashy like we're partnering with everybody kind of announcement, but

**[01:11:44]** with everybody kind of announcement, but

**[01:11:44]** with everybody kind of announcement, but um, if they do release it, uh, you know,

**[01:11:46]** um, if they do release it, uh, you know,

**[01:11:46]** um, if they do release it, uh, you know, there could be a lot more powerful

**[01:11:48]** there could be a lot more powerful

**[01:11:48]** there could be a lot more powerful things you can do over A to A versus

**[01:11:50]** things you can do over A to A versus

**[01:11:50]** things you can do over A to A versus MCP. Um but the you know the fact that

**[01:11:53]** MCP. Um but the you know the fact that

**[01:11:53]** MCP. Um but the you know the fact that Zapier now has um sorry in here yeah it

**[01:11:57]** Zapier now has um sorry in here yeah it

**[01:11:57]** Zapier now has um sorry in here yeah it has this instructions um this kind of

**[01:11:59]** has this instructions um this kind of


### [01:12:00 - 01:13:00]

**[01:12:00]** has this instructions um this kind of acts like like a remote agent right like

**[01:12:02]** acts like like a remote agent right like

**[01:12:02]** acts like like a remote agent right like you can you can just describe in natural

**[01:12:04]** you can you can just describe in natural

**[01:12:04]** you can you can just describe in natural language what you want it to do um and

**[01:12:07]** language what you want it to do um and

**[01:12:07]** language what you want it to do um and like maybe all the other fields just go

**[01:12:10]** like maybe all the other fields just go

**[01:12:10]** like maybe all the other fields just go away then right but then you're at the

**[01:12:11]** away then right but then you're at the

**[01:12:11]** away then right but then you're at the at the whim at the LLM.

**[01:12:14]** at the whim at the LLM.

**[01:12:14]** at the whim at the LLM. Yeah,

**[01:12:14]** Yeah,

**[01:12:14]** Yeah, this one's kind of a random question. Um

**[01:12:16]** this one's kind of a random question. Um

**[01:12:16]** this one's kind of a random question. Um I'm curious if you're seeing anybody do

**[01:12:18]** I'm curious if you're seeing anybody do

**[01:12:18]** I'm curious if you're seeing anybody do anything interesting from like an

**[01:12:19]** anything interesting from like an

**[01:12:19]** anything interesting from like an architecture perspective uh to get info

**[01:12:23]** architecture perspective uh to get info

**[01:12:23]** architecture perspective uh to get info that can only come from humans. So one

**[01:12:25]** that can only come from humans. So one

**[01:12:25]** that can only come from humans. So one of the things we've been testing is

**[01:12:27]** of the things we've been testing is

**[01:12:27]** of the things we've been testing is essentially making individual team

**[01:12:29]** essentially making individual team

**[01:12:29]** essentially making individual team members like the CFO CFO whatever tools

**[01:12:32]** members like the CFO CFO whatever tools

**[01:12:32]** members like the CFO CFO whatever tools of one of the agents and when it needs

**[01:12:34]** of one of the agents and when it needs

**[01:12:34]** of one of the agents and when it needs something that isn't in some other

**[01:12:36]** something that isn't in some other

**[01:12:36]** something that isn't in some other system only the CFO would have it

**[01:12:38]** system only the CFO would have it

**[01:12:38]** system only the CFO would have it literally messages uh the CFO like the

**[01:12:41]** literally messages uh the CFO like the

**[01:12:41]** literally messages uh the CFO like the actual tool is just a slack but the the

**[01:12:44]** actual tool is just a slack but the the

**[01:12:44]** actual tool is just a slack but the the CFO is described as a tool. So we're

**[01:12:46]** CFO is described as a tool. So we're

**[01:12:46]** CFO is described as a tool. So we're essentially making like the human the

**[01:12:48]** essentially making like the human the

**[01:12:48]** essentially making like the human the tool the agent rather than the other way

**[01:12:49]** tool the agent rather than the other way

**[01:12:49]** tool the agent rather than the other way around. Um, it's early days in terms of

**[01:12:52]** around. Um, it's early days in terms of

**[01:12:52]** around. Um, it's early days in terms of how we're testing. We're a little hacky

**[01:12:53]** how we're testing. We're a little hacky

**[01:12:53]** how we're testing. We're a little hacky with it, but I'm curious if you're

**[01:12:55]** with it, but I'm curious if you're

**[01:12:55]** with it, but I'm curious if you're seeing how how are you seeing people

**[01:12:57]** seeing how how are you seeing people

**[01:12:57]** seeing how how are you seeing people fill the gap of things that only the

**[01:12:59]** fill the gap of things that only the

**[01:12:59]** fill the gap of things that only the humans would have while giving that back


### [01:13:00 - 01:14:00]

**[01:13:02]** humans would have while giving that back

**[01:13:02]** humans would have while giving that back to the agent.

**[01:13:03]** to the agent.

**[01:13:03]** to the agent. Yeah. And I think voice agents is a good

**[01:13:05]** Yeah. And I think voice agents is a good

**[01:13:05]** Yeah. And I think voice agents is a good example where like you could have a tool

**[01:13:08]** example where like you could have a tool

**[01:13:08]** example where like you could have a tool and and I had it integrated with Bench

**[01:13:09]** and and I had it integrated with Bench

**[01:13:09]** and and I had it integrated with Bench where like it makes an outbound phone

**[01:13:11]** where like it makes an outbound phone

**[01:13:11]** where like it makes an outbound phone call and finds out some information and

**[01:13:14]** call and finds out some information and

**[01:13:14]** call and finds out some information and then brings it back, right? So you can

**[01:13:15]** then brings it back, right? So you can

**[01:13:15]** then brings it back, right? So you can you can have those scenarios. Um, you

**[01:13:18]** you can have those scenarios. Um, you

**[01:13:18]** you can have those scenarios. Um, you may want two-way communication to avoid

**[01:13:20]** may want two-way communication to avoid

**[01:13:20]** may want two-way communication to avoid just like hanging around for a long

**[01:13:22]** just like hanging around for a long

**[01:13:22]** just like hanging around for a long time. Um, so you could have, you know,

**[01:13:24]** time. Um, so you could have, you know,

**[01:13:24]** time. Um, so you could have, you know, your agent be both a client and a server

**[01:13:27]** your agent be both a client and a server

**[01:13:27]** your agent be both a client and a server and maybe it gets called with like, you

**[01:13:28]** and maybe it gets called with like, you

**[01:13:28]** and maybe it gets called with like, you know, a task ID and it's like, hey, I

**[01:13:30]** know, a task ID and it's like, hey, I

**[01:13:30]** know, a task ID and it's like, hey, I got the response.

**[01:13:31]** got the response.

**[01:13:31]** got the response. Yeah. Yeah. We've been doing like a like

**[01:13:33]** Yeah. Yeah. We've been doing like a like

**[01:13:33]** Yeah. Yeah. We've been doing like a like a node essentially. We use likely

**[01:13:37]** a node essentially. We use likely

**[01:13:37]** a node essentially. We use likely and we've been using their

**[01:13:39]** and we've been using their

**[01:13:39]** and we've been using their weight.

**[01:13:44]** Yeah. hesitations on it.

**[01:13:44]** Yeah. hesitations on it. I I believe with sampling you could hack

**[01:13:47]** I I believe with sampling you could hack

**[01:13:47]** I I believe with sampling you could hack that together. So So sampling can take

**[01:13:49]** that together. So So sampling can take

**[01:13:49]** that together. So So sampling can take user input as well as LLM uh responses.

**[01:13:54]** user input as well as LLM uh responses.

**[01:13:54]** user input as well as LLM uh responses. It's also interesting the spec too is

**[01:13:55]** It's also interesting the spec too is

**[01:13:56]** It's also interesting the spec too is evolving like I follow the spec pretty

**[01:13:58]** evolving like I follow the spec pretty

**[01:13:58]** evolving like I follow the spec pretty closely and they have that elicitation


### [01:14:00 - 01:15:00]

**[01:14:01]** closely and they have that elicitation

**[01:14:01]** closely and they have that elicitation is a new feature that they're adding

**[01:14:03]** is a new feature that they're adding

**[01:14:03]** is a new feature that they're adding where you can get input from the user.

**[01:14:05]** where you can get input from the user.

**[01:14:05]** where you can get input from the user. Is it architected that way where it's

**[01:14:07]** Is it architected that way where it's

**[01:14:07]** Is it architected that way where it's essentially like it functions like a

**[01:14:09]** essentially like it functions like a

**[01:14:09]** essentially like it functions like a tool like that's how you think of it

**[01:14:10]** tool like that's how you think of it

**[01:14:10]** tool like that's how you think of it from an architect? It's a new kind of

**[01:14:12]** from an architect? It's a new kind of

**[01:14:12]** from an architect? It's a new kind of protocol message where it sends it back

**[01:14:14]** protocol message where it sends it back

**[01:14:14]** protocol message where it sends it back from the server to the client and it

**[01:14:16]** from the server to the client and it

**[01:14:16]** from the server to the client and it asks for information from the user

**[01:14:18]** asks for information from the user

**[01:14:18]** asks for information from the user and then it continues after that.

**[01:14:21]** and then it continues after that.

**[01:14:21]** and then it continues after that. Yeah, I feel like that opens up the

**[01:14:23]** Yeah, I feel like that opens up the

**[01:14:23]** Yeah, I feel like that opens up the scope of like what the agent could do if

**[01:14:26]** scope of like what the agent could do if

**[01:14:26]** scope of like what the agent could do if you have a clear way for it to get

**[01:14:28]** you have a clear way for it to get

**[01:14:28]** you have a clear way for it to get information

**[01:14:31]** information

**[01:14:31]** information or

**[01:14:33]** or

**[01:14:33]** or Yeah. And then the the CFO is gonna have

**[01:14:35]** Yeah. And then the the CFO is gonna have

**[01:14:35]** Yeah. And then the the CFO is gonna have his own agent respond.

**[01:14:49]** Yeah, very very difficultly.

**[01:14:49]** Yeah, very very difficultly. Um I I have a set of prompts that I use

**[01:14:52]** Um I I have a set of prompts that I use

**[01:14:52]** Um I I have a set of prompts that I use and kind of monitor, you know, how the

**[01:14:54]** and kind of monitor, you know, how the

**[01:14:54]** and kind of monitor, you know, how the context grows like when did we when did

**[01:14:57]** context grows like when did we when did

**[01:14:57]** context grows like when did we when did we move the cache marker, how much did

**[01:14:59]** we move the cache marker, how much did

**[01:14:59]** we move the cache marker, how much did it cost, you know, what was the context


### [01:15:00 - 01:16:00]

**[01:15:01]** it cost, you know, what was the context

**[01:15:01]** it cost, you know, what was the context per tool. Um you know, definitely adding

**[01:15:04]** per tool. Um you know, definitely adding

**[01:15:04]** per tool. Um you know, definitely adding MCP servers willy-nilly is going to like

**[01:15:07]** MCP servers willy-nilly is going to like

**[01:15:07]** MCP servers willy-nilly is going to like bloat your context. Um, so we're coming

**[01:15:09]** bloat your context. Um, so we're coming

**[01:15:09]** bloat your context. Um, so we're coming up with ways to basically allow people

**[01:15:11]** up with ways to basically allow people

**[01:15:11]** up with ways to basically allow people to add MCB servers and then like hide

**[01:15:15]** to add MCB servers and then like hide

**[01:15:15]** to add MCB servers and then like hide that from the actual uh system.

**[01:15:22]** Also, when you have like agent to agent

**[01:15:22]** Also, when you have like agent to agent communications, right? So, let's say

**[01:15:23]** communications, right? So, let's say

**[01:15:23]** communications, right? So, let's say agent A calls agent B and agent B calls

**[01:15:26]** agent A calls agent B and agent B calls

**[01:15:26]** agent A calls agent B and agent B calls agent A.

**[01:15:27]** agent A.

**[01:15:27]** agent A. How can you make sure this uh recussion

**[01:15:29]** How can you make sure this uh recussion

**[01:15:29]** How can you make sure this uh recussion like when does it stop?

**[01:15:31]** like when does it stop?

**[01:15:32]** like when does it stop? Yeah, you you can have like a max turn,

**[01:15:34]** Yeah, you you can have like a max turn,

**[01:15:34]** Yeah, you you can have like a max turn, right, where you just kind of jump out

**[01:15:36]** right, where you just kind of jump out

**[01:15:36]** right, where you just kind of jump out of it. Um, like when I had the LLMs

**[01:15:39]** of it. Um, like when I had the LLMs

**[01:15:39]** of it. Um, like when I had the LLMs talking to each other, I just told them

**[01:15:40]** talking to each other, I just told them

**[01:15:40]** talking to each other, I just told them like take 50 turns. Um, you know, and it

**[01:15:44]** like take 50 turns. Um, you know, and it

**[01:15:44]** like take 50 turns. Um, you know, and it was funny as I was building that tool, I

**[01:15:47]** was funny as I was building that tool, I

**[01:15:47]** was funny as I was building that tool, I wanted to like talk to the claude for

**[01:15:49]** wanted to like talk to the claude for

**[01:15:49]** wanted to like talk to the claude for that thought it was conscious.

**[01:15:50]** that thought it was conscious.

**[01:15:50]** that thought it was conscious. So, I added a feature where I could just

**[01:15:52]** So, I added a feature where I could just

**[01:15:52]** So, I added a feature where I could just chat to it at that point in its

**[01:15:54]** chat to it at that point in its

**[01:15:54]** chat to it at that point in its conversation and but then the context

**[01:15:56]** conversation and but then the context

**[01:15:56]** conversation and but then the context kept like getting rate limited. So, then

**[01:15:58]** kept like getting rate limited. So, then

**[01:15:58]** kept like getting rate limited. So, then I was like, "Oh I'm going to have

**[01:15:59]** I was like, "Oh I'm going to have

**[01:15:59]** I was like, "Oh I'm going to have to implement, you know, prompt caching,


### [01:16:00 - 01:17:00]

**[01:16:02]** to implement, you know, prompt caching,

**[01:16:02]** to implement, you know, prompt caching, uh, pruning." So then I added like 23

**[01:16:04]** uh, pruning." So then I added like 23

**[01:16:04]** uh, pruning." So then I added like 23 tools to the agent just to continue the

**[01:16:06]** tools to the agent just to continue the

**[01:16:06]** tools to the agent just to continue the conversation. I gave it like memory and

**[01:16:08]** conversation. I gave it like memory and

**[01:16:08]** conversation. I gave it like memory and all these other things and like it kind

**[01:16:10]** all these other things and like it kind

**[01:16:10]** all these other things and like it kind of funny how you start out with just I

**[01:16:13]** of funny how you start out with just I

**[01:16:13]** of funny how you start out with just I just want to have a long conversation

**[01:16:14]** just want to have a long conversation

**[01:16:14]** just want to have a long conversation and then you end up with 23 tools.

**[01:16:17]** and then you end up with 23 tools.

**[01:16:17]** and then you end up with 23 tools. Yeah.

**[01:16:18]** Yeah.

**[01:16:18]** Yeah. Just following up one question like when

**[01:16:20]** Just following up one question like when

**[01:16:20]** Just following up one question like when testing because you are using lot of

**[01:16:23]** testing because you are using lot of

**[01:16:23]** testing because you are using lot of external tools like lab or salesforce

**[01:16:25]** external tools like lab or salesforce

**[01:16:25]** external tools like lab or salesforce etc as your MCP servers but then you are

**[01:16:28]** etc as your MCP servers but then you are

**[01:16:28]** etc as your MCP servers but then you are writing on the real world let's say.

**[01:16:30]** writing on the real world let's say.

**[01:16:30]** writing on the real world let's say. Say say again. So you are basically

**[01:16:31]** Say say again. So you are basically

**[01:16:32]** Say say again. So you are basically creating a message in Slack or like

**[01:16:35]** creating a message in Slack or like

**[01:16:35]** creating a message in Slack or like writing something on Salesforce,

**[01:16:36]** writing something on Salesforce,

**[01:16:36]** writing something on Salesforce, creating an entry or etc. So but how do

**[01:16:39]** creating an entry or etc. So but how do

**[01:16:39]** creating an entry or etc. So but how do you test those systems like do you mock

**[01:16:40]** you test those systems like do you mock

**[01:16:40]** you test those systems like do you mock everything every tool or do you do

**[01:16:43]** everything every tool or do you do

**[01:16:43]** everything every tool or do you do something else?

**[01:16:44]** something else?

**[01:16:44]** something else? We we use demo accounts in like

**[01:16:46]** We we use demo accounts in like

**[01:16:46]** We we use demo accounts in like Salesforce, we have a sample data,

**[01:16:48]** Salesforce, we have a sample data,

**[01:16:48]** Salesforce, we have a sample data, Slack, uh we have a few agents that

**[01:16:50]** Slack, uh we have a few agents that

**[01:16:50]** Slack, uh we have a few agents that actually will go in and and just post

**[01:16:53]** actually will go in and and just post

**[01:16:53]** actually will go in and and just post like conversations. Um, and then there's

**[01:16:55]** like conversations. Um, and then there's

**[01:16:55]** like conversations. Um, and then there's like a a bench support user that will

**[01:16:58]** like a a bench support user that will

**[01:16:58]** like a a bench support user that will respond to those fake customers and then


### [01:17:00 - 01:18:00]

**[01:17:00]** respond to those fake customers and then

**[01:17:00]** respond to those fake customers and then we can we can just test uh on synthetic

**[01:17:03]** we can we can just test uh on synthetic

**[01:17:03]** we can we can just test uh on synthetic data like that.

**[01:17:04]** data like that.

**[01:17:04]** data like that. So for every tool you will have a

**[01:17:05]** So for every tool you will have a

**[01:17:05]** So for every tool you will have a synthetic.

**[01:17:06]** synthetic.

**[01:17:06]** synthetic. Yeah. Yeah. You you can test in your

**[01:17:08]** Yeah. Yeah. You you can test in your

**[01:17:08]** Yeah. Yeah. You you can test in your production account but you can't really

**[01:17:10]** production account but you can't really

**[01:17:10]** production account but you can't really demo in your production account.

**[01:17:12]** demo in your production account.

**[01:17:12]** demo in your production account. Yeah.

**[01:17:13]** Yeah.

**[01:17:13]** Yeah. Yeah. So when you adopt agent to agent

**[01:17:16]** Yeah. So when you adopt agent to agent

**[01:17:16]** Yeah. So when you adopt agent to agent system, do you see an increase in the

**[01:17:19]** system, do you see an increase in the

**[01:17:19]** system, do you see an increase in the complexity of the task you can achieve

**[01:17:21]** complexity of the task you can achieve

**[01:17:21]** complexity of the task you can achieve but a decrease in the consistency of the

**[01:17:23]** but a decrease in the consistency of the

**[01:17:23]** but a decrease in the consistency of the performance?

**[01:17:24]** performance?

**[01:17:24]** performance? It it's kind of hard to quantify but I I

**[01:17:28]** It it's kind of hard to quantify but I I

**[01:17:28]** It it's kind of hard to quantify but I I don't know if A2A is is ready yet. Uh at

**[01:17:33]** don't know if A2A is is ready yet. Uh at

**[01:17:33]** don't know if A2A is is ready yet. Uh at least at least not for my use case. You

**[01:17:35]** least at least not for my use case. You

**[01:17:35]** least at least not for my use case. You know may maybe Salesforce can provide

**[01:17:38]** know may maybe Salesforce can provide

**[01:17:38]** know may maybe Salesforce can provide much better tools than like an SQL query

**[01:17:42]** much better tools than like an SQL query

**[01:17:42]** much better tools than like an SQL query MCP tool.

**[01:17:44]** MCP tool.

**[01:17:44]** MCP tool. Yeah. And and they they can just do a

**[01:17:46]** Yeah. And and they they can just do a

**[01:17:46]** Yeah. And and they they can just do a lot more than you can ever do in your

**[01:17:49]** lot more than you can ever do in your

**[01:17:49]** lot more than you can ever do in your code, right? Because you're you're only

**[01:17:50]** code, right? Because you're you're only

**[01:17:50]** code, right? Because you're you're only ever able to access, you know, certain

**[01:17:53]** ever able to access, you know, certain

**[01:17:53]** ever able to access, you know, certain things and and do certain uh calls and

**[01:17:56]** things and and do certain uh calls and

**[01:17:56]** things and and do certain uh calls and like if if if a third party can build a

**[01:17:59]** like if if if a third party can build a

**[01:17:59]** like if if if a third party can build a better uh system um that's opaque um


### [01:18:00 - 01:19:00]

**[01:18:03]** better uh system um that's opaque um

**[01:18:03]** better uh system um that's opaque um then that might you know improve

**[01:18:05]** then that might you know improve

**[01:18:05]** then that might you know improve performance. Um I I think like

**[01:18:08]** performance. Um I I think like

**[01:18:08]** performance. Um I I think like fundamentally it always comes down to

**[01:18:10]** fundamentally it always comes down to

**[01:18:10]** fundamentally it always comes down to like indexing data. Um, so like you know

**[01:18:13]** like indexing data. Um, so like you know

**[01:18:13]** like indexing data. Um, so like you know the more data you need to process to get

**[01:18:15]** the more data you need to process to get

**[01:18:15]** the more data you need to process to get the business value out of it and the

**[01:18:17]** the business value out of it and the

**[01:18:17]** the business value out of it and the harder it's going to be to actually do

**[01:18:19]** harder it's going to be to actually do

**[01:18:19]** harder it's going to be to actually do that through MCP or A2A.

**[01:18:22]** that through MCP or A2A.

**[01:18:22]** that through MCP or A2A. Yeah.

**[01:18:25]** Yeah.

**[01:18:25]** Yeah. Yeah.

**[01:18:26]** Yeah.

**[01:18:26]** Yeah. So some of these interactions right this

**[01:18:28]** So some of these interactions right this

**[01:18:28]** So some of these interactions right this can be done through REST API right

**[01:18:30]** can be done through REST API right

**[01:18:30]** can be done through REST API right instead of

**[01:18:36]** what is the difference?

**[01:18:36]** what is the difference? Yeah and it kind of goes back to uh one

**[01:18:38]** Yeah and it kind of goes back to uh one

**[01:18:38]** Yeah and it kind of goes back to uh one of the earlier slides. um yeah when not

**[01:18:43]** of the earlier slides. um yeah when not

**[01:18:43]** of the earlier slides. um yeah when not to use A3A or MCP and it's it's if you

**[01:18:46]** to use A3A or MCP and it's it's if you

**[01:18:46]** to use A3A or MCP and it's it's if you have full control of of the things that

**[01:18:50]** have full control of of the things that

**[01:18:50]** have full control of of the things that you're doing right so like you know if

**[01:18:52]** you're doing right so like you know if

**[01:18:52]** you're doing right so like you know if if you are a Salesforce

**[01:18:55]** if you are a Salesforce

**[01:18:55]** if you are a Salesforce um you know and you're building your own

**[01:18:56]** um you know and you're building your own

**[01:18:56]** um you know and you're building your own internal Salesforce agent like do you


### [01:19:00 - 01:20:00]

**[01:19:00]** internal Salesforce agent like do you

**[01:19:00]** internal Salesforce agent like do you need to use an MCP server or A2A no

**[01:19:03]** need to use an MCP server or A2A no

**[01:19:03]** need to use an MCP server or A2A no right you're you're you're actually able

**[01:19:05]** right you're you're you're actually able

**[01:19:05]** right you're you're you're actually able to run your own local functions that

**[01:19:07]** to run your own local functions that

**[01:19:07]** to run your own local functions that maybe access the database directly right

**[01:19:09]** maybe access the database directly right

**[01:19:09]** maybe access the database directly right um So like if if you're building

**[01:19:11]** um So like if if you're building

**[01:19:11]** um So like if if you're building something you know where you need file

**[01:19:13]** something you know where you need file

**[01:19:13]** something you know where you need file system access um you know do you need to

**[01:19:16]** system access um you know do you need to

**[01:19:16]** system access um you know do you need to use an MCP uh you know server running

**[01:19:20]** use an MCP uh you know server running

**[01:19:20]** use an MCP uh you know server running locally or do you just write some code

**[01:19:22]** locally or do you just write some code

**[01:19:22]** locally or do you just write some code that accesses the file system right

**[01:19:26]** that accesses the file system right

**[01:19:26]** that accesses the file system right I think the main difference is like in

**[01:19:29]** I think the main difference is like in

**[01:19:29]** I think the main difference is like in terms of how do you maintain your state

**[01:19:31]** terms of how do you maintain your state

**[01:19:31]** terms of how do you maintain your state right like MCP start up in a stateful

**[01:19:35]** right like MCP start up in a stateful

**[01:19:35]** right like MCP start up in a stateful resting

**[01:19:37]** resting

**[01:19:37]** resting your context magic it is really crucial

**[01:19:41]** your context magic it is really crucial

**[01:19:41]** your context magic it is really crucial to have MC

**[01:19:43]** to have MC

**[01:19:43]** to have MC whereas rest API you can't do that.

**[01:19:46]** whereas rest API you can't do that.

**[01:19:46]** whereas rest API you can't do that. Yeah. So like a lot of the time when you

**[01:19:49]** Yeah. So like a lot of the time when you

**[01:19:49]** Yeah. So like a lot of the time when you use a REST API you're going to be like

**[01:19:51]** use a REST API you're going to be like

**[01:19:51]** use a REST API you're going to be like querying like making a lot of calls to

**[01:19:53]** querying like making a lot of calls to

**[01:19:54]** querying like making a lot of calls to to build up the thing that you want to

**[01:19:56]** to build up the thing that you want to

**[01:19:56]** to build up the thing that you want to ask the question on. Right? So if it's

**[01:19:58]** ask the question on. Right? So if it's

**[01:19:58]** ask the question on. Right? So if it's like hey look at every Slack message in


### [01:20:00 - 01:21:00]

**[01:20:00]** like hey look at every Slack message in

**[01:20:00]** like hey look at every Slack message in in this channel like it's not just going

**[01:20:02]** in this channel like it's not just going

**[01:20:02]** in this channel like it's not just going to be like one API call right just

**[01:20:05]** to be like one API call right just

**[01:20:05]** to be like one API call right just pageionation. You're going to have to

**[01:20:06]** pageionation. You're going to have to

**[01:20:06]** pageionation. You're going to have to pull it all into memory. then you're

**[01:20:08]** pull it all into memory. then you're

**[01:20:08]** pull it all into memory. then you're going to have to run it through an LLM,

**[01:20:09]** going to have to run it through an LLM,

**[01:20:09]** going to have to run it through an LLM, right? So there's there's still state uh

**[01:20:12]** right? So there's there's still state uh

**[01:20:12]** right? So there's there's still state uh in your application that's leveraging

**[01:20:14]** in your application that's leveraging

**[01:20:14]** in your application that's leveraging those REST APIs.

**[01:20:16]** those REST APIs.

**[01:20:16]** those REST APIs. Yeah,

**[01:20:17]** Yeah,

**[01:20:17]** Yeah, I'm curious about the task concept. Uh

**[01:20:19]** I'm curious about the task concept. Uh

**[01:20:19]** I'm curious about the task concept. Uh is that actually is that kind of LLM

**[01:20:21]** is that actually is that kind of LLM

**[01:20:22]** is that actually is that kind of LLM defined or do you have code for that? Is

**[01:20:24]** defined or do you have code for that? Is

**[01:20:24]** defined or do you have code for that? Is it more of a system thing?

**[01:20:26]** it more of a system thing?

**[01:20:26]** it more of a system thing? Which task context?

**[01:20:27]** Which task context?

**[01:20:27]** Which task context? Um so at least in the flow diagram you

**[01:20:29]** Um so at least in the flow diagram you

**[01:20:30]** Um so at least in the flow diagram you have

**[01:20:30]** have

**[01:20:30]** have Oh, is this in the repo? Does it

**[01:20:36]** so from CLI interface it says it sends a

**[01:20:36]** so from CLI interface it says it sends a task to host a curious is that a proper

**[01:20:39]** task to host a curious is that a proper

**[01:20:39]** task to host a curious is that a proper task or is it just you know just what

**[01:20:40]** task or is it just you know just what

**[01:20:40]** task or is it just you know just what you call what what sends to it.

**[01:20:42]** you call what what sends to it.

**[01:20:42]** you call what what sends to it. Yeah. Yeah. It's just saying hey you

**[01:20:44]** Yeah. Yeah. It's just saying hey you

**[01:20:44]** Yeah. Yeah. It's just saying hey you know process this web hook as a task

**[01:20:46]** know process this web hook as a task

**[01:20:46]** know process this web hook as a task right

**[01:20:46]** right

**[01:20:46]** right have you explored anything where you're

**[01:20:48]** have you explored anything where you're

**[01:20:48]** have you explored anything where you're actually tracking a proper task and

**[01:20:50]** actually tracking a proper task and

**[01:20:50]** actually tracking a proper task and you're assigning tasks to agents and you

**[01:20:52]** you're assigning tasks to agents and you

**[01:20:52]** you're assigning tasks to agents and you have basically like you know like a

**[01:20:53]** have basically like you know like a

**[01:20:53]** have basically like you know like a planner where you basically have task a

**[01:20:56]** planner where you basically have task a

**[01:20:56]** planner where you basically have task a one two three is on this agent and so on

**[01:20:59]** one two three is on this agent and so on

**[01:20:59]** one two three is on this agent and so on and then in relation to the the question


### [01:21:00 - 01:22:00]

**[01:21:01]** and then in relation to the the question

**[01:21:01]** and then in relation to the the question about human in the loop you could have

**[01:21:03]** about human in the loop you could have

**[01:21:03]** about human in the loop you could have task assigned to humans as well right

**[01:21:05]** task assigned to humans as well right

**[01:21:05]** task assigned to humans as well right both

**[01:21:06]** both

**[01:21:06]** both humans and agents

**[01:21:07]** humans and agents

**[01:21:07]** humans and agents yeah so uh we're looking at uh directed

**[01:21:10]** yeah so uh we're looking at uh directed

**[01:21:10]** yeah so uh we're looking at uh directed a cyclic grass right so dags um as a

**[01:21:13]** a cyclic grass right so dags um as a

**[01:21:13]** a cyclic grass right so dags um as a part of of bench sub agent tasks, right?

**[01:21:16]** part of of bench sub agent tasks, right?

**[01:21:16]** part of of bench sub agent tasks, right? So, you know, you you need to have some

**[01:21:18]** So, you know, you you need to have some

**[01:21:18]** So, you know, you you need to have some sort of flow control, right? You know, I

**[01:21:21]** sort of flow control, right? You know, I

**[01:21:21]** sort of flow control, right? You know, I need five things done and then when

**[01:21:23]** need five things done and then when

**[01:21:23]** need five things done and then when that's done, I need to do one thing with

**[01:21:24]** that's done, I need to do one thing with

**[01:21:24]** that's done, I need to do one thing with it, but then I need to send that thing

**[01:21:26]** it, but then I need to send that thing

**[01:21:26]** it, but then I need to send that thing to five other things, right? So, you

**[01:21:27]** to five other things, right? So, you

**[01:21:27]** to five other things, right? So, you kind of have fan out, fan in uh style

**[01:21:30]** kind of have fan out, fan in uh style

**[01:21:30]** kind of have fan out, fan in uh style stuff. Um it's very similar to like

**[01:21:32]** stuff. Um it's very similar to like

**[01:21:32]** stuff. Um it's very similar to like CI/CD pipelines where, you know, you

**[01:21:34]** CI/CD pipelines where, you know, you

**[01:21:34]** CI/CD pipelines where, you know, you might want to lint in parallel and test

**[01:21:36]** might want to lint in parallel and test

**[01:21:36]** might want to lint in parallel and test in parallel, but you know, you're you're

**[01:21:38]** in parallel, but you know, you're you're

**[01:21:38]** in parallel, but you know, you're you're building in serial, right? Uh yeah.

**[01:21:42]** building in serial, right? Uh yeah.

**[01:21:42]** building in serial, right? Uh yeah. So I was looking at code base and you

**[01:21:44]** So I was looking at code base and you

**[01:21:44]** So I was looking at code base and you have this defined like a GitHub MCP

**[01:21:47]** have this defined like a GitHub MCP

**[01:21:47]** have this defined like a GitHub MCP server and uh in a separate file under

**[01:21:50]** server and uh in a separate file under

**[01:21:50]** server and uh in a separate file under the GitHub agent you have also the

**[01:21:52]** the GitHub agent you have also the

**[01:21:52]** the GitHub agent you have also the genkit.ts

**[01:21:53]** genkit.ts

**[01:21:53]** genkit.ts where you are wrapping the MCP in

**[01:21:55]** where you are wrapping the MCP in

**[01:21:55]** where you are wrapping the MCP in another function call why is that like

**[01:21:58]** another function call why is that like

**[01:21:58]** another function call why is that like can't the MCP just interpolate with our


### [01:22:00 - 01:23:00]

**[01:22:01]** can't the MCP just interpolate with our

**[01:22:01]** can't the MCP just interpolate with our A2A like why do we have to make rappers

**[01:22:04]** A2A like why do we have to make rappers

**[01:22:04]** A2A like why do we have to make rappers on top of

**[01:22:04]** on top of

**[01:22:04]** on top of that's a great question and and I think

**[01:22:07]** that's a great question and and I think

**[01:22:07]** that's a great question and and I think that's the fundamental question of A2A

**[01:22:09]** that's the fundamental question of A2A

**[01:22:09]** that's the fundamental question of A2A is like they they launched and they said

**[01:22:11]** is like they they launched and they said

**[01:22:11]** is like they they launched and they said oh yeah full MCP support you'll be hard

**[01:22:14]** oh yeah full MCP support you'll be hard

**[01:22:14]** oh yeah full MCP support you'll be hard pushed to find a single example online

**[01:22:17]** pushed to find a single example online

**[01:22:17]** pushed to find a single example online maybe maybe this is the only repo that

**[01:22:19]** maybe maybe this is the only repo that

**[01:22:19]** maybe maybe this is the only repo that actually has an example of A2A and MCP

**[01:22:21]** actually has an example of A2A and MCP

**[01:22:21]** actually has an example of A2A and MCP working together. Um, and it took a lot

**[01:22:24]** working together. Um, and it took a lot

**[01:22:24]** working together. Um, and it took a lot of work and actually I ended up uh

**[01:22:26]** of work and actually I ended up uh

**[01:22:26]** of work and actually I ended up uh having to use something called

**[01:22:29]** having to use something called

**[01:22:30]** having to use something called uh where is it? Genkit XMCP.

**[01:22:33]** uh where is it? Genkit XMCP.

**[01:22:33]** uh where is it? Genkit XMCP. That was the only way I could get it to

**[01:22:35]** That was the only way I could get it to

**[01:22:35]** That was the only way I could get it to work.

**[01:22:36]** work.

**[01:22:36]** work. Um, so yeah, they they don't really have

**[01:22:39]** Um, so yeah, they they don't really have

**[01:22:39]** Um, so yeah, they they don't really have like proper support yet. Uh, it was I I

**[01:22:43]** like proper support yet. Uh, it was I I

**[01:22:43]** like proper support yet. Uh, it was I I think if they had this this would have

**[01:22:45]** think if they had this this would have

**[01:22:45]** think if they had this this would have been a lot easier to build. Um, but

**[01:22:47]** been a lot easier to build. Um, but

**[01:22:47]** been a lot easier to build. Um, but yeah, hopefully in time.

**[01:22:51]** yeah, hopefully in time.

**[01:22:51]** yeah, hopefully in time. All righty, I think we're we're at time.

**[01:22:53]** All righty, I think we're we're at time.

**[01:22:53]** All righty, I think we're we're at time. Uh, thanks everybody for joining. Uh,

**[01:22:55]** Uh, thanks everybody for joining. Uh,

**[01:22:55]** Uh, thanks everybody for joining. Uh, hope you enjoyed it. Great conversation

**[01:22:57]** hope you enjoyed it. Great conversation

**[01:22:57]** hope you enjoyed it. Great conversation at the end. And yeah, definitely uh try

**[01:22:59]** at the end. And yeah, definitely uh try

**[01:22:59]** at the end. And yeah, definitely uh try out Bench, hit me up on uh LinkedIn. I


### [01:23:00 - 01:24:00]

**[01:23:02]** out Bench, hit me up on uh LinkedIn. I

**[01:23:02]** out Bench, hit me up on uh LinkedIn. I would love feedback uh before we go

**[01:23:04]** would love feedback uh before we go

**[01:23:04]** would love feedback uh before we go live.

**[01:23:06]** live.

**[01:23:06]** live. Thanks.


