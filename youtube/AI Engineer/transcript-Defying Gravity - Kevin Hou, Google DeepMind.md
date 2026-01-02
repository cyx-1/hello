# Defying Gravity - Kevin Hou, Google DeepMind

**Video URL:** https://www.youtube.com/watch?v=HN-F-OQe6j0

---

## Full Transcript

### [00:00 - 01:00]

**[00:23]** All right. Hello. Last one of the day.

**[00:23]** All right. Hello. Last one of the day. Can we get a uh little energy boost?

**[00:25]** Can we get a uh little energy boost?

**[00:25]** Can we get a uh little energy boost? Who's ready? Who's ready? [applause]

**[00:29]** Who's ready? Who's ready? [applause]

**[00:29]** Who's ready? Who's ready? [applause] All right, happy Friday. I hope everyone

**[00:31]** All right, happy Friday. I hope everyone

**[00:31]** All right, happy Friday. I hope everyone has had a good week, a good conference.

**[00:33]** has had a good week, a good conference.

**[00:33]** has had a good week, a good conference. Um, and let me tell you, it's been a

**[00:35]** Um, and let me tell you, it's been a

**[00:35]** Um, and let me tell you, it's been a really bad week if you are Gravity.

**[00:37]** really bad week if you are Gravity.

**[00:37]** really bad week if you are Gravity. Wicked 2 is coming out tonight. And

**[00:39]** Wicked 2 is coming out tonight. And

**[00:40]** Wicked 2 is coming out tonight. And then, of course, Anti-gravity came out

**[00:41]** then, of course, Anti-gravity came out

**[00:42]** then, of course, Anti-gravity came out earlier this week alongside Gemini 3 Pro

**[00:44]** earlier this week alongside Gemini 3 Pro

**[00:44]** earlier this week alongside Gemini 3 Pro on Tuesday.

**[00:46]** on Tuesday.

**[00:46]** on Tuesday. Google Anti-gravity is a brand new IDE

**[00:49]** Google Anti-gravity is a brand new IDE

**[00:49]** Google Anti-gravity is a brand new IDE out of Google DeepMind. It's the first

**[00:51]** out of Google DeepMind. It's the first

**[00:52]** out of Google DeepMind. It's the first one from a foundational lab and it is

**[00:54]** one from a foundational lab and it is

**[00:54]** one from a foundational lab and it is coming right off the press. In fact, um

**[00:57]** coming right off the press. In fact, um

**[00:57]** coming right off the press. In fact, um I probably should be working on the

**[00:58]** I probably should be working on the

**[00:58]** I probably should be working on the product right now, but I wanted to spend

**[00:59]** product right now, but I wanted to spend

**[00:59]** product right now, but I wanted to spend some time to share what we've built here


### [01:00 - 02:00]

**[01:01]** some time to share what we've built here

**[01:01]** some time to share what we've built here today.

**[01:04]** today.

**[01:04]** today. Anti-gravity is unapologetically

**[01:06]** Anti-gravity is unapologetically

**[01:06]** Anti-gravity is unapologetically agent first. And today, I'm going to

**[01:08]** agent first. And today, I'm going to

**[01:08]** agent first. And today, I'm going to tell you a little bit about what that

**[01:10]** tell you a little bit about what that

**[01:10]** tell you a little bit about what that means and how it manifests in the

**[01:12]** means and how it manifests in the

**[01:12]** means and how it manifests in the product. But perhaps maybe a little bit

**[01:14]** product. But perhaps maybe a little bit

**[01:14]** product. But perhaps maybe a little bit more interestingly, we're going to talk

**[01:15]** more interestingly, we're going to talk

**[01:15]** more interestingly, we're going to talk a little bit about how we got here.

**[01:17]** a little bit about how we got here.

**[01:17]** a little bit about how we got here. Product principles, direction of the

**[01:18]** Product principles, direction of the

**[01:18]** Product principles, direction of the industry, these sorts of things. Um so

**[01:21]** industry, these sorts of things. Um so

**[01:21]** industry, these sorts of things. Um so my name is Kevin How. I lead our product

**[01:22]** my name is Kevin How. I lead our product

**[01:22]** my name is Kevin How. I lead our product engineering team at Google Antigravity.

**[01:25]** engineering team at Google Antigravity.

**[01:25]** engineering team at Google Antigravity. And let's start with the basics. Um, and

**[01:28]** And let's start with the basics. Um, and

**[01:28]** And let's start with the basics. Um, and first just to get a sense of the room.

**[01:29]** first just to get a sense of the room.

**[01:29]** first just to get a sense of the room. Um, who has used anti-gravity?

**[01:33]** Um, who has used anti-gravity?

**[01:33]** Um, who has used anti-gravity? All right, there you go. Power of

**[01:34]** All right, there you go. Power of

**[01:34]** All right, there you go. Power of Google. Love it. Um, who's used the

**[01:37]** Google. Love it. Um, who's used the

**[01:37]** Google. Love it. Um, who's used the agent manager?

**[01:39]** agent manager?

**[01:40]** agent manager? Cool. Nice. Good. Good. All right. So,

**[01:42]** Cool. Nice. Good. Good. All right. So,

**[01:42]** Cool. Nice. Good. Good. All right. So, basics of anti-gravity.

**[01:45]** basics of anti-gravity.

**[01:45]** basics of anti-gravity. Anti-gravity, notably anti-gravity, not

**[01:47]** Anti-gravity, notably anti-gravity, not

**[01:47]** Anti-gravity, notably anti-gravity, not anti-gravity. Anti-gravity. It's an AI

**[01:49]** anti-gravity. Anti-gravity. It's an AI

**[01:49]** anti-gravity. Anti-gravity. It's an AI developer platform with three surfaces.

**[01:51]** developer platform with three surfaces.

**[01:51]** developer platform with three surfaces. The first one is an editor. The second

**[01:54]** The first one is an editor. The second

**[01:54]** The first one is an editor. The second one is a browser and the third one is

**[01:57]** one is a browser and the third one is

**[01:57]** one is a browser and the third one is the agent manager. So we'll dive into

**[01:59]** the agent manager. So we'll dive into

**[01:59]** the agent manager. So we'll dive into what this means, which one what what


### [02:00 - 03:00]

**[02:01]** what this means, which one what what

**[02:01]** what this means, which one what what each looks like. So a paradigm shift

**[02:04]** each looks like. So a paradigm shift

**[02:04]** each looks like. So a paradigm shift here is that agents are now living

**[02:07]** here is that agents are now living

**[02:07]** here is that agents are now living outside of your IDE and they can

**[02:08]** outside of your IDE and they can

**[02:08]** outside of your IDE and they can interact across many different surfaces

**[02:10]** interact across many different surfaces

**[02:10]** interact across many different surfaces that your agent or that you as a

**[02:12]** that your agent or that you as a

**[02:12]** that your agent or that you as a software developer might spend time in.

**[02:14]** software developer might spend time in.

**[02:14]** software developer might spend time in. And let's start with the agent manager.

**[02:15]** And let's start with the agent manager.

**[02:15]** And let's start with the agent manager. So that's the thing up top. This is your

**[02:17]** So that's the thing up top. This is your

**[02:17]** So that's the thing up top. This is your central hub. It's an agent first view

**[02:20]** central hub. It's an agent first view

**[02:20]** central hub. It's an agent first view and it pulls you one level higher than

**[02:22]** and it pulls you one level higher than

**[02:22]** and it pulls you one level higher than just looking at your code. So instead of

**[02:24]** just looking at your code. So instead of

**[02:24]** just looking at your code. So instead of looking at diffs, you'll be kind of a

**[02:27]** looking at diffs, you'll be kind of a

**[02:27]** looking at diffs, you'll be kind of a little bit further back. And at any

**[02:29]** little bit further back. And at any

**[02:29]** little bit further back. And at any given time, there is one agent manager

**[02:31]** given time, there is one agent manager

**[02:31]** given time, there is one agent manager window.

**[02:32]** window.

**[02:32]** window. Now you have an AI editor. This is

**[02:34]** Now you have an AI editor. This is

**[02:34]** Now you have an AI editor. This is probably what you've grown to love and

**[02:36]** probably what you've grown to love and

**[02:36]** probably what you've grown to love and expect. Has all the bells and whistles

**[02:38]** expect. Has all the bells and whistles

**[02:38]** expect. Has all the bells and whistles that you would expect. Uh lightning fast

**[02:40]** that you would expect. Uh lightning fast

**[02:40]** that you would expect. Uh lightning fast autocomplete. This is the part where you

**[02:42]** autocomplete. This is the part where you

**[02:42]** autocomplete. This is the part where you can make your memes about yes, we forked

**[02:43]** can make your memes about yes, we forked

**[02:43]** can make your memes about yes, we forked VS Code. And it has an agent sidebar.

**[02:46]** VS Code. And it has an agent sidebar.

**[02:46]** VS Code. And it has an agent sidebar. And this is the sort of thing it's

**[02:47]** And this is the sort of thing it's

**[02:47]** And this is the sort of thing it's mirrored with the agent manager. And

**[02:49]** mirrored with the agent manager. And

**[02:49]** mirrored with the agent manager. And this is when you need to dive into your

**[02:51]** this is when you need to dive into your

**[02:51]** this is when you need to dive into your editor to accomplish maybe your 80% to

**[02:53]** editor to accomplish maybe your 80% to

**[02:53]** editor to accomplish maybe your 80% to 100% of your task. And at any point, we

**[02:56]** 100% of your task. And at any point, we

**[02:56]** 100% of your task. And at any point, we made it very very easy because we

**[02:57]** made it very very easy because we

**[02:57]** made it very very easy because we recognize not everything can be done

**[02:58]** recognize not everything can be done

**[02:58]** recognize not everything can be done purely with an agent for you to command


### [03:00 - 04:00]

**[03:01]** purely with an agent for you to command

**[03:01]** purely with an agent for you to command E or control E and hop instantly from

**[03:04]** E or control E and hop instantly from

**[03:04]** E or control E and hop instantly from the editor into the agent manager and

**[03:06]** the editor into the agent manager and

**[03:06]** the editor into the agent manager and vice versa. And this takes on under 100

**[03:09]** vice versa. And this takes on under 100

**[03:09]** vice versa. And this takes on under 100 milliseconds. It's zippy. And then

**[03:11]** milliseconds. It's zippy. And then

**[03:11]** milliseconds. It's zippy. And then finally, something that I love, an agent

**[03:14]** finally, something that I love, an agent

**[03:14]** finally, something that I love, an agent controlled browser. This is really,

**[03:15]** controlled browser. This is really,

**[03:15]** controlled browser. This is really, really cool. And hopefully for the folks

**[03:17]** really cool. And hopefully for the folks

**[03:17]** really cool. And hopefully for the folks in the room that have tried

**[03:18]** in the room that have tried

**[03:18]** in the room that have tried anti-gravity, you've noticed some of the

**[03:19]** anti-gravity, you've noticed some of the

**[03:19]** anti-gravity, you've noticed some of the magic that we've put in behind here. So,

**[03:22]** magic that we've put in behind here. So,

**[03:22]** magic that we've put in behind here. So, we have an agent controlled Chrome

**[03:24]** we have an agent controlled Chrome

**[03:24]** we have an agent controlled Chrome browser. And this gives the agent access

**[03:26]** browser. And this gives the agent access

**[03:26]** browser. And this gives the agent access to the richness of the web. And I mean

**[03:28]** to the richness of the web. And I mean

**[03:28]** to the richness of the web. And I mean that in two ways. The first one, context

**[03:31]** that in two ways. The first one, context

**[03:31]** that in two ways. The first one, context retrieval, right? It has the same

**[03:32]** retrieval, right? It has the same

**[03:32]** retrieval, right? It has the same authentication that you would in your

**[03:33]** authentication that you would in your

**[03:34]** authentication that you would in your normal Chrome. You can give it access to

**[03:35]** normal Chrome. You can give it access to

**[03:35]** normal Chrome. You can give it access to your Google Docs. You can give it access

**[03:37]** your Google Docs. You can give it access

**[03:37]** your Google Docs. You can give it access to, you know, your GitHub dashboards and

**[03:39]** to, you know, your GitHub dashboards and

**[03:39]** to, you know, your GitHub dashboards and things like that and interact with a

**[03:40]** things like that and interact with a

**[03:40]** things like that and interact with a browser like you would as an engineer.

**[03:43]** browser like you would as an engineer.

**[03:43]** browser like you would as an engineer. But also what you're seeing on the

**[03:44]** But also what you're seeing on the

**[03:44]** But also what you're seeing on the screen is that it lets you it lets the

**[03:46]** screen is that it lets you it lets the

**[03:46]** screen is that it lets you it lets the agent take control of your browser,

**[03:48]** agent take control of your browser,

**[03:48]** agent take control of your browser, click and scroll and run JavaScript and

**[03:51]** click and scroll and run JavaScript and

**[03:51]** click and scroll and run JavaScript and do all the things that you would do to

**[03:52]** do all the things that you would do to

**[03:52]** do all the things that you would do to test your apps. So here I put together

**[03:55]** test your apps. So here I put together

**[03:55]** test your apps. So here I put together this like random artwork generator. All

**[03:57]** this like random artwork generator. All

**[03:57]** this like random artwork generator. All you do is refresh and you get a new

**[03:58]** you do is refresh and you get a new

**[03:58]** you do is refresh and you get a new picture of um like a Thomas piece of


### [04:00 - 05:00]

**[04:01]** picture of um like a Thomas piece of

**[04:01]** picture of um like a Thomas piece of Thomas Cole artwork. And now we added in

**[04:03]** Thomas Cole artwork. And now we added in

**[04:03]** Thomas Cole artwork. And now we added in a new feature which is this little

**[04:04]** a new feature which is this little

**[04:04]** a new feature which is this little little modal card. and the agent

**[04:06]** little modal card. and the agent

**[04:06]** little modal card. and the agent actually went out and said, "Okay, I

**[04:07]** actually went out and said, "Okay, I

**[04:07]** actually went out and said, "Okay, I made all the code, but instead of

**[04:09]** made all the code, but instead of

**[04:09]** made all the code, but instead of showing you a diff of what I did, let's

**[04:11]** showing you a diff of what I did, let's

**[04:11]** showing you a diff of what I did, let's instead show you a recording of Chrome."

**[04:13]** instead show you a recording of Chrome."

**[04:13]** instead show you a recording of Chrome." So, this is a recording of Chrome where

**[04:15]** So, this is a recording of Chrome where

**[04:15]** So, this is a recording of Chrome where the blue circle is the mouse. It's

**[04:17]** the blue circle is the mouse. It's

**[04:17]** the blue circle is the mouse. It's moving around the screen, and in this

**[04:18]** moving around the screen, and in this

**[04:18]** moving around the screen, and in this way, you get verifiable results. So,

**[04:21]** way, you get verifiable results. So,

**[04:21]** way, you get verifiable results. So, this is what we're very excited about

**[04:22]** this is what we're very excited about

**[04:22]** this is what we're very excited about our uh our Chrome browser. And then the

**[04:25]** our uh our Chrome browser. And then the

**[04:25]** our uh our Chrome browser. And then the agent manager can serve as your control

**[04:27]** agent manager can serve as your control

**[04:27]** agent manager can serve as your control panel. The editor and the browser are

**[04:29]** panel. The editor and the browser are

**[04:29]** panel. The editor and the browser are tools for your agent. And we want you to

**[04:32]** tools for your agent. And we want you to

**[04:32]** tools for your agent. And we want you to spend time in the agent manager. And as

**[04:34]** spend time in the agent manager. And as

**[04:34]** spend time in the agent manager. And as models get better and better, I bet you

**[04:36]** models get better and better, I bet you

**[04:36]** models get better and better, I bet you you're going to be spending more and

**[04:37]** you're going to be spending more and

**[04:37]** you're going to be spending more and more time inside of this agent manager.

**[04:39]** more time inside of this agent manager.

**[04:39]** more time inside of this agent manager. And it has an inbox, and I'll talk a

**[04:41]** And it has an inbox, and I'll talk a

**[04:41]** And it has an inbox, and I'll talk a little bit about this and sort of why we

**[04:43]** little bit about this and sort of why we

**[04:43]** little bit about this and sort of why we did this, but it lets you manage many

**[04:46]** did this, but it lets you manage many

**[04:46]** did this, but it lets you manage many agents at once. So you can have things

**[04:49]** agents at once. So you can have things

**[04:49]** agents at once. So you can have things that require your attention. For

**[04:50]** that require your attention. For

**[04:50]** that require your attention. For example, running terminal commands. We

**[04:52]** example, running terminal commands. We

**[04:52]** example, running terminal commands. We don't want it to just kind of go off and

**[04:53]** don't want it to just kind of go off and

**[04:53]** don't want it to just kind of go off and just run every terminal command. There

**[04:54]** just run every terminal command. There

**[04:54]** just run every terminal command. There are probably some commands that you want

**[04:55]** are probably some commands that you want

**[04:55]** are probably some commands that you want to make sure you you hit okay on. So

**[04:57]** to make sure you you hit okay on. So

**[04:57]** to make sure you you hit okay on. So things like this will get surfaced

**[04:58]** things like this will get surfaced

**[04:58]** things like this will get surfaced inside of this inbox. One click, you can


### [05:00 - 06:00]

**[05:00]** inside of this inbox. One click, you can

**[05:00]** inside of this inbox. One click, you can manage many different things happening

**[05:01]** manage many different things happening

**[05:01]** manage many different things happening at once.

**[05:03]** at once.

**[05:03]** at once. And it has a wonderful OS level

**[05:05]** And it has a wonderful OS level

**[05:05]** And it has a wonderful OS level notification. So if there is something

**[05:06]** notification. So if there is something

**[05:06]** notification. So if there is something that you need, it will sort of let you

**[05:08]** that you need, it will sort of let you

**[05:08]** that you need, it will sort of let you know. And this kind of solves that

**[05:09]** know. And this kind of solves that

**[05:09]** know. And this kind of solves that problem of multi-threading across many

**[05:12]** problem of multi-threading across many

**[05:12]** problem of multi-threading across many tasks at once. And so our team is

**[05:14]** tasks at once. And so our team is

**[05:14]** tasks at once. And so our team is thrilled to launch this brand new

**[05:15]** thrilled to launch this brand new

**[05:16]** thrilled to launch this brand new product. It's a brand new product

**[05:18]** product. It's a brand new product

**[05:18]** product. It's a brand new product paradigm. And we did so in conjunction

**[05:19]** paradigm. And we did so in conjunction

**[05:19]** paradigm. And we did so in conjunction with Gemini 3, which was a very exciting

**[05:21]** with Gemini 3, which was a very exciting

**[05:21]** with Gemini 3, which was a very exciting week for the team. But alas, we ran out

**[05:25]** week for the team. But alas, we ran out

**[05:25]** week for the team. But alas, we ran out of capacity.

**[05:26]** of capacity.

**[05:26]** of capacity. [laughter]

**[05:27]** [laughter]

**[05:27]** [laughter] Um, this has been tormenting me the last

**[05:29]** Um, this has been tormenting me the last

**[05:29]** Um, this has been tormenting me the last couple of days. And so I apologize. On

**[05:31]** couple of days. And so I apologize. On

**[05:31]** couple of days. And so I apologize. On behalf of the anti-gravity team, I'd

**[05:33]** behalf of the anti-gravity team, I'd

**[05:33]** behalf of the anti-gravity team, I'd like to apologize for our global chip

**[05:34]** like to apologize for our global chip

**[05:34]** like to apologize for our global chip shortage. Um, we're working around the

**[05:36]** shortage. Um, we're working around the

**[05:36]** shortage. Um, we're working around the clock to try and make this work for you.

**[05:37]** clock to try and make this work for you.

**[05:37]** clock to try and make this work for you. Uh, hopefully we'll have a few less of

**[05:39]** Uh, hopefully we'll have a few less of

**[05:39]** Uh, hopefully we'll have a few less of these sorts of errors. Um, but we, it's

**[05:41]** these sorts of errors. Um, but we, it's

**[05:41]** these sorts of errors. Um, but we, it's what's been really exciting is people

**[05:43]** what's been really exciting is people

**[05:43]** what's been really exciting is people who have used the product have seen what

**[05:45]** who have used the product have seen what

**[05:45]** who have used the product have seen what the magic of combining these three

**[05:46]** the magic of combining these three

**[05:46]** the magic of combining these three surfaces can do for your workflows, for

**[05:48]** surfaces can do for your workflows, for

**[05:48]** surfaces can do for your workflows, for your software development. Um, so let's

**[05:50]** your software development. Um, so let's

**[05:50]** your software development. Um, so let's talk about it. Why did we build the

**[05:53]** talk about it. Why did we build the

**[05:53]** talk about it. Why did we build the product? How did we arrive at this sort

**[05:55]** product? How did we arrive at this sort

**[05:55]** product? How did we arrive at this sort of conclusion? You might say, "Oh,

**[05:57]** of conclusion? You might say, "Oh,

**[05:57]** of conclusion? You might say, "Oh, adding in a new window, it's pretty

**[05:58]** adding in a new window, it's pretty

**[05:58]** adding in a new window, it's pretty pretty random, right? It's this one to

**[05:59]** pretty random, right? It's this one to

**[05:59]** pretty random, right? It's this one to many relationship between the agent


### [06:00 - 07:00]

**[06:01]** many relationship between the agent

**[06:01]** many relationship between the agent manager and many other surfaces.

**[06:04]** manager and many other surfaces.

**[06:04]** manager and many other surfaces. Um, and it's important to remember I've

**[06:06]** Um, and it's important to remember I've

**[06:06]** Um, and it's important to remember I've I've been at this conference a couple of

**[06:07]** I've been at this conference a couple of

**[06:07]** I've been at this conference a couple of times and and everything every single

**[06:09]** times and and everything every single

**[06:09]** times and and everything every single time there is this theme. The product is

**[06:11]** time there is this theme. The product is

**[06:11]** time there is this theme. The product is only ever as good as the models that

**[06:13]** only ever as good as the models that

**[06:13]** only ever as good as the models that power it. And this is very important for

**[06:15]** power it. And this is very important for

**[06:15]** power it. And this is very important for us as builders, right? Every year there

**[06:17]** us as builders, right? Every year there

**[06:17]** us as builders, right? Every year there is this sort of new step function. The

**[06:19]** is this sort of new step function. The

**[06:19]** is this sort of new step function. The first there was a year when it was

**[06:21]** first there was a year when it was

**[06:21]** first there was a year when it was autocomplete, right? Copilot. And this

**[06:23]** autocomplete, right? Copilot. And this

**[06:23]** autocomplete, right? Copilot. And this this sort of thing was only enabled

**[06:24]** this sort of thing was only enabled

**[06:24]** this sort of thing was only enabled because models suddenly got good at

**[06:26]** because models suddenly got good at

**[06:26]** because models suddenly got good at doing this short form autocomplete. And

**[06:28]** doing this short form autocomplete. And

**[06:28]** doing this short form autocomplete. And then we had chat. We had chat with RHF.

**[06:30]** then we had chat. We had chat with RHF.

**[06:30]** then we had chat. We had chat with RHF. Then we had agents. So you can see how

**[06:32]** Then we had agents. So you can see how

**[06:32]** Then we had agents. So you can see how every single one of these product

**[06:33]** every single one of these product

**[06:33]** every single one of these product paradigms is sort of motivated by some

**[06:35]** paradigms is sort of motivated by some

**[06:35]** paradigms is sort of motivated by some change that happens with model

**[06:36]** change that happens with model

**[06:36]** change that happens with model capabilities. And it's a blessing that

**[06:39]** capabilities. And it's a blessing that

**[06:39]** capabilities. And it's a blessing that our team is able to work and be embedded

**[06:41]** our team is able to work and be embedded

**[06:41]** our team is able to work and be embedded inside of DeepMind. We had access to

**[06:43]** inside of DeepMind. We had access to

**[06:44]** inside of DeepMind. We had access to Gemini for a couple of months um earlier

**[06:45]** Gemini for a couple of months um earlier

**[06:46]** Gemini for a couple of months um earlier and we were able to work with the

**[06:47]** and we were able to work with the

**[06:47]** and we were able to work with the research team to basically figure out

**[06:48]** research team to basically figure out

**[06:48]** research team to basically figure out you know what are the strengths that we

**[06:50]** you know what are the strengths that we

**[06:50]** you know what are the strengths that we want to show off in our product. what

**[06:51]** want to show off in our product. what

**[06:51]** want to show off in our product. what are the things that we can exploit and

**[06:52]** are the things that we can exploit and

**[06:52]** are the things that we can exploit and then also what are the gaps right this

**[06:54]** then also what are the gaps right this

**[06:54]** then also what are the gaps right this desired experience where are the gaps in

**[06:57]** desired experience where are the gaps in

**[06:57]** desired experience where are the gaps in the model and and how can we fix that

**[06:59]** the model and and how can we fix that

**[06:59]** the model and and how can we fix that right and so this is this was a very


### [07:00 - 08:00]

**[07:01]** right and so this is this was a very

**[07:01]** right and so this is this was a very very powerful part of why anti-gravity

**[07:03]** very powerful part of why anti-gravity

**[07:03]** very powerful part of why anti-gravity came to be and there are four main

**[07:05]** came to be and there are four main

**[07:05]** came to be and there are four main categories of improvements powered by a

**[07:07]** categories of improvements powered by a

**[07:07]** categories of improvements powered by a little nano banana artwork the first one

**[07:10]** little nano banana artwork the first one

**[07:10]** little nano banana artwork the first one is intelligence and reasoning you all

**[07:12]** is intelligence and reasoning you all

**[07:12]** is intelligence and reasoning you all are probably familiar with this you use

**[07:13]** are probably familiar with this you use

**[07:13]** are probably familiar with this you use nano or you used um Gemini 3 and you

**[07:16]** nano or you used um Gemini 3 and you

**[07:16]** nano or you used um Gemini 3 and you probably thought it was a smarter model

**[07:17]** probably thought it was a smarter model

**[07:17]** probably thought it was a smarter model this is good it's better at instruction

**[07:19]** this is good it's better at instruction

**[07:19]** this is good it's better at instruction following it's better at using tools.

**[07:21]** following it's better at using tools.

**[07:21]** following it's better at using tools. There's more nuance in the tool use. You

**[07:22]** There's more nuance in the tool use. You

**[07:22]** There's more nuance in the tool use. You can afford things like, you know,

**[07:24]** can afford things like, you know,

**[07:24]** can afford things like, you know, there's a browser now. There's a million

**[07:25]** there's a browser now. There's a million

**[07:25]** there's a browser now. There's a million things that you could do in a browser.

**[07:26]** things that you could do in a browser.

**[07:26]** things that you could do in a browser. It can literally even execute

**[07:28]** It can literally even execute

**[07:28]** It can literally even execute JavaScript. How do you get an agent to

**[07:29]** JavaScript. How do you get an agent to

**[07:30]** JavaScript. How do you get an agent to understand the nuance of all these

**[07:31]** understand the nuance of all these

**[07:31]** understand the nuance of all these tools? It can do longer [clears throat]

**[07:33]** tools? It can do longer [clears throat]

**[07:33]** tools? It can do longer [clears throat] running tasks. These things now take a

**[07:35]** running tasks. These things now take a

**[07:35]** running tasks. These things now take a bit longer, right? And so you can afford

**[07:37]** bit longer, right? And so you can afford

**[07:37]** bit longer, right? And so you can afford to run these things in the background.

**[07:39]** to run these things in the background.

**[07:39]** to run these things in the background. It thinks for longer. Just time has

**[07:41]** It thinks for longer. Just time has

**[07:41]** It thinks for longer. Just time has gotten stretched out. And then

**[07:43]** gotten stretched out. And then

**[07:43]** gotten stretched out. And then multimodal. I really love this property

**[07:45]** multimodal. I really love this property

**[07:45]** multimodal. I really love this property of what Google has been up to. the

**[07:47]** of what Google has been up to. the

**[07:47]** of what Google has been up to. the multimodal functionality of Gemini 3 is

**[07:49]** multimodal functionality of Gemini 3 is

**[07:49]** multimodal functionality of Gemini 3 is off the charts and you start combining

**[07:51]** off the charts and you start combining

**[07:51]** off the charts and you start combining it with all these other models like Nano

**[07:53]** it with all these other models like Nano

**[07:53]** it with all these other models like Nano Banana Pro um and you really get

**[07:55]** Banana Pro um and you really get

**[07:55]** Banana Pro um and you really get something magical. So we have these

**[07:56]** something magical. So we have these

**[07:56]** something magical. So we have these roughly four different categories where

**[07:58]** roughly four different categories where

**[07:58]** roughly four different categories where things have gotten much better


### [08:00 - 09:00]

**[08:01]** things have gotten much better

**[08:01]** things have gotten much better and if you think about these properties

**[08:02]** and if you think about these properties

**[08:02]** and if you think about these properties the question becomes what do we do about

**[08:04]** the question becomes what do we do about

**[08:04]** the question becomes what do we do about these differences and from a product

**[08:07]** these differences and from a product

**[08:07]** these differences and from a product perspective it's like how do you

**[08:08]** perspective it's like how do you

**[08:08]** perspective it's like how do you construct a product that can take

**[08:09]** construct a product that can take

**[08:09]** construct a product that can take advantage of this new wave and hopefully

**[08:11]** advantage of this new wave and hopefully

**[08:11]** advantage of this new wave and hopefully and in my opinion this is the next step

**[08:13]** and in my opinion this is the next step

**[08:13]** and in my opinion this is the next step function autocomplete chat agents and

**[08:16]** function autocomplete chat agents and

**[08:16]** function autocomplete chat agents and then I probably got to come up with

**[08:18]** then I probably got to come up with

**[08:18]** then I probably got to come up with something more interesting than whatever

**[08:19]** something more interesting than whatever

**[08:19]** something more interesting than whatever this thing is called.

**[08:21]** this thing is called.

**[08:22]** this thing is called. So step one is we want to raise the

**[08:24]** So step one is we want to raise the

**[08:24]** So step one is we want to raise the ceiling of capability.

**[08:26]** ceiling of capability.

**[08:26]** ceiling of capability. We want to aim higher, have higher

**[08:27]** We want to aim higher, have higher

**[08:27]** We want to aim higher, have higher ambition.

**[08:30]** ambition.

**[08:30]** ambition. And so a lot of the teams at DeepMind

**[08:33]** And so a lot of the teams at DeepMind

**[08:33]** And so a lot of the teams at DeepMind were working on all sorts of cutting

**[08:34]** were working on all sorts of cutting

**[08:34]** were working on all sorts of cutting edge research, right? There's Google is

**[08:37]** edge research, right? There's Google is

**[08:37]** edge research, right? There's Google is a big big company. And one of my

**[08:38]** a big big company. And one of my

**[08:38]** a big big company. And one of my learnings going from a startup to one of

**[08:40]** learnings going from a startup to one of

**[08:40]** learnings going from a startup to one of these bigger companies is that there is

**[08:41]** these bigger companies is that there is

**[08:41]** these bigger companies is that there is a team of people that is attacking a

**[08:43]** a team of people that is attacking a

**[08:43]** a team of people that is attacking a very very hard technical problem. And as

**[08:45]** very very hard technical problem. And as

**[08:45]** very very hard technical problem. And as a nerd, this is super exciting, right?

**[08:47]** a nerd, this is super exciting, right?

**[08:47]** a nerd, this is super exciting, right? And then as a product person it's like

**[08:48]** And then as a product person it's like

**[08:48]** And then as a product person it's like wow we can start using computer use. So

**[08:52]** wow we can start using computer use. So

**[08:52]** wow we can start using computer use. So browser use has been one of these huge

**[08:54]** browser use has been one of these huge

**[08:54]** browser use has been one of these huge unlocks.

**[08:57]** unlocks.

**[08:57]** unlocks. And this is twofold right I mentioned

**[08:58]** And this is twofold right I mentioned

**[08:58]** And this is twofold right I mentioned the sort of retrieval aspect of things.


### [09:00 - 10:00]

**[09:02]** the sort of retrieval aspect of things.

**[09:02]** the sort of retrieval aspect of things. Um

**[09:04]** Um

**[09:04]** Um I guess for for software engineers there

**[09:05]** I guess for for software engineers there

**[09:05]** I guess for for software engineers there is much more that happens that is beyond

**[09:07]** is much more that happens that is beyond

**[09:07]** is much more that happens that is beyond the code right you can roughly think

**[09:08]** the code right you can roughly think

**[09:08]** the code right you can roughly think about it as there's what to build

**[09:10]** about it as there's what to build

**[09:10]** about it as there's what to build there's how to build it and then you

**[09:11]** there's how to build it and then you

**[09:12]** there's how to build it and then you actually have to build it. I would say

**[09:13]** actually have to build it. I would say

**[09:13]** actually have to build it. I would say building it has become more or less you

**[09:16]** building it has become more or less you

**[09:16]** building it has become more or less you know it's reasonable for the model to

**[09:17]** know it's reasonable for the model to

**[09:17]** know it's reasonable for the model to now given context it can generate the

**[09:18]** now given context it can generate the

**[09:18]** now given context it can generate the code that hopefully functionally works

**[09:21]** code that hopefully functionally works

**[09:21]** code that hopefully functionally works and then you've got the what to build

**[09:22]** and then you've got the what to build

**[09:22]** and then you've got the what to build this is the part that is up to you kind

**[09:24]** this is the part that is up to you kind

**[09:24]** this is the part that is up to you kind of human imagination and then there's

**[09:26]** of human imagination and then there's

**[09:26]** of human imagination and then there's the how to build it right and there's

**[09:27]** the how to build it right and there's

**[09:27]** the how to build it right and there's this richness in context the richness

**[09:29]** this richness in context the richness

**[09:29]** this richness in context the richness and institutional knowledge and these

**[09:30]** and institutional knowledge and these

**[09:30]** and institutional knowledge and these are the sorts of things that having

**[09:33]** are the sorts of things that having

**[09:33]** are the sorts of things that having access to a browser having access to

**[09:34]** access to a browser having access to

**[09:34]** access to a browser having access to your bug dashboards having access to

**[09:36]** your bug dashboards having access to

**[09:36]** your bug dashboards having access to your experiments all these sorts of

**[09:38]** your experiments all these sorts of

**[09:38]** your experiments all these sorts of things that now gives the agent this

**[09:40]** things that now gives the agent this

**[09:40]** things that now gives the agent this additional level of context and maybe I

**[09:42]** additional level of context and maybe I

**[09:42]** additional level of context and maybe I should have clicked before, but if you

**[09:43]** should have clicked before, but if you

**[09:43]** should have clicked before, but if you saw on the screen, let's see, how do I

**[09:45]** saw on the screen, let's see, how do I

**[09:45]** saw on the screen, let's see, how do I do this?

**[09:46]** do this?

**[09:46]** do this? So, this is now the other side of

**[09:48]** So, this is now the other side of

**[09:48]** So, this is now the other side of things. Browser is verification. So, you

**[09:50]** things. Browser is verification. So, you

**[09:50]** things. Browser is verification. So, you might have seen this video, this is a

**[09:51]** might have seen this video, this is a

**[09:51]** might have seen this video, this is a tutorial video that we put together on

**[09:52]** tutorial video that we put together on

**[09:52]** tutorial video that we put together on just how to use it. But this is the

**[09:54]** just how to use it. But this is the

**[09:54]** just how to use it. But this is the agent. The blue border indicates that

**[09:56]** agent. The blue border indicates that

**[09:56]** agent. The blue border indicates that it's being in control by the agent. And

**[09:58]** it's being in control by the agent. And

**[09:58]** it's being in control by the agent. And so, this is a flight tracker. You put

**[09:59]** so, this is a flight tracker. You put

**[09:59]** so, this is a flight tracker. You put in, you know, a flight ID and then it'll


### [10:00 - 11:00]

**[10:01]** in, you know, a flight ID and then it'll

**[10:01]** in, you know, a flight ID and then it'll give you sort of the start and end of of

**[10:03]** give you sort of the start and end of of

**[10:03]** give you sort of the start and end of of that flight. And this is being done

**[10:04]** that flight. And this is being done

**[10:04]** that flight. And this is being done entirely by a Gemini computer use

**[10:07]** entirely by a Gemini computer use

**[10:07]** entirely by a Gemini computer use variant. So it can click, it can scroll,

**[10:10]** variant. So it can click, it can scroll,

**[10:10]** variant. So it can click, it can scroll, it can retrieve the DOM, it can do all

**[10:12]** it can retrieve the DOM, it can do all

**[10:12]** it can retrieve the DOM, it can do all the things. And then what's really cool

**[10:13]** the things. And then what's really cool

**[10:13]** the things. And then what's really cool is you end up with not just a diff, you

**[10:16]** is you end up with not just a diff, you

**[10:16]** is you end up with not just a diff, you end up with a screen recording of what

**[10:18]** end up with a screen recording of what

**[10:18]** end up with a screen recording of what it did. So it's changed the game. And

**[10:19]** it did. So it's changed the game. And

**[10:20]** it did. So it's changed the game. And the model can take this and because it

**[10:21]** the model can take this and because it

**[10:21]** the model can take this and because it has the ability to understand images, it

**[10:24]** has the ability to understand images, it

**[10:24]** has the ability to understand images, it can take this and iterate from there. So

**[10:26]** can take this and iterate from there. So

**[10:26]** can take this and iterate from there. So that was the first category, browser

**[10:27]** that was the first category, browser

**[10:27]** that was the first category, browser use, just an insane, insane magical

**[10:29]** use, just an insane, insane magical

**[10:29]** use, just an insane, insane magical experience. Now the second place that we

**[10:32]** experience. Now the second place that we

**[10:32]** experience. Now the second place that we wanted to spend time is on image

**[10:33]** wanted to spend time is on image

**[10:33]** wanted to spend time is on image generation. And we noticed this theme

**[10:35]** generation. And we noticed this theme

**[10:35]** generation. And we noticed this theme when we, you know, when I when I first

**[10:36]** when we, you know, when I when I first

**[10:36]** when we, you know, when I when I first started at at Google, we noticed, okay,

**[10:38]** started at at Google, we noticed, okay,

**[10:38]** started at at Google, we noticed, okay, Gemini is spending a lot of time on

**[10:39]** Gemini is spending a lot of time on

**[10:39]** Gemini is spending a lot of time on multimodal. And this is really great for

**[10:42]** multimodal. And this is really great for

**[10:42]** multimodal. And this is really great for consumer use cases, right? Nano Banana 2

**[10:43]** consumer use cases, right? Nano Banana 2

**[10:43]** consumer use cases, right? Nano Banana 2 was was mindboggling. Um, but also for

**[10:46]** was was mindboggling. Um, but also for

**[10:46]** was was mindboggling. Um, but also for devs. Devs are inherently this is a

**[10:49]** devs. Devs are inherently this is a

**[10:49]** devs. Devs are inherently this is a multimodal experience. You're not just

**[10:51]** multimodal experience. You're not just

**[10:51]** multimodal experience. You're not just looking at text. You're looking at the

**[10:52]** looking at text. You're looking at the

**[10:52]** looking at text. You're looking at the output of websites. You're looking at

**[10:53]** output of websites. You're looking at

**[10:53]** output of websites. You're looking at architecture diagrams. There's so much

**[10:55]** architecture diagrams. There's so much

**[10:55]** architecture diagrams. There's so much more to coding than just text. And so

**[10:59]** more to coding than just text. And so

**[10:59]** more to coding than just text. And so there's image understanding. This is


### [11:00 - 12:00]

**[11:01]** there's image understanding. This is

**[11:01]** there's image understanding. This is verifying screenshots, verifying

**[11:03]** verifying screenshots, verifying

**[11:03]** verifying screenshots, verifying recordings, all these sorts of things.

**[11:05]** recordings, all these sorts of things.

**[11:05]** recordings, all these sorts of things. And then the beautiful part about Google

**[11:06]** And then the beautiful part about Google

**[11:06]** And then the beautiful part about Google is that you have this synergistic

**[11:08]** is that you have this synergistic

**[11:08]** is that you have this synergistic nature. This product takes into account

**[11:09]** nature. This product takes into account

**[11:09]** nature. This product takes into account not just Gemini 3 Pro, but also takes

**[11:12]** not just Gemini 3 Pro, but also takes

**[11:12]** not just Gemini 3 Pro, but also takes into account the image side of things.

**[11:14]** into account the image side of things.

**[11:14]** into account the image side of things. And so here I want to give you a quick

**[11:15]** And so here I want to give you a quick

**[11:15]** And so here I want to give you a quick demo of um mockups. So I have a hunch

**[11:19]** demo of um mockups. So I have a hunch

**[11:19]** demo of um mockups. So I have a hunch and you all probably believe this too.

**[11:20]** and you all probably believe this too.

**[11:20]** and you all probably believe this too. Design is going to change, right? You're

**[11:24]** Design is going to change, right? You're

**[11:24]** Design is going to change, right? You're going to spend, you know, maybe some

**[11:25]** going to spend, you know, maybe some

**[11:25]** going to spend, you know, maybe some time iterating with an agent to to

**[11:26]** time iterating with an agent to to

**[11:26]** time iterating with an agent to to arrive at a mockup. But for something

**[11:28]** arrive at a mockup. But for something

**[11:28]** arrive at a mockup. But for something like, oh, let's build this website. we

**[11:30]** like, oh, let's build this website. we

**[11:30]** like, oh, let's build this website. we can start in image space. And what's

**[11:32]** can start in image space. And what's

**[11:32]** can start in image space. And what's really cool about image space is it lets

**[11:33]** really cool about image space is it lets

**[11:33]** really cool about image space is it lets you do really cool things like this. We

**[11:35]** you do really cool things like this. We

**[11:35]** you do really cool things like this. We can add comments. And so you end up

**[11:37]** can add comments. And so you end up

**[11:37]** can add comments. And so you end up commenting and leaving a bunch of a

**[11:39]** commenting and leaving a bunch of a

**[11:39]** commenting and leaving a bunch of a bunch of queued up responses. And it's

**[11:41]** bunch of queued up responses. And it's

**[11:41]** bunch of queued up responses. And it's kind of like GitHub. You'll just say,

**[11:42]** kind of like GitHub. You'll just say,

**[11:42]** kind of like GitHub. You'll just say, "All right, now update the design."

**[11:45]** "All right, now update the design."

**[11:45]** "All right, now update the design." And then it'll put it in here. The agent

**[11:47]** And then it'll put it in here. The agent

**[11:47]** And then it'll put it in here. The agent is smart enough to know when and how to

**[11:48]** is smart enough to know when and how to

**[11:48]** is smart enough to know when and how to apply those comments. And now we're

**[11:50]** apply those comments. And now we're

**[11:50]** apply those comments. And now we're iterating with the agent in image space.

**[11:52]** iterating with the agent in image space.

**[11:52]** iterating with the agent in image space. So really, really cool new capability.

**[11:54]** So really, really cool new capability.

**[11:54]** So really, really cool new capability. And what was awesome is that um we had

**[11:57]** And what was awesome is that um we had

**[11:57]** And what was awesome is that um we had Nano Banana Pro, you know, we pulled an

**[11:59]** Nano Banana Pro, you know, we pulled an

**[11:59]** Nano Banana Pro, you know, we pulled an allnighter for uh for the Gemini launch


### [12:00 - 13:00]

**[12:01]** allnighter for uh for the Gemini launch

**[12:01]** allnighter for uh for the Gemini launch because that was our first launch. Then

**[12:02]** because that was our first launch. Then

**[12:02]** because that was our first launch. Then they said, "Do it again. Do it on

**[12:04]** they said, "Do it again. Do it on

**[12:04]** they said, "Do it again. Do it on Thursday." So we made Gemini Pro um or

**[12:07]** Thursday." So we made Gemini Pro um or

**[12:07]** Thursday." So we made Gemini Pro um or I'm getting all these model names

**[12:08]** I'm getting all these model names

**[12:08]** I'm getting all these model names confused. The image Gen one, the Nano

**[12:10]** confused. The image Gen one, the Nano

**[12:10]** confused. The image Gen one, the Nano Banana one, we made that available on

**[12:11]** Banana one, we made that available on

**[12:11]** Banana one, we made that available on day one. I'm running on very little

**[12:13]** day one. I'm running on very little

**[12:13]** day one. I'm running on very little sleep on day one inside of the

**[12:15]** sleep on day one inside of the

**[12:15]** sleep on day one inside of the anti-gravity editor. And our hope is

**[12:17]** anti-gravity editor. And our hope is

**[12:17]** anti-gravity editor. And our hope is that the anti-gravity editor is this

**[12:18]** that the anti-gravity editor is this

**[12:18]** that the anti-gravity editor is this place where any sort of new capability

**[12:20]** place where any sort of new capability

**[12:20]** place where any sort of new capability can be represented inside of our

**[12:22]** can be represented inside of our

**[12:22]** can be represented inside of our product.

**[12:24]** product.

**[12:24]** product. And so step two was all right, we have

**[12:26]** And so step two was all right, we have

**[12:26]** And so step two was all right, we have this new capability. We've pushed the

**[12:27]** this new capability. We've pushed the

**[12:28]** this new capability. We've pushed the ceiling higher. Agents can do longer

**[12:29]** ceiling higher. Agents can do longer

**[12:30]** ceiling higher. Agents can do longer running tasks. They can do more

**[12:31]** running tasks. They can do more

**[12:31]** running tasks. They can do more complicated things. They can interact on

**[12:32]** complicated things. They can interact on

**[12:32]** complicated things. They can interact on other surfaces. And so this necessitates

**[12:35]** other surfaces. And so this necessitates

**[12:35]** other surfaces. And so this necessitates a new interaction pattern. And we're

**[12:37]** a new interaction pattern. And we're

**[12:37]** a new interaction pattern. And we're calling this artifacts.

**[12:40]** calling this artifacts.

**[12:40]** calling this artifacts. This is a new way to work with an agent.

**[12:43]** This is a new way to work with an agent.

**[12:43]** This is a new way to work with an agent. And this is one of my favorite parts

**[12:44]** And this is one of my favorite parts

**[12:44]** And this is one of my favorite parts about the product. And at its core is

**[12:46]** about the product. And at its core is

**[12:46]** about the product. And at its core is this agent manager.

**[12:48]** this agent manager.

**[12:48]** this agent manager. So let's start by defining an artifact.

**[12:51]** So let's start by defining an artifact.

**[12:51]** So let's start by defining an artifact. An artifact is a dynamic representation

**[12:54]** An artifact is a dynamic representation

**[12:54]** An artifact is a dynamic representation of something that the agent generates.

**[12:56]** of something that the agent generates.

**[12:56]** of something that the agent generates. Sorry, it's a an artifact is something

**[12:58]** Sorry, it's a an artifact is something

**[12:58]** Sorry, it's a an artifact is something that the agent generates that is a


### [13:00 - 14:00]

**[13:00]** that the agent generates that is a

**[13:00]** that the agent generates that is a dynamic representation of information

**[13:02]** dynamic representation of information

**[13:02]** dynamic representation of information for you and your use case. And the key

**[13:05]** for you and your use case. And the key

**[13:05]** for you and your use case. And the key here is that it's dynamic.

**[13:07]** here is that it's dynamic.

**[13:07]** here is that it's dynamic. Artifacts are used to keep the agent

**[13:09]** Artifacts are used to keep the agent

**[13:09]** Artifacts are used to keep the agent organized. They can use used for uh kind

**[13:11]** organized. They can use used for uh kind

**[13:11]** organized. They can use used for uh kind of like self-reflection and and

**[13:13]** of like self-reflection and and

**[13:13]** of like self-reflection and and self-organization. It can be used to

**[13:15]** self-organization. It can be used to

**[13:15]** self-organization. It can be used to communicate with the user to maybe give

**[13:17]** communicate with the user to maybe give

**[13:17]** communicate with the user to maybe give you a screenshot to maybe give you a

**[13:18]** you a screenshot to maybe give you a

**[13:18]** you a screenshot to maybe give you a screen recording like we described. And

**[13:20]** screen recording like we described. And

**[13:20]** screen recording like we described. And it can also be used across agents,

**[13:22]** it can also be used across agents,

**[13:22]** it can also be used across agents, whether this be with our browser sub

**[13:24]** whether this be with our browser sub

**[13:24]** whether this be with our browser sub agent or with other conversations or as

**[13:27]** agent or with other conversations or as

**[13:27]** agent or with other conversations or as memory. And this is what you see on the

**[13:29]** memory. And this is what you see on the

**[13:29]** memory. And this is what you see on the right side of this agent manager. We've

**[13:32]** right side of this agent manager. We've

**[13:32]** right side of this agent manager. We've dedicated sort of half the screen and

**[13:34]** dedicated sort of half the screen and

**[13:34]** dedicated sort of half the screen and and your sidebar to this concept of

**[13:36]** and your sidebar to this concept of

**[13:36]** and your sidebar to this concept of artifacts.

**[13:41]** And so we've all tried to follow along

**[13:41]** And so we've all tried to follow along chain of thought. And I would say this,

**[13:44]** chain of thought. And I would say this,

**[13:44]** chain of thought. And I would say this, you know, we did some fanciness here

**[13:45]** you know, we did some fanciness here

**[13:45]** you know, we did some fanciness here inside of the agent manager to make sure

**[13:47]** inside of the agent manager to make sure

**[13:47]** inside of the agent manager to make sure conversations are broken up into like

**[13:48]** conversations are broken up into like

**[13:48]** conversations are broken up into like chunks. So in theory, you could follow

**[13:50]** chunks. So in theory, you could follow

**[13:50]** chunks. So in theory, you could follow along a little bit better in the

**[13:51]** along a little bit better in the

**[13:51]** along a little bit better in the conversation view, but ultimately you're

**[13:53]** conversation view, but ultimately you're

**[13:53]** conversation view, but ultimately you're looking at a lot a lot of strings, a lot

**[13:54]** looking at a lot a lot of strings, a lot

**[13:54]** looking at a lot a lot of strings, a lot of tokens. This is like very hard to

**[13:56]** of tokens. This is like very hard to

**[13:56]** of tokens. This is like very hard to follow. And then this is actually like

**[13:58]** follow. And then this is actually like

**[13:58]** follow. And then this is actually like there's like 10 of these, right? So you


### [14:00 - 15:00]

**[14:00]** there's like 10 of these, right? So you

**[14:00]** there's like 10 of these, right? So you just scroll and scroll and scroll.

**[14:01]** just scroll and scroll and scroll.

**[14:01]** just scroll and scroll and scroll. You're like, "What the heck did this

**[14:02]** You're like, "What the heck did this

**[14:02]** You're like, "What the heck did this agent do?" And and this this has been

**[14:04]** agent do?" And and this this has been

**[14:04]** agent do?" And and this this has been traditionally the way that people review

**[14:07]** traditionally the way that people review

**[14:07]** traditionally the way that people review and sort of supervise agents. You're

**[14:08]** and sort of supervise agents. You're

**[14:08]** and sort of supervise agents. You're kind of just looking at the thought

**[14:10]** kind of just looking at the thought

**[14:10]** kind of just looking at the thought patterns.

**[14:11]** patterns.

**[14:12]** patterns. But isn't it much easier to understand

**[14:13]** But isn't it much easier to understand

**[14:13]** But isn't it much easier to understand what is going on inside of this visual

**[14:15]** what is going on inside of this visual

**[14:15]** what is going on inside of this visual representation? And that is what an

**[14:17]** representation? And that is what an

**[14:17]** representation? And that is what an artifact is. The whole point and the

**[14:19]** artifact is. The whole point and the

**[14:19]** artifact is. The whole point and the reason why I'm not just standing up here

**[14:20]** reason why I'm not just standing up here

**[14:20]** reason why I'm not just standing up here and giving you this long, you know,

**[14:22]** and giving you this long, you know,

**[14:22]** and giving you this long, you know, stream of consciousness is because I

**[14:23]** stream of consciousness is because I

**[14:23]** stream of consciousness is because I have a PowerPoint. The PowerPoint is my

**[14:25]** have a PowerPoint. The PowerPoint is my

**[14:25]** have a PowerPoint. The PowerPoint is my artifact. And so Gemini 3 is really

**[14:29]** artifact. And so Gemini 3 is really

**[14:29]** artifact. And so Gemini 3 is really really strong with this sort of visual

**[14:30]** really strong with this sort of visual

**[14:30]** really strong with this sort of visual representation. It's really strong with

**[14:32]** representation. It's really strong with

**[14:32]** representation. It's really strong with multimodal. And so instead of showing

**[14:34]** multimodal. And so instead of showing

**[14:34]** multimodal. And so instead of showing this, which of course we always let you

**[14:36]** this, which of course we always let you

**[14:36]** this, which of course we always let you show, we always we will always show you

**[14:37]** show, we always we will always show you

**[14:37]** show, we always we will always show you this, but we want to focus on this. And

**[14:39]** this, but we want to focus on this. And

**[14:39]** this, but we want to focus on this. And I think this is the game-changing part

**[14:41]** I think this is the game-changing part

**[14:41]** I think this is the game-changing part about anti-gravity.

**[14:43]** about anti-gravity.

**[14:43]** about anti-gravity. And the theme is this dynamicism.

**[14:46]** And the theme is this dynamicism.

**[14:46]** And the theme is this dynamicism. The model can decide if it wants to

**[14:49]** The model can decide if it wants to

**[14:49]** The model can decide if it wants to generate an artifact. And let's remember

**[14:50]** generate an artifact. And let's remember

**[14:50]** generate an artifact. And let's remember there are some tasks. We're changing a

**[14:52]** there are some tasks. We're changing a

**[14:52]** there are some tasks. We're changing a title. We're changing something small.

**[14:53]** title. We're changing something small.

**[14:53]** title. We're changing something small. Doesn't really need to to produce an

**[14:54]** Doesn't really need to to produce an

**[14:54]** Doesn't really need to to produce an artifact for this. So, it will decide if

**[14:57]** artifact for this. So, it will decide if

**[14:57]** artifact for this. So, it will decide if it needs an artifact. And then second,

**[14:59]** it needs an artifact. And then second,

**[14:59]** it needs an artifact. And then second, what type of artifact? And this is where


### [15:00 - 16:00]

**[15:01]** what type of artifact? And this is where

**[15:01]** what type of artifact? And this is where it's really cool. There there are many

**[15:03]** it's really cool. There there are many

**[15:03]** it's really cool. There there are many potential in potentially infinite ways

**[15:05]** potential in potentially infinite ways

**[15:05]** potential in potentially infinite ways that it can represent information. And

**[15:07]** that it can represent information. And

**[15:07]** that it can represent information. And so, the common ones are markdown in the

**[15:11]** so, the common ones are markdown in the

**[15:11]** so, the common ones are markdown in the concept of a of a plan and a

**[15:12]** concept of a of a plan and a

**[15:12]** concept of a of a plan and a walkthrough. So, this is probably what

**[15:13]** walkthrough. So, this is probably what

**[15:14]** walkthrough. So, this is probably what you've used most most often. When you

**[15:16]** you've used most most often. When you

**[15:16]** you've used most most often. When you start a task, it will do some research.

**[15:17]** start a task, it will do some research.

**[15:17]** start a task, it will do some research. It will put together a plan. This is

**[15:19]** It will put together a plan. This is

**[15:19]** It will put together a plan. This is much very much like a PRD. It will even

**[15:21]** much very much like a PRD. It will even

**[15:21]** much very much like a PRD. It will even list out open questions. So, you can see

**[15:22]** list out open questions. So, you can see

**[15:22]** list out open questions. So, you can see in this feedback section, it'll surface,

**[15:24]** in this feedback section, it'll surface,

**[15:24]** in this feedback section, it'll surface, hey, you should probably answer these

**[15:25]** hey, you should probably answer these

**[15:26]** hey, you should probably answer these three questions before I get going. And

**[15:27]** three questions before I get going. And

**[15:27]** three questions before I get going. And what's really awesome, and we're betting

**[15:28]** what's really awesome, and we're betting

**[15:28]** what's really awesome, and we're betting on the models here, what's really

**[15:30]** on the models here, what's really

**[15:30]** on the models here, what's really awesome is that the model will decide

**[15:31]** awesome is that the model will decide

**[15:31]** awesome is that the model will decide whether or not it can auto continue. If

**[15:33]** whether or not it can auto continue. If

**[15:33]** whether or not it can auto continue. If it has no questions, why should it wait?

**[15:35]** it has no questions, why should it wait?

**[15:35]** it has no questions, why should it wait? It should just go off. But more often

**[15:38]** It should just go off. But more often

**[15:38]** It should just go off. But more often than not, there are probably areas where

**[15:39]** than not, there are probably areas where

**[15:39]** than not, there are probably areas where you may be underspecified or maybe it

**[15:41]** you may be underspecified or maybe it

**[15:41]** you may be underspecified or maybe it did something during research, right?

**[15:42]** did something during research, right?

**[15:42]** did something during research, right? everyone has gone through and and

**[15:43]** everyone has gone through and and

**[15:43]** everyone has gone through and and started a big refactor then realized

**[15:45]** started a big refactor then realized

**[15:45]** started a big refactor then realized they actually don't have all the

**[15:45]** they actually don't have all the

**[15:45]** they actually don't have all the information ahead of them. They got to

**[15:46]** information ahead of them. They got to

**[15:46]** information ahead of them. They got to go back to the drawing board, maybe talk

**[15:48]** go back to the drawing board, maybe talk

**[15:48]** go back to the drawing board, maybe talk to some people. Same idea. So it'll

**[15:50]** to some people. Same idea. So it'll

**[15:50]** to some people. Same idea. So it'll surface um it'll surface open questions

**[15:53]** surface um it'll surface open questions

**[15:53]** surface um it'll surface open questions for you. And so that's you'll start with

**[15:55]** for you. And so that's you'll start with

**[15:55]** for you. And so that's you'll start with that implementation plan and then you'll

**[15:56]** that implementation plan and then you'll

**[15:56]** that implementation plan and then you'll say all right LGTM let's like send it.

**[15:59]** say all right LGTM let's like send it.

**[15:59]** say all right LGTM let's like send it. You go all the way down. It might


### [16:00 - 17:00]

**[16:00]** You go all the way down. It might

**[16:00]** You go all the way down. It might produce other artifacts. You know we've

**[16:01]** produce other artifacts. You know we've

**[16:02]** produce other artifacts. You know we've got a task list here. This is the way

**[16:03]** got a task list here. This is the way

**[16:03]** got a task list here. This is the way that you can monitor the the progress of

**[16:06]** that you can monitor the the progress of

**[16:06]** that you can monitor the the progress of the agent instead of looking at the

**[16:07]** the agent instead of looking at the

**[16:07]** the agent instead of looking at the conversation. might put together some

**[16:08]** conversation. might put together some

**[16:08]** conversation. might put together some architecture diagrams and then you'll

**[16:10]** architecture diagrams and then you'll

**[16:10]** architecture diagrams and then you'll get a you'll get a walkthrough at the

**[16:12]** get a you'll get a walkthrough at the

**[16:12]** get a you'll get a walkthrough at the end and this walkthrough you kind of saw

**[16:13]** end and this walkthrough you kind of saw

**[16:13]** end and this walkthrough you kind of saw a glimpse of this before but it is hey

**[16:16]** a glimpse of this before but it is hey

**[16:16]** a glimpse of this before but it is hey how do I prove to you agent to human

**[16:18]** how do I prove to you agent to human

**[16:18]** how do I prove to you agent to human that I did the correct thing and I did

**[16:20]** that I did the correct thing and I did

**[16:20]** that I did the correct thing and I did it well and then this is the part that

**[16:22]** it well and then this is the part that

**[16:22]** it well and then this is the part that you'll end with it's kind of like a PR

**[16:23]** you'll end with it's kind of like a PR

**[16:24]** you'll end with it's kind of like a PR description and then there's a whole

**[16:25]** description and then there's a whole

**[16:25]** description and then there's a whole host of other types right Images screen

**[16:27]** host of other types right Images screen

**[16:27]** host of other types right Images screen recordings these mermaid diagrams and

**[16:30]** recordings these mermaid diagrams and

**[16:30]** recordings these mermaid diagrams and really what's what's what's quite cool

**[16:32]** really what's what's what's quite cool

**[16:32]** really what's what's what's quite cool is that because it's dynamic the agent

**[16:33]** is that because it's dynamic the agent

**[16:34]** is that because it's dynamic the agent will decide this over time so suddenly

**[16:35]** will decide this over time so suddenly

**[16:35]** will decide this over time so suddenly there's maybe a new type of artifact

**[16:36]** there's maybe a new type of artifact

**[16:36]** there's maybe a new type of artifact that we maybe we missed Right? And then

**[16:39]** that we maybe we missed Right? And then

**[16:40]** that we maybe we missed Right? And then it'll figure that out. It'll just become

**[16:41]** it'll figure that out. It'll just become

**[16:41]** it'll figure that out. It'll just become part of the experience. So it's very

**[16:43]** part of the experience. So it's very

**[16:43]** part of the experience. So it's very scalable. But this artifact primitive is

**[16:44]** scalable. But this artifact primitive is

**[16:44]** scalable. But this artifact primitive is something that's very very powerful that

**[16:46]** something that's very very powerful that

**[16:46]** something that's very very powerful that I'm pretty excited about. And then I

**[16:49]** I'm pretty excited about. And then I

**[16:49]** I'm pretty excited about. And then I guess another question is why is it

**[16:50]** guess another question is why is it

**[16:50]** guess another question is why is it needed? So we'll always explain to the

**[16:52]** needed? So we'll always explain to the

**[16:52]** needed? So we'll always explain to the user what the purpose of this artifact

**[16:53]** user what the purpose of this artifact

**[16:53]** user what the purpose of this artifact is. Um and then interestingly like who

**[16:57]** is. Um and then interestingly like who

**[16:57]** is. Um and then interestingly like who should see it? So should the sub agents

**[16:59]** should see it? So should the sub agents

**[16:59]** should see it? So should the sub agents see it? Should the other agents see it?


### [17:00 - 18:00]

**[17:01]** see it? Should the other agents see it?

**[17:02]** see it? Should the other agents see it? Should other conversations see this?

**[17:03]** Should other conversations see this?

**[17:03]** Should other conversations see this? Should this be stored in my memory bank?

**[17:05]** Should this be stored in my memory bank?

**[17:05]** Should this be stored in my memory bank? Right? If this is something that I

**[17:06]** Right? If this is something that I

**[17:06]** Right? If this is something that I derived, one of the cool examples um

**[17:08]** derived, one of the cool examples um

**[17:08]** derived, one of the cool examples um that I like is like if you give it a a

**[17:10]** that I like is like if you give it a a

**[17:10]** that I like is like if you give it a a piece of documentation and give it your

**[17:11]** piece of documentation and give it your

**[17:11]** piece of documentation and give it your API key, it'll like go off and run curl

**[17:14]** API key, it'll like go off and run curl

**[17:14]** API key, it'll like go off and run curl requests to basically figure out the

**[17:15]** requests to basically figure out the

**[17:15]** requests to basically figure out the exact schema of like what the types of

**[17:17]** exact schema of like what the types of

**[17:18]** exact schema of like what the types of APIs you're using and it'll do this like

**[17:20]** APIs you're using and it'll do this like

**[17:20]** APIs you're using and it'll do this like deep research um for quite a while and

**[17:22]** deep research um for quite a while and

**[17:22]** deep research um for quite a while and then it'll give you a report and

**[17:23]** then it'll give you a report and

**[17:23]** then it'll give you a report and basically like deeply understand uh this

**[17:25]** basically like deeply understand uh this

**[17:25]** basically like deeply understand uh this sort of uh this sort of API. You

**[17:27]** sort of uh this sort of API. You

**[17:27]** sort of uh this sort of API. You wouldn't want to just throw that away

**[17:28]** wouldn't want to just throw that away

**[17:28]** wouldn't want to just throw that away and have to rederive it the second time

**[17:30]** and have to rederive it the second time

**[17:30]** and have to rederive it the second time you did this. So it'll store it in your

**[17:31]** you did this. So it'll store it in your

**[17:31]** you did this. So it'll store it in your memory and then all of a sudden that's

**[17:32]** memory and then all of a sudden that's

**[17:32]** memory and then all of a sudden that's just a part of your knowledge base. So,

**[17:35]** just a part of your knowledge base. So,

**[17:35]** just a part of your knowledge base. So, and then there's also this idea of like

**[17:37]** and then there's also this idea of like

**[17:37]** and then there's also this idea of like notifications, right? So, if there's an

**[17:38]** notifications, right? So, if there's an

**[17:38]** notifications, right? So, if there's an open question, you want the agent to be

**[17:40]** open question, you want the agent to be

**[17:40]** open question, you want the agent to be proactive with you. And that's another

**[17:43]** proactive with you. And that's another

**[17:43]** proactive with you. And that's another very cool property of this artifact

**[17:44]** very cool property of this artifact

**[17:44]** very cool property of this artifact system. We want to be able to provide

**[17:47]** system. We want to be able to provide

**[17:47]** system. We want to be able to provide feedback along this cycle. So, from task

**[17:50]** feedback along this cycle. So, from task

**[17:50]** feedback along this cycle. So, from task start to task end, we want to be able to

**[17:52]** start to task end, we want to be able to

**[17:52]** start to task end, we want to be able to provide feedback and inform the agent on

**[17:54]** provide feedback and inform the agent on

**[17:54]** provide feedback and inform the agent on what to change.

**[17:56]** what to change.

**[17:56]** what to change. And the artifact system lets you iterate

**[17:58]** And the artifact system lets you iterate

**[17:58]** And the artifact system lets you iterate with the model more fluidly


### [18:00 - 19:00]

**[18:01]** with the model more fluidly

**[18:01]** with the model more fluidly during this process of execution. And

**[18:04]** during this process of execution. And

**[18:04]** during this process of execution. And so, not to sound like a complete Google

**[18:05]** so, not to sound like a complete Google

**[18:05]** so, not to sound like a complete Google shell, but I love Google Docs, right?

**[18:07]** shell, but I love Google Docs, right?

**[18:07]** shell, but I love Google Docs, right? Google Docs is a great pattern. It's

**[18:09]** Google Docs is a great pattern. It's

**[18:09]** Google Docs is a great pattern. It's awesome. The comments are great. And

**[18:11]** awesome. The comments are great. And

**[18:11]** awesome. The comments are great. And this is how you might interact with a

**[18:12]** this is how you might interact with a

**[18:12]** this is how you might interact with a colleague, right? You're collaborating

**[18:13]** colleague, right? You're collaborating

**[18:13]** colleague, right? You're collaborating on a document. Then all of a sudden, you

**[18:14]** on a document. Then all of a sudden, you

**[18:14]** on a document. Then all of a sudden, you want to leave a textbased comment. So,

**[18:16]** want to leave a textbased comment. So,

**[18:16]** want to leave a textbased comment. So, we took inspiration from that. We took

**[18:18]** we took inspiration from that. We took

**[18:18]** we took inspiration from that. We took inspiration from GitHub. But you leave

**[18:20]** inspiration from GitHub. But you leave

**[18:20]** inspiration from GitHub. But you leave comments. You highlight text. You say,

**[18:21]** comments. You highlight text. You say,

**[18:21]** comments. You highlight text. You say, "Hey, maybe this part needs to get

**[18:22]** "Hey, maybe this part needs to get

**[18:22]** "Hey, maybe this part needs to get ironed out a bit more. Maybe there's a

**[18:24]** ironed out a bit more. Maybe there's a

**[18:24]** ironed out a bit more. Maybe there's a part that you missed or actually don't

**[18:25]** part that you missed or actually don't

**[18:25]** part that you missed or actually don't use Tailwind. Use vanilla CSS." So,

**[18:28]** use Tailwind. Use vanilla CSS." So,

**[18:28]** use Tailwind. Use vanilla CSS." So, these are the sorts of comments that you

**[18:29]** these are the sorts of comments that you

**[18:29]** these are the sorts of comments that you would leave. You'd batch them up and

**[18:30]** would leave. You'd batch them up and

**[18:30]** would leave. You'd batch them up and then you go off and send. And then in

**[18:32]** then you go off and send. And then in

**[18:32]** then you go off and send. And then in image space, this is very cool. We now

**[18:34]** image space, this is very cool. We now

**[18:34]** image space, this is very cool. We now have this like Figma style drag and drop

**[18:37]** have this like Figma style drag and drop

**[18:37]** have this like Figma style drag and drop like or not drag, you know, highlight to

**[18:38]** like or not drag, you know, highlight to

**[18:38]** like or not drag, you know, highlight to select. And now you're leaving comments

**[18:40]** select. And now you're leaving comments

**[18:40]** select. And now you're leaving comments in a in a completely different modality,

**[18:42]** in a in a completely different modality,

**[18:42]** in a in a completely different modality, right? And we've done this and

**[18:43]** right? And we've done this and

**[18:43]** right? And we've done this and instrumented the agent to ma naturally

**[18:46]** instrumented the agent to ma naturally

**[18:46]** instrumented the agent to ma naturally take your comments into consideration

**[18:47]** take your comments into consideration

**[18:47]** take your comments into consideration without interrupting that task execution

**[18:49]** without interrupting that task execution

**[18:49]** without interrupting that task execution loop. So at any point during your

**[18:52]** loop. So at any point during your

**[18:52]** loop. So at any point during your conversation, you could just say, "Oh,

**[18:53]** conversation, you could just say, "Oh,

**[18:53]** conversation, you could just say, "Oh, actually, you know, mid mid browser

**[18:55]** actually, you know, mid mid browser

**[18:55]** actually, you know, mid mid browser actuation, I actually really don't like

**[18:56]** actuation, I actually really don't like

**[18:56]** actuation, I actually really don't like the way that that turned out. Let me

**[18:57]** the way that that turned out. Let me

**[18:58]** the way that that turned out. Let me just highlight that, tell you,


### [19:00 - 20:00]

**[19:00]** just highlight that, tell you,

**[19:00]** just highlight that, tell you, send it off." and then I'll just get

**[19:02]** send it off." and then I'll just get

**[19:02]** send it off." and then I'll just get notified when you're done taking into

**[19:03]** notified when you're done taking into

**[19:03]** notified when you're done taking into consideration those comments. And so

**[19:06]** consideration those comments. And so

**[19:06]** consideration those comments. And so it's a whole new way of working. And

**[19:08]** it's a whole new way of working. And

**[19:08]** it's a whole new way of working. And this is really at the center of what

**[19:09]** this is really at the center of what

**[19:09]** this is really at the center of what we're trying to build with anti-gravity.

**[19:10]** we're trying to build with anti-gravity.

**[19:10]** we're trying to build with anti-gravity. It's pulling you out into this higher

**[19:12]** It's pulling you out into this higher

**[19:12]** It's pulling you out into this higher level view. And the agent manager really

**[19:15]** level view. And the agent manager really

**[19:15]** level view. And the agent manager really is built to optimize the UI of

**[19:18]** is built to optimize the UI of

**[19:18]** is built to optimize the UI of artifacts.

**[19:20]** artifacts.

**[19:20]** artifacts. So we have a beautiful, beautiful

**[19:22]** So we have a beautiful, beautiful

**[19:22]** So we have a beautiful, beautiful artifact review system. We're very proud

**[19:25]** artifact review system. We're very proud

**[19:25]** artifact review system. We're very proud of this. And it can also handle sort of

**[19:29]** of this. And it can also handle sort of

**[19:29]** of this. And it can also handle sort of the

**[19:30]** the

**[19:30]** the property that is like parallelism and

**[19:32]** property that is like parallelism and

**[19:32]** property that is like parallelism and orchestration. So whether this be many

**[19:34]** orchestration. So whether this be many

**[19:34]** orchestration. So whether this be many different projects, whether this be the

**[19:36]** different projects, whether this be the

**[19:36]** different projects, whether this be the same project and you just want to

**[19:37]** same project and you just want to

**[19:37]** same project and you just want to execute maybe a design mockup iteration

**[19:39]** execute maybe a design mockup iteration

**[19:39]** execute maybe a design mockup iteration at the same time you're doing research

**[19:41]** at the same time you're doing research

**[19:41]** at the same time you're doing research on an API at the same time you're

**[19:42]** on an API at the same time you're

**[19:42]** on an API at the same time you're iterating and and and actually building

**[19:44]** iterating and and and actually building

**[19:44]** iterating and and and actually building out your app. You can do all these

**[19:45]** out your app. You can do all these

**[19:45]** out your app. You can do all these things in parallel and the artifacts are

**[19:48]** things in parallel and the artifacts are

**[19:48]** things in parallel and the artifacts are the way that you provide that feedback.

**[19:49]** the way that you provide that feedback.

**[19:49]** the way that you provide that feedback. The notifications are the way that you

**[19:50]** The notifications are the way that you

**[19:50]** The notifications are the way that you know that something requires your

**[19:51]** know that something requires your

**[19:52]** know that something requires your attention. It's a completely different

**[19:53]** attention. It's a completely different

**[19:53]** attention. It's a completely different pattern. And what's really nice is that

**[19:55]** pattern. And what's really nice is that

**[19:55]** pattern. And what's really nice is that you can you can take a step back and of

**[19:57]** you can you can take a step back and of

**[19:57]** you can you can take a step back and of course you can always go into the

**[19:58]** course you can always go into the

**[19:58]** course you can always go into the editor. I'm not going to lie to you.

**[19:59]** editor. I'm not going to lie to you.

**[19:59]** editor. I'm not going to lie to you. There are tasks that you know you maybe


### [20:00 - 21:00]

**[20:01]** There are tasks that you know you maybe

**[20:01]** There are tasks that you know you maybe don't trust the agent yet. We don't

**[20:02]** don't trust the agent yet. We don't

**[20:02]** don't trust the agent yet. We don't trust the models yet. And so you can

**[20:04]** trust the models yet. And so you can

**[20:04]** trust the models yet. And so you can command E and you can command E and

**[20:05]** command E and you can command E and

**[20:05]** command E and you can command E and it'll open inside the editor within a

**[20:07]** it'll open inside the editor within a

**[20:07]** it'll open inside the editor within a split second with the exact files, the

**[20:09]** split second with the exact files, the

**[20:09]** split second with the exact files, the exact artifacts and that exact

**[20:11]** exact artifacts and that exact

**[20:11]** exact artifacts and that exact conversation open ready for you to

**[20:13]** conversation open ready for you to

**[20:13]** conversation open ready for you to autocomplete away to continue chatting

**[20:15]** autocomplete away to continue chatting

**[20:15]** autocomplete away to continue chatting synchronously to get you from 80% to

**[20:17]** synchronously to get you from 80% to

**[20:17]** synchronously to get you from 80% to 100%. So we always want to give devs

**[20:19]** 100%. So we always want to give devs

**[20:19]** 100%. So we always want to give devs that escape hatch. But in the future

**[20:22]** that escape hatch. But in the future

**[20:22]** that escape hatch. But in the future world, we're building for the future.

**[20:23]** world, we're building for the future.

**[20:23]** world, we're building for the future. You'll spend a lot of time in this agent

**[20:25]** You'll spend a lot of time in this agent

**[20:25]** You'll spend a lot of time in this agent manager working with parallel sub

**[20:27]** manager working with parallel sub

**[20:27]** manager working with parallel sub agents, right? It's a very very exciting

**[20:28]** agents, right? It's a very very exciting

**[20:28]** agents, right? It's a very very exciting concept.

**[20:31]** concept.

**[20:31]** concept. Okay, so now that you've seen we've got

**[20:33]** Okay, so now that you've seen we've got

**[20:33]** Okay, so now that you've seen we've got new capabilities, multitude of new

**[20:35]** new capabilities, multitude of new

**[20:35]** new capabilities, multitude of new capabilities, we've got a new form

**[20:37]** capabilities, we've got a new form

**[20:37]** capabilities, we've got a new form factor. Now the question is like what is

**[20:40]** factor. Now the question is like what is

**[20:40]** factor. Now the question is like what is going on under the hood at Deepmind? And

**[20:42]** going on under the hood at Deepmind? And

**[20:42]** going on under the hood at Deepmind? And the secret here is a lesson that I guess

**[20:45]** the secret here is a lesson that I guess

**[20:45]** the secret here is a lesson that I guess we've just learned over the past I don't

**[20:47]** we've just learned over the past I don't

**[20:47]** we've just learned over the past I don't know we've spent like or I I've

**[20:48]** know we've spent like or I I've

**[20:48]** know we've spent like or I I've personally spent like three years in in

**[20:50]** personally spent like three years in in

**[20:50]** personally spent like three years in in codegen. It's just to be your your

**[20:51]** codegen. It's just to be your your

**[20:52]** codegen. It's just to be your your biggest user, right? And that creates

**[20:54]** biggest user, right? And that creates

**[20:54]** biggest user, right? And that creates this research and product flywheel.

**[20:58]** this research and product flywheel.

**[20:58]** this research and product flywheel. And so I will tell you anti-gravity will

**[20:59]** And so I will tell you anti-gravity will

**[20:59]** And so I will tell you anti-gravity will be the most advanced product on the


### [21:00 - 22:00]

**[21:01]** be the most advanced product on the

**[21:01]** be the most advanced product on the market because we are building it for

**[21:02]** market because we are building it for

**[21:02]** market because we are building it for ourselves. We are our own users. And so

**[21:06]** ourselves. We are our own users. And so

**[21:06]** ourselves. We are our own users. And so in the dayto-day

**[21:08]** in the dayto-day

**[21:08]** in the dayto-day we were able to give Google engineers,

**[21:11]** we were able to give Google engineers,

**[21:11]** we were able to give Google engineers, deep mind researchers, we were able to

**[21:12]** deep mind researchers, we were able to

**[21:12]** deep mind researchers, we were able to give them an early access and now an

**[21:14]** give them an early access and now an

**[21:14]** give them an early access and now an official access to anti-gravity

**[21:16]** official access to anti-gravity

**[21:16]** official access to anti-gravity internally. And so now all of a sudden

**[21:19]** internally. And so now all of a sudden

**[21:19]** internally. And so now all of a sudden the actual experience of the models that

**[21:21]** the actual experience of the models that

**[21:21]** the actual experience of the models that people are improving, the actual

**[21:23]** people are improving, the actual

**[21:23]** people are improving, the actual experience of of using the agent manager

**[21:26]** experience of of using the agent manager

**[21:26]** experience of of using the agent manager and touching artifacts

**[21:28]** and touching artifacts

**[21:28]** and touching artifacts is letting them see at a very very real

**[21:31]** is letting them see at a very very real

**[21:31]** is letting them see at a very very real level what are the gaps in the model.

**[21:34]** level what are the gaps in the model.

**[21:34]** level what are the gaps in the model. And whether it be computer use, whether

**[21:37]** And whether it be computer use, whether

**[21:37]** And whether it be computer use, whether it be image generation, whether it be

**[21:41]** it be image generation, whether it be

**[21:41]** it be image generation, whether it be instruction following, right? Every

**[21:42]** instruction following, right? Every

**[21:42]** instruction following, right? Every single one of these teams, and there are

**[21:44]** single one of these teams, and there are

**[21:44]** single one of these teams, and there are many teams at Google, has some hand

**[21:46]** many teams at Google, has some hand

**[21:46]** many teams at Google, has some hand inside of this very, very full stack

**[21:48]** inside of this very, very full stack

**[21:48]** inside of this very, very full stack product.

**[21:50]** product.

**[21:50]** product. And so you might notice as an

**[21:51]** And so you might notice as an

**[21:51]** And so you might notice as an infrastructure engineer, you might say,

**[21:52]** infrastructure engineer, you might say,

**[21:52]** infrastructure engineer, you might say, "Oh, this is a bit slow.


### [22:00 - 23:00]

**[22:05]** page. Well, go off and and make that

**[22:05]** page. Well, go off and and make that better, right? So, it gives you this

**[22:07]** better, right? So, it gives you this

**[22:07]** better, right? So, it gives you this level of insight that eval just simply

**[22:08]** level of insight that eval just simply

**[22:08]** level of insight that eval just simply can't give you. And I think that's

**[22:10]** can't give you. And I think that's

**[22:10]** can't give you. And I think that's what's really cool about being a deep

**[22:11]** what's really cool about being a deep

**[22:11]** what's really cool about being a deep mind. You are able to integrate product

**[22:13]** mind. You are able to integrate product

**[22:14]** mind. You are able to integrate product and research in a way that creates this

**[22:15]** and research in a way that creates this

**[22:15]** and research in a way that creates this flywheel and pushes that frontier. And I

**[22:18]** flywheel and pushes that frontier. And I

**[22:18]** flywheel and pushes that frontier. And I guarantee you that whatever that

**[22:20]** guarantee you that whatever that

**[22:20]** guarantee you that whatever that frontier provides, we will provide an

**[22:21]** frontier provides, we will provide an

**[22:21]** frontier provides, we will provide an anti-gravity for the rest of the world.

**[22:23]** anti-gravity for the rest of the world.

**[22:23]** anti-gravity for the rest of the world. These are the same product. And so, I'll

**[22:25]** These are the same product. And so, I'll

**[22:25]** These are the same product. And so, I'll give you two examples of how this is has

**[22:27]** give you two examples of how this is has

**[22:27]** give you two examples of how this is has worked. The first one was that computer

**[22:28]** worked. The first one was that computer

**[22:28]** worked. The first one was that computer use example, right? in collaboration

**[22:31]** use example, right? in collaboration

**[22:31]** use example, right? in collaboration with the computer use team which we sit

**[22:33]** with the computer use team which we sit

**[22:33]** with the computer use team which we sit you know a couple couple tens of feet

**[22:35]** you know a couple couple tens of feet

**[22:35]** you know a couple couple tens of feet away from we identify gaps on both sides

**[22:38]** away from we identify gaps on both sides

**[22:38]** away from we identify gaps on both sides right so we're not just using an API we

**[22:40]** right so we're not just using an API we

**[22:40]** right so we're not just using an API we are interacting across teams to

**[22:42]** are interacting across teams to

**[22:42]** are interacting across teams to basically say oh like the capability is

**[22:44]** basically say oh like the capability is

**[22:44]** basically say oh like the capability is kind of off here can can we go off and

**[22:46]** kind of off here can can we go off and

**[22:46]** kind of off here can can we go off and figure out what's going on here maybe

**[22:47]** figure out what's going on here maybe

**[22:47]** figure out what's going on here maybe there's a there's a mismatch in data

**[22:48]** there's a there's a mismatch in data

**[22:48]** there's a there's a mismatch in data distribution and then on the other side

**[22:50]** distribution and then on the other side

**[22:50]** distribution and then on the other side it's like yo your like agent harness is

**[22:53]** it's like yo your like agent harness is

**[22:53]** it's like yo your like agent harness is like pretty screwed up you got to fix

**[22:55]** like pretty screwed up you got to fix

**[22:55]** like pretty screwed up you got to fix your tools right and so then we'll go

**[22:56]** your tools right and so then we'll go

**[22:56]** your tools right and so then we'll go off and we'll fix our side but it's this

**[22:58]** off and we'll fix our side but it's this

**[22:58]** off and we'll fix our side but it's this harmony it's it's both sides talking to


### [23:00 - 24:00]

**[23:00]** harmony it's it's both sides talking to

**[23:00]** harmony it's it's both sides talking to each other that really makes this type

**[23:01]** each other that really makes this type

**[23:01]** each other that really makes this type of thing possible. Similarly, you come

**[23:04]** of thing possible. Similarly, you come

**[23:04]** of thing possible. Similarly, you come up with a new product paradigm

**[23:05]** up with a new product paradigm

**[23:05]** up with a new product paradigm artifacts. Artifacts were not good on

**[23:08]** artifacts. Artifacts were not good on

**[23:08]** artifacts. Artifacts were not good on the initial on the initial uh versions,

**[23:10]** the initial on the initial uh versions,

**[23:10]** the initial on the initial uh versions, right? What part of training, what part

**[23:12]** right? What part of training, what part

**[23:12]** right? What part of training, what part of data distribution includes this like

**[23:14]** of data distribution includes this like

**[23:14]** of data distribution includes this like weird concept of reviews? And so, it

**[23:16]** weird concept of reviews? And so, it

**[23:16]** weird concept of reviews? And so, it took a little bit of plumbing, a little

**[23:17]** took a little bit of plumbing, a little

**[23:18]** took a little bit of plumbing, a little bit of work with the research team to

**[23:19]** bit of work with the research team to

**[23:19]** bit of work with the research team to figure out, all right, let's steadily

**[23:21]** figure out, all right, let's steadily

**[23:21]** figure out, all right, let's steadily improve this ability. Let's give you a

**[23:22]** improve this ability. Let's give you a

**[23:22]** improve this ability. Let's give you a hill to climb. And then now we were able

**[23:25]** hill to climb. And then now we were able

**[23:25]** hill to climb. And then now we were able to launch Gemini 3 Pro with a very good

**[23:28]** to launch Gemini 3 Pro with a very good

**[23:28]** to launch Gemini 3 Pro with a very good ability to handle these sorts of

**[23:29]** ability to handle these sorts of

**[23:29]** ability to handle these sorts of artifacts. And so it's this cyclic

**[23:31]** artifacts. And so it's this cyclic

**[23:31]** artifacts. And so it's this cyclic nature that I'm really really betting

**[23:33]** nature that I'm really really betting

**[23:33]** nature that I'm really really betting on.

**[23:34]** on.

**[23:34]** on. And this this is really how anti-gravity

**[23:37]** And this this is really how anti-gravity

**[23:37]** And this this is really how anti-gravity will defy gravity. We've got pushing the

**[23:40]** will defy gravity. We've got pushing the

**[23:40]** will defy gravity. We've got pushing the ceiling. We're going to have an agent

**[23:41]** ceiling. We're going to have an agent

**[23:41]** ceiling. We're going to have an agent with very very high level of ambition.

**[23:43]** with very very high level of ambition.

**[23:43]** with very very high level of ambition. We're going to try and do as much as we

**[23:44]** We're going to try and do as much as we

**[23:44]** We're going to try and do as much as we can. And this includes vibe coding.

**[23:47]** can. And this includes vibe coding.

**[23:47]** can. And this includes vibe coding. Though I will say there are some

**[23:48]** Though I will say there are some

**[23:48]** Though I will say there are some excellent products out there by Google.

**[23:50]** excellent products out there by Google.

**[23:50]** excellent products out there by Google. AI Studio is an excellent product.

**[23:53]** AI Studio is an excellent product.

**[23:53]** AI Studio is an excellent product. We are in the business of increasing the

**[23:55]** We are in the business of increasing the

**[23:55]** We are in the business of increasing the ceiling.

**[23:58]** ceiling.

**[23:58]** ceiling. Second, we built this agent first


### [24:00 - 25:00]

**[24:00]** Second, we built this agent first

**[24:00]** Second, we built this agent first experience artifacts agent manager. And

**[24:03]** experience artifacts agent manager. And

**[24:03]** experience artifacts agent manager. And then finally, we have this research

**[24:05]** then finally, we have this research

**[24:05]** then finally, we have this research product flywheel. And this is the magic.

**[24:07]** product flywheel. And this is the magic.

**[24:07]** product flywheel. And this is the magic. And this is the three-step process that

**[24:08]** And this is the three-step process that

**[24:08]** And this is the three-step process that we used in building anti-gravity.

**[24:13]** we used in building anti-gravity.

**[24:13]** we used in building anti-gravity. So, it's been a blast. I mean, I've I've

**[24:14]** So, it's been a blast. I mean, I've I've

**[24:14]** So, it's been a blast. I mean, I've I've been back at um AI Engineer Summit.

**[24:17]** been back at um AI Engineer Summit.

**[24:17]** been back at um AI Engineer Summit. Thank you again, Swix and Ben, for

**[24:18]** Thank you again, Swix and Ben, for

**[24:18]** Thank you again, Swix and Ben, for having me. It's been awesome to come

**[24:20]** having me. It's been awesome to come

**[24:20]** having me. It's been awesome to come back every year. And so on behalf of the

**[24:21]** back every year. And so on behalf of the

**[24:21]** back every year. And so on behalf of the anti-gravity team, I just want to thank

**[24:22]** anti-gravity team, I just want to thank

**[24:22]** anti-gravity team, I just want to thank you for your time, for your patience as

**[24:25]** you for your time, for your patience as

**[24:25]** you for your time, for your patience as you use the product um and your support.

**[24:28]** you use the product um and your support.

**[24:28]** you use the product um and your support. And of course,

**[24:30]** And of course,

**[24:30]** And of course, you too can adopt a TPU and help us uh

**[24:33]** you too can adopt a TPU and help us uh

**[24:33]** you too can adopt a TPU and help us uh turn off pager duty a bit more. Um and

**[24:35]** turn off pager duty a bit more. Um and

**[24:36]** turn off pager duty a bit more. Um and then of course, you know, you could also

**[24:37]** then of course, you know, you could also

**[24:37]** then of course, you know, you could also yell at me on Twitter. That's another

**[24:38]** yell at me on Twitter. That's another

**[24:38]** yell at me on Twitter. That's another way of doing it. Maybe do it in DMs

**[24:39]** way of doing it. Maybe do it in DMs

**[24:39]** way of doing it. Maybe do it in DMs instead. Um but we've got a lot of

**[24:41]** instead. Um but we've got a lot of

**[24:41]** instead. Um but we've got a lot of exciting things and I'm really really

**[24:42]** exciting things and I'm really really

**[24:42]** exciting things and I'm really really excited to bring anti-gravity to market.

**[24:44]** excited to bring anti-gravity to market.

**[24:44]** excited to bring anti-gravity to market. The team is thrilled that this is now

**[24:46]** The team is thrilled that this is now

**[24:46]** The team is thrilled that this is now out in the wild. So we welcome your

**[24:47]** out in the wild. So we welcome your

**[24:48]** out in the wild. So we welcome your feedback. Um, and thank you again for

**[24:50]** feedback. Um, and thank you again for

**[24:50]** feedback. Um, and thank you again for listening. Enjoy the rest of the

**[24:51]** listening. Enjoy the rest of the

**[24:51]** listening. Enjoy the rest of the conference. [applause]


