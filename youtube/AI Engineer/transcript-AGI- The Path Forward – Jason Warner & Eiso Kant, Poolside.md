# AGI- The Path Forward – Jason Warner & Eiso Kant, Poolside

**Video URL:** https://www.youtube.com/watch?v=OGCG_QkCcZo

---

## Full Transcript

### [00:00 - 01:00]

**[00:23]** How many people here know what poolside

**[00:23]** How many people here know what poolside is and does? Anyone? Anyone? Yeah. So,

**[00:28]** is and does? Anyone? Anyone? Yeah. So,

**[00:28]** is and does? Anyone? Anyone? Yeah. So, let's talk about that real quickly.

**[00:30]** let's talk about that real quickly.

**[00:30]** let's talk about that real quickly. Poolside exists to close the gap between

**[00:33]** Poolside exists to close the gap between

**[00:33]** Poolside exists to close the gap between models and human intelligence. That's

**[00:35]** models and human intelligence. That's

**[00:35]** models and human intelligence. That's literally it. That's what we're here to

**[00:37]** literally it. That's what we're here to

**[00:37]** literally it. That's what we're here to go do. We're building our own models

**[00:39]** go do. We're building our own models

**[00:39]** go do. We're building our own models from scratch to do this. We're based on

**[00:41]** from scratch to do this. We're based on

**[00:41]** from scratch to do this. We're based on the idea 2 and a half years ago that we

**[00:43]** the idea 2 and a half years ago that we

**[00:43]** the idea 2 and a half years ago that we thought next token prediction was an

**[00:45]** thought next token prediction was an

**[00:46]** thought next token prediction was an amazing techn technological

**[00:47]** amazing techn technological

**[00:47]** amazing techn technological breakthrough, but it need to be paired

**[00:49]** breakthrough, but it need to be paired

**[00:49]** breakthrough, but it need to be paired with reinforcement learning really to

**[00:51]** with reinforcement learning really to

**[00:51]** with reinforcement learning really to make that leap. So that's what we've

**[00:54]** make that leap. So that's what we've

**[00:54]** make that leap. So that's what we've been doing for the past 2 and a half

**[00:55]** been doing for the past 2 and a half

**[00:56]** been doing for the past 2 and a half years. So we're on our second generation

**[00:57]** years. So we're on our second generation

**[00:57]** years. So we're on our second generation of models now, Malibu agent. And instead


### [01:00 - 02:00]

**[01:00]** of models now, Malibu agent. And instead

**[01:00]** of models now, Malibu agent. And instead of kind of like walking you through some

**[01:03]** of kind of like walking you through some

**[01:03]** of kind of like walking you through some slides and all that, we just thought

**[01:04]** slides and all that, we just thought

**[01:04]** slides and all that, we just thought maybe I don't know, let's kind of show

**[01:06]** maybe I don't know, let's kind of show

**[01:06]** maybe I don't know, let's kind of show you what we're doing here. So

**[01:09]** you what we're doing here. So

**[01:09]** you what we're doing here. So are you there?

**[01:10]** are you there?

**[01:10]** are you there? >> I got you, Jason.

**[01:11]** >> I got you, Jason.

**[01:11]** >> I got you, Jason. >> So as I said, you were supposed to see

**[01:13]** >> So as I said, you were supposed to see

**[01:13]** >> So as I said, you were supposed to see him today, but there's

**[01:16]** him today, but there's

**[01:16]** him today, but there's I don't know. Our airline system kind of

**[01:18]** I don't know. Our airline system kind of

**[01:18]** I don't know. Our airline system kind of works sometimes, maybe. So he's stuck in

**[01:20]** works sometimes, maybe. So he's stuck in

**[01:20]** works sometimes, maybe. So he's stuck in California, but uh we thought we'd just

**[01:23]** California, but uh we thought we'd just

**[01:23]** California, but uh we thought we'd just walk you kind of through some um some

**[01:25]** walk you kind of through some um some

**[01:25]** walk you kind of through some um some demos here today. So what you're looking

**[01:27]** demos here today. So what you're looking

**[01:27]** demos here today. So what you're looking at here is a very modern programming

**[01:29]** at here is a very modern programming

**[01:29]** at here is a very modern programming language that the government uses to run

**[01:31]** language that the government uses to run

**[01:31]** language that the government uses to run all the world's critical infrastructure

**[01:33]** all the world's critical infrastructure

**[01:33]** all the world's critical infrastructure called ADA. Anyone familiar with ADA?

**[01:37]** called ADA. Anyone familiar with ADA?

**[01:37]** called ADA. Anyone familiar with ADA? >> Yes. Yes. Okay. So everyone I saw put

**[01:39]** >> Yes. Yes. Okay. So everyone I saw put

**[01:39]** >> Yes. Yes. Okay. So everyone I saw put their hands up for ADA either has no

**[01:40]** their hands up for ADA either has no

**[01:40]** their hands up for ADA either has no hair or gray hair like me. So that

**[01:43]** hair or gray hair like me. So that

**[01:43]** hair or gray hair like me. So that should tell you what's going on here. So

**[01:45]** should tell you what's going on here. So

**[01:45]** should tell you what's going on here. So ISO, why don't we uh why don't we figure

**[01:48]** ISO, why don't we uh why don't we figure

**[01:48]** ISO, why don't we uh why don't we figure out what's going on with this codebase

**[01:50]** out what's going on with this codebase

**[01:50]** out what's going on with this codebase here?

**[01:51]** here?

**[01:51]** here? >> Well, let's start asking what the

**[01:52]** >> Well, let's start asking what the

**[01:52]** >> Well, let's start asking what the codebase is about.

**[01:54]** codebase is about.

**[01:54]** codebase is about. >> That's great. And what you're seeing

**[01:55]** >> That's great. And what you're seeing

**[01:55]** >> That's great. And what you're seeing here is obviously our assistant in in

**[01:57]** here is obviously our assistant in in

**[01:57]** here is obviously our assistant in in Visual Studio Code backed by poolside


### [02:00 - 03:00]

**[02:01]** Visual Studio Code backed by poolside

**[02:01]** Visual Studio Code backed by poolside agent, a model we train from scratch

**[02:03]** agent, a model we train from scratch

**[02:03]** agent, a model we train from scratch using our proprietary techniques. Um,

**[02:06]** using our proprietary techniques. Um,

**[02:06]** using our proprietary techniques. Um, and you can see what's going on here.

**[02:07]** and you can see what's going on here.

**[02:07]** and you can see what's going on here. Kind of the stuff you expect from an

**[02:09]** Kind of the stuff you expect from an

**[02:09]** Kind of the stuff you expect from an agent. Uh and obviously the form factors

**[02:11]** agent. Uh and obviously the form factors

**[02:11]** agent. Uh and obviously the form factors of all of these things are going to

**[02:12]** of all of these things are going to

**[02:12]** of all of these things are going to change a couple of times over the next

**[02:14]** change a couple of times over the next

**[02:14]** change a couple of times over the next couple of years, but you know people

**[02:15]** couple of years, but you know people

**[02:15]** couple of years, but you know people seem to like VS Code. Uh so we're going

**[02:17]** seem to like VS Code. Uh so we're going

**[02:18]** seem to like VS Code. Uh so we're going to you know show you this demo here

**[02:19]** to you know show you this demo here

**[02:19]** to you know show you this demo here today. So you can see from this it kind

**[02:21]** today. So you can see from this it kind

**[02:21]** today. So you can see from this it kind of went through told you what this

**[02:22]** of went through told you what this

**[02:22]** of went through told you what this codebase is all about but um you know

**[02:26]** codebase is all about but um you know

**[02:26]** codebase is all about but um you know these things run in our satellites and

**[02:29]** these things run in our satellites and

**[02:29]** these things run in our satellites and uh I don't know anything about ADA but I

**[02:31]** uh I don't know anything about ADA but I

**[02:31]** uh I don't know anything about ADA but I do know a lot about a couple of other

**[02:32]** do know a lot about a couple of other

**[02:32]** do know a lot about a couple of other programming languages. So uh ISO what do

**[02:35]** programming languages. So uh ISO what do

**[02:35]** programming languages. So uh ISO what do we want to do here? Why don't we uh see

**[02:37]** we want to do here? Why don't we uh see

**[02:37]** we want to do here? Why don't we uh see what this thing might look like in Rust?

**[02:39]** what this thing might look like in Rust?

**[02:39]** what this thing might look like in Rust? Let's do it. Let's ask it convert this

**[02:42]** Let's do it. Let's ask it convert this

**[02:42]** Let's do it. Let's ask it convert this database to rest.

**[02:48]** >> So obviously you're going to see what's

**[02:48]** >> So obviously you're going to see what's going on here. Again, if you guys have

**[02:50]** going on here. Again, if you guys have

**[02:50]** going on here. Again, if you guys have used other tools, you're not going to

**[02:51]** used other tools, you're not going to

**[02:51]** used other tools, you're not going to expect too much of the difference for

**[02:53]** expect too much of the difference for

**[02:53]** expect too much of the difference for what's happening here. Except that

**[02:54]** what's happening here. Except that

**[02:54]** what's happening here. Except that again, we're backed by our own model.

**[02:56]** again, we're backed by our own model.

**[02:56]** again, we're backed by our own model. We're not using Open AI. We're not using

**[02:58]** We're not using Open AI. We're not using

**[02:58]** We're not using Open AI. We're not using Anthropic. This is poolside. And


### [03:00 - 04:00]

**[03:00]** Anthropic. This is poolside. And

**[03:00]** Anthropic. This is poolside. And poolside is a bottom and top stack that

**[03:03]** poolside is a bottom and top stack that

**[03:03]** poolside is a bottom and top stack that is right now if no one's touched it and

**[03:05]** is right now if no one's touched it and

**[03:05]** is right now if no one's touched it and I know no one in this room has touched

**[03:07]** I know no one in this room has touched

**[03:07]** I know no one in this room has touched this unless you work for a three-letter

**[03:08]** this unless you work for a three-letter

**[03:08]** this unless you work for a three-letter agency, a defense contractor, or you've

**[03:11]** agency, a defense contractor, or you've

**[03:11]** agency, a defense contractor, or you've sent missiles somewhere that we're not

**[03:14]** sent missiles somewhere that we're not

**[03:14]** sent missiles somewhere that we're not going to talk about in this session. Um

**[03:16]** going to talk about in this session. Um

**[03:16]** going to talk about in this session. Um because that's where we're working.

**[03:17]** because that's where we're working.

**[03:17]** because that's where we're working. We're working in high consequence code

**[03:18]** We're working in high consequence code

**[03:18]** We're working in high consequence code environments for the last year inside

**[03:20]** environments for the last year inside

**[03:20]** environments for the last year inside the the government and the the defense

**[03:22]** the the government and the the defense

**[03:22]** the the government and the the defense sector. Um as you can see from this

**[03:24]** sector. Um as you can see from this

**[03:24]** sector. Um as you can see from this demo. Um so what you see here is is kind

**[03:27]** demo. Um so what you see here is is kind

**[03:27]** demo. Um so what you see here is is kind of going through doing the conversions.

**[03:29]** of going through doing the conversions.

**[03:29]** of going through doing the conversions. What you see in the middle pane is

**[03:31]** What you see in the middle pane is

**[03:31]** What you see in the middle pane is something that we built to kind of show

**[03:33]** something that we built to kind of show

**[03:33]** something that we built to kind of show you as the streams come through all the

**[03:35]** you as the streams come through all the

**[03:35]** you as the streams come through all the different changes that are happening.

**[03:37]** different changes that are happening.

**[03:37]** different changes that are happening. Um, one of the tricky parts about

**[03:39]** Um, one of the tricky parts about

**[03:39]** Um, one of the tricky parts about working on inside the defense sector and

**[03:41]** working on inside the defense sector and

**[03:41]** working on inside the defense sector and things like that is you can't have an

**[03:43]** things like that is you can't have an

**[03:43]** things like that is you can't have an agent that's just going to run around

**[03:44]** agent that's just going to run around

**[03:44]** agent that's just going to run around and do stuff. I mean like I can't walk

**[03:46]** and do stuff. I mean like I can't walk

**[03:46]** and do stuff. I mean like I can't walk into half of these buildings. You can't

**[03:47]** into half of these buildings. You can't

**[03:47]** into half of these buildings. You can't give an agent access to these data

**[03:48]** give an agent access to these data

**[03:48]** give an agent access to these data source and just say, "Hey, go nuts." You

**[03:51]** source and just say, "Hey, go nuts." You

**[03:51]** source and just say, "Hey, go nuts." You need to have the right permissions. You

**[03:52]** need to have the right permissions. You

**[03:52]** need to have the right permissions. You got to actually really ratchet these

**[03:54]** got to actually really ratchet these

**[03:54]** got to actually really ratchet these things down to do things inside those

**[03:56]** things down to do things inside those

**[03:56]** things down to do things inside those environments that you know they feel

**[03:59]** environments that you know they feel

**[03:59]** environments that you know they feel comfortable with. So, uh, where are we


### [04:00 - 05:00]

**[04:01]** comfortable with. So, uh, where are we

**[04:01]** comfortable with. So, uh, where are we on this now? What is is it trying to fix

**[04:03]** on this now? What is is it trying to fix

**[04:03]** on this now? What is is it trying to fix itself yet? Yes, it's it wrote about

**[04:07]** itself yet? Yes, it's it wrote about

**[04:07]** itself yet? Yes, it's it wrote about 1152 lines of code. Uh, and it just

**[04:10]** 1152 lines of code. Uh, and it just

**[04:10]** 1152 lines of code. Uh, and it just popped up a command start and tested,

**[04:15]** popped up a command start and tested,

**[04:15]** popped up a command start and tested, excuse me. Uh, so we see here all the

**[04:17]** excuse me. Uh, so we see here all the

**[04:17]** excuse me. Uh, so we see here all the files on the left hand side that it

**[04:19]** files on the left hand side that it

**[04:19]** files on the left hand side that it created. Uh this is essentially our live

**[04:21]** created. Uh this is essentially our live

**[04:21]** created. Uh this is essentially our live diff view that's available.

**[04:24]** diff view that's available.

**[04:24]** diff view that's available. Uh and as we see it's currently starting

**[04:26]** Uh and as we see it's currently starting

**[04:26]** Uh and as we see it's currently starting to actually test it out.

**[04:35]** So this is the part where we just sit

**[04:35]** So this is the part where we just sit here and watch this for 3 minutes and I

**[04:36]** here and watch this for 3 minutes and I

**[04:36]** here and watch this for 3 minutes and I see nothing.

**[04:38]** see nothing.

**[04:38]** see nothing. >> No. What you see

**[04:38]** >> No. What you see

**[04:38]** >> No. What you see >> the good thing is that this is a very

**[04:40]** >> the good thing is that this is a very

**[04:40]** >> the good thing is that this is a very fast inference.

**[04:41]** fast inference.

**[04:41]** fast inference. >> Yes.

**[04:41]** >> Yes.

**[04:41]** >> Yes. >> So 1100 lines of code.

**[04:43]** >> So 1100 lines of code.

**[04:43]** >> So 1100 lines of code. >> Did it task completed?

**[04:45]** >> Did it task completed?

**[04:45]** >> Did it task completed? >> Do we know if this works yet?

**[04:48]** >> Do we know if this works yet?

**[04:48]** >> Do we know if this works yet? >> Well, let's have a look. So it actually

**[04:49]** >> Well, let's have a look. So it actually

**[04:50]** >> Well, let's have a look. So it actually wrote some bell commands to test it. And

**[04:53]** wrote some bell commands to test it. And

**[04:53]** wrote some bell commands to test it. And when we check out the output of those,

**[04:56]** when we check out the output of those,

**[04:56]** when we check out the output of those, this actually looks pretty good.

**[04:59]** this actually looks pretty good.

**[04:59]** this actually looks pretty good. >> We ask

**[04:59]** >> We ask

**[04:59]** >> We ask >> can we verify that


### [05:00 - 06:00]

**[05:00]** >> can we verify that

**[05:00]** >> can we verify that >> to run it? Let's go verify it. So of

**[05:03]** >> to run it? Let's go verify it. So of

**[05:03]** >> to run it? Let's go verify it. So of course our agent came back and gave a

**[05:06]** course our agent came back and gave a

**[05:06]** course our agent came back and gave a summary of what it did. But let's just

**[05:09]** summary of what it did. But let's just

**[05:09]** summary of what it did. But let's just ask how to run this.

**[05:20]** Okay.

**[05:20]** Okay. So,

**[05:21]** So,

**[05:21]** So, I'm going to go open up now. So, it says

**[05:24]** I'm going to go open up now. So, it says

**[05:24]** I'm going to go open up now. So, it says this is how I can run the ADA version

**[05:26]** this is how I can run the ADA version

**[05:26]** this is how I can run the ADA version and this is how I can run the Rust

**[05:27]** and this is how I can run the Rust

**[05:27]** and this is how I can run the Rust version. Let's run the Rust version.

**[05:32]** version. Let's run the Rust version.

**[05:32]** version. Let's run the Rust version. Perfect. Let's have a look at

**[05:35]** Perfect. Let's have a look at

**[05:35]** Perfect. Let's have a look at We might be hitting an actual

**[05:38]** We might be hitting an actual

**[05:38]** We might be hitting an actual >> an actual demo bug.

**[05:39]** >> an actual demo bug.

**[05:39]** >> an actual demo bug. >> Let's have a look.

**[05:40]** >> Let's have a look.

**[05:40]** >> Let's have a look. >> Let's see what happens.

**[05:41]** >> Let's see what happens.

**[05:41]** >> Let's see what happens. >> I know. No, no. Just warnings. Just

**[05:43]** >> I know. No, no. Just warnings. Just

**[05:43]** >> I know. No, no. Just warnings. Just warnings.

**[05:45]** warnings.

**[05:45]** warnings. >> Do we have an unwrap in there that we

**[05:46]** >> Do we have an unwrap in there that we

**[05:46]** >> Do we have an unwrap in there that we need to take care of? I heard that those

**[05:47]** need to take care of? I heard that those

**[05:48]** need to take care of? I heard that those things are dangerous.

**[05:49]** things are dangerous.

**[05:49]** things are dangerous. >> So, right now there's a ripple.

**[05:53]** >> So, right now there's a ripple.

**[05:53]** >> So, right now there's a ripple. Uh, let's hit help. See what we're able

**[05:55]** Uh, let's hit help. See what we're able

**[05:55]** Uh, let's hit help. See what we're able to do. So, it looks like we have a set

**[05:57]** to do. So, it looks like we have a set

**[05:57]** to do. So, it looks like we have a set of commands. I'm going to be lazy. I'm


### [06:00 - 07:00]

**[06:00]** of commands. I'm going to be lazy. I'm

**[06:00]** of commands. I'm going to be lazy. I'm going to copy paste these queries.

**[06:03]** going to copy paste these queries.

**[06:03]** going to copy paste these queries. So, create table users. Okay. So far so

**[06:05]** So, create table users. Okay. So far so

**[06:05]** So, create table users. Okay. So far so good.

**[06:07]** good.

**[06:07]** good. Let's insert a record.

**[06:11]** Let's insert a record.

**[06:11]** Let's insert a record. Okay. Well, let's find out if it

**[06:13]** Okay. Well, let's find out if it

**[06:13]** Okay. Well, let's find out if it actually did its job. Select start from

**[06:15]** actually did its job. Select start from

**[06:15]** actually did its job. Select start from users. Okay, we've got a record here.

**[06:18]** users. Okay, we've got a record here.

**[06:18]** users. Okay, we've got a record here. >> That's nice.

**[06:19]** >> That's nice.

**[06:19]** >> That's nice. >> Now, now I want to actually

**[06:21]** >> Now, now I want to actually

**[06:22]** >> Now, now I want to actually uh you see if I use the up arrow,

**[06:24]** uh you see if I use the up arrow,

**[06:24]** uh you see if I use the up arrow, it doesn't actually allow me to cycle

**[06:26]** it doesn't actually allow me to cycle

**[06:26]** it doesn't actually allow me to cycle through commands. Let's ask it to add a

**[06:28]** through commands. Let's ask it to add a

**[06:28]** through commands. Let's ask it to add a feature.

**[06:30]** feature.

**[06:30]** feature. Uh

**[06:33]** Uh

**[06:33]** Uh allows me to use the up arrow to cycle

**[06:37]** allows me to use the up arrow to cycle

**[06:37]** allows me to use the up arrow to cycle through.

**[06:39]** through.

**[06:39]** through. I think it will understand my center.

**[06:42]** I think it will understand my center.

**[06:42]** I think it will understand my center. >> The one thing we know about ISO is he

**[06:44]** >> The one thing we know about ISO is he

**[06:44]** >> The one thing we know about ISO is he actually does know how to read and write

**[06:45]** actually does know how to read and write

**[06:45]** actually does know how to read and write but he can't type. So all those errors

**[06:48]** but he can't type. So all those errors

**[06:48]** but he can't type. So all those errors that you're seeing in there. Uh yeah.

**[06:54]** >> So it looks like the agent's identified

**[06:54]** >> So it looks like the agent's identified a package that we can use. Let's just

**[06:57]** a package that we can use. Let's just

**[06:57]** a package that we can use. Let's just quickly look here. Compare this to the

**[06:59]** quickly look here. Compare this to the

**[06:59]** quickly look here. Compare this to the Virgin one.


### [07:00 - 08:00]

**[07:02]** Virgin one.

**[07:02]** Virgin one. And it looks like it's adding a library

**[07:03]** And it looks like it's adding a library

**[07:03]** And it looks like it's adding a library called rusty line and changing the files

**[07:07]** called rusty line and changing the files

**[07:07]** called rusty line and changing the files accordingly.

**[07:09]** accordingly.

**[07:09]** accordingly. It's currently built it and it looks

**[07:12]** It's currently built it and it looks

**[07:12]** It's currently built it and it looks like the build output is successful.

**[07:15]** like the build output is successful.

**[07:15]** like the build output is successful. There's some warnings. We'll ask it to

**[07:16]** There's some warnings. We'll ask it to

**[07:16]** There's some warnings. We'll ask it to clean those up later on. And it's now

**[07:18]** clean those up later on. And it's now

**[07:18]** clean those up later on. And it's now starting to test it.

**[07:28]** Okay, apparently it works. It's going to

**[07:28]** Okay, apparently it works. It's going to It wrote itself a little bash script to

**[07:30]** It wrote itself a little bash script to

**[07:30]** It wrote itself a little bash script to test the history.

**[07:33]** test the history.

**[07:33]** test the history. It's wrote itself a little final demo

**[07:35]** It's wrote itself a little final demo

**[07:35]** It's wrote itself a little final demo script.

**[07:36]** script.

**[07:36]** script. So let's let it Okay. So, and it gave us

**[07:40]** So let's let it Okay. So, and it gave us

**[07:40]** So let's let it Okay. So, and it gave us the summary. Well, now how do I rerun

**[07:44]** the summary. Well, now how do I rerun

**[07:44]** the summary. Well, now how do I rerun this? I do kind of know that, though.

**[07:46]** this? I do kind of know that, though.

**[07:46]** this? I do kind of know that, though. So, let's just

**[07:46]** So, let's just

**[07:46]** So, let's just >> should know that. That was 30 seconds

**[07:48]** >> should know that. That was 30 seconds

**[07:48]** >> should know that. That was 30 seconds ago.

**[07:49]** ago.

**[07:49]** ago. >> Let's build it. And let's run it again.

**[07:53]** >> Let's build it. And let's run it again.

**[07:53]** >> Let's build it. And let's run it again. Okay, let's do a help.

**[07:55]** Okay, let's do a help.

**[07:56]** Okay, let's do a help. And oh yeah, that's the up arrow. It

**[07:58]** And oh yeah, that's the up arrow. It

**[07:58]** And oh yeah, that's the up arrow. It works.

**[07:59]** works.

**[07:59]** works. >> Very nice.


### [08:00 - 09:00]

**[08:00]** >> Very nice.

**[08:00]** >> Very nice. >> Now, our models aren't just capable

**[08:03]** >> Now, our models aren't just capable

**[08:03]** >> Now, our models aren't just capable coding agents. They're capable in lots

**[08:05]** coding agents. They're capable in lots

**[08:05]** coding agents. They're capable in lots of areas of knowledge work. They're also

**[08:07]** of areas of knowledge work. They're also

**[08:07]** of areas of knowledge work. They're also emotionally intelligent. They're fun.

**[08:09]** emotionally intelligent. They're fun.

**[08:09]** emotionally intelligent. They're fun. They're great to write bedtime stories

**[08:11]** They're great to write bedtime stories

**[08:11]** They're great to write bedtime stories with for the kids. So, I'm going to ask

**[08:12]** with for the kids. So, I'm going to ask

**[08:12]** with for the kids. So, I'm going to ask you to write me a poem about all these

**[08:14]** you to write me a poem about all these

**[08:14]** you to write me a poem about all these changes, but that's just more for fun.

**[08:18]** changes, but that's just more for fun.

**[08:18]** changes, but that's just more for fun. So, as Isa was saying, this is just an

**[08:20]** So, as Isa was saying, this is just an

**[08:20]** So, as Isa was saying, this is just an interface into our platform. There's

**[08:22]** interface into our platform. There's

**[08:22]** interface into our platform. There's other interfaces into it if you're

**[08:23]** other interfaces into it if you're

**[08:23]** other interfaces into it if you're inside one of those organizations that

**[08:25]** inside one of those organizations that

**[08:25]** inside one of those organizations that has adopted poolside. So this is the

**[08:27]** has adopted poolside. So this is the

**[08:27]** has adopted poolside. So this is the coding interface into it but we also

**[08:29]** coding interface into it but we also

**[08:29]** coding interface into it but we also have other ways in which you you can

**[08:31]** have other ways in which you you can

**[08:31]** have other ways in which you you can interact with it web as well as an agent

**[08:33]** interact with it web as well as an agent

**[08:33]** interact with it web as well as an agent that you can download on your machine

**[08:35]** that you can download on your machine

**[08:35]** that you can download on your machine but um yeah we don't really tout the

**[08:37]** but um yeah we don't really tout the

**[08:37]** but um yeah we don't really tout the poem writing or the songwriting though I

**[08:40]** poem writing or the songwriting though I

**[08:40]** poem writing or the songwriting though I did send this to my wife to see and I

**[08:43]** did send this to my wife to see and I

**[08:43]** did send this to my wife to see and I have been sending her love letters

**[08:44]** have been sending her love letters

**[08:44]** have been sending her love letters written by poolside so I kind of hope

**[08:46]** written by poolside so I kind of hope

**[08:46]** written by poolside so I kind of hope that she did not enter this session to

**[08:48]** that she did not enter this session to

**[08:48]** that she did not enter this session to know exactly how I've been doing that

**[08:50]** know exactly how I've been doing that

**[08:50]** know exactly how I've been doing that for the past 6 months but uh yeah so

**[08:52]** for the past 6 months but uh yeah so

**[08:52]** for the past 6 months but uh yeah so this is kind of poolside this is what

**[08:54]** this is kind of poolside this is what

**[08:54]** this is kind of poolside this is what we've been up to Um, so as I said,

**[08:56]** we've been up to Um, so as I said,

**[08:56]** we've been up to Um, so as I said, Malibu agent is as a second generation.

**[08:59]** Malibu agent is as a second generation.

**[08:59]** Malibu agent is as a second generation. We've got a ton more compute coming


### [09:00 - 10:00]

**[09:01]** We've got a ton more compute coming

**[09:01]** We've got a ton more compute coming online and that's when we're training

**[09:02]** online and that's when we're training

**[09:02]** online and that's when we're training our next generation. That is be going to

**[09:05]** our next generation. That is be going to

**[09:05]** our next generation. That is be going to be the one that comes out publicly to

**[09:06]** be the one that comes out publicly to

**[09:06]** be the one that comes out publicly to everybody very early next year. We're

**[09:08]** everybody very early next year. We're

**[09:08]** everybody very early next year. We're going to have it behind our own API.

**[09:10]** going to have it behind our own API.

**[09:10]** going to have it behind our own API. It'll be on Amazon behind the bedrock

**[09:12]** It'll be on Amazon behind the bedrock

**[09:12]** It'll be on Amazon behind the bedrock API. Anybody in the world who's building

**[09:14]** API. Anybody in the world who's building

**[09:14]** API. Anybody in the world who's building out any sort of on a one side the

**[09:16]** out any sort of on a one side the

**[09:16]** out any sort of on a one side the engineering assistants like the cursors,

**[09:18]** engineering assistants like the cursors,

**[09:18]** engineering assistants like the cursors, windsurfs, cognitions, replets of the

**[09:21]** windsurfs, cognitions, replets of the

**[09:21]** windsurfs, cognitions, replets of the world, you can use ours. or if you use

**[09:23]** world, you can use ours. or if you use

**[09:23]** world, you can use ours. or if you use building out on any other side of the

**[09:24]** building out on any other side of the

**[09:24]** building out on any other side of the fence, the Harveys, the writers, the

**[09:26]** fence, the Harveys, the writers, the

**[09:26]** fence, the Harveys, the writers, the whatever applications of the world,

**[09:28]** whatever applications of the world,

**[09:28]** whatever applications of the world, there's going to be a fifth model out

**[09:29]** there's going to be a fifth model out

**[09:29]** there's going to be a fifth model out there that's going to be at that level

**[09:30]** there that's going to be at that level

**[09:30]** there that's going to be at that level that you can you can consume. But we're

**[09:33]** that you can you can consume. But we're

**[09:33]** that you can you can consume. But we're dead set on doing this and bringing this

**[09:35]** dead set on doing this and bringing this

**[09:35]** dead set on doing this and bringing this out to everybody in the world and kind

**[09:36]** out to everybody in the world and kind

**[09:36]** out to everybody in the world and kind of advancing that state-of-the-art and

**[09:37]** of advancing that state-of-the-art and

**[09:37]** of advancing that state-of-the-art and we're just going to keep pushing that

**[09:38]** we're just going to keep pushing that

**[09:38]** we're just going to keep pushing that out. So, that's kind of who we are. Um,

**[09:41]** out. So, that's kind of who we are. Um,

**[09:41]** out. So, that's kind of who we are. Um, and uh you can find out very little more

**[09:43]** and uh you can find out very little more

**[09:43]** and uh you can find out very little more at our website since we don't put much

**[09:45]** at our website since we don't put much

**[09:45]** at our website since we don't put much out there.

**[09:47]** out there.

**[09:47]** out there. But Iso, anything else you want to say

**[09:49]** But Iso, anything else you want to say

**[09:49]** But Iso, anything else you want to say before you uh try to go make your flight

**[09:51]** before you uh try to go make your flight

**[09:51]** before you uh try to go make your flight this time, please?

**[09:58]** >> So, I would say that it's been a pretty

**[09:58]** >> So, I would say that it's been a pretty incredible journey for the last 2 and

**[09:59]** incredible journey for the last 2 and

**[09:59]** incredible journey for the last 2 and 1/2 years of starting entirely from


### [10:00 - 11:00]

**[10:01]** 1/2 years of starting entirely from

**[10:01]** 1/2 years of starting entirely from scratch and now building to a place

**[10:03]** scratch and now building to a place

**[10:03]** scratch and now building to a place where we see our models have grown up to

**[10:05]** where we see our models have grown up to

**[10:05]** where we see our models have grown up to become increasingly more intelligent.

**[10:07]** become increasingly more intelligent.

**[10:07]** become increasingly more intelligent. And the kind of missing ingredient that

**[10:09]** And the kind of missing ingredient that

**[10:09]** And the kind of missing ingredient that we had was compute. And now that it's

**[10:11]** we had was compute. And now that it's

**[10:11]** we had was compute. And now that it's unlocked for us and and with a large

**[10:13]** unlocked for us and and with a large

**[10:13]** unlocked for us and and with a large number of over 40,000 GB300s coming

**[10:15]** number of over 40,000 GB300s coming

**[10:15]** number of over 40,000 GB300s coming online, we see how we can start scaling

**[10:17]** online, we see how we can start scaling

**[10:17]** online, we see how we can start scaling up some of those models uh to get even

**[10:19]** up some of those models uh to get even

**[10:19]** up some of those models uh to get even further uh in in their level of

**[10:21]** further uh in in their level of

**[10:21]** further uh in in their level of capabilities and software development

**[10:23]** capabilities and software development

**[10:23]** capabilities and software development and other types of long horizon

**[10:24]** and other types of long horizon

**[10:24]** and other types of long horizon knowledge work. What I think is exciting

**[10:26]** knowledge work. What I think is exciting

**[10:26]** knowledge work. What I think is exciting about this conference and this audience

**[10:28]** about this conference and this audience

**[10:28]** about this conference and this audience is of all the work that's happening of

**[10:30]** is of all the work that's happening of

**[10:30]** is of all the work that's happening of evolving the form factor. Right? Right

**[10:32]** evolving the form factor. Right? Right

**[10:32]** evolving the form factor. Right? Right now what we looked at was this

**[10:33]** now what we looked at was this

**[10:33]** now what we looked at was this asynchronous way of of operating with

**[10:35]** asynchronous way of of operating with

**[10:35]** asynchronous way of of operating with agents. You know, Jason, you and I, we

**[10:36]** agents. You know, Jason, you and I, we

**[10:36]** agents. You know, Jason, you and I, we have agents running that are doing tasks

**[10:38]** have agents running that are doing tasks

**[10:38]** have agents running that are doing tasks for for hours, and I think in the near

**[10:40]** for for hours, and I think in the near

**[10:40]** for for hours, and I think in the near future, we can see a world where they're

**[10:41]** future, we can see a world where they're

**[10:41]** future, we can see a world where they're able to start doing tasks in days in the

**[10:43]** able to start doing tasks in days in the

**[10:43]** able to start doing tasks in days in the coming years. And so, I think the

**[10:45]** coming years. And so, I think the

**[10:45]** coming years. And so, I think the interface will continue to change. Uh,

**[10:47]** interface will continue to change. Uh,

**[10:47]** interface will continue to change. Uh, we're really focused on the

**[10:48]** we're really focused on the

**[10:48]** we're really focused on the fundamentals, building intelligence, and

**[10:50]** fundamentals, building intelligence, and

**[10:50]** fundamentals, building intelligence, and being able to scale up and serve it. And

**[10:52]** being able to scale up and serve it. And

**[10:52]** being able to scale up and serve it. And it's why we go full vertical. It's why

**[10:53]** it's why we go full vertical. It's why

**[10:54]** it's why we go full vertical. It's why we go from our multi gigawatt campus in

**[10:55]** we go from our multi gigawatt campus in

**[10:55]** we go from our multi gigawatt campus in West Texas where we're building out data

**[10:57]** West Texas where we're building out data

**[10:57]** West Texas where we're building out data centers building out models. And the


### [11:00 - 12:00]

**[11:00]** centers building out models. And the

**[11:00]** centers building out models. And the interface that you saw today is just our

**[11:01]** interface that you saw today is just our

**[11:01]** interface that you saw today is just our version of an expression. But I think

**[11:03]** version of an expression. But I think

**[11:03]** version of an expression. But I think this audience is going to do an

**[11:04]** this audience is going to do an

**[11:04]** this audience is going to do an incredible job of building lots better

**[11:06]** incredible job of building lots better

**[11:06]** incredible job of building lots better versions of how to express using that

**[11:08]** versions of how to express using that

**[11:08]** versions of how to express using that intelligence uh into actually, you know,

**[11:10]** intelligence uh into actually, you know,

**[11:10]** intelligence uh into actually, you know, valuable, economically valuable work.

**[11:13]** valuable, economically valuable work.

**[11:13]** valuable, economically valuable work. Couldn't have said it better. Can't wait

**[11:14]** Couldn't have said it better. Can't wait

**[11:14]** Couldn't have said it better. Can't wait to see what you guys build on this uh in

**[11:16]** to see what you guys build on this uh in

**[11:16]** to see what you guys build on this uh in the future when it's publicly available.

**[11:18]** the future when it's publicly available.

**[11:18]** the future when it's publicly available. And if anyone really does want to build

**[11:19]** And if anyone really does want to build

**[11:19]** And if anyone really does want to build a data center campus, we are hiring for

**[11:21]** a data center campus, we are hiring for

**[11:21]** a data center campus, we are hiring for that. Um it is weird to be putting

**[11:24]** that. Um it is weird to be putting

**[11:24]** that. Um it is weird to be putting shovels in ground again like we did in

**[11:25]** shovels in ground again like we did in

**[11:25]** shovels in ground again like we did in the '9s and early 2000s, but that's what

**[11:27]** the '9s and early 2000s, but that's what

**[11:27]** the '9s and early 2000s, but that's what you got to do to scale intelligence

**[11:29]** you got to do to scale intelligence

**[11:29]** you got to do to scale intelligence these days. So,

**[11:30]** these days. So,

**[11:30]** these days. So, >> I would make one other non-scheduled

**[11:32]** >> I would make one other non-scheduled

**[11:32]** >> I would make one other non-scheduled statement if you're going to be okay

**[11:34]** statement if you're going to be okay

**[11:34]** statement if you're going to be okay with this one, Jason.

**[11:37]** with this one, Jason.

**[11:37]** with this one, Jason. As as our models are are getting more

**[11:40]** As as our models are are getting more

**[11:40]** As as our models are are getting more capable, we'd love to also see who wants

**[11:43]** capable, we'd love to also see who wants

**[11:43]** capable, we'd love to also see who wants to build with them. Right now, the the

**[11:45]** to build with them. Right now, the the

**[11:45]** to build with them. Right now, the the vast majority of of you know, companies

**[11:47]** vast majority of of you know, companies

**[11:47]** vast majority of of you know, companies that are doing additional reinforcement

**[11:48]** that are doing additional reinforcement

**[11:48]** that are doing additional reinforcement learning and fine-tuning on top of

**[11:50]** learning and fine-tuning on top of

**[11:50]** learning and fine-tuning on top of models are are doing it on what I would

**[11:52]** models are are doing it on what I would

**[11:52]** models are are doing it on what I would consider right now the you know,

**[11:53]** consider right now the you know,

**[11:53]** consider right now the you know, best-in-class open source models, the

**[11:55]** best-in-class open source models, the

**[11:55]** best-in-class open source models, the the Quens and Fumies and Miniaxes of the

**[11:57]** the Quens and Fumies and Miniaxes of the

**[11:57]** the Quens and Fumies and Miniaxes of the world. And uh we'd like to start

**[11:59]** world. And uh we'd like to start

**[11:59]** world. And uh we'd like to start figuring out how we can you know partner


### [12:00 - 13:00]

**[12:01]** figuring out how we can you know partner

**[12:01]** figuring out how we can you know partner with you with our our models anywhere

**[12:03]** with you with our our models anywhere

**[12:03]** with you with our our models anywhere from any checkpoint early on to where we

**[12:05]** from any checkpoint early on to where we

**[12:05]** from any checkpoint early on to where we are today for you to be building closer

**[12:07]** are today for you to be building closer

**[12:07]** are today for you to be building closer together with us on top of things. Uh we

**[12:09]** together with us on top of things. Uh we

**[12:09]** together with us on top of things. Uh we haven't really figured out the approach

**[12:10]** haven't really figured out the approach

**[12:10]** haven't really figured out the approach to it yet. Uh but I think since we have

**[12:12]** to it yet. Uh but I think since we have

**[12:12]** to it yet. Uh but I think since we have this audience it's uh it's not a bad

**[12:13]** this audience it's uh it's not a bad

**[12:14]** this audience it's uh it's not a bad place to put it out there and so

**[12:15]** place to put it out there and so

**[12:15]** place to put it out there and so definitely reach out to us. Uh we think

**[12:17]** definitely reach out to us. Uh we think

**[12:17]** definitely reach out to us. Uh we think the world till date was built by

**[12:18]** the world till date was built by

**[12:18]** the world till date was built by intelligence. The world in the future

**[12:19]** intelligence. The world in the future

**[12:20]** intelligence. The world in the future has been built on top of intelligence

**[12:21]** has been built on top of intelligence

**[12:21]** has been built on top of intelligence and so be a great way to partner.

**[12:25]** and so be a great way to partner.

**[12:25]** and so be a great way to partner. >> Well thanks ISO. Thanks everybody here.

**[12:26]** >> Well thanks ISO. Thanks everybody here.

**[12:26]** >> Well thanks ISO. Thanks everybody here. And now we do have 5 minutes left. I

**[12:28]** And now we do have 5 minutes left. I

**[12:28]** And now we do have 5 minutes left. I don't know if we're supposed to take

**[12:29]** don't know if we're supposed to take

**[12:29]** don't know if we're supposed to take questions, but I'm happy to. So, if

**[12:31]** questions, but I'm happy to. So, if

**[12:31]** questions, but I'm happy to. So, if anyone does, but if not, I'm just going

**[12:32]** anyone does, but if not, I'm just going

**[12:32]** anyone does, but if not, I'm just going to go that way.

**[12:34]** to go that way.

**[12:34]** to go that way. >> What was that?

**[12:37]** >> What was that?

**[12:37]** >> What was that? >> Sort of. I mean, I think of him that

**[12:40]** >> Sort of. I mean, I think of him that

**[12:40]** >> Sort of. I mean, I think of him that way. Here, here's a fun story. Here's

**[12:42]** way. Here, here's a fun story. Here's

**[12:42]** way. Here, here's a fun story. Here's how I met ISO. I like to tell this story

**[12:44]** how I met ISO. I like to tell this story

**[12:44]** how I met ISO. I like to tell this story because um ISO is a fun fun dude. I met

**[12:47]** because um ISO is a fun fun dude. I met

**[12:47]** because um ISO is a fun fun dude. I met ISO because started with a failed

**[12:49]** ISO because started with a failed

**[12:49]** ISO because started with a failed acquisition at GitHub. So back when I

**[12:52]** acquisition at GitHub. So back when I

**[12:52]** acquisition at GitHub. So back when I joined GitHub in 2017 as a CTO, I wanted

**[12:54]** joined GitHub in 2017 as a CTO, I wanted

**[12:54]** joined GitHub in 2017 as a CTO, I wanted to take GitHub from a kind of

**[12:56]** to take GitHub from a kind of

**[12:56]** to take GitHub from a kind of collaborative collaborative code host

**[12:57]** collaborative collaborative code host

**[12:57]** collaborative collaborative code host with open source bent and turn it into

**[12:59]** with open source bent and turn it into

**[12:59]** with open source bent and turn it into an endto-end software development


### [13:00 - 14:00]

**[13:00]** an endto-end software development

**[13:00]** an endto-end software development platform infused by intelligence. And so

**[13:02]** platform infused by intelligence. And so

**[13:02]** platform infused by intelligence. And so you know the the products that we

**[13:03]** you know the the products that we

**[13:03]** you know the the products that we launched from 27 on or 17 on GitHub

**[13:07]** launched from 27 on or 17 on GitHub

**[13:07]** launched from 27 on or 17 on GitHub actions, packages, alerts,

**[13:08]** actions, packages, alerts,

**[13:08]** actions, packages, alerts, notifications, eventually code spaces,

**[13:11]** notifications, eventually code spaces,

**[13:11]** notifications, eventually code spaces, um and then co-pilot was the last thing

**[13:13]** um and then co-pilot was the last thing

**[13:13]** um and then co-pilot was the last thing that the office of the CTO did before I

**[13:15]** that the office of the CTO did before I

**[13:15]** that the office of the CTO did before I left with Nat Friedman, Uga De Moore,

**[13:17]** left with Nat Friedman, Uga De Moore,

**[13:17]** left with Nat Friedman, Uga De Moore, and a couple of other folks inside

**[13:18]** and a couple of other folks inside

**[13:18]** and a couple of other folks inside there. But ISO in 2017 when I joined uh

**[13:22]** there. But ISO in 2017 when I joined uh

**[13:22]** there. But ISO in 2017 when I joined uh he had working code completion before

**[13:24]** he had working code completion before

**[13:24]** he had working code completion before the transform architecture had landed

**[13:26]** the transform architecture had landed

**[13:26]** the transform architecture had landed fully. He had on LSTMs and so I quickly

**[13:28]** fully. He had on LSTMs and so I quickly

**[13:28]** fully. He had on LSTMs and so I quickly tried to acquire his company and he just

**[13:31]** tried to acquire his company and he just

**[13:31]** tried to acquire his company and he just he just said no. So he just said no to

**[13:34]** he just said no. So he just said no to

**[13:34]** he just said no. So he just said no to me. Uh but we had that was a long drawn

**[13:36]** me. Uh but we had that was a long drawn

**[13:36]** me. Uh but we had that was a long drawn out process talking about what we

**[13:38]** out process talking about what we

**[13:38]** out process talking about what we thought neural networks were going to

**[13:39]** thought neural networks were going to

**[13:39]** thought neural networks were going to mean for the world. And so during that

**[13:42]** mean for the world. And so during that

**[13:42]** mean for the world. And so during that process, which was a lengthy one, we

**[13:43]** process, which was a lengthy one, we

**[13:43]** process, which was a lengthy one, we became really good friends and we'd

**[13:45]** became really good friends and we'd

**[13:45]** became really good friends and we'd stayed in close contact over the years.

**[13:47]** stayed in close contact over the years.

**[13:47]** stayed in close contact over the years. And then 22 rolled around, obviously

**[13:48]** And then 22 rolled around, obviously

**[13:48]** And then 22 rolled around, obviously Chat GPT comes out, Anthropics out, and

**[13:51]** Chat GPT comes out, Anthropics out, and

**[13:51]** Chat GPT comes out, Anthropics out, and we kind of saw the endgame at play and

**[13:54]** we kind of saw the endgame at play and

**[13:54]** we kind of saw the endgame at play and we said, "Do we jump back in or not?"

**[13:55]** we said, "Do we jump back in or not?"

**[13:55]** we said, "Do we jump back in or not?" And of course, yes, we jump back in. But

**[13:58]** And of course, yes, we jump back in. But

**[13:58]** And of course, yes, we jump back in. But I like to tell that story about how he

**[13:59]** I like to tell that story about how he


### [14:00 - 15:00]

**[14:00]** I like to tell that story about how he just kept saying no to me and I just

**[14:01]** just kept saying no to me and I just

**[14:01]** just kept saying no to me and I just kept asking him questions and eventually

**[14:03]** kept asking him questions and eventually

**[14:03]** kept asking him questions and eventually he said, "Yes, we should found a

**[14:04]** he said, "Yes, we should found a

**[14:04]** he said, "Yes, we should found a company." Cuz by the way, when I asked

**[14:05]** company." Cuz by the way, when I asked

**[14:05]** company." Cuz by the way, when I asked him if we should do this, he said, "Oh,

**[14:07]** him if we should do this, he said, "Oh,

**[14:07]** him if we should do this, he said, "Oh, god damn no." That were his exact words.

**[14:09]** god damn no." That were his exact words.

**[14:10]** god damn no." That were his exact words. He's like, "No, we should just learn how

**[14:11]** He's like, "No, we should just learn how

**[14:11]** He's like, "No, we should just learn how to paint and sail." But here we are.

**[14:15]** to paint and sail." But here we are.

**[14:15]** to paint and sail." But here we are. So,

**[14:15]** So,

**[14:15]** So, >> yeah,

**[14:17]** >> yeah,

**[14:17]** >> yeah, >> it's it's been a great journey together.

**[14:18]** >> it's it's been a great journey together.

**[14:18]** >> it's it's been a great journey together. Jason, I I think the reason we ended up

**[14:21]** Jason, I I think the reason we ended up

**[14:21]** Jason, I I think the reason we ended up doing this is because of our our

**[14:24]** doing this is because of our our

**[14:24]** doing this is because of our our opinionated view on what it was going to

**[14:25]** opinionated view on what it was going to

**[14:25]** opinionated view on what it was going to take to build more capable intelligence.

**[14:27]** take to build more capable intelligence.

**[14:27]** take to build more capable intelligence. And in the first 18 months of this

**[14:29]** And in the first 18 months of this

**[14:29]** And in the first 18 months of this company, you know, obsessing and

**[14:30]** company, you know, obsessing and

**[14:30]** company, you know, obsessing and focusing on reinforcement learning

**[14:31]** focusing on reinforcement learning

**[14:32]** focusing on reinforcement learning combined with LMS felt like one of the

**[14:34]** combined with LMS felt like one of the

**[14:34]** combined with LMS felt like one of the most contrarian opinions in the world,

**[14:35]** most contrarian opinions in the world,

**[14:35]** most contrarian opinions in the world, but I think today it's absolutely not.

**[14:37]** but I think today it's absolutely not.

**[14:37]** but I think today it's absolutely not. And it's super exciting to see the the

**[14:39]** And it's super exciting to see the the

**[14:39]** And it's super exciting to see the the progress that's continuing to make like

**[14:41]** progress that's continuing to make like

**[14:41]** progress that's continuing to make like we're in the coming years we're going to

**[14:43]** we're in the coming years we're going to

**[14:43]** we're in the coming years we're going to see the world that started in

**[14:44]** see the world that started in

**[14:44]** see the world that started in completions and went to chat and is now

**[14:46]** completions and went to chat and is now

**[14:46]** completions and went to chat and is now at a gentic increasingly approach more

**[14:48]** at a gentic increasingly approach more

**[14:48]** at a gentic increasingly approach more autonomous and we're all of it is

**[14:51]** autonomous and we're all of it is

**[14:52]** autonomous and we're all of it is stemming effectively from the

**[14:53]** stemming effectively from the

**[14:53]** stemming effectively from the combination of bringing highly capable

**[14:54]** combination of bringing highly capable

**[14:54]** combination of bringing highly capable models that are constantly evolving

**[14:56]** models that are constantly evolving

**[14:56]** models that are constantly evolving together with real world problems and

**[14:59]** together with real world problems and

**[14:59]** together with real world problems and and I think what we're starting to see


### [15:00 - 16:00]

**[15:00]** and I think what we're starting to see

**[15:00]** and I think what we're starting to see now is we're entering these kind of

**[15:01]** now is we're entering these kind of

**[15:01]** now is we're entering these kind of awkward teenage years ahead of AGI where

**[15:04]** awkward teenage years ahead of AGI where

**[15:04]** awkward teenage years ahead of AGI where everybody in this room is building out

**[15:06]** everybody in this room is building out

**[15:06]** everybody in this room is building out incredible companies and applications is

**[15:08]** incredible companies and applications is

**[15:08]** incredible companies and applications is bridging this gap of what it really

**[15:10]** bridging this gap of what it really

**[15:10]** bridging this gap of what it really takes to make intelligence that in its

**[15:12]** takes to make intelligence that in its

**[15:12]** takes to make intelligence that in its raw form actually be valuable and we uh

**[15:15]** raw form actually be valuable and we uh

**[15:15]** raw form actually be valuable and we uh we want to be a small humble part of

**[15:17]** we want to be a small humble part of

**[15:17]** we want to be a small humble part of that. We've got a lot of work still

**[15:18]** that. We've got a lot of work still

**[15:18]** that. We've got a lot of work still ahead of us. Uh the team is growing. Uh

**[15:21]** ahead of us. Uh the team is growing. Uh

**[15:21]** ahead of us. Uh the team is growing. Uh but hopefully what you've seen today uh

**[15:23]** but hopefully what you've seen today uh

**[15:23]** but hopefully what you've seen today uh is what our our customers and

**[15:25]** is what our our customers and

**[15:25]** is what our our customers and enterprises have been having access to

**[15:26]** enterprises have been having access to

**[15:26]** enterprises have been having access to and seeing for a while is that we're you

**[15:28]** and seeing for a while is that we're you

**[15:28]** and seeing for a while is that we're you know hard at work at uh at really

**[15:30]** know hard at work at uh at really

**[15:30]** know hard at work at uh at really pushing those capabilities. We also want

**[15:31]** pushing those capabilities. We also want

**[15:31]** pushing those capabilities. We also want to make sure we make them available to

**[15:33]** to make sure we make them available to

**[15:33]** to make sure we make them available to build together with others.

**[15:35]** build together with others.

**[15:35]** build together with others. >> Well, that's it. Thanks everybody.


