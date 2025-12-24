# The Infinite Software Crisis – Jake Nations, Netflix

**Video URL:** https://youtu.be/eIoohUmYpGI

---

## Full Transcript

### [00:00 - 01:00]

**[00:23]** Hey everyone, good afternoon. Um, I'm

**[00:23]** Hey everyone, good afternoon. Um, I'm going to start my talk with a bit of a

**[00:24]** going to start my talk with a bit of a

**[00:24]** going to start my talk with a bit of a confession. Uh, I've shipped code I

**[00:28]** confession. Uh, I've shipped code I

**[00:28]** confession. Uh, I've shipped code I didn't quite understand. Generated it,

**[00:30]** didn't quite understand. Generated it,

**[00:30]** didn't quite understand. Generated it, tested it, deployed it. Couldn't explain

**[00:32]** tested it, deployed it. Couldn't explain

**[00:32]** tested it, deployed it. Couldn't explain how it worked. And here's the thing,

**[00:34]** how it worked. And here's the thing,

**[00:34]** how it worked. And here's the thing, though. I'm willing to bet every one of

**[00:36]** though. I'm willing to bet every one of

**[00:36]** though. I'm willing to bet every one of you have, too. [applause]

**[00:41]** So, now I'm going to admit that we all

**[00:41]** So, now I'm going to admit that we all ship code that we don't understand

**[00:42]** ship code that we don't understand

**[00:42]** ship code that we don't understand anymore. I want to take a bit of a

**[00:44]** anymore. I want to take a bit of a

**[00:44]** anymore. I want to take a bit of a journey, see how this kind of has come

**[00:45]** journey, see how this kind of has come

**[00:45]** journey, see how this kind of has come to be. First, look back in history. We

**[00:48]** to be. First, look back in history. We

**[00:48]** to be. First, look back in history. We see that history tends to repeat itself.

**[00:50]** see that history tends to repeat itself.

**[00:50]** see that history tends to repeat itself. Second, we've fallen into a bit of a

**[00:51]** Second, we've fallen into a bit of a

**[00:52]** Second, we've fallen into a bit of a trap. We've confused easy with simple.

**[00:55]** trap. We've confused easy with simple.

**[00:55]** trap. We've confused easy with simple. Lastly, there is a fix, but it requires

**[00:57]** Lastly, there is a fix, but it requires

**[00:57]** Lastly, there is a fix, but it requires us not to outsource our thinking.


### [01:00 - 02:00]

**[01:01]** us not to outsource our thinking.

**[01:01]** us not to outsource our thinking. So, I spent the last few years at

**[01:03]** So, I spent the last few years at

**[01:03]** So, I spent the last few years at Netflix helping drive adoption of AI

**[01:04]** Netflix helping drive adoption of AI

**[01:04]** Netflix helping drive adoption of AI tools, and I have to say the

**[01:05]** tools, and I have to say the

**[01:05]** tools, and I have to say the acceleration is absolutely real. Backlog

**[01:08]** acceleration is absolutely real. Backlog

**[01:08]** acceleration is absolutely real. Backlog items that used to take days now take

**[01:09]** items that used to take days now take

**[01:09]** items that used to take days now take hours, and large refactors that have

**[01:12]** hours, and large refactors that have

**[01:12]** hours, and large refactors that have been on the books for years are finally

**[01:13]** been on the books for years are finally

**[01:13]** been on the books for years are finally being done. Here's the thing, though.

**[01:16]** being done. Here's the thing, though.

**[01:16]** being done. Here's the thing, though. Large production systems always fail in

**[01:18]** Large production systems always fail in

**[01:18]** Large production systems always fail in unexpected ways. Like, look what

**[01:19]** unexpected ways. Like, look what

**[01:19]** unexpected ways. Like, look what happened with CloudFare recently. When

**[01:21]** happened with CloudFare recently. When

**[01:21]** happened with CloudFare recently. When they do, you better understand the code

**[01:23]** they do, you better understand the code

**[01:23]** they do, you better understand the code you're debugging. And the problem is now

**[01:25]** you're debugging. And the problem is now

**[01:25]** you're debugging. And the problem is now we're generating code at such speed and

**[01:26]** we're generating code at such speed and

**[01:26]** we're generating code at such speed and such volume our understanding is having

**[01:28]** such volume our understanding is having

**[01:28]** such volume our understanding is having a hard time keeping up.

**[01:32]** a hard time keeping up.

**[01:32]** a hard time keeping up. Hell, I know I've done it myself. I've

**[01:34]** Hell, I know I've done it myself. I've

**[01:34]** Hell, I know I've done it myself. I've generated a bunch of code, looked at it,

**[01:36]** generated a bunch of code, looked at it,

**[01:36]** generated a bunch of code, looked at it, thought, I have no idea how this what

**[01:38]** thought, I have no idea how this what

**[01:38]** thought, I have no idea how this what this does. But, you know, the test pass,

**[01:40]** this does. But, you know, the test pass,

**[01:40]** this does. But, you know, the test pass, it works. So, I shipped it. The thing

**[01:43]** it works. So, I shipped it. The thing

**[01:43]** it works. So, I shipped it. The thing here is this isn't really new. Every

**[01:44]** here is this isn't really new. Every

**[01:44]** here is this isn't really new. Every generation of software engineers has

**[01:46]** generation of software engineers has

**[01:46]** generation of software engineers has eventually hit a wall where software

**[01:48]** eventually hit a wall where software

**[01:48]** eventually hit a wall where software complexity has exceeded their ability to

**[01:49]** complexity has exceeded their ability to

**[01:49]** complexity has exceeded their ability to manage it. We're not the fa first to

**[01:51]** manage it. We're not the fa first to

**[01:51]** manage it. We're not the fa first to face a software crisis. were the first

**[01:53]** face a software crisis. were the first

**[01:53]** face a software crisis. were the first to face it at this infinite scale of

**[01:54]** to face it at this infinite scale of

**[01:54]** to face it at this infinite scale of generation. So let's take a step back to

**[01:57]** generation. So let's take a step back to

**[01:57]** generation. So let's take a step back to see where this all started.

**[01:59]** see where this all started.

**[01:59]** see where this all started. In the late 60s, early '7s, a bunch of


### [02:00 - 03:00]

**[02:01]** In the late 60s, early '7s, a bunch of

**[02:02]** In the late 60s, early '7s, a bunch of smart computer scientists at the time

**[02:03]** smart computer scientists at the time

**[02:03]** smart computer scientists at the time came together and said, "Hey, we're in a

**[02:05]** came together and said, "Hey, we're in a

**[02:05]** came together and said, "Hey, we're in a software crisis. We have this huge

**[02:08]** software crisis. We have this huge

**[02:08]** software crisis. We have this huge demand for software and yet we're not

**[02:10]** demand for software and yet we're not

**[02:10]** demand for software and yet we're not really able to keep up and like projects

**[02:12]** really able to keep up and like projects

**[02:12]** really able to keep up and like projects are taking too long and it's just really

**[02:14]** are taking too long and it's just really

**[02:14]** are taking too long and it's just really slow. We're not doing a good job."

**[02:16]** slow. We're not doing a good job."

**[02:16]** slow. We're not doing a good job." So Dystra Kano came up with a really

**[02:19]** So Dystra Kano came up with a really

**[02:19]** So Dystra Kano came up with a really great quote and he said when we had a

**[02:21]** great quote and he said when we had a

**[02:21]** great quote and he said when we had a few weak computers and I mean to

**[02:22]** few weak computers and I mean to

**[02:22]** few weak computers and I mean to paraphrase a longer quote when we had a

**[02:23]** paraphrase a longer quote when we had a

**[02:23]** paraphrase a longer quote when we had a few weak computers programming was a

**[02:26]** few weak computers programming was a

**[02:26]** few weak computers programming was a mild problem and now we have gigantic

**[02:27]** mild problem and now we have gigantic

**[02:27]** mild problem and now we have gigantic computers programming has become a

**[02:29]** computers programming has become a

**[02:29]** computers programming has become a gigantic problem. He was explaining as

**[02:31]** gigantic problem. He was explaining as

**[02:31]** gigantic problem. He was explaining as hardware power grew by a factor of a

**[02:33]** hardware power grew by a factor of a

**[02:33]** hardware power grew by a factor of a thousand society's wants of software

**[02:35]** thousand society's wants of software

**[02:35]** thousand society's wants of software grew in proportion and so it left us the

**[02:38]** grew in proportion and so it left us the

**[02:38]** grew in proportion and so it left us the programmers to figure out between the

**[02:40]** programmers to figure out between the

**[02:40]** programmers to figure out between the ways and the means how do we support

**[02:42]** ways and the means how do we support

**[02:42]** ways and the means how do we support this much more software.

**[02:44]** this much more software.

**[02:44]** this much more software. So this kind of keeps happening in a

**[02:46]** So this kind of keeps happening in a

**[02:46]** So this kind of keeps happening in a cycle. In the 70s we get the C

**[02:48]** cycle. In the 70s we get the C

**[02:48]** cycle. In the 70s we get the C programming language so we could write

**[02:49]** programming language so we could write

**[02:49]** programming language so we could write bigger systems. The 80s we have personal

**[02:51]** bigger systems. The 80s we have personal

**[02:51]** bigger systems. The 80s we have personal computers. Now everyone can write

**[02:52]** computers. Now everyone can write

**[02:52]** computers. Now everyone can write software. In the '9s we get

**[02:54]** software. In the '9s we get

**[02:54]** software. In the '9s we get object-oriented programming inheritance

**[02:57]** object-oriented programming inheritance

**[02:57]** object-oriented programming inheritance hierarchies from hell where you know

**[02:58]** hierarchies from hell where you know

**[02:58]** hierarchies from hell where you know thanks Java for that. In the 2000s we


### [03:00 - 04:00]

**[03:01]** thanks Java for that. In the 2000s we

**[03:01]** thanks Java for that. In the 2000s we get agile and we sprints and scrum

**[03:03]** get agile and we sprints and scrum

**[03:03]** get agile and we sprints and scrum masters telling us what to do. There's

**[03:05]** masters telling us what to do. There's

**[03:05]** masters telling us what to do. There's no more waterfall. In the 2010s we had

**[03:07]** no more waterfall. In the 2010s we had

**[03:07]** no more waterfall. In the 2010s we had cloud mobile devops you know everything.

**[03:09]** cloud mobile devops you know everything.

**[03:09]** cloud mobile devops you know everything. Software truly ate the world.

**[03:12]** Software truly ate the world.

**[03:12]** Software truly ate the world. And today now we have AI. you know,

**[03:14]** And today now we have AI. you know,

**[03:14]** And today now we have AI. you know, co-pilot, cursor, claude, codeex,

**[03:16]** co-pilot, cursor, claude, codeex,

**[03:16]** co-pilot, cursor, claude, codeex, gemini, you name it. We could generate

**[03:17]** gemini, you name it. We could generate

**[03:17]** gemini, you name it. We could generate code as fast as we can describe it. The

**[03:19]** code as fast as we can describe it. The

**[03:20]** code as fast as we can describe it. The pattern continues, but the stale has

**[03:21]** pattern continues, but the stale has

**[03:21]** pattern continues, but the stale has really changed. It's it's infinite now.

**[03:25]** really changed. It's it's infinite now.

**[03:25]** really changed. It's it's infinite now. So, uh, Fred Brooks, you might know him

**[03:27]** So, uh, Fred Brooks, you might know him

**[03:27]** So, uh, Fred Brooks, you might know him from writing the mythical man month. He

**[03:29]** from writing the mythical man month. He

**[03:29]** from writing the mythical man month. He also wrote a paper in 1986 called No

**[03:31]** also wrote a paper in 1986 called No

**[03:31]** also wrote a paper in 1986 called No Silver Bullet. And in this, he argued

**[03:33]** Silver Bullet. And in this, he argued

**[03:33]** Silver Bullet. And in this, he argued that there'd be no single innovation

**[03:35]** that there'd be no single innovation

**[03:35]** that there'd be no single innovation that would give us an order of magnitude

**[03:37]** that would give us an order of magnitude

**[03:37]** that would give us an order of magnitude improvement in software productivity.

**[03:39]** improvement in software productivity.

**[03:39]** improvement in software productivity. Why? Because he said the hard part

**[03:41]** Why? Because he said the hard part

**[03:41]** Why? Because he said the hard part wasn't ever the mechanics of coding. the

**[03:44]** wasn't ever the mechanics of coding. the

**[03:44]** wasn't ever the mechanics of coding. the syntax, the typing, the boilerplate. It

**[03:46]** syntax, the typing, the boilerplate. It

**[03:46]** syntax, the typing, the boilerplate. It was about understanding the actual

**[03:47]** was about understanding the actual

**[03:47]** was about understanding the actual problem and designing the solution. And

**[03:49]** problem and designing the solution. And

**[03:49]** problem and designing the solution. And no tool can eliminate that fundamental

**[03:51]** no tool can eliminate that fundamental

**[03:51]** no tool can eliminate that fundamental difficulty. Every tool and technique

**[03:53]** difficulty. Every tool and technique

**[03:53]** difficulty. Every tool and technique we've created up to this point makes the

**[03:54]** we've created up to this point makes the

**[03:54]** we've created up to this point makes the mechanics easier. The core challenge

**[03:56]** mechanics easier. The core challenge

**[03:56]** mechanics easier. The core challenge though, understanding what to build, how

**[03:58]** though, understanding what to build, how

**[03:58]** though, understanding what to build, how it should work remains just as hard.


### [04:00 - 05:00]

**[04:04]** So, if the problem isn't in the

**[04:04]** So, if the problem isn't in the mechanics, why do we keep optimizing for

**[04:06]** mechanics, why do we keep optimizing for

**[04:06]** mechanics, why do we keep optimizing for it? How do experienced engineers end up

**[04:07]** it? How do experienced engineers end up

**[04:07]** it? How do experienced engineers end up with code they don't understand? Now,

**[04:09]** with code they don't understand? Now,

**[04:09]** with code they don't understand? Now, the answer, I think, comes down to two

**[04:11]** the answer, I think, comes down to two

**[04:11]** the answer, I think, comes down to two words we tend to confuse. simple and

**[04:13]** words we tend to confuse. simple and

**[04:13]** words we tend to confuse. simple and easy. We tend to use them

**[04:15]** easy. We tend to use them

**[04:15]** easy. We tend to use them interchangeably, but they really mean

**[04:16]** interchangeably, but they really mean

**[04:16]** interchangeably, but they really mean completely different things. Uh I was

**[04:19]** completely different things. Uh I was

**[04:19]** completely different things. Uh I was outed at the speaker dinner as being a

**[04:20]** outed at the speaker dinner as being a

**[04:20]** outed at the speaker dinner as being a closure guy, so this is kind of clear

**[04:22]** closure guy, so this is kind of clear

**[04:22]** closure guy, so this is kind of clear here. But Rich Hickey, the creator of

**[04:24]** here. But Rich Hickey, the creator of

**[04:24]** here. But Rich Hickey, the creator of the closure programming language,

**[04:25]** the closure programming language,

**[04:25]** the closure programming language, explained this in his talk from 2011

**[04:27]** explained this in his talk from 2011

**[04:27]** explained this in his talk from 2011 called simple made easy. He defined

**[04:30]** called simple made easy. He defined

**[04:30]** called simple made easy. He defined simple meaning one fold, one braid, and

**[04:32]** simple meaning one fold, one braid, and

**[04:32]** simple meaning one fold, one braid, and no entanglement. Each piece does one

**[04:34]** no entanglement. Each piece does one

**[04:34]** no entanglement. Each piece does one thing and doesn't intertwine with

**[04:35]** thing and doesn't intertwine with

**[04:35]** thing and doesn't intertwine with others. He defines easy as meaning

**[04:37]** others. He defines easy as meaning

**[04:38]** others. He defines easy as meaning adjacent. What's within reach? What can

**[04:39]** adjacent. What's within reach? What can

**[04:39]** adjacent. What's within reach? What can you access without effort? Copy paste

**[04:42]** you access without effort? Copy paste

**[04:42]** you access without effort? Copy paste ship. Simple is about structure. Easy is

**[04:45]** ship. Simple is about structure. Easy is

**[04:45]** ship. Simple is about structure. Easy is about proximity.

**[04:48]** about proximity.

**[04:48]** about proximity. The thing is we can't make something

**[04:49]** The thing is we can't make something

**[04:49]** The thing is we can't make something simple by wishing it. So simplicity

**[04:51]** simple by wishing it. So simplicity

**[04:51]** simple by wishing it. So simplicity requires thought, design and untangling.

**[04:54]** requires thought, design and untangling.

**[04:54]** requires thought, design and untangling. But we can always make something easier.

**[04:56]** But we can always make something easier.

**[04:56]** But we can always make something easier. You just put it closer. Install a

**[04:58]** You just put it closer. Install a

**[04:58]** You just put it closer. Install a package, generate it with AI, you know,


### [05:00 - 06:00]

**[05:00]** package, generate it with AI, you know,

**[05:00]** package, generate it with AI, you know, copy a solution off of Stack Overflow.

**[05:03]** copy a solution off of Stack Overflow.

**[05:03]** copy a solution off of Stack Overflow. It's it's human nature to take the easy

**[05:05]** It's it's human nature to take the easy

**[05:05]** It's it's human nature to take the easy path. We're wired for it. You know, as I

**[05:08]** path. We're wired for it. You know, as I

**[05:08]** path. We're wired for it. You know, as I said, copy something from Stack

**[05:09]** said, copy something from Stack

**[05:09]** said, copy something from Stack Overflow. It's right there. framework

**[05:10]** Overflow. It's right there. framework

**[05:10]** Overflow. It's right there. framework that handles everything for you with

**[05:12]** that handles everything for you with

**[05:12]** that handles everything for you with magic. Install and go. But easy doesn't

**[05:15]** magic. Install and go. But easy doesn't

**[05:15]** magic. Install and go. But easy doesn't mean simple. Easy means you can add to

**[05:16]** mean simple. Easy means you can add to

**[05:16]** mean simple. Easy means you can add to your system quickly. Simple means you

**[05:18]** your system quickly. Simple means you

**[05:18]** your system quickly. Simple means you can understand the work that you've

**[05:20]** can understand the work that you've

**[05:20]** can understand the work that you've done. Every time we choose easy, we're

**[05:22]** done. Every time we choose easy, we're

**[05:22]** done. Every time we choose easy, we're choosing speed now. Complexity later.

**[05:23]** choosing speed now. Complexity later.

**[05:24]** choosing speed now. Complexity later. And honestly,

**[05:25]** And honestly,

**[05:25]** And honestly, that trade-off really used to work. The

**[05:28]** that trade-off really used to work. The

**[05:28]** that trade-off really used to work. The complexity accumulated in our codebases

**[05:30]** complexity accumulated in our codebases

**[05:30]** complexity accumulated in our codebases slowly enough that we can refactor,

**[05:31]** slowly enough that we can refactor,

**[05:32]** slowly enough that we can refactor, rethink, and rebuild when needed. I

**[05:34]** rethink, and rebuild when needed. I

**[05:34]** rethink, and rebuild when needed. I think AI has destroyed that balance

**[05:36]** think AI has destroyed that balance

**[05:36]** think AI has destroyed that balance because it's the ultimate easy bun. And

**[05:37]** because it's the ultimate easy bun. And

**[05:37]** because it's the ultimate easy bun. And it makes the easy path so frictionless

**[05:39]** it makes the easy path so frictionless

**[05:39]** it makes the easy path so frictionless that we don't even consider the simple

**[05:40]** that we don't even consider the simple

**[05:40]** that we don't even consider the simple one anymore. Why think about

**[05:42]** one anymore. Why think about

**[05:42]** one anymore. Why think about architecture when code appears

**[05:43]** architecture when code appears

**[05:43]** architecture when code appears instantly.

**[05:46]** instantly.

**[05:46]** instantly. So let me show you how this happens. How

**[05:47]** So let me show you how this happens. How

**[05:47]** So let me show you how this happens. How a simple task evolves into a mess of

**[05:49]** a simple task evolves into a mess of

**[05:49]** a simple task evolves into a mess of complexity through a conversational

**[05:50]** complexity through a conversational

**[05:50]** complexity through a conversational interface that we've all come to love.

**[05:53]** interface that we've all come to love.

**[05:53]** interface that we've all come to love. You know this is a contrived example but

**[05:54]** You know this is a contrived example but

**[05:54]** You know this is a contrived example but you know say we have our app. We want to

**[05:56]** you know say we have our app. We want to

**[05:56]** you know say we have our app. We want to add uh some authentication to it. We say

**[05:58]** add uh some authentication to it. We say

**[05:58]** add uh some authentication to it. We say add o. So we get a nice clean o.js file.


### [06:00 - 07:00]

**[06:01]** add o. So we get a nice clean o.js file.

**[06:01]** add o. So we get a nice clean o.js file. Iterate on a few times it gets a message

**[06:02]** Iterate on a few times it gets a message

**[06:02]** Iterate on a few times it gets a message file. You're like okay cool. We're going

**[06:03]** file. You're like okay cool. We're going

**[06:03]** file. You're like okay cool. We're going to add OOTH now too because and now

**[06:05]** to add OOTH now too because and now

**[06:06]** to add OOTH now too because and now we've got an OJS and OOTHJS. We keep

**[06:08]** we've got an OJS and OOTHJS. We keep

**[06:08]** we've got an OJS and OOTHJS. We keep iterating and then we find ourselves

**[06:09]** iterating and then we find ourselves

**[06:09]** iterating and then we find ourselves that sessions are broken and we got a

**[06:11]** that sessions are broken and we got a

**[06:11]** that sessions are broken and we got a bunch of conflicts and by the time you

**[06:12]** bunch of conflicts and by the time you

**[06:12]** bunch of conflicts and by the time you get to turn 20, you're not really having

**[06:14]** get to turn 20, you're not really having

**[06:14]** get to turn 20, you're not really having a discussion anymore. You're managing

**[06:15]** a discussion anymore. You're managing

**[06:15]** a discussion anymore. You're managing context that become so complex that even

**[06:18]** context that become so complex that even

**[06:18]** context that become so complex that even you don't remember all the constraints

**[06:19]** you don't remember all the constraints

**[06:19]** you don't remember all the constraints that you've added to it. Dead code from

**[06:21]** that you've added to it. Dead code from

**[06:21]** that you've added to it. Dead code from abandoned approaches. Uh tests that got

**[06:23]** abandoned approaches. Uh tests that got

**[06:23]** abandoned approaches. Uh tests that got fixed by just making them work. You

**[06:25]** fixed by just making them work. You

**[06:25]** fixed by just making them work. You know, fragments of three different

**[06:26]** know, fragments of three different

**[06:26]** know, fragments of three different solutions because you have saying wait

**[06:28]** solutions because you have saying wait

**[06:28]** solutions because you have saying wait actually each new instruction is

**[06:30]** actually each new instruction is

**[06:30]** actually each new instruction is overwriting architectural patterns. We

**[06:32]** overwriting architectural patterns. We

**[06:32]** overwriting architectural patterns. We said make the off work here. It did.

**[06:33]** said make the off work here. It did.

**[06:33]** said make the off work here. It did. When we said fix this error, it did.

**[06:35]** When we said fix this error, it did.

**[06:35]** When we said fix this error, it did. There's no resistance to bad

**[06:37]** There's no resistance to bad

**[06:37]** There's no resistance to bad architectural decisions. The code just

**[06:38]** architectural decisions. The code just

**[06:38]** architectural decisions. The code just morphs to satisfy your latest request.

**[06:40]** morphs to satisfy your latest request.

**[06:40]** morphs to satisfy your latest request. Each interaction is choosing easy over

**[06:42]** Each interaction is choosing easy over

**[06:42]** Each interaction is choosing easy over simple. And easy always means more

**[06:45]** simple. And easy always means more

**[06:45]** simple. And easy always means more complexity. We know better. But when the

**[06:47]** complexity. We know better. But when the

**[06:48]** complexity. We know better. But when the easy path is just this easy, we take it.

**[06:50]** easy path is just this easy, we take it.

**[06:50]** easy path is just this easy, we take it. And complexity is going to compound

**[06:51]** And complexity is going to compound

**[06:51]** And complexity is going to compound until it's too late.

**[06:57]** AI really takes easy to its logical

**[06:57]** AI really takes easy to its logical extreme. Decide what you want. Get code


### [07:00 - 08:00]

**[07:00]** extreme. Decide what you want. Get code

**[07:00]** extreme. Decide what you want. Get code instantly. But here's the danger in

**[07:02]** instantly. But here's the danger in

**[07:02]** instantly. But here's the danger in that. The generated code treats every

**[07:04]** that. The generated code treats every

**[07:04]** that. The generated code treats every pattern in your codebase the same. You

**[07:07]** pattern in your codebase the same. You

**[07:07]** pattern in your codebase the same. You know, when an agent analyzed your

**[07:08]** know, when an agent analyzed your

**[07:08]** know, when an agent analyzed your codebase, every line becomes a pattern

**[07:09]** codebase, every line becomes a pattern

**[07:10]** codebase, every line becomes a pattern to preserve. The authentication check on

**[07:11]** to preserve. The authentication check on

**[07:11]** to preserve. The authentication check on line 47, that's a pattern. That weird

**[07:14]** line 47, that's a pattern. That weird

**[07:14]** line 47, that's a pattern. That weird gRPC code that's acting like GraphQL

**[07:16]** gRPC code that's acting like GraphQL

**[07:16]** gRPC code that's acting like GraphQL that I may have had in 2019, that's also

**[07:18]** that I may have had in 2019, that's also

**[07:18]** that I may have had in 2019, that's also a pattern. Technical debt doesn't

**[07:20]** a pattern. Technical debt doesn't

**[07:20]** a pattern. Technical debt doesn't register as debt. It's just more code.

**[07:22]** register as debt. It's just more code.

**[07:22]** register as debt. It's just more code. The real problem here is complexity. I

**[07:25]** The real problem here is complexity. I

**[07:25]** The real problem here is complexity. I know I've been saying that word a bunch

**[07:27]** know I've been saying that word a bunch

**[07:27]** know I've been saying that word a bunch in this talk without really defining it,

**[07:29]** in this talk without really defining it,

**[07:29]** in this talk without really defining it, but the best way to think about it is

**[07:30]** but the best way to think about it is

**[07:30]** but the best way to think about it is it's the opposite of simplicity. It just

**[07:31]** it's the opposite of simplicity. It just

**[07:32]** it's the opposite of simplicity. It just means intertwined. And when things are

**[07:33]** means intertwined. And when things are

**[07:33]** means intertwined. And when things are complex, everything touches everything

**[07:35]** complex, everything touches everything

**[07:35]** complex, everything touches everything else. You can't change one thing without

**[07:37]** else. You can't change one thing without

**[07:37]** else. You can't change one thing without affecting 10 others.

**[07:41]** affecting 10 others.

**[07:41]** affecting 10 others. So, back to Fred Brooks's no bullet

**[07:43]** So, back to Fred Brooks's no bullet

**[07:43]** So, back to Fred Brooks's no bullet paper. In it, he identified that there's

**[07:45]** paper. In it, he identified that there's

**[07:45]** paper. In it, he identified that there's two main types of complexity in every

**[07:46]** two main types of complexity in every

**[07:46]** two main types of complexity in every system. There's the essential

**[07:48]** system. There's the essential

**[07:48]** system. There's the essential complexity, which is really the

**[07:50]** complexity, which is really the

**[07:50]** complexity, which is really the fundamental difficulty of the actual

**[07:52]** fundamental difficulty of the actual

**[07:52]** fundamental difficulty of the actual problem you're trying to solve. Users

**[07:53]** problem you're trying to solve. Users

**[07:53]** problem you're trying to solve. Users need to pay for things, orders must be

**[07:55]** need to pay for things, orders must be

**[07:55]** need to pay for things, orders must be fulfilled. This is the complexity of why

**[07:57]** fulfilled. This is the complexity of why

**[07:57]** fulfilled. This is the complexity of why your software system exists in the first

**[07:58]** your software system exists in the first

**[07:58]** your software system exists in the first place. And then second, there's this


### [08:00 - 09:00]

**[08:01]** place. And then second, there's this

**[08:01]** place. And then second, there's this idea of accidental complexity.

**[08:03]** idea of accidental complexity.

**[08:03]** idea of accidental complexity. Everything else we've added along the

**[08:04]** Everything else we've added along the

**[08:04]** Everything else we've added along the way, workarounds, defensive code,

**[08:06]** way, workarounds, defensive code,

**[08:06]** way, workarounds, defensive code, frameworks, abstractions that made sense

**[08:08]** frameworks, abstractions that made sense

**[08:08]** frameworks, abstractions that made sense a while ago, it's all the stuff that we

**[08:10]** a while ago, it's all the stuff that we

**[08:10]** a while ago, it's all the stuff that we put together to make the code itself

**[08:11]** put together to make the code itself

**[08:11]** put together to make the code itself work.

**[08:13]** work.

**[08:13]** work. In a real codebase, these two types of

**[08:14]** In a real codebase, these two types of

**[08:14]** In a real codebase, these two types of complexity are everywhere and they get

**[08:17]** complexity are everywhere and they get

**[08:17]** complexity are everywhere and they get so tangled together that separating them

**[08:18]** so tangled together that separating them

**[08:18]** so tangled together that separating them requires context, history, and

**[08:19]** requires context, history, and

**[08:19]** requires context, history, and experience.

**[08:21]** experience.

**[08:21]** experience. the generated output makes no such

**[08:23]** the generated output makes no such

**[08:23]** the generated output makes no such distinction and so every pattern is

**[08:25]** distinction and so every pattern is

**[08:25]** distinction and so every pattern is keeps just getting preserved.

**[08:31]** So here's a real example from uh some

**[08:31]** So here's a real example from uh some work we're doing at Netflix. I have a

**[08:32]** work we're doing at Netflix. I have a

**[08:32]** work we're doing at Netflix. I have a system that has a abstraction layer

**[08:34]** system that has a abstraction layer

**[08:34]** system that has a abstraction layer sitting between our old authorization

**[08:35]** sitting between our old authorization

**[08:36]** sitting between our old authorization code we wrote say five or so years ago

**[08:38]** code we wrote say five or so years ago

**[08:38]** code we wrote say five or so years ago and a new centralized o system. We

**[08:41]** and a new centralized o system. We

**[08:41]** and a new centralized o system. We didn't have time to rebuild our whole

**[08:42]** didn't have time to rebuild our whole

**[08:42]** didn't have time to rebuild our whole app. So we just kind of put a shim in

**[08:43]** app. So we just kind of put a shim in

**[08:44]** app. So we just kind of put a shim in between. So now we have AI. This is a

**[08:46]** between. So now we have AI. This is a

**[08:46]** between. So now we have AI. This is a great opportunity to refactor our code

**[08:47]** great opportunity to refactor our code

**[08:47]** great opportunity to refactor our code to use the new system directly. Seems

**[08:49]** to use the new system directly. Seems

**[08:49]** to use the new system directly. Seems like a simple request, right?

**[08:52]** like a simple request, right?

**[08:52]** like a simple request, right? And no, it's like the old code was just

**[08:54]** And no, it's like the old code was just

**[08:54]** And no, it's like the old code was just so tightly coupled to its authorization

**[08:56]** so tightly coupled to its authorization

**[08:56]** so tightly coupled to its authorization patterns. Like we had permission checks

**[08:58]** patterns. Like we had permission checks

**[08:58]** patterns. Like we had permission checks woven through business logic, ro

**[08:59]** woven through business logic, ro

**[08:59]** woven through business logic, ro assumptions baked into data models and


### [09:00 - 10:00]

**[09:01]** assumptions baked into data models and

**[09:01]** assumptions baked into data models and off calls scattered across hundreds of

**[09:03]** off calls scattered across hundreds of

**[09:03]** off calls scattered across hundreds of files. The agent would start

**[09:05]** files. The agent would start

**[09:05]** files. The agent would start refactoring, get a few files in and hit

**[09:07]** refactoring, get a few files in and hit

**[09:07]** refactoring, get a few files in and hit a dependency couldn't untangle and just

**[09:09]** a dependency couldn't untangle and just

**[09:09]** a dependency couldn't untangle and just spiral out of control and give up or

**[09:11]** spiral out of control and give up or

**[09:11]** spiral out of control and give up or worse it would try and preserve some

**[09:13]** worse it would try and preserve some

**[09:13]** worse it would try and preserve some existing logic that from the old system

**[09:15]** existing logic that from the old system

**[09:16]** existing logic that from the old system and recreating it using the new system

**[09:17]** and recreating it using the new system

**[09:17]** and recreating it using the new system which I think is not great too.

**[09:21]** which I think is not great too.

**[09:21]** which I think is not great too. The thing is it couldn't see the scenes.

**[09:23]** The thing is it couldn't see the scenes.

**[09:23]** The thing is it couldn't see the scenes. It couldn't identify where the business

**[09:24]** It couldn't identify where the business

**[09:24]** It couldn't identify where the business logic ended and the off logic began.

**[09:26]** logic ended and the off logic began.

**[09:26]** logic ended and the off logic began. Everything was so tangled together that

**[09:28]** Everything was so tangled together that

**[09:28]** Everything was so tangled together that even with perfect information, the AI

**[09:31]** even with perfect information, the AI

**[09:31]** even with perfect information, the AI couldn't find a clean path through. When

**[09:33]** couldn't find a clean path through. When

**[09:33]** couldn't find a clean path through. When your accidental complexity gets this

**[09:34]** your accidental complexity gets this

**[09:34]** your accidental complexity gets this tangled, AI is not the best help to

**[09:37]** tangled, AI is not the best help to

**[09:37]** tangled, AI is not the best help to actually make it any better. I found it

**[09:39]** actually make it any better. I found it

**[09:39]** actually make it any better. I found it only adds more layers on top.

**[09:42]** only adds more layers on top.

**[09:42]** only adds more layers on top. We can tell the difference, or at least

**[09:43]** We can tell the difference, or at least

**[09:43]** We can tell the difference, or at least we can when we slow down enough to

**[09:45]** we can when we slow down enough to

**[09:45]** we can when we slow down enough to think. We know which patterns are

**[09:47]** think. We know which patterns are

**[09:47]** think. We know which patterns are essential and which are just how someone

**[09:48]** essential and which are just how someone

**[09:48]** essential and which are just how someone solved it a few years ago. We carry the

**[09:51]** solved it a few years ago. We carry the

**[09:51]** solved it a few years ago. We carry the context that the AI can infer, but only

**[09:53]** context that the AI can infer, but only

**[09:53]** context that the AI can infer, but only if we time to make take time to make

**[09:54]** if we time to make take time to make

**[09:54]** if we time to make take time to make these distinctions before we start.


### [10:00 - 11:00]

**[10:02]** So how do you actually do it? How do you

**[10:02]** So how do you actually do it? How do you separate the accidental and essential

**[10:04]** separate the accidental and essential

**[10:04]** separate the accidental and essential complexity when you're staring at a huge

**[10:05]** complexity when you're staring at a huge

**[10:05]** complexity when you're staring at a huge codebase? Codebase I work on Netflix has

**[10:08]** codebase? Codebase I work on Netflix has

**[10:08]** codebase? Codebase I work on Netflix has around a million lines of Java and the

**[10:10]** around a million lines of Java and the

**[10:10]** around a million lines of Java and the main service in it is about 5 million

**[10:11]** main service in it is about 5 million

**[10:11]** main service in it is about 5 million tokens last time I checked. no context

**[10:14]** tokens last time I checked. no context

**[10:14]** tokens last time I checked. no context window I have access to uh can hold it.

**[10:17]** window I have access to uh can hold it.

**[10:17]** window I have access to uh can hold it. So when I wanted to work with it, I

**[10:18]** So when I wanted to work with it, I

**[10:18]** So when I wanted to work with it, I first thought, hey, maybe I could just

**[10:19]** first thought, hey, maybe I could just

**[10:19]** first thought, hey, maybe I could just copy large swaths of this codebase into

**[10:21]** copy large swaths of this codebase into

**[10:21]** copy large swaths of this codebase into the into the context and see if the

**[10:23]** the into the context and see if the

**[10:23]** the into the context and see if the patterns were emerged, see if it would

**[10:24]** patterns were emerged, see if it would

**[10:24]** patterns were emerged, see if it would just be able to figure out what's

**[10:25]** just be able to figure out what's

**[10:25]** just be able to figure out what's happening. And just like the

**[10:27]** happening. And just like the

**[10:27]** happening. And just like the authorization refactor from previously,

**[10:28]** authorization refactor from previously,

**[10:28]** authorization refactor from previously, [clears throat] the output just got lost

**[10:29]** [clears throat] the output just got lost

**[10:30]** [clears throat] the output just got lost in its own complexity. So with this, I

**[10:32]** in its own complexity. So with this, I

**[10:32]** in its own complexity. So with this, I was forced to do something different. I

**[10:34]** was forced to do something different. I

**[10:34]** was forced to do something different. I had to select what to include. Design

**[10:35]** had to select what to include. Design

**[10:36]** had to select what to include. Design docs, architecture, diagrams, key

**[10:37]** docs, architecture, diagrams, key

**[10:37]** docs, architecture, diagrams, key interfaces, you name it, and take time

**[10:39]** interfaces, you name it, and take time

**[10:39]** interfaces, you name it, and take time writing out the requirements of how

**[10:40]** writing out the requirements of how

**[10:40]** writing out the requirements of how components should interact and what

**[10:42]** components should interact and what

**[10:42]** components should interact and what patterns to follow.

**[10:44]** patterns to follow.

**[10:44]** patterns to follow. See, I was writing a spec. Uh 5 million

**[10:47]** See, I was writing a spec. Uh 5 million

**[10:47]** See, I was writing a spec. Uh 5 million tokens became 2,000 words of

**[10:48]** tokens became 2,000 words of

**[10:48]** tokens became 2,000 words of specification. And then to take it even

**[10:50]** specification. And then to take it even

**[10:50]** specification. And then to take it even further, take that spec and create an

**[10:52]** further, take that spec and create an

**[10:52]** further, take that spec and create an exact step set of steps of code to

**[10:54]** exact step set of steps of code to

**[10:54]** exact step set of steps of code to execute. No vague instructions, just a

**[10:56]** execute. No vague instructions, just a

**[10:56]** execute. No vague instructions, just a precise sequence of operations. I found

**[10:58]** precise sequence of operations. I found

**[10:58]** precise sequence of operations. I found this produced much cleaner and more


### [11:00 - 12:00]

**[11:00]** this produced much cleaner and more

**[11:00]** this produced much cleaner and more focused code that I could understand. As

**[11:02]** focused code that I could understand. As

**[11:02]** focused code that I could understand. As I defined it first and planned its own

**[11:04]** I defined it first and planned its own

**[11:04]** I defined it first and planned its own execution,

**[11:10]** this became the approach which I called

**[11:10]** this became the approach which I called context compression a while ago. But you

**[11:11]** context compression a while ago. But you

**[11:11]** context compression a while ago. But you call it context engineering or

**[11:12]** call it context engineering or

**[11:12]** call it context engineering or spectriven development, whatever you

**[11:14]** spectriven development, whatever you

**[11:14]** spectriven development, whatever you want. The name doesn't matter. What only

**[11:17]** want. The name doesn't matter. What only

**[11:17]** want. The name doesn't matter. What only matters here is that thinking and

**[11:18]** matters here is that thinking and

**[11:18]** matters here is that thinking and planning become a majority of the work.

**[11:20]** planning become a majority of the work.

**[11:20]** planning become a majority of the work. So let me walk you through that how this

**[11:22]** So let me walk you through that how this

**[11:22]** So let me walk you through that how this works in practice.

**[11:24]** works in practice.

**[11:24]** works in practice. So we have step one, phase one,

**[11:25]** So we have step one, phase one,

**[11:25]** So we have step one, phase one, research. You know, I go and feed

**[11:27]** research. You know, I go and feed

**[11:27]** research. You know, I go and feed everything to it up front. Architecture

**[11:29]** everything to it up front. Architecture

**[11:29]** everything to it up front. Architecture diagrams, documentation, Slack threads.

**[11:31]** diagrams, documentation, Slack threads.

**[11:31]** diagrams, documentation, Slack threads. I been over this a bunch, but really

**[11:33]** I been over this a bunch, but really

**[11:33]** I been over this a bunch, but really just bring as much context as you can

**[11:34]** just bring as much context as you can

**[11:34]** just bring as much context as you can that's going to be relevant to the

**[11:35]** that's going to be relevant to the

**[11:35]** that's going to be relevant to the changes you're making. And then use the

**[11:38]** changes you're making. And then use the

**[11:38]** changes you're making. And then use the agent to analyze the codebase and map

**[11:39]** agent to analyze the codebase and map

**[11:39]** agent to analyze the codebase and map out the components and dependencies.

**[11:41]** out the components and dependencies.

**[11:42]** out the components and dependencies. This shouldn't be a oneshot process. I

**[11:43]** This shouldn't be a oneshot process. I

**[11:43]** This shouldn't be a oneshot process. I like to probe say like what about the

**[11:45]** like to probe say like what about the

**[11:45]** like to probe say like what about the caching? How does this handle failures?

**[11:47]** caching? How does this handle failures?

**[11:47]** caching? How does this handle failures? And when it's analysis is wrong, I'll

**[11:48]** And when it's analysis is wrong, I'll

**[11:48]** And when it's analysis is wrong, I'll correct it. And if it's missing context,

**[11:50]** correct it. And if it's missing context,

**[11:50]** correct it. And if it's missing context, I provide it. Each iteration refineses

**[11:53]** I provide it. Each iteration refineses

**[11:53]** I provide it. Each iteration refineses its analysis.

**[11:55]** its analysis.

**[11:55]** its analysis. The output here is a single research

**[11:56]** The output here is a single research

**[11:56]** The output here is a single research document. Here's what exists. Here's

**[11:58]** document. Here's what exists. Here's

**[11:58]** document. Here's what exists. Here's what connects to what. And here's what


### [12:00 - 13:00]

**[12:00]** what connects to what. And here's what

**[12:00]** what connects to what. And here's what your change will affect. Hours of

**[12:01]** your change will affect. Hours of

**[12:01]** your change will affect. Hours of exploration are compressed into minutes

**[12:03]** exploration are compressed into minutes

**[12:03]** exploration are compressed into minutes of reading.

**[12:05]** of reading.

**[12:05]** of reading. [snorts] I know Dex mentioned it this

**[12:07]** [snorts] I know Dex mentioned it this

**[12:07]** [snorts] I know Dex mentioned it this morning, but the human checkpoint here

**[12:08]** morning, but the human checkpoint here

**[12:08]** morning, but the human checkpoint here is critical. This is where you validate

**[12:10]** is critical. This is where you validate

**[12:10]** is critical. This is where you validate the analysis against reality. The

**[12:12]** the analysis against reality. The

**[12:12]** the analysis against reality. The highest leverage moment in the entire

**[12:14]** highest leverage moment in the entire

**[12:14]** highest leverage moment in the entire process. Catch errors here. Prevent

**[12:16]** process. Catch errors here. Prevent

**[12:16]** process. Catch errors here. Prevent disasters later.

**[12:19]** disasters later.

**[12:19]** disasters later. Onto phase two. Now that you have some

**[12:21]** Onto phase two. Now that you have some

**[12:21]** Onto phase two. Now that you have some valid research in hand, we create a

**[12:22]** valid research in hand, we create a

**[12:22]** valid research in hand, we create a detailed imple implementation plan. Real

**[12:24]** detailed imple implementation plan. Real

**[12:24]** detailed imple implementation plan. Real code structure, function signatures,

**[12:26]** code structure, function signatures,

**[12:26]** code structure, function signatures, type definitions, data flow. You want

**[12:28]** type definitions, data flow. You want

**[12:28]** type definitions, data flow. You want this to be so any developer can follow

**[12:30]** this to be so any developer can follow

**[12:30]** this to be so any developer can follow it. I I kind of liken it to paint by

**[12:32]** it. I I kind of liken it to paint by

**[12:32]** it. I I kind of liken it to paint by numbers. You should be able to hand it

**[12:33]** numbers. You should be able to hand it

**[12:33]** numbers. You should be able to hand it to your most junior engineer and say,

**[12:34]** to your most junior engineer and say,

**[12:34]** to your most junior engineer and say, "Go do this." And if they copy it line

**[12:37]** "Go do this." And if they copy it line

**[12:37]** "Go do this." And if they copy it line by line, it should just work.

**[12:40]** by line, it should just work.

**[12:40]** by line, it should just work. This step is where we make a lot of the

**[12:41]** This step is where we make a lot of the

**[12:41]** This step is where we make a lot of the important architectural decisions. You

**[12:43]** important architectural decisions. You

**[12:43]** important architectural decisions. You know, make sure complex logic is

**[12:45]** know, make sure complex logic is

**[12:45]** know, make sure complex logic is correct. Make sure business requirements

**[12:47]** correct. Make sure business requirements

**[12:47]** correct. Make sure business requirements are, you know, following good practice.

**[12:50]** are, you know, following good practice.

**[12:50]** are, you know, following good practice. Make sure there's good service

**[12:51]** Make sure there's good service

**[12:51]** Make sure there's good service boundaries, clean separation, and

**[12:52]** boundaries, clean separation, and

**[12:52]** boundaries, clean separation, and preventing any unnecessary coupling. We

**[12:54]** preventing any unnecessary coupling. We

**[12:54]** preventing any unnecessary coupling. We spot the problems before they happen

**[12:56]** spot the problems before they happen

**[12:56]** spot the problems before they happen because we've lived through them. AI

**[12:58]** because we've lived through them. AI

**[12:58]** because we've lived through them. AI doesn't have that option. It treats

**[12:59]** doesn't have that option. It treats

**[12:59]** doesn't have that option. It treats every pattern as a requirement.


### [13:00 - 14:00]

**[13:02]** every pattern as a requirement.

**[13:02]** every pattern as a requirement. The real magic in this step is the

**[13:04]** The real magic in this step is the

**[13:04]** The real magic in this step is the review speed. We can validate this plan

**[13:06]** review speed. We can validate this plan

**[13:06]** review speed. We can validate this plan in minutes and know exactly what's going

**[13:08]** in minutes and know exactly what's going

**[13:08]** in minutes and know exactly what's going to be built. And in order to keep up

**[13:10]** to be built. And in order to keep up

**[13:10]** to be built. And in order to keep up with the speed at which we want to

**[13:12]** with the speed at which we want to

**[13:12]** with the speed at which we want to generate code, we need to be able to

**[13:13]** generate code, we need to be able to

**[13:13]** generate code, we need to be able to comprehend what we're doing just as

**[13:15]** comprehend what we're doing just as

**[13:15]** comprehend what we're doing just as fast.

**[13:17]** fast.

**[13:17]** fast. Lastly, we have implementation. And now

**[13:20]** Lastly, we have implementation. And now

**[13:20]** Lastly, we have implementation. And now that we have a clear plan and like

**[13:21]** that we have a clear plan and like

**[13:22]** that we have a clear plan and like backed by a clear research, this phase

**[13:24]** backed by a clear research, this phase

**[13:24]** backed by a clear research, this phase should be pretty simple. And that's the

**[13:27]** should be pretty simple. And that's the

**[13:27]** should be pretty simple. And that's the point. You know, when AI has a clear

**[13:29]** point. You know, when AI has a clear

**[13:29]** point. You know, when AI has a clear specification to follow, the context

**[13:31]** specification to follow, the context

**[13:31]** specification to follow, the context remains clean and focused. We've

**[13:33]** remains clean and focused. We've

**[13:33]** remains clean and focused. We've prevented the complexity spiral of long

**[13:34]** prevented the complexity spiral of long

**[13:34]** prevented the complexity spiral of long conversations. And instead of 50

**[13:36]** conversations. And instead of 50

**[13:36]** conversations. And instead of 50 messages of evolutionary code, we have

**[13:38]** messages of evolutionary code, we have

**[13:38]** messages of evolutionary code, we have three focused outputs, each validated

**[13:40]** three focused outputs, each validated

**[13:40]** three focused outputs, each validated before proceeding. No abandoned

**[13:42]** before proceeding. No abandoned

**[13:42]** before proceeding. No abandoned approaches, no conflicting patterns, no

**[13:44]** approaches, no conflicting patterns, no

**[13:44]** approaches, no conflicting patterns, no wait actually moments that leave dead

**[13:46]** wait actually moments that leave dead

**[13:46]** wait actually moments that leave dead code everywhere.

**[13:48]** code everywhere.

**[13:48]** code everywhere. To me, what I see is the real payoff of

**[13:50]** To me, what I see is the real payoff of

**[13:50]** To me, what I see is the real payoff of this is that you can use a background

**[13:51]** this is that you can use a background

**[13:51]** this is that you can use a background agent to do a lot of this work because

**[13:53]** agent to do a lot of this work because

**[13:53]** agent to do a lot of this work because you've done all the thinking and hard

**[13:55]** you've done all the thinking and hard

**[13:55]** you've done all the thinking and hard work ahead of time. It can just start

**[13:57]** work ahead of time. It can just start

**[13:57]** work ahead of time. It can just start the implementation. You can go work on

**[13:59]** the implementation. You can go work on

**[13:59]** the implementation. You can go work on something else and come back to review


### [14:00 - 15:00]

**[14:01]** something else and come back to review

**[14:01]** something else and come back to review and you can review this quickly because

**[14:03]** and you can review this quickly because

**[14:03]** and you can review this quickly because you're just verifying it's conforming to

**[14:04]** you're just verifying it's conforming to

**[14:04]** you're just verifying it's conforming to your plan, not trying to understand if

**[14:06]** your plan, not trying to understand if

**[14:06]** your plan, not trying to understand if anything got invented.

**[14:11]** The thing here is we're not using AI to

**[14:12]** The thing here is we're not using AI to think for us. We're using it to

**[14:13]** think for us. We're using it to

**[14:13]** think for us. We're using it to accelerate the mechanical parts while

**[14:15]** accelerate the mechanical parts while

**[14:15]** accelerate the mechanical parts while maintaining our ability to understand

**[14:16]** maintaining our ability to understand

**[14:16]** maintaining our ability to understand it. Research is faster, planning is more

**[14:19]** it. Research is faster, planning is more

**[14:19]** it. Research is faster, planning is more thorough, and the implementation is

**[14:20]** thorough, and the implementation is

**[14:20]** thorough, and the implementation is cleaner. The thinking, the synthesis,

**[14:23]** cleaner. The thinking, the synthesis,

**[14:23]** cleaner. The thinking, the synthesis, and the judgment though that remains

**[14:25]** and the judgment though that remains

**[14:25]** and the judgment though that remains with us.

**[14:32]** So remember that uh authorization

**[14:32]** So remember that uh authorization refactor I said that AI couldn't handle.

**[14:34]** refactor I said that AI couldn't handle.

**[14:34]** refactor I said that AI couldn't handle. The thing is now we're actually, you

**[14:36]** The thing is now we're actually, you

**[14:36]** The thing is now we're actually, you know, working on it now starting to make

**[14:37]** know, working on it now starting to make

**[14:37]** know, working on it now starting to make some good progress on it. The thing is

**[14:40]** some good progress on it. The thing is

**[14:40]** some good progress on it. The thing is it's not because we found better

**[14:41]** it's not because we found better

**[14:41]** it's not because we found better prompts. We found we couldn't even jump

**[14:43]** prompts. We found we couldn't even jump

**[14:43]** prompts. We found we couldn't even jump into doing any sort of research,

**[14:45]** into doing any sort of research,

**[14:45]** into doing any sort of research, planning, implementation. We actually

**[14:46]** planning, implementation. We actually

**[14:46]** planning, implementation. We actually had to go make this change ourself by

**[14:48]** had to go make this change ourself by

**[14:48]** had to go make this change ourself by hand. No AI, just reading the code,

**[14:51]** hand. No AI, just reading the code,

**[14:51]** hand. No AI, just reading the code, understanding dependencies, and making

**[14:52]** understanding dependencies, and making

**[14:52]** understanding dependencies, and making changes to see what broke. That manual

**[14:55]** changes to see what broke. That manual

**[14:55]** changes to see what broke. That manual migration was, I'll be honest, it was a

**[14:57]** migration was, I'll be honest, it was a

**[14:57]** migration was, I'll be honest, it was a pain, but it was crucial. It revealed

**[14:59]** pain, but it was crucial. It revealed

**[14:59]** pain, but it was crucial. It revealed all the hidden constraints, which


### [15:00 - 16:00]

**[15:01]** all the hidden constraints, which

**[15:01]** all the hidden constraints, which invariants had to hold true, and which

**[15:02]** invariants had to hold true, and which

**[15:02]** invariants had to hold true, and which services would break if the off changed.

**[15:05]** services would break if the off changed.

**[15:05]** services would break if the off changed. things no amount of code an analysis

**[15:07]** things no amount of code an analysis

**[15:07]** things no amount of code an analysis would have surfaced for us. And then we

**[15:09]** would have surfaced for us. And then we

**[15:09]** would have surfaced for us. And then we fed that pull request of the actual

**[15:12]** fed that pull request of the actual

**[15:12]** fed that pull request of the actual manual migration into our research

**[15:14]** manual migration into our research

**[15:14]** manual migration into our research process and had it use that as the seed

**[15:16]** process and had it use that as the seed

**[15:16]** process and had it use that as the seed for any sort of research going forward.

**[15:18]** for any sort of research going forward.

**[15:18]** for any sort of research going forward. The AI could then see what a clean

**[15:22]** The AI could then see what a clean

**[15:22]** The AI could then see what a clean migration looks like. The thing is each

**[15:24]** migration looks like. The thing is each

**[15:24]** migration looks like. The thing is each of these entities are slightly

**[15:26]** of these entities are slightly

**[15:26]** of these entities are slightly different. So we have to go and

**[15:27]** different. So we have to go and

**[15:27]** different. So we have to go and interrogate it and say hey what do we

**[15:28]** interrogate it and say hey what do we

**[15:28]** interrogate it and say hey what do we about do about this? Some things are

**[15:30]** about do about this? Some things are

**[15:30]** about do about this? Some things are encrypted some things are not. We had to

**[15:32]** encrypted some things are not. We had to

**[15:32]** encrypted some things are not. We had to provide that extra context each time uh

**[15:34]** provide that extra context each time uh

**[15:34]** provide that extra context each time uh through a bunch of iteration.

**[15:37]** through a bunch of iteration.

**[15:37]** through a bunch of iteration. Then and only then we could generate a

**[15:39]** Then and only then we could generate a

**[15:39]** Then and only then we could generate a plan that might work in one shot. And

**[15:42]** plan that might work in one shot. And

**[15:42]** plan that might work in one shot. And the key and might's the key word here is

**[15:44]** the key and might's the key word here is

**[15:44]** the key and might's the key word here is we're still validating, still adjusting,

**[15:46]** we're still validating, still adjusting,

**[15:46]** we're still validating, still adjusting, and still discovering edge cases.

**[15:54]** The three-phase approach is not magic.

**[15:54]** The three-phase approach is not magic. It only works because we did this one

**[15:56]** It only works because we did this one

**[15:56]** It only works because we did this one migration by hand. We had to earn the

**[15:58]** migration by hand. We had to earn the

**[15:58]** migration by hand. We had to earn the understanding before we can code into

**[15:59]** understanding before we can code into

**[15:59]** understanding before we can code into our process. I still think there's no


### [16:00 - 17:00]

**[16:01]** our process. I still think there's no

**[16:02]** our process. I still think there's no silver bullet. I don't think there's

**[16:03]** silver bullet. I don't think there's

**[16:03]** silver bullet. I don't think there's better prompts, better models, or even

**[16:04]** better prompts, better models, or even

**[16:04]** better prompts, better models, or even writing better specs, just the work of

**[16:07]** writing better specs, just the work of

**[16:07]** writing better specs, just the work of understanding your system deeply enough

**[16:08]** understanding your system deeply enough

**[16:08]** understanding your system deeply enough that you can make changes to it safely.

**[16:16]** So why go through with all this? Like

**[16:16]** So why go through with all this? Like why not just iterate with AI until it

**[16:17]** why not just iterate with AI until it

**[16:17]** why not just iterate with AI until it works? Like eventually won't models get

**[16:19]** works? Like eventually won't models get

**[16:19]** works? Like eventually won't models get strong enough and it just works. The

**[16:21]** strong enough and it just works. The

**[16:21]** strong enough and it just works. The thing to me is it works isn't enough.

**[16:24]** thing to me is it works isn't enough.

**[16:24]** thing to me is it works isn't enough. There's a difference between code that

**[16:26]** There's a difference between code that

**[16:26]** There's a difference between code that passes test and code that survives in

**[16:27]** passes test and code that survives in

**[16:27]** passes test and code that survives in production. between systems that

**[16:30]** production. between systems that

**[16:30]** production. between systems that function today and systems that that can

**[16:32]** function today and systems that that can

**[16:32]** function today and systems that that can be changed by someone else in the

**[16:34]** be changed by someone else in the

**[16:34]** be changed by someone else in the future. The real problem here is a

**[16:37]** future. The real problem here is a

**[16:37]** future. The real problem here is a knowledge gap. When AI can generate

**[16:39]** knowledge gap. When AI can generate

**[16:39]** knowledge gap. When AI can generate thousands of lines of code in seconds,

**[16:41]** thousands of lines of code in seconds,

**[16:41]** thousands of lines of code in seconds, understanding it could take you hours,

**[16:43]** understanding it could take you hours,

**[16:43]** understanding it could take you hours, maybe days if it's complex. Who knows,

**[16:46]** maybe days if it's complex. Who knows,

**[16:46]** maybe days if it's complex. Who knows, maybe never if it's really that tangled.

**[16:50]** maybe never if it's really that tangled.

**[16:50]** maybe never if it's really that tangled. And here's something that I don't think

**[16:51]** And here's something that I don't think

**[16:51]** And here's something that I don't think many people are even talking about this

**[16:52]** many people are even talking about this

**[16:52]** many people are even talking about this point. Every time we skip thinking to

**[16:54]** point. Every time we skip thinking to

**[16:54]** point. Every time we skip thinking to keep up with generation speed, we're not

**[16:56]** keep up with generation speed, we're not

**[16:56]** keep up with generation speed, we're not just adding code that we don't

**[16:57]** just adding code that we don't

**[16:57]** just adding code that we don't understand. We're losing our ability to

**[16:59]** understand. We're losing our ability to

**[16:59]** understand. We're losing our ability to recognize problems. That instinct that


### [17:00 - 18:00]

**[17:01]** recognize problems. That instinct that

**[17:01]** recognize problems. That instinct that says, "Hey, this is getting complex." It

**[17:04]** says, "Hey, this is getting complex." It

**[17:04]** says, "Hey, this is getting complex." It atrophies when you don't understand your

**[17:05]** atrophies when you don't understand your

**[17:05]** atrophies when you don't understand your own system.

**[17:07]** own system.

**[17:07]** own system. [snorts]

**[17:09]** [snorts]

**[17:09]** [snorts] Pattern recognition comes from

**[17:10]** Pattern recognition comes from

**[17:10]** Pattern recognition comes from experience. When I spot a dangerous

**[17:12]** experience. When I spot a dangerous

**[17:12]** experience. When I spot a dangerous architecture, it's because I'm the one

**[17:13]** architecture, it's because I'm the one

**[17:13]** architecture, it's because I'm the one up at 3:00 in the morning dealing with

**[17:15]** up at 3:00 in the morning dealing with

**[17:15]** up at 3:00 in the morning dealing with it. When I push for simpler solutions,

**[17:17]** it. When I push for simpler solutions,

**[17:17]** it. When I push for simpler solutions, it's because I've had to maintain the

**[17:19]** it's because I've had to maintain the

**[17:19]** it's because I've had to maintain the alternative from someone else. AI

**[17:22]** alternative from someone else. AI

**[17:22]** alternative from someone else. AI generates what you ask it for. It

**[17:23]** generates what you ask it for. It

**[17:23]** generates what you ask it for. It doesn't encode lessons from past

**[17:25]** doesn't encode lessons from past

**[17:25]** doesn't encode lessons from past failures.

**[17:27]** failures.

**[17:27]** failures. The three-phase approach bridges this

**[17:28]** The three-phase approach bridges this

**[17:28]** The three-phase approach bridges this gap. It compresses understanding into

**[17:30]** gap. It compresses understanding into

**[17:30]** gap. It compresses understanding into artifacts we can review at the speed of

**[17:32]** artifacts we can review at the speed of

**[17:32]** artifacts we can review at the speed of generation. Without it, we're just

**[17:34]** generation. Without it, we're just

**[17:34]** generation. Without it, we're just accumulating complexity faster than we

**[17:36]** accumulating complexity faster than we

**[17:36]** accumulating complexity faster than we can comprehend it.

**[17:42]** AI changes everything about how we write

**[17:42]** AI changes everything about how we write code. But honestly, I don't think it

**[17:44]** code. But honestly, I don't think it

**[17:44]** code. But honestly, I don't think it changes anything about why software

**[17:46]** changes anything about why software

**[17:46]** changes anything about why software itself fails. Every generation has faced

**[17:48]** itself fails. Every generation has faced

**[17:48]** itself fails. Every generation has faced their own software crisis. Dystra's

**[17:51]** their own software crisis. Dystra's

**[17:51]** their own software crisis. Dystra's generation faced it by creating the

**[17:52]** generation faced it by creating the

**[17:52]** generation faced it by creating the discipline of software engineering. And

**[17:54]** discipline of software engineering. And

**[17:54]** discipline of software engineering. And now we face ours with infinite code

**[17:56]** now we face ours with infinite code

**[17:56]** now we face ours with infinite code generation.

**[17:58]** generation.

**[17:58]** generation. I don't think the solution is another

**[17:59]** I don't think the solution is another

**[17:59]** I don't think the solution is another tool or methodology. It's remembering


### [18:00 - 19:00]

**[18:01]** tool or methodology. It's remembering

**[18:01]** tool or methodology. It's remembering what we've always known. That software

**[18:03]** what we've always known. That software

**[18:03]** what we've always known. That software is a human endeavor. The hard part was

**[18:05]** is a human endeavor. The hard part was

**[18:06]** is a human endeavor. The hard part was never typing the code. It was knowing

**[18:07]** never typing the code. It was knowing

**[18:07]** never typing the code. It was knowing what to type in the first place. The

**[18:09]** what to type in the first place. The

**[18:09]** what to type in the first place. The developers who thrive won't just be the

**[18:11]** developers who thrive won't just be the

**[18:11]** developers who thrive won't just be the ones who generate the most code, but

**[18:13]** ones who generate the most code, but

**[18:13]** ones who generate the most code, but they'll be the ones who understand what

**[18:15]** they'll be the ones who understand what

**[18:15]** they'll be the ones who understand what they're building, who can still see the

**[18:16]** they're building, who can still see the

**[18:16]** they're building, who can still see the seams, who can recognize that they're

**[18:17]** seams, who can recognize that they're

**[18:18]** seams, who can recognize that they're solving the wrong problem. That's still

**[18:20]** solving the wrong problem. That's still

**[18:20]** solving the wrong problem. That's still us. That will only be us.

**[18:23]** us. That will only be us.

**[18:23]** us. That will only be us. I want to leave on a question and I

**[18:24]** I want to leave on a question and I

**[18:24]** I want to leave on a question and I don't think the question is whether or

**[18:25]** don't think the question is whether or

**[18:25]** don't think the question is whether or not we will use AI. That's a foregone

**[18:27]** not we will use AI. That's a foregone

**[18:27]** not we will use AI. That's a foregone conclusion. The ship has already sailed.

**[18:30]** conclusion. The ship has already sailed.

**[18:30]** conclusion. The ship has already sailed. To me, the question is going to be

**[18:31]** To me, the question is going to be

**[18:31]** To me, the question is going to be whether we will still understand our own

**[18:33]** whether we will still understand our own

**[18:33]** whether we will still understand our own systems when AI is writing most of our

**[18:34]** systems when AI is writing most of our

**[18:34]** systems when AI is writing most of our code.

**[18:37]** code.

**[18:37]** code. Thank you. [applause]

**[18:40]** Thank you. [applause]

**[18:40]** Thank you. [applause] [music]


