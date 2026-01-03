# Useful General Intelligence — Danielle Perszyk, Amazon AGI

**Video URL:** https://www.youtube.com/watch?v=Dj0b_cEBHBI

---

## Full Transcript

### [00:00 - 01:00]

**[00:16]** Hi everyone.

**[00:16]** Hi everyone. That's a little loud. I'm Danielle and

**[00:19]** That's a little loud. I'm Danielle and

**[00:19]** That's a little loud. I'm Danielle and I'm a cognitive scientist working at the

**[00:21]** I'm a cognitive scientist working at the

**[00:21]** I'm a cognitive scientist working at the experimental new Amazon AGI SF lab. And

**[00:25]** experimental new Amazon AGI SF lab. And

**[00:25]** experimental new Amazon AGI SF lab. And throughout this conference, you're going

**[00:26]** throughout this conference, you're going

**[00:26]** throughout this conference, you're going to hear a lot of talks about building

**[00:28]** to hear a lot of talks about building

**[00:28]** to hear a lot of talks about building and scaling agents, including some from

**[00:30]** and scaling agents, including some from

**[00:30]** and scaling agents, including some from my colleagues at AWS. But this talk is

**[00:32]** my colleagues at AWS. But this talk is

**[00:32]** my colleagues at AWS. But this talk is going to be a little different. I want

**[00:34]** going to be a little different. I want

**[00:34]** going to be a little different. I want to think about how we can co-evolve with

**[00:36]** to think about how we can co-evolve with

**[00:36]** to think about how we can co-evolve with general purpose agents and what it will

**[00:38]** general purpose agents and what it will

**[00:38]** general purpose agents and what it will take to make them reliable and aligned

**[00:41]** take to make them reliable and aligned

**[00:41]** take to make them reliable and aligned with our own intelligence. So, I'd like

**[00:43]** with our own intelligence. So, I'd like

**[00:43]** with our own intelligence. So, I'd like to set the set the stage by reminding us

**[00:46]** to set the set the stage by reminding us

**[00:46]** to set the set the stage by reminding us of a fact about the reliability of our

**[00:49]** of a fact about the reliability of our

**[00:49]** of a fact about the reliability of our own minds. We're all hallucinating right

**[00:51]** own minds. We're all hallucinating right

**[00:52]** own minds. We're all hallucinating right now. Our brains don't have direct access

**[00:55]** now. Our brains don't have direct access

**[00:55]** now. Our brains don't have direct access to reality. So they're they're stuck

**[00:57]** to reality. So they're they're stuck

**[00:57]** to reality. So they're they're stuck inside our heads. So they can only

**[00:59]** inside our heads. So they can only

**[00:59]** inside our heads. So they can only really do a few things. They can make


### [01:00 - 02:00]

**[01:01]** really do a few things. They can make

**[01:01]** really do a few things. They can make predictions with their world models.

**[01:04]** predictions with their world models.

**[01:04]** predictions with their world models. They can take in sensory information.

**[01:07]** They can take in sensory information.

**[01:07]** They can take in sensory information. And they can reconcile errors between

**[01:09]** And they can reconcile errors between

**[01:09]** And they can reconcile errors between the two. That's about it. And that's why

**[01:11]** the two. That's about it. And that's why

**[01:11]** the two. That's about it. And that's why neuroscientists call our brains

**[01:13]** neuroscientists call our brains

**[01:13]** neuroscientists call our brains prediction machines and say that

**[01:15]** prediction machines and say that

**[01:15]** prediction machines and say that perception is controlled hallucination.

**[01:19]** perception is controlled hallucination.

**[01:19]** perception is controlled hallucination. Uh, but there's no way, of course, that

**[01:21]** Uh, but there's no way, of course, that

**[01:21]** Uh, but there's no way, of course, that I could be standing up here in front of

**[01:22]** I could be standing up here in front of

**[01:22]** I could be standing up here in front of you if I didn't have my hallucinations

**[01:24]** you if I didn't have my hallucinations

**[01:24]** you if I didn't have my hallucinations under control. The controlled part is

**[01:25]** under control. The controlled part is

**[01:25]** under control. The controlled part is the critical bit. But that's not all

**[01:27]** the critical bit. But that's not all

**[01:27]** the critical bit. But that's not all that's happening right now. If you're

**[01:29]** that's happening right now. If you're

**[01:29]** that's happening right now. If you're understanding my words, then I'm also

**[01:32]** understanding my words, then I'm also

**[01:32]** understanding my words, then I'm also influencing your hallucinations. And

**[01:34]** influencing your hallucinations. And

**[01:34]** influencing your hallucinations. And assuming you do understand my words,

**[01:37]** assuming you do understand my words,

**[01:37]** assuming you do understand my words, then your brain just did something else.

**[01:39]** then your brain just did something else.

**[01:39]** then your brain just did something else. It activated all meanings of the word

**[01:41]** It activated all meanings of the word

**[01:41]** It activated all meanings of the word hallucination, including this one. So

**[01:44]** hallucination, including this one. So

**[01:44]** hallucination, including this one. So today we rely upon hallucinating chat

**[01:47]** today we rely upon hallucinating chat

**[01:47]** today we rely upon hallucinating chat bots for brainstorming, generating

**[01:50]** bots for brainstorming, generating

**[01:50]** bots for brainstorming, generating content and code and images of

**[01:52]** content and code and images of

**[01:52]** content and code and images of themselves like this. But what they

**[01:54]** themselves like this. But what they

**[01:54]** themselves like this. But what they can't yet do is think, learn, or act in

**[01:57]** can't yet do is think, learn, or act in

**[01:57]** can't yet do is think, learn, or act in a reliable general purpose way. And

**[01:59]** a reliable general purpose way. And

**[01:59]** a reliable general purpose way. And we're not satisfied with that because


### [02:00 - 03:00]

**[02:01]** we're not satisfied with that because

**[02:01]** we're not satisfied with that because we've set our sights on building AI that

**[02:04]** we've set our sights on building AI that

**[02:04]** we've set our sights on building AI that more closely resembles our own

**[02:06]** more closely resembles our own

**[02:06]** more closely resembles our own intelligence.

**[02:08]** intelligence.

**[02:08]** intelligence. But what makes our intelligence general?

**[02:11]** But what makes our intelligence general?

**[02:11]** But what makes our intelligence general? Well, one thing we know is that

**[02:12]** Well, one thing we know is that

**[02:12]** Well, one thing we know is that hallucinations are necessary because

**[02:14]** hallucinations are necessary because

**[02:14]** hallucinations are necessary because they allow us to go beyond the data.

**[02:17]** they allow us to go beyond the data.

**[02:17]** they allow us to go beyond the data. They're features rather than bugs of AI

**[02:20]** They're features rather than bugs of AI

**[02:20]** They're features rather than bugs of AI that's flexible like ours. So, we just

**[02:22]** that's flexible like ours. So, we just

**[02:22]** that's flexible like ours. So, we just need to figure out how to control them.

**[02:24]** need to figure out how to control them.

**[02:24]** need to figure out how to control them. I'm going to be drawing a lot of

**[02:26]** I'm going to be drawing a lot of

**[02:26]** I'm going to be drawing a lot of parallels to our intelligence, but I'm

**[02:29]** parallels to our intelligence, but I'm

**[02:29]** parallels to our intelligence, but I'm not saying that we are or should be

**[02:30]** not saying that we are or should be

**[02:30]** not saying that we are or should be building something like a human brain.

**[02:33]** building something like a human brain.

**[02:33]** building something like a human brain. We don't want AI to replace us or

**[02:35]** We don't want AI to replace us or

**[02:35]** We don't want AI to replace us or replicate us. We want it to complement

**[02:38]** replicate us. We want it to complement

**[02:38]** replicate us. We want it to complement us. We want AI plus humans to be greater

**[02:41]** us. We want AI plus humans to be greater

**[02:41]** us. We want AI plus humans to be greater than the sum of our parts. Now, this

**[02:44]** than the sum of our parts. Now, this

**[02:44]** than the sum of our parts. Now, this isn't typically what we think about when

**[02:45]** isn't typically what we think about when

**[02:45]** isn't typically what we think about when we hear AGI. We think about the AI

**[02:48]** we hear AGI. We think about the AI

**[02:48]** we hear AGI. We think about the AI becoming more advanced. But this

**[02:51]** becoming more advanced. But this

**[02:51]** becoming more advanced. But this reflects a category error about how our

**[02:53]** reflects a category error about how our

**[02:54]** reflects a category error about how our intelligence actually works. And that

**[02:56]** intelligence actually works. And that

**[02:56]** intelligence actually works. And that error is that general intelligence can

**[02:59]** error is that general intelligence can

**[02:59]** error is that general intelligence can exist within a thinking machine. So when


### [03:00 - 04:00]

**[03:02]** exist within a thinking machine. So when

**[03:02]** exist within a thinking machine. So when you think about AGI, you probably think

**[03:05]** you think about AGI, you probably think

**[03:05]** you think about AGI, you probably think about something like this. And you might

**[03:07]** about something like this. And you might

**[03:07]** about something like this. And you might think that it's right around the corner,

**[03:09]** think that it's right around the corner,

**[03:09]** think that it's right around the corner, but why does it then feel like agents

**[03:12]** but why does it then feel like agents

**[03:12]** but why does it then feel like agents are closer to something like this?

**[03:19]** The reality is that models can't yet

**[03:19]** The reality is that models can't yet reliably click, type, or scroll. And so

**[03:22]** reliably click, type, or scroll. And so

**[03:22]** reliably click, type, or scroll. And so everyone wants to know how do we make

**[03:25]** everyone wants to know how do we make

**[03:25]** everyone wants to know how do we make agents reliable? That's the question I'm

**[03:27]** agents reliable? That's the question I'm

**[03:27]** agents reliable? That's the question I'm going to focus on today. So first I'll

**[03:29]** going to focus on today. So first I'll

**[03:29]** going to focus on today. So first I'll share our lab's vision for agents.

**[03:33]** share our lab's vision for agents.

**[03:33]** share our lab's vision for agents. Then I will show you how Novaact which

**[03:35]** Then I will show you how Novaact which

**[03:35]** Then I will show you how Novaact which is a research preview of our agent works

**[03:37]** is a research preview of our agent works

**[03:37]** is a research preview of our agent works today. And then finally I'll show you

**[03:39]** today. And then finally I'll show you

**[03:39]** today. And then finally I'll show you how Novaact will evolve and how you are

**[03:42]** how Novaact will evolve and how you are

**[03:42]** how Novaact will evolve and how you are all central to that evolution. So let's

**[03:45]** all central to that evolution. So let's

**[03:45]** all central to that evolution. So let's start with the big picture. Our vision

**[03:47]** start with the big picture. Our vision

**[03:47]** start with the big picture. Our vision for agents is different than the

**[03:49]** for agents is different than the

**[03:49]** for agents is different than the standard vision which reflects this long

**[03:51]** standard vision which reflects this long

**[03:51]** standard vision which reflects this long lineage of thought that has become

**[03:53]** lineage of thought that has become

**[03:53]** lineage of thought that has become folklore. So you all know the story by

**[03:55]** folklore. So you all know the story by

**[03:55]** folklore. So you all know the story by now which is why you probably spotted

**[03:58]** now which is why you probably spotted

**[03:58]** now which is why you probably spotted the hallucination here. The concept of


### [04:00 - 05:00]

**[04:00]** the hallucination here. The concept of

**[04:00]** the hallucination here. The concept of machines that can think like humans

**[04:02]** machines that can think like humans

**[04:02]** machines that can think like humans didn't originate in the 2010s, but in

**[04:05]** didn't originate in the 2010s, but in

**[04:05]** didn't originate in the 2010s, but in 1956 when a group of engineers and

**[04:07]** 1956 when a group of engineers and

**[04:08]** 1956 when a group of engineers and mathematicians set out to build thinking

**[04:10]** mathematicians set out to build thinking

**[04:10]** mathematicians set out to build thinking machines so they could solve

**[04:11]** machines so they could solve

**[04:11]** machines so they could solve intelligence. Of course, you also all

**[04:14]** intelligence. Of course, you also all

**[04:14]** intelligence. Of course, you also all know that these guys didn't solve

**[04:16]** know that these guys didn't solve

**[04:16]** know that these guys didn't solve intelligence, but they did succeed in

**[04:18]** intelligence, but they did succeed in

**[04:18]** intelligence, but they did succeed in founding the field of AI and sparking a

**[04:20]** founding the field of AI and sparking a

**[04:20]** founding the field of AI and sparking a feedback loop that changed how we live

**[04:23]** feedback loop that changed how we live

**[04:23]** feedback loop that changed how we live and work. So first we built more

**[04:25]** and work. So first we built more

**[04:25]** and work. So first we built more powerful computers. Then we connected

**[04:27]** powerful computers. Then we connected

**[04:27]** powerful computers. Then we connected them together to build the internet

**[04:28]** them together to build the internet

**[04:28]** them together to build the internet which enabled more sophisticated

**[04:30]** which enabled more sophisticated

**[04:30]** which enabled more sophisticated learning algorithms. And this made our

**[04:32]** learning algorithms. And this made our

**[04:32]** learning algorithms. And this made our computers even more powerful. And now

**[04:34]** computers even more powerful. And now

**[04:34]** computers even more powerful. And now we're back to aiming for thinking

**[04:36]** we're back to aiming for thinking

**[04:36]** we're back to aiming for thinking machines by another name, artificial

**[04:38]** machines by another name, artificial

**[04:38]** machines by another name, artificial general intelligence or AGI. So the

**[04:41]** general intelligence or AGI. So the

**[04:41]** general intelligence or AGI. So the standard vision is to make AI smarter

**[04:43]** standard vision is to make AI smarter

**[04:43]** standard vision is to make AI smarter and give it more agency. And notice that

**[04:46]** and give it more agency. And notice that

**[04:46]** and give it more agency. And notice that this is about the technology, not us.

**[04:49]** this is about the technology, not us.

**[04:49]** this is about the technology, not us. Well, luckily this wasn't the only

**[04:50]** Well, luckily this wasn't the only

**[04:50]** Well, luckily this wasn't the only historical perspective. Does anybody

**[04:53]** historical perspective. Does anybody

**[04:53]** historical perspective. Does anybody know who this is?

**[04:56]** know who this is?

**[04:56]** know who this is? This is Douglas Angelbart and he

**[04:58]** This is Douglas Angelbart and he

**[04:58]** This is Douglas Angelbart and he invented the computer mouse and the

**[04:59]** invented the computer mouse and the

**[04:59]** invented the computer mouse and the guey. He didn't care so much about


### [05:00 - 06:00]

**[05:02]** guey. He didn't care so much about

**[05:02]** guey. He didn't care so much about thinking machines and solving

**[05:03]** thinking machines and solving

**[05:03]** thinking machines and solving intelligence. What he cared about was

**[05:06]** intelligence. What he cared about was

**[05:06]** intelligence. What he cared about was thinking humans and augmenting our

**[05:08]** thinking humans and augmenting our

**[05:08]** thinking humans and augmenting our intelligence. And he proposed that

**[05:10]** intelligence. And he proposed that

**[05:10]** intelligence. And he proposed that computers could make us smarter. Of

**[05:13]** computers could make us smarter. Of

**[05:13]** computers could make us smarter. Of course, he was absolutely right. So, as

**[05:15]** course, he was absolutely right. So, as

**[05:15]** course, he was absolutely right. So, as computers became pervasive, they also

**[05:17]** computers became pervasive, they also

**[05:17]** computers became pervasive, they also started changing our brains. We began

**[05:20]** started changing our brains. We began

**[05:20]** started changing our brains. We began offloading our computation to devices,

**[05:23]** offloading our computation to devices,

**[05:24]** offloading our computation to devices, distributing our cognition across the

**[05:26]** distributing our cognition across the

**[05:26]** distributing our cognition across the digital environment. And this had the

**[05:28]** digital environment. And this had the

**[05:28]** digital environment. And this had the effect of augmenting our intelligence.

**[05:31]** effect of augmenting our intelligence.

**[05:31]** effect of augmenting our intelligence. Scientists call this technosocial

**[05:33]** Scientists call this technosocial

**[05:33]** Scientists call this technosocial co-evolution. It just means that we

**[05:35]** co-evolution. It just means that we

**[05:35]** co-evolution. It just means that we invent new technologies that then shape

**[05:38]** invent new technologies that then shape

**[05:38]** invent new technologies that then shape us. So here we have two historical

**[05:41]** us. So here we have two historical

**[05:41]** us. So here we have two historical perspectives for the goal of building

**[05:43]** perspectives for the goal of building

**[05:43]** perspectives for the goal of building more advanced intelligence that

**[05:45]** more advanced intelligence that

**[05:45]** more advanced intelligence that resembles our own. We can build AI that

**[05:48]** resembles our own. We can build AI that

**[05:48]** resembles our own. We can build AI that is as smart as or even smarter than us.

**[05:50]** is as smart as or even smarter than us.

**[05:50]** is as smart as or even smarter than us. Or we can build AI that makes us

**[05:53]** Or we can build AI that makes us

**[05:53]** Or we can build AI that makes us smarter. We all believe that more

**[05:55]** smarter. We all believe that more

**[05:55]** smarter. We all believe that more general purpose agents are going to be

**[05:57]** general purpose agents are going to be

**[05:57]** general purpose agents are going to be more useful. But how? Well, things are


### [06:00 - 07:00]

**[06:00]** more useful. But how? Well, things are

**[06:00]** more useful. But how? Well, things are useful when they have one of two

**[06:01]** useful when they have one of two

**[06:01]** useful when they have one of two effects. They can simplify our lives by

**[06:04]** effects. They can simplify our lives by

**[06:04]** effects. They can simplify our lives by allowing us to offload things or they

**[06:06]** allowing us to offload things or they

**[06:06]** allowing us to offload things or they can give us more leverage. And yes,

**[06:09]** can give us more leverage. And yes,

**[06:10]** can give us more leverage. And yes, automation is an engine for

**[06:11]** automation is an engine for

**[06:11]** automation is an engine for augmentation. This is how we become

**[06:13]** augmentation. This is how we become

**[06:13]** augmentation. This is how we become expert at things. We start by paying

**[06:15]** expert at things. We start by paying

**[06:15]** expert at things. We start by paying conscious attention to the details. We

**[06:17]** conscious attention to the details. We

**[06:17]** conscious attention to the details. We practice and then our brain moves things

**[06:19]** practice and then our brain moves things

**[06:19]** practice and then our brain moves things over to our subconscious. Automation

**[06:22]** over to our subconscious. Automation

**[06:22]** over to our subconscious. Automation frees up our attention to focus on other

**[06:24]** frees up our attention to focus on other

**[06:24]** frees up our attention to focus on other things.

**[06:26]** things.

**[06:26]** things. The problem is that automation doesn't

**[06:29]** The problem is that automation doesn't

**[06:29]** The problem is that automation doesn't always lead to augmentation. Sometimes

**[06:31]** always lead to augmentation. Sometimes

**[06:31]** always lead to augmentation. Sometimes it even comes at a cost. How many hours

**[06:33]** it even comes at a cost. How many hours

**[06:33]** it even comes at a cost. How many hours have we lost to scrolling? Or how many

**[06:35]** have we lost to scrolling? Or how many

**[06:35]** have we lost to scrolling? Or how many echo chambers have we been trapped

**[06:37]** echo chambers have we been trapped

**[06:37]** echo chambers have we been trapped within? How many times has autocomplete

**[06:40]** within? How many times has autocomplete

**[06:40]** within? How many times has autocomplete just shut down our thinking? So this is

**[06:42]** just shut down our thinking? So this is

**[06:42]** just shut down our thinking? So this is how algorithms can reduce our agency.

**[06:45]** how algorithms can reduce our agency.

**[06:45]** how algorithms can reduce our agency. And it's how increasingly intelligent

**[06:47]** And it's how increasingly intelligent

**[06:47]** And it's how increasingly intelligent agents might cause more problems than

**[06:49]** agents might cause more problems than

**[06:50]** agents might cause more problems than they solve. But if we have precise

**[06:52]** they solve. But if we have precise

**[06:52]** they solve. But if we have precise control and we actively tailor these

**[06:54]** control and we actively tailor these

**[06:54]** control and we actively tailor these systems the way that we want, then we

**[06:56]** systems the way that we want, then we

**[06:56]** systems the way that we want, then we can actually increase our agency. And

**[06:59]** can actually increase our agency. And

**[06:59]** can actually increase our agency. And this is the crossroads in front of us.


### [07:00 - 08:00]

**[07:01]** this is the crossroads in front of us.

**[07:01]** this is the crossroads in front of us. We can continue to make AI smarter and

**[07:04]** We can continue to make AI smarter and

**[07:04]** We can continue to make AI smarter and give it more agency. uh we can focus on

**[07:07]** give it more agency. uh we can focus on

**[07:07]** give it more agency. uh we can focus on unhobling the AI as it's fashionable to

**[07:09]** unhobling the AI as it's fashionable to

**[07:09]** unhobling the AI as it's fashionable to say, but this doesn't guarantee that it

**[07:11]** say, but this doesn't guarantee that it

**[07:11]** say, but this doesn't guarantee that it will be useful to us. It just guarantees

**[07:13]** will be useful to us. It just guarantees

**[07:13]** will be useful to us. It just guarantees that we'll continue to see a lot of the

**[07:15]** that we'll continue to see a lot of the

**[07:15]** that we'll continue to see a lot of the same patterns that we've seen in tech

**[07:17]** same patterns that we've seen in tech

**[07:17]** same patterns that we've seen in tech recently. And that's why that our vision

**[07:19]** recently. And that's why that our vision

**[07:19]** recently. And that's why that our vision is to build AI that makes us smarter and

**[07:22]** is to build AI that makes us smarter and

**[07:22]** is to build AI that makes us smarter and gives us more agency to build AI that

**[07:25]** gives us more agency to build AI that

**[07:25]** gives us more agency to build AI that unhobles humans. So, how do we do that?

**[07:28]** unhobles humans. So, how do we do that?

**[07:28]** unhobles humans. So, how do we do that? Well, in these early stages, we need to

**[07:31]** Well, in these early stages, we need to

**[07:31]** Well, in these early stages, we need to do two things. We need to meet the

**[07:33]** do two things. We need to meet the

**[07:33]** do two things. We need to meet the models where they are and meet the

**[07:36]** models where they are and meet the

**[07:36]** models where they are and meet the builders where they are. So all of you

**[07:38]** builders where they are. So all of you

**[07:38]** builders where they are. So all of you have a million ideas about what you want

**[07:40]** have a million ideas about what you want

**[07:40]** have a million ideas about what you want to do with agents. We have to make it

**[07:41]** to do with agents. We have to make it

**[07:41]** to do with agents. We have to make it frictionless for you to get started.

**[07:45]** frictionless for you to get started.

**[07:45]** frictionless for you to get started. And Nova Act does these two things.

**[07:48]** And Nova Act does these two things.

**[07:48]** And Nova Act does these two things. We're building a future where the atomic

**[07:51]** We're building a future where the atomic

**[07:51]** We're building a future where the atomic unit of all digital interactions will be

**[07:53]** unit of all digital interactions will be

**[07:53]** unit of all digital interactions will be an agent call. The big obstacle is that

**[07:56]** an agent call. The big obstacle is that

**[07:56]** an agent call. The big obstacle is that we still only have some infrastructure

**[07:58]** we still only have some infrastructure

**[07:58]** we still only have some infrastructure for APIs.


### [08:00 - 09:00]

**[08:00]** for APIs.

**[08:00]** for APIs. Most websites are built for visual UIs

**[08:03]** Most websites are built for visual UIs

**[08:03]** Most websites are built for visual UIs and so since most websites lack APIs, we

**[08:06]** and so since most websites lack APIs, we

**[08:06]** and so since most websites lack APIs, we need to use the browser itself as a tool

**[08:09]** need to use the browser itself as a tool

**[08:09]** need to use the browser itself as a tool and that's why we've trained a model of

**[08:12]** and that's why we've trained a model of

**[08:12]** and that's why we've trained a model of uh Amazon's foundation model Nova to be

**[08:14]** uh Amazon's foundation model Nova to be

**[08:14]** uh Amazon's foundation model Nova to be really good at UIs to interact with UIs

**[08:17]** really good at UIs to interact with UIs

**[08:17]** really good at UIs to interact with UIs like we do. Nova Act combines this model

**[08:21]** like we do. Nova Act combines this model

**[08:21]** like we do. Nova Act combines this model with an SDK to allow developers to build

**[08:24]** with an SDK to allow developers to build

**[08:24]** with an SDK to allow developers to build and deploy agents. All you have to do is

**[08:27]** and deploy agents. All you have to do is

**[08:27]** and deploy agents. All you have to do is make an act call, which translates

**[08:29]** make an act call, which translates

**[08:29]** make an act call, which translates action uh natural language into actions

**[08:31]** action uh natural language into actions

**[08:31]** action uh natural language into actions on the screen. And I'm going to show you

**[08:34]** on the screen. And I'm going to show you

**[08:34]** on the screen. And I'm going to show you a demo here where my teammate Carolyn uh

**[08:36]** a demo here where my teammate Carolyn uh

**[08:36]** a demo here where my teammate Carolyn uh will show you how you can use Nova Act.

**[08:44]** Nova Act to find our dream apartment.

**[08:44]** Nova Act to find our dream apartment. We're searching for a two-bedroom, one

**[08:46]** We're searching for a two-bedroom, one

**[08:46]** We're searching for a two-bedroom, one bath in Redwood City. Here we've given

**[08:49]** bath in Redwood City. Here we've given

**[08:49]** bath in Redwood City. Here we've given our first act call to the agent. It's

**[08:51]** our first act call to the agent. It's

**[08:51]** our first act call to the agent. It's going to break down how to complete this

**[08:53]** going to break down how to complete this

**[08:53]** going to break down how to complete this task, considering the outcome of each

**[08:54]** task, considering the outcome of each

**[08:54]** task, considering the outcome of each step as it plans the next one. Behind

**[08:57]** step as it plans the next one. Behind

**[08:57]** step as it plans the next one. Behind the scenes, this is all powered by a

**[08:59]** the scenes, this is all powered by a

**[08:59]** the scenes, this is all powered by a specialized version of Amazon Nova


### [09:00 - 10:00]

**[09:01]** specialized version of Amazon Nova

**[09:01]** specialized version of Amazon Nova trained for high reliability on UI

**[09:03]** trained for high reliability on UI

**[09:03]** trained for high reliability on UI tasks.

**[09:09]** And next, I'm going to show you my

**[09:09]** And next, I'm going to show you my teammate Fjord, who will describe how

**[09:11]** teammate Fjord, who will describe how

**[09:11]** teammate Fjord, who will describe how you can uh do even more things with

**[09:13]** you can uh do even more things with

**[09:13]** you can uh do even more things with Python integrations. All right, we see a

**[09:16]** Python integrations. All right, we see a

**[09:16]** Python integrations. All right, we see a bunch of rentals on the screen. So,

**[09:17]** bunch of rentals on the screen. So,

**[09:17]** bunch of rentals on the screen. So, let's grab them using a structured

**[09:19]** let's grab them using a structured

**[09:19]** let's grab them using a structured extract. We'll define a pyantic class

**[09:21]** extract. We'll define a pyantic class

**[09:21]** extract. We'll define a pyantic class and ask the agent to return JSON

**[09:23]** and ask the agent to return JSON

**[09:23]** and ask the agent to return JSON matching that schema.

**[09:27]** matching that schema.

**[09:27]** matching that schema. For my commute, I want to know the

**[09:28]** For my commute, I want to know the

**[09:28]** For my commute, I want to know the biking distance to the nearest Cal Train

**[09:30]** biking distance to the nearest Cal Train

**[09:30]** biking distance to the nearest Cal Train station for each of these results. Let's

**[09:32]** station for each of these results. Let's

**[09:32]** station for each of these results. Let's define a helper function. Add biking

**[09:34]** define a helper function. Add biking

**[09:34]** define a helper function. Add biking distance will take in an apartment and

**[09:36]** distance will take in an apartment and

**[09:36]** distance will take in an apartment and then use Google Maps to calculate the

**[09:38]** then use Google Maps to calculate the

**[09:38]** then use Google Maps to calculate the distance.

**[09:41]** distance.

**[09:41]** distance. Now, I don't want to wait for each of

**[09:42]** Now, I don't want to wait for each of

**[09:42]** Now, I don't want to wait for each of these searches to complete one by one.

**[09:44]** these searches to complete one by one.

**[09:44]** these searches to complete one by one. So, let's do this in parallel. Since

**[09:45]** So, let's do this in parallel. Since

**[09:45]** So, let's do this in parallel. Since this is Python, we can just use a thread

**[09:47]** this is Python, we can just use a thread

**[09:47]** this is Python, we can just use a thread pool to spin up multiple browsers, one

**[09:49]** pool to spin up multiple browsers, one

**[09:49]** pool to spin up multiple browsers, one for each address.

**[09:52]** for each address.

**[09:52]** for each address. Finally, I'll use pandas to turn all

**[09:54]** Finally, I'll use pandas to turn all

**[09:54]** Finally, I'll use pandas to turn all these results into a table and sort by

**[09:56]** these results into a table and sort by

**[09:56]** these results into a table and sort by biking time to the cow train station.

**[09:59]** biking time to the cow train station.

**[09:59]** biking time to the cow train station. We've checked this script into the


### [10:00 - 11:00]

**[10:01]** We've checked this script into the

**[10:01]** We've checked this script into the samples folder of our GitHub repo. So,

**[10:03]** samples folder of our GitHub repo. So,

**[10:03]** samples folder of our GitHub repo. So, feel free to give it a try.

**[10:06]** feel free to give it a try.

**[10:06]** feel free to give it a try. So, we've made it really easy to get

**[10:08]** So, we've made it really easy to get

**[10:08]** So, we've made it really easy to get started. It's just three lines of code.

**[10:11]** started. It's just three lines of code.

**[10:11]** started. It's just three lines of code. And under the hood, we're constantly

**[10:12]** And under the hood, we're constantly

**[10:12]** And under the hood, we're constantly making improvements to our model and

**[10:15]** making improvements to our model and

**[10:15]** making improvements to our model and shipping those every few weeks. And this

**[10:17]** shipping those every few weeks. And this

**[10:17]** shipping those every few weeks. And this is important. Because even the building

**[10:19]** is important. Because even the building

**[10:19]** is important. Because even the building blocks of computer use are deceptively

**[10:21]** blocks of computer use are deceptively

**[10:21]** blocks of computer use are deceptively challenging. Here's why. This is the

**[10:24]** challenging. Here's why. This is the

**[10:24]** challenging. Here's why. This is the Amazon website. And let me ask you, what

**[10:26]** Amazon website. And let me ask you, what

**[10:26]** Amazon website. And let me ask you, what do these icons mean? We typically take

**[10:29]** do these icons mean? We typically take

**[10:29]** do these icons mean? We typically take for granted that even if we've never

**[10:30]** for granted that even if we've never

**[10:30]** for granted that even if we've never seen them before, we can easily

**[10:31]** seen them before, we can easily

**[10:32]** seen them before, we can easily interpret them. Uh and and when we

**[10:33]** interpret them. Uh and and when we

**[10:33]** interpret them. Uh and and when we can't, there are usually plenty of cues

**[10:35]** can't, there are usually plenty of cues

**[10:35]** can't, there are usually plenty of cues for us to know what they mean. Now,

**[10:37]** for us to know what they mean. Now,

**[10:37]** for us to know what they mean. Now, Amazon actually labels these, but in

**[10:39]** Amazon actually labels these, but in

**[10:39]** Amazon actually labels these, but in many contexts, the icons are not

**[10:41]** many contexts, the icons are not

**[10:41]** many contexts, the icons are not labeled, and we couldn't possibly teach

**[10:43]** labeled, and we couldn't possibly teach

**[10:43]** labeled, and we couldn't possibly teach our agent all of the different icons,

**[10:45]** our agent all of the different icons,

**[10:45]** our agent all of the different icons, let alone all of the different useful

**[10:47]** let alone all of the different useful

**[10:47]** let alone all of the different useful ways that it could use a computer. So,

**[10:49]** ways that it could use a computer. So,

**[10:49]** ways that it could use a computer. So, we have to let our agent explore and

**[10:51]** we have to let our agent explore and

**[10:51]** we have to let our agent explore and learn with RL. And it's really

**[10:53]** learn with RL. And it's really

**[10:53]** learn with RL. And it's really fascinating to think about how RL will

**[10:56]** fascinating to think about how RL will

**[10:56]** fascinating to think about how RL will enable these agents to discover how to

**[10:58]** enable these agents to discover how to

**[10:58]** enable these agents to discover how to use computers in entirely new ways. And


### [11:00 - 12:00]

**[11:01]** use computers in entirely new ways. And

**[11:01]** use computers in entirely new ways. And that's okay because we want them to be

**[11:02]** that's okay because we want them to be

**[11:02]** that's okay because we want them to be complimentary to us. But if we're going

**[11:04]** complimentary to us. But if we're going

**[11:04]** complimentary to us. But if we're going to diverge in our computer use methods,

**[11:06]** to diverge in our computer use methods,

**[11:06]** to diverge in our computer use methods, then it's really critical that our

**[11:08]** then it's really critical that our

**[11:08]** then it's really critical that our agents perception of the digital world

**[11:10]** agents perception of the digital world

**[11:10]** agents perception of the digital world is aligned with our own. And that's not

**[11:14]** is aligned with our own. And that's not

**[11:14]** is aligned with our own. And that's not what most agents can can do right now.

**[11:16]** what most agents can can do right now.

**[11:16]** what most agents can can do right now. So current agents are LLM rappers that

**[11:20]** So current agents are LLM rappers that

**[11:20]** So current agents are LLM rappers that function as readonly assistants. They

**[11:22]** function as readonly assistants. They

**[11:22]** function as readonly assistants. They can use tools and some of them are

**[11:24]** can use tools and some of them are

**[11:24]** can use tools and some of them are getting really good at code, but they

**[11:26]** getting really good at code, but they

**[11:26]** getting really good at code, but they don't have an environment to ground

**[11:28]** don't have an environment to ground

**[11:28]** don't have an environment to ground their interactions. They lack a world

**[11:30]** their interactions. They lack a world

**[11:30]** their interactions. They lack a world model. Computer use agents are

**[11:33]** model. Computer use agents are

**[11:33]** model. Computer use agents are different. They can see pixels and

**[11:36]** different. They can see pixels and

**[11:36]** different. They can see pixels and interact with UIs just like us. So you

**[11:38]** interact with UIs just like us. So you

**[11:38]** interact with UIs just like us. So you can think of them as kind of having this

**[11:40]** can think of them as kind of having this

**[11:40]** can think of them as kind of having this early form of embodiment. Now we're not

**[11:43]** early form of embodiment. Now we're not

**[11:43]** early form of embodiment. Now we're not the only ones working on computer use

**[11:45]** the only ones working on computer use

**[11:45]** the only ones working on computer use agents, but our approach is different.

**[11:48]** agents, but our approach is different.

**[11:48]** agents, but our approach is different. We are focusing on making the smallest

**[11:51]** We are focusing on making the smallest

**[11:51]** We are focusing on making the smallest units of interaction reliable and giving

**[11:52]** units of interaction reliable and giving

**[11:52]** units of interaction reliable and giving you granular control over them. Just

**[11:55]** you granular control over them. Just

**[11:55]** you granular control over them. Just like you can string together words to

**[11:57]** like you can string together words to

**[11:57]** like you can string together words to generate infinite combinations of

**[11:59]** generate infinite combinations of


### [12:00 - 13:00]

**[12:00]** generate infinite combinations of meaning, you can string together atomic

**[12:02]** meaning, you can string together atomic

**[12:02]** meaning, you can string together atomic actions to generate increasingly complex

**[12:04]** actions to generate increasingly complex

**[12:04]** actions to generate increasingly complex workflows.

**[12:06]** workflows.

**[12:06]** workflows. Now, grounding our interactions in a

**[12:08]** Now, grounding our interactions in a

**[12:08]** Now, grounding our interactions in a shared environment uh is necessary for

**[12:11]** shared environment uh is necessary for

**[12:11]** shared environment uh is necessary for building aligned generalpurpose agents,

**[12:13]** building aligned generalpurpose agents,

**[12:13]** building aligned generalpurpose agents, but it's not sufficient. Computer use

**[12:16]** but it's not sufficient. Computer use

**[12:16]** but it's not sufficient. Computer use agents will need something else to be

**[12:18]** agents will need something else to be

**[12:18]** agents will need something else to be able to really reliably understand our

**[12:20]** able to really reliably understand our

**[12:20]** able to really reliably understand our higher level goals. So how will NOVA act

**[12:24]** higher level goals. So how will NOVA act

**[12:24]** higher level goals. So how will NOVA act need to evolve to make us smarter and

**[12:26]** need to evolve to make us smarter and

**[12:26]** need to evolve to make us smarter and give us more agency? In other words,

**[12:28]** give us more agency? In other words,

**[12:28]** give us more agency? In other words, what is it that makes our intelligence

**[12:30]** what is it that makes our intelligence

**[12:30]** what is it that makes our intelligence reliable and uh flexible and general

**[12:33]** reliable and uh flexible and general

**[12:33]** reliable and uh flexible and general purpose? Well, it turns out that over

**[12:36]** purpose? Well, it turns out that over

**[12:36]** purpose? Well, it turns out that over the past decades, as engineers were

**[12:39]** the past decades, as engineers were

**[12:39]** the past decades, as engineers were building more advanced intelligence,

**[12:41]** building more advanced intelligence,

**[12:41]** building more advanced intelligence, scientists were learning about how it

**[12:43]** scientists were learning about how it

**[12:43]** scientists were learning about how it works. And what they learned was that

**[12:45]** works. And what they learned was that

**[12:45]** works. And what they learned was that this isn't the whole story. It's just

**[12:48]** this isn't the whole story. It's just

**[12:48]** this isn't the whole story. It's just the most recent uh story of our

**[12:51]** the most recent uh story of our

**[12:51]** the most recent uh story of our co-evolution with technology. So

**[12:53]** co-evolution with technology. So

**[12:53]** co-evolution with technology. So computers co-evolving with computers is

**[12:55]** computers co-evolving with computers is

**[12:55]** computers co-evolving with computers is is this thing that we're fixated on. But

**[12:58]** is this thing that we're fixated on. But

**[12:58]** is this thing that we're fixated on. But the story goes back a lot longer. And


### [13:00 - 14:00]

**[13:01]** the story goes back a lot longer. And

**[13:01]** the story goes back a lot longer. And Engelbart actually hinted at this. He

**[13:03]** Engelbart actually hinted at this. He

**[13:03]** Engelbart actually hinted at this. He said in a very real sense as represented

**[13:06]** said in a very real sense as represented

**[13:06]** said in a very real sense as represented by the steady evolution of our

**[13:08]** by the steady evolution of our

**[13:08]** by the steady evolution of our augmentation means the development of

**[13:09]** augmentation means the development of

**[13:10]** augmentation means the development of artificial intelligence has been going

**[13:11]** artificial intelligence has been going

**[13:11]** artificial intelligence has been going on for centuries. Now he was correct but

**[13:14]** on for centuries. Now he was correct but

**[13:14]** on for centuries. Now he was correct but it was actually going on for a lot

**[13:15]** it was actually going on for a lot

**[13:15]** it was actually going on for a lot longer than that. So let me take you

**[13:17]** longer than that. So let me take you

**[13:17]** longer than that. So let me take you back to the beginning. Around six

**[13:19]** back to the beginning. Around six

**[13:19]** back to the beginning. Around six million years ago, the environment

**[13:21]** million years ago, the environment

**[13:21]** million years ago, the environment changed for our ancestors and they had

**[13:23]** changed for our ancestors and they had

**[13:23]** changed for our ancestors and they had exactly two options. They could solve

**[13:26]** exactly two options. They could solve

**[13:26]** exactly two options. They could solve intelligence or go extinct. And the ones

**[13:29]** intelligence or go extinct. And the ones

**[13:29]** intelligence or go extinct. And the ones that solved intelligence did so through

**[13:32]** that solved intelligence did so through

**[13:32]** that solved intelligence did so through a feedback loop that changed our social

**[13:34]** a feedback loop that changed our social

**[13:34]** a feedback loop that changed our social cognition. This should look familiar.

**[13:37]** cognition. This should look familiar.

**[13:37]** cognition. This should look familiar. First, our brains got bigger. Then we

**[13:40]** First, our brains got bigger. Then we

**[13:40]** First, our brains got bigger. Then we connected them together, which enabled

**[13:42]** connected them together, which enabled

**[13:42]** connected them together, which enabled us to further fine-tune into social

**[13:44]** us to further fine-tune into social

**[13:44]** us to further fine-tune into social information. And this made our brains

**[13:46]** information. And this made our brains

**[13:46]** information. And this made our brains even bigger. But now you know that this

**[13:49]** even bigger. But now you know that this

**[13:49]** even bigger. But now you know that this scaling part is only half of the story.

**[13:51]** scaling part is only half of the story.

**[13:52]** scaling part is only half of the story. The other half had to do with how we all

**[13:54]** The other half had to do with how we all

**[13:54]** The other half had to do with how we all got smarter. So we offloaded our

**[13:56]** got smarter. So we offloaded our

**[13:56]** got smarter. So we offloaded our computation to each other's minds and

**[13:59]** computation to each other's minds and

**[13:59]** computation to each other's minds and distributed our cognition across the


### [14:00 - 15:00]

**[14:01]** distributed our cognition across the

**[14:01]** distributed our cognition across the social environment. And this had the

**[14:03]** social environment. And this had the

**[14:03]** social environment. And this had the effect of augmenting our intelligence.

**[14:06]** effect of augmenting our intelligence.

**[14:06]** effect of augmenting our intelligence. So scientists call the thing that we got

**[14:09]** So scientists call the thing that we got

**[14:09]** So scientists call the thing that we got better at through these flywheels

**[14:11]** better at through these flywheels

**[14:11]** better at through these flywheels representational alignment. We figured

**[14:13]** representational alignment. We figured

**[14:13]** representational alignment. We figured out how to reproduce the contents of our

**[14:16]** out how to reproduce the contents of our

**[14:16]** out how to reproduce the contents of our minds to better cooperate. The key

**[14:19]** minds to better cooperate. The key

**[14:19]** minds to better cooperate. The key insight here is that the history of

**[14:21]** insight here is that the history of

**[14:21]** insight here is that the history of upgrading our intelligence didn't start

**[14:23]** upgrading our intelligence didn't start

**[14:23]** upgrading our intelligence didn't start with computers. It started with an

**[14:25]** with computers. It started with an

**[14:25]** with computers. It started with an evolutionary adaptation that allowed us

**[14:28]** evolutionary adaptation that allowed us

**[14:28]** evolutionary adaptation that allowed us to use each other's minds as tools. Let

**[14:31]** to use each other's minds as tools. Let

**[14:31]** to use each other's minds as tools. Let me say that in another way. The thing

**[14:32]** me say that in another way. The thing

**[14:32]** me say that in another way. The thing that makes our intelligence general and

**[14:34]** that makes our intelligence general and

**[14:34]** that makes our intelligence general and flexible is inferring the existence of

**[14:37]** flexible is inferring the existence of

**[14:37]** flexible is inferring the existence of other minds. This means that this is

**[14:40]** other minds. This means that this is

**[14:40]** other minds. This means that this is general intelligence. This can be

**[14:42]** general intelligence. This can be

**[14:42]** general intelligence. This can be general intelligence. This could

**[14:45]** general intelligence. This could

**[14:46]** general intelligence. This could possibly be general intelligence, but

**[14:48]** possibly be general intelligence, but

**[14:48]** possibly be general intelligence, but it's not uh there's no reason to expect

**[14:49]** it's not uh there's no reason to expect

**[14:50]** it's not uh there's no reason to expect that it will be aligned. And this is not

**[14:52]** that it will be aligned. And this is not

**[14:52]** that it will be aligned. And this is not general intelligence. Intelligence of

**[14:55]** general intelligence. Intelligence of

**[14:55]** general intelligence. Intelligence of the variety that humans have can't exist

**[14:58]** the variety that humans have can't exist

**[14:58]** the variety that humans have can't exist in a vacuum. It doesn't exist in


### [15:00 - 16:00]

**[15:00]** in a vacuum. It doesn't exist in

**[15:00]** in a vacuum. It doesn't exist in individual humans. It won't exist in

**[15:02]** individual humans. It won't exist in

**[15:02]** individual humans. It won't exist in individual models. Instead, general

**[15:05]** individual models. Instead, general

**[15:05]** individual models. Instead, general intelligence emerges through our

**[15:06]** intelligence emerges through our

**[15:06]** intelligence emerges through our interactions. It's social, distributed,

**[15:09]** interactions. It's social, distributed,

**[15:09]** interactions. It's social, distributed, ever evolving. And that means that we

**[15:11]** ever evolving. And that means that we

**[15:11]** ever evolving. And that means that we need to measure the interactions and

**[15:13]** need to measure the interactions and

**[15:13]** need to measure the interactions and optimize for the interactions that we

**[15:15]** optimize for the interactions that we

**[15:15]** optimize for the interactions that we have with agents. We can't just measure

**[15:17]** have with agents. We can't just measure

**[15:18]** have with agents. We can't just measure model capabilities or things like time

**[15:20]** model capabilities or things like time

**[15:20]** model capabilities or things like time spent on platform. We have to measure

**[15:22]** spent on platform. We have to measure

**[15:22]** spent on platform. We have to measure human things like creativity,

**[15:24]** human things like creativity,

**[15:24]** human things like creativity, productivity, strategic thinking, even

**[15:27]** productivity, strategic thinking, even

**[15:27]** productivity, strategic thinking, even things like states of flow.

**[15:29]** things like states of flow.

**[15:29]** things like states of flow. So let's take a closer look at this

**[15:31]** So let's take a closer look at this

**[15:31]** So let's take a closer look at this evolutionary adaptation. Any ideas as to

**[15:34]** evolutionary adaptation. Any ideas as to

**[15:34]** evolutionary adaptation. Any ideas as to what it was?

**[15:36]** what it was?

**[15:36]** what it was? It was language. So, language co-evolved

**[15:39]** It was language. So, language co-evolved

**[15:39]** It was language. So, language co-evolved with our models of minds in yet another

**[15:42]** with our models of minds in yet another

**[15:42]** with our models of minds in yet another flywheel that integrated our systems for

**[15:45]** flywheel that integrated our systems for

**[15:45]** flywheel that integrated our systems for communication and representation. And it

**[15:47]** communication and representation. And it

**[15:47]** communication and representation. And it did this by being both a cause and an

**[15:49]** did this by being both a cause and an

**[15:49]** did this by being both a cause and an effect of modeling our minds. Let's

**[15:52]** effect of modeling our minds. Let's

**[15:52]** effect of modeling our minds. Let's break that down. We've got our models

**[15:54]** break that down. We've got our models

**[15:54]** break that down. We've got our models and our communicative interfaces. And

**[15:56]** and our communicative interfaces. And

**[15:56]** and our communicative interfaces. And then here's how they became integrated.

**[15:58]** then here's how they became integrated.

**[15:58]** then here's how they became integrated. As we fine-tuned into social cues, our


### [16:00 - 17:00]

**[16:02]** As we fine-tuned into social cues, our

**[16:02]** As we fine-tuned into social cues, our models of mind became more stable. This

**[16:05]** models of mind became more stable. This

**[16:05]** models of mind became more stable. This advanced our language and our language

**[16:07]** advanced our language and our language

**[16:07]** advanced our language and our language made our models of mind even more

**[16:09]** made our models of mind even more

**[16:09]** made our models of mind even more stable. And then here's the big bang

**[16:12]** stable. And then here's the big bang

**[16:12]** stable. And then here's the big bang moment for our intelligence.

**[16:14]** moment for our intelligence.

**[16:14]** moment for our intelligence. Our models of mind became the original

**[16:16]** Our models of mind became the original

**[16:16]** Our models of mind became the original placeholder concept, the first variable

**[16:19]** placeholder concept, the first variable

**[16:19]** placeholder concept, the first variable for being able to represent any concept.

**[16:22]** for being able to represent any concept.

**[16:22]** for being able to represent any concept. That right there is generalization. So

**[16:25]** That right there is generalization. So

**[16:25]** That right there is generalization. So you might be thinking, but is this

**[16:26]** you might be thinking, but is this

**[16:26]** you might be thinking, but is this different from other languages? And the

**[16:28]** different from other languages? And the

**[16:28]** different from other languages? And the answer is yes. Other communication

**[16:30]** answer is yes. Other communication

**[16:30]** answer is yes. Other communication systems don't have models of mind.

**[16:34]** systems don't have models of mind.

**[16:34]** systems don't have models of mind. Programming languages don't negotiate

**[16:36]** Programming languages don't negotiate

**[16:36]** Programming languages don't negotiate meaning in real time. This is why code

**[16:37]** meaning in real time. This is why code

**[16:37]** meaning in real time. This is why code is so easily verifiable. And LLMs don't

**[16:41]** is so easily verifiable. And LLMs don't

**[16:41]** is so easily verifiable. And LLMs don't understand language. What do we mean

**[16:43]** understand language. What do we mean

**[16:43]** understand language. What do we mean they don't understand language? They

**[16:45]** they don't understand language? They

**[16:45]** they don't understand language? They don't understand that words refer to

**[16:47]** don't understand that words refer to

**[16:47]** don't understand that words refer to things that minds make up. So when we

**[16:49]** things that minds make up. So when we

**[16:49]** things that minds make up. So when we ask what's in a word, the answer is

**[16:52]** ask what's in a word, the answer is

**[16:52]** ask what's in a word, the answer is quite literally a mind.

**[16:54]** quite literally a mind.

**[16:54]** quite literally a mind. So language was so immensely useful that

**[16:57]** So language was so immensely useful that

**[16:57]** So language was so immensely useful that it triggered a whole new series of

**[16:59]** it triggered a whole new series of

**[16:59]** it triggered a whole new series of flywheels that scientists call cognitive


### [17:00 - 18:00]

**[17:02]** flywheels that scientists call cognitive

**[17:02]** flywheels that scientists call cognitive technologies. Each one is a foundation

**[17:04]** technologies. Each one is a foundation

**[17:04]** technologies. Each one is a foundation for the next and each one allows us to

**[17:07]** for the next and each one allows us to

**[17:07]** for the next and each one allows us to have increasingly abstract thoughts.

**[17:09]** have increasingly abstract thoughts.

**[17:09]** have increasingly abstract thoughts. They become useful by evolving within

**[17:12]** They become useful by evolving within

**[17:12]** They become useful by evolving within communities. So early commu computers

**[17:15]** communities. So early commu computers

**[17:15]** communities. So early commu computers were not very useful to many people.

**[17:17]** were not very useful to many people.

**[17:17]** were not very useful to many people. They didn't have great interfaces. But

**[17:19]** They didn't have great interfaces. But

**[17:19]** They didn't have great interfaces. But Engelbart changed this. Now computers

**[17:22]** Engelbart changed this. Now computers

**[17:22]** Engelbart changed this. Now computers are getting in our way. We've never had

**[17:25]** are getting in our way. We've never had

**[17:25]** are getting in our way. We've never had the world's information so easily

**[17:27]** the world's information so easily

**[17:27]** the world's information so easily accessible, but also we've never had

**[17:29]** accessible, but also we've never had

**[17:29]** accessible, but also we've never had more distractions. And agents can help

**[17:32]** more distractions. And agents can help

**[17:32]** more distractions. And agents can help fix this. They can do the repetitive

**[17:35]** fix this. They can do the repetitive

**[17:35]** fix this. They can do the repetitive stuff for us. They can learn from us and

**[17:37]** stuff for us. They can learn from us and

**[17:37]** stuff for us. They can learn from us and redistribute our skills across

**[17:39]** redistribute our skills across

**[17:39]** redistribute our skills across communities. And they can teach us new

**[17:41]** communities. And they can teach us new

**[17:41]** communities. And they can teach us new things when they discover new knowledge.

**[17:43]** things when they discover new knowledge.

**[17:43]** things when they discover new knowledge. In essence, agents can become our

**[17:45]** In essence, agents can become our

**[17:45]** In essence, agents can become our collective subconscious. But we need to

**[17:48]** collective subconscious. But we need to

**[17:48]** collective subconscious. But we need to build them in a way that reflects this

**[17:50]** build them in a way that reflects this

**[17:50]** build them in a way that reflects this larger pattern. So collectively these

**[17:54]** larger pattern. So collectively these

**[17:54]** larger pattern. So collectively these tools for thought stabilize our

**[17:56]** tools for thought stabilize our

**[17:56]** tools for thought stabilize our thinking,

**[17:58]** thinking,

**[17:58]** thinking, reorganize our brains and control our


### [18:00 - 19:00]

**[18:00]** reorganize our brains and control our

**[18:00]** reorganize our brains and control our hallucinations. How do they control our

**[18:03]** hallucinations. How do they control our

**[18:03]** hallucinations. How do they control our hallucinations? Well, they direct our

**[18:05]** hallucinations? Well, they direct our

**[18:05]** hallucinations? Well, they direct our attention to the same things in the

**[18:07]** attention to the same things in the

**[18:07]** attention to the same things in the environment. They pick out the relevant

**[18:09]** environment. They pick out the relevant

**[18:09]** environment. They pick out the relevant signals and the noise and then we

**[18:11]** signals and the noise and then we

**[18:11]** signals and the noise and then we stabilize these signals to co-create

**[18:13]** stabilize these signals to co-create

**[18:13]** stabilize these signals to co-create these shared world models. And what does

**[18:16]** these shared world models. And what does

**[18:16]** these shared world models. And what does that sound like? It sounds like what

**[18:18]** that sound like? It sounds like what

**[18:18]** that sound like? It sounds like what we're building. So another way of

**[18:20]** we're building. So another way of

**[18:20]** we're building. So another way of thinking about Nova Act is as the

**[18:22]** thinking about Nova Act is as the

**[18:22]** thinking about Nova Act is as the primitives for a cognitive technology

**[18:24]** primitives for a cognitive technology

**[18:24]** primitives for a cognitive technology that aligns agents and humans

**[18:26]** that aligns agents and humans

**[18:26]** that aligns agents and humans representations. And just like with

**[18:28]** representations. And just like with

**[18:28]** representations. And just like with other cognitive technologies, early

**[18:31]** other cognitive technologies, early

**[18:31]** other cognitive technologies, early agents will need to uh evolve in diverse

**[18:35]** agents will need to uh evolve in diverse

**[18:35]** agents will need to uh evolve in diverse communities. So that's where all of you

**[18:37]** communities. So that's where all of you

**[18:37]** communities. So that's where all of you come in. But reliability isn't just

**[18:40]** come in. But reliability isn't just

**[18:40]** come in. But reliability isn't just about clicking in the same place every

**[18:42]** about clicking in the same place every

**[18:42]** about clicking in the same place every time. It's about understanding the

**[18:43]** time. It's about understanding the

**[18:43]** time. It's about understanding the larger goal. So to return to our big

**[18:46]** larger goal. So to return to our big

**[18:46]** larger goal. So to return to our big question, how do we make agents

**[18:48]** question, how do we make agents

**[18:48]** question, how do we make agents reliable? Eventually they're going to

**[18:50]** reliable? Eventually they're going to

**[18:50]** reliable? Eventually they're going to need models of our minds. So the next

**[18:53]** need models of our minds. So the next

**[18:54]** need models of our minds. So the next thing that we'll need to build is agents

**[18:56]** thing that we'll need to build is agents

**[18:56]** thing that we'll need to build is agents with models of our minds. But we don't

**[18:58]** with models of our minds. But we don't

**[18:58]** with models of our minds. But we don't actually build those directly. We need


### [19:00 - 20:00]

**[19:00]** actually build those directly. We need

**[19:00]** actually build those directly. We need to set the preconditions for them to

**[19:02]** to set the preconditions for them to

**[19:02]** to set the preconditions for them to emerge. And this requires a common

**[19:05]** emerge. And this requires a common

**[19:05]** emerge. And this requires a common language for humans and computers. And

**[19:07]** language for humans and computers. And

**[19:07]** language for humans and computers. And at this point, you know what this

**[19:08]** at this point, you know what this

**[19:08]** at this point, you know what this entails? Agents will need a a model of

**[19:12]** entails? Agents will need a a model of

**[19:12]** entails? Agents will need a a model of our shared environment and interfaces

**[19:14]** our shared environment and interfaces

**[19:14]** our shared environment and interfaces that support intuitive interactions with

**[19:17]** that support intuitive interactions with

**[19:17]** that support intuitive interactions with us. These will enable humans and agents

**[19:20]** us. These will enable humans and agents

**[19:20]** us. These will enable humans and agents to reciprocally level up one another's

**[19:22]** to reciprocally level up one another's

**[19:22]** to reciprocally level up one another's intelligence. To advance the models, we

**[19:25]** intelligence. To advance the models, we

**[19:25]** intelligence. To advance the models, we will need human agent interaction data.

**[19:28]** will need human agent interaction data.

**[19:28]** will need human agent interaction data. And to motivate people to use the agents

**[19:29]** And to motivate people to use the agents

**[19:30]** And to motivate people to use the agents in the first place, we'll need useful

**[19:31]** in the first place, we'll need useful

**[19:31]** in the first place, we'll need useful products. The more useful the products

**[19:33]** products. The more useful the products

**[19:33]** products. The more useful the products become, the smarter we will all become.

**[19:36]** become, the smarter we will all become.

**[19:36]** become, the smarter we will all become. So this is how we can collectively build

**[19:39]** So this is how we can collectively build

**[19:39]** So this is how we can collectively build useful general intelligence. Um if you

**[19:42]** useful general intelligence. Um if you

**[19:42]** useful general intelligence. Um if you want to learn more about Nova Act then

**[19:44]** want to learn more about Nova Act then

**[19:44]** want to learn more about Nova Act then stick around right here for the upcoming

**[19:46]** stick around right here for the upcoming

**[19:46]** stick around right here for the upcoming workshop. And thank you for your time.


