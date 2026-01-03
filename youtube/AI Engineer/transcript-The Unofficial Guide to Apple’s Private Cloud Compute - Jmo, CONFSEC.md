# The Unofficial Guide to Apple’s Private Cloud Compute - Jmo, CONFSEC

**Video URL:** https://www.youtube.com/watch?v=CCsWZ5bJlO8

---

## Full Transcript

### [00:00 - 01:00]

**[00:15]** So, we're going to talk about Apple's

**[00:15]** So, we're going to talk about Apple's private cloud compute. This is an

**[00:17]** private cloud compute. This is an

**[00:17]** private cloud compute. This is an unofficial guide. Uh, I don't work at

**[00:19]** unofficial guide. Uh, I don't work at

**[00:19]** unofficial guide. Uh, I don't work at Apple. We'll talk about it um in a sec.

**[00:22]** Apple. We'll talk about it um in a sec.

**[00:22]** Apple. We'll talk about it um in a sec. But, so um this is my background. My PhD

**[00:25]** But, so um this is my background. My PhD

**[00:25]** But, so um this is my background. My PhD in bio uh in data science, biomedical

**[00:27]** in bio uh in data science, biomedical

**[00:28]** in bio uh in data science, biomedical informatics. I've sold two companies.

**[00:29]** informatics. I've sold two companies.

**[00:29]** informatics. I've sold two companies. one in AI and uh data, one in cyber

**[00:31]** one in AI and uh data, one in cyber

**[00:31]** one in AI and uh data, one in cyber security and infrastructure. I'm not

**[00:33]** security and infrastructure. I'm not

**[00:33]** security and infrastructure. I'm not South Park Commons. I'm building a

**[00:34]** South Park Commons. I'm building a

**[00:34]** South Park Commons. I'm building a company called Confident Security, which

**[00:36]** company called Confident Security, which

**[00:36]** company called Confident Security, which we'll get to at the end. Um but again,

**[00:38]** we'll get to at the end. Um but again,

**[00:38]** we'll get to at the end. Um but again, disclaimer, put this I'm not an Apple

**[00:40]** disclaimer, put this I'm not an Apple

**[00:40]** disclaimer, put this I'm not an Apple employee. I'm not speaking on their

**[00:41]** employee. I'm not speaking on their

**[00:41]** employee. I'm not speaking on their behalf. Everything I've ganed is from

**[00:42]** behalf. Everything I've ganed is from

**[00:42]** behalf. Everything I've ganed is from public sources. And hopefully what we'll

**[00:45]** public sources. And hopefully what we'll

**[00:45]** public sources. And hopefully what we'll learn today is some tools that we can

**[00:46]** learn today is some tools that we can

**[00:46]** learn today is some tools that we can use ourselves. There's really six key

**[00:48]** use ourselves. There's really six key

**[00:48]** use ourselves. There's really six key components or and some approaches to

**[00:51]** components or and some approaches to

**[00:51]** components or and some approaches to ensure privacy. And privacy and security

**[00:52]** ensure privacy. And privacy and security

**[00:52]** ensure privacy. And privacy and security are very related, not perfectly

**[00:55]** are very related, not perfectly

**[00:55]** are very related, not perfectly overlapping, but related. So, um, before

**[00:57]** overlapping, but related. So, um, before

**[00:57]** overlapping, but related. So, um, before I get there, I know that we're in the

**[00:59]** I get there, I know that we're in the

**[00:59]** I get there, I know that we're in the security track, but I want to motivate


### [01:00 - 02:00]

**[01:00]** security track, but I want to motivate

**[01:00]** security track, but I want to motivate why you might care about privacy. Not

**[01:03]** why you might care about privacy. Not

**[01:03]** why you might care about privacy. Not everyone believes that you should have

**[01:04]** everyone believes that you should have

**[01:04]** everyone believes that you should have privacy. Uh, so let me just give some

**[01:07]** privacy. Uh, so let me just give some

**[01:07]** privacy. Uh, so let me just give some give some examples. This year, Deep Seek

**[01:10]** give some examples. This year, Deep Seek

**[01:10]** give some examples. This year, Deep Seek leaked 100 a million sensitive records

**[01:13]** leaked 100 a million sensitive records

**[01:13]** leaked 100 a million sensitive records of chat logs. And you might say to

**[01:15]** of chat logs. And you might say to

**[01:15]** of chat logs. And you might say to yourself like, well, that's DeepSeek.

**[01:17]** yourself like, well, that's DeepSeek.

**[01:17]** yourself like, well, that's DeepSeek. Everyone knew that was going to happen.

**[01:18]** Everyone knew that was going to happen.

**[01:18]** Everyone knew that was going to happen. Um, but uh before before I show you the

**[01:21]** Um, but uh before before I show you the

**[01:21]** Um, but uh before before I show you the next piece, I want to pull the audience.

**[01:23]** next piece, I want to pull the audience.

**[01:23]** next piece, I want to pull the audience. How many here care about privacy?

**[01:26]** How many here care about privacy?

**[01:26]** How many here care about privacy? All right. How many of us use chat GPT?

**[01:31]** All right. How many of us use chat GPT?

**[01:31]** All right. How many of us use chat GPT? All right. How many consider ChatGpt to

**[01:33]** All right. How many consider ChatGpt to

**[01:33]** All right. How many consider ChatGpt to be private? Okay, good. Um, how many use

**[01:37]** be private? Okay, good. Um, how many use

**[01:37]** be private? Okay, good. Um, how many use the ChatGpt private mode?

**[01:40]** the ChatGpt private mode?

**[01:40]** the ChatGpt private mode? Uh, and then how many use the API but

**[01:42]** Uh, and then how many use the API but

**[01:42]** Uh, and then how many use the API but with zero data retention? Kind of like

**[01:44]** with zero data retention? Kind of like

**[01:44]** with zero data retention? Kind of like the default state. Okay, great. Well, as

**[01:47]** the default state. Okay, great. Well, as

**[01:47]** the default state. Okay, great. Well, as of yesterday, uh, Open AAI has to retain

**[01:50]** of yesterday, uh, Open AAI has to retain

**[01:50]** of yesterday, uh, Open AAI has to retain everything uh, anyway, whether or not

**[01:52]** everything uh, anyway, whether or not

**[01:52]** everything uh, anyway, whether or not you flagged it as private or not. uh and

**[01:55]** you flagged it as private or not. uh and

**[01:55]** you flagged it as private or not. uh and I don't want to get into the comments of

**[01:56]** I don't want to get into the comments of

**[01:56]** I don't want to get into the comments of why they have to do that, but the point

**[01:58]** why they have to do that, but the point

**[01:58]** why they have to do that, but the point is is that uh they have the capability


### [02:00 - 03:00]

**[02:01]** is is that uh they have the capability

**[02:01]** is is that uh they have the capability of retaining your private chats that you

**[02:03]** of retaining your private chats that you

**[02:03]** of retaining your private chats that you can flag on the UI as not private other

**[02:05]** can flag on the UI as not private other

**[02:05]** can flag on the UI as not private other things. And uh obviously being forced to

**[02:08]** things. And uh obviously being forced to

**[02:08]** things. And uh obviously being forced to do that is not great, but this is why we

**[02:10]** do that is not great, but this is why we

**[02:10]** do that is not great, but this is why we should all care about privacy.

**[02:13]** should all care about privacy.

**[02:13]** should all care about privacy. So Apple doesn't want to have these

**[02:16]** So Apple doesn't want to have these

**[02:16]** So Apple doesn't want to have these headlines uh because they're one of

**[02:17]** headlines uh because they're one of

**[02:18]** headlines uh because they're one of their major value props is privacy. So

**[02:20]** their major value props is privacy. So

**[02:20]** their major value props is privacy. So let's talk a little bit about the

**[02:21]** let's talk a little bit about the

**[02:21]** let's talk a little bit about the problems that Apple solved and then how

**[02:23]** problems that Apple solved and then how

**[02:23]** problems that Apple solved and then how we might use it. So fundamentally AI

**[02:26]** we might use it. So fundamentally AI

**[02:26]** we might use it. So fundamentally AI requires more compute than a phone. Uh

**[02:28]** requires more compute than a phone. Uh

**[02:28]** requires more compute than a phone. Uh but every obviously they want to bundle

**[02:30]** but every obviously they want to bundle

**[02:30]** but every obviously they want to bundle AI into their phones. Privacy is a major

**[02:32]** AI into their phones. Privacy is a major

**[02:32]** AI into their phones. Privacy is a major selling point. Anytime you give up

**[02:34]** selling point. Anytime you give up

**[02:34]** selling point. Anytime you give up private data to something remote, you're

**[02:36]** private data to something remote, you're

**[02:36]** private data to something remote, you're inherently reducing your privacy, right?

**[02:38]** inherently reducing your privacy, right?

**[02:38]** inherently reducing your privacy, right? Anytime I give you my data, it's not as

**[02:40]** Anytime I give you my data, it's not as

**[02:40]** Anytime I give you my data, it's not as private as it was the second before. So

**[02:42]** private as it was the second before. So

**[02:42]** private as it was the second before. So the question that Apple is trying to

**[02:44]** the question that Apple is trying to

**[02:44]** the question that Apple is trying to answer in their PCC system which is now

**[02:47]** answer in their PCC system which is now

**[02:47]** answer in their PCC system which is now available on all of our iPhones and used

**[02:48]** available on all of our iPhones and used

**[02:48]** available on all of our iPhones and used for inference is how do you get remote

**[02:50]** for inference is how do you get remote

**[02:50]** for inference is how do you get remote compute while remaining private and the

**[02:52]** compute while remaining private and the

**[02:52]** compute while remaining private and the simple way to do that would be to buy

**[02:54]** simple way to do that would be to buy

**[02:54]** simple way to do that would be to buy all of the iPhones H100s pair them in

**[02:56]** all of the iPhones H100s pair them in

**[02:56]** all of the iPhones H100s pair them in the cloud you get your own H100 boom but

**[02:58]** the cloud you get your own H100 boom but

**[02:58]** the cloud you get your own H100 boom but obviously AI is even more expensive so


### [03:00 - 04:00]

**[03:01]** obviously AI is even more expensive so

**[03:01]** obviously AI is even more expensive so uh that's not going to work so they

**[03:03]** uh that's not going to work so they

**[03:03]** uh that's not going to work so they actually need some approach which is how

**[03:05]** actually need some approach which is how

**[03:05]** actually need some approach which is how do you get remote compute while

**[03:06]** do you get remote compute while

**[03:06]** do you get remote compute while remaining private and cheap uh otherwise

**[03:09]** remaining private and cheap uh otherwise

**[03:09]** remaining private and cheap uh otherwise it doesn't work so I'm going to kind of

**[03:11]** it doesn't work so I'm going to kind of

**[03:11]** it doesn't work so I'm going to kind of frame a problem this way. You've got an

**[03:13]** frame a problem this way. You've got an

**[03:13]** frame a problem this way. You've got an iPhone. You've got an untrusted remote

**[03:15]** iPhone. You've got an untrusted remote

**[03:15]** iPhone. You've got an untrusted remote server. You can't see inside of it. It's

**[03:17]** server. You can't see inside of it. It's

**[03:17]** server. You can't see inside of it. It's a black box. Once you give them your

**[03:19]** a black box. Once you give them your

**[03:19]** a black box. Once you give them your data, you have no idea what happens

**[03:20]** data, you have no idea what happens

**[03:20]** data, you have no idea what happens inside. And what Apple does is tries to

**[03:23]** inside. And what Apple does is tries to

**[03:23]** inside. And what Apple does is tries to make it not a black box so that the

**[03:24]** make it not a black box so that the

**[03:24]** make it not a black box so that the iPhone has some control of what happens

**[03:27]** iPhone has some control of what happens

**[03:27]** iPhone has some control of what happens to the data inside Apple's remote

**[03:29]** to the data inside Apple's remote

**[03:29]** to the data inside Apple's remote servers.

**[03:31]** servers.

**[03:31]** servers. Uh and hopefully that this trusted

**[03:32]** Uh and hopefully that this trusted

**[03:32]** Uh and hopefully that this trusted remote service is also hard to hack. So,

**[03:35]** remote service is also hard to hack. So,

**[03:35]** remote service is also hard to hack. So, for the remainder of the talk and uh

**[03:37]** for the remainder of the talk and uh

**[03:37]** for the remainder of the talk and uh we're not going to be able to get into

**[03:38]** we're not going to be able to get into

**[03:38]** we're not going to be able to get into all of it in 16 minutes, uh but we're

**[03:41]** all of it in 16 minutes, uh but we're

**[03:41]** all of it in 16 minutes, uh but we're going to talk about Apple's PCC

**[03:43]** going to talk about Apple's PCC

**[03:43]** going to talk about Apple's PCC requirements that they set up and I'll

**[03:45]** requirements that they set up and I'll

**[03:45]** requirements that they set up and I'll review a conceptual architecture about

**[03:46]** review a conceptual architecture about

**[03:46]** review a conceptual architecture about how they meet those requirements. Then

**[03:48]** how they meet those requirements. Then

**[03:48]** how they meet those requirements. Then we'll go into two specific components of

**[03:50]** we'll go into two specific components of

**[03:50]** we'll go into two specific components of the six because I don't have time to go

**[03:52]** the six because I don't have time to go

**[03:52]** the six because I don't have time to go through all six and you'll be bored by

**[03:54]** through all six and you'll be bored by

**[03:54]** through all six and you'll be bored by that point. Uh and then talk about some

**[03:56]** that point. Uh and then talk about some

**[03:56]** that point. Uh and then talk about some some pros and cons of Apple's things and

**[03:58]** some pros and cons of Apple's things and

**[03:58]** some pros and cons of Apple's things and how we might use some of those

**[03:59]** how we might use some of those

**[03:59]** how we might use some of those components ourselves.


### [04:00 - 05:00]

**[04:01]** components ourselves.

**[04:02]** components ourselves. So there are five key requirements to

**[04:05]** So there are five key requirements to

**[04:05]** So there are five key requirements to Apple's private cloud compute that

**[04:07]** Apple's private cloud compute that

**[04:07]** Apple's private cloud compute that they're trying to meet when they design

**[04:08]** they're trying to meet when they design

**[04:08]** they're trying to meet when they design the system. The first one is stateless

**[04:09]** the system. The first one is stateless

**[04:09]** the system. The first one is stateless computation. This is essentially the

**[04:11]** computation. This is essentially the

**[04:11]** computation. This is essentially the guarantee that when Apple receives your

**[04:13]** guarantee that when Apple receives your

**[04:13]** guarantee that when Apple receives your data, it's only used to satisfy the

**[04:15]** data, it's only used to satisfy the

**[04:15]** data, it's only used to satisfy the request and cannot be used. It's

**[04:16]** request and cannot be used. It's

**[04:16]** request and cannot be used. It's impossible to use it for anything else.

**[04:18]** impossible to use it for anything else.

**[04:18]** impossible to use it for anything else. You can't log it, anything like that.

**[04:20]** You can't log it, anything like that.

**[04:20]** You can't log it, anything like that. Um, the second thing is enforceable

**[04:23]** Um, the second thing is enforceable

**[04:23]** Um, the second thing is enforceable guarantees. That these notion that the

**[04:25]** guarantees. That these notion that the

**[04:25]** guarantees. That these notion that the code, everything's enforced with code,

**[04:27]** code, everything's enforced with code,

**[04:27]** code, everything's enforced with code, not by some sort of policy. Not I

**[04:29]** not by some sort of policy. Not I

**[04:29]** not by some sort of policy. Not I shouldn't SSH to the instance, but I can

**[04:31]** shouldn't SSH to the instance, but I can

**[04:31]** shouldn't SSH to the instance, but I can SSH to the instances. No, there's no SSH

**[04:33]** SSH to the instances. No, there's no SSH

**[04:33]** SSH to the instances. No, there's no SSH on the instance. You can't SSH to it.

**[04:35]** on the instance. You can't SSH to it.

**[04:35]** on the instance. You can't SSH to it. Um, you don't want to save things. Well,

**[04:37]** Um, you don't want to save things. Well,

**[04:37]** Um, you don't want to save things. Well, don't have a disk, right? So, these are

**[04:39]** don't have a disk, right? So, these are

**[04:39]** don't have a disk, right? So, these are what they call enforceable guarantees,

**[04:40]** what they call enforceable guarantees,

**[04:40]** what they call enforceable guarantees, not just policies. The third principle

**[04:43]** not just policies. The third principle

**[04:43]** not just policies. The third principle or requirement is non-targetability.

**[04:45]** or requirement is non-targetability.

**[04:45]** or requirement is non-targetability. That means that if you wanted to hack my

**[04:48]** That means that if you wanted to hack my

**[04:48]** That means that if you wanted to hack my data on PCC, you'd have to target

**[04:50]** data on PCC, you'd have to target

**[04:50]** data on PCC, you'd have to target everyone and sift through all of it

**[04:52]** everyone and sift through all of it

**[04:52]** everyone and sift through all of it rather than having some easy way to find

**[04:54]** rather than having some easy way to find

**[04:54]** rather than having some easy way to find just me.

**[04:57]** just me.

**[04:57]** just me. No privilege runtime access. I just


### [05:00 - 06:00]

**[05:00]** No privilege runtime access. I just

**[05:00]** No privilege runtime access. I just briefly touched on it earlier, but

**[05:02]** briefly touched on it earlier, but

**[05:02]** briefly touched on it earlier, but essentially there's no way to bypass

**[05:03]** essentially there's no way to bypass

**[05:03]** essentially there's no way to bypass these restrictions in production.

**[05:06]** these restrictions in production.

**[05:06]** these restrictions in production. Um, and then the final one and the most

**[05:08]** Um, and then the final one and the most

**[05:08]** Um, and then the final one and the most important one is verifiable

**[05:09]** important one is verifiable

**[05:09]** important one is verifiable transparency. Verifiable transparency

**[05:11]** transparency. Verifiable transparency

**[05:12]** transparency. Verifiable transparency essentially says we can prove that all

**[05:13]** essentially says we can prove that all

**[05:13]** essentially says we can prove that all of the above items are true. Great.

**[05:19]** of the above items are true. Great.

**[05:19]** of the above items are true. Great. So let's talk about again this is a

**[05:21]** So let's talk about again this is a

**[05:21]** So let's talk about again this is a little more bigger representation of the

**[05:23]** little more bigger representation of the

**[05:23]** little more bigger representation of the black box. um in a classic you know kind

**[05:27]** black box. um in a classic you know kind

**[05:27]** black box. um in a classic you know kind of remote system you have some sort of

**[05:28]** of remote system you have some sort of

**[05:28]** of remote system you have some sort of off service and then we have an AI

**[05:30]** off service and then we have an AI

**[05:30]** off service and then we have an AI engine and in this AI engine you have

**[05:32]** engine and in this AI engine you have

**[05:32]** engine and in this AI engine you have some S sur who can access it and some

**[05:34]** some S sur who can access it and some

**[05:34]** some S sur who can access it and some disk that you can write to it but again

**[05:36]** disk that you can write to it but again

**[05:36]** disk that you can write to it but again the iPhone doesn't know uh what it's

**[05:37]** the iPhone doesn't know uh what it's

**[05:38]** the iPhone doesn't know uh what it's sending its data to but this is

**[05:39]** sending its data to but this is

**[05:39]** sending its data to but this is fundamentally so let's see how we can

**[05:41]** fundamentally so let's see how we can

**[05:41]** fundamentally so let's see how we can change this to uh get to some of these

**[05:44]** change this to uh get to some of these

**[05:44]** change this to uh get to some of these at a conceptual level so the first thing

**[05:46]** at a conceptual level so the first thing

**[05:46]** at a conceptual level so the first thing that Apple does is it adds an anonymizer

**[05:51]** that Apple does is it adds an anonymizer

**[05:51]** that Apple does is it adds an anonymizer and uh this anonymizer is the first part

**[05:55]** and uh this anonymizer is the first part

**[05:55]** and uh this anonymizer is the first part of two parts of non-targetability. But

**[05:57]** of two parts of non-targetability. But

**[05:57]** of two parts of non-targetability. But ideally, right, Apple can't tell who the

**[05:59]** ideally, right, Apple can't tell who the


### [06:00 - 07:00]

**[06:00]** ideally, right, Apple can't tell who the data is coming from. So, it would be

**[06:01]** data is coming from. So, it would be

**[06:01]** data is coming from. So, it would be harder for an attacker to come and like

**[06:04]** harder for an attacker to come and like

**[06:04]** harder for an attacker to come and like fish out my particular set of data. Um,

**[06:08]** fish out my particular set of data. Um,

**[06:08]** fish out my particular set of data. Um, if but if you're a student and looking

**[06:10]** if but if you're a student and looking

**[06:10]** if but if you're a student and looking at this, there's still O behind the

**[06:11]** at this, there's still O behind the

**[06:11]** at this, there's still O behind the anonymizer and so the iPhone provides

**[06:13]** anonymizer and so the iPhone provides

**[06:13]** anonymizer and so the iPhone provides some sort of O credentials and those O

**[06:14]** some sort of O credentials and those O

**[06:14]** some sort of O credentials and those O credentials are obviously tied to the

**[06:15]** credentials are obviously tied to the

**[06:16]** credentials are obviously tied to the user. So, the second thing that Apple

**[06:17]** user. So, the second thing that Apple

**[06:17]** user. So, the second thing that Apple does is separates O. Um, and

**[06:20]** does is separates O. Um, and

**[06:20]** does is separates O. Um, and conceptually you think of this as if

**[06:21]** conceptually you think of this as if

**[06:21]** conceptually you think of this as if you're going to the arcade uh and you

**[06:23]** you're going to the arcade uh and you

**[06:23]** you're going to the arcade uh and you want to go spend your money on an arcade

**[06:25]** want to go spend your money on an arcade

**[06:25]** want to go spend your money on an arcade machines. You first put your money into

**[06:26]** machines. You first put your money into

**[06:26]** machines. You first put your money into the coin machine. You get some coins

**[06:28]** the coin machine. You get some coins

**[06:28]** the coin machine. You get some coins out. These coins are anonymous. Now you

**[06:31]** out. These coins are anonymous. Now you

**[06:31]** out. These coins are anonymous. Now you can go to the machine and no one knows

**[06:32]** can go to the machine and no one knows

**[06:32]** can go to the machine and no one knows uh what machines you spent your money

**[06:34]** uh what machines you spent your money

**[06:34]** uh what machines you spent your money on. That's essentially what happens

**[06:35]** on. That's essentially what happens

**[06:35]** on. That's essentially what happens here. It's called blind signatures.

**[06:37]** here. It's called blind signatures.

**[06:37]** here. It's called blind signatures. We're not going to have time to get into

**[06:38]** We're not going to have time to get into

**[06:38]** We're not going to have time to get into it today, but that's what happens. So

**[06:40]** it today, but that's what happens. So

**[06:40]** it today, but that's what happens. So now the iPhone is making an anonymous

**[06:43]** now the iPhone is making an anonymous

**[06:43]** now the iPhone is making an anonymous request going through an anonymizer

**[06:45]** request going through an anonymizer

**[06:45]** request going through an anonymizer that's taking everyone's it's kind of

**[06:47]** that's taking everyone's it's kind of

**[06:47]** that's taking everyone's it's kind of like tour. It's like laundering

**[06:48]** like tour. It's like laundering

**[06:48]** like tour. It's like laundering everyone's data. Uh so that if someone

**[06:52]** everyone's data. Uh so that if someone

**[06:52]** everyone's data. Uh so that if someone were to access the system internally,

**[06:54]** were to access the system internally,

**[06:54]** were to access the system internally, they wouldn't know who it's coming from.

**[06:56]** they wouldn't know who it's coming from.

**[06:56]** they wouldn't know who it's coming from. So that gets us non-targetability.

**[06:58]** So that gets us non-targetability.

**[06:58]** So that gets us non-targetability. The second thing that Apple does is it

**[06:59]** The second thing that Apple does is it


### [07:00 - 08:00]

**[07:00]** The second thing that Apple does is it changes the set of requests that are

**[07:01]** changes the set of requests that are

**[07:02]** changes the set of requests that are happening. The first thing it does is

**[07:03]** happening. The first thing it does is

**[07:03]** happening. The first thing it does is before it sends its data, it says what

**[07:05]** before it sends its data, it says what

**[07:05]** before it sends its data, it says what are you running? Uh and if the AI engine

**[07:08]** are you running? Uh and if the AI engine

**[07:08]** are you running? Uh and if the AI engine replies with I'm running this and only

**[07:10]** replies with I'm running this and only

**[07:10]** replies with I'm running this and only this, the iPhone might say okay, I trust

**[07:12]** this, the iPhone might say okay, I trust

**[07:12]** this, the iPhone might say okay, I trust that. uh and if that remains true then

**[07:15]** that. uh and if that remains true then

**[07:15]** that. uh and if that remains true then you can run this this AI on the data

**[07:18]** you can run this this AI on the data

**[07:18]** you can run this this AI on the data that I'm submitting. Um this is where

**[07:20]** that I'm submitting. Um this is where

**[07:20]** that I'm submitting. Um this is where how they achieve verifiable

**[07:22]** how they achieve verifiable

**[07:22]** how they achieve verifiable transparency. There's a little more

**[07:23]** transparency. There's a little more

**[07:23]** transparency. There's a little more subtlety to that which we are going to

**[07:24]** subtlety to that which we are going to

**[07:24]** subtlety to that which we are going to get into. Um but it's essentially the

**[07:26]** get into. Um but it's essentially the

**[07:26]** get into. Um but it's essentially the iPhone says I trust the code that you're

**[07:28]** iPhone says I trust the code that you're

**[07:28]** iPhone says I trust the code that you're running. You can only decrypt my data if

**[07:29]** running. You can only decrypt my data if

**[07:29]** running. You can only decrypt my data if you're still running that code. So the

**[07:31]** you're still running that code. So the

**[07:31]** you're still running that code. So the iPhone can verify what they're doing.

**[07:33]** iPhone can verify what they're doing.

**[07:33]** iPhone can verify what they're doing. The next thing no privilege runtime

**[07:35]** The next thing no privilege runtime

**[07:35]** The next thing no privilege runtime access. That was easy. Just get rid of

**[07:36]** access. That was easy. Just get rid of

**[07:36]** access. That was easy. Just get rid of SSHD. Make it no way of accessing those

**[07:39]** SSHD. Make it no way of accessing those

**[07:39]** SSHD. Make it no way of accessing those machines. Uh enforceable guarantees. get

**[07:42]** machines. Uh enforceable guarantees. get

**[07:42]** machines. Uh enforceable guarantees. get rid of the disk. We talked about that.

**[07:45]** rid of the disk. We talked about that.

**[07:45]** rid of the disk. We talked about that. And then stateless computation again

**[07:46]** And then stateless computation again

**[07:46]** And then stateless computation again with no disk, no access. There's nothing

**[07:48]** with no disk, no access. There's nothing

**[07:48]** with no disk, no access. There's nothing to do with the data other than respond

**[07:50]** to do with the data other than respond

**[07:50]** to do with the data other than respond to the iPhone. Um, and since the iPhone

**[07:54]** to the iPhone. Um, and since the iPhone

**[07:54]** to the iPhone. Um, and since the iPhone verified the code that was running on

**[07:55]** verified the code that was running on

**[07:55]** verified the code that was running on this machine, it knows it's not being

**[07:57]** this machine, it knows it's not being

**[07:57]** this machine, it knows it's not being logged anywhere before it gives them the

**[07:58]** logged anywhere before it gives them the

**[07:58]** logged anywhere before it gives them the data. Okay, so they achieve those five


### [08:00 - 09:00]

**[08:03]** data. Okay, so they achieve those five

**[08:03]** data. Okay, so they achieve those five guarantees that I talked about here

**[08:05]** guarantees that I talked about here

**[08:05]** guarantees that I talked about here using six technical components. And

**[08:07]** using six technical components. And

**[08:08]** using six technical components. And again, we're going to go into two of

**[08:09]** again, we're going to go into two of

**[08:09]** again, we're going to go into two of them. Um, but I'll describe them all

**[08:12]** them. Um, but I'll describe them all

**[08:12]** them. Um, but I'll describe them all very briefly. Oblivious HTTP is a spec

**[08:15]** very briefly. Oblivious HTTP is a spec

**[08:15]** very briefly. Oblivious HTTP is a spec developed by Cloudflare and Apple and

**[08:17]** developed by Cloudflare and Apple and

**[08:17]** developed by Cloudflare and Apple and others that allows you to essentially

**[08:19]** others that allows you to essentially

**[08:19]** others that allows you to essentially make anonymous requests using a third

**[08:22]** make anonymous requests using a third

**[08:22]** make anonymous requests using a third party to uh use the launder your

**[08:25]** party to uh use the launder your

**[08:25]** party to uh use the launder your requests through this third party. So

**[08:26]** requests through this third party. So

**[08:26]** requests through this third party. So all of the request that goes to Apple's

**[08:28]** all of the request that goes to Apple's

**[08:28]** all of the request that goes to Apple's private cloud compute first goes through

**[08:29]** private cloud compute first goes through

**[08:29]** private cloud compute first goes through Cloudflare. So when Apple receives it,

**[08:31]** Cloudflare. So when Apple receives it,

**[08:31]** Cloudflare. So when Apple receives it, it only knows that it came from

**[08:33]** it only knows that it came from

**[08:33]** it only knows that it came from Cloudflare, not from an individual

**[08:34]** Cloudflare, not from an individual

**[08:34]** Cloudflare, not from an individual user's IP address. The second thing that

**[08:37]** user's IP address. The second thing that

**[08:37]** user's IP address. The second thing that they use is blind signatures. Blind

**[08:39]** they use is blind signatures. Blind

**[08:39]** they use is blind signatures. Blind signatures is that arcade analogy that I

**[08:41]** signatures is that arcade analogy that I

**[08:41]** signatures is that arcade analogy that I gave you, but it essentially is a way to

**[08:43]** gave you, but it essentially is a way to

**[08:43]** gave you, but it essentially is a way to O separately and then verify that you're

**[08:46]** O separately and then verify that you're

**[08:46]** O separately and then verify that you're bearing true authentication, but you

**[08:48]** bearing true authentication, but you

**[08:48]** bearing true authentication, but you can't link it to your identity. And

**[08:50]** can't link it to your identity. And

**[08:50]** can't link it to your identity. And again, we don't have time to go into

**[08:51]** again, we don't have time to go into

**[08:51]** again, we don't have time to go into that, but if you want to look it up,

**[08:52]** that, but if you want to look it up,

**[08:52]** that, but if you want to look it up, it's a formal spec as well. There's lots

**[08:54]** it's a formal spec as well. There's lots

**[08:54]** it's a formal spec as well. There's lots of packages and open source libraries

**[08:56]** of packages and open source libraries

**[08:56]** of packages and open source libraries that let you to use that.

**[08:58]** that let you to use that.

**[08:58]** that let you to use that. Third component is the secure enclave.


### [09:00 - 10:00]

**[09:01]** Third component is the secure enclave.

**[09:01]** Third component is the secure enclave. Um, this is an equivalent we have in in

**[09:04]** Um, this is an equivalent we have in in

**[09:04]** Um, this is an equivalent we have in in our world that if we're not programming

**[09:05]** our world that if we're not programming

**[09:05]** our world that if we're not programming on Apple is TPMs, if you've heard of

**[09:07]** on Apple is TPMs, if you've heard of

**[09:07]** on Apple is TPMs, if you've heard of that, but they're essentially a place, a

**[09:09]** that, but they're essentially a place, a

**[09:09]** that, but they're essentially a place, a separate piece of hardware where the

**[09:11]** separate piece of hardware where the

**[09:11]** separate piece of hardware where the private keys are kept and that makes a

**[09:13]** private keys are kept and that makes a

**[09:13]** private keys are kept and that makes a guarantee that those keys can never be

**[09:16]** guarantee that those keys can never be

**[09:16]** guarantee that those keys can never be removed from the hardware. That's really

**[09:17]** removed from the hardware. That's really

**[09:17]** removed from the hardware. That's really important um because you don't want the

**[09:21]** important um because you don't want the

**[09:21]** important um because you don't want the keys to be given away that does all of

**[09:23]** keys to be given away that does all of

**[09:23]** keys to be given away that does all of these all of the interactions that this

**[09:25]** these all of the interactions that this

**[09:25]** these all of the interactions that this is doing is with keys that they prove

**[09:27]** is doing is with keys that they prove

**[09:27]** is doing is with keys that they prove who they are. if they could move it and

**[09:29]** who they are. if they could move it and

**[09:29]** who they are. if they could move it and have some third party hold it, then it

**[09:31]** have some third party hold it, then it

**[09:31]** have some third party hold it, then it wouldn't be trusted, right? You could

**[09:32]** wouldn't be trusted, right? You could

**[09:32]** wouldn't be trusted, right? You could essentially fake everyone out that you

**[09:34]** essentially fake everyone out that you

**[09:34]** essentially fake everyone out that you are an official AI engine, but actually

**[09:36]** are an official AI engine, but actually

**[09:36]** are an official AI engine, but actually you're somewhere else. So, the secure

**[09:38]** you're somewhere else. So, the secure

**[09:38]** you're somewhere else. So, the secure enclave helps with that. Again, won't be

**[09:39]** enclave helps with that. Again, won't be

**[09:39]** enclave helps with that. Again, won't be getting into those. We're going to get

**[09:40]** getting into those. We're going to get

**[09:40]** getting into those. We're going to get into these two. Uh, the last one is

**[09:42]** into these two. Uh, the last one is

**[09:42]** into these two. Uh, the last one is secure boot and hardened operating

**[09:43]** secure boot and hardened operating

**[09:43]** secure boot and hardened operating system. This is like a standard

**[09:46]** system. This is like a standard

**[09:46]** system. This is like a standard technique. Um, but it's essentially they

**[09:49]** technique. Um, but it's essentially they

**[09:49]** technique. Um, but it's essentially they run a very limited version of iOS. Um,

**[09:51]** run a very limited version of iOS. Um,

**[09:51]** run a very limited version of iOS. Um, that makes it very difficult to hack or

**[09:52]** that makes it very difficult to hack or

**[09:52]** that makes it very difficult to hack or modify. Um everything has to be signed

**[09:55]** modify. Um everything has to be signed

**[09:55]** modify. Um everything has to be signed just like every if you've done an iOS

**[09:56]** just like every if you've done an iOS

**[09:56]** just like every if you've done an iOS now app now you have to do signatures

**[09:58]** now app now you have to do signatures

**[09:58]** now app now you have to do signatures but theirs is like even crazier. Um okay


### [10:00 - 11:00]

**[10:01]** but theirs is like even crazier. Um okay

**[10:01]** but theirs is like even crazier. Um okay so the ones we're going to talk about

**[10:03]** so the ones we're going to talk about

**[10:03]** so the ones we're going to talk about are remote attestation that was this

**[10:05]** are remote attestation that was this

**[10:05]** are remote attestation that was this flow I talked about here um great and

**[10:09]** flow I talked about here um great and

**[10:09]** flow I talked about here um great and then uh the other one is the

**[10:10]** then uh the other one is the

**[10:10]** then uh the other one is the transparency log the transparency log is

**[10:13]** transparency log the transparency log is

**[10:13]** transparency log the transparency log is a record of all the software that

**[10:14]** a record of all the software that

**[10:14]** a record of all the software that Apple's deploying on their private nodes

**[10:17]** Apple's deploying on their private nodes

**[10:17]** Apple's deploying on their private nodes so that you can go and verify what's on

**[10:19]** so that you can go and verify what's on

**[10:19]** so that you can go and verify what's on the record is actually what's being sent

**[10:21]** the record is actually what's being sent

**[10:21]** the record is actually what's being sent to you during the attestation. Okay, so

**[10:23]** to you during the attestation. Okay, so

**[10:23]** to you during the attestation. Okay, so let's talk about remote attestation very

**[10:26]** let's talk about remote attestation very

**[10:26]** let's talk about remote attestation very briefly.

**[10:28]** briefly.

**[10:28]** briefly. Uh, and I'm going to talk about it

**[10:29]** Uh, and I'm going to talk about it

**[10:29]** Uh, and I'm going to talk about it abstractly, not with iPhones. So, you

**[10:32]** abstractly, not with iPhones. So, you

**[10:32]** abstractly, not with iPhones. So, you have some client and the client says,

**[10:33]** have some client and the client says,

**[10:33]** have some client and the client says, "What are you running?" Uh, and the

**[10:35]** "What are you running?" Uh, and the

**[10:35]** "What are you running?" Uh, and the server replies with two things, a set of

**[10:37]** server replies with two things, a set of

**[10:37]** server replies with two things, a set of signed claims and then a public key. And

**[10:40]** signed claims and then a public key. And

**[10:40]** signed claims and then a public key. And the signed claims essentially say, "I'm

**[10:43]** the signed claims essentially say, "I'm

**[10:43]** the signed claims essentially say, "I'm on genuine hardware. Uh, I'm running a

**[10:45]** on genuine hardware. Uh, I'm running a

**[10:45]** on genuine hardware. Uh, I'm running a genuine GPU. Uh, I am running this set

**[10:48]** genuine GPU. Uh, I am running this set

**[10:48]** genuine GPU. Uh, I am running this set of software. I use this bootloadader. I

**[10:51]** of software. I use this bootloadader. I

**[10:51]** of software. I use this bootloadader. I use this version of Linux. And then the

**[10:54]** use this version of Linux. And then the

**[10:54]** use this version of Linux. And then the client gets to look at those claims and

**[10:55]** client gets to look at those claims and

**[10:55]** client gets to look at those claims and decide whether it trusts that version.

**[10:59]** decide whether it trusts that version.

**[10:59]** decide whether it trusts that version. Uh right, it might be like, oh, I only


### [11:00 - 12:00]

**[11:00]** Uh right, it might be like, oh, I only

**[11:00]** Uh right, it might be like, oh, I only trust this version of the Linux kernel

**[11:02]** trust this version of the Linux kernel

**[11:02]** trust this version of the Linux kernel and above. Um or I only trust that it's

**[11:05]** and above. Um or I only trust that it's

**[11:05]** and above. Um or I only trust that it's been signed by Apple. Uh and if so, it

**[11:08]** been signed by Apple. Uh and if so, it

**[11:08]** been signed by Apple. Uh and if so, it can use this public key that comes

**[11:10]** can use this public key that comes

**[11:10]** can use this public key that comes across to encrypt data that is later

**[11:13]** across to encrypt data that is later

**[11:13]** across to encrypt data that is later sent to the server.

**[11:16]** sent to the server.

**[11:16]** sent to the server. uh and this is really important which is

**[11:19]** uh and this is really important which is

**[11:19]** uh and this is really important which is this public key and these claims are

**[11:20]** this public key and these claims are

**[11:20]** this public key and these claims are tied together. So during later

**[11:22]** tied together. So during later

**[11:22]** tied together. So during later interactions with the server the client

**[11:24]** interactions with the server the client

**[11:24]** interactions with the server the client will encrypt using the public key and

**[11:26]** will encrypt using the public key and

**[11:26]** will encrypt using the public key and the signed claims and the server will

**[11:28]** the signed claims and the server will

**[11:28]** the signed claims and the server will only be able to decrypt if it is still

**[11:30]** only be able to decrypt if it is still

**[11:30]** only be able to decrypt if it is still matching those signed claims. There's a

**[11:32]** matching those signed claims. There's a

**[11:32]** matching those signed claims. There's a whole bunch of cryptography that makes

**[11:34]** whole bunch of cryptography that makes

**[11:34]** whole bunch of cryptography that makes this possible and a bunch of certificate

**[11:36]** this possible and a bunch of certificate

**[11:36]** this possible and a bunch of certificate chains and a bunch of like trust and

**[11:38]** chains and a bunch of like trust and

**[11:38]** chains and a bunch of like trust and vendors but that's the fundamental idea

**[11:40]** vendors but that's the fundamental idea

**[11:40]** vendors but that's the fundamental idea and this is what is letting you change

**[11:42]** and this is what is letting you change

**[11:42]** and this is what is letting you change that black box to something that's a

**[11:44]** that black box to something that's a

**[11:44]** that black box to something that's a little more translucent, right? You're

**[11:45]** little more translucent, right? You're

**[11:45]** little more translucent, right? You're not just throwing it over the wall. You

**[11:46]** not just throwing it over the wall. You

**[11:46]** not just throwing it over the wall. You can kind of see what's going on inside.

**[11:50]** can kind of see what's going on inside.

**[11:50]** can kind of see what's going on inside. Okay. The second thing is the

**[11:52]** Okay. The second thing is the

**[11:52]** Okay. The second thing is the transparency log. Transparency log is

**[11:54]** transparency log. Transparency log is

**[11:54]** transparency log. Transparency log is actually very simple conceptually. It's

**[11:56]** actually very simple conceptually. It's

**[11:56]** actually very simple conceptually. It's just a database with records for each

**[11:59]** just a database with records for each

**[11:59]** just a database with records for each software release and or each component


### [12:00 - 13:00]

**[12:00]** software release and or each component

**[12:00]** software release and or each component in a software release signed by a

**[12:03]** in a software release signed by a

**[12:03]** in a software release signed by a particular person. Um so for example in

**[12:06]** particular person. Um so for example in

**[12:06]** particular person. Um so for example in this record Bob added this binary or

**[12:10]** this record Bob added this binary or

**[12:10]** this record Bob added this binary or piece of like compiled source code. Uh,

**[12:13]** piece of like compiled source code. Uh,

**[12:13]** piece of like compiled source code. Uh, and this is the hash of that binary on

**[12:14]** and this is the hash of that binary on

**[12:14]** and this is the hash of that binary on November 1st of 24. And then, uh, that's

**[12:18]** November 1st of 24. And then, uh, that's

**[12:18]** November 1st of 24. And then, uh, that's it. It's just a declaration that this

**[12:20]** it. It's just a declaration that this

**[12:20]** it. It's just a declaration that this binary was signed by Bob. Uh, why does

**[12:23]** binary was signed by Bob. Uh, why does

**[12:23]** binary was signed by Bob. Uh, why does that matter? Why would you care about

**[12:25]** that matter? Why would you care about

**[12:25]** that matter? Why would you care about this? Well, first of all, um, reviewers

**[12:28]** this? Well, first of all, um, reviewers

**[12:28]** this? Well, first of all, um, reviewers can go through and offline look at these

**[12:31]** can go through and offline look at these

**[12:31]** can go through and offline look at these binaries that are made publicly

**[12:33]** binaries that are made publicly

**[12:33]** binaries that are made publicly available and verify their behavior.

**[12:36]** available and verify their behavior.

**[12:36]** available and verify their behavior. And so then when you get a remote

**[12:37]** And so then when you get a remote

**[12:37]** And so then when you get a remote attestation and the remote attestation

**[12:39]** attestation and the remote attestation

**[12:39]** attestation and the remote attestation says this hash of this binary is there

**[12:41]** says this hash of this binary is there

**[12:41]** says this hash of this binary is there you can be like oh yeah I've already

**[12:42]** you can be like oh yeah I've already

**[12:42]** you can be like oh yeah I've already checked this binary I believe that it's

**[12:44]** checked this binary I believe that it's

**[12:44]** checked this binary I believe that it's doing the right thing. Um the second

**[12:47]** doing the right thing. Um the second

**[12:47]** doing the right thing. Um the second thing so that's what I said the second

**[12:48]** thing so that's what I said the second

**[12:48]** thing so that's what I said the second point which is you can check that remote

**[12:49]** point which is you can check that remote

**[12:50]** point which is you can check that remote attestations match what's in the log.

**[12:52]** attestations match what's in the log.

**[12:52]** attestations match what's in the log. And then finally if you see an

**[12:53]** And then finally if you see an

**[12:54]** And then finally if you see an attestation that's not on the log you

**[12:56]** attestation that's not on the log you

**[12:56]** attestation that's not on the log you know the whole system's been compromised

**[12:58]** know the whole system's been compromised

**[12:58]** know the whole system's been compromised because if if it's not on the log

**[12:59]** because if if it's not on the log

**[12:59]** because if if it's not on the log definitely someone is like doing some


### [13:00 - 14:00]

**[13:01]** definitely someone is like doing some

**[13:01]** definitely someone is like doing some sort of shenanigans right they might

**[13:03]** sort of shenanigans right they might

**[13:03]** sort of shenanigans right they might have like hijacked your connection or

**[13:05]** have like hijacked your connection or

**[13:05]** have like hijacked your connection or whatever. Um, and it's just because like

**[13:07]** whatever. Um, and it's just because like

**[13:07]** whatever. Um, and it's just because like a limited set of people can write to

**[13:09]** a limited set of people can write to

**[13:09]** a limited set of people can write to this log and there's no way to modify

**[13:11]** this log and there's no way to modify

**[13:11]** this log and there's no way to modify the log, right? It's append only. It

**[13:12]** the log, right? It's append only. It

**[13:12]** the log, right? It's append only. It uses like a Merkel tree so that you

**[13:14]** uses like a Merkel tree so that you

**[13:14]** uses like a Merkel tree so that you can't change the contents. Um, great.

**[13:19]** can't change the contents. Um, great.

**[13:19]** can't change the contents. Um, great. So that is the transparency log. Um, so

**[13:22]** So that is the transparency log. Um, so

**[13:22]** So that is the transparency log. Um, so let me tell you how this all comes

**[13:23]** let me tell you how this all comes

**[13:23]** let me tell you how this all comes together, right? So remote attestation

**[13:26]** together, right? So remote attestation

**[13:26]** together, right? So remote attestation is this flow again. uh the iPhone first

**[13:30]** is this flow again. uh the iPhone first

**[13:30]** is this flow again. uh the iPhone first through the anonymizer requests a remote

**[13:32]** through the anonymizer requests a remote

**[13:32]** through the anonymizer requests a remote attestation package uh and then says

**[13:35]** attestation package uh and then says

**[13:35]** attestation package uh and then says well if I believe that remote

**[13:36]** well if I believe that remote

**[13:36]** well if I believe that remote attestation package I trust the contents

**[13:38]** attestation package I trust the contents

**[13:38]** attestation package I trust the contents that is running on the server I can then

**[13:41]** that is running on the server I can then

**[13:41]** that is running on the server I can then send my data and I phrase this as try to

**[13:43]** send my data and I phrase this as try to

**[13:43]** send my data and I phrase this as try to decrypt the data and run the AI again if

**[13:45]** decrypt the data and run the AI again if

**[13:45]** decrypt the data and run the AI again if the attestation changed

**[13:48]** the attestation changed

**[13:48]** the attestation changed the AI engine would not be able to

**[13:49]** the AI engine would not be able to

**[13:49]** the AI engine would not be able to decrypt the data right so that's the

**[13:51]** decrypt the data right so that's the

**[13:51]** decrypt the data right so that's the most important part right it says I'm

**[13:52]** most important part right it says I'm

**[13:52]** most important part right it says I'm running this thing trust me and it says

**[13:54]** running this thing trust me and it says

**[13:54]** running this thing trust me and it says I trust you okay great encrypt it and I

**[13:56]** I trust you okay great encrypt it and I

**[13:56]** I trust you okay great encrypt it and I can only decrypt it as long as it's

**[13:58]** can only decrypt it as long as it's

**[13:58]** can only decrypt it as long as it's still running the exact thing I said I

**[13:59]** still running the exact thing I said I

**[13:59]** still running the exact thing I said I trusted.


### [14:00 - 15:00]

**[14:01]** trusted.

**[14:01]** trusted. And the second item we talked about is

**[14:03]** And the second item we talked about is

**[14:03]** And the second item we talked about is the transparency log which is check if

**[14:05]** the transparency log which is check if

**[14:05]** the transparency log which is check if the attested claims match the

**[14:07]** the attested claims match the

**[14:07]** the attested claims match the transparency log. And this transparency

**[14:09]** transparency log. And this transparency

**[14:09]** transparency log. And this transparency log we talked about so on here Apple is

**[14:11]** log we talked about so on here Apple is

**[14:11]** log we talked about so on here Apple is writing a lot a lot of software onto the

**[14:13]** writing a lot a lot of software onto the

**[14:13]** writing a lot a lot of software onto the log and then essentially saying uh trust

**[14:16]** log and then essentially saying uh trust

**[14:16]** log and then essentially saying uh trust what's on the log. You can verify it

**[14:18]** what's on the log. You can verify it

**[14:18]** what's on the log. You can verify it offline and then when the attestation

**[14:20]** offline and then when the attestation

**[14:20]** offline and then when the attestation claims come in just double check that

**[14:22]** claims come in just double check that

**[14:22]** claims come in just double check that they do indeed match.

**[14:25]** they do indeed match.

**[14:25]** they do indeed match. Um okay. And then I I don't have time to

**[14:27]** Um okay. And then I I don't have time to

**[14:27]** Um okay. And then I I don't have time to get into all of these. Um but uh here

**[14:31]** get into all of these. Um but uh here

**[14:31]** get into all of these. Um but uh here are some of the other items that we

**[14:32]** are some of the other items that we

**[14:32]** are some of the other items that we talked about. The blind signatures,

**[14:35]** talked about. The blind signatures,

**[14:35]** talked about. The blind signatures, the oblivious HTTP is the anonymizer.

**[14:38]** the oblivious HTTP is the anonymizer.

**[14:38]** the oblivious HTTP is the anonymizer. Blind signatures are the way to do the

**[14:39]** Blind signatures are the way to do the

**[14:39]** Blind signatures are the way to do the O. Um and then of course uh over here we

**[14:44]** O. Um and then of course uh over here we

**[14:44]** O. Um and then of course uh over here we have the secure enclave. I kind of put

**[14:46]** have the secure enclave. I kind of put

**[14:46]** have the secure enclave. I kind of put that outside of the AI engine. They're

**[14:48]** that outside of the AI engine. They're

**[14:48]** that outside of the AI engine. They're they're separate pieces of hardware. And

**[14:50]** they're separate pieces of hardware. And

**[14:50]** they're separate pieces of hardware. And then the hardening is just this little

**[14:52]** then the hardening is just this little

**[14:52]** then the hardening is just this little lock, but you know, we don't have time

**[14:53]** lock, but you know, we don't have time

**[14:53]** lock, but you know, we don't have time to get into it. Um,

**[14:56]** to get into it. Um,

**[14:56]** to get into it. Um, and uh, that's kind of at a very

**[14:59]** and uh, that's kind of at a very

**[14:59]** and uh, that's kind of at a very conceptual level, like you could


### [15:00 - 16:00]

**[15:00]** conceptual level, like you could

**[15:00]** conceptual level, like you could essentially do a PhD on each of these.

**[15:02]** essentially do a PhD on each of these.

**[15:02]** essentially do a PhD on each of these. Um, how Apple's PCC works. So, what are

**[15:06]** Um, how Apple's PCC works. So, what are

**[15:06]** Um, how Apple's PCC works. So, what are the gaps? What are the downsides? Well,

**[15:09]** the gaps? What are the downsides? Well,

**[15:09]** the gaps? What are the downsides? Well, first you have to put all of your trust

**[15:10]** first you have to put all of your trust

**[15:10]** first you have to put all of your trust in Apple still, right? On the bright

**[15:13]** in Apple still, right? On the bright

**[15:13]** in Apple still, right? On the bright side, like Apple runs their whole supply

**[15:14]** side, like Apple runs their whole supply

**[15:14]** side, like Apple runs their whole supply chain. They verify the nodes when they

**[15:17]** chain. They verify the nodes when they

**[15:17]** chain. They verify the nodes when they get them at their data center. they

**[15:19]** get them at their data center. they

**[15:19]** get them at their data center. they actually resign them what's called

**[15:21]** actually resign them what's called

**[15:21]** actually resign them what's called what's called data center

**[15:23]** what's called data center

**[15:23]** what's called data center identity keys or something like that

**[15:24]** identity keys or something like that

**[15:24]** identity keys or something like that DCIKs. Um but there's no guarantee that

**[15:28]** DCIKs. Um but there's no guarantee that

**[15:28]** DCIKs. Um but there's no guarantee that Apple doesn't share the searchs with

**[15:29]** Apple doesn't share the searchs with

**[15:29]** Apple doesn't share the searchs with anyone uh or insecurely generate them or

**[15:31]** anyone uh or insecurely generate them or

**[15:31]** anyone uh or insecurely generate them or set the private key to one everywhere.

**[15:34]** set the private key to one everywhere.

**[15:34]** set the private key to one everywhere. Now I I think they are trying to do

**[15:36]** Now I I think they are trying to do

**[15:36]** Now I I think they are trying to do their best effort but you you still have

**[15:38]** their best effort but you you still have

**[15:38]** their best effort but you you still have to trust you've shifted the trust now

**[15:40]** to trust you've shifted the trust now

**[15:40]** to trust you've shifted the trust now into like Apple's behavior rather than

**[15:42]** into like Apple's behavior rather than

**[15:42]** into like Apple's behavior rather than the hardware. Um but anyhow, and then

**[15:45]** the hardware. Um but anyhow, and then

**[15:45]** the hardware. Um but anyhow, and then they're only available on Apple devices

**[15:47]** they're only available on Apple devices

**[15:47]** they're only available on Apple devices for consumer use uh on official apps.

**[15:50]** for consumer use uh on official apps.

**[15:50]** for consumer use uh on official apps. Maybe at some point they'll make PCC

**[15:51]** Maybe at some point they'll make PCC

**[15:51]** Maybe at some point they'll make PCC available to everyone else uh but not

**[15:53]** available to everyone else uh but not

**[15:53]** available to everyone else uh but not yet.

**[15:55]** yet.

**[15:55]** yet. So what trade-offs does Apple PCC make?

**[15:59]** So what trade-offs does Apple PCC make?

**[15:59]** So what trade-offs does Apple PCC make? Um they're limited by latencies to Apple


### [16:00 - 17:00]

**[16:01]** Um they're limited by latencies to Apple

**[16:01]** Um they're limited by latencies to Apple data centers. So um they do have local

**[16:04]** data centers. So um they do have local

**[16:04]** data centers. So um they do have local models first that they try and use. Um

**[16:05]** models first that they try and use. Um

**[16:06]** models first that they try and use. Um but if those local models aren't

**[16:07]** but if those local models aren't

**[16:07]** but if those local models aren't adequate, they'll send them to data

**[16:08]** adequate, they'll send them to data

**[16:08]** adequate, they'll send them to data centers. uh as we start to do like

**[16:12]** centers. uh as we start to do like

**[16:12]** centers. uh as we start to do like real-time voice and other things uh this

**[16:14]** real-time voice and other things uh this

**[16:14]** real-time voice and other things uh this is a little more latency uh like adds a

**[16:17]** is a little more latency uh like adds a

**[16:17]** is a little more latency uh like adds a lot more latency to the system. Um the

**[16:19]** lot more latency to the system. Um the

**[16:19]** lot more latency to the system. Um the compute costs are higher. There's doing

**[16:21]** compute costs are higher. There's doing

**[16:21]** compute costs are higher. There's doing a lot more encryption. There's like I

**[16:22]** a lot more encryption. There's like I

**[16:22]** a lot more encryption. There's like I didn't I mean you're not seeing it but

**[16:24]** didn't I mean you're not seeing it but

**[16:24]** didn't I mean you're not seeing it but there's like six layers of encryption

**[16:25]** there's like six layers of encryption

**[16:25]** there's like six layers of encryption before it even gets to that node that

**[16:27]** before it even gets to that node that

**[16:27]** before it even gets to that node that actually that actually makes it happen.

**[16:28]** actually that actually makes it happen.

**[16:28]** actually that actually makes it happen. So you're spending a little bit more

**[16:29]** So you're spending a little bit more

**[16:29]** So you're spending a little bit more compute there. Like I told you no custom

**[16:32]** compute there. Like I told you no custom

**[16:32]** compute there. Like I told you no custom models, no fine-tuning. The client

**[16:34]** models, no fine-tuning. The client

**[16:34]** models, no fine-tuning. The client libraries are very complicated. um the

**[16:37]** libraries are very complicated. um the

**[16:37]** libraries are very complicated. um the client having to orchestrate all of

**[16:39]** client having to orchestrate all of

**[16:39]** client having to orchestrate all of these requests, this transparency log,

**[16:41]** these requests, this transparency log,

**[16:42]** these requests, this transparency log, this O, that's way more complicated than

**[16:43]** this O, that's way more complicated than

**[16:43]** this O, that's way more complicated than a simple HTTP request, which kind of

**[16:46]** a simple HTTP request, which kind of

**[16:46]** a simple HTTP request, which kind of sucks. Um, and what if your iPhone goes

**[16:50]** sucks. Um, and what if your iPhone goes

**[16:50]** sucks. Um, and what if your iPhone goes down after it's authenticated and then

**[16:52]** down after it's authenticated and then

**[16:52]** down after it's authenticated and then it loses all the authentication keys?

**[16:54]** it loses all the authentication keys?

**[16:54]** it loses all the authentication keys? Like you've essentially like lost all of

**[16:56]** Like you've essentially like lost all of

**[16:56]** Like you've essentially like lost all of your state, right? So, it's a lot more

**[16:57]** your state, right? So, it's a lot more

**[16:57]** your state, right? So, it's a lot more stateful.

**[16:59]** stateful.

**[16:59]** stateful. Um,


### [17:00 - 18:00]

**[17:01]** Um,

**[17:01]** Um, operationally complex. You can't SSH in

**[17:03]** operationally complex. You can't SSH in

**[17:03]** operationally complex. You can't SSH in the machines and then there's no

**[17:03]** the machines and then there's no

**[17:03]** the machines and then there's no logging. So, that's difficult. uh not

**[17:06]** logging. So, that's difficult. uh not

**[17:06]** logging. So, that's difficult. uh not everyone would sign up for that. Um you

**[17:09]** everyone would sign up for that. Um you

**[17:09]** everyone would sign up for that. Um you can't do any usage tracking. If you

**[17:11]** can't do any usage tracking. If you

**[17:11]** can't do any usage tracking. If you could do usage tracking, then you'd be

**[17:12]** could do usage tracking, then you'd be

**[17:12]** could do usage tracking, then you'd be identified, right? And so Apple can't

**[17:14]** identified, right? And so Apple can't

**[17:14]** identified, right? And so Apple can't like parcel out, you know, you get 2,000

**[17:17]** like parcel out, you know, you get 2,000

**[17:17]** like parcel out, you know, you get 2,000 tokens. They do do some fraud and abuse

**[17:20]** tokens. They do do some fraud and abuse

**[17:20]** tokens. They do do some fraud and abuse tracking at a very gross level. But um

**[17:22]** tracking at a very gross level. But um

**[17:22]** tracking at a very gross level. But um if you wanted to use this and maybe pass

**[17:24]** if you wanted to use this and maybe pass

**[17:24]** if you wanted to use this and maybe pass on your costs, a similar architecture,

**[17:26]** on your costs, a similar architecture,

**[17:26]** on your costs, a similar architecture, and pass on your costs to the customer,

**[17:27]** and pass on your costs to the customer,

**[17:28]** and pass on your costs to the customer, you wouldn't be able to know which

**[17:29]** you wouldn't be able to know which

**[17:29]** you wouldn't be able to know which customer was doing what, right? Um and

**[17:31]** customer was doing what, right? Um and

**[17:32]** customer was doing what, right? Um and then not open to thirdparty developers.

**[17:34]** then not open to thirdparty developers.

**[17:34]** then not open to thirdparty developers. Okay. What can I learn from this? I gave

**[17:37]** Okay. What can I learn from this? I gave

**[17:37]** Okay. What can I learn from this? I gave you the list of six that Apple uses and

**[17:40]** you the list of six that Apple uses and

**[17:40]** you the list of six that Apple uses and here's what's available in our world. If

**[17:42]** here's what's available in our world. If

**[17:42]** here's what's available in our world. If you're not developing on Apple silicon

**[17:43]** you're not developing on Apple silicon

**[17:43]** you're not developing on Apple silicon and Apple hardware, you still have

**[17:45]** and Apple hardware, you still have

**[17:45]** and Apple hardware, you still have oblivious HTTP and blind signatures.

**[17:47]** oblivious HTTP and blind signatures.

**[17:47]** oblivious HTTP and blind signatures. There are libraries to do that. So, we

**[17:49]** There are libraries to do that. So, we

**[17:49]** There are libraries to do that. So, we don't have secure enclaves, but we have

**[17:50]** don't have secure enclaves, but we have

**[17:50]** don't have secure enclaves, but we have TPMs. Uh, almost all Intel and AMD

**[17:54]** TPMs. Uh, almost all Intel and AMD

**[17:54]** TPMs. Uh, almost all Intel and AMD hardware now has TPMs. And then in the

**[17:56]** hardware now has TPMs. And then in the

**[17:56]** hardware now has TPMs. And then in the cloud environment, they have virtual

**[17:57]** cloud environment, they have virtual

**[17:57]** cloud environment, they have virtual TPMs uh that provide the same behavior


### [18:00 - 19:00]

**[18:00]** TPMs uh that provide the same behavior

**[18:00]** TPMs uh that provide the same behavior as a TPM. And again, that that's where

**[18:01]** as a TPM. And again, that that's where

**[18:01]** as a TPM. And again, that that's where you put a bunch of your private keys

**[18:03]** you put a bunch of your private keys

**[18:03]** you put a bunch of your private keys that are tied to that public key that I

**[18:05]** that are tied to that public key that I

**[18:05]** that are tied to that public key that I talked about. These are available for

**[18:07]** talked about. These are available for

**[18:07]** talked about. These are available for us. Secure boot and hardened operating

**[18:09]** us. Secure boot and hardened operating

**[18:09]** us. Secure boot and hardened operating system. Um,

**[18:12]** system. Um,

**[18:12]** system. Um, remote attestation is kind of available.

**[18:15]** remote attestation is kind of available.

**[18:15]** remote attestation is kind of available. It's kind of tied to the TPM. There

**[18:17]** It's kind of tied to the TPM. There

**[18:17]** It's kind of tied to the TPM. There aren't great standards yet. Um, but

**[18:19]** aren't great standards yet. Um, but

**[18:20]** aren't great standards yet. Um, but there is a little bit of work there.

**[18:21]** there is a little bit of work there.

**[18:21]** there is a little bit of work there. Transparency log. There are two open

**[18:23]** Transparency log. There are two open

**[18:23]** Transparency log. There are two open ones. One's called SIG SUM. The other

**[18:25]** ones. One's called SIG SUM. The other

**[18:25]** ones. One's called SIG SUM. The other one's called SIG Store if you've heard

**[18:26]** one's called SIG Store if you've heard

**[18:26]** one's called SIG Store if you've heard of them. if not um

**[18:29]** of them. if not um

**[18:29]** of them. if not um and then confidential VMs are just

**[18:31]** and then confidential VMs are just

**[18:31]** and then confidential VMs are just becoming available on cloud providers

**[18:34]** becoming available on cloud providers

**[18:34]** becoming available on cloud providers with GPUs. So confidential computing has

**[18:37]** with GPUs. So confidential computing has

**[18:37]** with GPUs. So confidential computing has been around for a while. Uh but now you

**[18:39]** been around for a while. Uh but now you

**[18:39]** been around for a while. Uh but now you also have to have confidential H100s and

**[18:41]** also have to have confidential H100s and

**[18:41]** also have to have confidential H100s and only H100s support and H200 support

**[18:44]** only H100s support and H200 support

**[18:44]** only H100s support and H200 support confidentiality. What that means is that

**[18:45]** confidentiality. What that means is that

**[18:46]** confidentiality. What that means is that their memor is encrypted. So if you were

**[18:47]** their memor is encrypted. So if you were

**[18:47]** their memor is encrypted. So if you were to physically go up to the H100 and like

**[18:50]** to physically go up to the H100 and like

**[18:50]** to physically go up to the H100 and like try to look at its RAM, you wouldn't be

**[18:52]** try to look at its RAM, you wouldn't be

**[18:52]** try to look at its RAM, you wouldn't be able to see what's going on there or

**[18:53]** able to see what's going on there or

**[18:53]** able to see what's going on there or figure out what's going on there. And

**[18:55]** figure out what's going on there. And

**[18:55]** figure out what's going on there. And then finally, what we have that Apple

**[18:57]** then finally, what we have that Apple

**[18:57]** then finally, what we have that Apple doesn't have is we have open source and

**[18:58]** doesn't have is we have open source and

**[18:58]** doesn't have is we have open source and we have reproducible builds. We have the


### [19:00 - 20:00]

**[19:00]** we have reproducible builds. We have the

**[19:00]** we have reproducible builds. We have the ability to link the source code to the

**[19:01]** ability to link the source code to the

**[19:01]** ability to link the source code to the binaries. Uh, and so we can have

**[19:04]** binaries. Uh, and so we can have

**[19:04]** binaries. Uh, and so we can have security research look at the source

**[19:05]** security research look at the source

**[19:05]** security research look at the source code as well as, you know, blackbox test

**[19:08]** code as well as, you know, blackbox test

**[19:08]** code as well as, you know, blackbox test the binaries and develop confidence in

**[19:10]** the binaries and develop confidence in

**[19:10]** the binaries and develop confidence in what the server might be running. All

**[19:13]** what the server might be running. All

**[19:13]** what the server might be running. All right, what's next? Okay, so Apple has

**[19:16]** right, what's next? Okay, so Apple has

**[19:16]** right, what's next? Okay, so Apple has set the standard for private AI and the

**[19:18]** set the standard for private AI and the

**[19:18]** set the standard for private AI and the market is definitely following um in

**[19:21]** market is definitely following um in

**[19:21]** market is definitely following um in that was in June of 2024. wasn't

**[19:23]** that was in June of 2024. wasn't

**[19:23]** that was in June of 2024. wasn't actually released until October of 2024.

**[19:25]** actually released until October of 2024.

**[19:25]** actually released until October of 2024. Azure Open AAI or sorry, Azure AI, not

**[19:28]** Azure Open AAI or sorry, Azure AI, not

**[19:28]** Azure Open AAI or sorry, Azure AI, not Azure OpenAI, is doing private

**[19:29]** Azure OpenAI, is doing private

**[19:29]** Azure OpenAI, is doing private inferencing starting as September.

**[19:31]** inferencing starting as September.

**[19:31]** inferencing starting as September. They're still in private preview. And

**[19:33]** They're still in private preview. And

**[19:33]** They're still in private preview. And then about a month ago, Meta of all

**[19:35]** then about a month ago, Meta of all

**[19:35]** then about a month ago, Meta of all companies, I guess I'm recorded. Meta of

**[19:37]** companies, I guess I'm recorded. Meta of

**[19:37]** companies, I guess I'm recorded. Meta of all these great companies uh also added

**[19:40]** all these great companies uh also added

**[19:40]** all these great companies uh also added uh private processing, which if you read

**[19:43]** uh private processing, which if you read

**[19:43]** uh private processing, which if you read their blog post, it's like they copy and

**[19:44]** their blog post, it's like they copy and

**[19:44]** their blog post, it's like they copy and pasted this. Maybe they used Llama to

**[19:46]** pasted this. Maybe they used Llama to

**[19:46]** pasted this. Maybe they used Llama to rewrite it um into their language, but

**[19:48]** rewrite it um into their language, but

**[19:48]** rewrite it um into their language, but it's essentially identical, which is

**[19:49]** it's essentially identical, which is

**[19:49]** it's essentially identical, which is great for all of us thinking about

**[19:51]** great for all of us thinking about

**[19:51]** great for all of us thinking about privacy. Um, and sure I'm sure uh

**[19:53]** privacy. Um, and sure I'm sure uh

**[19:53]** privacy. Um, and sure I'm sure uh WhatsApp also doesn't want those like

**[19:55]** WhatsApp also doesn't want those like

**[19:55]** WhatsApp also doesn't want those like press releases like I showed earlier.

**[19:58]** press releases like I showed earlier.

**[19:58]** press releases like I showed earlier. Um, so I'll just close by saying we're

**[19:59]** Um, so I'll just close by saying we're


### [20:00 - 21:00]

**[20:00]** Um, so I'll just close by saying we're building the same thing. Uh, but for

**[20:01]** building the same thing. Uh, but for

**[20:01]** building the same thing. Uh, but for everyone else, if you're not on Apple or

**[20:03]** everyone else, if you're not on Apple or

**[20:03]** everyone else, if you're not on Apple or you're not in WhatsApp, we have it. Uh,

**[20:05]** you're not in WhatsApp, we have it. Uh,

**[20:05]** you're not in WhatsApp, we have it. Uh, it's called confident security. Um, and

**[20:08]** it's called confident security. Um, and

**[20:08]** it's called confident security. Um, and if you'd like to talk more, let me know.

**[20:10]** if you'd like to talk more, let me know.

**[20:10]** if you'd like to talk more, let me know. By the way, this is an anti-AII shirt.

**[20:13]** By the way, this is an anti-AII shirt.

**[20:13]** By the way, this is an anti-AII shirt. Uh, which means that if you take

**[20:14]** Uh, which means that if you take

**[20:14]** Uh, which means that if you take pictures of me, it will confuse all the

**[20:16]** pictures of me, it will confuse all the

**[20:16]** pictures of me, it will confuse all the facial recognition stuff. We have

**[20:18]** facial recognition stuff. We have

**[20:18]** facial recognition stuff. We have others. If you have some cool questions

**[20:20]** others. If you have some cool questions

**[20:20]** others. If you have some cool questions and want to talk afterward, if it deems

**[20:22]** and want to talk afterward, if it deems

**[20:22]** and want to talk afterward, if it deems it worthy, I will give you an anti-AII

**[20:24]** it worthy, I will give you an anti-AII

**[20:24]** it worthy, I will give you an anti-AII shirt. We also have some other privacy

**[20:26]** shirt. We also have some other privacy

**[20:26]** shirt. We also have some other privacy based swag in the back, so come hit me

**[20:28]** based swag in the back, so come hit me

**[20:28]** based swag in the back, so come hit me up. Thanks everyone.


