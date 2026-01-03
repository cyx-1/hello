# Building Agents at Cloud Scale — Antje Barth, AWS

**Video URL:** https://www.youtube.com/watch?v=WJjInLeaJjo

---

## Full Transcript

### [00:00 - 01:00]

**[00:26]** Hi everyone. I'm thrilled to be back on

**[00:26]** Hi everyone. I'm thrilled to be back on stage here again at the engineer worlds

**[00:29]** stage here again at the engineer worlds

**[00:29]** stage here again at the engineer worlds fair and it's amazing to see this

**[00:31]** fair and it's amazing to see this

**[00:31]** fair and it's amazing to see this community grow. So today I'm going to

**[00:34]** community grow. So today I'm going to

**[00:34]** community grow. So today I'm going to speak about how we can build agents at

**[00:37]** speak about how we can build agents at

**[00:37]** speak about how we can build agents at clouds scale.

**[00:39]** clouds scale.

**[00:39]** clouds scale. Now at Amazon and AWS we truly believe

**[00:44]** Now at Amazon and AWS we truly believe

**[00:44]** Now at Amazon and AWS we truly believe that virtually every customer experience

**[00:47]** that virtually every customer experience

**[00:47]** that virtually every customer experience we know of will be reinvented with AI.

**[00:51]** we know of will be reinvented with AI.

**[00:51]** we know of will be reinvented with AI. And not just the existing experiences,

**[00:53]** And not just the existing experiences,

**[00:53]** And not just the existing experiences, but there will also be brand new

**[00:55]** but there will also be brand new

**[00:55]** but there will also be brand new experiences we are now able to build

**[00:57]** experiences we are now able to build

**[00:57]** experiences we are now able to build with the help of AI agents.


### [01:00 - 02:00]

**[01:01]** with the help of AI agents.

**[01:01]** with the help of AI agents. And we're not just theorizing about

**[01:03]** And we're not just theorizing about

**[01:03]** And we're not just theorizing about this, right? We're all here together to

**[01:06]** this, right? We're all here together to

**[01:06]** this, right? We're all here together to actually build the future.

**[01:10]** actually build the future.

**[01:10]** actually build the future. Now, I want to start just with a little

**[01:13]** Now, I want to start just with a little

**[01:13]** Now, I want to start just with a little bit of what that means internally across

**[01:16]** bit of what that means internally across

**[01:16]** bit of what that means internally across Amazon as a business.

**[01:19]** Amazon as a business.

**[01:19]** Amazon as a business. At Amazon, we have over 1,000

**[01:22]** At Amazon, we have over 1,000

**[01:22]** At Amazon, we have over 1,000 generative AI applications that are

**[01:24]** generative AI applications that are

**[01:24]** generative AI applications that are either built or in development,

**[01:28]** either built or in development,

**[01:28]** either built or in development, transforming everything from how we

**[01:30]** transforming everything from how we

**[01:30]** transforming everything from how we forecast inventory to how we optimize

**[01:34]** forecast inventory to how we optimize

**[01:34]** forecast inventory to how we optimize delivery routes to how customers shop

**[01:37]** delivery routes to how customers shop

**[01:37]** delivery routes to how customers shop and how they interact with their homes.

**[01:40]** and how they interact with their homes.

**[01:40]** and how they interact with their homes. And one of the most ambitious

**[01:43]** And one of the most ambitious

**[01:43]** And one of the most ambitious deployments of AI agents is the complete

**[01:46]** deployments of AI agents is the complete

**[01:46]** deployments of AI agents is the complete reimagining of Alexa.

**[01:49]** reimagining of Alexa.

**[01:49]** reimagining of Alexa. And I know many of us have been waiting

**[01:51]** And I know many of us have been waiting

**[01:51]** And I know many of us have been waiting for this for a long time. So what you're

**[01:54]** for this for a long time. So what you're

**[01:54]** for this for a long time. So what you're about to see here represents the largest

**[01:58]** about to see here represents the largest

**[01:58]** about to see here represents the largest integration of services, agentic


### [02:00 - 03:00]

**[02:01]** integration of services, agentic

**[02:01]** integration of services, agentic capabilities, and LLM that we know of

**[02:05]** capabilities, and LLM that we know of

**[02:05]** capabilities, and LLM that we know of anywhere. So let's have a brief look.

**[02:13]** Wow. Wow. Look at my style. I know you

**[02:13]** Wow. Wow. Look at my style. I know you ain't seen it like this in a while. Oh,

**[02:16]** ain't seen it like this in a while. Oh,

**[02:16]** ain't seen it like this in a while. Oh, hey there. So, we can just like talk

**[02:19]** hey there. So, we can just like talk

**[02:19]** hey there. So, we can just like talk now. I'm all ears. Figuratively

**[02:20]** now. I'm all ears. Figuratively

**[02:20]** now. I'm all ears. Figuratively speaking.

**[02:22]** speaking.

**[02:22]** speaking. Do you know how to manage my kids

**[02:23]** Do you know how to manage my kids

**[02:24]** Do you know how to manage my kids schedules? I noticed a birthday party

**[02:26]** schedules? I noticed a birthday party

**[02:26]** schedules? I noticed a birthday party conflicts with picking up grandma at the

**[02:27]** conflicts with picking up grandma at the

**[02:27]** conflicts with picking up grandma at the airport. Want me to book her a ride?

**[02:30]** airport. Want me to book her a ride?

**[02:30]** airport. Want me to book her a ride? Billy Eyish is in town soon. No way. I

**[02:32]** Billy Eyish is in town soon. No way. I

**[02:32]** Billy Eyish is in town soon. No way. I can share when tickets are available in

**[02:34]** can share when tickets are available in

**[02:34]** can share when tickets are available in your city. Yes, please.

**[02:36]** your city. Yes, please.

**[02:36]** your city. Yes, please. Got any spring break ideas? Somewhere

**[02:38]** Got any spring break ideas? Somewhere

**[02:38]** Got any spring break ideas? Somewhere not too far, only if there's a beach and

**[02:40]** not too far, only if there's a beach and

**[02:40]** not too far, only if there's a beach and nice weather. Santa Barbara is great for

**[02:42]** nice weather. Santa Barbara is great for

**[02:42]** nice weather. Santa Barbara is great for everyone. I found a restaurant downtown

**[02:44]** everyone. I found a restaurant downtown

**[02:44]** everyone. I found a restaurant downtown I think you'd like. What is Santa

**[02:46]** I think you'd like. What is Santa

**[02:46]** I think you'd like. What is Santa Barbara known for? It has great upscale

**[02:48]** Barbara known for? It has great upscale

**[02:48]** Barbara known for? It has great upscale shops and oceanfront dining. Can you go

**[02:50]** shops and oceanfront dining. Can you go

**[02:50]** shops and oceanfront dining. Can you go whale watching? Absolutely. Want me to

**[02:52]** whale watching? Absolutely. Want me to

**[02:52]** whale watching? Absolutely. Want me to book a catamaran tour? Wow. What's the

**[02:55]** book a catamaran tour? Wow. What's the

**[02:55]** book a catamaran tour? Wow. What's the next step? Remove the nut holding the

**[02:57]** next step? Remove the nut holding the

**[02:57]** next step? Remove the nut holding the cartridge. Should I get bangs? You might

**[02:59]** cartridge. Should I get bangs? You might

**[02:59]** cartridge. Should I get bangs? You might only love them for a little while.


### [03:00 - 04:00]

**[03:01]** only love them for a little while.

**[03:01]** only love them for a little while. You're probably right. Make a slideshow

**[03:02]** You're probably right. Make a slideshow

**[03:02]** You're probably right. Make a slideshow of baby teap. Mom, what part am I

**[03:05]** of baby teap. Mom, what part am I

**[03:05]** of baby teap. Mom, what part am I looking for again? 2in washers. Your

**[03:08]** looking for again? 2in washers. Your

**[03:08]** looking for again? 2in washers. Your Uber is 2 minutes away. For real?

**[03:11]** Uber is 2 minutes away. For real?

**[03:11]** Uber is 2 minutes away. For real? Wait, did someone let the dog out today?

**[03:13]** Wait, did someone let the dog out today?

**[03:13]** Wait, did someone let the dog out today? I checked the cameras and yes, in fact,

**[03:15]** I checked the cameras and yes, in fact,

**[03:15]** I checked the cameras and yes, in fact, Mozart was just out.

**[03:28]** I love sharing this video because it

**[03:28]** I love sharing this video because it shows really the power of agents at

**[03:32]** shows really the power of agents at

**[03:32]** shows really the power of agents at scale and just to have a quick look what

**[03:35]** scale and just to have a quick look what

**[03:35]** scale and just to have a quick look what that means in terms of numbers.

**[03:38]** that means in terms of numbers.

**[03:38]** that means in terms of numbers. We have over 600 million Alexa devices

**[03:42]** We have over 600 million Alexa devices

**[03:42]** We have over 600 million Alexa devices now out in the world and with the help

**[03:45]** now out in the world and with the help

**[03:45]** now out in the world and with the help of the latest advancements in AI, we

**[03:48]** of the latest advancements in AI, we

**[03:48]** of the latest advancements in AI, we were able to really reimagine this

**[03:50]** were able to really reimagine this

**[03:50]** were able to really reimagine this experience.

**[03:52]** experience.

**[03:52]** experience. Alexa Plus works through hundreds of

**[03:55]** Alexa Plus works through hundreds of

**[03:55]** Alexa Plus works through hundreds of specialized expert systems. That's what

**[03:58]** specialized expert systems. That's what

**[03:58]** specialized expert systems. That's what the Alexa team calls groups of


### [04:00 - 05:00]

**[04:00]** the Alexa team calls groups of

**[04:00]** the Alexa team calls groups of capabilities, APIs, and instructions to

**[04:04]** capabilities, APIs, and instructions to

**[04:04]** capabilities, APIs, and instructions to accomplish a specific task for you. And

**[04:07]** accomplish a specific task for you. And

**[04:07]** accomplish a specific task for you. And all of these experts also orchestrate

**[04:10]** all of these experts also orchestrate

**[04:10]** all of these experts also orchestrate across tens of thousands of partner

**[04:13]** across tens of thousands of partner

**[04:13]** across tens of thousands of partner services and devices to get the things

**[04:16]** services and devices to get the things

**[04:16]** services and devices to get the things done, which you just seen a glimpse of

**[04:19]** done, which you just seen a glimpse of

**[04:19]** done, which you just seen a glimpse of this here in this video. And we truly

**[04:21]** this here in this video. And we truly

**[04:22]** this here in this video. And we truly believe that the future will be full of

**[04:24]** believe that the future will be full of

**[04:24]** believe that the future will be full of those specialized agents, each with

**[04:27]** those specialized agents, each with

**[04:27]** those specialized agents, each with their own unique capabilities and

**[04:30]** their own unique capabilities and

**[04:30]** their own unique capabilities and working together seamlessly with other

**[04:32]** working together seamlessly with other

**[04:32]** working together seamlessly with other AI agents.

**[04:38]** Now, this example shows what's possible

**[04:38]** Now, this example shows what's possible at this massive scale. But how do we get

**[04:42]** at this massive scale. But how do we get

**[04:42]** at this massive scale. But how do we get there? How do we operate at this scale?

**[04:45]** there? How do we operate at this scale?

**[04:46]** there? How do we operate at this scale? or said differently, how do we move from

**[04:48]** or said differently, how do we move from

**[04:48]** or said differently, how do we move from web services that we've built for many

**[04:51]** web services that we've built for many

**[04:51]** web services that we've built for many years now into developing those agentic

**[04:54]** years now into developing those agentic

**[04:54]** years now into developing those agentic services? And luckily, many of the

**[04:57]** services? And luckily, many of the

**[04:57]** services? And luckily, many of the underlying principles remain the same.


### [05:00 - 06:00]

**[05:00]** underlying principles remain the same.

**[05:00]** underlying principles remain the same. Whether you're building for millions of

**[05:01]** Whether you're building for millions of

**[05:02]** Whether you're building for millions of devices, whether you're reimagining and

**[05:05]** devices, whether you're reimagining and

**[05:05]** devices, whether you're reimagining and integrating AI experiences into your

**[05:07]** integrating AI experiences into your

**[05:07]** integrating AI experiences into your enterprise applications, or you're a

**[05:10]** enterprise applications, or you're a

**[05:10]** enterprise applications, or you're a startup and you're really just looking

**[05:11]** startup and you're really just looking

**[05:11]** startup and you're really just looking to kind of scale your idea to the next

**[05:13]** to kind of scale your idea to the next

**[05:13]** to kind of scale your idea to the next level.

**[05:15]** level.

**[05:15]** level. Now, another example I want to show you

**[05:18]** Now, another example I want to show you

**[05:18]** Now, another example I want to show you is an agentic service that we built at

**[05:21]** is an agentic service that we built at

**[05:21]** is an agentic service that we built at AWS.

**[05:23]** AWS.

**[05:23]** AWS. You might have heard about Amazon Q

**[05:25]** You might have heard about Amazon Q

**[05:25]** You might have heard about Amazon Q developer which is our code assistant

**[05:28]** developer which is our code assistant

**[05:28]** developer which is our code assistant that helps you really kind of across the

**[05:30]** that helps you really kind of across the

**[05:30]** that helps you really kind of across the software development life cycle and just

**[05:33]** software development life cycle and just

**[05:33]** software development life cycle and just a few months ago we released an Q

**[05:36]** a few months ago we released an Q

**[05:36]** a few months ago we released an Q developer agent for your CLI. So it

**[05:39]** developer agent for your CLI. So it

**[05:39]** developer agent for your CLI. So it brings the agendic chat experience into

**[05:41]** brings the agendic chat experience into

**[05:41]** brings the agendic chat experience into the terminal. It helps you to debug

**[05:43]** the terminal. It helps you to debug

**[05:43]** the terminal. It helps you to debug issues. You can ask it natural

**[05:45]** issues. You can ask it natural

**[05:45]** issues. You can ask it natural questions. It can read and write files

**[05:47]** questions. It can read and write files

**[05:48]** questions. It can read and write files and really kind of help to make your

**[05:49]** and really kind of help to make your

**[05:50]** and really kind of help to make your day-to-day in the terminal more

**[05:51]** day-to-day in the terminal more

**[05:51]** day-to-day in the terminal more productive.

**[05:52]** productive.

**[05:52]** productive. So let's have a quick look how this

**[05:54]** So let's have a quick look how this

**[05:54]** So let's have a quick look how this looks.

**[05:56]** looks.

**[05:56]** looks. Here is Amazon Q in the CLI and I'll

**[05:59]** Here is Amazon Q in the CLI and I'll

**[05:59]** Here is Amazon Q in the CLI and I'll just ask a good question here. In this


### [06:00 - 07:00]

**[06:01]** just ask a good question here. In this

**[06:01]** just ask a good question here. In this case, hey, what do you know about Amazon

**[06:03]** case, hey, what do you know about Amazon

**[06:03]** case, hey, what do you know about Amazon Bedrock? CLI is integrated with MCP. So

**[06:06]** Bedrock? CLI is integrated with MCP. So

**[06:06]** Bedrock? CLI is integrated with MCP. So what it does, it actually figures out

**[06:09]** what it does, it actually figures out

**[06:09]** what it does, it actually figures out there is a tool. Our AWS documentation

**[06:12]** there is a tool. Our AWS documentation

**[06:12]** there is a tool. Our AWS documentation team has released an MCP server. It's

**[06:14]** team has released an MCP server. It's

**[06:14]** team has released an MCP server. It's connecting to it. You see the tool is

**[06:16]** connecting to it. You see the tool is

**[06:16]** connecting to it. You see the tool is happening and it's asking for

**[06:18]** happening and it's asking for

**[06:18]** happening and it's asking for permissions. So I give it the

**[06:19]** permissions. So I give it the

**[06:19]** permissions. So I give it the permissions and then it comes back with

**[06:21]** permissions and then it comes back with

**[06:21]** permissions and then it comes back with a response that is grounded in the

**[06:24]** a response that is grounded in the

**[06:24]** a response that is grounded in the official AWS documentation.

**[06:27]** official AWS documentation.

**[06:27]** official AWS documentation. Now I don't want to talk much more about

**[06:29]** Now I don't want to talk much more about

**[06:29]** Now I don't want to talk much more about Q but I do want to ask for you just to

**[06:33]** Q but I do want to ask for you just to

**[06:34]** Q but I do want to ask for you just to quickly think about how long did it take

**[06:37]** quickly think about how long did it take

**[06:37]** quickly think about how long did it take for the AWS internal teams to build and

**[06:40]** for the AWS internal teams to build and

**[06:40]** for the AWS internal teams to build and ship this agentic service and let's just

**[06:43]** ship this agentic service and let's just

**[06:43]** ship this agentic service and let's just do it with a quick raise of hands who

**[06:45]** do it with a quick raise of hands who

**[06:45]** do it with a quick raise of hands who think it took two months to develop and

**[06:46]** think it took two months to develop and

**[06:46]** think it took two months to develop and ship this

**[06:49]** ship this

**[06:49]** ship this It's a few hands. Who thinks three

**[06:51]** It's a few hands. Who thinks three

**[06:51]** It's a few hands. Who thinks three weeks?

**[06:52]** weeks?

**[06:52]** weeks? All right, it's a bunch of more hands.

**[06:54]** All right, it's a bunch of more hands.

**[06:54]** All right, it's a bunch of more hands. Who do you think it took half a year?

**[06:58]** Who do you think it took half a year?

**[06:58]** Who do you think it took half a year? Almost none. Wow, you folks are great.


### [07:00 - 08:00]

**[07:01]** Almost none. Wow, you folks are great.

**[07:01]** Almost none. Wow, you folks are great. We built and shipped this within 3

**[07:03]** We built and shipped this within 3

**[07:03]** We built and shipped this within 3 weeks. And to me, this is just almost

**[07:07]** weeks. And to me, this is just almost

**[07:07]** weeks. And to me, this is just almost insane, right? Like the speed and we

**[07:10]** insane, right? Like the speed and we

**[07:10]** insane, right? Like the speed and we heard it earlier like the mode of of AI,

**[07:13]** heard it earlier like the mode of of AI,

**[07:13]** heard it earlier like the mode of of AI, one of the keynote speakers called it

**[07:14]** one of the keynote speakers called it

**[07:14]** one of the keynote speakers called it out is execution, right? And I think

**[07:17]** out is execution, right? And I think

**[07:17]** out is execution, right? And I think three weeks is super impressive.

**[07:19]** three weeks is super impressive.

**[07:19]** three weeks is super impressive. Now,

**[07:21]** Now,

**[07:21]** Now, how do we enable teams and not just

**[07:24]** how do we enable teams and not just

**[07:24]** how do we enable teams and not just internally at AWS, but in general to

**[07:27]** internally at AWS, but in general to

**[07:27]** internally at AWS, but in general to build and ship production ready AI

**[07:29]** build and ship production ready AI

**[07:29]** build and ship production ready AI agents this quickly? What we did

**[07:32]** agents this quickly? What we did

**[07:32]** agents this quickly? What we did internally, our teams, we needed to

**[07:34]** internally, our teams, we needed to

**[07:34]** internally, our teams, we needed to fundamentally rethink how to build

**[07:37]** fundamentally rethink how to build

**[07:37]** fundamentally rethink how to build agents. And what we did is we developed

**[07:39]** agents. And what we did is we developed

**[07:40]** agents. And what we did is we developed a model-driven approach that really kind

**[07:41]** a model-driven approach that really kind

**[07:42]** a model-driven approach that really kind of taps into the power of LLMs these

**[07:45]** of taps into the power of LLMs these

**[07:45]** of taps into the power of LLMs these days and models that are so much more

**[07:47]** days and models that are so much more

**[07:47]** days and models that are so much more capable in deciding, planning,

**[07:49]** capable in deciding, planning,

**[07:49]** capable in deciding, planning, reasoning, taking actions and let the

**[07:53]** reasoning, taking actions and let the

**[07:53]** reasoning, taking actions and let the developers focus on what their agent

**[07:55]** developers focus on what their agent

**[07:56]** developers focus on what their agent should do rather than telling it exactly

**[07:58]** should do rather than telling it exactly

**[07:58]** should do rather than telling it exactly how to do it. And the great news is we


### [08:00 - 09:00]

**[08:02]** how to do it. And the great news is we

**[08:02]** how to do it. And the great news is we made it available for all of you to use

**[08:05]** made it available for all of you to use

**[08:05]** made it available for all of you to use as well. So just a few weeks ago, we

**[08:08]** as well. So just a few weeks ago, we

**[08:08]** as well. So just a few weeks ago, we released Strand agents. It's an open-

**[08:11]** released Strand agents. It's an open-

**[08:11]** released Strand agents. It's an open- source Python SDK which you can check

**[08:14]** source Python SDK which you can check

**[08:14]** source Python SDK which you can check out and start building and running AI

**[08:17]** out and start building and running AI

**[08:18]** out and start building and running AI agents in just a few lines of code. So

**[08:21]** agents in just a few lines of code. So

**[08:21]** agents in just a few lines of code. So let me show you quickly how this looks

**[08:22]** let me show you quickly how this looks

**[08:22]** let me show you quickly how this looks like. And before I go in here, just a

**[08:26]** like. And before I go in here, just a

**[08:26]** like. And before I go in here, just a fun fact. If you wonder why did they

**[08:28]** fun fact. If you wonder why did they

**[08:28]** fun fact. If you wonder why did they call it trans agents?

**[08:31]** call it trans agents?

**[08:31]** call it trans agents? Well, this is what happens if you let AI

**[08:33]** Well, this is what happens if you let AI

**[08:33]** Well, this is what happens if you let AI pick its own name.

**[08:36]** pick its own name.

**[08:36]** pick its own name. All right. So the reasoning behind

**[08:38]** All right. So the reasoning behind

**[08:38]** All right. So the reasoning behind because again the AI agent is is capable

**[08:41]** because again the AI agent is is capable

**[08:41]** because again the AI agent is is capable of reasoning. It came up with like think

**[08:43]** of reasoning. It came up with like think

**[08:43]** of reasoning. It came up with like think about the two strands of DNA

**[08:46]** about the two strands of DNA

**[08:46]** about the two strands of DNA and just like the two strands of DNA

**[08:49]** and just like the two strands of DNA

**[08:49]** and just like the two strands of DNA strands agents connects the two core

**[08:51]** strands agents connects the two core

**[08:51]** strands agents connects the two core pieces of an agent together the model

**[08:55]** pieces of an agent together the model

**[08:55]** pieces of an agent together the model and the tools.

**[08:57]** and the tools.

**[08:57]** and the tools. And it helps you building agents. It


### [09:00 - 10:00]

**[09:00]** And it helps you building agents. It

**[09:00]** And it helps you building agents. It simplifies it by you really relying on

**[09:02]** simplifies it by you really relying on

**[09:02]** simplifies it by you really relying on those state-of-the-art models to reason,

**[09:05]** those state-of-the-art models to reason,

**[09:05]** those state-of-the-art models to reason, to plan, and take action. You can simply

**[09:08]** to plan, and take action. You can simply

**[09:08]** to plan, and take action. You can simply start with defining a prompt and your

**[09:10]** start with defining a prompt and your

**[09:10]** start with defining a prompt and your tools in code and then test it out

**[09:13]** tools in code and then test it out

**[09:13]** tools in code and then test it out locally and then once you're ready,

**[09:15]** locally and then once you're ready,

**[09:15]** locally and then once you're ready, deploy it for example in the cloud.

**[09:19]** deploy it for example in the cloud.

**[09:19]** deploy it for example in the cloud. And this is how simple it is. Again,

**[09:21]** And this is how simple it is. Again,

**[09:21]** And this is how simple it is. Again, just a couple of lines should look

**[09:23]** just a couple of lines should look

**[09:23]** just a couple of lines should look pretty familiar. You install strands

**[09:25]** pretty familiar. You install strands

**[09:25]** pretty familiar. You install strands agents, you import it and then it comes

**[09:27]** agents, you import it and then it comes

**[09:27]** agents, you import it and then it comes with pre-built tools which I talk about

**[09:29]** with pre-built tools which I talk about

**[09:29]** with pre-built tools which I talk about a little bit more in detail and

**[09:32]** a little bit more in detail and

**[09:32]** a little bit more in detail and basically you just add the tools to your

**[09:34]** basically you just add the tools to your

**[09:34]** basically you just add the tools to your agent and then you can start asking it

**[09:36]** agent and then you can start asking it

**[09:36]** agent and then you can start asking it questions or building more complex

**[09:38]** questions or building more complex

**[09:38]** questions or building more complex workflows with it.

**[09:40]** workflows with it.

**[09:40]** workflows with it. Now by default strands agents integrates

**[09:44]** Now by default strands agents integrates

**[09:44]** Now by default strands agents integrates with Amazon Bedrock as the model

**[09:45]** with Amazon Bedrock as the model

**[09:45]** with Amazon Bedrock as the model provider. So you can check the model

**[09:47]** provider. So you can check the model

**[09:47]** provider. So you can check the model config here using cloud 3.7 sonnet. But

**[09:52]** config here using cloud 3.7 sonnet. But

**[09:52]** config here using cloud 3.7 sonnet. But of course, it's not just limited to AWS.

**[09:56]** of course, it's not just limited to AWS.

**[09:56]** of course, it's not just limited to AWS. You can use Strand agents across

**[09:59]** You can use Strand agents across

**[09:59]** You can use Strand agents across multiple providers. For example, we have


### [10:00 - 11:00]

**[10:01]** multiple providers. For example, we have

**[10:01]** multiple providers. For example, we have integrations with a llama. So you can

**[10:03]** integrations with a llama. So you can

**[10:03]** integrations with a llama. So you can start developing locally, testing it

**[10:05]** start developing locally, testing it

**[10:05]** start developing locally, testing it out. We have integrations and tropicedit

**[10:08]** out. We have integrations and tropicedit

**[10:08]** out. We have integrations and tropicedit integrations, metaedit integrations to

**[10:10]** integrations, metaedit integrations to

**[10:10]** integrations, metaedit integrations to the llama API. You can use openAI models

**[10:13]** the llama API. You can use openAI models

**[10:13]** the llama API. You can use openAI models and any other providers available

**[10:14]** and any other providers available

**[10:14]** and any other providers available through the integration with light LLM.

**[10:17]** through the integration with light LLM.

**[10:17]** through the integration with light LLM. And of course, you can also develop your

**[10:19]** And of course, you can also develop your

**[10:19]** And of course, you can also develop your own custom model provider.

**[10:26]** Now quickly on the tools as I said

**[10:26]** Now quickly on the tools as I said agents comes with over 20 pre-built

**[10:29]** agents comes with over 20 pre-built

**[10:29]** agents comes with over 20 pre-built tools. So anything from simple tasks

**[10:31]** tools. So anything from simple tasks

**[10:31]** tools. So anything from simple tasks like hey I just want to do some file

**[10:34]** like hey I just want to do some file

**[10:34]** like hey I just want to do some file manipulation some API calls obviously

**[10:36]** manipulation some API calls obviously

**[10:36]** manipulation some API calls obviously integrate with AWS services but then

**[10:39]** integrate with AWS services but then

**[10:39]** integrate with AWS services but then also more complex use cases and I just

**[10:42]** also more complex use cases and I just

**[10:42]** also more complex use cases and I just want to call out a couple of them. So

**[10:45]** want to call out a couple of them. So

**[10:45]** want to call out a couple of them. So there's a whole group of integrated

**[10:47]** there's a whole group of integrated

**[10:47]** there's a whole group of integrated tools for memory and rack. One tool

**[10:50]** tools for memory and rack. One tool

**[10:50]** tools for memory and rack. One tool specifically called retrieve which lets

**[10:52]** specifically called retrieve which lets

**[10:52]** specifically called retrieve which lets you do semantic search over a knowledge

**[10:55]** you do semantic search over a knowledge

**[10:55]** you do semantic search over a knowledge base. And just to show you the power of

**[10:57]** base. And just to show you the power of

**[10:57]** base. And just to show you the power of this, we have an internal agent at AWS


### [11:00 - 12:00]

**[11:01]** this, we have an internal agent at AWS

**[11:01]** this, we have an internal agent at AWS that manages over 6,000 tools.

**[11:05]** that manages over 6,000 tools.

**[11:05]** that manages over 6,000 tools. Now 6,000 is a hard number of tools to

**[11:08]** Now 6,000 is a hard number of tools to

**[11:08]** Now 6,000 is a hard number of tools to put into a single context window and

**[11:10]** put into a single context window and

**[11:10]** put into a single context window and give um one model to decide. So what we

**[11:13]** give um one model to decide. So what we

**[11:13]** give um one model to decide. So what we did is we put the descriptions of those

**[11:15]** did is we put the descriptions of those

**[11:15]** did is we put the descriptions of those tools in a knowledge base and use the

**[11:18]** tools in a knowledge base and use the

**[11:18]** tools in a knowledge base and use the retrieve tool here. So the agent can

**[11:21]** retrieve tool here. So the agent can

**[11:21]** retrieve tool here. So the agent can find the most relevant tools for the

**[11:23]** find the most relevant tools for the

**[11:23]** find the most relevant tools for the task at hand and only pull those tools

**[11:26]** task at hand and only pull those tools

**[11:26]** task at hand and only pull those tools back into the model context for the

**[11:28]** back into the model context for the

**[11:28]** back into the model context for the model to decide which one to take. So

**[11:30]** model to decide which one to take. So

**[11:30]** model to decide which one to take. So that's just one use case how we're

**[11:32]** that's just one use case how we're

**[11:32]** that's just one use case how we're leveraging that. Also there is support

**[11:35]** leveraging that. Also there is support

**[11:35]** leveraging that. Also there is support for multimodality across images, video

**[11:38]** for multimodality across images, video

**[11:38]** for multimodality across images, video and audio with strands. There is a tool

**[11:42]** and audio with strands. There is a tool

**[11:42]** and audio with strands. There is a tool to kind of prompt for more thinking and

**[11:45]** to kind of prompt for more thinking and

**[11:45]** to kind of prompt for more thinking and deep reasoning and it also comes with

**[11:48]** deep reasoning and it also comes with

**[11:48]** deep reasoning and it also comes with pre-built tools to implement multi- aent

**[11:50]** pre-built tools to implement multi- aent

**[11:50]** pre-built tools to implement multi- aent workflows whether it's graph-based

**[11:53]** workflows whether it's graph-based

**[11:53]** workflows whether it's graph-based workflows or a swarm of sub aents

**[11:56]** workflows or a swarm of sub aents

**[11:56]** workflows or a swarm of sub aents working together.


### [12:00 - 13:00]

**[12:02]** Now you cannot talk about tools without

**[12:02]** Now you cannot talk about tools without mentioning MCP right?

**[12:05]** mentioning MCP right?

**[12:05]** mentioning MCP right? So obviously we integrated MCP here

**[12:08]** So obviously we integrated MCP here

**[12:08]** So obviously we integrated MCP here natively within strands. So you can just

**[12:10]** natively within strands. So you can just

**[12:10]** natively within strands. So you can just use this also to connect to thousands of

**[12:12]** use this also to connect to thousands of

**[12:12]** use this also to connect to thousands of available MCP servers and make them

**[12:15]** available MCP servers and make them

**[12:15]** available MCP servers and make them available as tools for your agent.

**[12:18]** available as tools for your agent.

**[12:18]** available as tools for your agent. Support for A2A is also coming soon. But

**[12:22]** Support for A2A is also coming soon. But

**[12:22]** Support for A2A is also coming soon. But let's start and talk a little bit about

**[12:24]** let's start and talk a little bit about

**[12:24]** let's start and talk a little bit about MCP first.

**[12:27]** MCP first.

**[12:27]** MCP first. If you're building on AWS already, make

**[12:29]** If you're building on AWS already, make

**[12:29]** If you're building on AWS already, make sure to bookmark this GitHub repo. It's

**[12:32]** sure to bookmark this GitHub repo. It's

**[12:32]** sure to bookmark this GitHub repo. It's labmc.

**[12:33]** labmc.

**[12:34]** labmc. And here you can find a very long list

**[12:36]** And here you can find a very long list

**[12:36]** And here you can find a very long list much longer than you what would you see

**[12:37]** much longer than you what would you see

**[12:37]** much longer than you what would you see here on this slide of and growing number

**[12:40]** here on this slide of and growing number

**[12:40]** here on this slide of and growing number of the MCP server implementations

**[12:42]** of the MCP server implementations

**[12:42]** of the MCP server implementations specifically if you're working and

**[12:44]** specifically if you're working and

**[12:44]** specifically if you're working and building on AWS.

**[12:51]** Now, one of the challenges stems from

**[12:51]** Now, one of the challenges stems from the fact that once we all started

**[12:53]** the fact that once we all started

**[12:53]** the fact that once we all started building MCP servers, what we had was

**[12:55]** building MCP servers, what we had was

**[12:55]** building MCP servers, what we had was standard IO, right? So, it started out

**[12:58]** standard IO, right? So, it started out

**[12:58]** standard IO, right? So, it started out to help locally connect your systems,


### [13:00 - 14:00]

**[13:01]** to help locally connect your systems,

**[13:01]** to help locally connect your systems, your clients to respective tools.

**[13:05]** your clients to respective tools.

**[13:05]** your clients to respective tools. And here's just a quick example, which

**[13:07]** And here's just a quick example, which

**[13:07]** And here's just a quick example, which is important for a demo I'll show in a

**[13:09]** is important for a demo I'll show in a

**[13:09]** is important for a demo I'll show in a little bit. This is just a standard IO

**[13:12]** little bit. This is just a standard IO

**[13:12]** little bit. This is just a standard IO implementation of an MCP server. should

**[13:14]** implementation of an MCP server. should

**[13:14]** implementation of an MCP server. should look familiar to most of you working

**[13:15]** look familiar to most of you working

**[13:15]** look familiar to most of you working with MCP using the Python SDK using fast

**[13:19]** with MCP using the Python SDK using fast

**[13:19]** with MCP using the Python SDK using fast MCP. All I'm doing here is set up my

**[13:22]** MCP. All I'm doing here is set up my

**[13:22]** MCP. All I'm doing here is set up my server and using the decorator to define

**[13:24]** server and using the decorator to define

**[13:24]** server and using the decorator to define a tool. In this case, my tool is to roll

**[13:27]** a tool. In this case, my tool is to roll

**[13:28]** a tool. In this case, my tool is to roll a dice. And you might see in the code

**[13:31]** a dice. And you might see in the code

**[13:31]** a dice. And you might see in the code here, it has an input to define the

**[13:33]** here, it has an input to define the

**[13:33]** here, it has an input to define the number of sides. And I had to put a

**[13:37]** number of sides. And I had to put a

**[13:37]** number of sides. And I had to put a picture here because I have to admit,

**[13:39]** picture here because I have to admit,

**[13:39]** picture here because I have to admit, um, I just learned this myself. Do we

**[13:41]** um, I just learned this myself. Do we

**[13:41]** um, I just learned this myself. Do we have DND fans in the room?

**[13:44]** have DND fans in the room?

**[13:44]** have DND fans in the room? Woohoo. All right, a few of them. So,

**[13:46]** Woohoo. All right, a few of them. So,

**[13:46]** Woohoo. All right, a few of them. So, you all know what I'm talking about. For

**[13:49]** you all know what I'm talking about. For

**[13:49]** you all know what I'm talking about. For the rest of us, I just learned um there

**[13:52]** the rest of us, I just learned um there

**[13:52]** the rest of us, I just learned um there are dices, and I have one here. Not sure

**[13:54]** are dices, and I have one here. Not sure

**[13:54]** are dices, and I have one here. Not sure if the camera can catch this. Um it's

**[13:56]** if the camera can catch this. Um it's

**[13:56]** if the camera can catch this. Um it's just one of them here on the slide. A

**[13:59]** just one of them here on the slide. A

**[13:59]** just one of them here on the slide. A dice that has, for example, this one has


### [14:00 - 15:00]

**[14:01]** dice that has, for example, this one has

**[14:01]** dice that has, for example, this one has 20 sides. Something very normal in the

**[14:04]** 20 sides. Something very normal in the

**[14:04]** 20 sides. Something very normal in the D&D world to start, I think, your game.

**[14:07]** D&D world to start, I think, your game.

**[14:07]** D&D world to start, I think, your game. Um, don't ask me questions about D and

**[14:09]** Um, don't ask me questions about D and

**[14:09]** Um, don't ask me questions about D and D. my colleague Mike Chambers who is

**[14:11]** D. my colleague Mike Chambers who is

**[14:11]** D. my colleague Mike Chambers who is either here or in the expo right now. He

**[14:12]** either here or in the expo right now. He

**[14:12]** either here or in the expo right now. He built the demo, so kudos to him and he

**[14:14]** built the demo, so kudos to him and he

**[14:14]** built the demo, so kudos to him and he can answer all of the D&D questions. All

**[14:17]** can answer all of the D&D questions. All

**[14:17]** can answer all of the D&D questions. All right, just keep that in mind. Um, I'll

**[14:19]** right, just keep that in mind. Um, I'll

**[14:19]** right, just keep that in mind. Um, I'll come back to this in just a second.

**[14:22]** come back to this in just a second.

**[14:22]** come back to this in just a second. Now, what we want to do here is to

**[14:25]** Now, what we want to do here is to

**[14:25]** Now, what we want to do here is to decouple and kind of connect to remote

**[14:28]** decouple and kind of connect to remote

**[14:28]** decouple and kind of connect to remote MCP servers because the topic is to

**[14:30]** MCP servers because the topic is to

**[14:30]** MCP servers because the topic is to scale, right? And the way to do this is

**[14:34]** scale, right? And the way to do this is

**[14:34]** scale, right? And the way to do this is in the AWS world as easy as just

**[14:36]** in the AWS world as easy as just

**[14:36]** in the AWS world as easy as just deploying it as an Lambda function. So

**[14:39]** deploying it as an Lambda function. So

**[14:39]** deploying it as an Lambda function. So we can do this now with streamable HTTP.

**[14:42]** we can do this now with streamable HTTP.

**[14:42]** we can do this now with streamable HTTP. And the same concepts apply. You put

**[14:44]** And the same concepts apply. You put

**[14:44]** And the same concepts apply. You put your Lambda functions as you would have

**[14:46]** your Lambda functions as you would have

**[14:46]** your Lambda functions as you would have before behind an MCP gateway and then

**[14:49]** before behind an MCP gateway and then

**[14:49]** before behind an MCP gateway and then connect. And because we care about

**[14:51]** connect. And because we care about

**[14:51]** connect. And because we care about security and authorization in the quick

**[14:53]** security and authorization in the quick

**[14:53]** security and authorization in the quick demo I'm going to show you, I'm using an

**[14:55]** demo I'm going to show you, I'm using an

**[14:55]** demo I'm going to show you, I'm using an authorizer. Um you can also plug in a

**[14:57]** authorizer. Um you can also plug in a

**[14:57]** authorizer. Um you can also plug in a Cognto framework for this part. And I'm


### [15:00 - 16:00]

**[15:00]** Cognto framework for this part. And I'm

**[15:00]** Cognto framework for this part. And I'm also going to store session data in a

**[15:02]** also going to store session data in a

**[15:02]** also going to store session data in a Dynamob table.

**[15:04]** Dynamob table.

**[15:04]** Dynamob table. So let's roll this quick demo here. So

**[15:06]** So let's roll this quick demo here. So

**[15:06]** So let's roll this quick demo here. So what you see here is an MCP Lambda

**[15:09]** what you see here is an MCP Lambda

**[15:09]** what you see here is an MCP Lambda handler that we developed. It's

**[15:10]** handler that we developed. It's

**[15:10]** handler that we developed. It's available on the GitHub repo which makes

**[15:12]** available on the GitHub repo which makes

**[15:12]** available on the GitHub repo which makes it really easy to kind of set up your

**[15:14]** it really easy to kind of set up your

**[15:14]** it really easy to kind of set up your MCP server in Lambda. Here's a very

**[15:16]** MCP server in Lambda. Here's a very

**[15:16]** MCP server in Lambda. Here's a very simple hello world example. The tool is

**[15:19]** simple hello world example. The tool is

**[15:19]** simple hello world example. The tool is just um again defined with a tool

**[15:21]** just um again defined with a tool

**[15:22]** just um again defined with a tool decorator in here and then in the lambda

**[15:23]** decorator in here and then in the lambda

**[15:23]** decorator in here and then in the lambda handler function you can reference um

**[15:26]** handler function you can reference um

**[15:26]** handler function you can reference um the input here the invoke function and

**[15:28]** the input here the invoke function and

**[15:28]** the input here the invoke function and pass it to that MCP server. Now if we're

**[15:31]** pass it to that MCP server. Now if we're

**[15:31]** pass it to that MCP server. Now if we're looking at the server implementation and

**[15:32]** looking at the server implementation and

**[15:32]** looking at the server implementation and here we're doing a little bit more. You

**[15:34]** here we're doing a little bit more. You

**[15:34]** here we're doing a little bit more. You can see how we're adding session table

**[15:37]** can see how we're adding session table

**[15:37]** can see how we're adding session table support which is a DynamoB table. We're

**[15:39]** support which is a DynamoB table. We're

**[15:39]** support which is a DynamoB table. We're defining the tool. This is the rolling

**[15:42]** defining the tool. This is the rolling

**[15:42]** defining the tool. This is the rolling dice tool that I just pointed out but

**[15:44]** dice tool that I just pointed out but

**[15:44]** dice tool that I just pointed out but this time it's hosted as a lambda

**[15:46]** this time it's hosted as a lambda

**[15:46]** this time it's hosted as a lambda function. You can write all the code you

**[15:48]** function. You can write all the code you

**[15:48]** function. You can write all the code you want to have there as well. And then at

**[15:50]** want to have there as well. And then at

**[15:50]** want to have there as well. And then at the very end, it's the same single line

**[15:51]** the very end, it's the same single line

**[15:52]** the very end, it's the same single line that basically when you call the lambda

**[15:54]** that basically when you call the lambda

**[15:54]** that basically when you call the lambda function passes this on to the MCP

**[15:56]** function passes this on to the MCP

**[15:56]** function passes this on to the MCP server.


### [16:00 - 17:00]

**[16:01]** Let's deploy this. And again, we're

**[16:01]** Let's deploy this. And again, we're using the existing tools to deploy

**[16:03]** using the existing tools to deploy

**[16:03]** using the existing tools to deploy Lambda functions as we have before. So

**[16:05]** Lambda functions as we have before. So

**[16:05]** Lambda functions as we have before. So this one is using AWS SAM to just deploy

**[16:08]** this one is using AWS SAM to just deploy

**[16:08]** this one is using AWS SAM to just deploy that to the cloud. And then we will

**[16:10]** that to the cloud. And then we will

**[16:10]** that to the cloud. And then we will receive the API gateway URL as well. Now

**[16:14]** receive the API gateway URL as well. Now

**[16:14]** receive the API gateway URL as well. Now from the client side here I'm using

**[16:15]** from the client side here I'm using

**[16:16]** from the client side here I'm using strands agents as you can see and then I

**[16:19]** strands agents as you can see and then I

**[16:19]** strands agents as you can see and then I am using the MCP integration. I'm

**[16:23]** am using the MCP integration. I'm

**[16:23]** am using the MCP integration. I'm passing here my API gateway URL to

**[16:26]** passing here my API gateway URL to

**[16:26]** passing here my API gateway URL to connect for author authorization. I have

**[16:29]** connect for author authorization. I have

**[16:29]** connect for author authorization. I have a bureau token. Again this is a simple

**[16:30]** a bureau token. Again this is a simple

**[16:30]** a bureau token. Again this is a simple concept demo but you can build more

**[16:33]** concept demo but you can build more

**[16:33]** concept demo but you can build more robust integrations here as well. I'm

**[16:36]** robust integrations here as well. I'm

**[16:36]** robust integrations here as well. I'm calling the list tool and then I'm

**[16:38]** calling the list tool and then I'm

**[16:38]** calling the list tool and then I'm passing those tools to my agent as we've

**[16:40]** passing those tools to my agent as we've

**[16:40]** passing those tools to my agent as we've seen before. This time it's the MCP

**[16:42]** seen before. This time it's the MCP

**[16:42]** seen before. This time it's the MCP available tools. And then if we run this

**[16:46]** available tools. And then if we run this

**[16:46]** available tools. And then if we run this here, we can quickly see this in action

**[16:50]** here, we can quickly see this in action

**[16:50]** here, we can quickly see this in action and basically going to ask it here to

**[16:52]** and basically going to ask it here to

**[16:52]** and basically going to ask it here to roll a dice.

**[16:55]** roll a dice.

**[16:55]** roll a dice. And we're asking it to roll a d20. So

**[16:57]** And we're asking it to roll a d20. So

**[16:57]** And we're asking it to roll a d20. So again, 20 sides and it's coming back.


### [17:00 - 18:00]

**[17:02]** again, 20 sides and it's coming back.

**[17:02]** again, 20 sides and it's coming back. What did we roll? You can see the tool

**[17:04]** What did we roll? You can see the tool

**[17:04]** What did we roll? You can see the tool is kicking in here. We rolled a seven.

**[17:06]** is kicking in here. We rolled a seven.

**[17:06]** is kicking in here. We rolled a seven. Great. So this is just really a quick

**[17:09]** Great. So this is just really a quick

**[17:09]** Great. So this is just really a quick example. The good news is once you're in

**[17:11]** example. The good news is once you're in

**[17:11]** example. The good news is once you're in the AWS world and you're working in

**[17:12]** the AWS world and you're working in

**[17:12]** the AWS world and you're working in Lambda, everything you can build with

**[17:14]** Lambda, everything you can build with

**[17:14]** Lambda, everything you can build with Lambda, you can integrate there. So

**[17:16]** Lambda, you can integrate there. So

**[17:16]** Lambda, you can integrate there. So basically you have access again to all

**[17:18]** basically you have access again to all

**[17:18]** basically you have access again to all of the great features, capabilities,

**[17:19]** of the great features, capabilities,

**[17:19]** of the great features, capabilities, applications you might have already

**[17:21]** applications you might have already

**[17:21]** applications you might have already built on AWS.

**[17:23]** built on AWS.

**[17:23]** built on AWS. Now the next step here is how do we make

**[17:26]** Now the next step here is how do we make

**[17:26]** Now the next step here is how do we make agents talk to each other, right? That's

**[17:27]** agents talk to each other, right? That's

**[17:28]** agents talk to each other, right? That's kind of the the next frontier. And we

**[17:30]** kind of the the next frontier. And we

**[17:30]** kind of the the next frontier. And we are super excited about the all the open

**[17:32]** are super excited about the all the open

**[17:32]** are super excited about the all the open protocols that are emerging right now

**[17:35]** protocols that are emerging right now

**[17:35]** protocols that are emerging right now with MCP. For example, we joined the

**[17:37]** with MCP. For example, we joined the

**[17:37]** with MCP. For example, we joined the steering committee. We're active part of

**[17:39]** steering committee. We're active part of

**[17:39]** steering committee. We're active part of the community contributing code and

**[17:41]** the community contributing code and

**[17:41]** the community contributing code and helping to further evolve MCP. If you

**[17:44]** helping to further evolve MCP. If you

**[17:44]** helping to further evolve MCP. If you want to learn more about this, here is

**[17:45]** want to learn more about this, here is

**[17:45]** want to learn more about this, here is the QR code. We have a whole blog series

**[17:48]** the QR code. We have a whole blog series

**[17:48]** the QR code. We have a whole blog series started on our open source blog. Feel

**[17:50]** started on our open source blog. Feel

**[17:50]** started on our open source blog. Feel free to check that out as we continue to

**[17:52]** free to check that out as we continue to

**[17:52]** free to check that out as we continue to help evolve those protocols.

**[17:56]** help evolve those protocols.

**[17:56]** help evolve those protocols. Now, what's next? We all are aware that


### [18:00 - 19:00]

**[18:00]** Now, what's next? We all are aware that

**[18:00]** Now, what's next? We all are aware that this is just the beginning, right? There

**[18:02]** this is just the beginning, right? There

**[18:02]** this is just the beginning, right? There will be so much more coming. And if you

**[18:04]** will be so much more coming. And if you

**[18:04]** will be so much more coming. And if you had a chance to check out my colleague

**[18:06]** had a chance to check out my colleague

**[18:06]** had a chance to check out my colleague Danielle's talk yesterday on useful

**[18:08]** Danielle's talk yesterday on useful

**[18:08]** Danielle's talk yesterday on useful general intelligence, I just want to

**[18:09]** general intelligence, I just want to

**[18:09]** general intelligence, I just want to quote her a little bit. She said, "The

**[18:12]** quote her a little bit. She said, "The

**[18:12]** quote her a little bit. She said, "The atomic unit of all digital interactions

**[18:15]** atomic unit of all digital interactions

**[18:15]** atomic unit of all digital interactions will be an agent call." So we can

**[18:18]** will be an agent call." So we can

**[18:18]** will be an agent call." So we can imagine a future here where you might

**[18:19]** imagine a future here where you might

**[18:19]** imagine a future here where you might just have personal agent like shown like

**[18:21]** just have personal agent like shown like

**[18:21]** just have personal agent like shown like this connecting to an agent store and

**[18:25]** this connecting to an agent store and

**[18:25]** this connecting to an agent store and really kind of having agents together

**[18:27]** really kind of having agents together

**[18:27]** really kind of having agents together accomplishing tasks for you. And some of

**[18:29]** accomplishing tasks for you. And some of

**[18:29]** accomplishing tasks for you. And some of you here in the room might already be

**[18:30]** you here in the room might already be

**[18:30]** you here in the room might already be building this, right?

**[18:32]** building this, right?

**[18:32]** building this, right? So let's go and build this future

**[18:34]** So let's go and build this future

**[18:34]** So let's go and build this future together. Thanks so much. Check out the

**[18:37]** together. Thanks so much. Check out the

**[18:37]** together. Thanks so much. Check out the additional sessions we have. My

**[18:39]** additional sessions we have. My

**[18:39]** additional sessions we have. My colleague Mike is going much more into

**[18:40]** colleague Mike is going much more into

**[18:40]** colleague Mike is going much more into the rolling dice demo, everything MCP

**[18:43]** the rolling dice demo, everything MCP

**[18:43]** the rolling dice demo, everything MCP and strands. And my colleague Suman

**[18:44]** and strands. And my colleague Suman

**[18:44]** and strands. And my colleague Suman tomorrow will also have a deep dive on

**[18:46]** tomorrow will also have a deep dive on

**[18:46]** tomorrow will also have a deep dive on strands. And with that, thank you very

**[18:48]** strands. And with that, thank you very

**[18:48]** strands. And with that, thank you very much. Check us out in the expo hall and

**[18:51]** much. Check us out in the expo hall and

**[18:51]** much. Check us out in the expo hall and grab your own D20.

**[18:53]** grab your own D20.

**[18:53]** grab your own D20. [Music]


