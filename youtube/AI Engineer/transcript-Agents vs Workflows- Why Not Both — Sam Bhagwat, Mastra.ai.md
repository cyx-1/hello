# Agents vs Workflows- Why Not Both — Sam Bhagwat, Mastra.ai

**Video URL:** https://www.youtube.com/watch?v=8SUJEqQNClw

---

## Full Transcript

### [00:00 - 01:00]

**[00:16]** Okay. Agents or workflows? Why not both?

**[00:16]** Okay. Agents or workflows? Why not both? Uh, thank you, Alex, for the nice intro.

**[00:19]** Uh, thank you, Alex, for the nice intro.

**[00:19]** Uh, thank you, Alex, for the nice intro. Um, uh, like like he said, I used to be

**[00:22]** Um, uh, like like he said, I used to be

**[00:22]** Um, uh, like like he said, I used to be the founder of co-founder of Gatsby. Um,

**[00:25]** the founder of co-founder of Gatsby. Um,

**[00:25]** the founder of co-founder of Gatsby. Um, I wrote a book called Principles of AI

**[00:27]** I wrote a book called Principles of AI

**[00:27]** I wrote a book called Principles of AI agents, which is floating around.

**[00:28]** agents, which is floating around.

**[00:28]** agents, which is floating around. Hopefully many of you have gotten a

**[00:30]** Hopefully many of you have gotten a

**[00:30]** Hopefully many of you have gotten a copy. We we have more around the

**[00:32]** copy. We we have more around the

**[00:32]** copy. We we have more around the conference. Uh there was a big debate uh

**[00:35]** conference. Uh there was a big debate uh

**[00:35]** conference. Uh there was a big debate uh a couple of months ago which the term on

**[00:39]** a couple of months ago which the term on

**[00:39]** a couple of months ago which the term on Twitter people may have noticed um which

**[00:41]** Twitter people may have noticed um which

**[00:42]** Twitter people may have noticed um which I just referenced. Um and I think like

**[00:44]** I just referenced. Um and I think like

**[00:44]** I just referenced. Um and I think like this is a big reason why I'm h why we're

**[00:48]** this is a big reason why I'm h why we're

**[00:48]** this is a big reason why I'm h why we're having this talk why we're having this

**[00:49]** having this talk why we're having this

**[00:49]** having this talk why we're having this track. Um this is going to be kind of

**[00:51]** track. Um this is going to be kind of

**[00:51]** track. Um this is going to be kind of like a reverse mullet talk or something

**[00:53]** like a reverse mullet talk or something

**[00:53]** like a reverse mullet talk or something like that. It's like party in the front,

**[00:54]** like that. It's like party in the front,

**[00:54]** like that. It's like party in the front, business in the back or something. So,

**[00:56]** business in the back or something. So,

**[00:56]** business in the back or something. So, we're going to start with the party or

**[00:57]** we're going to start with the party or

**[00:57]** we're going to start with the party or the debate or or whatever this is. Um,


### [01:00 - 02:00]

**[01:00]** the debate or or whatever this is. Um,

**[01:00]** the debate or or whatever this is. Um, this is referenced in the last talk as

**[01:01]** this is referenced in the last talk as

**[01:02]** this is referenced in the last talk as well. Anthropic wrote a great uh blog

**[01:03]** well. Anthropic wrote a great uh blog

**[01:03]** well. Anthropic wrote a great uh blog post in December. Um, it was called

**[01:06]** post in December. Um, it was called

**[01:06]** post in December. Um, it was called building effective agents. It had great

**[01:08]** building effective agents. It had great

**[01:08]** building effective agents. It had great diagrams. It showed what an agent was.

**[01:10]** diagrams. It showed what an agent was.

**[01:10]** diagrams. It showed what an agent was. Can we close the door, please? Um, it it

**[01:13]** Can we close the door, please? Um, it it

**[01:13]** Can we close the door, please? Um, it it showed uh like some workflow examples um

**[01:17]** showed uh like some workflow examples um

**[01:17]** showed uh like some workflow examples um like different sort of types of routing

**[01:20]** like different sort of types of routing

**[01:20]** like different sort of types of routing and orchestration. It was a great blog

**[01:22]** and orchestration. It was a great blog

**[01:22]** and orchestration. It was a great blog post. Um, in April, OpenAI also released

**[01:26]** post. Um, in April, OpenAI also released

**[01:26]** post. Um, in April, OpenAI also released a paper. I think there was some

**[01:28]** a paper. I think there was some

**[01:28]** a paper. I think there was some controversy about that on Twitter

**[01:29]** controversy about that on Twitter

**[01:29]** controversy about that on Twitter because some of the points people made

**[01:32]** because some of the points people made

**[01:32]** because some of the points people made was like, look, this isn't a lot of new

**[01:33]** was like, look, this isn't a lot of new

**[01:33]** was like, look, this isn't a lot of new material. Um, other people pointed out

**[01:36]** material. Um, other people pointed out

**[01:36]** material. Um, other people pointed out this kind of call out at the end, which

**[01:38]** this kind of call out at the end, which

**[01:38]** this kind of call out at the end, which is basically like an anti-workflow

**[01:40]** is basically like an anti-workflow

**[01:40]** is basically like an anti-workflow blast. It's like, hey, like and and I

**[01:43]** blast. It's like, hey, like and and I

**[01:43]** blast. It's like, hey, like and and I think people were like, hey yo, what's

**[01:45]** think people were like, hey yo, what's

**[01:45]** think people were like, hey yo, what's going on here? This is just like not

**[01:46]** going on here? This is just like not

**[01:46]** going on here? This is just like not accurate and it's coming from a big

**[01:47]** accurate and it's coming from a big

**[01:48]** accurate and it's coming from a big model provider. It's just kind of

**[01:49]** model provider. It's just kind of

**[01:49]** model provider. It's just kind of muddying the water. There was there was

**[01:51]** muddying the water. There was there was

**[01:51]** muddying the water. There was there was a lot of uh controversy around that that

**[01:54]** a lot of uh controversy around that that

**[01:54]** a lot of uh controversy around that that was the uh Swix blog post I was

**[01:56]** was the uh Swix blog post I was

**[01:56]** was the uh Swix blog post I was referencing uh emergency blog post um

**[01:59]** referencing uh emergency blog post um

**[01:59]** referencing uh emergency blog post um went out on latent space. Uh I have a


### [02:00 - 03:00]

**[02:02]** went out on latent space. Uh I have a

**[02:02]** went out on latent space. Uh I have a couple hot takes on that and then I have

**[02:03]** couple hot takes on that and then I have

**[02:03]** couple hot takes on that and then I have a takeaway. I promise both the hot takes

**[02:05]** a takeaway. I promise both the hot takes

**[02:05]** a takeaway. I promise both the hot takes and the takeaway are relevant to the

**[02:07]** and the takeaway are relevant to the

**[02:07]** and the takeaway are relevant to the systems you're building. Um we care a

**[02:09]** systems you're building. Um we care a

**[02:09]** systems you're building. Um we care a lot about this. There's a reason we

**[02:10]** lot about this. There's a reason we

**[02:10]** lot about this. There's a reason we wrote a we wrote a book. Um first hot

**[02:13]** wrote a we wrote a book. Um first hot

**[02:13]** wrote a we wrote a book. Um first hot take is like look just this I'm going to

**[02:16]** take is like look just this I'm going to

**[02:16]** take is like look just this I'm going to add open AI here but it's like just

**[02:17]** add open AI here but it's like just

**[02:17]** add open AI here but it's like just don't be that guy. Um, and I'll I'll

**[02:19]** don't be that guy. Um, and I'll I'll

**[02:19]** don't be that guy. Um, and I'll I'll explain like the context of the like I

**[02:22]** explain like the context of the like I

**[02:22]** explain like the context of the like I mean I think we know this meme but like

**[02:23]** mean I think we know this meme but like

**[02:24]** mean I think we know this meme but like the what I mean by that guy in this

**[02:25]** the what I mean by that guy in this

**[02:25]** the what I mean by that guy in this context. So that guy just thinks that

**[02:27]** context. So that guy just thinks that

**[02:28]** context. So that guy just thinks that like they and they alone like know the

**[02:29]** like they and they alone like know the

**[02:29]** like they and they alone like know the only right way to do development. Um

**[02:33]** only right way to do development. Um

**[02:33]** only right way to do development. Um sometimes and like we I actually ran

**[02:35]** sometimes and like we I actually ran

**[02:35]** sometimes and like we I actually ran into Lori Voss in the hallway yesterday

**[02:39]** into Lori Voss in the hallway yesterday

**[02:39]** into Lori Voss in the hallway yesterday and we started talking about that guy

**[02:40]** and we started talking about that guy

**[02:40]** and we started talking about that guy that we sort of had known from the last

**[02:43]** that we sort of had known from the last

**[02:43]** that we sort of had known from the last decade. Um, but sometimes that guy works

**[02:45]** decade. Um, but sometimes that guy works

**[02:45]** decade. Um, but sometimes that guy works for this for like a fang style company

**[02:48]** for this for like a fang style company

**[02:48]** for this for like a fang style company and they're in like a public facing role

**[02:49]** and they're in like a public facing role

**[02:49]** and they're in like a public facing role and then the rest of us are just really

**[02:51]** and then the rest of us are just really

**[02:51]** and then the rest of us are just really in for it. Um, because like if you sort

**[02:54]** in for it. Um, because like if you sort

**[02:54]** in for it. Um, because like if you sort of look at the last decade, a lot of web

**[02:57]** of look at the last decade, a lot of web

**[02:57]** of look at the last decade, a lot of web devs got these like lectures by not all

**[02:59]** devs got these like lectures by not all

**[02:59]** devs got these like lectures by not all Googlers but like certain Googlers about


### [03:00 - 04:00]

**[03:01]** Googlers but like certain Googlers about

**[03:01]** Googlers but like certain Googlers about like the right way to use the platform.

**[03:03]** like the right way to use the platform.

**[03:03]** like the right way to use the platform. Um, and it was just, you know, again,

**[03:05]** Um, and it was just, you know, again,

**[03:05]** Um, and it was just, you know, again, I'm going to go really deep. I don't

**[03:07]** I'm going to go really deep. I don't

**[03:07]** I'm going to go really deep. I don't know how deep into webdev like folks

**[03:09]** know how deep into webdev like folks

**[03:09]** know how deep into webdev like folks are, but like it was just sort of a this

**[03:11]** are, but like it was just sort of a this

**[03:11]** are, but like it was just sort of a this code anti-react code word and it was

**[03:13]** code anti-react code word and it was

**[03:13]** code anti-react code word and it was kind of like they were sort of pushing

**[03:15]** kind of like they were sort of pushing

**[03:15]** kind of like they were sort of pushing these technologies that were not very

**[03:16]** these technologies that were not very

**[03:16]** these technologies that were not very easy to use instead. Um I'm just kind of

**[03:19]** easy to use instead. Um I'm just kind of

**[03:19]** easy to use instead. Um I'm just kind of hoping like the the the model providers

**[03:21]** hoping like the the the model providers

**[03:21]** hoping like the the the model providers like kind of have this like elevated

**[03:23]** like kind of have this like elevated

**[03:23]** like kind of have this like elevated position in the ecosystem. So whatever

**[03:25]** position in the ecosystem. So whatever

**[03:25]** position in the ecosystem. So whatever they say carries a lot of weight um

**[03:27]** they say carries a lot of weight um

**[03:27]** they say carries a lot of weight um similar to like the the fang companies

**[03:29]** similar to like the the fang companies

**[03:29]** similar to like the the fang companies in in like you know webdev and and and

**[03:33]** in in like you know webdev and and and

**[03:33]** in in like you know webdev and and and in general. So like let's just here's

**[03:35]** in general. So like let's just here's

**[03:35]** in general. So like let's just here's here's the hoping for a good quality of

**[03:37]** here's the hoping for a good quality of

**[03:37]** here's the hoping for a good quality of a discourse this time around. Um here's

**[03:40]** a discourse this time around. Um here's

**[03:40]** a discourse this time around. Um here's a hot take number two and I'm gonna add

**[03:42]** a hot take number two and I'm gonna add

**[03:42]** a hot take number two and I'm gonna add lang chain here. Um we should consider

**[03:45]** lang chain here. Um we should consider

**[03:45]** lang chain here. Um we should consider like graph node and edge terminal APIs

**[03:48]** like graph node and edge terminal APIs

**[03:48]** like graph node and edge terminal APIs within frameworks harmful. Um and and

**[03:52]** within frameworks harmful. Um and and

**[03:52]** within frameworks harmful. Um and and like I say this as someone who used to

**[03:55]** like I say this as someone who used to

**[03:55]** like I say this as someone who used to be a co-founder of a React meta

**[03:57]** be a co-founder of a React meta

**[03:57]** be a co-founder of a React meta framework that famously used GraphQL as


### [04:00 - 05:00]

**[04:00]** framework that famously used GraphQL as

**[04:00]** framework that famously used GraphQL as a default way of fetching data.

**[04:05]** a default way of fetching data.

**[04:05]** a default way of fetching data. We wrote that we wrote our data fetching

**[04:07]** We wrote that we wrote our data fetching

**[04:07]** We wrote that we wrote our data fetching queries like this. Um it was really cool

**[04:09]** queries like this. Um it was really cool

**[04:09]** queries like this. Um it was really cool in 2017. Um we GraphQL is still cool,

**[04:13]** in 2017. Um we GraphQL is still cool,

**[04:14]** in 2017. Um we GraphQL is still cool, right? GraphQL is a great technology but

**[04:15]** right? GraphQL is a great technology but

**[04:15]** right? GraphQL is a great technology but we index on on this pattern and it

**[04:17]** we index on on this pattern and it

**[04:17]** we index on on this pattern and it became kind of the default way of

**[04:19]** became kind of the default way of

**[04:19]** became kind of the default way of fetching data in Gatsby. Um

**[04:23]** fetching data in Gatsby. Um

**[04:23]** fetching data in Gatsby. Um some of our users love this but many of

**[04:25]** some of our users love this but many of

**[04:25]** some of our users love this but many of them didn't. Many of them just wanted a

**[04:28]** them didn't. Many of them just wanted a

**[04:28]** them didn't. Many of them just wanted a React meta framework. Okay, why is he

**[04:29]** React meta framework. Okay, why is he

**[04:29]** React meta framework. Okay, why is he talking about like the last decade of

**[04:31]** talking about like the last decade of

**[04:31]** talking about like the last decade of web development? Well, you'll see why

**[04:33]** web development? Well, you'll see why

**[04:33]** web development? Well, you'll see why they ended up using other frameworks

**[04:34]** they ended up using other frameworks

**[04:34]** they ended up using other frameworks instead. Um, and when I see APIs that

**[04:38]** instead. Um, and when I see APIs that

**[04:38]** instead. Um, and when I see APIs that look something like this, it gives me

**[04:41]** look something like this, it gives me

**[04:41]** look something like this, it gives me flashbacks.

**[04:43]** flashbacks.

**[04:43]** flashbacks. I do not think you should need to learn

**[04:46]** I do not think you should need to learn

**[04:46]** I do not think you should need to learn graph theory to write workflows to build

**[04:50]** graph theory to write workflows to build

**[04:50]** graph theory to write workflows to build production applications. More

**[04:52]** production applications. More

**[04:52]** production applications. More problematically, you should also

**[04:54]** problematically, you should also

**[04:54]** problematically, you should also probably not need your like all of your

**[04:57]** probably not need your like all of your

**[04:57]** probably not need your like all of your team to to to gro graph theory. a more


### [05:00 - 06:00]

**[05:00]** team to to to gro graph theory. a more

**[05:00]** team to to to gro graph theory. a more grockable pattern like looks something

**[05:02]** grockable pattern like looks something

**[05:02]** grockable pattern like looks something like this. And I've used like I've used

**[05:04]** like this. And I've used like I've used

**[05:04]** like this. And I've used like I've used master workflows um here. Um but it is

**[05:08]** master workflows um here. Um but it is

**[05:08]** master workflows um here. Um but it is sort of like a fluent syntax. You can

**[05:09]** sort of like a fluent syntax. You can

**[05:10]** sort of like a fluent syntax. You can like clearly see the control flow. Um

**[05:12]** like clearly see the control flow. Um

**[05:12]** like clearly see the control flow. Um but I mean like this is like the ingest

**[05:14]** but I mean like this is like the ingest

**[05:14]** but I mean like this is like the ingest workflow syntax. Um you can you can kind

**[05:17]** workflow syntax. Um you can you can kind

**[05:17]** workflow syntax. Um you can you can kind of clearly see the the flow of of of the

**[05:20]** of clearly see the the flow of of of the

**[05:20]** of clearly see the the flow of of of the code. You can see what happens and then

**[05:22]** code. You can see what happens and then

**[05:22]** code. You can see what happens and then what happens after that and what happens

**[05:24]** what happens after that and what happens

**[05:24]** what happens after that and what happens after that. you can just see it by like

**[05:27]** after that. you can just see it by like

**[05:27]** after that. you can just see it by like when you sort of like step when you're

**[05:29]** when you sort of like step when you're

**[05:29]** when you sort of like step when you're reading the code your your eyes can go

**[05:30]** reading the code your your eyes can go

**[05:30]** reading the code your your eyes can go from the top to the bottom and okay I I

**[05:33]** from the top to the bottom and okay I I

**[05:33]** from the top to the bottom and okay I I see what's going on here great I get it

**[05:35]** see what's going on here great I get it

**[05:35]** see what's going on here great I get it right it's readable code it's it's it's

**[05:37]** right it's readable code it's it's it's

**[05:37]** right it's readable code it's it's it's like a readable way of doing things um I

**[05:39]** like a readable way of doing things um I

**[05:39]** like a readable way of doing things um I think when if we have to use nodes and

**[05:42]** think when if we have to use nodes and

**[05:42]** think when if we have to use nodes and edges and connect things we lose that

**[05:45]** edges and connect things we lose that

**[05:45]** edges and connect things we lose that readability of code which is really

**[05:47]** readability of code which is really

**[05:47]** readability of code which is really important when we're building we all

**[05:48]** important when we're building we all

**[05:48]** important when we're building we all build software in teams right generally

**[05:50]** build software in teams right generally

**[05:50]** build software in teams right generally um uh uh so to is I mentioned this

**[05:56]** um uh uh so to is I mentioned this

**[05:56]** um uh uh so to is I mentioned this earlier right like you and your

**[05:57]** earlier right like you and your

**[05:58]** earlier right like you and your colleagues should be able to use a

**[05:59]** colleagues should be able to use a

**[05:59]** colleagues should be able to use a workflow framework or whatever without


### [06:00 - 07:00]

**[06:02]** workflow framework or whatever without

**[06:02]** workflow framework or whatever without learning graph theory um

**[06:05]** learning graph theory um

**[06:05]** learning graph theory um again like I said it's a reverse reverse

**[06:07]** again like I said it's a reverse reverse

**[06:07]** again like I said it's a reverse reverse mullet like party in the front hot tick

**[06:10]** mullet like party in the front hot tick

**[06:10]** mullet like party in the front hot tick in the front like business in the back

**[06:12]** in the front like business in the back

**[06:12]** in the front like business in the back um okay so so like now that we've kind

**[06:14]** um okay so so like now that we've kind

**[06:14]** um okay so so like now that we've kind of like talked about like we we've sort

**[06:16]** of like talked about like we we've sort

**[06:16]** of like talked about like we we've sort of like opined on the discourse of the

**[06:18]** of like opined on the discourse of the

**[06:18]** of like opined on the discourse of the day um let's get down to business okay

**[06:21]** day um let's get down to business okay

**[06:21]** day um let's get down to business okay um design patterns for agents and

**[06:24]** um design patterns for agents and

**[06:24]** um design patterns for agents and workflows and when I say design patterns

**[06:26]** workflows and when I say design patterns

**[06:26]** workflows and when I say design patterns like this phrase has kind of a storied

**[06:28]** like this phrase has kind of a storied

**[06:28]** like this phrase has kind of a storied history. So this is a book which came

**[06:29]** history. So this is a book which came

**[06:29]** history. So this is a book which came out I think like late '7s by this guy

**[06:31]** out I think like late '7s by this guy

**[06:31]** out I think like late '7s by this guy named Christopher Alexander. Um it was

**[06:34]** named Christopher Alexander. Um it was

**[06:34]** named Christopher Alexander. Um it was very famous. It spawned a bunch of like

**[06:36]** very famous. It spawned a bunch of like

**[06:36]** very famous. It spawned a bunch of like not he so okay Christopher Alexander was

**[06:38]** not he so okay Christopher Alexander was

**[06:38]** not he so okay Christopher Alexander was a professor at Berkeley. Um he was a

**[06:41]** a professor at Berkeley. Um he was a

**[06:41]** a professor at Berkeley. Um he was a architect. He sort of um cataloged in

**[06:45]** architect. He sort of um cataloged in

**[06:45]** architect. He sort of um cataloged in both uh sort of uh like urban planning

**[06:49]** both uh sort of uh like urban planning

**[06:49]** both uh sort of uh like urban planning as well as like internal sort of like

**[06:51]** as well as like internal sort of like

**[06:51]** as well as like internal sort of like inbuilding architecture. like these are

**[06:53]** inbuilding architecture. like these are

**[06:53]** inbuilding architecture. like these are a couple hundred of the patterns of what

**[06:55]** a couple hundred of the patterns of what

**[06:55]** a couple hundred of the patterns of what we see are the right ways of building.

**[06:58]** we see are the right ways of building.

**[06:58]** we see are the right ways of building. Um and um just wrote them all up in a


### [07:00 - 08:00]

**[07:01]** Um and um just wrote them all up in a

**[07:01]** Um and um just wrote them all up in a book. Um and so um oddly architects were

**[07:04]** book. Um and so um oddly architects were

**[07:04]** book. Um and so um oddly architects were not very fond of this but like software

**[07:06]** not very fond of this but like software

**[07:06]** not very fond of this but like software engineers loved it and sort of it became

**[07:08]** engineers loved it and sort of it became

**[07:08]** engineers loved it and sort of it became all the rage in like the this predates

**[07:10]** all the rage in like the this predates

**[07:10]** all the rage in like the this predates me but like the late 80s early 90s

**[07:12]** me but like the late 80s early 90s

**[07:12]** me but like the late 80s early 90s sometime around then. Um uh and so so I

**[07:16]** sometime around then. Um uh and so so I

**[07:16]** sometime around then. Um uh and so so I think there's like I think what we do

**[07:18]** think there's like I think what we do

**[07:18]** think there's like I think what we do not yet have um we have sort of like

**[07:21]** not yet have um we have sort of like

**[07:21]** not yet have um we have sort of like steps towards this but what we do not

**[07:22]** steps towards this but what we do not

**[07:22]** steps towards this but what we do not yet have is a commonly accepted verbiage

**[07:26]** yet have is a commonly accepted verbiage

**[07:26]** yet have is a commonly accepted verbiage and and like language and glossery of of

**[07:29]** and and like language and glossery of of

**[07:29]** and and like language and glossery of of what are agentic patterns right um what

**[07:32]** what are agentic patterns right um what

**[07:32]** what are agentic patterns right um what are agentic workflow patterns um and so

**[07:36]** are agentic workflow patterns um and so

**[07:36]** are agentic workflow patterns um and so um okay let's just start with like what

**[07:38]** um okay let's just start with like what

**[07:38]** um okay let's just start with like what are agents and workflows um maybe I'm

**[07:40]** are agents and workflows um maybe I'm

**[07:40]** are agents and workflows um maybe I'm not going to spend a lot of time on the

**[07:42]** not going to spend a lot of time on the

**[07:42]** not going to spend a lot of time on the slide because I think previous speaker

**[07:44]** slide because I think previous speaker

**[07:44]** slide because I think previous speaker talked about this. I was honestly

**[07:46]** talked about this. I was honestly

**[07:46]** talked about this. I was honestly because people have covered this ground.

**[07:47]** because people have covered this ground.

**[07:47]** because people have covered this ground. These guys did a a workshop yesterday

**[07:49]** These guys did a a workshop yesterday

**[07:49]** These guys did a a workshop yesterday and they did a great job. So, I was just

**[07:51]** and they did a great job. So, I was just

**[07:51]** and they did a great job. So, I was just like took their slides and put them in

**[07:52]** like took their slides and put them in

**[07:52]** like took their slides and put them in put them in here. Props to Nick and Zach

**[07:54]** put them in here. Props to Nick and Zach

**[07:54]** put them in here. Props to Nick and Zach if they're in the room somewhere. Uh but

**[07:56]** if they're in the room somewhere. Uh but

**[07:56]** if they're in the room somewhere. Uh but uh they're um they're they did a

**[07:59]** uh they're um they're they did a

**[07:59]** uh they're um they're they did a workshop on Monster X yesterday, which


### [08:00 - 09:00]

**[08:00]** workshop on Monster X yesterday, which

**[08:00]** workshop on Monster X yesterday, which is amazing. Um okay. Um so, but like

**[08:03]** is amazing. Um okay. Um so, but like

**[08:03]** is amazing. Um okay. Um so, but like okay, like let's just like how would we

**[08:06]** okay, like let's just like how would we

**[08:06]** okay, like let's just like how would we explain it to a friend? Okay. I I think

**[08:09]** explain it to a friend? Okay. I I think

**[08:09]** explain it to a friend? Okay. I I think about agents like a turn-based game,

**[08:10]** about agents like a turn-based game,

**[08:10]** about agents like a turn-based game, right? Like I take a turn, then the

**[08:12]** right? Like I take a turn, then the

**[08:12]** right? Like I take a turn, then the agent takes a turn, then I take a turn,

**[08:15]** agent takes a turn, then I take a turn,

**[08:15]** agent takes a turn, then I take a turn, then the agent takes a turn, and then

**[08:17]** then the agent takes a turn, and then

**[08:17]** then the agent takes a turn, and then the agent takes another turn, maybe

**[08:18]** the agent takes another turn, maybe

**[08:18]** the agent takes another turn, maybe makes like a tool call or something,

**[08:19]** makes like a tool call or something,

**[08:19]** makes like a tool call or something, right? It's like back and forth. Um, and

**[08:22]** right? It's like back and forth. Um, and

**[08:22]** right? It's like back and forth. Um, and then I think about like workflows are

**[08:23]** then I think about like workflows are

**[08:23]** then I think about like workflows are like this rules engine for your uh for

**[08:26]** like this rules engine for your uh for

**[08:26]** like this rules engine for your uh for your tech tree, right? Okay, we got to I

**[08:28]** your tech tree, right? Okay, we got to I

**[08:28]** your tech tree, right? Okay, we got to I I played civil a lot when I was a kid.

**[08:30]** I played civil a lot when I was a kid.

**[08:30]** I played civil a lot when I was a kid. Um, I I I I you got to discover bronze

**[08:32]** Um, I I I I you got to discover bronze

**[08:32]** Um, I I I I you got to discover bronze working before you can research iron

**[08:34]** working before you can research iron

**[08:34]** working before you can research iron working, right? You've got to get my

**[08:36]** working, right? You've got to get my

**[08:36]** working, right? You've got to get my before you can uh research gunpowder,

**[08:38]** before you can uh research gunpowder,

**[08:38]** before you can uh research gunpowder, right? like there's there's some sort of

**[08:40]** right? like there's there's some sort of

**[08:40]** right? like there's there's some sort of dependency chain here. Um, and it's

**[08:42]** dependency chain here. Um, and it's

**[08:42]** dependency chain here. Um, and it's important to kind of track the

**[08:43]** important to kind of track the

**[08:43]** important to kind of track the dependencies because you can't do step B

**[08:45]** dependencies because you can't do step B

**[08:45]** dependencies because you can't do step B until you do step A. And a lot of

**[08:47]** until you do step A. And a lot of

**[08:47]** until you do step A. And a lot of workflows are these like data pipelines.

**[08:49]** workflows are these like data pipelines.

**[08:49]** workflows are these like data pipelines. Step A, step B, step C, step D, step E,

**[08:51]** Step A, step B, step C, step D, step E,

**[08:51]** Step A, step B, step C, step D, step E, execute them all in order, go right. Um,

**[08:56]** execute them all in order, go right. Um,

**[08:56]** execute them all in order, go right. Um, you know, um, conversations have

**[08:58]** you know, um, conversations have

**[08:58]** you know, um, conversations have threads, you can have memory, like these


### [09:00 - 10:00]

**[09:00]** threads, you can have memory, like these

**[09:00]** threads, you can have memory, like these are all the emergent properties that

**[09:01]** are all the emergent properties that

**[09:01]** are all the emergent properties that happen when you think about uh when you

**[09:04]** happen when you think about uh when you

**[09:04]** happen when you think about uh when you think about like lots and lots and lots

**[09:06]** think about like lots and lots and lots

**[09:06]** think about like lots and lots and lots of messages. Um similarly if you think

**[09:08]** of messages. Um similarly if you think

**[09:08]** of messages. Um similarly if you think about these sort of like um dependencies

**[09:11]** about these sort of like um dependencies

**[09:12]** about these sort of like um dependencies you can think about branching and

**[09:13]** you can think about branching and

**[09:13]** you can think about branching and parallelism and conditions and loops and

**[09:16]** parallelism and conditions and loops and

**[09:16]** parallelism and conditions and loops and suspending and resuming and replaying

**[09:18]** suspending and resuming and replaying

**[09:18]** suspending and resuming and replaying and all this fun stuff like those are

**[09:19]** and all this fun stuff like those are

**[09:20]** and all this fun stuff like those are sort of the emergent properties of of

**[09:21]** sort of the emergent properties of of

**[09:21]** sort of the emergent properties of of workflows. Uh, and I mean just kind of

**[09:25]** workflows. Uh, and I mean just kind of

**[09:25]** workflows. Uh, and I mean just kind of recapping like workflows have been

**[09:27]** recapping like workflows have been

**[09:27]** recapping like workflows have been around for a while. Obviously, they're

**[09:29]** around for a while. Obviously, they're

**[09:29]** around for a while. Obviously, they're becoming more popular now for a variety

**[09:31]** becoming more popular now for a variety

**[09:31]** becoming more popular now for a variety of reasons, but one of them just, and I

**[09:33]** of reasons, but one of them just, and I

**[09:33]** of reasons, but one of them just, and I want to bring this back here because

**[09:34]** want to bring this back here because

**[09:34]** want to bring this back here because it's important, right? Like you can

**[09:36]** it's important, right? Like you can

**[09:36]** it's important, right? Like you can always just write um, you know, code

**[09:38]** always just write um, you know, code

**[09:38]** always just write um, you know, code that says do A and then do B and do C

**[09:40]** that says do A and then do B and do C

**[09:40]** that says do A and then do B and do C and do D. Um, but the reason why they

**[09:42]** and do D. Um, but the reason why they

**[09:42]** and do D. Um, but the reason why they like they're just more popular in AI

**[09:44]** like they're just more popular in AI

**[09:44]** like they're just more popular in AI engineering than sort of like normal

**[09:46]** engineering than sort of like normal

**[09:46]** engineering than sort of like normal engineering is because like

**[09:47]** engineering is because like

**[09:47]** engineering is because like non-determinism is is sort of core core

**[09:51]** non-determinism is is sort of core core

**[09:51]** non-determinism is is sort of core core to what we're doing here and and we and

**[09:53]** to what we're doing here and and we and

**[09:53]** to what we're doing here and and we and being able to kind of trace it and

**[09:54]** being able to kind of trace it and

**[09:54]** being able to kind of trace it and figure out what happened is like if it's

**[09:57]** figure out what happened is like if it's

**[09:57]** figure out what happened is like if it's important in in in software engineering,

**[09:59]** important in in in software engineering,

**[09:59]** important in in in software engineering, it's 10x as important as in in AI


### [10:00 - 11:00]

**[10:01]** it's 10x as important as in in AI

**[10:01]** it's 10x as important as in in AI engineering. Um, so um let's see. Look,

**[10:05]** engineering. Um, so um let's see. Look,

**[10:05]** engineering. Um, so um let's see. Look, at the end of the day, it's just a

**[10:06]** at the end of the day, it's just a

**[10:06]** at the end of the day, it's just a trade-off, right? Um, you can have power

**[10:08]** trade-off, right? Um, you can have power

**[10:08]** trade-off, right? Um, you can have power or you can have control. You can decide

**[10:10]** or you can have control. You can decide

**[10:10]** or you can have control. You can decide which parts you want power on, which

**[10:12]** which parts you want power on, which

**[10:12]** which parts you want power on, which parts you want control on. You can start

**[10:14]** parts you want control on. You can start

**[10:14]** parts you want control on. You can start with power and then anything that like

**[10:15]** with power and then anything that like

**[10:15]** with power and then anything that like goes off the rails, you can add control.

**[10:17]** goes off the rails, you can add control.

**[10:17]** goes off the rails, you can add control. Um, at the end of the day, like many

**[10:18]** Um, at the end of the day, like many

**[10:18]** Um, at the end of the day, like many things we do, it's just a trade-off. Um

**[10:22]** things we do, it's just a trade-off. Um

**[10:22]** things we do, it's just a trade-off. Um uh this slide was uh was not able to

**[10:25]** uh this slide was uh was not able to

**[10:25]** uh this slide was uh was not able to drop in but uh the photo I wanted to

**[10:27]** drop in but uh the photo I wanted to

**[10:27]** drop in but uh the photo I wanted to drop in but um uh we you know we we've

**[10:30]** drop in but um uh we you know we we've

**[10:30]** drop in but um uh we you know we we've done a lot of whiteboarding sessions

**[10:32]** done a lot of whiteboarding sessions

**[10:32]** done a lot of whiteboarding sessions with like hey I'm starting to build an

**[10:33]** with like hey I'm starting to build an

**[10:33]** with like hey I'm starting to build an agent and uh I I want to think trying to

**[10:37]** agent and uh I I want to think trying to

**[10:37]** agent and uh I I want to think trying to figure out how to think about this or my

**[10:38]** figure out how to think about this or my

**[10:38]** figure out how to think about this or my agent is I'm feeding in this giant PDF

**[10:41]** agent is I'm feeding in this giant PDF

**[10:41]** agent is I'm feeding in this giant PDF of medical documentation and I'm not I'm

**[10:43]** of medical documentation and I'm not I'm

**[10:43]** of medical documentation and I'm not I'm trying to diagnose 12 symptoms and I'm

**[10:45]** trying to diagnose 12 symptoms and I'm

**[10:45]** trying to diagnose 12 symptoms and I'm they're not it's not accurately pulling

**[10:48]** they're not it's not accurately pulling

**[10:48]** they're not it's not accurately pulling out the right information. Um, okay.

**[10:51]** out the right information. Um, okay.

**[10:51]** out the right information. Um, okay. Have you considered breaking that one LM

**[10:53]** Have you considered breaking that one LM

**[10:53]** Have you considered breaking that one LM call into 12 LM calls? Right? A lot of

**[10:55]** call into 12 LM calls? Right? A lot of

**[10:55]** call into 12 LM calls? Right? A lot of what you do in these kinds of sessions

**[10:57]** what you do in these kinds of sessions

**[10:57]** what you do in these kinds of sessions is you sort of think about you kind of


### [11:00 - 12:00]

**[11:00]** is you sort of think about you kind of

**[11:00]** is you sort of think about you kind of ask, hey, what part of your application

**[11:01]** ask, hey, what part of your application

**[11:01]** ask, hey, what part of your application is performing not very well in in terms

**[11:06]** is performing not very well in in terms

**[11:06]** is performing not very well in in terms of reliability and then like how could

**[11:07]** of reliability and then like how could

**[11:08]** of reliability and then like how could you add some structure to the process

**[11:10]** you add some structure to the process

**[11:10]** you add some structure to the process here so you could you you can get

**[11:12]** here so you could you you can get

**[11:12]** here so you could you you can get additional reliability. Um, and I

**[11:15]** additional reliability. Um, and I

**[11:15]** additional reliability. Um, and I encourage that sort of like practice. We

**[11:19]** encourage that sort of like practice. We

**[11:19]** encourage that sort of like practice. We could have encouraged that practice like

**[11:20]** could have encouraged that practice like

**[11:20]** could have encouraged that practice like obviously we're happy to do that with

**[11:21]** obviously we're happy to do that with

**[11:21]** obviously we're happy to do that with whoever but like also just like do it

**[11:23]** whoever but like also just like do it

**[11:23]** whoever but like also just like do it with each other and like just try

**[11:24]** with each other and like just try

**[11:24]** with each other and like just try explaining your architecture to your

**[11:25]** explaining your architecture to your

**[11:25]** explaining your architecture to your friend or your colleague right and then

**[11:27]** friend or your colleague right and then

**[11:27]** friend or your colleague right and then like diagram it out on a board because

**[11:30]** like diagram it out on a board because

**[11:30]** like diagram it out on a board because you can match when you're doing these

**[11:32]** you can match when you're doing these

**[11:32]** you can match when you're doing these things like magically like you realize

**[11:35]** things like magically like you realize

**[11:35]** things like magically like you realize that uh actually there's a better way of

**[11:38]** that uh actually there's a better way of

**[11:38]** that uh actually there's a better way of doing a certain thing and maybe a more

**[11:40]** doing a certain thing and maybe a more

**[11:40]** doing a certain thing and maybe a more creative way of using the primitives

**[11:42]** creative way of using the primitives

**[11:42]** creative way of using the primitives together. Um coming to that right so

**[11:45]** together. Um coming to that right so

**[11:46]** together. Um coming to that right so here's just some thoughts right agents

**[11:49]** here's just some thoughts right agents

**[11:49]** here's just some thoughts right agents and workflow composition so agents have

**[11:51]** and workflow composition so agents have

**[11:51]** and workflow composition so agents have tools and you know they they can call

**[11:54]** tools and you know they they can call

**[11:54]** tools and you know they they can call tools you know workflows have steps an

**[11:56]** tools you know workflows have steps an

**[11:56]** tools you know workflows have steps an agent can be a step a workflow can be a

**[11:58]** agent can be a step a workflow can be a

**[11:58]** agent can be a step a workflow can be a tool an agent can be a tool a workflow


### [12:00 - 13:00]

**[12:01]** tool an agent can be a tool a workflow

**[12:01]** tool an agent can be a tool a workflow can be a step

**[12:03]** can be a step

**[12:03]** can be a step and like most primitives the magic

**[12:05]** and like most primitives the magic

**[12:05]** and like most primitives the magic happens when you combine these things

**[12:07]** happens when you combine these things

**[12:07]** happens when you combine these things together um

**[12:10]** together um

**[12:10]** together um the agent supervisor model you have an

**[12:12]** the agent supervisor model you have an

**[12:12]** the agent supervisor model you have an agent that is calling other agents as

**[12:15]** agent that is calling other agents as

**[12:15]** agent that is calling other agents as tools, right? So, um let's see, we have

**[12:17]** tools, right? So, um let's see, we have

**[12:18]** tools, right? So, um let's see, we have this one was a research agent and a

**[12:19]** this one was a research agent and a

**[12:19]** this one was a research agent and a summary agent and then like an

**[12:20]** summary agent and then like an

**[12:20]** summary agent and then like an orchestrator agent. These are like these

**[12:22]** orchestrator agent. These are like these

**[12:22]** orchestrator agent. These are like these these are all like MRA um sort of like

**[12:25]** these are all like MRA um sort of like

**[12:25]** these are all like MRA um sort of like MRA code is just more of like an example

**[12:27]** MRA code is just more of like an example

**[12:27]** MRA code is just more of like an example of like you know but but I think like

**[12:29]** of like you know but but I think like

**[12:29]** of like you know but but I think like it's illustrative not the particular

**[12:31]** it's illustrative not the particular

**[12:31]** it's illustrative not the particular lines of code and what they are but like

**[12:33]** lines of code and what they are but like

**[12:33]** lines of code and what they are but like these examples are sort of simple enough

**[12:35]** these examples are sort of simple enough

**[12:35]** these examples are sort of simple enough to fit in the you know slightly smaller

**[12:38]** to fit in the you know slightly smaller

**[12:38]** to fit in the you know slightly smaller version of the right panel of my slide

**[12:39]** version of the right panel of my slide

**[12:40]** version of the right panel of my slide right and that then that's sort of the

**[12:41]** right and that then that's sort of the

**[12:41]** right and that then that's sort of the interesting thing we can use these terms

**[12:43]** interesting thing we can use these terms

**[12:43]** interesting thing we can use these terms and the implementation is not too long

**[12:47]** and the implementation is not too long

**[12:47]** and the implementation is not too long it's grockable in a slide um and and so

**[12:51]** it's grockable in a slide um and and so

**[12:51]** it's grockable in a slide um and and so again like that's kind of what gives us

**[12:53]** again like that's kind of what gives us

**[12:53]** again like that's kind of what gives us power is that like the primitives are

**[12:54]** power is that like the primitives are

**[12:54]** power is that like the primitives are simple but the combinations are also

**[12:56]** simple but the combinations are also

**[12:56]** simple but the combinations are also like once we get a hang around once we

**[12:59]** like once we get a hang around once we

**[12:59]** like once we get a hang around once we get the hang of them we can you know run


### [13:00 - 14:00]

**[13:01]** get the hang of them we can you know run

**[13:01]** get the hang of them we can you know run pretty fast you know you could have

**[13:03]** pretty fast you know you could have

**[13:03]** pretty fast you know you could have workflows as tools um

**[13:07]** workflows as tools um

**[13:07]** workflows as tools um so um I think it you know it's like hey

**[13:09]** so um I think it you know it's like hey

**[13:09]** so um I think it you know it's like hey like you want to plan location you want

**[13:11]** like you want to plan location you want

**[13:11]** like you want to plan location you want to like check the weather then you want

**[13:12]** to like check the weather then you want

**[13:12]** to like check the weather then you want to plan a trip maybe these are like more

**[13:14]** to plan a trip maybe these are like more

**[13:14]** to plan a trip maybe these are like more more complex workflows pass that to an

**[13:16]** more complex workflows pass that to an

**[13:16]** more complex workflows pass that to an agent let it sort of like iterate and

**[13:19]** agent let it sort of like iterate and

**[13:19]** agent let it sort of like iterate and decide um workflows is doing agent

**[13:21]** decide um workflows is doing agent

**[13:21]** decide um workflows is doing agent handoffs. Uh I'm looking at time here.

**[13:23]** handoffs. Uh I'm looking at time here.

**[13:23]** handoffs. Uh I'm looking at time here. Dynamic tool injection. This is

**[13:25]** Dynamic tool injection. This is

**[13:25]** Dynamic tool injection. This is interesting too. I think like you know

**[13:27]** interesting too. I think like you know

**[13:27]** interesting too. I think like you know agents um can start failing if you give

**[13:30]** agents um can start failing if you give

**[13:30]** agents um can start failing if you give them let's say double-digit numbers of

**[13:32]** them let's say double-digit numbers of

**[13:32]** them let's say double-digit numbers of tools. And you may want to be thoughtful

**[13:35]** tools. And you may want to be thoughtful

**[13:35]** tools. And you may want to be thoughtful about which tools you're handing in

**[13:37]** about which tools you're handing in

**[13:37]** about which tools you're handing in handing to a particular agent at a

**[13:39]** handing to a particular agent at a

**[13:39]** handing to a particular agent at a particular time when it's performing a

**[13:40]** particular time when it's performing a

**[13:40]** particular time when it's performing a particular task. You can also um you

**[13:43]** particular task. You can also um you

**[13:43]** particular task. You can also um you know nested workflows. Again, workflow

**[13:44]** know nested workflows. Again, workflow

**[13:44]** know nested workflows. Again, workflow is a step, but again, like the real and

**[13:47]** is a step, but again, like the real and

**[13:47]** is a step, but again, like the real and and just I'm going to re-emphasize this,

**[13:48]** and just I'm going to re-emphasize this,

**[13:48]** and just I'm going to re-emphasize this, the real alpha comes from sort of like

**[13:50]** the real alpha comes from sort of like

**[13:50]** the real alpha comes from sort of like using these patterns together in the

**[13:53]** using these patterns together in the

**[13:53]** using these patterns together in the right sort of way. Um, reality has a

**[13:56]** right sort of way. Um, reality has a

**[13:56]** right sort of way. Um, reality has a surprising amount of detail and so do

**[13:58]** surprising amount of detail and so do

**[13:58]** surprising amount of detail and so do agentic workflows that um sort of like


### [14:00 - 15:00]

**[14:01]** agentic workflows that um sort of like

**[14:01]** agentic workflows that um sort of like by the time they enter production. Um,

**[14:05]** by the time they enter production. Um,

**[14:05]** by the time they enter production. Um, I think I I also have a couple minutes

**[14:07]** I think I I also have a couple minutes

**[14:07]** I think I I also have a couple minutes for questions. So, uh,

**[14:10]** for questions. So, uh,

**[14:10]** for questions. So, uh, so do you think

**[14:22]** Uh so the question yeah the question is

**[14:22]** Uh so the question yeah the question is uh would it be better to combine the

**[14:24]** uh would it be better to combine the

**[14:24]** uh would it be better to combine the deep research agent? I have a workflow

**[14:27]** deep research agent? I have a workflow

**[14:27]** deep research agent? I have a workflow that I know for a fact.

**[14:40]** So the the question is your agent works

**[14:40]** So the the question is your agent works great with 20 tools. I I would say like

**[14:42]** great with 20 tools. I I would say like

**[14:42]** great with 20 tools. I I would say like we are a community of practice more than

**[14:44]** we are a community of practice more than

**[14:44]** we are a community of practice more than we are a community of theory. If your

**[14:46]** we are a community of theory. If your

**[14:46]** we are a community of theory. If your agent is working according to what you

**[14:48]** agent is working according to what you

**[14:48]** agent is working according to what you would need like like do it if it's not

**[14:51]** would need like like do it if it's not

**[14:51]** would need like like do it if it's not theoretically correct that probably

**[14:53]** theoretically correct that probably

**[14:53]** theoretically correct that probably means the theory is wrong not not the uh

**[14:55]** means the theory is wrong not not the uh

**[14:55]** means the theory is wrong not not the uh not the practice. This is a young field

**[14:58]** not the practice. This is a young field

**[14:58]** not the practice. This is a young field and the the the the practice is evolving


### [15:00 - 16:00]

**[15:01]** and the the the the practice is evolving

**[15:01]** and the the the the practice is evolving faster than the theory. Right? I think

**[15:02]** faster than the theory. Right? I think

**[15:02]** faster than the theory. Right? I think that's just my general um comment. Uh

**[15:05]** that's just my general um comment. Uh

**[15:05]** that's just my general um comment. Uh one more question.

**[15:11]** Where can we find you after the talk?

**[15:12]** Where can we find you after the talk? Uh, you can find me around the

**[15:13]** Uh, you can find me around the

**[15:13]** Uh, you can find me around the conference. You can at I'm calcam.

**[15:16]** conference. You can at I'm calcam.

**[15:16]** conference. You can at I'm calcam. That's CALC like calculator and SAM like

**[15:18]** That's CALC like calculator and SAM like

**[15:18]** That's CALC like calculator and SAM like my name, which is my handle when I was

**[15:20]** my name, which is my handle when I was

**[15:20]** my name, which is my handle when I was 12 because I was Yeah. Yeah. Anyway, uh,

**[15:25]** 12 because I was Yeah. Yeah. Anyway, uh,

**[15:25]** 12 because I was Yeah. Yeah. Anyway, uh, thanks everyone for coming. Really

**[15:26]** thanks everyone for coming. Really

**[15:26]** thanks everyone for coming. Really appreciate it. Please grab a copy of the

**[15:28]** appreciate it. Please grab a copy of the

**[15:28]** appreciate it. Please grab a copy of the book around the comments.

**[15:30]** book around the comments.

**[15:30]** book around the comments. [Music]


