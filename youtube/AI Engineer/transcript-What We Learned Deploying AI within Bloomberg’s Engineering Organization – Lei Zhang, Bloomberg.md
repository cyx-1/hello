# What We Learned Deploying AI within Bloomberg’s Engineering Organization – Lei Zhang, Bloomberg

**Video URL:** https://www.youtube.com/watch?v=Q81AzlA-VE8

---

## Full Transcript

### [00:00 - 01:00]

**[00:22]** I don't have a joke about the dot. I

**[00:22]** I don't have a joke about the dot. I don't have a joke about the uh hot dog

**[00:24]** don't have a joke about the uh hot dog

**[00:24]** don't have a joke about the uh hot dog either. So, I would just jump to the

**[00:25]** either. So, I would just jump to the

**[00:25]** either. So, I would just jump to the topic right away. Um, so my name is Lei.

**[00:29]** topic right away. Um, so my name is Lei.

**[00:29]** topic right away. Um, so my name is Lei. Um I lead the uh department of

**[00:31]** Um I lead the uh department of

**[00:31]** Um I lead the uh department of technology infrastructure in Bloommer.

**[00:32]** technology infrastructure in Bloommer.

**[00:32]** technology infrastructure in Bloommer. So we're basically a group of

**[00:34]** So we're basically a group of

**[00:34]** So we're basically a group of technologists focus on global

**[00:36]** technologists focus on global

**[00:36]** technologists focus on global infrastructure. Thank data centers

**[00:38]** infrastructure. Thank data centers

**[00:38]** infrastructure. Thank data centers connectivities

**[00:40]** connectivities

**[00:40]** connectivities um developer productivities uh thank SCS

**[00:44]** um developer productivities uh thank SCS

**[00:44]** um developer productivities uh thank SCS tooling and also uh reliability

**[00:47]** tooling and also uh reliability

**[00:47]** tooling and also uh reliability solutions think telemetry and instant

**[00:49]** solutions think telemetry and instant

**[00:49]** solutions think telemetry and instant responses right so um depends on

**[00:53]** responses right so um depends on

**[00:53]** responses right so um depends on audience sometimes uh you know you're

**[00:56]** audience sometimes uh you know you're

**[00:56]** audience sometimes uh you know you're familiar with what Bloomer is sometimes

**[00:57]** familiar with what Bloomer is sometimes

**[00:58]** familiar with what Bloomer is sometimes you don't so I thought it might be a

**[00:59]** you don't so I thought it might be a

**[00:59]** you don't so I thought it might be a good idea to talk a little bit about


### [01:00 - 02:00]

**[01:01]** good idea to talk a little bit about

**[01:01]** good idea to talk a little bit about about our company

**[01:03]** about our company

**[01:03]** about our company um so there's no better way to talk

**[01:05]** um so there's no better way to talk

**[01:05]** um so there's no better way to talk about our company by sharing some

**[01:06]** about our company by sharing some

**[01:06]** about our company by sharing some numbers

**[01:07]** numbers

**[01:07]** numbers I want to highlight a few numbers. We

**[01:09]** I want to highlight a few numbers. We

**[01:09]** I want to highlight a few numbers. We have more than 9,000 engineers and most

**[01:12]** have more than 9,000 engineers and most

**[01:12]** have more than 9,000 engineers and most of them are software engineers. Uh we

**[01:14]** of them are software engineers. Uh we

**[01:14]** of them are software engineers. Uh we handle a lot of market techs uh which in

**[01:17]** handle a lot of market techs uh which in

**[01:17]** handle a lot of market techs uh which in the billions and 600 billions I believe.

**[01:19]** the billions and 600 billions I believe.

**[01:19]** the billions and 600 billions I believe. And um we also have tons of folks uh

**[01:23]** And um we also have tons of folks uh

**[01:23]** And um we also have tons of folks uh focus on AI research and engineering. So

**[01:27]** focus on AI research and engineering. So

**[01:27]** focus on AI research and engineering. So we have a more than you know really

**[01:29]** we have a more than you know really

**[01:29]** we have a more than you know really today's 500 plus employees focus on AI

**[01:32]** today's 500 plus employees focus on AI

**[01:32]** today's 500 plus employees focus on AI products uh for um sort of our

**[01:35]** products uh for um sort of our

**[01:35]** products uh for um sort of our customers.

**[01:37]** customers.

**[01:37]** customers. So takeaway here is we are I guess you

**[01:41]** So takeaway here is we are I guess you

**[01:41]** So takeaway here is we are I guess you know building a lot of software and use

**[01:44]** know building a lot of software and use

**[01:44]** know building a lot of software and use a lot of data to empower our flagship

**[01:47]** a lot of data to empower our flagship

**[01:47]** a lot of data to empower our flagship product which is called the Bloomer

**[01:48]** product which is called the Bloomer

**[01:48]** product which is called the Bloomer terminal and to really support our users

**[01:51]** terminal and to really support our users

**[01:51]** terminal and to really support our users to make the most important f decisions

**[01:54]** to make the most important f decisions

**[01:54]** to make the most important f decisions for them to do their job um the best. Um

**[01:59]** for them to do their job um the best. Um

**[01:59]** for them to do their job um the best. Um in the technical lens um a lot of time


### [02:00 - 03:00]

**[02:03]** in the technical lens um a lot of time

**[02:03]** in the technical lens um a lot of time kind of to explain that we actually have

**[02:05]** kind of to explain that we actually have

**[02:05]** kind of to explain that we actually have one of the largest private network uh in

**[02:07]** one of the largest private network uh in

**[02:07]** one of the largest private network uh in the whole world. We also have one of the

**[02:09]** the whole world. We also have one of the

**[02:09]** the whole world. We also have one of the largest JavaScript codebase um in the

**[02:12]** largest JavaScript codebase um in the

**[02:12]** largest JavaScript codebase um in the world. Um we because the domain where I

**[02:17]** world. Um we because the domain where I

**[02:17]** world. Um we because the domain where I am uh so promot terminal is really you

**[02:20]** am uh so promot terminal is really you

**[02:20]** am uh so promot terminal is really you can think of a um software that supports

**[02:24]** can think of a um software that supports

**[02:24]** can think of a um software that supports thousands of different applications. uh

**[02:26]** thousands of different applications. uh

**[02:26]** thousands of different applications. uh we call them functions right um email is

**[02:30]** we call them functions right um email is

**[02:30]** we call them functions right um email is a function uh news is a group of

**[02:33]** a function uh news is a group of

**[02:33]** a function uh news is a group of functions

**[02:35]** functions

**[02:35]** functions um let's say fixed income price to yield

**[02:37]** um let's say fixed income price to yield

**[02:37]** um let's say fixed income price to yield calculation to spread calculation is

**[02:39]** calculation to spread calculation is

**[02:39]** calculation to spread calculation is another function um trading workflows is

**[02:43]** another function um trading workflows is

**[02:43]** another function um trading workflows is another group of functions so there's

**[02:44]** another group of functions so there's

**[02:44]** another group of functions so there's many many many different type of

**[02:46]** many many many different type of

**[02:46]** many many many different type of functions as you can imagine we kind of

**[02:47]** functions as you can imagine we kind of

**[02:47]** functions as you can imagine we kind of have to utilize different technologies

**[02:50]** have to utilize different technologies

**[02:50]** have to utilize different technologies to really support those uh

**[02:52]** to really support those uh

**[02:52]** to really support those uh functionalities

**[02:54]** functionalities

**[02:54]** functionalities uh we also

**[02:56]** uh we also

**[02:56]** uh we also increasingly more than used but also

**[02:59]** increasingly more than used but also

**[02:59]** increasingly more than used but also contribute to open source communities.


### [03:00 - 04:00]

**[03:01]** contribute to open source communities.

**[03:01]** contribute to open source communities. um for this audience I guess I want to

**[03:03]** um for this audience I guess I want to

**[03:03]** um for this audience I guess I want to call out you know we kind of helped

**[03:05]** call out you know we kind of helped

**[03:05]** call out you know we kind of helped creation of the case envoy AI gateways

**[03:09]** creation of the case envoy AI gateways

**[03:09]** creation of the case envoy AI gateways and among many many other things that

**[03:10]** and among many many other things that

**[03:10]** and among many many other things that that we deploy inhouse and support the

**[03:12]** that we deploy inhouse and support the

**[03:12]** that we deploy inhouse and support the communities again in summary there's a

**[03:15]** communities again in summary there's a

**[03:16]** communities again in summary there's a lot of software there's a lot of data uh

**[03:18]** lot of software there's a lot of data uh

**[03:18]** lot of software there's a lot of data uh we kind of have to um figure out how to

**[03:21]** we kind of have to um figure out how to

**[03:22]** we kind of have to um figure out how to make the best of AI tooling to support

**[03:23]** make the best of AI tooling to support

**[03:23]** make the best of AI tooling to support us to do our engineering work all right

**[03:27]** us to do our engineering work all right

**[03:27]** us to do our engineering work all right so get to what is AI for coding Um we

**[03:32]** so get to what is AI for coding Um we

**[03:32]** so get to what is AI for coding Um we started about two years ago maybe a

**[03:35]** started about two years ago maybe a

**[03:35]** started about two years ago maybe a little bit more than that. Um and as I

**[03:38]** little bit more than that. Um and as I

**[03:38]** little bit more than that. Um and as I guess the rest of the world we look at

**[03:40]** guess the rest of the world we look at

**[03:40]** guess the rest of the world we look at the toolings provided and you know I

**[03:43]** the toolings provided and you know I

**[03:43]** the toolings provided and you know I apologize if if your logos are not here.

**[03:46]** apologize if if your logos are not here.

**[03:46]** apologize if if your logos are not here. Um but as you can imagine it's kind of

**[03:48]** Um but as you can imagine it's kind of

**[03:48]** Um but as you can imagine it's kind of like overwhelming right there's so many

**[03:49]** like overwhelming right there's so many

**[03:50]** like overwhelming right there's so many things and every day there's news about

**[03:51]** things and every day there's news about

**[03:51]** things and every day there's news about this is great this is great. Um so at

**[03:55]** this is great this is great. Um so at

**[03:55]** this is great this is great. Um so at the time we actually didn't know what

**[03:58]** the time we actually didn't know what

**[03:58]** the time we actually didn't know what all the AI solutions can help us to


### [04:00 - 05:00]

**[04:03]** all the AI solutions can help us to

**[04:03]** all the AI solutions can help us to uh boost our productivities as well as

**[04:05]** uh boost our productivities as well as

**[04:05]** uh boost our productivities as well as stability. But one thing we knew at the

**[04:08]** stability. But one thing we knew at the

**[04:08]** stability. But one thing we knew at the time is um unless we deploy and try we

**[04:15]** time is um unless we deploy and try we

**[04:15]** time is um unless we deploy and try we wouldn't know what's the best way to

**[04:16]** wouldn't know what's the best way to

**[04:16]** wouldn't know what's the best way to benefit from all the awesome work and

**[04:18]** benefit from all the awesome work and

**[04:18]** benefit from all the awesome work and and you know a lot of folks are

**[04:20]** and you know a lot of folks are

**[04:20]** and you know a lot of folks are contributing to. So at the time uh we

**[04:23]** contributing to. So at the time uh we

**[04:23]** contributing to. So at the time uh we quickly form a team people start

**[04:26]** quickly form a team people start

**[04:26]** quickly form a team people start kind of like release um kind a set of

**[04:30]** kind of like release um kind a set of

**[04:30]** kind of like release um kind a set of capabilities so that people start

**[04:31]** capabilities so that people start

**[04:32]** capabilities so that people start iterating on um utilizing the toolings

**[04:35]** iterating on um utilizing the toolings

**[04:35]** iterating on um utilizing the toolings and then of course you know we are data

**[04:37]** and then of course you know we are data

**[04:37]** and then of course you know we are data company so kind of want to get a sense

**[04:39]** company so kind of want to get a sense

**[04:39]** company so kind of want to get a sense of how we measure the impact and um what

**[04:43]** of how we measure the impact and um what

**[04:43]** of how we measure the impact and um what we can do from the capability we provide

**[04:45]** we can do from the capability we provide

**[04:45]** we can do from the capability we provide right so we look at the typical

**[04:49]** right so we look at the typical

**[04:49]** right so we look at the typical developer productivity measurements

**[04:51]** developer productivity measurements

**[04:51]** developer productivity measurements We ran a few survey. Uh it was very

**[04:54]** We ran a few survey. Uh it was very

**[04:54]** We ran a few survey. Uh it was very obvious that people felt like there's

**[04:56]** obvious that people felt like there's

**[04:56]** obvious that people felt like there's much quicker uh proof of concept, people

**[04:59]** much quicker uh proof of concept, people


### [05:00 - 06:00]

**[05:00]** much quicker uh proof of concept, people rolled out tests. Uh there's a lot of

**[05:03]** rolled out tests. Uh there's a lot of

**[05:03]** rolled out tests. Uh there's a lot of one time use scripts being generated and

**[05:05]** one time use scripts being generated and

**[05:05]** one time use scripts being generated and then the measurements dropped actually

**[05:06]** then the measurements dropped actually

**[05:06]** then the measurements dropped actually pretty quickly when you

**[05:09]** pretty quickly when you

**[05:09]** pretty quickly when you go beyond all the green field type of

**[05:12]** go beyond all the green field type of

**[05:12]** go beyond all the green field type of thing, right? And then then we start

**[05:15]** thing, right? And then then we start

**[05:15]** thing, right? And then then we start thinking like okay so what are the

**[05:17]** thinking like okay so what are the

**[05:17]** thinking like okay so what are the things that we should really be doing

**[05:19]** things that we should really be doing

**[05:19]** things that we should really be doing using all those wonderful things so that

**[05:21]** using all those wonderful things so that

**[05:21]** using all those wonderful things so that we can really make a dent um in the in

**[05:25]** we can really make a dent um in the in

**[05:25]** we can really make a dent um in the in the space and then at this time we also

**[05:29]** the space and then at this time we also

**[05:29]** the space and then at this time we also kind of like also [clears throat] be

**[05:30]** kind of like also [clears throat] be

**[05:30]** kind of like also [clears throat] be thoughtful of um unleash a very powerful

**[05:36]** thoughtful of um unleash a very powerful

**[05:36]** thoughtful of um unleash a very powerful tool right uh the the benefits is it's

**[05:39]** tool right uh the the benefits is it's

**[05:39]** tool right uh the the benefits is it's very fast the challenge is also it's

**[05:42]** very fast the challenge is also it's

**[05:42]** very fast the challenge is also it's very

**[05:43]** very

**[05:43]** very Right. Um for any of you who actually

**[05:45]** Right. Um for any of you who actually

**[05:45]** Right. Um for any of you who actually dealt with hundreds of millions of lines

**[05:49]** dealt with hundreds of millions of lines

**[05:49]** dealt with hundreds of millions of lines of code, you probably understand the

**[05:52]** of code, you probably understand the

**[05:52]** of code, you probably understand the system complexity is a at least [snorts]

**[05:57]** system complexity is a at least [snorts]

**[05:57]** system complexity is a at least [snorts] um exponential or at least polomial I


### [06:00 - 07:00]

**[06:00]** um exponential or at least polomial I

**[06:00]** um exponential or at least polomial I guess function of your live code on

**[06:03]** guess function of your live code on

**[06:03]** guess function of your live code on software assets, right? So at some point

**[06:05]** software assets, right? So at some point

**[06:05]** software assets, right? So at some point you kind of want to be very careful uh

**[06:07]** you kind of want to be very careful uh

**[06:07]** you kind of want to be very careful uh what you do with your software assets.

**[06:10]** what you do with your software assets.

**[06:10]** what you do with your software assets. And what we thought so maybe we should

**[06:11]** And what we thought so maybe we should

**[06:11]** And what we thought so maybe we should look at some of the basics. One idea we

**[06:14]** look at some of the basics. One idea we

**[06:14]** look at some of the basics. One idea we had is um all right so AI for coding

**[06:18]** had is um all right so AI for coding

**[06:18]** had is um all right so AI for coding there's narrow definition of what coding

**[06:20]** there's narrow definition of what coding

**[06:20]** there's narrow definition of what coding is but there's also a broader definition

**[06:22]** is but there's also a broader definition

**[06:22]** is but there's also a broader definition of what software engineering right and

**[06:24]** of what software engineering right and

**[06:24]** of what software engineering right and then maybe we can also look into some of

**[06:27]** then maybe we can also look into some of

**[06:27]** then maybe we can also look into some of the work our developers don't really

**[06:30]** the work our developers don't really

**[06:30]** the work our developers don't really prefer to do for instance

**[06:33]** prefer to do for instance

**[06:34]** prefer to do for instance um some men work some of the migration

**[06:37]** um some men work some of the migration

**[06:37]** um some men work some of the migration work some of the I don't know men work

**[06:39]** work some of the I don't know men work

**[06:39]** work some of the I don't know men work and stuff like that so I want to give

**[06:41]** and stuff like that so I want to give

**[06:41]** and stuff like that so I want to give some examples of the things that we been

**[06:43]** some examples of the things that we been

**[06:43]** some examples of the things that we been trying and we think there's pretty good

**[06:45]** trying and we think there's pretty good

**[06:45]** trying and we think there's pretty good return investment.

**[06:48]** return investment.

**[06:48]** return investment. So the question we ask ourselves how do

**[06:49]** So the question we ask ourselves how do

**[06:50]** So the question we ask ourselves how do we evolve our codebase right the first

**[06:52]** we evolve our codebase right the first

**[06:52]** we evolve our codebase right the first one is all right wouldn't it be cool uh

**[06:56]** one is all right wouldn't it be cool uh

**[06:56]** one is all right wouldn't it be cool uh the day you get a ticket saying hey you

**[06:58]** the day you get a ticket saying hey you

**[06:58]** the day you get a ticket saying hey you know this piece of software needs

**[06:59]** know this piece of software needs

**[06:59]** know this piece of software needs patched at the same time you have a pull


### [07:00 - 08:00]

**[07:02]** patched at the same time you have a pull

**[07:02]** patched at the same time you have a pull request with the fix with a patch and

**[07:06]** request with the fix with a patch and

**[07:06]** request with the fix with a patch and also with thinking why the patch

**[07:08]** also with thinking why the patch

**[07:08]** also with thinking why the patch happened that way right so it's kind of

**[07:10]** happened that way right so it's kind of

**[07:10]** happened that way right so it's kind of like we're trying to uh broadly deploy

**[07:13]** like we're trying to uh broadly deploy

**[07:13]** like we're trying to uh broadly deploy something called uplift agents

**[07:16]** something called uplift agents

**[07:16]** something called uplift agents um broadly scan through our codebase and

**[07:19]** um broadly scan through our codebase and

**[07:19]** um broadly scan through our codebase and figure out what the patch would be

**[07:19]** figure out what the patch would be

**[07:20]** figure out what the patch would be applicable and be able to apply those

**[07:21]** applicable and be able to apply those

**[07:21]** applicable and be able to apply those patch step back a little bit. We did

**[07:24]** patch step back a little bit. We did

**[07:24]** patch step back a little bit. We did have a reg based refraction tool um it

**[07:27]** have a reg based refraction tool um it

**[07:27]** have a reg based refraction tool um it works to some extent but it's limited

**[07:29]** works to some extent but it's limited

**[07:30]** works to some extent but it's limited right now with um LMS and other tooling.

**[07:33]** right now with um LMS and other tooling.

**[07:33]** right now with um LMS and other tooling. So we are able to uh see very much

**[07:35]** So we are able to uh see very much

**[07:35]** So we are able to uh see very much better results from the um uplift

**[07:37]** better results from the um uplift

**[07:37]** better results from the um uplift agents. So there are few challenges in

**[07:40]** agents. So there are few challenges in

**[07:40]** agents. So there are few challenges in case you also plan to deploy such

**[07:42]** case you also plan to deploy such

**[07:42]** case you also plan to deploy such capabilities. The first one is

**[07:46]** capabilities. The first one is

**[07:46]** capabilities. The first one is I guess any AI or ML it would be really

**[07:48]** I guess any AI or ML it would be really

**[07:48]** I guess any AI or ML it would be really nice if there's some detistic

**[07:50]** nice if there's some detistic

**[07:50]** nice if there's some detistic verification capability. uh oftentimes

**[07:53]** verification capability. uh oftentimes

**[07:53]** verification capability. uh oftentimes it's not so easy especially if you have

**[07:54]** it's not so easy especially if you have

**[07:54]** it's not so easy especially if you have test cases if you don't have good

**[07:55]** test cases if you don't have good

**[07:55]** test cases if you don't have good llinter if you don't have good

**[07:57]** llinter if you don't have good

**[07:57]** llinter if you don't have good verification the the patch can sometimes

**[07:59]** verification the the patch can sometimes


### [08:00 - 09:00]

**[08:00]** verification the the patch can sometimes be uh uh difficult to to to be applied

**[08:05]** be uh uh difficult to to to be applied

**[08:05]** be uh uh difficult to to to be applied and uh one thing we also realized when

**[08:07]** and uh one thing we also realized when

**[08:07]** and uh one thing we also realized when we deploy AI tooling is the average open

**[08:11]** we deploy AI tooling is the average open

**[08:11]** we deploy AI tooling is the average open pull requests increased and time to

**[08:13]** pull requests increased and time to

**[08:13]** pull requests increased and time to merge also increased uh because you spin

**[08:17]** merge also increased uh because you spin

**[08:17]** merge also increased uh because you spin a lot of new code and then still we have

**[08:19]** a lot of new code and then still we have

**[08:19]** a lot of new code and then still we have to review the code and merge the code

**[08:21]** to review the code and merge the code

**[08:21]** to review the code and merge the code right so time to merge merge become a

**[08:22]** right so time to merge merge become a

**[08:22]** right so time to merge merge become a challenge sometimes and the last one is

**[08:25]** challenge sometimes and the last one is

**[08:25]** challenge sometimes and the last one is um I think it applies to any gen is the

**[08:29]** um I think it applies to any gen is the

**[08:29]** um I think it applies to any gen is the shift becomes what do we want to achieve

**[08:31]** shift becomes what do we want to achieve

**[08:31]** shift becomes what do we want to achieve rather than how we want to achieve right

**[08:33]** rather than how we want to achieve right

**[08:33]** rather than how we want to achieve right so

**[08:34]** so

**[08:34]** so the second example that I I want to

**[08:37]** the second example that I I want to

**[08:37]** the second example that I I want to share is uh the other area that people

**[08:41]** share is uh the other area that people

**[08:41]** share is uh the other area that people kind of like sometimes

**[08:43]** kind of like sometimes

**[08:43]** kind of like sometimes really impact our productivity in a

**[08:44]** really impact our productivity in a

**[08:44]** really impact our productivity in a negative way or impact our stability in

**[08:46]** negative way or impact our stability in

**[08:46]** negative way or impact our stability in negative way is how we handle instance

**[08:49]** negative way is how we handle instance

**[08:49]** negative way is how we handle instance so we're trying to develop and then

**[08:51]** so we're trying to develop and then

**[08:51]** so we're trying to develop and then deploy

**[08:52]** deploy

**[08:52]** deploy um yes response agents. Um now

**[08:58]** um yes response agents. Um now

**[08:58]** um yes response agents. Um now the importance of this is if you really


### [09:00 - 10:00]

**[09:01]** the importance of this is if you really

**[09:01]** the importance of this is if you really think about GI tools it's really really

**[09:03]** think about GI tools it's really really

**[09:03]** think about GI tools it's really really fast and it's also unbiased right in

**[09:07]** fast and it's also unbiased right in

**[09:07]** fast and it's also unbiased right in IMA's instance it can go through your

**[09:10]** IMA's instance it can go through your

**[09:10]** IMA's instance it can go through your codebase really quickly it can go

**[09:11]** codebase really quickly it can go

**[09:11]** codebase really quickly it can go through your telemetry system very

**[09:13]** through your telemetry system very

**[09:13]** through your telemetry system very quickly it can go through your feature

**[09:15]** quickly it can go through your feature

**[09:15]** quickly it can go through your feature flags very quickly it can go through

**[09:17]** flags very quickly it can go through

**[09:17]** flags very quickly it can go through your um I don't call trace very quickly

**[09:19]** your um I don't call trace very quickly

**[09:19]** your um I don't call trace very quickly and in unbiased lens when we do

**[09:22]** and in unbiased lens when we do

**[09:22]** and in unbiased lens when we do troubleshooting sometimes we have this

**[09:24]** troubleshooting sometimes we have this

**[09:24]** troubleshooting sometimes we have this biased views it must be this. It turns

**[09:26]** biased views it must be this. It turns

**[09:26]** biased views it must be this. It turns out to be not the case. So there's many

**[09:28]** out to be not the case. So there's many

**[09:28]** out to be not the case. So there's many many interesting benefits um by uh

**[09:32]** many interesting benefits um by uh

**[09:32]** many interesting benefits um by uh deploying agents from this perspective.

**[09:37]** deploying agents from this perspective.

**[09:37]** deploying agents from this perspective. And then the second question is become

**[09:39]** And then the second question is become

**[09:39]** And then the second question is become interesting is imagine you have

**[09:42]** interesting is imagine you have

**[09:42]** interesting is imagine you have organization of 10,000 pe um let's say

**[09:44]** organization of 10,000 pe um let's say

**[09:44]** organization of 10,000 pe um let's say 9,000 people as I described a lot of

**[09:47]** 9,000 people as I described a lot of

**[09:47]** 9,000 people as I described a lot of people trying to fix those problems

**[09:49]** people trying to fix those problems

**[09:49]** people trying to fix those problems right and you have 10 teams who wants to

**[09:51]** right and you have 10 teams who wants to

**[09:51]** right and you have 10 teams who wants to build a pull request review bots. you

**[09:54]** build a pull request review bots. you

**[09:54]** build a pull request review bots. you have too many teams who wants to build a

**[09:56]** have too many teams who wants to build a

**[09:56]** have too many teams who wants to build a instant response agents right they

**[09:59]** instant response agents right they

**[09:59]** instant response agents right they become very quickly chaotic and


### [10:00 - 11:00]

**[10:02]** become very quickly chaotic and

**[10:02]** become very quickly chaotic and sometimes can have duplications

**[10:05]** sometimes can have duplications

**[10:05]** sometimes can have duplications so before I talk about the p pass I

**[10:08]** so before I talk about the p pass I

**[10:08]** so before I talk about the p pass I going to give example of the uh instance

**[10:11]** going to give example of the uh instance

**[10:11]** going to give example of the uh instance response agent so basically this is what

**[10:13]** response agent so basically this is what

**[10:13]** response agent so basically this is what you know a in response agent will look

**[10:17]** you know a in response agent will look

**[10:17]** you know a in response agent will look like um the key part is we're going to

**[10:19]** like um the key part is we're going to

**[10:19]** like um the key part is we're going to need to build a lot of MCP servers to

**[10:21]** need to build a lot of MCP servers to

**[10:21]** need to build a lot of MCP servers to connect to the um the metrics and logs

**[10:24]** connect to the um the metrics and logs

**[10:24]** connect to the um the metrics and logs dashboards you have connect to the

**[10:26]** dashboards you have connect to the

**[10:26]** dashboards you have connect to the topology you have whether it's network

**[10:28]** topology you have whether it's network

**[10:28]** topology you have whether it's network topology or it's the um your service

**[10:31]** topology or it's the um your service

**[10:31]** topology or it's the um your service dependency topology uh your alarms your

**[10:33]** dependency topology uh your alarms your

**[10:34]** dependency topology uh your alarms your triggers right your SLOs's

**[10:37]** triggers right your SLOs's

**[10:37]** triggers right your SLOs's and then we kind of don't want people

**[10:39]** and then we kind of don't want people

**[10:39]** and then we kind of don't want people just start building MCP servers uh

**[10:42]** just start building MCP servers uh

**[10:42]** just start building MCP servers uh without a pay pass so we created a pay

**[10:45]** without a pay pass so we created a pay

**[10:45]** without a pay pass so we created a pay pass in partnership with our AI

**[10:47]** pass in partnership with our AI

**[10:47]** pass in partnership with our AI organization and I will talk a little

**[10:49]** organization and I will talk a little

**[10:50]** organization and I will talk a little bit what that means

**[10:52]** bit what that means

**[10:52]** bit what that means before at um I do want to explain a

**[10:55]** before at um I do want to explain a

**[10:55]** before at um I do want to explain a little bit some of the platform

**[10:56]** little bit some of the platform

**[10:56]** little bit some of the platform principles.

**[10:58]** principles.

**[10:58]** principles. Some company allow teams to be have a


### [11:00 - 12:00]

**[11:02]** Some company allow teams to be have a

**[11:02]** Some company allow teams to be have a lot of freedom as at the same time

**[11:05]** lot of freedom as at the same time

**[11:05]** lot of freedom as at the same time responsibility in the sense a business

**[11:07]** responsibility in the sense a business

**[11:07]** responsibility in the sense a business unit can build whatever infrastructure

**[11:08]** unit can build whatever infrastructure

**[11:08]** unit can build whatever infrastructure whatever platform.

**[11:10]** whatever platform.

**[11:10]** whatever platform. um some organization

**[11:13]** um some organization

**[11:13]** um some organization have a very very strong tight

**[11:15]** have a very very strong tight

**[11:15]** have a very very strong tight abstraction of the service

**[11:16]** abstraction of the service

**[11:16]** abstraction of the service infrastructure and typically kind of

**[11:18]** infrastructure and typically kind of

**[11:18]** infrastructure and typically kind of have to use their platforms right so

**[11:21]** have to use their platforms right so

**[11:21]** have to use their platforms right so Bloomberg is kind of in the middle if

**[11:22]** Bloomberg is kind of in the middle if

**[11:22]** Bloomberg is kind of in the middle if you look at the golden ones we kind of

**[11:25]** you look at the golden ones we kind of

**[11:25]** you look at the golden ones we kind of believe in provide a golden path

**[11:28]** believe in provide a golden path

**[11:28]** believe in provide a golden path um with enablement teams so my team is

**[11:32]** um with enablement teams so my team is

**[11:32]** um with enablement teams so my team is really a en enabling team and one of the

**[11:36]** really a en enabling team and one of the

**[11:36]** really a en enabling team and one of the guiding principle for us is we want to

**[11:39]** guiding principle for us is we want to

**[11:39]** guiding principle for us is we want to make easy things extremely easy to do.

**[11:41]** make easy things extremely easy to do.

**[11:41]** make easy things extremely easy to do. Uh sorry, the right thing is extremely

**[11:43]** Uh sorry, the right thing is extremely

**[11:43]** Uh sorry, the right thing is extremely easy to do and we want to make sure the

**[11:44]** easy to do and we want to make sure the

**[11:44]** easy to do and we want to make sure the wrong thing is ridiculous hard to do.

**[11:46]** wrong thing is ridiculous hard to do.

**[11:46]** wrong thing is ridiculous hard to do. Right? So that's the guiding principle

**[11:48]** Right? So that's the guiding principle

**[11:48]** Right? So that's the guiding principle here.

**[11:50]** here.

**[11:50]** here. Now move on. So what is the pay path

**[11:52]** Now move on. So what is the pay path

**[11:52]** Now move on. So what is the pay path here? So the pay path is

**[11:55]** here? So the pay path is

**[11:55]** here? So the pay path is uh we have a gateway so that teams can

**[11:58]** uh we have a gateway so that teams can

**[11:58]** uh we have a gateway so that teams can easily figure out which model works the

**[11:59]** easily figure out which model works the


### [12:00 - 13:00]

**[12:00]** easily figure out which model works the best. They can do quick experiments.

**[12:02]** best. They can do quick experiments.

**[12:02]** best. They can do quick experiments. they can um we can have visibility what

**[12:05]** they can um we can have visibility what

**[12:05]** they can um we can have visibility what kind of models being used and we can

**[12:06]** kind of models being used and we can

**[12:06]** kind of models being used and we can also guide through teams which model

**[12:08]** also guide through teams which model

**[12:08]** also guide through teams which model should is a better fit for the for the

**[12:10]** should is a better fit for the for the

**[12:10]** should is a better fit for the for the problem they want to solve. uh we have a

**[12:12]** problem they want to solve. uh we have a

**[12:12]** problem they want to solve. uh we have a two discovery uh basically MCP directory

**[12:15]** two discovery uh basically MCP directory

**[12:15]** two discovery uh basically MCP directory via hub so that let's say team A wants

**[12:18]** via hub so that let's say team A wants

**[12:18]** via hub so that let's say team A wants to do something they will go to the hub

**[12:19]** to do something they will go to the hub

**[12:20]** to do something they will go to the hub okay someone is building MCB server

**[12:21]** okay someone is building MCB server

**[12:21]** okay someone is building MCB server already maybe I should partner with them

**[12:23]** already maybe I should partner with them

**[12:23]** already maybe I should partner with them to build it together right

**[12:26]** to build it together right

**[12:26]** to build it together right uh tool creation and deployment is via a

**[12:28]** uh tool creation and deployment is via a

**[12:28]** uh tool creation and deployment is via a pass it's basically a um you know a

**[12:32]** pass it's basically a um you know a

**[12:32]** pass it's basically a um you know a standard platform service where you can

**[12:35]** standard platform service where you can

**[12:35]** standard platform service where you can do your STLC and and we provide runtime

**[12:37]** do your STLC and and we provide runtime

**[12:37]** do your STLC and and we provide runtime environment for you as well taking care

**[12:39]** environment for you as well taking care

**[12:39]** environment for you as well taking care of all the off and side of things as

**[12:40]** of all the off and side of things as

**[12:40]** of all the off and side of things as well so it reduce friction of for for

**[12:43]** well so it reduce friction of for for

**[12:43]** well so it reduce friction of for for teams to to deploy um their MT MCP

**[12:46]** teams to to deploy um their MT MCP

**[12:46]** teams to to deploy um their MT MCP servers.

**[12:48]** servers.

**[12:48]** servers. And then the this is kind of interesting

**[12:51]** And then the this is kind of interesting

**[12:51]** And then the this is kind of interesting is we want to make demo very easy so

**[12:53]** is we want to make demo very easy so

**[12:53]** is we want to make demo very easy so that or I really say prove concept very

**[12:55]** that or I really say prove concept very

**[12:55]** that or I really say prove concept very easy so that people can try have ideal

**[12:58]** easy so that people can try have ideal

**[12:58]** easy so that people can try have ideal generation uh because we believe in


### [13:00 - 14:00]

**[13:00]** generation uh because we believe in

**[13:00]** generation uh because we believe in creativity come from some freedom of try

**[13:03]** creativity come from some freedom of try

**[13:03]** creativity come from some freedom of try different new things but we also want to

**[13:06]** different new things but we also want to

**[13:06]** different new things but we also want to make sure the production requires some

**[13:08]** make sure the production requires some

**[13:08]** make sure the production requires some quality control. um

**[13:12]** quality control. um

**[13:12]** quality control. um because at the end of the day stability

**[13:14]** because at the end of the day stability

**[13:14]** because at the end of the day stability and system reliability is at the core of

**[13:16]** and system reliability is at the core of

**[13:16]** and system reliability is at the core of our business. So this is sort of the pay

**[13:19]** our business. So this is sort of the pay

**[13:19]** our business. So this is sort of the pay path that we deployed um and enabled the

**[13:23]** path that we deployed um and enabled the

**[13:23]** path that we deployed um and enabled the rest of engineering really the 9,000

**[13:24]** rest of engineering really the 9,000

**[13:24]** rest of engineering really the 9,000 software engineers to do their job.

**[13:27]** software engineers to do their job.

**[13:27]** software engineers to do their job. Okay.

**[13:29]** Okay.

**[13:29]** Okay. And um with all this and then we start

**[13:32]** And um with all this and then we start

**[13:32]** And um with all this and then we start maybe okay yes we got p uh path we have

**[13:36]** maybe okay yes we got p uh path we have

**[13:36]** maybe okay yes we got p uh path we have some good ideas of how to evolve our

**[13:38]** some good ideas of how to evolve our

**[13:38]** some good ideas of how to evolve our codebase help our people right um now

**[13:43]** codebase help our people right um now

**[13:43]** codebase help our people right um now this is where I find that

**[13:47]** this is where I find that

**[13:47]** this is where I find that any new things any adoption of new

**[13:49]** any new things any adoption of new

**[13:49]** any new things any adoption of new things provide opportunity to leverage

**[13:52]** things provide opportunity to leverage

**[13:52]** things provide opportunity to leverage the strengths you have and also identify

**[13:54]** the strengths you have and also identify

**[13:54]** the strengths you have and also identify the some of the weakness that you may

**[13:55]** the some of the weakness that you may

**[13:55]** the some of the weakness that you may have. So um in Bloomberg we have a

**[13:59]** have. So um in Bloomberg we have a

**[13:59]** have. So um in Bloomberg we have a wellestablished training program uh it's


### [14:00 - 15:00]

**[14:02]** wellestablished training program uh it's

**[14:02]** wellestablished training program uh it's more than 20 years so there's on

**[14:03]** more than 20 years so there's on

**[14:03]** more than 20 years so there's on boarding training depends on entry level

**[14:05]** boarding training depends on entry level

**[14:05]** boarding training depends on entry level it depends on senior level um so we have

**[14:08]** it depends on senior level um so we have

**[14:08]** it depends on senior level um so we have this whole training program to prepare

**[14:10]** this whole training program to prepare

**[14:10]** this whole training program to prepare folks to before they join a team and

**[14:12]** folks to before they join a team and

**[14:12]** folks to before they join a team and what we did is we just incorporate AI

**[14:14]** what we did is we just incorporate AI

**[14:14]** what we did is we just incorporate AI coding in on boarding training program

**[14:17]** coding in on boarding training program

**[14:17]** coding in on boarding training program and also show them how to best utilize

**[14:20]** and also show them how to best utilize

**[14:20]** and also show them how to best utilize them with our principles and our

**[14:21]** them with our principles and our

**[14:21]** them with our principles and our technologies right there's a huge

**[14:23]** technologies right there's a huge

**[14:23]** technologies right there's a huge benefits here because um if any of you

**[14:26]** benefits here because um if any of you

**[14:26]** benefits here because um if any of you run into the challenge of adoption

**[14:28]** run into the challenge of adoption

**[14:28]** run into the challenge of adoption somehow run into a chasm right the rest

**[14:31]** somehow run into a chasm right the rest

**[14:31]** somehow run into a chasm right the rest of orc is not uh adopt as quick as

**[14:33]** of orc is not uh adopt as quick as

**[14:33]** of orc is not uh adopt as quick as possible whenever we have folks join a

**[14:36]** possible whenever we have folks join a

**[14:36]** possible whenever we have folks join a company they learn how to do things in

**[14:38]** company they learn how to do things in

**[14:38]** company they learn how to do things in new way when they go back to their team

**[14:39]** new way when they go back to their team

**[14:39]** new way when they go back to their team they were like hey why don't we do that

**[14:41]** they were like hey why don't we do that

**[14:41]** they were like hey why don't we do that right they're going to challenge the

**[14:42]** right they're going to challenge the

**[14:42]** right they're going to challenge the some of the senior folks as well to say

**[14:44]** some of the senior folks as well to say

**[14:44]** some of the senior folks as well to say hey there's a new way to do this type of

**[14:46]** hey there's a new way to do this type of

**[14:46]** hey there's a new way to do this type of things why don't we do that so we

**[14:47]** things why don't we do that so we

**[14:47]** things why don't we do that so we actually find this program extremely

**[14:49]** actually find this program extremely

**[14:49]** actually find this program extremely effective uh to be a change agent for

**[14:52]** effective uh to be a change agent for

**[14:52]** effective uh to be a change agent for anything want to push out

**[14:55]** anything want to push out

**[14:55]** anything want to push out and then bunch results there's a lot

**[14:57]** and then bunch results there's a lot

**[14:57]** and then bunch results there's a lot more f familiarity and comfort with the

**[14:59]** more f familiarity and comfort with the

**[14:59]** more f familiarity and comfort with the tooling. Um and also the important part


### [15:00 - 16:00]

**[15:02]** tooling. Um and also the important part

**[15:02]** tooling. Um and also the important part is there's a lot more nuance insights of

**[15:05]** is there's a lot more nuance insights of

**[15:05]** is there's a lot more nuance insights of where it's at value right

**[15:08]** where it's at value right

**[15:08]** where it's at value right the second one is um often times we run

**[15:12]** the second one is um often times we run

**[15:12]** the second one is um often times we run organization to push uh new initiatives

**[15:15]** organization to push uh new initiatives

**[15:16]** organization to push uh new initiatives so within Bloomer we have something

**[15:17]** so within Bloomer we have something

**[15:17]** so within Bloomer we have something called um a champ program and a guild

**[15:20]** called um a champ program and a guild

**[15:20]** called um a champ program and a guild program that's basically a cross

**[15:22]** program that's basically a cross

**[15:22]** program that's basically a cross organization or tech communities where

**[15:24]** organization or tech communities where

**[15:24]** organization or tech communities where people have similar interest and similar

**[15:26]** people have similar interest and similar

**[15:26]** people have similar interest and similar passion they get together and get stuff

**[15:28]** passion they get together and get stuff

**[15:28]** passion they get together and get stuff done so Um we had this for more than 10

**[15:32]** done so Um we had this for more than 10

**[15:32]** done so Um we had this for more than 10 years now. Uh we sort of bootstrapped

**[15:35]** years now. Uh we sort of bootstrapped

**[15:36]** years now. Uh we sort of bootstrapped engineer AI productivity community two

**[15:38]** engineer AI productivity community two

**[15:38]** engineer AI productivity community two years back leveraged the community we

**[15:40]** years back leveraged the community we

**[15:40]** years back leveraged the community we have already and then have some few

**[15:43]** have already and then have some few

**[15:43]** have already and then have some few results uh because we have this pretty

**[15:46]** results uh because we have this pretty

**[15:46]** results uh because we have this pretty much everyone passionate about this and

**[15:47]** much everyone passionate about this and

**[15:47]** much everyone passionate about this and will be in that community. So

**[15:50]** will be in that community. So

**[15:50]** will be in that community. So organically it dduplicates efforts and

**[15:53]** organically it dduplicates efforts and

**[15:53]** organically it dduplicates efforts and there's shared learning uh shared

**[15:55]** there's shared learning uh shared

**[15:55]** there's shared learning uh shared learning happening

**[15:57]** learning happening

**[15:57]** learning happening and it also helps to boost inner source

**[15:59]** and it also helps to boost inner source


### [16:00 - 17:00]

**[16:00]** and it also helps to boost inner source contributions and then visit engineer

**[16:01]** contributions and then visit engineer

**[16:01]** contributions and then visit engineer idea right often times team A wants to

**[16:03]** idea right often times team A wants to

**[16:03]** idea right often times team A wants to do something team B let's say a platform

**[16:05]** do something team B let's say a platform

**[16:05]** do something team B let's say a platform team have different prioritization and

**[16:08]** team have different prioritization and

**[16:08]** team have different prioritization and the way we solve this is via inner

**[16:11]** the way we solve this is via inner

**[16:11]** the way we solve this is via inner source or via visit engineer we just

**[16:12]** source or via visit engineer we just

**[16:12]** source or via visit engineer we just move someone over the team work for six

**[16:14]** move someone over the team work for six

**[16:14]** move someone over the team work for six months a year get it done and then we

**[16:16]** months a year get it done and then we

**[16:16]** months a year get it done and then we can move on Um the last one is

**[16:19]** can move on Um the last one is

**[16:19]** can move on Um the last one is interesting. So our data shows

**[16:21]** interesting. So our data shows

**[16:21]** interesting. So our data shows individual contributors have a much

**[16:24]** individual contributors have a much

**[16:24]** individual contributors have a much better stronger adoption than our

**[16:26]** better stronger adoption than our

**[16:26]** better stronger adoption than our leadership team. Now if you think about

**[16:28]** leadership team. Now if you think about

**[16:28]** leadership team. Now if you think about this a lot of software TLS and managers

**[16:33]** this a lot of software TLS and managers

**[16:34]** this a lot of software TLS and managers in the age of AI they kind of don't

**[16:37]** in the age of AI they kind of don't

**[16:37]** in the age of AI they kind of don't really have

**[16:39]** really have

**[16:39]** really have um enough experience to truly guide

**[16:42]** um enough experience to truly guide

**[16:42]** um enough experience to truly guide their teams to build software. Right? So

**[16:45]** their teams to build software. Right? So

**[16:45]** their teams to build software. Right? So often times the stuff that they learned

**[16:47]** often times the stuff that they learned

**[16:47]** often times the stuff that they learned before might not be exactly applicable,

**[16:50]** before might not be exactly applicable,

**[16:50]** before might not be exactly applicable, still very valuable, but there's some

**[16:51]** still very valuable, but there's some

**[16:51]** still very valuable, but there's some missing piece there to make sure they

**[16:53]** missing piece there to make sure they

**[16:53]** missing piece there to make sure they can continue to guide the team to do the

**[16:54]** can continue to guide the team to do the

**[16:54]** can continue to guide the team to do the right thing. So we're rolling out

**[16:56]** right thing. So we're rolling out

**[16:56]** right thing. So we're rolling out leadership workshops to make sure our

**[16:58]** leadership workshops to make sure our

**[16:58]** leadership workshops to make sure our leaders are equipped with whatever

**[16:59]** leaders are equipped with whatever

**[16:59]** leaders are equipped with whatever knowledge they need to have to drive the


### [17:00 - 18:00]

**[17:01]** knowledge they need to have to drive the

**[17:01]** knowledge they need to have to drive the techn um innovation.

**[17:05]** techn um innovation.

**[17:05]** techn um innovation. So um I'm going to close my part and to

**[17:10]** So um I'm going to close my part and to

**[17:10]** So um I'm going to close my part and to share with you what uh the part I'm I

**[17:12]** share with you what uh the part I'm I

**[17:12]** share with you what uh the part I'm I feel most excited about. The part I feel

**[17:15]** feel most excited about. The part I feel

**[17:15]** feel most excited about. The part I feel most excite most excited about is that

**[17:18]** most excite most excited about is that

**[17:18]** most excite most excited about is that with a lot of um creativity and

**[17:21]** with a lot of um creativity and

**[17:21]** with a lot of um creativity and innovation in the GI space, it actually

**[17:24]** innovation in the GI space, it actually

**[17:24]** innovation in the GI space, it actually changes the cost function of software

**[17:27]** changes the cost function of software

**[17:27]** changes the cost function of software engineering.

**[17:29]** engineering.

**[17:29]** engineering. Meaning

**[17:31]** Meaning

**[17:31]** Meaning the trade-off decision of whether we do

**[17:33]** the trade-off decision of whether we do

**[17:33]** the trade-off decision of whether we do something versus we don't do something

**[17:35]** something versus we don't do something

**[17:35]** something versus we don't do something actually changed because some of the

**[17:37]** actually changed because some of the

**[17:37]** actually changed because some of the work become a lot cheaper to do and some

**[17:39]** work become a lot cheaper to do and some

**[17:39]** work become a lot cheaper to do and some work become a lot more expensive to do.

**[17:41]** work become a lot more expensive to do.

**[17:41]** work become a lot more expensive to do. I tend to think it is a great

**[17:43]** I tend to think it is a great

**[17:43]** I tend to think it is a great opportunity for engineers and

**[17:47]** opportunity for engineers and

**[17:47]** opportunity for engineers and engineering leaders to get back to some

**[17:50]** engineering leaders to get back to some

**[17:50]** engineering leaders to get back to some of the uh basic principles and sort of

**[17:54]** of the uh basic principles and sort of

**[17:54]** of the uh basic principles and sort of ask a soul searching question. What is a

**[17:56]** ask a soul searching question. What is a

**[17:56]** ask a soul searching question. What is a high quality soft engineering and how

**[17:58]** high quality soft engineering and how

**[17:58]** high quality soft engineering and how can we use a tool for that purpose? So


### [18:00 - 19:00]

**[18:00]** can we use a tool for that purpose? So

**[18:00]** can we use a tool for that purpose? So that's it. Thank you very much.

**[18:02]** that's it. Thank you very much.

**[18:02]** that's it. Thank you very much. [applause]

**[18:04]** [applause]

**[18:04]** [applause] [music]


