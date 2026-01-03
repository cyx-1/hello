# Robotics- why now - Quan Vuong and Jost Tobias Springberg, Physical Intelligence

**Video URL:** https://www.youtube.com/watch?v=cGLa8DsOYdk

---

## Full Transcript

### [00:00 - 01:00]

**[00:17]** So, good morning. Uh, thanks for being

**[00:17]** So, good morning. Uh, thanks for being here with us. My name isWan. This is

**[00:19]** here with us. My name isWan. This is

**[00:19]** here with us. My name isWan. This is Toby. Um, our mission is to make a model

**[00:23]** Toby. Um, our mission is to make a model

**[00:23]** Toby. Um, our mission is to make a model that can control any robot to do any

**[00:25]** that can control any robot to do any

**[00:25]** that can control any robot to do any task. Now, this is not something that's

**[00:28]** task. Now, this is not something that's

**[00:28]** task. Now, this is not something that's ready today. uh we believe that there

**[00:30]** ready today. uh we believe that there

**[00:30]** ready today. uh we believe that there are multiple scientific uh breakthrough

**[00:31]** are multiple scientific uh breakthrough

**[00:32]** are multiple scientific uh breakthrough that needs to happen for us to get

**[00:33]** that needs to happen for us to get

**[00:33]** that needs to happen for us to get there. And so we're very open. We

**[00:35]** there. And so we're very open. We

**[00:35]** there. And so we're very open. We publish our research. We open source our

**[00:37]** publish our research. We open source our

**[00:37]** publish our research. We open source our model and we talk very publicly about

**[00:39]** model and we talk very publicly about

**[00:39]** model and we talk very publicly about what is that we do. And so if you think

**[00:42]** what is that we do. And so if you think

**[00:42]** what is that we do. And so if you think about robotics before and not to say

**[00:44]** about robotics before and not to say

**[00:44]** about robotics before and not to say that it's not useful, you know, it's

**[00:45]** that it's not useful, you know, it's

**[00:45]** that it's not useful, you know, it's incredibly impactful on the world. Um

**[00:47]** incredibly impactful on the world. Um

**[00:48]** incredibly impactful on the world. Um but the scenario that you often see

**[00:50]** but the scenario that you often see

**[00:50]** but the scenario that you often see robotic in is either in a very

**[00:52]** robotic in is either in a very

**[00:52]** robotic in is either in a very constrained environment such as you know

**[00:53]** constrained environment such as you know

**[00:53]** constrained environment such as you know a factory very reparative motion very

**[00:57]** a factory very reparative motion very

**[00:57]** a factory very reparative motion very structure environment um and then when

**[00:59]** structure environment um and then when


### [01:00 - 02:00]

**[01:00]** structure environment um and then when you try to bring them into the real

**[01:01]** you try to bring them into the real

**[01:01]** you try to bring them into the real world just kind of like semistructure I

**[01:03]** world just kind of like semistructure I

**[01:03]** world just kind of like semistructure I think this is a pretty kind of

**[01:05]** think this is a pretty kind of

**[01:05]** think this is a pretty kind of well-known video of a full body humano

**[01:08]** well-known video of a full body humano

**[01:08]** well-known video of a full body humano you know struggling to perform a

**[01:10]** you know struggling to perform a

**[01:10]** you know struggling to perform a somewhat simple task um it was from some

**[01:13]** somewhat simple task um it was from some

**[01:13]** somewhat simple task um it was from some time ago um if you look at robotics

**[01:16]** time ago um if you look at robotics

**[01:16]** time ago um if you look at robotics today what do You see

**[01:19]** today what do You see

**[01:19]** today what do You see you see

**[01:27]** you see kind of humanoid dancing. I know

**[01:28]** you see kind of humanoid dancing. I know I don't think I can do that dance move.

**[01:30]** I don't think I can do that dance move.

**[01:30]** I don't think I can do that dance move. Um

**[01:32]** Um

**[01:32]** Um um I'll try. And so uh you see kind of

**[01:35]** um I'll try. And so uh you see kind of

**[01:35]** um I'll try. And so uh you see kind of very complex physical motion that robots

**[01:38]** very complex physical motion that robots

**[01:38]** very complex physical motion that robots are capable of. Um, and you also see uh

**[01:41]** are capable of. Um, and you also see uh

**[01:41]** are capable of. Um, and you also see uh this video on the right, which is what

**[01:42]** this video on the right, which is what

**[01:42]** this video on the right, which is what we released late last year of a robot

**[01:45]** we released late last year of a robot

**[01:45]** we released late last year of a robot operating with kind of somewhat

**[01:46]** operating with kind of somewhat

**[01:46]** operating with kind of somewhat semistructure objects. You know, this is

**[01:49]** semistructure objects. You know, this is

**[01:49]** semistructure objects. You know, this is clothing that just came out of a dryer

**[01:51]** clothing that just came out of a dryer

**[01:51]** clothing that just came out of a dryer that ran before. So, it's very hard to

**[01:53]** that ran before. So, it's very hard to

**[01:53]** that ran before. So, it's very hard to control, you know, the exact initial

**[01:55]** control, you know, the exact initial

**[01:55]** control, you know, the exact initial scene of, you know, how the shirt should

**[01:57]** scene of, you know, how the shirt should

**[01:57]** scene of, you know, how the shirt should be. You know, it takes out all of the

**[01:58]** be. You know, it takes out all of the

**[01:58]** be. You know, it takes out all of the shirts, managed to put them in a basket.


### [02:00 - 03:00]

**[02:01]** shirts, managed to put them in a basket.

**[02:01]** shirts, managed to put them in a basket. And in the full video, you know, it goes

**[02:03]** And in the full video, you know, it goes

**[02:03]** And in the full video, you know, it goes on, you know, bring it to a table and

**[02:04]** on, you know, bring it to a table and

**[02:04]** on, you know, bring it to a table and then complete the fold them. So, what

**[02:06]** then complete the fold them. So, what

**[02:06]** then complete the fold them. So, what really changed? You know, the obvious

**[02:07]** really changed? You know, the obvious

**[02:08]** really changed? You know, the obvious answer is that there is this AI wave

**[02:10]** answer is that there is this AI wave

**[02:10]** answer is that there is this AI wave that we're all riding on. Robotic

**[02:12]** that we're all riding on. Robotic

**[02:12]** that we're all riding on. Robotic benefits a lot from kind of general AI

**[02:14]** benefits a lot from kind of general AI

**[02:14]** benefits a lot from kind of general AI development, but there is also this

**[02:16]** development, but there is also this

**[02:16]** development, but there is also this vision language action model that uh

**[02:18]** vision language action model that uh

**[02:18]** vision language action model that uh we're pioneering. And so, what are they?

**[02:21]** we're pioneering. And so, what are they?

**[02:21]** we're pioneering. And so, what are they? I'll pass it off to Toby.

**[02:24]** I'll pass it off to Toby.

**[02:24]** I'll pass it off to Toby. Cool. Yeah. So, vision language action

**[02:27]** Cool. Yeah. So, vision language action

**[02:27]** Cool. Yeah. So, vision language action models, what are they? As Quan asked.

**[02:28]** models, what are they? As Quan asked.

**[02:28]** models, what are they? As Quan asked. Um, well, you probably all know by now

**[02:30]** Um, well, you probably all know by now

**[02:30]** Um, well, you probably all know by now what a multimodal LLM or we often refer

**[02:33]** what a multimodal LLM or we often refer

**[02:33]** what a multimodal LLM or we often refer to it as a vision language model or VLM

**[02:36]** to it as a vision language model or VLM

**[02:36]** to it as a vision language model or VLM is by now. Um, essentially a VLM

**[02:39]** is by now. Um, essentially a VLM

**[02:39]** is by now. Um, essentially a VLM generally takes text and images as

**[02:41]** generally takes text and images as

**[02:42]** generally takes text and images as input. So you have some sort of prompt

**[02:43]** input. So you have some sort of prompt

**[02:43]** input. So you have some sort of prompt for the model. Um, and then it embeds

**[02:45]** for the model. Um, and then it embeds

**[02:45]** for the model. Um, and then it embeds them and pass them to a transformer

**[02:47]** them and pass them to a transformer

**[02:47]** them and pass them to a transformer model to auto reggressively produce an

**[02:49]** model to auto reggressively produce an

**[02:49]** model to auto reggressively produce an answer in text. Right? So you interact

**[02:51]** answer in text. Right? So you interact

**[02:51]** answer in text. Right? So you interact with these models probably uh as I do

**[02:53]** with these models probably uh as I do

**[02:53]** with these models probably uh as I do every day now. Um so and then a VLA is

**[02:56]** every day now. Um so and then a VLA is

**[02:56]** every day now. Um so and then a VLA is essentially an adaptation of a VLM for

**[02:59]** essentially an adaptation of a VLM for

**[02:59]** essentially an adaptation of a VLM for the purpose of robotics. The model


### [03:00 - 04:00]

**[03:01]** the purpose of robotics. The model

**[03:01]** the purpose of robotics. The model additionally gets inputs describing the

**[03:03]** additionally gets inputs describing the

**[03:03]** additionally gets inputs describing the robot states such as its joints

**[03:06]** robot states such as its joints

**[03:06]** robot states such as its joints positions and um instead of asking

**[03:08]** positions and um instead of asking

**[03:08]** positions and um instead of asking questions about what's going on in the

**[03:10]** questions about what's going on in the

**[03:10]** questions about what's going on in the scene, we ask the model to produce

**[03:13]** scene, we ask the model to produce

**[03:13]** scene, we ask the model to produce actions to control the robot directly.

**[03:15]** actions to control the robot directly.

**[03:15]** actions to control the robot directly. Right?

**[03:17]** Right?

**[03:17]** Right? So if VLMs and VAS are so similar in

**[03:20]** So if VLMs and VAS are so similar in

**[03:20]** So if VLMs and VAS are so similar in kind of principle then what are the

**[03:22]** kind of principle then what are the

**[03:22]** kind of principle then what are the additional engineering challenges that

**[03:23]** additional engineering challenges that

**[03:23]** additional engineering challenges that we face when we try to train such a VA.

**[03:26]** we face when we try to train such a VA.

**[03:26]** we face when we try to train such a VA. Um to understand this I want to contrast

**[03:28]** Um to understand this I want to contrast

**[03:28]** Um to understand this I want to contrast a little bit pipelines for VLM training

**[03:31]** a little bit pipelines for VLM training

**[03:31]** a little bit pipelines for VLM training to what we have to do when we train a VA

**[03:33]** to what we have to do when we train a VA

**[03:33]** to what we have to do when we train a VA for robotics. So when you as kind of

**[03:36]** for robotics. So when you as kind of

**[03:36]** for robotics. So when you as kind of like a downstream customer of these like

**[03:38]** like a downstream customer of these like

**[03:38]** like a downstream customer of these like big models that have been trained want

**[03:40]** big models that have been trained want

**[03:40]** big models that have been trained want to use a VLM, you generally kind of take

**[03:43]** to use a VLM, you generally kind of take

**[03:43]** to use a VLM, you generally kind of take um a model and you can source data from

**[03:45]** um a model and you can source data from

**[03:45]** um a model and you can source data from the web and maybe you have a little bit

**[03:47]** the web and maybe you have a little bit

**[03:47]** the web and maybe you have a little bit of extra data that that you have for

**[03:49]** of extra data that that you have for

**[03:49]** of extra data that that you have for your specific task that you're

**[03:50]** your specific task that you're

**[03:50]** your specific task that you're interested in that you supplement um and

**[03:52]** interested in that you supplement um and

**[03:52]** interested in that you supplement um and then you probably train an use an

**[03:55]** then you probably train an use an

**[03:55]** then you probably train an use an offtheshelf model and you fine-tune it

**[03:56]** offtheshelf model and you fine-tune it

**[03:56]** offtheshelf model and you fine-tune it on a large cluster somewhere in the

**[03:58]** on a large cluster somewhere in the

**[03:58]** on a large cluster somewhere in the cloud and then finally you can use well


### [04:00 - 05:00]

**[04:00]** cloud and then finally you can use well

**[04:00]** cloud and then finally you can use well established libraries for inference and

**[04:02]** established libraries for inference and

**[04:02]** established libraries for inference and deployment in the cloud. Right? So all

**[04:04]** deployment in the cloud. Right? So all

**[04:04]** deployment in the cloud. Right? So all of this is like probably bread and

**[04:05]** of this is like probably bread and

**[04:05]** of this is like probably bread and better for for a bunch of you. Now in

**[04:08]** better for for a bunch of you. Now in

**[04:08]** better for for a bunch of you. Now in contrast to that um if we want to do VLA

**[04:11]** contrast to that um if we want to do VLA

**[04:11]** contrast to that um if we want to do VLA training

**[04:13]** training

**[04:13]** training um you want to train a model to exhibit

**[04:15]** um you want to train a model to exhibit

**[04:15]** um you want to train a model to exhibit kind of dextrous frontier level behavior

**[04:19]** kind of dextrous frontier level behavior

**[04:19]** kind of dextrous frontier level behavior then it's an open question what the

**[04:21]** then it's an open question what the

**[04:21]** then it's an open question what the analytical data source for the web

**[04:23]** analytical data source for the web

**[04:23]** analytical data source for the web actually is right and we believe that

**[04:25]** actually is right and we believe that

**[04:25]** actually is right and we believe that this is kind of a trillion dollar

**[04:26]** this is kind of a trillion dollar

**[04:26]** this is kind of a trillion dollar question for the industry in some sense

**[04:28]** question for the industry in some sense

**[04:28]** question for the industry in some sense and it's an entirely open resource

**[04:30]** and it's an entirely open resource

**[04:30]** and it's an entirely open resource question as Quan already uh said

**[04:33]** question as Quan already uh said

**[04:33]** question as Quan already uh said and then secondly while we can use um

**[04:36]** and then secondly while we can use um

**[04:36]** and then secondly while we can use um VLM backbones so we can reuse use some

**[04:38]** VLM backbones so we can reuse use some

**[04:38]** VLM backbones so we can reuse use some pre-trained models, we typically have to

**[04:40]** pre-trained models, we typically have to

**[04:40]** pre-trained models, we typically have to adapt them and adapt the model

**[04:41]** adapt them and adapt the model

**[04:42]** adapt them and adapt the model architectures in order to allow for

**[04:43]** architectures in order to allow for

**[04:43]** architectures in order to allow for models that can control robots at

**[04:45]** models that can control robots at

**[04:45]** models that can control robots at somehow high frequency controls that we

**[04:48]** somehow high frequency controls that we

**[04:48]** somehow high frequency controls that we need to actually make progress.

**[04:50]** need to actually make progress.

**[04:50]** need to actually make progress. And then finally, we there's also no

**[04:53]** And then finally, we there's also no

**[04:53]** And then finally, we there's also no standard solution for deploying large

**[04:55]** standard solution for deploying large

**[04:55]** standard solution for deploying large robot policies in multiple locations on

**[04:58]** robot policies in multiple locations on

**[04:58]** robot policies in multiple locations on premise on device for robots, right? So


### [05:00 - 06:00]

**[05:00]** premise on device for robots, right? So

**[05:00]** premise on device for robots, right? So this just doesn't exist. I won't really

**[05:02]** this just doesn't exist. I won't really

**[05:02]** this just doesn't exist. I won't really have time to talk about the third thing

**[05:04]** have time to talk about the third thing

**[05:04]** have time to talk about the third thing in detail here, but I want to dive into

**[05:05]** in detail here, but I want to dive into

**[05:06]** in detail here, but I want to dive into a little bit about data and model

**[05:08]** a little bit about data and model

**[05:08]** a little bit about data and model training for robotics that we do at PI.

**[05:11]** training for robotics that we do at PI.

**[05:11]** training for robotics that we do at PI. So, first, how can we design a data

**[05:13]** So, first, how can we design a data

**[05:13]** So, first, how can we design a data engine that enables robust, highly

**[05:15]** engine that enables robust, highly

**[05:15]** engine that enables robust, highly dextrous policies for difficult tasks

**[05:17]** dextrous policies for difficult tasks

**[05:17]** dextrous policies for difficult tasks with robots? At PI, we kind of believe

**[05:19]** with robots? At PI, we kind of believe

**[05:19]** with robots? At PI, we kind of believe that there currently is no standard

**[05:21]** that there currently is no standard

**[05:21]** that there currently is no standard solution for this at all that would

**[05:22]** solution for this at all that would

**[05:22]** solution for this at all that would enable us to do this. And so, we're

**[05:24]** enable us to do this. And so, we're

**[05:24]** enable us to do this. And so, we're building essentially a data engine from

**[05:26]** building essentially a data engine from

**[05:26]** building essentially a data engine from the ground up, from zero. We are

**[05:28]** the ground up, from zero. We are

**[05:28]** the ground up, from zero. We are designing this pipeline to get us very

**[05:29]** designing this pipeline to get us very

**[05:30]** designing this pipeline to get us very quickly to some sort of impressive

**[05:31]** quickly to some sort of impressive

**[05:31]** quickly to some sort of impressive capability and I hope at the end of the

**[05:33]** capability and I hope at the end of the

**[05:33]** capability and I hope at the end of the talk you'll agree that it looks somewhat

**[05:34]** talk you'll agree that it looks somewhat

**[05:34]** talk you'll agree that it looks somewhat impressive but also to enable

**[05:36]** impressive but also to enable

**[05:36]** impressive but also to enable significant scaling in the next few

**[05:37]** significant scaling in the next few

**[05:38]** significant scaling in the next few years.

**[05:39]** years.

**[05:39]** years. Um so we have seen firsthand that

**[05:41]** Um so we have seen firsthand that

**[05:41]** Um so we have seen firsthand that operationalizing this pipeline is

**[05:43]** operationalizing this pipeline is

**[05:43]** operationalizing this pipeline is actually kind of one of the main

**[05:45]** actually kind of one of the main

**[05:45]** actually kind of one of the main ingredients is probably more than 50% of

**[05:47]** ingredients is probably more than 50% of

**[05:47]** ingredients is probably more than 50% of the work is getting the data pipeline

**[05:48]** the work is getting the data pipeline

**[05:48]** the work is getting the data pipeline right getting the right data getting it

**[05:50]** right getting the right data getting it

**[05:50]** right getting the right data getting it to be high quality. So how does it work?

**[05:52]** to be high quality. So how does it work?

**[05:52]** to be high quality. So how does it work? Well, we typically start from a set of

**[05:55]** Well, we typically start from a set of

**[05:55]** Well, we typically start from a set of everexpanding tasks that we pick to test

**[05:57]** everexpanding tasks that we pick to test

**[05:57]** everexpanding tasks that we pick to test what's possible in the moment, right?

**[05:59]** what's possible in the moment, right?

**[05:59]** what's possible in the moment, right? So, these are tasks such as folding


### [06:00 - 07:00]

**[06:01]** So, these are tasks such as folding

**[06:01]** So, these are tasks such as folding clothes, bagging groceries, many other

**[06:03]** clothes, bagging groceries, many other

**[06:03]** clothes, bagging groceries, many other tasks that we're interested in. And we

**[06:05]** tasks that we're interested in. And we

**[06:05]** tasks that we're interested in. And we then have human operators control our

**[06:06]** then have human operators control our

**[06:06]** then have human operators control our robots using a custom runtime and

**[06:08]** robots using a custom runtime and

**[06:08]** robots using a custom runtime and teleoperation system. You can see the

**[06:11]** teleoperation system. You can see the

**[06:11]** teleoperation system. You can see the system in this video here. Uh so what

**[06:14]** system in this video here. Uh so what

**[06:14]** system in this video here. Uh so what happens there is there's human operators

**[06:16]** happens there is there's human operators

**[06:16]** happens there is there's human operators and they are controlling what we call

**[06:17]** and they are controlling what we call

**[06:17]** and they are controlling what we call leader arms where they basically trace

**[06:20]** leader arms where they basically trace

**[06:20]** leader arms where they basically trace out motions with their arms with uh

**[06:22]** out motions with their arms with uh

**[06:22]** out motions with their arms with uh robot arms kind of strapped to their

**[06:24]** robot arms kind of strapped to their

**[06:24]** robot arms kind of strapped to their arms and the motion gets transferred via

**[06:26]** arms and the motion gets transferred via

**[06:26]** arms and the motion gets transferred via software to the actual robot and right

**[06:28]** software to the actual robot and right

**[06:28]** software to the actual robot and right and this way you can demonstrate fairly

**[06:30]** and this way you can demonstrate fairly

**[06:30]** and this way you can demonstrate fairly intricate highly dextrous tasks and

**[06:33]** intricate highly dextrous tasks and

**[06:33]** intricate highly dextrous tasks and collect that data for training

**[06:34]** collect that data for training

**[06:34]** collect that data for training afterwards.

**[06:37]** afterwards.

**[06:37]** afterwards. Um and then afterwards we have a bunch

**[06:40]** Um and then afterwards we have a bunch

**[06:40]** Um and then afterwards we have a bunch of uh facilities to do kind of uh

**[06:44]** of uh facilities to do kind of uh

**[06:44]** of uh facilities to do kind of uh tracking of metrics of what's going on

**[06:46]** tracking of metrics of what's going on

**[06:46]** tracking of metrics of what's going on at the moment. I think there's another

**[06:48]** at the moment. I think there's another

**[06:48]** at the moment. I think there's another slide here. Yep. Uh so we basically

**[06:50]** slide here. Yep. Uh so we basically

**[06:50]** slide here. Yep. Uh so we basically schedule these data collection uh

**[06:52]** schedule these data collection uh

**[06:52]** schedule these data collection uh sessions all the time and each dash in

**[06:55]** sessions all the time and each dash in

**[06:55]** sessions all the time and each dash in this uh dashboard here shows from this

**[06:57]** this uh dashboard here shows from this

**[06:58]** this uh dashboard here shows from this week this is I think from from Tuesday


### [07:00 - 08:00]

**[07:00]** week this is I think from from Tuesday

**[07:00]** week this is I think from from Tuesday an operator doing a specific episode for

**[07:02]** an operator doing a specific episode for

**[07:02]** an operator doing a specific episode for a specific task. Right? So we collect a

**[07:04]** a specific task. Right? So we collect a

**[07:04]** a specific task. Right? So we collect a lot of this data all around the clock

**[07:05]** lot of this data all around the clock

**[07:05]** lot of this data all around the clock basically.

**[07:07]** basically.

**[07:07]** basically. And then we uh annotate that data in the

**[07:09]** And then we uh annotate that data in the

**[07:09]** And then we uh annotate that data in the cloud. We we we serve it uh in in big

**[07:12]** cloud. We we we serve it uh in in big

**[07:12]** cloud. We we we serve it uh in in big buckets there and can filter it back

**[07:15]** buckets there and can filter it back

**[07:15]** buckets there and can filter it back down based on annotations and use it for

**[07:17]** down based on annotations and use it for

**[07:17]** down based on annotations and use it for model training.

**[07:19]** model training.

**[07:19]** model training. After we've trained, we then get

**[07:21]** After we've trained, we then get

**[07:21]** After we've trained, we then get policies that can actually solve the

**[07:23]** policies that can actually solve the

**[07:23]** policies that can actually solve the denominated tasks autonomously. So here

**[07:25]** denominated tasks autonomously. So here

**[07:25]** denominated tasks autonomously. So here in this video, you see a model that is

**[07:27]** in this video, you see a model that is

**[07:27]** in this video, you see a model that is PI zero. So this is the model that Quan

**[07:29]** PI zero. So this is the model that Quan

**[07:29]** PI zero. So this is the model that Quan referred to earlier already that we

**[07:31]** referred to earlier already that we

**[07:31]** referred to earlier already that we released uh late last year. And as you

**[07:33]** released uh late last year. And as you

**[07:33]** released uh late last year. And as you can see, it can kind of do these like

**[07:35]** can see, it can kind of do these like

**[07:35]** can see, it can kind of do these like fairly impressive, highly dextrous tasks

**[07:37]** fairly impressive, highly dextrous tasks

**[07:37]** fairly impressive, highly dextrous tasks such as as shirt folding.

**[07:40]** such as as shirt folding.

**[07:40]** such as as shirt folding. Okay, so how far have we gotten by

**[07:42]** Okay, so how far have we gotten by

**[07:42]** Okay, so how far have we gotten by following this approach? Well, when we

**[07:44]** following this approach? Well, when we

**[07:44]** following this approach? Well, when we started, the biggest publicly available

**[07:45]** started, the biggest publicly available

**[07:45]** started, the biggest publicly available data set was the open cross embodiment

**[07:47]** data set was the open cross embodiment

**[07:47]** data set was the open cross embodiment data set, which contained about 3,800

**[07:50]** data set, which contained about 3,800

**[07:50]** data set, which contained about 3,800 hours of data largely from static scenes

**[07:52]** hours of data largely from static scenes

**[07:52]** hours of data largely from static scenes in different robot labs around the

**[07:54]** in different robot labs around the

**[07:54]** in different robot labs around the world. After kind of running this data

**[07:57]** world. After kind of running this data

**[07:57]** world. After kind of running this data pad that I've described for six months,

**[07:59]** pad that I've described for six months,

**[07:59]** pad that I've described for six months, we had collected about 10,000 hours of


### [08:00 - 09:00]

**[08:01]** we had collected about 10,000 hours of

**[08:01]** we had collected about 10,000 hours of successful episodes. This is successful

**[08:03]** successful episodes. This is successful

**[08:03]** successful episodes. This is successful data uh in tens of environments covering

**[08:06]** data uh in tens of environments covering

**[08:06]** data uh in tens of environments covering hundreds of different tasks enabling for

**[08:08]** hundreds of different tasks enabling for

**[08:08]** hundreds of different tasks enabling for example the kind of shortfolding

**[08:10]** example the kind of shortfolding

**[08:10]** example the kind of shortfolding policies you you saw before. Oops.

**[08:13]** policies you you saw before. Oops.

**[08:14]** policies you you saw before. Oops. Um cool. Is that video actually playing?

**[08:16]** Um cool. Is that video actually playing?

**[08:16]** Um cool. Is that video actually playing? Why is that video not playing?

**[08:20]** Why is that video not playing?

**[08:20]** Why is that video not playing? Can I get it to play?

**[08:23]** Can I get it to play?

**[08:23]** Can I get it to play? account.

**[08:26]** account.

**[08:26]** account. Let's see what we do with the next

**[08:27]** Let's see what we do with the next

**[08:27]** Let's see what we do with the next video. Um, and then after another six

**[08:29]** video. Um, and then after another six

**[08:29]** video. Um, and then after another six months, this place, uh, we have

**[08:32]** months, this place, uh, we have

**[08:32]** months, this place, uh, we have collected many more hours of data in

**[08:33]** collected many more hours of data in

**[08:33]** collected many more hours of data in static scenes, but crucially have also

**[08:35]** static scenes, but crucially have also

**[08:35]** static scenes, but crucially have also started to collect significant amounts

**[08:37]** started to collect significant amounts

**[08:37]** started to collect significant amounts of data using mobile manipulation setups

**[08:39]** of data using mobile manipulation setups

**[08:39]** of data using mobile manipulation setups such as the ones you see here. So, the

**[08:42]** such as the ones you see here. So, the

**[08:42]** such as the ones you see here. So, the data now spends many many more tasks and

**[08:45]** data now spends many many more tasks and

**[08:45]** data now spends many many more tasks and importantly has massively grown in

**[08:46]** importantly has massively grown in

**[08:46]** importantly has massively grown in diversity covering hundreds of different

**[08:48]** diversity covering hundreds of different

**[08:48]** diversity covering hundreds of different scenes and environments. And as you can

**[08:50]** scenes and environments. And as you can

**[08:50]** scenes and environments. And as you can imagine, this scale and diversity

**[08:52]** imagine, this scale and diversity

**[08:52]** imagine, this scale and diversity enables new leaps as you can kind of see

**[08:54]** enables new leaps as you can kind of see

**[08:54]** enables new leaps as you can kind of see here by this policy that is already

**[08:57]** here by this policy that is already

**[08:57]** here by this policy that is already running autonomously. And I'll go into

**[08:58]** running autonomously. And I'll go into

**[08:58]** running autonomously. And I'll go into detail a little bit how this works, but


### [09:00 - 10:00]

**[09:00]** detail a little bit how this works, but

**[09:00]** detail a little bit how this works, but also brings lots of additional

**[09:02]** also brings lots of additional

**[09:02]** also brings lots of additional engineering challenges.

**[09:04]** engineering challenges.

**[09:04]** engineering challenges. So now that we have kind of described

**[09:06]** So now that we have kind of described

**[09:06]** So now that we have kind of described how we get the data, then the question

**[09:08]** how we get the data, then the question

**[09:08]** how we get the data, then the question is what kind of capabilities can we

**[09:10]** is what kind of capabilities can we

**[09:10]** is what kind of capabilities can we elicit with this data in VAS, right? And

**[09:13]** elicit with this data in VAS, right? And

**[09:13]** elicit with this data in VAS, right? And to understand where we are today, I

**[09:15]** to understand where we are today, I

**[09:15]** to understand where we are today, I think it's kind of useful to draw an

**[09:16]** think it's kind of useful to draw an

**[09:16]** think it's kind of useful to draw an analogy between the industry trends for

**[09:18]** analogy between the industry trends for

**[09:18]** analogy between the industry trends for VLMs and VAS which have been kind of

**[09:20]** VLMs and VAS which have been kind of

**[09:20]** VLMs and VAS which have been kind of ongoing in the last three years.

**[09:23]** ongoing in the last three years.

**[09:23]** ongoing in the last three years. So first for multimodal LLMs or VLMs, we

**[09:26]** So first for multimodal LLMs or VLMs, we

**[09:26]** So first for multimodal LLMs or VLMs, we have seen a constant stream of

**[09:27]** have seen a constant stream of

**[09:28]** have seen a constant stream of improvements over the last three years

**[09:29]** improvements over the last three years

**[09:29]** improvements over the last three years kind of starting from initial

**[09:30]** kind of starting from initial

**[09:30]** kind of starting from initial conversational agents that you've all

**[09:32]** conversational agents that you've all

**[09:32]** conversational agents that you've all interacted with all the way to the RL

**[09:35]** interacted with all the way to the RL

**[09:35]** interacted with all the way to the RL trained multimodel reasoning models and

**[09:38]** trained multimodel reasoning models and

**[09:38]** trained multimodel reasoning models and coding assistants that we all have

**[09:39]** coding assistants that we all have

**[09:39]** coding assistants that we all have today, right? And we all use um for VAS

**[09:43]** today, right? And we all use um for VAS

**[09:43]** today, right? And we all use um for VAS they follow a similar but time lag

**[09:45]** they follow a similar but time lag

**[09:45]** they follow a similar but time lag trajectory basically. So initial VALAS

**[09:47]** trajectory basically. So initial VALAS

**[09:47]** trajectory basically. So initial VALAS such as RT2 for example done by some of

**[09:50]** such as RT2 for example done by some of

**[09:50]** such as RT2 for example done by some of my colleagues that are now at PI emerged

**[09:53]** my colleagues that are now at PI emerged

**[09:53]** my colleagues that are now at PI emerged in 2023 after LLM had already been

**[09:56]** in 2023 after LLM had already been

**[09:56]** in 2023 after LLM had already been enhanced with with vision encoders. And

**[09:58]** enhanced with with vision encoders. And

**[09:58]** enhanced with with vision encoders. And in fact actually some of the earliest


### [10:00 - 11:00]

**[10:00]** in fact actually some of the earliest

**[10:00]** in fact actually some of the earliest multimodal LLMs were trained for

**[10:02]** multimodal LLMs were trained for

**[10:02]** multimodal LLMs were trained for robotics purposes by some of my

**[10:05]** robotics purposes by some of my

**[10:05]** robotics purposes by some of my colleagues Danny and others that are now

**[10:07]** colleagues Danny and others that are now

**[10:07]** colleagues Danny and others that are now working with us at PI. These were kind

**[10:10]** working with us at PI. These were kind

**[10:10]** working with us at PI. These were kind of impressive as first proofs of concept

**[10:12]** of impressive as first proofs of concept

**[10:12]** of impressive as first proofs of concept and showed some generalization

**[10:14]** and showed some generalization

**[10:14]** and showed some generalization capabilities. So you could kind of like

**[10:15]** capabilities. So you could kind of like

**[10:15]** capabilities. So you could kind of like ask them to pick different objects in

**[10:17]** ask them to pick different objects in

**[10:17]** ask them to pick different objects in the same kind of scene that kind of is

**[10:19]** the same kind of scene that kind of is

**[10:19]** the same kind of scene that kind of is in the training data. But they are

**[10:21]** in the training data. But they are

**[10:21]** in the training data. But they are generally held back by a lack of

**[10:22]** generally held back by a lack of

**[10:22]** generally held back by a lack of available robot data. But you know

**[10:25]** available robot data. But you know

**[10:25]** available robot data. But you know nonetheless they sparked this big

**[10:26]** nonetheless they sparked this big

**[10:26]** nonetheless they sparked this big explosion of interest in the field which

**[10:28]** explosion of interest in the field which

**[10:28]** explosion of interest in the field which is probably why you're here today. Um

**[10:31]** is probably why you're here today. Um

**[10:31]** is probably why you're here today. Um then in the mid 20 so mid 2024 towards

**[10:34]** then in the mid 20 so mid 2024 towards

**[10:34]** then in the mid 20 so mid 2024 towards ends 2024 the first kind of really

**[10:36]** ends 2024 the first kind of really

**[10:36]** ends 2024 the first kind of really dextrous multi-root vas uh appeared

**[10:39]** dextrous multi-root vas uh appeared

**[10:39]** dextrous multi-root vas uh appeared right and the industry at large has now

**[10:41]** right and the industry at large has now

**[10:41]** right and the industry at large has now produced several of those uh there are

**[10:43]** produced several of those uh there are

**[10:43]** produced several of those uh there are models for example such as Gemini for

**[10:45]** models for example such as Gemini for

**[10:45]** models for example such as Gemini for robotics or Nvidia's group models that I

**[10:47]** robotics or Nvidia's group models that I

**[10:47]** robotics or Nvidia's group models that I think you'll hear a little bit about

**[10:49]** think you'll hear a little bit about

**[10:49]** think you'll hear a little bit about later as well and our entry in this

**[10:51]** later as well and our entry in this

**[10:51]** later as well and our entry in this category was PI zero which we believe is

**[10:53]** category was PI zero which we believe is

**[10:53]** category was PI zero which we believe is kind of perhaps the most dextrous uh

**[10:56]** kind of perhaps the most dextrous uh

**[10:56]** kind of perhaps the most dextrous uh multi-root model that you can you can

**[10:58]** multi-root model that you can you can

**[10:58]** multi-root model that you can you can use and in fact is open source as well.


### [11:00 - 12:00]

**[11:02]** use and in fact is open source as well.

**[11:02]** use and in fact is open source as well. So these models generally adjust

**[11:03]** So these models generally adjust

**[11:03]** So these models generally adjust architectures to produce actions via

**[11:05]** architectures to produce actions via

**[11:05]** architectures to produce actions via diffusion to enable kind of very fast

**[11:08]** diffusion to enable kind of very fast

**[11:08]** diffusion to enable kind of very fast generation at high frequencies you need

**[11:10]** generation at high frequencies you need

**[11:10]** generation at high frequencies you need for for robot control. So if that's

**[11:13]** for for robot control. So if that's

**[11:13]** for for robot control. So if that's where we were then what's next? Where

**[11:15]** where we were then what's next? Where

**[11:15]** where we were then what's next? Where are we now? Right? Um

**[11:18]** are we now? Right? Um

**[11:18]** are we now? Right? Um so for us the next leap was to study

**[11:21]** so for us the next leap was to study

**[11:21]** so for us the next leap was to study just how exactly model capabilities

**[11:23]** just how exactly model capabilities

**[11:23]** just how exactly model capabilities change when we increase data collection

**[11:26]** change when we increase data collection

**[11:26]** change when we increase data collection diversity. And this led us to develop

**[11:28]** diversity. And this led us to develop

**[11:28]** diversity. And this led us to develop PIO5 which is basically a VLA with open

**[11:31]** PIO5 which is basically a VLA with open

**[11:31]** PIO5 which is basically a VLA with open world generalization. And I want to talk

**[11:32]** world generalization. And I want to talk

**[11:32]** world generalization. And I want to talk a little bit more about this. Um so what

**[11:34]** a little bit more about this. Um so what

**[11:34]** a little bit more about this. Um so what does this look like? In general, we have

**[11:37]** does this look like? In general, we have

**[11:37]** does this look like? In general, we have expanded massively as I kind of said the

**[11:39]** expanded massively as I kind of said the

**[11:39]** expanded massively as I kind of said the data we take in during training. It now

**[11:41]** data we take in during training. It now

**[11:41]** data we take in during training. It now consists on both static and mobile robot

**[11:43]** consists on both static and mobile robot

**[11:43]** consists on both static and mobile robot data on the right here as well as an

**[11:45]** data on the right here as well as an

**[11:45]** data on the right here as well as an extended set of multimodal VLM data such

**[11:47]** extended set of multimodal VLM data such

**[11:47]** extended set of multimodal VLM data such as data from the web, object detection

**[11:49]** as data from the web, object detection

**[11:49]** as data from the web, object detection data, and general language annotations

**[11:52]** data, and general language annotations

**[11:52]** data, and general language annotations for the robot data that we've collected.

**[11:54]** for the robot data that we've collected.

**[11:54]** for the robot data that we've collected. So we have a huge annotation pipeline as

**[11:56]** So we have a huge annotation pipeline as

**[11:56]** So we have a huge annotation pipeline as well. And this is what's on the left

**[11:57]** well. And this is what's on the left

**[11:57]** well. And this is what's on the left here. We then feed this data into a

**[11:59]** here. We then feed this data into a


### [12:00 - 13:00]

**[12:00]** here. We then feed this data into a specially designed VLM which starts from

**[12:01]** specially designed VLM which starts from

**[12:02]** specially designed VLM which starts from a pre-trained transformer model and is

**[12:04]** a pre-trained transformer model and is

**[12:04]** a pre-trained transformer model and is expanded with an action expert

**[12:06]** expanded with an action expert

**[12:06]** expanded with an action expert transformer to the right. This VLM part

**[12:09]** transformer to the right. This VLM part

**[12:09]** transformer to the right. This VLM part so the big backbone of it is trained to

**[12:11]** so the big backbone of it is trained to

**[12:11]** so the big backbone of it is trained to give predictions for both general

**[12:13]** give predictions for both general

**[12:13]** give predictions for both general questions about the scene. Now, but also

**[12:15]** questions about the scene. Now, but also

**[12:15]** questions about the scene. Now, but also to subdivide highle requests that a

**[12:17]** to subdivide highle requests that a

**[12:17]** to subdivide highle requests that a human might have uh for the model such

**[12:20]** human might have uh for the model such

**[12:20]** human might have uh for the model such as for example clean my bedroom. Right?

**[12:22]** as for example clean my bedroom. Right?

**[12:22]** as for example clean my bedroom. Right? So it is trained to subdivide these

**[12:24]** So it is trained to subdivide these

**[12:24]** So it is trained to subdivide these tasks into u subtasks such as pick up a

**[12:27]** tasks into u subtasks such as pick up a

**[12:27]** tasks into u subtasks such as pick up a pillow in the case of cleaning the bed

**[12:29]** pillow in the case of cleaning the bed

**[12:29]** pillow in the case of cleaning the bed and at the same time the action expert

**[12:31]** and at the same time the action expert

**[12:31]** and at the same time the action expert transformer can attend to the internals

**[12:34]** transformer can attend to the internals

**[12:34]** transformer can attend to the internals of the large VM and can run at much

**[12:36]** of the large VM and can run at much

**[12:36]** of the large VM and can run at much higher rate and produces the actual

**[12:38]** higher rate and produces the actual

**[12:38]** higher rate and produces the actual continuous output actions via diffusion

**[12:40]** continuous output actions via diffusion

**[12:40]** continuous output actions via diffusion flow matching objective basically.

**[12:44]** flow matching objective basically.

**[12:44]** flow matching objective basically. Cool. Hope this video please

**[12:47]** Cool. Hope this video please

**[12:47]** Cool. Hope this video please get it to play.

**[12:50]** get it to play.

**[12:50]** get it to play. Yes. So training this architecture on

**[12:53]** Yes. So training this architecture on

**[12:53]** Yes. So training this architecture on all our data then leads us to a VA that

**[12:55]** all our data then leads us to a VA that

**[12:55]** all our data then leads us to a VA that can perform difficult long horizon tasks

**[12:57]** can perform difficult long horizon tasks

**[12:57]** can perform difficult long horizon tasks of up to 10 minutes in in each episodes


### [13:00 - 14:00]

**[13:00]** of up to 10 minutes in in each episodes

**[13:00]** of up to 10 minutes in in each episodes and this is I think much much longer

**[13:03]** and this is I think much much longer

**[13:03]** and this is I think much much longer than what we've seen before right and it

**[13:05]** than what we've seen before right and it

**[13:05]** than what we've seen before right and it can do this in entirely unseen homes

**[13:07]** can do this in entirely unseen homes

**[13:07]** can do this in entirely unseen homes showcasing perhaps the first sign like

**[13:09]** showcasing perhaps the first sign like

**[13:09]** showcasing perhaps the first sign like the first true sign that broad

**[13:10]** the first true sign that broad

**[13:10]** the first true sign that broad generalization can emerge from VA

**[13:12]** generalization can emerge from VA

**[13:12]** generalization can emerge from VA training so in this video here you see

**[13:14]** training so in this video here you see

**[13:14]** training so in this video here you see my uh colleague Chelsea prompting the

**[13:17]** my uh colleague Chelsea prompting the

**[13:17]** my uh colleague Chelsea prompting the model in in an yeah you know an entirely

**[13:20]** model in in an yeah you know an entirely

**[13:20]** model in in an yeah you know an entirely new home that is not in a train data to

**[13:22]** new home that is not in a train data to

**[13:22]** new home that is not in a train data to essentially do perform multiple cleaning

**[13:24]** essentially do perform multiple cleaning

**[13:24]** essentially do perform multiple cleaning tasks such as cleaning a surface here uh

**[13:26]** tasks such as cleaning a surface here uh

**[13:26]** tasks such as cleaning a surface here uh in a kitchen.

**[13:35]** Cool.

**[13:35]** Cool. And to understand this ability to

**[13:37]** And to understand this ability to

**[13:37]** And to understand this ability to generalize a little bit further, we

**[13:39]** generalize a little bit further, we

**[13:39]** generalize a little bit further, we tested how it emerges by training PIO5

**[13:42]** tested how it emerges by training PIO5

**[13:42]** tested how it emerges by training PIO5 on a fixed number of data but varying

**[13:44]** on a fixed number of data but varying

**[13:44]** on a fixed number of data but varying the number of uh homes from which data

**[13:47]** the number of uh homes from which data

**[13:47]** the number of uh homes from which data was introduced during training.

**[13:49]** was introduced during training.

**[13:49]** was introduced during training. basically then testing it in a held out

**[13:51]** basically then testing it in a held out

**[13:51]** basically then testing it in a held out location, right? And as you can see with

**[13:53]** location, right? And as you can see with

**[13:53]** location, right? And as you can see with increasing amounts of locations added,

**[13:55]** increasing amounts of locations added,

**[13:55]** increasing amounts of locations added, so this is the yellow curve here,

**[13:57]** so this is the yellow curve here,

**[13:57]** so this is the yellow curve here, performance generally increases in the

**[13:59]** performance generally increases in the

**[13:59]** performance generally increases in the test scene as you would expect until it


### [14:00 - 15:00]

**[14:01]** test scene as you would expect until it

**[14:01]** test scene as you would expect until it surprisingly perhaps matches and even

**[14:03]** surprisingly perhaps matches and even

**[14:03]** surprisingly perhaps matches and even slightly surpasses training with the

**[14:05]** slightly surpasses training with the

**[14:05]** slightly surpasses training with the held out scene specifically, right? So

**[14:07]** held out scene specifically, right? So

**[14:07]** held out scene specifically, right? So this was a very cool result for us

**[14:08]** this was a very cool result for us

**[14:08]** this was a very cool result for us because we saw that we could kind of

**[14:10]** because we saw that we could kind of

**[14:10]** because we saw that we could kind of expand with more and more training data

**[14:13]** expand with more and more training data

**[14:13]** expand with more and more training data collections in different homes the

**[14:16]** collections in different homes the

**[14:16]** collections in different homes the capabilities of the model in new

**[14:18]** capabilities of the model in new

**[14:18]** capabilities of the model in new environments which I think is is pretty

**[14:20]** environments which I think is is pretty

**[14:20]** environments which I think is is pretty cool.

**[14:23]** cool.

**[14:23]** cool. And then here we see the same model

**[14:25]** And then here we see the same model

**[14:25]** And then here we see the same model performing a bedroom cleanup task in a

**[14:29]** performing a bedroom cleanup task in a

**[14:29]** performing a bedroom cleanup task in a new home. And in this specific case

**[14:31]** new home. And in this specific case

**[14:31]** new home. And in this specific case Laura a colleague of mine uh is

**[14:33]** Laura a colleague of mine uh is

**[14:33]** Laura a colleague of mine uh is prompting a model only to basically

**[14:34]** prompting a model only to basically

**[14:34]** prompting a model only to basically clean the bedroom. Right? And you see

**[14:35]** clean the bedroom. Right? And you see

**[14:36]** clean the bedroom. Right? And you see here the power of this these

**[14:37]** here the power of this these

**[14:37]** here the power of this these capabilities of subdividing into several

**[14:39]** capabilities of subdividing into several

**[14:39]** capabilities of subdividing into several tasks such as you know throwing trash in

**[14:41]** tasks such as you know throwing trash in

**[14:42]** tasks such as you know throwing trash in the bin and then uh cleaning uh making a

**[14:44]** the bin and then uh cleaning uh making a

**[14:44]** the bin and then uh cleaning uh making a bed basically. And the as you can see at

**[14:46]** bed basically. And the as you can see at

**[14:46]** bed basically. And the as you can see at the bottom with the timer you know this

**[14:48]** the bottom with the timer you know this

**[14:48]** the bottom with the timer you know this policy is autonomously collecting uh

**[14:51]** policy is autonomously collecting uh

**[14:51]** policy is autonomously collecting uh controlling this robot for multiple

**[14:53]** controlling this robot for multiple

**[14:53]** controlling this robot for multiple minutes at a time basically.

**[14:57]** minutes at a time basically.

**[14:57]** minutes at a time basically. Cool. And with that uh I give it back to

**[14:59]** Cool. And with that uh I give it back to

**[14:59]** Cool. And with that uh I give it back to Quan to talk to you a little bit about


### [15:00 - 16:00]

**[15:01]** Quan to talk to you a little bit about

**[15:01]** Quan to talk to you a little bit about partnerships.

**[15:03]** partnerships.

**[15:03]** partnerships. Thank you Toby.

**[15:05]** Thank you Toby.

**[15:05]** Thank you Toby. So what you're seeing is a robot that we

**[15:10]** So what you're seeing is a robot that we

**[15:10]** So what you're seeing is a robot that we have never seen in person. Um we mean

**[15:12]** have never seen in person. Um we mean

**[15:12]** have never seen in person. Um we mean the team at PI. Uh we've never have

**[15:15]** the team at PI. Uh we've never have

**[15:15]** the team at PI. Uh we've never have access to it. Um this robot is running

**[15:19]** access to it. Um this robot is running

**[15:19]** access to it. Um this robot is running very very far away from where our office

**[15:21]** very very far away from where our office

**[15:21]** very very far away from where our office is. Um it's performing a somewhat

**[15:23]** is. Um it's performing a somewhat

**[15:23]** is. Um it's performing a somewhat interesting task of making a cup of

**[15:25]** interesting task of making a cup of

**[15:26]** interesting task of making a cup of coffee end to end. Um and it works

**[15:30]** coffee end to end. Um and it works

**[15:30]** coffee end to end. Um and it works pretty well. we didn't need to kind of

**[15:31]** pretty well. we didn't need to kind of

**[15:31]** pretty well. we didn't need to kind of iterate many times to to to be able to

**[15:33]** iterate many times to to to be able to

**[15:33]** iterate many times to to to be able to produce this video. Now why is this

**[15:36]** produce this video. Now why is this

**[15:36]** produce this video. Now why is this important? Um when you think about

**[15:39]** important? Um when you think about

**[15:39]** important? Um when you think about robotic you know oftent times you would

**[15:41]** robotic you know oftent times you would

**[15:41]** robotic you know oftent times you would think about hardware you would think

**[15:43]** think about hardware you would think

**[15:43]** think about hardware you would think about kind of real deployment

**[15:44]** about kind of real deployment

**[15:44]** about kind of real deployment challenges. Now those are important but

**[15:47]** challenges. Now those are important but

**[15:47]** challenges. Now those are important but it's our belief that actually one of the

**[15:49]** it's our belief that actually one of the

**[15:49]** it's our belief that actually one of the main bottleneck is software and just

**[15:52]** main bottleneck is software and just

**[15:52]** main bottleneck is software and just model intelligence. And if you think

**[15:54]** model intelligence. And if you think

**[15:54]** model intelligence. And if you think about what if successful would scale

**[15:56]** about what if successful would scale

**[15:56]** about what if successful would scale with maximum velocity in the sense that

**[15:59]** with maximum velocity in the sense that

**[15:59]** with maximum velocity in the sense that you know suddenly next year you have


### [16:00 - 17:00]

**[16:01]** you know suddenly next year you have

**[16:01]** you know suddenly next year you have thousand and millions of robot deploy

**[16:03]** thousand and millions of robot deploy

**[16:03]** thousand and millions of robot deploy it's really about demonstrating the

**[16:05]** it's really about demonstrating the

**[16:05]** it's really about demonstrating the hypothesis that our model can run across

**[16:08]** hypothesis that our model can run across

**[16:08]** hypothesis that our model can run across many different hardware platform out

**[16:10]** many different hardware platform out

**[16:10]** many different hardware platform out there um without us having to invest

**[16:13]** there um without us having to invest

**[16:13]** there um without us having to invest significant time and effort into trying

**[16:15]** significant time and effort into trying

**[16:15]** significant time and effort into trying to work with that hardware platform. So

**[16:17]** to work with that hardware platform. So

**[16:17]** to work with that hardware platform. So I think the demonstration that we've

**[16:19]** I think the demonstration that we've

**[16:19]** I think the demonstration that we've never touched this robot before, we

**[16:21]** never touched this robot before, we

**[16:22]** never touched this robot before, we don't know how it works internally and

**[16:23]** don't know how it works internally and

**[16:23]** don't know how it works internally and yet our model can control that robot to

**[16:25]** yet our model can control that robot to

**[16:25]** yet our model can control that robot to perform a fairly interesting task um is

**[16:28]** perform a fairly interesting task um is

**[16:28]** perform a fairly interesting task um is a piece of evidence in that direction.

**[16:30]** a piece of evidence in that direction.

**[16:30]** a piece of evidence in that direction. Uh we have many more evidence here. Um

**[16:33]** Uh we have many more evidence here. Um

**[16:33]** Uh we have many more evidence here. Um and so that's why it's important. Um we

**[16:35]** and so that's why it's important. Um we

**[16:35]** and so that's why it's important. Um we are also very open when we work with

**[16:37]** are also very open when we work with

**[16:38]** are also very open when we work with other company because we believe that

**[16:40]** other company because we believe that

**[16:40]** other company because we believe that you know the problem is far from being

**[16:42]** you know the problem is far from being

**[16:42]** you know the problem is far from being solved. So when we work with this

**[16:43]** solved. So when we work with this

**[16:43]** solved. So when we work with this company for example that you can ask how

**[16:45]** company for example that you can ask how

**[16:45]** company for example that you can ask how do we run inference we literally sent

**[16:47]** do we run inference we literally sent

**[16:47]** do we run inference we literally sent them the model checkpoint for them to

**[16:49]** them the model checkpoint for them to

**[16:49]** them the model checkpoint for them to run like inference with um and you know

**[16:51]** run like inference with um and you know

**[16:51]** run like inference with um and you know we we have very low-level technical

**[16:53]** we we have very low-level technical

**[16:54]** we we have very low-level technical discussion with them this is to say that

**[16:56]** discussion with them this is to say that

**[16:56]** discussion with them this is to say that you know if you think there's a company

**[16:58]** you know if you think there's a company

**[16:58]** you know if you think there's a company that we should be talking to um please


### [17:00 - 18:00]

**[17:00]** that we should be talking to um please

**[17:00]** that we should be talking to um please let us know you can let me and Toby know

**[17:02]** let us know you can let me and Toby know

**[17:02]** let us know you can let me and Toby know in person and also you know just shoot

**[17:05]** in person and also you know just shoot

**[17:05]** in person and also you know just shoot us an email um yep

**[17:09]** us an email um yep

**[17:09]** us an email um yep and if you ask you know what is our

**[17:11]** and if you ask you know what is our

**[17:11]** and if you ask you know what is our biggest bottleneck right right now uh

**[17:13]** biggest bottleneck right right now uh

**[17:13]** biggest bottleneck right right now uh because we're after this mission of

**[17:15]** because we're after this mission of

**[17:15]** because we're after this mission of building a model that can work on any

**[17:17]** building a model that can work on any

**[17:17]** building a model that can work on any robot to perform any task. Um it's a

**[17:21]** robot to perform any task. Um it's a

**[17:21]** robot to perform any task. Um it's a scientific problem, engineering problem,

**[17:23]** scientific problem, engineering problem,

**[17:24]** scientific problem, engineering problem, operation problem that are far from

**[17:25]** operation problem that are far from

**[17:25]** operation problem that are far from being solved. And so our biggest

**[17:27]** being solved. And so our biggest

**[17:27]** being solved. And so our biggest bottleneck really is we need the best

**[17:29]** bottleneck really is we need the best

**[17:29]** bottleneck really is we need the best people in the world in this area to help

**[17:30]** people in the world in this area to help

**[17:30]** people in the world in this area to help us assate progress. Um and so for a

**[17:33]** us assate progress. Um and so for a

**[17:34]** us assate progress. Um and so for a research organization, you know, any

**[17:35]** research organization, you know, any

**[17:35]** research organization, you know, any role that you might think we might need,

**[17:37]** role that you might think we might need,

**[17:37]** role that you might think we might need, we're hiring for it. Even if there is a

**[17:39]** we're hiring for it. Even if there is a

**[17:39]** we're hiring for it. Even if there is a role that you think you're exceptional

**[17:41]** role that you think you're exceptional

**[17:41]** role that you think you're exceptional at that you know we don't have on our

**[17:42]** at that you know we don't have on our

**[17:42]** at that you know we don't have on our website, please feel free to also let us

**[17:44]** website, please feel free to also let us

**[17:44]** website, please feel free to also let us know that you know you should really be

**[17:46]** know that you know you should really be

**[17:46]** know that you know you should really be hiring for this role and happy to have a

**[17:47]** hiring for this role and happy to have a

**[17:47]** hiring for this role and happy to have a conversation with you about it. Um again

**[17:50]** conversation with you about it. Um again

**[17:50]** conversation with you about it. Um again you can talk to me and Toby in person

**[17:53]** you can talk to me and Toby in person

**[17:53]** you can talk to me and Toby in person about you know what is how hiring needs

**[17:54]** about you know what is how hiring needs

**[17:54]** about you know what is how hiring needs right now but you can also apply online

**[17:56]** right now but you can also apply online

**[17:56]** right now but you can also apply online and shoot us a DM on Twitter. Uh thank

**[17:58]** and shoot us a DM on Twitter. Uh thank

**[17:58]** and shoot us a DM on Twitter. Uh thank you for listening.


### [18:00 - 19:00]

**[18:00]** you for listening.

**[18:00]** you for listening. [Applause]

**[18:02]** [Applause]

**[18:02]** [Applause] [Music]


