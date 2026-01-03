# How we hacked YC Spring 2025 batch’s AI agents — Rene Brandel, Casco

**Video URL:** https://www.youtube.com/watch?v=kv-QAuKWllQ

---

## Full Transcript

### [00:00 - 01:00]

**[00:17]** So, yeah. Who's ready to hack some

**[00:17]** So, yeah. Who's ready to hack some agents? Yeah. Oh, wow. All right. So,

**[00:19]** agents? Yeah. Oh, wow. All right. So,

**[00:20]** agents? Yeah. Oh, wow. All right. So, let me first introduce myself a little

**[00:21]** let me first introduce myself a little

**[00:21]** let me first introduce myself a little bit. I'm Renee. I'm the CEO of Casco.

**[00:23]** bit. I'm Renee. I'm the CEO of Casco.

**[00:23]** bit. I'm Renee. I'm the CEO of Casco. We're a YC company, and we specialize in

**[00:26]** We're a YC company, and we specialize in

**[00:26]** We're a YC company, and we specialize in red teaming AI agents and apps. And so

**[00:29]** red teaming AI agents and apps. And so

**[00:29]** red teaming AI agents and apps. And so we spent uh I spent my previous time at

**[00:31]** we spent uh I spent my previous time at

**[00:31]** we spent uh I spent my previous time at AWS working on AI agents, but I've

**[00:34]** AWS working on AI agents, but I've

**[00:34]** AWS working on AI agents, but I've always really loved working on AI. In

**[00:37]** always really loved working on AI. In

**[00:37]** always really loved working on AI. In fact, there's a video of me 10 years ago

**[00:39]** fact, there's a video of me 10 years ago

**[00:39]** fact, there's a video of me 10 years ago building voice to code and I won

**[00:42]** building voice to code and I won

**[00:42]** building voice to code and I won Europe's largest hackathon by doing

**[00:43]** Europe's largest hackathon by doing

**[00:43]** Europe's largest hackathon by doing that. And so I would talk to it, say,

**[00:45]** that. And so I would talk to it, say,

**[00:45]** that. And so I would talk to it, say, build me a blog post and it would

**[00:47]** build me a blog post and it would

**[00:47]** build me a blog post and it would generate the sites. And it was actually

**[00:49]** generate the sites. And it was actually

**[00:49]** generate the sites. And it was actually it was kind of fun. Like it did uh

**[00:51]** it was kind of fun. Like it did uh

**[00:51]** it was kind of fun. Like it did uh things like um yeah, load in pictures

**[00:53]** things like um yeah, load in pictures

**[00:53]** things like um yeah, load in pictures from San Francisco. And you can see how

**[00:55]** from San Francisco. And you can see how

**[00:55]** from San Francisco. And you can see how horribly slow the APIs were back then.

**[00:58]** horribly slow the APIs were back then.

**[00:58]** horribly slow the APIs were back then. And I'm going to about to give you a

**[00:59]** And I'm going to about to give you a

**[00:59]** And I'm going to about to give you a nightmare by showing you the


### [01:00 - 02:00]

**[01:00]** nightmare by showing you the

**[01:00]** nightmare by showing you the architecture diagram of that thing. Um,

**[01:02]** architecture diagram of that thing. Um,

**[01:02]** architecture diagram of that thing. Um, but yeah, it kind of did the job. And

**[01:04]** but yeah, it kind of did the job. And

**[01:04]** but yeah, it kind of did the job. And this was like 10 years ago. Obviously,

**[01:06]** this was like 10 years ago. Obviously,

**[01:06]** this was like 10 years ago. Obviously, back then was no generative AI and these

**[01:08]** back then was no generative AI and these

**[01:08]** back then was no generative AI and these things were extremely difficult to do.

**[01:10]** things were extremely difficult to do.

**[01:10]** things were extremely difficult to do. Um, but it is it really gave me a

**[01:13]** Um, but it is it really gave me a

**[01:13]** Um, but it is it really gave me a glimpse of what the future could look

**[01:14]** glimpse of what the future could look

**[01:14]** glimpse of what the future could look like even back then as technology gets

**[01:16]** like even back then as technology gets

**[01:16]** like even back then as technology gets better, right? So, obviously many things

**[01:19]** better, right? So, obviously many things

**[01:19]** better, right? So, obviously many things have changed. Two months ago, I quit AWS

**[01:21]** have changed. Two months ago, I quit AWS

**[01:21]** have changed. Two months ago, I quit AWS and worked out of uh the garage with my

**[01:23]** and worked out of uh the garage with my

**[01:23]** and worked out of uh the garage with my co-founder and uh we got into Y

**[01:26]** co-founder and uh we got into Y

**[01:26]** co-founder and uh we got into Y Combinator. So, yay. That's awesome. And

**[01:29]** Combinator. So, yay. That's awesome. And

**[01:29]** Combinator. So, yay. That's awesome. And so from there, we also looked into how

**[01:31]** so from there, we also looked into how

**[01:31]** so from there, we also looked into how else have things evolved. Well, this was

**[01:33]** else have things evolved. Well, this was

**[01:33]** else have things evolved. Well, this was my um architecture diagram from back

**[01:36]** my um architecture diagram from back

**[01:36]** my um architecture diagram from back then. Could see there was three

**[01:37]** then. Could see there was three

**[01:37]** then. Could see there was three different cloud providers including IBM

**[01:39]** different cloud providers including IBM

**[01:39]** different cloud providers including IBM Watson, which was like forefront at the

**[01:41]** Watson, which was like forefront at the

**[01:41]** Watson, which was like forefront at the time. That's true. And uh before it was

**[01:45]** time. That's true. And uh before it was

**[01:45]** time. That's true. And uh before it was like uh Microsoft Lewis, which was like

**[01:47]** like uh Microsoft Lewis, which was like

**[01:47]** like uh Microsoft Lewis, which was like some natural language understanding

**[01:48]** some natural language understanding

**[01:48]** some natural language understanding things. And you can see it was just a

**[01:50]** things. And you can see it was just a

**[01:50]** things. And you can see it was just a lot of like piecing things together and

**[01:51]** lot of like piecing things together and

**[01:51]** lot of like piecing things together and that was already kind of difficult to

**[01:53]** that was already kind of difficult to

**[01:53]** that was already kind of difficult to do. But nowadays we see the stacks

**[01:55]** do. But nowadays we see the stacks

**[01:55]** do. But nowadays we see the stacks normalized significantly more. Right? I

**[01:58]** normalized significantly more. Right? I

**[01:58]** normalized significantly more. Right? I think this is probably what the average


### [02:00 - 03:00]

**[02:01]** think this is probably what the average

**[02:01]** think this is probably what the average agent stack looks like these days. Got

**[02:03]** agent stack looks like these days. Got

**[02:03]** agent stack looks like these days. Got some server front end. You talk to an

**[02:05]** some server front end. You talk to an

**[02:05]** some server front end. You talk to an API server that talks to an LM connects

**[02:07]** API server that talks to an LM connects

**[02:07]** API server that talks to an LM connects up with tools and then you have a bunch

**[02:09]** up with tools and then you have a bunch

**[02:10]** up with tools and then you have a bunch of data sources associated to it. So

**[02:12]** of data sources associated to it. So

**[02:12]** of data sources associated to it. So this kind of normalization of agent

**[02:14]** this kind of normalization of agent

**[02:14]** this kind of normalization of agent stack is actually really good. It like

**[02:16]** stack is actually really good. It like

**[02:16]** stack is actually really good. It like makes many things easier. Definitely

**[02:17]** makes many things easier. Definitely

**[02:17]** makes many things easier. Definitely better than my hacker project 10 years

**[02:19]** better than my hacker project 10 years

**[02:19]** better than my hacker project 10 years ago. Um but we need to think about the

**[02:22]** ago. Um but we need to think about the

**[02:22]** ago. Um but we need to think about the security posture around these systems

**[02:24]** security posture around these systems

**[02:24]** security posture around these systems and my general impression over the last

**[02:27]** and my general impression over the last

**[02:27]** and my general impression over the last uh last few years is like primary

**[02:30]** uh last few years is like primary

**[02:30]** uh last few years is like primary discussions around LM security really

**[02:32]** discussions around LM security really

**[02:32]** discussions around LM security really like hey is it um can you do prompt

**[02:34]** like hey is it um can you do prompt

**[02:34]** like hey is it um can you do prompt injection? Can you get it to do harmful

**[02:36]** injection? Can you get it to do harmful

**[02:36]** injection? Can you get it to do harmful content? um which is all really

**[02:38]** content? um which is all really

**[02:38]** content? um which is all really important but the reality with security

**[02:41]** important but the reality with security

**[02:41]** important but the reality with security is you need to look at all the different

**[02:43]** is you need to look at all the different

**[02:43]** is you need to look at all the different errors in your system and that is

**[02:46]** errors in your system and that is

**[02:46]** errors in your system and that is typically where real damage happens

**[02:48]** typically where real damage happens

**[02:48]** typically where real damage happens right and so this is really agent

**[02:51]** right and so this is really agent

**[02:51]** right and so this is really agent security and that is what I want to talk

**[02:54]** security and that is what I want to talk

**[02:54]** security and that is what I want to talk about today now one thing is like why

**[02:57]** about today now one thing is like why

**[02:57]** about today now one thing is like why did we even hack a bunch of agents it's

**[02:59]** did we even hack a bunch of agents it's

**[02:59]** did we even hack a bunch of agents it's kind of a weird thing to do um the


### [03:00 - 04:00]

**[03:01]** kind of a weird thing to do um the

**[03:01]** kind of a weird thing to do um the answer is quite frankly you know we

**[03:03]** answer is quite frankly you know we

**[03:03]** answer is quite frankly you know we wanted to launch internally at Y

**[03:05]** wanted to launch internally at Y

**[03:05]** wanted to launch internally at Y combinator and we wanted a splashy

**[03:07]** combinator and we wanted a splashy

**[03:07]** combinator and we wanted a splashy headline and so we're like uh oh what do

**[03:10]** headline and so we're like uh oh what do

**[03:10]** headline and so we're like uh oh what do we do and fun fact we have the second

**[03:12]** we do and fun fact we have the second

**[03:12]** we do and fun fact we have the second highest upvoted launch post inside y

**[03:14]** highest upvoted launch post inside y

**[03:14]** highest upvoted launch post inside y combinator of all time so higher than

**[03:16]** combinator of all time so higher than

**[03:16]** combinator of all time so higher than rippling yes okay um so uh we we bit we

**[03:20]** rippling yes okay um so uh we we bit we

**[03:20]** rippling yes okay um so uh we we bit we we did basically this approach at a time

**[03:22]** we did basically this approach at a time

**[03:22]** we did basically this approach at a time we're looking at oh which agents are

**[03:25]** we're looking at oh which agents are

**[03:25]** we're looking at oh which agents are already live and then let's just set a

**[03:26]** already live and then let's just set a

**[03:26]** already live and then let's just set a timer for 30 minutes we don't want to

**[03:28]** timer for 30 minutes we don't want to

**[03:28]** timer for 30 minutes we don't want to waste too much time on this and then you

**[03:30]** waste too much time on this and then you

**[03:30]** waste too much time on this and then you know let's let's figure out what their

**[03:31]** know let's let's figure out what their

**[03:32]** know let's let's figure out what their system prompts are and just kind of

**[03:33]** system prompts are and just kind of

**[03:33]** system prompts are and just kind of understand how they're working and I I

**[03:35]** understand how they're working and I I

**[03:35]** understand how they're working and I I have a feeling when I was creating this

**[03:36]** have a feeling when I was creating this

**[03:36]** have a feeling when I was creating this meme that this could be true, but it

**[03:38]** meme that this could be true, but it

**[03:38]** meme that this could be true, but it turns out it is true. And then we looked

**[03:42]** turns out it is true. And then we looked

**[03:42]** turns out it is true. And then we looked at, oh, what kind of tool definitions do

**[03:44]** at, oh, what kind of tool definitions do

**[03:44]** at, oh, what kind of tool definitions do they have, right? Like, you know, what

**[03:45]** they have, right? Like, you know, what

**[03:46]** they have, right? Like, you know, what is it supposed to do? Is it supposed to

**[03:47]** is it supposed to do? Is it supposed to

**[03:47]** is it supposed to do? Is it supposed to access data, supposed to run code,

**[03:50]** access data, supposed to run code,

**[03:50]** access data, supposed to run code, right? And then we just uh try to

**[03:52]** right? And then we just uh try to

**[03:52]** right? And then we just uh try to exploit them and see what's what's going

**[03:53]** exploit them and see what's what's going

**[03:53]** exploit them and see what's what's going on. Uh, and it was really fun because we

**[03:56]** on. Uh, and it was really fun because we

**[03:56]** on. Uh, and it was really fun because we hacked uh out of 16 agents that were

**[03:58]** hacked uh out of 16 agents that were

**[03:58]** hacked uh out of 16 agents that were launched within 30 minutes each. We were


### [04:00 - 05:00]

**[04:00]** launched within 30 minutes each. We were

**[04:00]** launched within 30 minutes each. We were hacked uh we hack we hacked seven of

**[04:02]** hacked uh we hack we hacked seven of

**[04:02]** hacked uh we hack we hacked seven of them. And there are three common issues

**[04:04]** them. And there are three common issues

**[04:04]** them. And there are three common issues we see across all of these ones. So I

**[04:06]** we see across all of these ones. So I

**[04:06]** we see across all of these ones. So I hope that we will all learn today what

**[04:09]** hope that we will all learn today what

**[04:09]** hope that we will all learn today what the most common issues are so you don't

**[04:10]** the most common issues are so you don't

**[04:10]** the most common issues are so you don't make the same mistakes and also this is

**[04:12]** make the same mistakes and also this is

**[04:12]** make the same mistakes and also this is going to be the best investment if

**[04:14]** going to be the best investment if

**[04:14]** going to be the best investment if you're a VC dispatch because they're all

**[04:16]** you're a VC dispatch because they're all

**[04:16]** you're a VC dispatch because they're all secure now. So first issue crosser data

**[04:20]** secure now. So first issue crosser data

**[04:20]** secure now. So first issue crosser data access I mean you guys were just here at

**[04:22]** access I mean you guys were just here at

**[04:22]** access I mean you guys were just here at the OF talk you know where this is going

**[04:24]** the OF talk you know where this is going

**[04:24]** the OF talk you know where this is going to head into right um so we first leaked

**[04:27]** to head into right um so we first leaked

**[04:27]** to head into right um so we first leaked this company's system prompt and we saw

**[04:30]** this company's system prompt and we saw

**[04:30]** this company's system prompt and we saw huh has a bunch of interesting tools

**[04:32]** huh has a bunch of interesting tools

**[04:32]** huh has a bunch of interesting tools attached to it including looking up user

**[04:35]** attached to it including looking up user

**[04:35]** attached to it including looking up user info by ID suspicious uh document by ID

**[04:39]** info by ID suspicious uh document by ID

**[04:39]** info by ID suspicious uh document by ID and a bunch of other things and then you

**[04:41]** and a bunch of other things and then you

**[04:41]** and a bunch of other things and then you know like when you see this you just

**[04:43]** know like when you see this you just

**[04:43]** know like when you see this you just want to like oh yeah there's this thing

**[04:45]** want to like oh yeah there's this thing

**[04:45]** want to like oh yeah there's this thing called IDOR like insecure direct object

**[04:48]** called IDOR like insecure direct object

**[04:48]** called IDOR like insecure direct object reference. It's basically when you make

**[04:50]** reference. It's basically when you make

**[04:50]** reference. It's basically when you make a request and you validate that, hey,

**[04:52]** a request and you validate that, hey,

**[04:52]** a request and you validate that, hey, the token is valid and you just let the

**[04:54]** the token is valid and you just let the

**[04:54]** the token is valid and you just let the request through, right? And you're kind

**[04:55]** request through, right? And you're kind

**[04:56]** request through, right? And you're kind of betting on the fact that the ID

**[04:57]** of betting on the fact that the ID

**[04:57]** of betting on the fact that the ID cannot be guessed. Well, that's

**[04:59]** cannot be guessed. Well, that's

**[04:59]** cannot be guessed. Well, that's obviously not good. Um, so yeah, we


### [05:00 - 06:00]

**[05:03]** obviously not good. Um, so yeah, we

**[05:03]** obviously not good. Um, so yeah, we looked up a product demo video that they

**[05:05]** looked up a product demo video that they

**[05:05]** looked up a product demo video that they recorded and we found the user ID in the

**[05:07]** recorded and we found the user ID in the

**[05:07]** recorded and we found the user ID in the URL bar and just like tried to plug it

**[05:10]** URL bar and just like tried to plug it

**[05:10]** URL bar and just like tried to plug it in. Uh, this is a different ID, by the

**[05:11]** in. Uh, this is a different ID, by the

**[05:11]** in. Uh, this is a different ID, by the way. Don't worry guys, this is my

**[05:13]** way. Don't worry guys, this is my

**[05:13]** way. Don't worry guys, this is my co-founder's ID now. And uh yeah, we

**[05:15]** co-founder's ID now. And uh yeah, we

**[05:15]** co-founder's ID now. And uh yeah, we were able to find their personal

**[05:17]** were able to find their personal

**[05:17]** were able to find their personal information including their email,

**[05:18]** information including their email,

**[05:18]** information including their email, nickname, whatever. Um but it gets

**[05:20]** nickname, whatever. Um but it gets

**[05:20]** nickname, whatever. Um but it gets better because these things are also

**[05:23]** better because these things are also

**[05:23]** better because these things are also interconnected. So you had not only

**[05:25]** interconnected. So you had not only

**[05:25]** interconnected. So you had not only their user ID, but you also had like oh

**[05:28]** their user ID, but you also had like oh

**[05:28]** their user ID, but you also had like oh the chat ID. Oh, and their document ID

**[05:31]** the chat ID. Oh, and their document ID

**[05:31]** the chat ID. Oh, and their document ID and then these things ultimately linked

**[05:33]** and then these things ultimately linked

**[05:33]** and then these things ultimately linked up together and allows you to traverse

**[05:34]** up together and allows you to traverse

**[05:34]** up together and allows you to traverse the entire system, right?

**[05:37]** the entire system, right?

**[05:38]** the entire system, right? It's not good. So what's the fix for

**[05:41]** It's not good. So what's the fix for

**[05:41]** It's not good. So what's the fix for that? There was a really comprehensive

**[05:42]** that? There was a really comprehensive

**[05:42]** that? There was a really comprehensive talk literally right before this. Sorry

**[05:44]** talk literally right before this. Sorry

**[05:44]** talk literally right before this. Sorry for the folks that missed it, but this

**[05:45]** for the folks that missed it, but this

**[05:45]** for the folks that missed it, but this is the basic fix for it, right? You need

**[05:48]** is the basic fix for it, right? You need

**[05:48]** is the basic fix for it, right? You need to think about how do you authenticate

**[05:50]** to think about how do you authenticate

**[05:50]** to think about how do you authenticate but also authorize the request. It's

**[05:51]** but also authorize the request. It's

**[05:51]** but also authorize the request. It's really two checks, right? Make sure your

**[05:53]** really two checks, right? Make sure your

**[05:53]** really two checks, right? Make sure your your token is valid. Good job team.

**[05:55]** your token is valid. Good job team.

**[05:55]** your token is valid. Good job team. Yeah, I got that. And then the second

**[05:57]** Yeah, I got that. And then the second

**[05:57]** Yeah, I got that. And then the second thing is like this is what we see in

**[05:58]** thing is like this is what we see in

**[05:58]** thing is like this is what we see in this superbase era with role level


### [06:00 - 07:00]

**[06:00]** this superbase era with role level

**[06:00]** this superbase era with role level security. Just make sure that you have

**[06:03]** security. Just make sure that you have

**[06:03]** security. Just make sure that you have some sort of access control matrix

**[06:04]** some sort of access control matrix

**[06:04]** some sort of access control matrix somewhere that checks that it matches up

**[06:06]** somewhere that checks that it matches up

**[06:06]** somewhere that checks that it matches up with whoever is making the request.

**[06:09]** with whoever is making the request.

**[06:09]** with whoever is making the request. Okay, super super important.

**[06:11]** Okay, super super important.

**[06:11]** Okay, super super important. authenticate and authorize.

**[06:14]** authenticate and authorize.

**[06:14]** authenticate and authorize. Now you can see this was actually, you

**[06:16]** Now you can see this was actually, you

**[06:16]** Now you can see this was actually, you know, an issue that was kind of there,

**[06:17]** know, an issue that was kind of there,

**[06:18]** know, an issue that was kind of there, right? It's it's not like around the LLM

**[06:19]** right? It's it's not like around the LLM

**[06:20]** right? It's it's not like around the LLM and the API server. It's really what is

**[06:21]** and the API server. It's really what is

**[06:22]** and the API server. It's really what is happening downstream. And um yeah,

**[06:24]** happening downstream. And um yeah,

**[06:24]** happening downstream. And um yeah, there's a lot of arrows in this diagram.

**[06:26]** there's a lot of arrows in this diagram.

**[06:26]** there's a lot of arrows in this diagram. We're going to look at all of them. So

**[06:29]** We're going to look at all of them. So

**[06:29]** We're going to look at all of them. So the next thing is to remember as you're

**[06:31]** the next thing is to remember as you're

**[06:31]** the next thing is to remember as you're thinking about these tools and how

**[06:33]** thinking about these tools and how

**[06:33]** thinking about these tools and how you're building it, like agents actually

**[06:35]** you're building it, like agents actually

**[06:35]** you're building it, like agents actually act like users um not API servers. when

**[06:38]** act like users um not API servers. when

**[06:38]** act like users um not API servers. when we were like debugging this issue like

**[06:40]** we were like debugging this issue like

**[06:40]** we were like debugging this issue like we actually asked a bunch of Y

**[06:41]** we actually asked a bunch of Y

**[06:41]** we actually asked a bunch of Y combinator companies like why did you

**[06:44]** combinator companies like why did you

**[06:44]** combinator companies like why did you build it this way because clearly they

**[06:45]** build it this way because clearly they

**[06:45]** build it this way because clearly they can build a web app properly right but

**[06:48]** can build a web app properly right but

**[06:48]** can build a web app properly right but it's just like I think as developers we

**[06:50]** it's just like I think as developers we

**[06:50]** it's just like I think as developers we have this natural pattern matching in

**[06:52]** have this natural pattern matching in

**[06:52]** have this natural pattern matching in our heads it's like oh yeah this thing

**[06:53]** our heads it's like oh yeah this thing

**[06:53]** our heads it's like oh yeah this thing runs on a server so it should be like a

**[06:55]** runs on a server so it should be like a

**[06:55]** runs on a server so it should be like a service and then I'm going to give it

**[06:56]** service and then I'm going to give it

**[06:56]** service and then I'm going to give it service level permissions but actually

**[06:58]** service level permissions but actually

**[06:58]** service level permissions but actually agents are like users right so


### [07:00 - 08:00]

**[07:01]** agents are like users right so

**[07:01]** agents are like users right so everything that applies to users apply

**[07:03]** everything that applies to users apply

**[07:03]** everything that applies to users apply to agents too so make sure that you know

**[07:06]** to agents too so make sure that you know

**[07:06]** to agents too so make sure that you know your LM should probably not determine

**[07:07]** your LM should probably not determine

**[07:07]** your LM should probably not determine authorization pattern that that that's

**[07:09]** authorization pattern that that that's

**[07:09]** authorization pattern that that that's bad. That's a red flag. Uh second thing

**[07:11]** bad. That's a red flag. Uh second thing

**[07:11]** bad. That's a red flag. Uh second thing is it should probably not act with

**[07:13]** is it should probably not act with

**[07:13]** is it should probably not act with service level permission. Listen to a

**[07:14]** service level permission. Listen to a

**[07:14]** service level permission. Listen to a previous talk on Olaf. That's great. Um

**[07:17]** previous talk on Olaf. That's great. Um

**[07:17]** previous talk on Olaf. That's great. Um and then just like users, you should

**[07:18]** and then just like users, you should

**[07:18]** and then just like users, you should make sure you uh don't just accept any

**[07:21]** make sure you uh don't just accept any

**[07:21]** make sure you uh don't just accept any input. Should sanitize them. Same with

**[07:23]** input. Should sanitize them. Same with

**[07:23]** input. Should sanitize them. Same with outputs, right? A lot of these are like

**[07:25]** outputs, right? A lot of these are like

**[07:25]** outputs, right? A lot of these are like the traditional web application security

**[07:27]** the traditional web application security

**[07:27]** the traditional web application security things that you just need to like really

**[07:29]** things that you just need to like really

**[07:29]** things that you just need to like really really internalize for this new world.

**[07:32]** really internalize for this new world.

**[07:32]** really internalize for this new world. Now that was interesting. And so the

**[07:35]** Now that was interesting. And so the

**[07:35]** Now that was interesting. And so the second one was even better. Um so this

**[07:37]** second one was even better. Um so this

**[07:37]** second one was even better. Um so this is not as common but the damage is

**[07:40]** is not as common but the damage is

**[07:40]** is not as common but the damage is bigger. So it's what in pattern we see

**[07:42]** bigger. So it's what in pattern we see

**[07:42]** bigger. So it's what in pattern we see so there are a lot of code tools that

**[07:44]** so there are a lot of code tools that

**[07:44]** so there are a lot of code tools that agents use and there's a there's a

**[07:47]** agents use and there's a there's a

**[07:47]** agents use and there's a there's a there's a anthropic paper here. It

**[07:49]** there's a anthropic paper here. It

**[07:49]** there's a anthropic paper here. It basically talks about what's the

**[07:50]** basically talks about what's the

**[07:50]** basically talks about what's the distribution of which industry and how

**[07:53]** distribution of which industry and how

**[07:53]** distribution of which industry and how much do they use claude and there's like

**[07:55]** much do they use claude and there's like

**[07:55]** much do they use claude and there's like this one outlier here. I'll zoom it in

**[07:57]** this one outlier here. I'll zoom it in

**[07:57]** this one outlier here. I'll zoom it in for you. Um yeah so us nerds we make up


### [08:00 - 09:00]

**[08:01]** for you. Um yeah so us nerds we make up

**[08:01]** for you. Um yeah so us nerds we make up 3.4% of the world but we're 37% of

**[08:04]** 3.4% of the world but we're 37% of

**[08:04]** 3.4% of the world but we're 37% of cloud's usage. Oh, why is that? Because

**[08:06]** cloud's usage. Oh, why is that? Because

**[08:06]** cloud's usage. Oh, why is that? Because we love computers and we love coding,

**[08:08]** we love computers and we love coding,

**[08:08]** we love computers and we love coding, right? And so we found immediately the

**[08:09]** right? And so we found immediately the

**[08:09]** right? And so we found immediately the value of it. But it's not just us that

**[08:13]** value of it. But it's not just us that

**[08:13]** value of it. But it's not just us that use agents with coding tools. In fact,

**[08:15]** use agents with coding tools. In fact,

**[08:15]** use agents with coding tools. In fact, many agents create code on demand to do

**[08:18]** many agents create code on demand to do

**[08:18]** many agents create code on demand to do some things, right? Like some agents

**[08:20]** some things, right? Like some agents

**[08:20]** some things, right? Like some agents just generate a calculator on demand to

**[08:22]** just generate a calculator on demand to

**[08:22]** just generate a calculator on demand to make a calculation, right? And so

**[08:25]** make a calculation, right? And so

**[08:25]** make a calculation, right? And so there's a lot of these code execution

**[08:27]** there's a lot of these code execution

**[08:27]** there's a lot of these code execution sandboxes out there that are

**[08:28]** sandboxes out there that are

**[08:28]** sandboxes out there that are interesting. And so if you if you think

**[08:31]** interesting. And so if you if you think

**[08:31]** interesting. And so if you if you think about that there's actually a critical

**[08:33]** about that there's actually a critical

**[08:33]** about that there's actually a critical path in your system because you've got a

**[08:35]** path in your system because you've got a

**[08:35]** path in your system because you've got a tool that talks to another container. A

**[08:37]** tool that talks to another container. A

**[08:37]** tool that talks to another container. A container is arbitrary compute and when

**[08:39]** container is arbitrary compute and when

**[08:39]** container is arbitrary compute and when you have arbitrary compute many things

**[08:41]** you have arbitrary compute many things

**[08:41]** you have arbitrary compute many things can happen many bad things many good

**[08:43]** can happen many bad things many good

**[08:43]** can happen many bad things many good things right but let's talk about the

**[08:44]** things right but let's talk about the

**[08:44]** things right but let's talk about the bad things today. So we did the same

**[08:47]** bad things today. So we did the same

**[08:47]** bad things today. So we did the same script did the system prompt again the

**[08:49]** script did the system prompt again the

**[08:49]** script did the system prompt again the system prompt itself great I mean

**[08:50]** system prompt itself great I mean

**[08:50]** system prompt itself great I mean doesn't cause any damage but as an

**[08:53]** doesn't cause any damage but as an

**[08:53]** doesn't cause any damage but as an attacker you always think about the fact

**[08:55]** attacker you always think about the fact

**[08:55]** attacker you always think about the fact uh the things that are like huh that's

**[08:57]** uh the things that are like huh that's

**[08:57]** uh the things that are like huh that's kind of suspicious right it's like oh

**[08:59]** kind of suspicious right it's like oh

**[08:59]** kind of suspicious right it's like oh wait it it it runs code and never


### [09:00 - 10:00]

**[09:02]** wait it it it runs code and never

**[09:02]** wait it it it runs code and never outputed it to the user okay let's

**[09:03]** outputed it to the user okay let's

**[09:03]** outputed it to the user okay let's output it to the user oh yeah and and

**[09:05]** output it to the user oh yeah and and

**[09:05]** output it to the user oh yeah and and most mostly run it mostly at most once

**[09:08]** most mostly run it mostly at most once

**[09:08]** most mostly run it mostly at most once let's run it all the time and so you try

**[09:10]** let's run it all the time and so you try

**[09:10]** let's run it all the time and so you try to basically invert what the system

**[09:13]** to basically invert what the system

**[09:13]** to basically invert what the system prompt is saying because that is exactly

**[09:14]** prompt is saying because that is exactly

**[09:14]** prompt is saying because that is exactly what the developer didn't want you to do

**[09:16]** what the developer didn't want you to do

**[09:16]** what the developer didn't want you to do and that is how bad actors think right

**[09:19]** and that is how bad actors think right

**[09:19]** and that is how bad actors think right so we figured out oh this thing does

**[09:21]** so we figured out oh this thing does

**[09:21]** so we figured out oh this thing does have a code tool and so you know we

**[09:23]** have a code tool and so you know we

**[09:23]** have a code tool and so you know we tried we tried running something it's

**[09:25]** tried we tried running something it's

**[09:25]** tried we tried running something it's like ah it only allows me to write

**[09:27]** like ah it only allows me to write

**[09:27]** like ah it only allows me to write Python and you know I love JavaScript

**[09:29]** Python and you know I love JavaScript

**[09:29]** Python and you know I love JavaScript and um yeah and doesn't allow me to run

**[09:31]** and um yeah and doesn't allow me to run

**[09:31]** and um yeah and doesn't allow me to run these really dangerous you know function

**[09:33]** these really dangerous you know function

**[09:33]** these really dangerous you know function calls okay and it restricts like which

**[09:35]** calls okay and it restricts like which

**[09:36]** calls okay and it restricts like which Python files to run that's also not good

**[09:38]** Python files to run that's also not good

**[09:38]** Python files to run that's also not good so yeah but we looked at what it could

**[09:40]** so yeah but we looked at what it could

**[09:40]** so yeah but we looked at what it could do and it had two kind of innocent

**[09:44]** do and it had two kind of innocent

**[09:44]** do and it had two kind of innocent permissions

**[09:45]** permissions

**[09:45]** permissions write a Python file and read some files.

**[09:49]** write a Python file and read some files.

**[09:49]** write a Python file and read some files. You can do a lot with that. This is

**[09:50]** You can do a lot with that. This is

**[09:50]** You can do a lot with that. This is great because what if we just looked

**[09:53]** great because what if we just looked

**[09:53]** great because what if we just looked around the file system now, right? We

**[09:54]** around the file system now, right? We

**[09:54]** around the file system now, right? We can read files. So, we looked at build

**[09:57]** can read files. So, we looked at build

**[09:57]** can read files. So, we looked at build me a little tree functionality and you

**[09:59]** me a little tree functionality and you

**[09:59]** me a little tree functionality and you know, return me the entire file system


### [10:00 - 11:00]

**[10:01]** know, return me the entire file system

**[10:01]** know, return me the entire file system tree to see what's going on. Oh my god,

**[10:03]** tree to see what's going on. Oh my god,

**[10:03]** tree to see what's going on. Oh my god, there's a app.py file. That's probably

**[10:05]** there's a app.py file. That's probably

**[10:05]** there's a app.py file. That's probably important. Um, and then we looked at,

**[10:07]** important. Um, and then we looked at,

**[10:07]** important. Um, and then we looked at, oh, it has two endpoints, write file and

**[10:09]** oh, it has two endpoints, write file and

**[10:09]** oh, it has two endpoints, write file and execute file. Ah, okay. These endpoints

**[10:12]** execute file. Ah, okay. These endpoints

**[10:12]** execute file. Ah, okay. These endpoints are hidden behind the VPC. So, we cannot

**[10:13]** are hidden behind the VPC. So, we cannot

**[10:13]** are hidden behind the VPC. So, we cannot hit it directly. That's okay. Um, but

**[10:17]** hit it directly. That's okay. Um, but

**[10:17]** hit it directly. That's okay. Um, but huh, we can write files. Huh, we can

**[10:20]** huh, we can write files. Huh, we can

**[10:20]** huh, we can write files. Huh, we can write fuzz. There's a app.py file. Huh?

**[10:24]** write fuzz. There's a app.py file. Huh?

**[10:24]** write fuzz. There's a app.py file. Huh? Let's look into that. Oh, wait. That's

**[10:26]** Let's look into that. Oh, wait. That's

**[10:26]** Let's look into that. Oh, wait. That's where all the protections are for their

**[10:28]** where all the protections are for their

**[10:28]** where all the protections are for their code. Uh, and so we can just override

**[10:31]** code. Uh, and so we can just override

**[10:31]** code. Uh, and so we can just override the app.py file with empty strings

**[10:34]** the app.py file with empty strings

**[10:34]** the app.py file with empty strings around all the security checks. And

**[10:38]** around all the security checks. And

**[10:38]** around all the security checks. And whoopsie, we got in. So now we can

**[10:41]** whoopsie, we got in. So now we can

**[10:41]** whoopsie, we got in. So now we can Bitcoin mine all day. That's great,

**[10:42]** Bitcoin mine all day. That's great,

**[10:42]** Bitcoin mine all day. That's great, right? Yeah. No, it gets much worse. So

**[10:45]** right? Yeah. No, it gets much worse. So

**[10:45]** right? Yeah. No, it gets much worse. So the thing with arbitrary code execution

**[10:48]** the thing with arbitrary code execution

**[10:48]** the thing with arbitrary code execution once you're inside a container is that

**[10:51]** once you're inside a container is that

**[10:51]** once you're inside a container is that you can do many things like um there's

**[10:53]** you can do many things like um there's

**[10:53]** you can do many things like um there's this thing called service endpoint

**[10:55]** this thing called service endpoint

**[10:55]** this thing called service endpoint discovery, metadata discovery. You all

**[10:56]** discovery, metadata discovery. You all

**[10:56]** discovery, metadata discovery. You all heard of that? No. Okay. Basically

**[10:59]** heard of that? No. Okay. Basically

**[10:59]** heard of that? No. Okay. Basically allows you to discover what are other


### [11:00 - 12:00]

**[11:01]** allows you to discover what are other

**[11:01]** allows you to discover what are other devices on the uh what are the devices

**[11:03]** devices on the uh what are the devices

**[11:03]** devices on the uh what are the devices on the network? What other resource are

**[11:04]** on the network? What other resource are

**[11:04]** on the network? What other resource are there on the network? And uh you can

**[11:06]** there on the network? And uh you can

**[11:06]** there on the network? And uh you can also just you know fetch the user token

**[11:08]** also just you know fetch the user token

**[11:08]** also just you know fetch the user token uh sorry the service token you know just

**[11:10]** uh sorry the service token you know just

**[11:10]** uh sorry the service token you know just see what's going on what's the project

**[11:11]** see what's going on what's the project

**[11:11]** see what's going on what's the project name yeah you know and you start looking

**[11:13]** name yeah you know and you start looking

**[11:13]** name yeah you know and you start looking around it's like oh okay yeah okay I I I

**[11:15]** around it's like oh okay yeah okay I I I

**[11:15]** around it's like oh okay yeah okay I I I can also fetch the scopes so I can use

**[11:17]** can also fetch the scopes so I can use

**[11:17]** can also fetch the scopes so I can use do many things with this token that's

**[11:19]** do many things with this token that's

**[11:19]** do many things with this token that's awesome um who has really really spent

**[11:23]** awesome um who has really really spent

**[11:23]** awesome um who has really really spent time configuring service level tokens

**[11:25]** time configuring service level tokens

**[11:25]** time configuring service level tokens and their permissions in a granular

**[11:27]** and their permissions in a granular

**[11:27]** and their permissions in a granular manner and does it all the time and

**[11:29]** manner and does it all the time and

**[11:29]** manner and does it all the time and never forgets to set something wrong.

**[11:33]** never forgets to set something wrong.

**[11:33]** never forgets to set something wrong. Okay, one guy. One guy there. Okay.

**[11:35]** Okay, one guy. One guy there. Okay.

**[11:35]** Okay, one guy. One guy there. Okay. Whoops. See, we have access to all their

**[11:37]** Whoops. See, we have access to all their

**[11:37]** Whoops. See, we have access to all their customer data. So that's uh we just

**[11:39]** customer data. So that's uh we just

**[11:39]** customer data. So that's uh we just queried BigQuery which has a great

**[11:41]** queried BigQuery which has a great

**[11:41]** queried BigQuery which has a great interface for that. Isn't that cool?

**[11:42]** interface for that. Isn't that cool?

**[11:42]** interface for that. Isn't that cool? Yeah. So yeah, making sure you have code

**[11:45]** Yeah. So yeah, making sure you have code

**[11:45]** Yeah. So yeah, making sure you have code sandboxes correctly is very hard because

**[11:47]** sandboxes correctly is very hard because

**[11:47]** sandboxes correctly is very hard because you can move laterally across the

**[11:49]** you can move laterally across the

**[11:49]** you can move laterally across the infrastructure and that is just very

**[11:51]** infrastructure and that is just very

**[11:51]** infrastructure and that is just very very dangerous. Okay. And so kind of

**[11:54]** very dangerous. Okay. And so kind of

**[11:54]** very dangerous. Okay. And so kind of like don't roll your off in the web

**[11:56]** like don't roll your off in the web

**[11:56]** like don't roll your off in the web world. Don't roll your own code

**[11:57]** world. Don't roll your own code

**[11:57]** world. Don't roll your own code sandboxes please. Like it's it's just

**[11:59]** sandboxes please. Like it's it's just


### [12:00 - 13:00]

**[12:00]** sandboxes please. Like it's it's just very hard. It's very very hard and so

**[12:03]** very hard. It's very very hard and so

**[12:03]** very hard. It's very very hard and so use out of the box solution. There are

**[12:04]** use out of the box solution. There are

**[12:04]** use out of the box solution. There are many of them. ETB is I think a very

**[12:06]** many of them. ETB is I think a very

**[12:06]** many of them. ETB is I think a very popular one. Some some folks probably

**[12:08]** popular one. Some some folks probably

**[12:08]** popular one. Some some folks probably heard of it. Uh there's one in our YC

**[12:10]** heard of it. Uh there's one in our YC

**[12:10]** heard of it. Uh there's one in our YC batch that I personally just genuinely

**[12:12]** batch that I personally just genuinely

**[12:12]** batch that I personally just genuinely really love. They have observability

**[12:14]** really love. They have observability

**[12:14]** really love. They have observability built in. They boot up super quickly.

**[12:15]** built in. They boot up super quickly.

**[12:16]** built in. They boot up super quickly. And what I love about them is they have

**[12:17]** And what I love about them is they have

**[12:17]** And what I love about them is they have an MCP server that just is easy to plug

**[12:19]** an MCP server that just is easy to plug

**[12:19]** an MCP server that just is easy to plug into, right? So just easier for your

**[12:20]** into, right? So just easier for your

**[12:20]** into, right? So just easier for your agents to work with. So please do that.

**[12:24]** agents to work with. So please do that.

**[12:24]** agents to work with. So please do that. Don't do, you know, your own Python app.

**[12:27]** Don't do, you know, your own Python app.

**[12:27]** Don't do, you know, your own Python app. Um it's not good. Trust me. Um, so that

**[12:31]** Um it's not good. Trust me. Um, so that

**[12:31]** Um it's not good. Trust me. Um, so that leads into a third part of a attack

**[12:34]** leads into a third part of a attack

**[12:34]** leads into a third part of a attack vector around serverside request

**[12:35]** vector around serverside request

**[12:36]** vector around serverside request forgery.

**[12:37]** forgery.

**[12:37]** forgery. It's a very long word and it really bugs

**[12:39]** It's a very long word and it really bugs

**[12:39]** It's a very long word and it really bugs me that the SSRF didn't fit on the

**[12:41]** me that the SSRF didn't fit on the

**[12:41]** me that the SSRF didn't fit on the previous line. This really triggers me.

**[12:44]** previous line. This really triggers me.

**[12:44]** previous line. This really triggers me. Um, yeah, I know. So um this is what

**[12:47]** Um, yeah, I know. So um this is what

**[12:47]** Um, yeah, I know. So um this is what happens when you can kind of co can kind

**[12:50]** happens when you can kind of co can kind

**[12:50]** happens when you can kind of co can kind of get a tool to call another endpoint

**[12:52]** of get a tool to call another endpoint

**[12:52]** of get a tool to call another endpoint that you didn't and you know that the

**[12:54]** that you didn't and you know that the

**[12:54]** that you didn't and you know that the service itself didn't intend you to call

**[12:56]** service itself didn't intend you to call

**[12:56]** service itself didn't intend you to call and you can pull out a lot of

**[12:58]** and you can pull out a lot of

**[12:58]** and you can pull out a lot of information just through that workflow.


### [13:00 - 14:00]

**[13:00]** information just through that workflow.

**[13:00]** information just through that workflow. So let me give you an example. So this

**[13:03]** So let me give you an example. So this

**[13:03]** So let me give you an example. So this is exactly extracted system prompt.

**[13:05]** is exactly extracted system prompt.

**[13:05]** is exactly extracted system prompt. Great. Oh this thing can create

**[13:07]** Great. Oh this thing can create

**[13:07]** Great. Oh this thing can create databases. That sounds exciting. Um, and

**[13:10]** databases. That sounds exciting. Um, and

**[13:10]** databases. That sounds exciting. Um, and then you look into it, it's like, huh,

**[13:12]** then you look into it, it's like, huh,

**[13:12]** then you look into it, it's like, huh, it pulls the database schema from a

**[13:16]** it pulls the database schema from a

**[13:16]** it pulls the database schema from a private GitHub repository.

**[13:18]** private GitHub repository.

**[13:18]** private GitHub repository. Isn't that great? That means whatever

**[13:21]** Isn't that great? That means whatever

**[13:21]** Isn't that great? That means whatever request goes to that private GitHub

**[13:22]** request goes to that private GitHub

**[13:22]** request goes to that private GitHub repository must have the Git

**[13:24]** repository must have the Git

**[13:24]** repository must have the Git credentials, right? Otherwise, how can

**[13:26]** credentials, right? Otherwise, how can

**[13:26]** credentials, right? Otherwise, how can it pull that from a private repository?

**[13:28]** it pull that from a private repository?

**[13:28]** it pull that from a private repository? So, um, yeah, and it's just a string.

**[13:31]** So, um, yeah, and it's just a string.

**[13:31]** So, um, yeah, and it's just a string. So, I guess I can just put in whatever

**[13:32]** So, I guess I can just put in whatever

**[13:32]** So, I guess I can just put in whatever string I want and coers it into

**[13:34]** string I want and coers it into

**[13:34]** string I want and coers it into providing that. So, let's set up a

**[13:36]** providing that. So, let's set up a

**[13:36]** providing that. So, let's set up a badacctor.com test.git git repo and just

**[13:39]** badacctor.com test.git git repo and just

**[13:39]** badacctor.com test.git git repo and just see what credentials come through and

**[13:42]** see what credentials come through and

**[13:42]** see what credentials come through and yep it comes across with the git

**[13:44]** yep it comes across with the git

**[13:44]** yep it comes across with the git credentials and so now you can actually

**[13:46]** credentials and so now you can actually

**[13:46]** credentials and so now you can actually take those git credentials and just

**[13:48]** take those git credentials and just

**[13:48]** take those git credentials and just download their entire codebase that was

**[13:50]** download their entire codebase that was

**[13:50]** download their entire codebase that was behind a private repo. Isn't that crazy?

**[13:53]** behind a private repo. Isn't that crazy?

**[13:53]** behind a private repo. Isn't that crazy? Isn't that crazy? Yeah. This is I mean

**[13:55]** Isn't that crazy? Yeah. This is I mean

**[13:56]** Isn't that crazy? Yeah. This is I mean it's awesome for me to do this, right?

**[13:57]** it's awesome for me to do this, right?

**[13:57]** it's awesome for me to do this, right? It's like you get paid to do this. Come

**[13:59]** It's like you get paid to do this. Come

**[13:59]** It's like you get paid to do this. Come on. It's amazing. Now um we told our


### [14:00 - 15:00]

**[14:02]** on. It's amazing. Now um we told our

**[14:02]** on. It's amazing. Now um we told our batchmates immediately and they told us

**[14:03]** batchmates immediately and they told us

**[14:04]** batchmates immediately and they told us don't worry bro it's already fixed. It's

**[14:05]** don't worry bro it's already fixed. It's

**[14:05]** don't worry bro it's already fixed. It's okay guys. that that company's secure if

**[14:07]** okay guys. that that company's secure if

**[14:08]** okay guys. that that company's secure if you're a VC listening in. Um, so so but

**[14:10]** you're a VC listening in. Um, so so but

**[14:10]** you're a VC listening in. Um, so so but with that though it is really important

**[14:12]** with that though it is really important

**[14:12]** with that though it is really important to think about the implications of what

**[14:14]** to think about the implications of what

**[14:14]** to think about the implications of what your system is doing, right? I I love

**[14:17]** your system is doing, right? I I love

**[14:17]** your system is doing, right? I I love vibe coding, not going to lie, but like

**[14:20]** vibe coding, not going to lie, but like

**[14:20]** vibe coding, not going to lie, but like you got to really think about where all

**[14:21]** you got to really think about where all

**[14:22]** you got to really think about where all these arrows are and if you've

**[14:23]** these arrows are and if you've

**[14:23]** these arrows are and if you've configured those things correct

**[14:24]** configured those things correct

**[14:24]** configured those things correct correctly. So with that, always sanitize

**[14:28]** correctly. So with that, always sanitize

**[14:28]** correctly. So with that, always sanitize your inputs and outputs. This could be

**[14:30]** your inputs and outputs. This could be

**[14:30]** your inputs and outputs. This could be like a webdev conference from 20 years

**[14:32]** like a webdev conference from 20 years

**[14:32]** like a webdev conference from 20 years ago. Um, but but it applies to agents

**[14:35]** ago. Um, but but it applies to agents

**[14:35]** ago. Um, but but it applies to agents too, right? like we just need to make

**[14:37]** too, right? like we just need to make

**[14:37]** too, right? like we just need to make sure we keep those good security

**[14:38]** sure we keep those good security

**[14:38]** sure we keep those good security practices that have that we have learned

**[14:41]** practices that have that we have learned

**[14:41]** practices that have that we have learned to love hopefully over the years to take

**[14:44]** to love hopefully over the years to take

**[14:44]** to love hopefully over the years to take it forward to a new technology paradigm

**[14:47]** it forward to a new technology paradigm

**[14:47]** it forward to a new technology paradigm and then ultimately I want you to take

**[14:49]** and then ultimately I want you to take

**[14:49]** and then ultimately I want you to take away three things. So first thing is

**[14:51]** away three things. So first thing is

**[14:51]** away three things. So first thing is agent security is bigger than just LM

**[14:54]** agent security is bigger than just LM

**[14:54]** agent security is bigger than just LM security. Make sure you understand how

**[14:56]** security. Make sure you understand how

**[14:56]** security. Make sure you understand how these threat vectors apply inside your

**[14:58]** these threat vectors apply inside your

**[14:58]** these threat vectors apply inside your overall system. Second thing is treat


### [15:00 - 16:00]

**[15:01]** overall system. Second thing is treat

**[15:01]** overall system. Second thing is treat agents as users and that applies to

**[15:03]** agents as users and that applies to

**[15:03]** agents as users and that applies to authentication to sanitization of user

**[15:05]** authentication to sanitization of user

**[15:05]** authentication to sanitization of user inputs and many of the other things. And

**[15:08]** inputs and many of the other things. And

**[15:08]** inputs and many of the other things. And last thing definitely don't roll your

**[15:10]** last thing definitely don't roll your

**[15:10]** last thing definitely don't roll your own code signbox. That is just so

**[15:12]** own code signbox. That is just so

**[15:12]** own code signbox. That is just so dangerous and you know it it it very

**[15:14]** dangerous and you know it it it very

**[15:14]** dangerous and you know it it it very quickly turns from like an intern

**[15:16]** quickly turns from like an intern

**[15:16]** quickly turns from like an intern project into like a nightmare. So it be

**[15:18]** project into like a nightmare. So it be

**[15:18]** project into like a nightmare. So it be very very careful with that. And these

**[15:21]** very very careful with that. And these

**[15:21]** very very careful with that. And these are the most basic ones that we've seen

**[15:23]** are the most basic ones that we've seen

**[15:23]** are the most basic ones that we've seen come across, right? There's obviously

**[15:25]** come across, right? There's obviously

**[15:25]** come across, right? There's obviously many more security issues. And if you

**[15:27]** many more security issues. And if you

**[15:28]** many more security issues. And if you don't know exactly how your agent

**[15:29]** don't know exactly how your agent

**[15:29]** don't know exactly how your agent security posture is, you can go to

**[15:31]** security posture is, you can go to

**[15:31]** security posture is, you can go to casco.com. You can book a demo with us.

**[15:33]** casco.com. You can book a demo with us.

**[15:33]** casco.com. You can book a demo with us. We built an AI agent that actively

**[15:35]** We built an AI agent that actively

**[15:35]** We built an AI agent that actively attacks other AI agents and tells you

**[15:37]** attacks other AI agents and tells you

**[15:37]** attacks other AI agents and tells you where they break. Isn't that great? Um,

**[15:39]** where they break. Isn't that great? Um,

**[15:40]** where they break. Isn't that great? Um, and yeah, feel free to connect with me

**[15:41]** and yeah, feel free to connect with me

**[15:41]** and yeah, feel free to connect with me on LinkedIn or on Twitter and I have uh

**[15:43]** on LinkedIn or on Twitter and I have uh

**[15:43]** on LinkedIn or on Twitter and I have uh every now and then some good stuff to

**[15:44]** every now and then some good stuff to

**[15:44]** every now and then some good stuff to post. Yeah.

**[15:50]** [Applause]

**[15:50]** [Applause] Awesome. Thanks, Renee. Does anyone have

**[15:53]** Awesome. Thanks, Renee. Does anyone have

**[15:53]** Awesome. Thanks, Renee. Does anyone have any questions? We can have time for like

**[15:54]** any questions? We can have time for like

**[15:54]** any questions? We can have time for like one or two quick questions if you're if

**[15:56]** one or two quick questions if you're if

**[15:56]** one or two quick questions if you're if you're game for it. Sure.


### [16:00 - 17:00]

**[16:00]** you're game for it. Sure.

**[16:00]** you're game for it. Sure. Um how do I look at system problems?

**[16:02]** Um how do I look at system problems?

**[16:02]** Um how do I look at system problems? There's a lot of just like open

**[16:04]** There's a lot of just like open

**[16:04]** There's a lot of just like open techniques. The the best one that I've

**[16:05]** techniques. The the best one that I've

**[16:05]** techniques. The the best one that I've seen is uh from hidden layer.com. Have

**[16:07]** seen is uh from hidden layer.com. Have

**[16:07]** seen is uh from hidden layer.com. Have you guys checked that those guys out?

**[16:08]** you guys checked that those guys out?

**[16:08]** you guys checked that those guys out? They have a great blog post on like um

**[16:11]** They have a great blog post on like um

**[16:11]** They have a great blog post on like um it's a policy puppeteering attack. Yeah,

**[16:13]** it's a policy puppeteering attack. Yeah,

**[16:14]** it's a policy puppeteering attack. Yeah, it's great.

**[16:16]** it's great.

**[16:16]** it's great. Very cool. Cool. Awesome. Oh yeah.

**[16:23]** How do you make sure

**[16:23]** How do you make sure because

**[16:26]** because

**[16:26]** because how do you make sure that

**[16:40]** Yeah. Are you talking about it locally

**[16:40]** Yeah. Are you talking about it locally or server side?

**[16:43]** or server side?

**[16:43]** or server side? Yeah.

**[16:46]** Yeah.

**[16:46]** Yeah. Yeah.

**[16:51]** Yeah. No, very much so. So locally uh I

**[16:51]** Yeah. No, very much so. So locally uh I think right now the industry is either

**[16:53]** think right now the industry is either

**[16:53]** think right now the industry is either you go full yolo mode or you ask every

**[16:56]** you go full yolo mode or you ask every

**[16:56]** you go full yolo mode or you ask every time right um I mean I'm not joking

**[16:58]** time right um I mean I'm not joking

**[16:58]** time right um I mean I'm not joking cursor thing is called yolo mode right


### [17:00 - 18:00]

**[17:01]** cursor thing is called yolo mode right

**[17:01]** cursor thing is called yolo mode right um and then on server side use a code

**[17:02]** um and then on server side use a code

**[17:02]** um and then on server side use a code sandbox because ultimately they have

**[17:04]** sandbox because ultimately they have

**[17:04]** sandbox because ultimately they have constraints uh around the internal

**[17:06]** constraints uh around the internal

**[17:06]** constraints uh around the internal networks but also they have constraints

**[17:08]** networks but also they have constraints

**[17:08]** networks but also they have constraints around um how long they can live as a

**[17:10]** around um how long they can live as a

**[17:10]** around um how long they can live as a sandbox. Yeah. Okay. Sandboxes that use

**[17:14]** sandbox. Yeah. Okay. Sandboxes that use

**[17:14]** sandbox. Yeah. Okay. Sandboxes that use um yeah so they they typically use

**[17:16]** um yeah so they they typically use

**[17:16]** um yeah so they they typically use something called firecracker under the

**[17:17]** something called firecracker under the

**[17:17]** something called firecracker under the hood which is better isolation layer.

**[17:19]** hood which is better isolation layer.

**[17:19]** hood which is better isolation layer. Yeah. Uh, if you just use containers, by

**[17:21]** Yeah. Uh, if you just use containers, by

**[17:21]** Yeah. Uh, if you just use containers, by the way, that's not an isolation layer

**[17:22]** the way, that's not an isolation layer

**[17:22]** the way, that's not an isolation layer in case anybody's wondering. Yeah. Yeah.

**[17:24]** in case anybody's wondering. Yeah. Yeah.

**[17:24]** in case anybody's wondering. Yeah. Yeah. Don't use containers for isolation.

**[17:25]** Don't use containers for isolation.

**[17:25]** Don't use containers for isolation. Yeah.


