# Building Alice’s Brain- an AI Sales Rep that Learns Like a Human - Sherwood & Satwik, 11x

**Video URL:** https://www.youtube.com/watch?v=KWmkMV0FNwQ

---

## Full Transcript

### [00:00 - 01:00]

**[00:18]** Okay, thanks everyone for coming today.

**[00:18]** Okay, thanks everyone for coming today. Uh, so today's talk is called Building

**[00:19]** Uh, so today's talk is called Building

**[00:20]** Uh, so today's talk is called Building Alice's Brain. How we built an AI sales

**[00:22]** Alice's Brain. How we built an AI sales

**[00:22]** Alice's Brain. How we built an AI sales rep that learns like a human.

**[00:25]** rep that learns like a human.

**[00:25]** rep that learns like a human. Uh, my name is Sherwood. I am one of the

**[00:26]** Uh, my name is Sherwood. I am one of the

**[00:26]** Uh, my name is Sherwood. I am one of the tech leads here at 11X. I lead

**[00:28]** tech leads here at 11X. I lead

**[00:28]** tech leads here at 11X. I lead engineering for our Alice product and

**[00:30]** engineering for our Alice product and

**[00:30]** engineering for our Alice product and I'm joined by my colleague Saw.

**[00:34]** I'm joined by my colleague Saw.

**[00:34]** I'm joined by my colleague Saw. So 11X for those of you who are

**[00:35]** So 11X for those of you who are

**[00:35]** So 11X for those of you who are unfamiliar is a company that's building

**[00:37]** unfamiliar is a company that's building

**[00:37]** unfamiliar is a company that's building digital workers for the go to market

**[00:39]** digital workers for the go to market

**[00:39]** digital workers for the go to market organization. We have two digital

**[00:41]** organization. We have two digital

**[00:41]** organization. We have two digital workers today. We have Alice who is our

**[00:42]** workers today. We have Alice who is our

**[00:42]** workers today. We have Alice who is our AI SDR and then we also have Julian who

**[00:45]** AI SDR and then we also have Julian who

**[00:45]** AI SDR and then we also have Julian who is our voice agent and we have more

**[00:47]** is our voice agent and we have more

**[00:47]** is our voice agent and we have more workers on the way.

**[00:49]** workers on the way.

**[00:49]** workers on the way. Today we're going to be talking about

**[00:50]** Today we're going to be talking about

**[00:50]** Today we're going to be talking about Alice specifically and actually uh

**[00:53]** Alice specifically and actually uh

**[00:53]** Alice specifically and actually uh Alice's brain or the knowledge base

**[00:55]** Alice's brain or the knowledge base

**[00:55]** Alice's brain or the knowledge base which is effectively her brain.

**[00:58]** which is effectively her brain.

**[00:58]** which is effectively her brain. So let's start from the basics. Uh what


### [01:00 - 02:00]

**[01:00]** So let's start from the basics. Uh what

**[01:00]** So let's start from the basics. Uh what what is an SDR? Well, an SDR is is a

**[01:02]** what is an SDR? Well, an SDR is is a

**[01:02]** what is an SDR? Well, an SDR is is a sales development representative if

**[01:04]** sales development representative if

**[01:04]** sales development representative if you're not familiar. I know that's a

**[01:05]** you're not familiar. I know that's a

**[01:05]** you're not familiar. I know that's a room full of engineers, so I thought I

**[01:07]** room full of engineers, so I thought I

**[01:07]** room full of engineers, so I thought I would start with the basics. And this is

**[01:08]** would start with the basics. And this is

**[01:08]** would start with the basics. And this is essentially an entry-level sales role.

**[01:10]** essentially an entry-level sales role.

**[01:10]** essentially an entry-level sales role. This is the kind of job that you might

**[01:11]** This is the kind of job that you might

**[01:12]** This is the kind of job that you might get uh right out of school. And your

**[01:14]** get uh right out of school. And your

**[01:14]** get uh right out of school. And your responsibilities basically boil down to

**[01:16]** responsibilities basically boil down to

**[01:16]** responsibilities basically boil down to three things. First, you're sourcing

**[01:18]** three things. First, you're sourcing

**[01:18]** three things. First, you're sourcing leads. These are people that you'd like

**[01:19]** leads. These are people that you'd like

**[01:19]** leads. These are people that you'd like to sell to. Then you're contacting them

**[01:22]** to sell to. Then you're contacting them

**[01:22]** to sell to. Then you're contacting them or engaging them across channels. And

**[01:24]** or engaging them across channels. And

**[01:24]** or engaging them across channels. And finally, you're booking meetings with

**[01:25]** finally, you're booking meetings with

**[01:25]** finally, you're booking meetings with those people. So your goal here is to

**[01:28]** those people. So your goal here is to

**[01:28]** those people. So your goal here is to generate positive replies and meetings

**[01:30]** generate positive replies and meetings

**[01:30]** generate positive replies and meetings booked. These are the two uh key metrics

**[01:31]** booked. These are the two uh key metrics

**[01:31]** booked. These are the two uh key metrics for an SDR.

**[01:34]** for an SDR.

**[01:34]** for an SDR. And a lot of an SDR's job boils down to

**[01:36]** And a lot of an SDR's job boils down to

**[01:36]** And a lot of an SDR's job boils down to writing emails like the one that you see

**[01:38]** writing emails like the one that you see

**[01:38]** writing emails like the one that you see in front of you right now. This is

**[01:39]** in front of you right now. This is

**[01:39]** in front of you right now. This is actually an email that Alice has written

**[01:41]** actually an email that Alice has written

**[01:41]** actually an email that Alice has written and uh it's an example of the type of uh

**[01:45]** and uh it's an example of the type of uh

**[01:45]** and uh it's an example of the type of uh type of work output that Alice has. Uh

**[01:47]** type of work output that Alice has. Uh

**[01:47]** type of work output that Alice has. Uh Alice sends about 50,000 of these emails

**[01:49]** Alice sends about 50,000 of these emails

**[01:49]** Alice sends about 50,000 of these emails to uh in a given day and that's in

**[01:52]** to uh in a given day and that's in

**[01:52]** to uh in a given day and that's in comparison to a human SDR who would send

**[01:54]** comparison to a human SDR who would send

**[01:54]** comparison to a human SDR who would send 20 to 50. Uh and Alice is now running

**[01:57]** 20 to 50. Uh and Alice is now running

**[01:57]** 20 to 50. Uh and Alice is now running campaigns for about 300 different uh


### [02:00 - 03:00]

**[02:00]** campaigns for about 300 different uh

**[02:00]** campaigns for about 300 different uh business organizations.

**[02:03]** business organizations.

**[02:03]** business organizations. So before we go any further, I want to

**[02:05]** So before we go any further, I want to

**[02:05]** So before we go any further, I want to define some terms because since we work

**[02:07]** define some terms because since we work

**[02:07]** define some terms because since we work at 11X, we have our customers but then

**[02:09]** at 11X, we have our customers but then

**[02:09]** at 11X, we have our customers but then our customers also have their customers.

**[02:11]** our customers also have their customers.

**[02:11]** our customers also have their customers. So things get a little confusing. Uh

**[02:13]** So things get a little confusing. Uh

**[02:13]** So things get a little confusing. Uh today we'll be using the term seller to

**[02:15]** today we'll be using the term seller to

**[02:15]** today we'll be using the term seller to refer to the company that is selling

**[02:16]** refer to the company that is selling

**[02:16]** refer to the company that is selling something through Alice. That is our

**[02:18]** something through Alice. That is our

**[02:18]** something through Alice. That is our customer. And then we'll be using the

**[02:20]** customer. And then we'll be using the

**[02:20]** customer. And then we'll be using the term lead to refer to the person who's

**[02:21]** term lead to refer to the person who's

**[02:21]** term lead to refer to the person who's being sold to.

**[02:24]** being sold to.

**[02:24]** being sold to. And here's what that looks like as a

**[02:25]** And here's what that looks like as a

**[02:25]** And here's what that looks like as a diagram. You can see the seller is

**[02:27]** diagram. You can see the seller is

**[02:27]** diagram. You can see the seller is pushing context about their business.

**[02:29]** pushing context about their business.

**[02:29]** pushing context about their business. These are the the products that they

**[02:31]** These are the the products that they

**[02:31]** These are the the products that they sell or the uh case studies that they

**[02:33]** sell or the uh case studies that they

**[02:33]** sell or the uh case studies that they have that they can reference in emails.

**[02:34]** have that they can reference in emails.

**[02:34]** have that they can reference in emails. She they're pushing that to Alice and

**[02:36]** She they're pushing that to Alice and

**[02:36]** She they're pushing that to Alice and then Alice is then using that to

**[02:38]** then Alice is then using that to

**[02:38]** then Alice is then using that to personalize emails for each of the leads

**[02:39]** personalize emails for each of the leads

**[02:39]** personalize emails for each of the leads that she contacts.

**[02:42]** that she contacts.

**[02:42]** that she contacts. So there are two requirements that Alice

**[02:44]** So there are two requirements that Alice

**[02:44]** So there are two requirements that Alice needs to uh in order to succeed in her

**[02:46]** needs to uh in order to succeed in her

**[02:46]** needs to uh in order to succeed in her role. The first is that she needs to

**[02:48]** role. The first is that she needs to

**[02:48]** role. The first is that she needs to know the seller, the products, the the

**[02:50]** know the seller, the products, the the

**[02:50]** know the seller, the products, the the services, the case studies, the pain

**[02:52]** services, the case studies, the pain

**[02:52]** services, the case studies, the pain points, the value props, the ICP. And

**[02:54]** points, the value props, the ICP. And

**[02:54]** points, the value props, the ICP. And the second is that she needs to know the

**[02:56]** the second is that she needs to know the

**[02:56]** the second is that she needs to know the lead, uh their role, their

**[02:58]** lead, uh their role, their

**[02:58]** lead, uh their role, their responsibilities, what they care about,

**[02:59]** responsibilities, what they care about,

**[02:59]** responsibilities, what they care about, what other solutions they've tried, uh


### [03:00 - 04:00]

**[03:01]** what other solutions they've tried, uh

**[03:01]** what other solutions they've tried, uh pain points that they might have be

**[03:02]** pain points that they might have be

**[03:02]** pain points that they might have be experiencing, the company they work for.

**[03:05]** experiencing, the company they work for.

**[03:05]** experiencing, the company they work for. And today we're going to be really

**[03:06]** And today we're going to be really

**[03:06]** And today we're going to be really focused on knowing the seller.

**[03:09]** focused on knowing the seller.

**[03:09]** focused on knowing the seller. So in our in the old version of our

**[03:11]** So in our in the old version of our

**[03:11]** So in our in the old version of our product, the seller would be responsible

**[03:13]** product, the seller would be responsible

**[03:13]** product, the seller would be responsible for pushing context about her uh about

**[03:15]** for pushing context about her uh about

**[03:15]** for pushing context about her uh about their business to Alice. And they did so

**[03:18]** their business to Alice. And they did so

**[03:18]** their business to Alice. And they did so through a manual experience uh called

**[03:21]** through a manual experience uh called

**[03:21]** through a manual experience uh called the library. And here you could see what

**[03:22]** the library. And here you could see what

**[03:22]** the library. And here you could see what it looks like there where the library

**[03:24]** it looks like there where the library

**[03:24]** it looks like there where the library shows uh all of the different products

**[03:26]** shows uh all of the different products

**[03:26]** shows uh all of the different products and offers that are available for this

**[03:28]** and offers that are available for this

**[03:28]** and offers that are available for this business that uh Alice can then

**[03:30]** business that uh Alice can then

**[03:30]** business that uh Alice can then reference when she writes emails. The

**[03:32]** reference when she writes emails. The

**[03:32]** reference when she writes emails. The user would have to enter details about

**[03:34]** user would have to enter details about

**[03:34]** user would have to enter details about all every individual product and service

**[03:36]** all every individual product and service

**[03:36]** all every individual product and service and all of the pain points and solutions

**[03:37]** and all of the pain points and solutions

**[03:37]** and all of the pain points and solutions and value props associated with them in

**[03:39]** and value props associated with them in

**[03:40]** and value props associated with them in our dashboard and including these

**[03:41]** our dashboard and including these

**[03:41]** our dashboard and including these detailed descriptions. And those

**[03:43]** detailed descriptions. And those

**[03:43]** detailed descriptions. And those descriptions would uh were were

**[03:45]** descriptions would uh were were

**[03:45]** descriptions would uh were were important to get right because these

**[03:46]** important to get right because these

**[03:46]** important to get right because these actually get included in the context for

**[03:48]** actually get included in the context for

**[03:48]** actually get included in the context for the emails or for Alice when she writes

**[03:50]** the emails or for Alice when she writes

**[03:50]** the emails or for Alice when she writes the emails.

**[03:52]** the emails.

**[03:52]** the emails. Then later on during campaign creation,

**[03:55]** Then later on during campaign creation,

**[03:55]** Then later on during campaign creation, this is what it looks like to to create

**[03:56]** this is what it looks like to to create

**[03:56]** this is what it looks like to to create a campaign. And you can see we have a

**[03:57]** a campaign. And you can see we have a

**[03:57]** a campaign. And you can see we have a lead in the top left and the user is


### [04:00 - 05:00]

**[04:00]** lead in the top left and the user is

**[04:00]** lead in the top left and the user is selecting the different offers that

**[04:01]** selecting the different offers that

**[04:01]** selecting the different offers that they've defined from the library in the

**[04:03]** they've defined from the library in the

**[04:03]** they've defined from the library in the top right that and these are the offers

**[04:05]** top right that and these are the offers

**[04:05]** top right that and these are the offers that Alice has access to when she's

**[04:06]** that Alice has access to when she's

**[04:06]** that Alice has access to when she's generating her emails.

**[04:09]** generating her emails.

**[04:09]** generating her emails. We had a lot of problems with this user

**[04:11]** We had a lot of problems with this user

**[04:11]** We had a lot of problems with this user experience and the first one was it was

**[04:13]** experience and the first one was it was

**[04:13]** experience and the first one was it was just extremely tedious. It was a really

**[04:15]** just extremely tedious. It was a really

**[04:15]** just extremely tedious. It was a really bad and and and cumbersome user

**[04:17]** bad and and and cumbersome user

**[04:17]** bad and and and cumbersome user experience. The user had to enter a lot

**[04:18]** experience. The user had to enter a lot

**[04:18]** experience. The user had to enter a lot of information and that created this

**[04:20]** of information and that created this

**[04:20]** of information and that created this onboarding friction where uh users

**[04:23]** onboarding friction where uh users

**[04:23]** onboarding friction where uh users couldn't actually run campaigns until

**[04:25]** couldn't actually run campaigns until

**[04:25]** couldn't actually run campaigns until they hadn't filled out their library.

**[04:27]** they hadn't filled out their library.

**[04:27]** they hadn't filled out their library. And finally, the emails that we were

**[04:29]** And finally, the emails that we were

**[04:29]** And finally, the emails that we were generating using this approach were just

**[04:30]** generating using this approach were just

**[04:30]** generating using this approach were just sub-optimal. Users would have to either

**[04:32]** sub-optimal. Users would have to either

**[04:32]** sub-optimal. Users would have to either choose between too few email or too few

**[04:34]** choose between too few email or too few

**[04:34]** choose between too few email or too few offers, uh, which meant that, uh, you'd

**[04:36]** offers, uh, which meant that, uh, you'd

**[04:36]** offers, uh, which meant that, uh, you'd have irrelevant offers for a given lead,

**[04:38]** have irrelevant offers for a given lead,

**[04:38]** have irrelevant offers for a given lead, or too many offers, which means that you

**[04:40]** or too many offers, which means that you

**[04:40]** or too many offers, which means that you have all of the stuff in the context

**[04:42]** have all of the stuff in the context

**[04:42]** have all of the stuff in the context window, and Alice just wasn't as smart

**[04:43]** window, and Alice just wasn't as smart

**[04:43]** window, and Alice just wasn't as smart when she write writes those emails.

**[04:47]** when she write writes those emails.

**[04:47]** when she write writes those emails. So, how can we address this?

**[04:49]** So, how can we address this?

**[04:49]** So, how can we address this? Well, we had an idea which is that

**[04:51]** Well, we had an idea which is that

**[04:51]** Well, we had an idea which is that instead of the seller being responsible

**[04:53]** instead of the seller being responsible

**[04:53]** instead of the seller being responsible for pushing context about the business

**[04:55]** for pushing context about the business

**[04:55]** for pushing context about the business to Alice, we could flip things around so

**[04:57]** to Alice, we could flip things around so

**[04:57]** to Alice, we could flip things around so that Alice can proactively uh pull all


### [05:00 - 06:00]

**[05:00]** that Alice can proactively uh pull all

**[05:00]** that Alice can proactively uh pull all of the context about the seller into her

**[05:02]** of the context about the seller into her

**[05:02]** of the context about the seller into her system and then use what'sever whatever

**[05:04]** system and then use what'sever whatever

**[05:04]** system and then use what'sever whatever is most relevant when writing those

**[05:05]** is most relevant when writing those

**[05:05]** is most relevant when writing those emails. And that's effectively what we

**[05:07]** emails. And that's effectively what we

**[05:07]** emails. And that's effectively what we accomplished with the knowledge base

**[05:09]** accomplished with the knowledge base

**[05:09]** accomplished with the knowledge base which we'll tell you more about in just

**[05:10]** which we'll tell you more about in just

**[05:10]** which we'll tell you more about in just a moment.

**[05:12]** a moment.

**[05:12]** a moment. So for the rest of the talk, we're going

**[05:13]** So for the rest of the talk, we're going

**[05:13]** So for the rest of the talk, we're going to first do a highle overview of the

**[05:15]** to first do a highle overview of the

**[05:16]** to first do a highle overview of the knowledge base and how it works. Then we

**[05:18]** knowledge base and how it works. Then we

**[05:18]** knowledge base and how it works. Then we will do a deep dive on the pipeline, the

**[05:20]** will do a deep dive on the pipeline, the

**[05:20]** will do a deep dive on the pipeline, the different steps in our rag system

**[05:22]** different steps in our rag system

**[05:22]** different steps in our rag system pipeline.

**[05:24]** pipeline.

**[05:24]** pipeline. Then after that we will talk through the

**[05:26]** Then after that we will talk through the

**[05:26]** Then after that we will talk through the user experience of the knowledge base

**[05:28]** user experience of the knowledge base

**[05:28]** user experience of the knowledge base and we will wrap up with some lessons

**[05:29]** and we will wrap up with some lessons

**[05:30]** and we will wrap up with some lessons from this project and uh future plans.

**[05:33]** from this project and uh future plans.

**[05:33]** from this project and uh future plans. So let's start out with an overview. All

**[05:35]** So let's start out with an overview. All

**[05:35]** So let's start out with an overview. All right. So overview, what is knowledge

**[05:37]** right. So overview, what is knowledge

**[05:37]** right. So overview, what is knowledge base, right? It's basically a way for us

**[05:41]** base, right? It's basically a way for us

**[05:41]** base, right? It's basically a way for us to kind of get closer to a human

**[05:42]** to kind of get closer to a human

**[05:42]** to kind of get closer to a human experience. Like if a hum if you're

**[05:45]** experience. Like if a hum if you're

**[05:45]** experience. Like if a hum if you're training a human SDR, you would kind of

**[05:46]** training a human SDR, you would kind of

**[05:46]** training a human SDR, you would kind of get them in and then you will basically

**[05:49]** get them in and then you will basically

**[05:49]** get them in and then you will basically dump a bunch of documents on them and

**[05:50]** dump a bunch of documents on them and

**[05:50]** dump a bunch of documents on them and then they ramp up throughout a period of

**[05:53]** then they ramp up throughout a period of

**[05:53]** then they ramp up throughout a period of like weeks or months. Um, and you can

**[05:56]** like weeks or months. Um, and you can

**[05:56]** like weeks or months. Um, and you can basically check in on their prog

**[05:57]** basically check in on their prog

**[05:57]** basically check in on their prog progress. Um, and similar to that,


### [06:00 - 07:00]

**[06:00]** progress. Um, and similar to that,

**[06:00]** progress. Um, and similar to that, knowledge base is basically a

**[06:02]** knowledge base is basically a

**[06:02]** knowledge base is basically a centralized repository on our platform

**[06:03]** centralized repository on our platform

**[06:03]** centralized repository on our platform for the seller info and then users can

**[06:05]** for the seller info and then users can

**[06:05]** for the seller info and then users can kind of come in, dump all their source

**[06:07]** kind of come in, dump all their source

**[06:07]** kind of come in, dump all their source material and then we are able to

**[06:09]** material and then we are able to

**[06:09]** material and then we are able to reference that information at the time

**[06:11]** reference that information at the time

**[06:11]** reference that information at the time of message generation. Um, now what

**[06:13]** of message generation. Um, now what

**[06:14]** of message generation. Um, now what resources do SDRs care about? Here's a

**[06:16]** resources do SDRs care about? Here's a

**[06:16]** resources do SDRs care about? Here's a little glimpse into that. Marketing

**[06:17]** little glimpse into that. Marketing

**[06:17]** little glimpse into that. Marketing materials, case studies, uh, sales

**[06:20]** materials, case studies, uh, sales

**[06:20]** materials, case studies, uh, sales calls, press releases, you know, and a

**[06:21]** calls, press releases, you know, and a

**[06:21]** calls, press releases, you know, and a bunch of other stuff. Um, now, how do we

**[06:24]** bunch of other stuff. Um, now, how do we

**[06:24]** bunch of other stuff. Um, now, how do we bucket these into categories that we're

**[06:26]** bucket these into categories that we're

**[06:26]** bucket these into categories that we're actually going to parse? Uh, well, we

**[06:29]** actually going to parse? Uh, well, we

**[06:29]** actually going to parse? Uh, well, we created documents and images, websites,

**[06:32]** created documents and images, websites,

**[06:32]** created documents and images, websites, and then media, audio, video, and you're

**[06:33]** and then media, audio, video, and you're

**[06:33]** and then media, audio, video, and you're going to see why that's important.

**[06:36]** going to see why that's important.

**[06:36]** going to see why that's important. So, here's an overview of what the

**[06:38]** So, here's an overview of what the

**[06:38]** So, here's an overview of what the architecture looks like. It starts off

**[06:40]** architecture looks like. It starts off

**[06:40]** architecture looks like. It starts off with the user uploading something any

**[06:42]** with the user uploading something any

**[06:42]** with the user uploading something any document or resource in the client and

**[06:44]** document or resource in the client and

**[06:44]** document or resource in the client and then we save it to our S3 bucket and

**[06:46]** then we save it to our S3 bucket and

**[06:46]** then we save it to our S3 bucket and then send it to the back end um which

**[06:49]** then send it to the back end um which

**[06:49]** then send it to the back end um which then you know creates a bunch of

**[06:51]** then you know creates a bunch of

**[06:51]** then you know creates a bunch of resources in our DB and then kicks off a

**[06:53]** resources in our DB and then kicks off a

**[06:53]** resources in our DB and then kicks off a bunch of jobs depending on the resource

**[06:54]** bunch of jobs depending on the resource

**[06:54]** bunch of jobs depending on the resource type and the vendor selected. Now the

**[06:57]** type and the vendor selected. Now the

**[06:57]** type and the vendor selected. Now the vendors are asynchronously doing the

**[06:59]** vendors are asynchronously doing the

**[06:59]** vendors are asynchronously doing the parsing. Once they're done, they send a


### [07:00 - 08:00]

**[07:00]** parsing. Once they're done, they send a

**[07:00]** parsing. Once they're done, they send a web hook to us which we consume via

**[07:02]** web hook to us which we consume via

**[07:02]** web hook to us which we consume via ingest and then once we've consumed that

**[07:05]** ingest and then once we've consumed that

**[07:05]** ingest and then once we've consumed that web hook, we take that parsed uh

**[07:09]** web hook, we take that parsed uh

**[07:09]** web hook, we take that parsed uh artifact that we get back from the

**[07:11]** artifact that we get back from the

**[07:11]** artifact that we get back from the vendors and then we store it in our DB

**[07:13]** vendors and then we store it in our DB

**[07:13]** vendors and then we store it in our DB and then at the same time upsert it to

**[07:15]** and then at the same time upsert it to

**[07:15]** and then at the same time upsert it to pine cone and embed it. Um, and then

**[07:18]** pine cone and embed it. Um, and then

**[07:18]** pine cone and embed it. Um, and then eventually once we store it in local DB,

**[07:20]** eventually once we store it in local DB,

**[07:20]** eventually once we store it in local DB, we have like a UI update and then

**[07:23]** we have like a UI update and then

**[07:23]** we have like a UI update and then eventually our agent can query pine

**[07:25]** eventually our agent can query pine

**[07:26]** eventually our agent can query pine cone, our vector DB for that stored

**[07:28]** cone, our vector DB for that stored

**[07:28]** cone, our vector DB for that stored information that we just put in. So now

**[07:31]** information that we just put in. So now

**[07:32]** information that we just put in. So now that we have a high level of

**[07:33]** that we have a high level of

**[07:33]** that we have a high level of understanding of how the knowledge base

**[07:34]** understanding of how the knowledge base

**[07:34]** understanding of how the knowledge base works, let's dig into each individual

**[07:36]** works, let's dig into each individual

**[07:36]** works, let's dig into each individual step in the pipeline. There are five

**[07:38]** step in the pipeline. There are five

**[07:38]** step in the pipeline. There are five different steps in the pipeline. The

**[07:39]** different steps in the pipeline. The

**[07:40]** different steps in the pipeline. The first is parsing. Then there's chunking.

**[07:43]** first is parsing. Then there's chunking.

**[07:43]** first is parsing. Then there's chunking. Then there's storage. Then there's

**[07:45]** Then there's storage. Then there's

**[07:45]** Then there's storage. Then there's retrieval. And finally, we have

**[07:47]** retrieval. And finally, we have

**[07:47]** retrieval. And finally, we have visualization, which will uh sounds a

**[07:49]** visualization, which will uh sounds a

**[07:49]** visualization, which will uh sounds a little untraditional, but we'll cover it

**[07:50]** little untraditional, but we'll cover it

**[07:50]** little untraditional, but we'll cover it in a in a moment. So, let's start with

**[07:52]** in a in a moment. So, let's start with

**[07:52]** in a in a moment. So, let's start with parsing. Uh what is parsing? I think

**[07:55]** parsing. Uh what is parsing? I think

**[07:55]** parsing. Uh what is parsing? I think that we probably all take this for

**[07:56]** that we probably all take this for

**[07:56]** that we probably all take this for granted, but it's worth defining.

**[07:58]** granted, but it's worth defining.

**[07:58]** granted, but it's worth defining. Parsing is the process of converting a


### [08:00 - 09:00]

**[08:00]** Parsing is the process of converting a

**[08:00]** Parsing is the process of converting a non-ext resource into text. And the

**[08:03]** non-ext resource into text. And the

**[08:03]** non-ext resource into text. And the reason that this is necessary is

**[08:04]** reason that this is necessary is

**[08:04]** reason that this is necessary is because, as we all know, language

**[08:06]** because, as we all know, language

**[08:06]** because, as we all know, language models, they speak text. So in order to

**[08:08]** models, they speak text. So in order to

**[08:08]** models, they speak text. So in order to make information that is represented in

**[08:10]** make information that is represented in

**[08:10]** make information that is represented in a different form like a PDF or an MP4

**[08:13]** a different form like a PDF or an MP4

**[08:13]** a different form like a PDF or an MP4 file or a or an image legible or useful

**[08:17]** file or a or an image legible or useful

**[08:17]** file or a or an image legible or useful to the LLM, we need to first convert it

**[08:18]** to the LLM, we need to first convert it

**[08:18]** to the LLM, we need to first convert it to text. And so one way of thinking

**[08:21]** to text. And so one way of thinking

**[08:21]** to text. And so one way of thinking about parsing is it's the process of

**[08:22]** about parsing is it's the process of

**[08:22]** about parsing is it's the process of making non-ext information legible to a

**[08:24]** making non-ext information legible to a

**[08:24]** making non-ext information legible to a large language model. Um and we do have

**[08:26]** large language model. Um and we do have

**[08:26]** large language model. Um and we do have multimodal models that are one solution

**[08:28]** multimodal models that are one solution

**[08:28]** multimodal models that are one solution to this, but there are lots of

**[08:29]** to this, but there are lots of

**[08:29]** to this, but there are lots of restrictions on multimodal models that

**[08:31]** restrictions on multimodal models that

**[08:31]** restrictions on multimodal models that make it u that make parsing still

**[08:33]** make it u that make parsing still

**[08:33]** make it u that make parsing still relevant.

**[08:35]** relevant.

**[08:35]** relevant. So to illustrate that we have the five

**[08:37]** So to illustrate that we have the five

**[08:37]** So to illustrate that we have the five different document types or resource

**[08:38]** different document types or resource

**[08:38]** different document types or resource types that we mentioned momentarily ago

**[08:40]** types that we mentioned momentarily ago

**[08:40]** types that we mentioned momentarily ago uh going through our parsing process and

**[08:42]** uh going through our parsing process and

**[08:42]** uh going through our parsing process and coming out is actually markdown which is

**[08:44]** coming out is actually markdown which is

**[08:44]** coming out is actually markdown which is a type of text that as we all know

**[08:46]** a type of text that as we all know

**[08:46]** a type of text that as we all know contains some structural information and

**[08:48]** contains some structural information and

**[08:48]** contains some structural information and formatting which is actually

**[08:49]** formatting which is actually

**[08:49]** formatting which is actually semantically semantically meaningful and

**[08:51]** semantically semantically meaningful and

**[08:51]** semantically semantically meaningful and useful.

**[08:53]** useful.

**[08:53]** useful. Let's talk about the process of how we

**[08:54]** Let's talk about the process of how we

**[08:54]** Let's talk about the process of how we implemented parsid and the the short

**[08:56]** implemented parsid and the the short

**[08:56]** implemented parsid and the the short answer is that we did not we didn't want

**[08:58]** answer is that we did not we didn't want

**[08:58]** answer is that we did not we didn't want to build this from scratch and we had a


### [09:00 - 10:00]

**[09:01]** to build this from scratch and we had a

**[09:01]** to build this from scratch and we had a few different reasons for doing this.

**[09:02]** few different reasons for doing this.

**[09:02]** few different reasons for doing this. The first is that you just saw that we

**[09:04]** The first is that you just saw that we

**[09:04]** The first is that you just saw that we had five different resource types and a

**[09:06]** had five different resource types and a

**[09:06]** had five different resource types and a lot of different file types within each

**[09:07]** lot of different file types within each

**[09:07]** lot of different file types within each of them. We thought it was going to be

**[09:08]** of them. We thought it was going to be

**[09:08]** of them. We thought it was going to be too many and we thought it was going to

**[09:10]** too many and we thought it was going to

**[09:10]** too many and we thought it was going to be too much work. We wanted to get to

**[09:11]** be too much work. We wanted to get to

**[09:11]** be too much work. We wanted to get to market quickly. Um the last reason was

**[09:14]** market quickly. Um the last reason was

**[09:14]** market quickly. Um the last reason was that we just weren't that confident in

**[09:15]** that we just weren't that confident in

**[09:16]** that we just weren't that confident in the outcome. There are vendors who

**[09:17]** the outcome. There are vendors who

**[09:17]** the outcome. There are vendors who dedicate their entire company to

**[09:19]** dedicate their entire company to

**[09:19]** dedicate their entire company to building an effective parsing system for

**[09:21]** building an effective parsing system for

**[09:21]** building an effective parsing system for a specific resource type. We didn't want

**[09:23]** a specific resource type. We didn't want

**[09:23]** a specific resource type. We didn't want our team to to have to become

**[09:25]** our team to to have to become

**[09:25]** our team to to have to become specialists in in parsing for each one

**[09:27]** specialists in in parsing for each one

**[09:27]** specialists in in parsing for each one of these resource types and to build a a

**[09:29]** of these resource types and to build a a

**[09:29]** of these resource types and to build a a parsing system for that. We thought that

**[09:31]** parsing system for that. We thought that

**[09:31]** parsing system for that. We thought that maybe if we tried to do this, the

**[09:33]** maybe if we tried to do this, the

**[09:33]** maybe if we tried to do this, the outcome actually just wouldn't be that

**[09:34]** outcome actually just wouldn't be that

**[09:34]** outcome actually just wouldn't be that that successful. So, we chose to work

**[09:37]** that successful. So, we chose to work

**[09:37]** that successful. So, we chose to work with a vendor and here are a bunch of

**[09:39]** with a vendor and here are a bunch of

**[09:39]** with a vendor and here are a bunch of the vendors that we we came across. You

**[09:41]** the vendors that we we came across. You

**[09:41]** the vendors that we we came across. You can find 10 or 20 or 50 with just a

**[09:44]** can find 10 or 20 or 50 with just a

**[09:44]** can find 10 or 20 or 50 with just a quick Google search, but these are some

**[09:45]** quick Google search, but these are some

**[09:45]** quick Google search, but these are some of the leaders that we evaluated

**[09:48]** of the leaders that we evaluated

**[09:48]** of the leaders that we evaluated and in order to make a decision, we came

**[09:50]** and in order to make a decision, we came

**[09:50]** and in order to make a decision, we came up with some requirements and three

**[09:52]** up with some requirements and three

**[09:52]** up with some requirements and three specific requirements. The first was

**[09:54]** specific requirements. The first was

**[09:54]** specific requirements. The first was that we needed support for our necessary

**[09:56]** that we needed support for our necessary

**[09:56]** that we needed support for our necessary resource types. That goes without

**[09:58]** resource types. That goes without

**[09:58]** resource types. That goes without saying. We also wanted markdown output.


### [10:00 - 11:00]

**[10:01]** saying. We also wanted markdown output.

**[10:01]** saying. We also wanted markdown output. And then finally, we wanted this vendor

**[10:02]** And then finally, we wanted this vendor

**[10:02]** And then finally, we wanted this vendor to support web hooks. We wanted to be

**[10:04]** to support web hooks. We wanted to be

**[10:04]** to support web hooks. We wanted to be able to receive that output in a

**[10:05]** able to receive that output in a

**[10:06]** able to receive that output in a convenient manner.

**[10:08]** convenient manner.

**[10:08]** convenient manner. A few things that we didn't consider to

**[10:09]** A few things that we didn't consider to

**[10:09]** A few things that we didn't consider to start out with. Accuracy.

**[10:12]** start out with. Accuracy.

**[10:12]** start out with. Accuracy. Crazy. We didn't consider accuracy. We

**[10:15]** Crazy. We didn't consider accuracy. We

**[10:15]** Crazy. We didn't consider accuracy. We didn't consider either accuracy or

**[10:16]** didn't consider either accuracy or

**[10:16]** didn't consider either accuracy or comprehensiveness. Our assumption here

**[10:19]** comprehensiveness. Our assumption here

**[10:19]** comprehensiveness. Our assumption here was that most of the vendors that are

**[10:20]** was that most of the vendors that are

**[10:20]** was that most of the vendors that are leaders in the market are going to be

**[10:22]** leaders in the market are going to be

**[10:22]** leaders in the market are going to be within a reasonable band of accuracy and

**[10:24]** within a reasonable band of accuracy and

**[10:24]** within a reasonable band of accuracy and comprehensiveness. And accuracy would

**[10:26]** comprehensiveness. And accuracy would

**[10:26]** comprehensiveness. And accuracy would refer to whether or not the extracted

**[10:28]** refer to whether or not the extracted

**[10:28]** refer to whether or not the extracted output is actually matches the the

**[10:30]** output is actually matches the the

**[10:30]** output is actually matches the the original resource. Comprehensiveness on

**[10:32]** original resource. Comprehensiveness on

**[10:32]** original resource. Comprehensiveness on the other hand is the amount of

**[10:34]** the other hand is the amount of

**[10:34]** the other hand is the amount of extracted information that is uh

**[10:36]** extracted information that is uh

**[10:36]** extracted information that is uh available um in the in the final output.

**[10:39]** available um in the in the final output.

**[10:39]** available um in the in the final output. The last thing that we didn't really

**[10:40]** The last thing that we didn't really

**[10:40]** The last thing that we didn't really consider was cost uh to be honest and

**[10:42]** consider was cost uh to be honest and

**[10:42]** consider was cost uh to be honest and this was because we were this system was

**[10:44]** this was because we were this system was

**[10:44]** this was because we were this system was pre-production. We didn't have real

**[10:46]** pre-production. We didn't have real

**[10:46]** pre-production. We didn't have real production data yet and we didn't know

**[10:48]** production data yet and we didn't know

**[10:48]** production data yet and we didn't know uh what our usage would be. And so we we

**[10:51]** uh what our usage would be. And so we we

**[10:51]** uh what our usage would be. And so we we figured what we would do is would come

**[10:52]** figured what we would do is would come

**[10:52]** figured what we would do is would come back and optimize cost once we had real

**[10:54]** back and optimize cost once we had real

**[10:54]** back and optimize cost once we had real usage data.

**[10:56]** usage data.

**[10:56]** usage data. So on to our final selections for

**[10:59]** So on to our final selections for

**[10:59]** So on to our final selections for documents and images. We chose to work


### [11:00 - 12:00]

**[11:01]** documents and images. We chose to work

**[11:01]** documents and images. We chose to work with llama parse which is a llama index

**[11:03]** with llama parse which is a llama index

**[11:03]** with llama parse which is a llama index product. Uh I think Jerry was up here

**[11:05]** product. Uh I think Jerry was up here

**[11:05]** product. Uh I think Jerry was up here earlier today. Uh and the reasons that

**[11:07]** earlier today. Uh and the reasons that

**[11:07]** earlier today. Uh and the reasons that we chose to work with llama parse was

**[11:09]** we chose to work with llama parse was

**[11:09]** we chose to work with llama parse was first it supported the most number of

**[11:11]** first it supported the most number of

**[11:11]** first it supported the most number of file types out of any document parsing

**[11:13]** file types out of any document parsing

**[11:13]** file types out of any document parsing solution we could find. And second their

**[11:15]** solution we could find. And second their

**[11:15]** solution we could find. And second their support was really great. Jerry and his

**[11:17]** support was really great. Jerry and his

**[11:17]** support was really great. Jerry and his team were were were were quick to get in

**[11:19]** team were were were were quick to get in

**[11:19]** team were were were were quick to get in a Slack channel with us. I think within

**[11:20]** a Slack channel with us. I think within

**[11:20]** a Slack channel with us. I think within just a couple of hours of us doing an

**[11:22]** just a couple of hours of us doing an

**[11:22]** just a couple of hours of us doing an initial evaluation.

**[11:25]** initial evaluation.

**[11:25]** initial evaluation. And with Llama Parse, we're able to turn

**[11:27]** And with Llama Parse, we're able to turn

**[11:27]** And with Llama Parse, we're able to turn documents like this PDF of a 11X sales

**[11:30]** documents like this PDF of a 11X sales

**[11:30]** documents like this PDF of a 11X sales deck into a markdown file like the one

**[11:32]** deck into a markdown file like the one

**[11:32]** deck into a markdown file like the one you see on the right.

**[11:34]** you see on the right.

**[11:34]** you see on the right. For websites, we chose to work with

**[11:35]** For websites, we chose to work with

**[11:36]** For websites, we chose to work with Firecrawl. The other main vendor that we

**[11:37]** Firecrawl. The other main vendor that we

**[11:37]** Firecrawl. The other main vendor that we were considering was Tavi. And this is

**[11:39]** were considering was Tavi. And this is

**[11:39]** were considering was Tavi. And this is actually not really a a major knock on

**[11:41]** actually not really a a major knock on

**[11:41]** actually not really a a major knock on Tavi. For Firecrawl, we chose to work

**[11:43]** Tavi. For Firecrawl, we chose to work

**[11:43]** Tavi. For Firecrawl, we chose to work with them because first we were

**[11:44]** with them because first we were

**[11:44]** with them because first we were familiar. we had already worked with

**[11:45]** familiar. we had already worked with

**[11:45]** familiar. we had already worked with them on a previous project. And

**[11:47]** them on a previous project. And

**[11:47]** them on a previous project. And secondly, Taval's crawl endpoint, which

**[11:49]** secondly, Taval's crawl endpoint, which

**[11:50]** secondly, Taval's crawl endpoint, which is the endpoint that we would have

**[11:51]** is the endpoint that we would have

**[11:51]** is the endpoint that we would have needed for this project, was still in

**[11:53]** needed for this project, was still in

**[11:53]** needed for this project, was still in development at the time. So, it wasn't

**[11:54]** development at the time. So, it wasn't

**[11:54]** development at the time. So, it wasn't something we could actually use.

**[11:57]** something we could actually use.

**[11:57]** something we could actually use. And similar to uh llama parse with t

**[11:59]** And similar to uh llama parse with t

**[11:59]** And similar to uh llama parse with t with fire crawl, we are able to take a


### [12:00 - 13:00]

**[12:01]** with fire crawl, we are able to take a

**[12:01]** with fire crawl, we are able to take a website like this homepage that you see

**[12:03]** website like this homepage that you see

**[12:03]** website like this homepage that you see here and turn it into another markdown

**[12:05]** here and turn it into another markdown

**[12:05]** here and turn it into another markdown document.

**[12:07]** document.

**[12:07]** document. Then we have audio and video. And for

**[12:08]** Then we have audio and video. And for

**[12:08]** Then we have audio and video. And for audio and video, we chose to work with a

**[12:10]** audio and video, we chose to work with a

**[12:10]** audio and video, we chose to work with a newer uh upstart vendor called

**[12:12]** newer uh upstart vendor called

**[12:12]** newer uh upstart vendor called Cloudglue.

**[12:13]** Cloudglue.

**[12:13]** Cloudglue. And the reasons that we chose to work

**[12:15]** And the reasons that we chose to work

**[12:15]** And the reasons that we chose to work with Cloud Glue were first they

**[12:16]** with Cloud Glue were first they

**[12:16]** with Cloud Glue were first they supported both audio and video, not just

**[12:18]** supported both audio and video, not just

**[12:18]** supported both audio and video, not just audio. And second, they were actually

**[12:21]** audio. And second, they were actually

**[12:21]** audio. And second, they were actually capable of extracting information from

**[12:23]** capable of extracting information from

**[12:23]** capable of extracting information from the video itself as opposed to just

**[12:25]** the video itself as opposed to just

**[12:25]** the video itself as opposed to just transcribing the video and giving us

**[12:27]** transcribing the video and giving us

**[12:27]** transcribing the video and giving us back a markdown file that contains the

**[12:29]** back a markdown file that contains the

**[12:29]** back a markdown file that contains the transcript of the audio.

**[12:32]** transcript of the audio.

**[12:32]** transcript of the audio. And so with Cloud Glue, we're able to

**[12:33]** And so with Cloud Glue, we're able to

**[12:34]** And so with Cloud Glue, we're able to turn uh YouTube videos and MP4 files and

**[12:36]** turn uh YouTube videos and MP4 files and

**[12:36]** turn uh YouTube videos and MP4 files and other video formats into markdown like

**[12:37]** other video formats into markdown like

**[12:37]** other video formats into markdown like you see on the right. So now that

**[12:40]** you see on the right. So now that

**[12:40]** you see on the right. So now that everything is marked down, we move on to

**[12:41]** everything is marked down, we move on to

**[12:41]** everything is marked down, we move on to the next step, which is chunking. All

**[12:43]** the next step, which is chunking. All

**[12:43]** the next step, which is chunking. All right, markdown. Let's go. Now,

**[12:46]** right, markdown. Let's go. Now,

**[12:46]** right, markdown. Let's go. Now, basically, we have a blob of markdown,

**[12:48]** basically, we have a blob of markdown,

**[12:48]** basically, we have a blob of markdown, right? And we want to kind of break it

**[12:50]** right? And we want to kind of break it

**[12:50]** right? And we want to kind of break it down into like semantic entities that we

**[12:53]** down into like semantic entities that we

**[12:53]** down into like semantic entities that we can embed and put it in our vector DB.

**[12:56]** can embed and put it in our vector DB.

**[12:56]** can embed and put it in our vector DB. At the same time, we want to uh protect

**[12:59]** At the same time, we want to uh protect

**[12:59]** At the same time, we want to uh protect the structure of the markdown because it


### [13:00 - 14:00]

**[13:01]** the structure of the markdown because it

**[13:01]** the structure of the markdown because it contains some meaning inherently like

**[13:03]** contains some meaning inherently like

**[13:03]** contains some meaning inherently like something's a title versus something's a

**[13:04]** something's a title versus something's a

**[13:04]** something's a title versus something's a paragraph. There is inherent meaning

**[13:06]** paragraph. There is inherent meaning

**[13:06]** paragraph. There is inherent meaning behind that. Um, so we're splitting

**[13:09]** behind that. Um, so we're splitting

**[13:09]** behind that. Um, so we're splitting these long blobs of text like 10-page

**[13:12]** these long blobs of text like 10-page

**[13:12]** these long blobs of text like 10-page documents into chunks that we can

**[13:14]** documents into chunks that we can

**[13:14]** documents into chunks that we can eventually retrieve uh after we've

**[13:15]** eventually retrieve uh after we've

**[13:16]** eventually retrieve uh after we've embedded and stored them in a vector DB,

**[13:17]** embedded and stored them in a vector DB,

**[13:17]** embedded and stored them in a vector DB, right? And now basically we can like

**[13:21]** right? And now basically we can like

**[13:21]** right? And now basically we can like take all of this and we're thinking

**[13:23]** take all of this and we're thinking

**[13:23]** take all of this and we're thinking about how we can you know split a long

**[13:27]** about how we can you know split a long

**[13:27]** about how we can you know split a long document into chunks, right? So chunking

**[13:29]** document into chunks, right? So chunking

**[13:29]** document into chunks, right? So chunking strategies um you have various things

**[13:32]** strategies um you have various things

**[13:32]** strategies um you have various things that you can do. You can split on

**[13:33]** that you can do. You can split on

**[13:33]** that you can do. You can split on tokens, you can split on sentences, you

**[13:35]** tokens, you can split on sentences, you

**[13:36]** tokens, you can split on sentences, you can also split on markdown headers,

**[13:37]** can also split on markdown headers,

**[13:37]** can also split on markdown headers, right? And then you can do like LLM

**[13:40]** right? And then you can do like LLM

**[13:40]** right? And then you can do like LLM calls and have an LLM split your

**[13:43]** calls and have an LLM split your

**[13:43]** calls and have an LLM split your document into chunks, you know, or any

**[13:45]** document into chunks, you know, or any

**[13:45]** document into chunks, you know, or any combination of the above. Um, now what

**[13:47]** combination of the above. Um, now what

**[13:47]** combination of the above. Um, now what you want to ask yourself when you're

**[13:48]** you want to ask yourself when you're

**[13:48]** you want to ask yourself when you're deciding on a chunking strategy is like

**[13:50]** deciding on a chunking strategy is like

**[13:50]** deciding on a chunking strategy is like um what kind of logical units am I

**[13:53]** um what kind of logical units am I

**[13:53]** um what kind of logical units am I trying to preserve in my data, right?

**[13:55]** trying to preserve in my data, right?

**[13:55]** trying to preserve in my data, right? What do I eventually want to extract

**[13:57]** What do I eventually want to extract

**[13:57]** What do I eventually want to extract during my retrieval, right? what

**[13:59]** during my retrieval, right? what

**[13:59]** during my retrieval, right? what strategy will keep them intact and at


### [14:00 - 15:00]

**[14:01]** strategy will keep them intact and at

**[14:01]** strategy will keep them intact and at the same time you're able to

**[14:02]** the same time you're able to

**[14:02]** the same time you're able to successfully embed them and store them

**[14:04]** successfully embed them and store them

**[14:04]** successfully embed them and store them in whatever DB you want. Um so and then

**[14:08]** in whatever DB you want. Um so and then

**[14:08]** in whatever DB you want. Um so and then should I try a different strategy for

**[14:10]** should I try a different strategy for

**[14:10]** should I try a different strategy for different resource types we have like we

**[14:11]** different resource types we have like we

**[14:11]** different resource types we have like we have to deal with PDFs, powerpoints,

**[14:13]** have to deal with PDFs, powerpoints,

**[14:13]** have to deal with PDFs, powerpoints, videos, right? Um and then eventually

**[14:16]** videos, right? Um and then eventually

**[14:16]** videos, right? Um and then eventually what kinds of queries or retrieval

**[14:17]** what kinds of queries or retrieval

**[14:18]** what kinds of queries or retrieval strategies am I expecting? Um and then

**[14:21]** strategies am I expecting? Um and then

**[14:21]** strategies am I expecting? Um and then we ended up with like a combination of

**[14:24]** we ended up with like a combination of

**[14:24]** we ended up with like a combination of all the three like all the things that

**[14:25]** all the three like all the things that

**[14:25]** all the three like all the things that we mentioned. So we split on markdown

**[14:28]** we mentioned. So we split on markdown

**[14:28]** we mentioned. So we split on markdown headers and then we kind of a waterfall.

**[14:30]** headers and then we kind of a waterfall.

**[14:30]** headers and then we kind of a waterfall. So because we want our like records in

**[14:33]** So because we want our like records in

**[14:33]** So because we want our like records in our vector DB to be a certain token

**[14:35]** our vector DB to be a certain token

**[14:35]** our vector DB to be a certain token count. So we split our markdown headers

**[14:37]** count. So we split our markdown headers

**[14:37]** count. So we split our markdown headers and then we split on sentences and then

**[14:39]** and then we split on sentences and then

**[14:39]** and then we split on sentences and then eventually we split on tokens and then

**[14:41]** eventually we split on tokens and then

**[14:41]** eventually we split on tokens and then yeah it's like worked well for us for

**[14:44]** yeah it's like worked well for us for

**[14:44]** yeah it's like worked well for us for all types of documents. Um and it has

**[14:46]** all types of documents. Um and it has

**[14:46]** all types of documents. Um and it has successfully preserved our markdown

**[14:48]** successfully preserved our markdown

**[14:48]** successfully preserved our markdown chunks that we can kind of cleanly show

**[14:49]** chunks that we can kind of cleanly show

**[14:49]** chunks that we can kind of cleanly show in the UI. Um, and it also prevents

**[14:52]** in the UI. Um, and it also prevents

**[14:52]** in the UI. Um, and it also prevents super long chunks which are, you know,

**[14:54]** super long chunks which are, you know,

**[14:54]** super long chunks which are, you know, diluting the meaning behind your

**[14:55]** diluting the meaning behind your

**[14:55]** diluting the meaning behind your document if you end up with that. Okay,

**[14:58]** document if you end up with that. Okay,

**[14:58]** document if you end up with that. Okay, so we have split all of our markdown


### [15:00 - 16:00]

**[15:00]** so we have split all of our markdown

**[15:00]** so we have split all of our markdown into individual chunks. It's now time to

**[15:02]** into individual chunks. It's now time to

**[15:02]** into individual chunks. It's now time to put those chunks somewhere. We're going

**[15:03]** put those chunks somewhere. We're going

**[15:03]** put those chunks somewhere. We're going to store them. Let's talk about storage

**[15:05]** to store them. Let's talk about storage

**[15:05]** to store them. Let's talk about storage technologies.

**[15:06]** technologies.

**[15:06]** technologies. So for storage technologies, I'm sure

**[15:08]** So for storage technologies, I'm sure

**[15:08]** So for storage technologies, I'm sure everyone is like here for the rag

**[15:09]** everyone is like here for the rag

**[15:09]** everyone is like here for the rag section. So they think that we're using

**[15:11]** section. So they think that we're using

**[15:11]** section. So they think that we're using a vector database. We actually are using

**[15:12]** a vector database. We actually are using

**[15:12]** a vector database. We actually are using a vector database. But to be pedantic,

**[15:15]** a vector database. But to be pedantic,

**[15:15]** a vector database. But to be pedantic, rag is retrieval augmented generation.

**[15:17]** rag is retrieval augmented generation.

**[15:17]** rag is retrieval augmented generation. So we all know that uh anytime you're

**[15:19]** So we all know that uh anytime you're

**[15:19]** So we all know that uh anytime you're retrieving context from an external

**[15:21]** retrieving context from an external

**[15:21]** retrieving context from an external source whether it's a graph database or

**[15:23]** source whether it's a graph database or

**[15:23]** source whether it's a graph database or elastic search or uh a file in the file

**[15:26]** elastic search or uh a file in the file

**[15:26]** elastic search or uh a file in the file system that also qualifies as rag. Um

**[15:29]** system that also qualifies as rag. Um

**[15:29]** system that also qualifies as rag. Um some of the other options you can use

**[15:31]** some of the other options you can use

**[15:31]** some of the other options you can use for rag uh I just mentioned a graph

**[15:33]** for rag uh I just mentioned a graph

**[15:33]** for rag uh I just mentioned a graph database document databases uh

**[15:35]** database document databases uh

**[15:35]** database document databases uh relational databases key value stores

**[15:38]** relational databases key value stores

**[15:38]** relational databases key value stores you could even use object storage like

**[15:40]** you could even use object storage like

**[15:40]** you could even use object storage like S3. In our case, we did use a vector

**[15:43]** S3. In our case, we did use a vector

**[15:43]** S3. In our case, we did use a vector database and that's because we wanted to

**[15:45]** database and that's because we wanted to

**[15:45]** database and that's because we wanted to do sim similarity search which is what

**[15:47]** do sim similarity search which is what

**[15:47]** do sim similarity search which is what vector databases are are built for and

**[15:49]** vector databases are are built for and

**[15:49]** vector databases are are built for and optimized for.

**[15:51]** optimized for.

**[15:51]** optimized for. Once again, we had a lot of options to

**[15:53]** Once again, we had a lot of options to

**[15:54]** Once again, we had a lot of options to choose from. This is uh not a complete

**[15:56]** choose from. This is uh not a complete

**[15:56]** choose from. This is uh not a complete or an exhaustive list.

**[15:58]** or an exhaustive list.

**[15:58]** or an exhaustive list. In the end, we chose to work with a


### [16:00 - 17:00]

**[16:00]** In the end, we chose to work with a

**[16:00]** In the end, we chose to work with a company called Pine Cone. And the reason

**[16:02]** company called Pine Cone. And the reason

**[16:02]** company called Pine Cone. And the reason that we chose to work with Pine Cone was

**[16:03]** that we chose to work with Pine Cone was

**[16:03]** that we chose to work with Pine Cone was first it was a well-known solution. We

**[16:05]** first it was a well-known solution. We

**[16:05]** first it was a well-known solution. We were kind of new to the space and we

**[16:07]** were kind of new to the space and we

**[16:07]** were kind of new to the space and we thought probably can't go wrong going

**[16:09]** thought probably can't go wrong going

**[16:09]** thought probably can't go wrong going with the market leader. It was cloud

**[16:11]** with the market leader. It was cloud

**[16:11]** with the market leader. It was cloud hosted so our team wouldn't have to spin

**[16:14]** hosted so our team wouldn't have to spin

**[16:14]** hosted so our team wouldn't have to spin up any additional infrastructure.

**[16:16]** up any additional infrastructure.

**[16:16]** up any additional infrastructure. It was really easy to get started. They

**[16:17]** It was really easy to get started. They

**[16:17]** It was really easy to get started. They had great getting started guides and

**[16:19]** had great getting started guides and

**[16:19]** had great getting started guides and SDKs.

**[16:20]** SDKs.

**[16:20]** SDKs. Uh they had embedding models bundled

**[16:22]** Uh they had embedding models bundled

**[16:22]** Uh they had embedding models bundled with the solution. So for a vector

**[16:24]** with the solution. So for a vector

**[16:24]** with the solution. So for a vector database typically you have to embed the

**[16:26]** database typically you have to embed the

**[16:26]** database typically you have to embed the information before it goes into the

**[16:27]** information before it goes into the

**[16:27]** information before it goes into the database. Uh that would require the use

**[16:29]** database. Uh that would require the use

**[16:29]** database. Uh that would require the use of a third party or an external vector

**[16:31]** of a third party or an external vector

**[16:31]** of a third party or an external vector vector excuse me embedding model. And uh

**[16:34]** vector excuse me embedding model. And uh

**[16:34]** vector excuse me embedding model. And uh with Pine Cone, we didn't actually have

**[16:35]** with Pine Cone, we didn't actually have

**[16:35]** with Pine Cone, we didn't actually have to go find another embedding model

**[16:37]** to go find another embedding model

**[16:37]** to go find another embedding model provider or host our own embedding

**[16:38]** provider or host our own embedding

**[16:38]** provider or host our own embedding model. We just used the one that they

**[16:40]** model. We just used the one that they

**[16:40]** model. We just used the one that they provide. And last but not least, their

**[16:42]** provide. And last but not least, their

**[16:42]** provide. And last but not least, their customer support was awesome. They got

**[16:44]** customer support was awesome. They got

**[16:44]** customer support was awesome. They got on a lot of calls with us, helped us

**[16:45]** on a lot of calls with us, helped us

**[16:45]** on a lot of calls with us, helped us analyze different vector data database

**[16:47]** analyze different vector data database

**[16:48]** analyze different vector data database options and think through a graph

**[16:49]** options and think through a graph

**[16:49]** options and think through a graph databases and graph rag whether that

**[16:51]** databases and graph rag whether that

**[16:51]** databases and graph rag whether that made sense for us.

**[16:54]** made sense for us.

**[16:54]** made sense for us. So retrieval, the rag part of the rag

**[16:57]** So retrieval, the rag part of the rag

**[16:57]** So retrieval, the rag part of the rag workflow that we just built, right? Um

**[16:59]** workflow that we just built, right? Um

**[16:59]** workflow that we just built, right? Um you'll see that there's actually an


### [17:00 - 18:00]

**[17:01]** you'll see that there's actually an

**[17:01]** you'll see that there's actually an evolution of different rag techniques

**[17:02]** evolution of different rag techniques

**[17:02]** evolution of different rag techniques over the last year. We started off with

**[17:04]** over the last year. We started off with

**[17:04]** over the last year. We started off with just traditional rag which is kind of a

**[17:06]** just traditional rag which is kind of a

**[17:06]** just traditional rag which is kind of a play on you're pulling information and

**[17:08]** play on you're pulling information and

**[17:08]** play on you're pulling information and then enriching your system prompt for an

**[17:11]** then enriching your system prompt for an

**[17:11]** then enriching your system prompt for an LLM API call right and then eventually

**[17:13]** LLM API call right and then eventually

**[17:13]** LLM API call right and then eventually that turned into an agentic rag form

**[17:15]** that turned into an agentic rag form

**[17:15]** that turned into an agentic rag form where now you have all these tools for

**[17:18]** where now you have all these tools for

**[17:18]** where now you have all these tools for getting information retrieval and then

**[17:20]** getting information retrieval and then

**[17:20]** getting information retrieval and then you attach those tools to whatever

**[17:23]** you attach those tools to whatever

**[17:23]** you attach those tools to whatever agentic flow that you have and then it

**[17:25]** agentic flow that you have and then it

**[17:25]** agentic flow that you have and then it calls the tool as a part of its larger

**[17:28]** calls the tool as a part of its larger

**[17:28]** calls the tool as a part of its larger flow. Right now something we we're

**[17:30]** flow. Right now something we we're

**[17:30]** flow. Right now something we we're seeing emerge in the last couple of

**[17:32]** seeing emerge in the last couple of

**[17:32]** seeing emerge in the last couple of months is deep research rack where now

**[17:34]** months is deep research rack where now

**[17:34]** months is deep research rack where now you have these deep research agents

**[17:36]** you have these deep research agents

**[17:36]** you have these deep research agents which are coming up with a plan and then

**[17:38]** which are coming up with a plan and then

**[17:38]** which are coming up with a plan and then they execute them and the plan may

**[17:40]** they execute them and the plan may

**[17:40]** they execute them and the plan may contain one or many steps of retrieval.

**[17:42]** contain one or many steps of retrieval.

**[17:42]** contain one or many steps of retrieval. Right? These deep research agents can go

**[17:45]** Right? These deep research agents can go

**[17:45]** Right? These deep research agents can go broad or deep depending on the context

**[17:47]** broad or deep depending on the context

**[17:47]** broad or deep depending on the context needs and they can evaluate whether or

**[17:49]** needs and they can evaluate whether or

**[17:49]** needs and they can evaluate whether or not they want to do more retrieval. Um

**[17:51]** not they want to do more retrieval. Um

**[17:51]** not they want to do more retrieval. Um we ended up building a deep research

**[17:53]** we ended up building a deep research

**[17:53]** we ended up building a deep research agent. Um we actually used a company

**[17:55]** agent. Um we actually used a company

**[17:55]** agent. Um we actually used a company called Leta. Leta is a cloud agent

**[17:58]** called Leta. Leta is a cloud agent

**[17:58]** called Leta. Leta is a cloud agent provider and they're really easy to


### [18:00 - 19:00]

**[18:00]** provider and they're really easy to

**[18:00]** provider and they're really easy to build with. Um how it works basically we

**[18:04]** build with. Um how it works basically we

**[18:04]** build with. Um how it works basically we pass in the lead information to our

**[18:06]** pass in the lead information to our

**[18:06]** pass in the lead information to our agent and then it basically comes up

**[18:08]** agent and then it basically comes up

**[18:08]** agent and then it basically comes up with a plan. plan contains one or many

**[18:10]** with a plan. plan contains one or many

**[18:10]** with a plan. plan contains one or many context retrieval steps and then

**[18:13]** context retrieval steps and then

**[18:13]** context retrieval steps and then eventually you know does the tool call

**[18:16]** eventually you know does the tool call

**[18:16]** eventually you know does the tool call summarizes the results and then

**[18:18]** summarizes the results and then

**[18:18]** summarizes the results and then generates an answer for us in a nice

**[18:21]** generates an answer for us in a nice

**[18:21]** generates an answer for us in a nice clean Q&A manner right and then this is

**[18:24]** clean Q&A manner right and then this is

**[18:24]** clean Q&A manner right and then this is kind of how it looks like for a system

**[18:26]** kind of how it looks like for a system

**[18:26]** kind of how it looks like for a system with two questions that we ask

**[18:29]** with two questions that we ask

**[18:29]** with two questions that we ask um now on to visualization the most uh

**[18:32]** um now on to visualization the most uh

**[18:32]** um now on to visualization the most uh mysterious part of the pipeline so what

**[18:34]** mysterious part of the pipeline so what

**[18:34]** mysterious part of the pipeline so what does visualization have to do with a a

**[18:36]** does visualization have to do with a a

**[18:36]** does visualization have to do with a a rag or ETL pipeline Um, for more

**[18:39]** rag or ETL pipeline Um, for more

**[18:39]** rag or ETL pipeline Um, for more context, our customers are trusting

**[18:42]** context, our customers are trusting

**[18:42]** context, our customers are trusting Alice to represent their business. They

**[18:44]** Alice to represent their business. They

**[18:44]** Alice to represent their business. They really want to know that Alice knows her

**[18:46]** really want to know that Alice knows her

**[18:46]** really want to know that Alice knows her stuff, that she actually knows the

**[18:47]** stuff, that she actually knows the

**[18:47]** stuff, that she actually knows the products that they sell, and she's not

**[18:48]** products that they sell, and she's not

**[18:48]** products that they sell, and she's not going to lie about case studies or

**[18:49]** going to lie about case studies or

**[18:49]** going to lie about case studies or testimonials or make things up about the

**[18:51]** testimonials or make things up about the

**[18:52]** testimonials or make things up about the pain points that they address. So, how

**[18:53]** pain points that they address. So, how

**[18:53]** pain points that they address. So, how can we reassure them? In our case, we

**[18:56]** can we reassure them? In our case, we

**[18:56]** can we reassure them? In our case, we came up with a solution, which is to let

**[18:58]** came up with a solution, which is to let

**[18:58]** came up with a solution, which is to let al let users peek into Alice's brain.


### [19:00 - 20:00]

**[19:01]** al let users peek into Alice's brain.

**[19:01]** al let users peek into Alice's brain. Get ready.

**[19:03]** Get ready.

**[19:03]** Get ready. This is what that looks like.

**[19:05]** This is what that looks like.

**[19:05]** This is what that looks like. We have a a interactive 3D visualization

**[19:07]** We have a a interactive 3D visualization

**[19:08]** We have a a interactive 3D visualization of the knowledge base available in the

**[19:09]** of the knowledge base available in the

**[19:09]** of the knowledge base available in the product. What we've done here is taken

**[19:11]** product. What we've done here is taken

**[19:11]** product. What we've done here is taken all of the vectors vectors from our uh

**[19:13]** all of the vectors vectors from our uh

**[19:14]** all of the vectors vectors from our uh pine cone vector database and uh

**[19:16]** pine cone vector database and uh

**[19:16]** pine cone vector database and uh collapsed or actually excuse me I think

**[19:17]** collapsed or actually excuse me I think

**[19:18]** collapsed or actually excuse me I think the correct term is projected them down

**[19:19]** the correct term is projected them down

**[19:19]** the correct term is projected them down to just three dimensions. So we're going

**[19:21]** to just three dimensions. So we're going

**[19:21]** to just three dimensions. So we're going to render them as nodes in

**[19:22]** to render them as nodes in

**[19:22]** to render them as nodes in threedimensional space um um um with

**[19:25]** threedimensional space um um um with

**[19:25]** threedimensional space um um um with using um uh and once the nodes are

**[19:29]** using um uh and once the nodes are

**[19:29]** using um uh and once the nodes are visible in this space you can click on

**[19:31]** visible in this space you can click on

**[19:31]** visible in this space you can click on any given node to view the associated

**[19:33]** any given node to view the associated

**[19:33]** any given node to view the associated chunk. This is one of the ways that uh

**[19:35]** chunk. This is one of the ways that uh

**[19:35]** chunk. This is one of the ways that uh for example our sales team or support

**[19:36]** for example our sales team or support

**[19:36]** for example our sales team or support team will demonstrate Alice's knowledge.

**[19:39]** team will demonstrate Alice's knowledge.

**[19:40]** team will demonstrate Alice's knowledge. Now how does it look like in the actual

**[19:41]** Now how does it look like in the actual

**[19:41]** Now how does it look like in the actual UI? Right? Basically you start off with

**[19:43]** UI? Right? Basically you start off with

**[19:43]** UI? Right? Basically you start off with this nice little modal you know you drop

**[19:45]** this nice little modal you know you drop

**[19:46]** this nice little modal you know you drop in your URLs, your web pages, your

**[19:47]** in your URLs, your web pages, your

**[19:48]** in your URLs, your web pages, your documents, your videos and then you

**[19:49]** documents, your videos and then you

**[19:50]** documents, your videos and then you click learn and then it kind of shows up

**[19:51]** click learn and then it kind of shows up

**[19:51]** click learn and then it kind of shows up nicely in the UI. Um you have all the

**[19:54]** nicely in the UI. Um you have all the

**[19:54]** nicely in the UI. Um you have all the resources there and then you have the

**[19:56]** resources there and then you have the

**[19:56]** resources there and then you have the ability to interrogate Alice about what

**[19:58]** ability to interrogate Alice about what

**[19:58]** ability to interrogate Alice about what she knows of your knowledge base. Right?


### [20:00 - 21:00]

**[20:00]** she knows of your knowledge base. Right?

**[20:00]** she knows of your knowledge base. Right? It's a really nice agent that we built

**[20:02]** It's a really nice agent that we built

**[20:02]** It's a really nice agent that we built again using Leta. And here's how it

**[20:05]** again using Leta. And here's how it

**[20:05]** again using Leta. And here's how it looks like in the campaign creation

**[20:07]** looks like in the campaign creation

**[20:07]** looks like in the campaign creation flow. You see that on the left hand side

**[20:09]** flow. You see that on the left hand side

**[20:09]** flow. You see that on the left hand side we have the knowledgebased content

**[20:11]** we have the knowledgebased content

**[20:11]** we have the knowledgebased content showing up as a nice Q&A where you can

**[20:13]** showing up as a nice Q&A where you can

**[20:14]** showing up as a nice Q&A where you can click on the questions and it shows you

**[20:15]** click on the questions and it shows you

**[20:15]** click on the questions and it shows you a drop down of the chunks that we

**[20:16]** a drop down of the chunks that we

**[20:16]** a drop down of the chunks that we retrieved and these were used as a part

**[20:18]** retrieved and these were used as a part

**[20:18]** retrieved and these were used as a part of the messaging flow.

**[20:21]** of the messaging flow.

**[20:21]** of the messaging flow. So now with that we have achieved our

**[20:23]** So now with that we have achieved our

**[20:23]** So now with that we have achieved our goal. Our agent is closer to a human

**[20:25]** goal. Our agent is closer to a human

**[20:25]** goal. Our agent is closer to a human than being an email. Right? We are now

**[20:30]** than being an email. Right? We are now

**[20:30]** than being an email. Right? We are now we are now basically uh emulating how

**[20:33]** we are now basically uh emulating how

**[20:33]** we are now basically uh emulating how you onboard a human SDR. You dump in a

**[20:35]** you onboard a human SDR. You dump in a

**[20:35]** you onboard a human SDR. You dump in a bunch of context and they just know.

**[20:38]** bunch of context and they just know.

**[20:38]** bunch of context and they just know. So in conclusion, the knowledge base was

**[20:39]** So in conclusion, the knowledge base was

**[20:40]** So in conclusion, the knowledge base was a pretty revolutionary project for our

**[20:42]** a pretty revolutionary project for our

**[20:42]** a pretty revolutionary project for our product and really changed the user

**[20:43]** product and really changed the user

**[20:43]** product and really changed the user experience and also leveled up our team

**[20:45]** experience and also leveled up our team

**[20:45]** experience and also leveled up our team a lot. Uh we learned a lot of lessons.

**[20:48]** a lot. Uh we learned a lot of lessons.

**[20:48]** a lot. Uh we learned a lot of lessons. It was hard to create this slide, but

**[20:49]** It was hard to create this slide, but

**[20:50]** It was hard to create this slide, but there are just three that I want to

**[20:50]** there are just three that I want to

**[20:50]** there are just three that I want to highlight for you today. The first was

**[20:53]** highlight for you today. The first was

**[20:53]** highlight for you today. The first was that rag is complex. It was a lot harder

**[20:55]** that rag is complex. It was a lot harder

**[20:55]** that rag is complex. It was a lot harder than we thought it was going to be.

**[20:57]** than we thought it was going to be.

**[20:57]** than we thought it was going to be. There were a lot of micro decisions made

**[20:58]** There were a lot of micro decisions made

**[20:58]** There were a lot of micro decisions made along the way, a lot of different


### [21:00 - 22:00]

**[21:00]** along the way, a lot of different

**[21:00]** along the way, a lot of different technologies we had to evaluate.

**[21:02]** technologies we had to evaluate.

**[21:02]** technologies we had to evaluate. Supporting different research types was

**[21:03]** Supporting different research types was

**[21:03]** Supporting different research types was hard. Hopefully, you all have a better

**[21:05]** hard. Hopefully, you all have a better

**[21:05]** hard. Hopefully, you all have a better appreciation of how complicated RAD can

**[21:07]** appreciation of how complicated RAD can

**[21:07]** appreciation of how complicated RAD can be.

**[21:08]** be.

**[21:08]** be. The second lesson was that you should

**[21:10]** The second lesson was that you should

**[21:10]** The second lesson was that you should first get to production before

**[21:12]** first get to production before

**[21:12]** first get to production before benchmarking and then you can improve.

**[21:14]** benchmarking and then you can improve.

**[21:14]** benchmarking and then you can improve. And the idea here is that with all of

**[21:16]** And the idea here is that with all of

**[21:16]** And the idea here is that with all of those decisions and vendors to evaluate,

**[21:18]** those decisions and vendors to evaluate,

**[21:18]** those decisions and vendors to evaluate, uh, it can be hard to get started. So we

**[21:20]** uh, it can be hard to get started. So we

**[21:20]** uh, it can be hard to get started. So we recommend just getting something in

**[21:21]** recommend just getting something in

**[21:21]** recommend just getting something in production that satisfies the product

**[21:23]** production that satisfies the product

**[21:23]** production that satisfies the product requirements and then establishing some

**[21:24]** requirements and then establishing some

**[21:24]** requirements and then establishing some real benchmarks which you can use to

**[21:26]** real benchmarks which you can use to

**[21:26]** real benchmarks which you can use to iterate and improve. And the last

**[21:29]** iterate and improve. And the last

**[21:29]** iterate and improve. And the last learning here was that you should lean

**[21:30]** learning here was that you should lean

**[21:30]** learning here was that you should lean on vendors. You guys are all going to be

**[21:32]** on vendors. You guys are all going to be

**[21:32]** on vendors. You guys are all going to be buying solutions and they're going to be

**[21:34]** buying solutions and they're going to be

**[21:34]** buying solutions and they're going to be fighting for your business. Make them

**[21:35]** fighting for your business. Make them

**[21:35]** fighting for your business. Make them work for it. Make them teach you about

**[21:37]** work for it. Make them teach you about

**[21:37]** work for it. Make them teach you about the different uh the different offerings

**[21:39]** the different uh the different offerings

**[21:39]** the different uh the different offerings and why their solution is better. And so

**[21:42]** and why their solution is better. And so

**[21:42]** and why their solution is better. And so our future plans are to first track and

**[21:44]** our future plans are to first track and

**[21:44]** our future plans are to first track and address hallucinations in our emails.

**[21:47]** address hallucinations in our emails.

**[21:47]** address hallucinations in our emails. Evaluate parsing vendors on accuracy and

**[21:49]** Evaluate parsing vendors on accuracy and

**[21:49]** Evaluate parsing vendors on accuracy and completeness, those metrics that we uh

**[21:51]** completeness, those metrics that we uh

**[21:51]** completeness, those metrics that we uh identified earlier. Experiment with

**[21:53]** identified earlier. Experiment with

**[21:53]** identified earlier. Experiment with hybrid rag, the introduction of a graph

**[21:55]** hybrid rag, the introduction of a graph

**[21:55]** hybrid rag, the introduction of a graph database alongside our vector database.

**[21:58]** database alongside our vector database.

**[21:58]** database alongside our vector database. And finally, to just focus on reducing


### [22:00 - 23:00]

**[22:00]** And finally, to just focus on reducing

**[22:00]** And finally, to just focus on reducing cost across our entire pipeline.

**[22:03]** cost across our entire pipeline.

**[22:03]** cost across our entire pipeline. And if any of this sounds interesting to

**[22:04]** And if any of this sounds interesting to

**[22:04]** And if any of this sounds interesting to you, we are hiring. So, please reach out

**[22:06]** you, we are hiring. So, please reach out

**[22:06]** you, we are hiring. So, please reach out to either Sautwick or myself. Join us.

**[22:09]** to either Sautwick or myself. Join us.

**[22:09]** to either Sautwick or myself. Join us. And uh thank you all for coming today.

**[22:12]** And uh thank you all for coming today.

**[22:12]** And uh thank you all for coming today. [Music]


