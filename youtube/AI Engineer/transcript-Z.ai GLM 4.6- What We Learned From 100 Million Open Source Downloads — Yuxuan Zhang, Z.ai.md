# Z.ai GLM 4.6- What We Learned From 100 Million Open Source Downloads — Yuxuan Zhang, Z.ai

**Video URL:** https://www.youtube.com/watch?v=m6MF1OR_9kM

---

## Full Transcript

### [00:00 - 01:00]

**[00:05]** Hello everyone. I'm John from VAI and

**[00:05]** Hello everyone. I'm John from VAI and I'm very happy to here to talk about our

**[00:08]** I'm very happy to here to talk about our

**[00:08]** I'm very happy to here to talk about our latest model series uh J 4.6 series. And

**[00:13]** latest model series uh J 4.6 series. And

**[00:13]** latest model series uh J 4.6 series. And let's jump right in.

**[00:21]** First uh I will introduce the GM series

**[00:21]** First uh I will introduce the GM series model.

**[00:23]** model.

**[00:23]** model. Gen 4.6 Six is not our first open source

**[00:26]** Gen 4.6 Six is not our first open source

**[00:26]** Gen 4.6 Six is not our first open source model since 2022 starting from the very

**[00:30]** model since 2022 starting from the very

**[00:30]** model since 2022 starting from the very first G30B.

**[00:33]** first G30B.

**[00:33]** first G30B. We have been quite serious about open

**[00:35]** We have been quite serious about open

**[00:35]** We have been quite serious about open source our work. Over the years, we have

**[00:38]** source our work. Over the years, we have

**[00:38]** source our work. Over the years, we have released a whole family of models such

**[00:41]** released a whole family of models such

**[00:41]** released a whole family of models such as chat gem 6p for language model and

**[00:44]** as chat gem 6p for language model and

**[00:44]** as chat gem 6p for language model and the code for vision understanding code

**[00:47]** the code for vision understanding code

**[00:47]** the code for vision understanding code view for image generation and the video

**[00:50]** view for image generation and the video

**[00:50]** view for image generation and the video for video generation and the very uh

**[00:53]** for video generation and the very uh

**[00:53]** for video generation and the very uh many more across the different domains

**[00:55]** many more across the different domains

**[00:55]** many more across the different domains and on this side you can see a map of

**[00:58]** and on this side you can see a map of

**[00:58]** and on this side you can see a map of our open source model so far and include


### [01:00 - 02:00]

**[01:01]** our open source model so far and include

**[01:02]** our open source model so far and include the different color such as the white is

**[01:04]** the different color such as the white is

**[01:04]** the different color such as the white is for the language model the z GM series

**[01:07]** for the language model the z GM series

**[01:07]** for the language model the z GM series and the pink for the multi mode

**[01:09]** and the pink for the multi mode

**[01:09]** and the pink for the multi mode understanding such as the code VM and

**[01:12]** understanding such as the code VM and

**[01:12]** understanding such as the code VM and now it's called GMV and the green one is

**[01:15]** now it's called GMV and the green one is

**[01:15]** now it's called GMV and the green one is for image generation and the yellow is

**[01:17]** for image generation and the yellow is

**[01:17]** for image generation and the yellow is for video generation.

**[01:20]** for video generation.

**[01:20]** for video generation. Uh 2025 is our open source year of and

**[01:25]** Uh 2025 is our open source year of and

**[01:25]** Uh 2025 is our open source year of and in this year we added even more models

**[01:28]** in this year we added even more models

**[01:28]** in this year we added even more models including the GM4 0414 dense model

**[01:32]** including the GM4 0414 dense model

**[01:32]** including the GM4 0414 dense model including like 9B and 32B and the GM4.5

**[01:37]** including like 9B and 32B and the GM4.5

**[01:37]** including like 9B and 32B and the GM4.5 G4.6 M O series model which is actually

**[01:41]** G4.6 M O series model which is actually

**[01:41]** G4.6 M O series model which is actually our first MO models family. So up to now

**[01:46]** our first MO models family. So up to now

**[01:46]** our first MO models family. So up to now we have released over 65 module in total

**[01:51]** we have released over 65 module in total

**[01:51]** we have released over 65 module in total and the closed platform like hing face

**[01:53]** and the closed platform like hing face

**[01:53]** and the closed platform like hing face monoscope and others we have already

**[01:56]** monoscope and others we have already

**[01:56]** monoscope and others we have already passed 100 million downloads. If you

**[01:59]** passed 100 million downloads. If you

**[01:59]** passed 100 million downloads. If you search for the GM or video on GitHub you


### [02:00 - 03:00]

**[02:02]** search for the GM or video on GitHub you

**[02:02]** search for the GM or video on GitHub you will find 105 1,500 community project

**[02:06]** will find 105 1,500 community project

**[02:06]** will find 105 1,500 community project really top of them and is much a

**[02:09]** really top of them and is much a

**[02:09]** really top of them and is much a communitydriven ecosystem. Now

**[02:13]** communitydriven ecosystem. Now

**[02:13]** communitydriven ecosystem. Now let's move to uh GE 4.6.

**[02:17]** let's move to uh GE 4.6.

**[02:17]** let's move to uh GE 4.6. Uh I will introduce it now.

**[02:20]** Uh I will introduce it now.

**[02:20]** Uh I will introduce it now. So G 4.6 is our latest flagship model or

**[02:25]** So G 4.6 is our latest flagship model or

**[02:25]** So G 4.6 is our latest flagship model or many public benchmark especially in math

**[02:28]** many public benchmark especially in math

**[02:28]** many public benchmark especially in math and coding. G 4.6 shows a clear game

**[02:31]** and coding. G 4.6 shows a clear game

**[02:31]** and coding. G 4.6 shows a clear game over GM 4.5.

**[02:34]** over GM 4.5.

**[02:34]** over GM 4.5. It also output opensource model release

**[02:36]** It also output opensource model release

**[02:36]** It also output opensource model release in the same period like dipstick version

**[02:39]** in the same period like dipstick version

**[02:39]** in the same period like dipstick version 3.2.

**[02:40]** 3.2.

**[02:40]** 3.2. and even beat this commercial model such

**[02:43]** and even beat this commercial model such

**[02:43]** and even beat this commercial model such as the cloud SOS 4 on several

**[02:45]** as the cloud SOS 4 on several

**[02:45]** as the cloud SOS 4 on several benchmarks.

**[02:47]** benchmarks.

**[02:47]** benchmarks. Of course, if we compare to the clock

**[02:49]** Of course, if we compare to the clock

**[02:49]** Of course, if we compare to the clock 4.5, there still be a noticeable uh

**[02:52]** 4.5, there still be a noticeable uh

**[02:52]** 4.5, there still be a noticeable uh noticeable gap. So, we are not coming

**[02:55]** noticeable gap. So, we are not coming

**[02:55]** noticeable gap. So, we are not coming with everything, but we're getting close

**[02:57]** with everything, but we're getting close

**[02:57]** with everything, but we're getting close and close.

**[02:59]** and close.

**[02:59]** and close. uh but what makes us especially happy is


### [03:00 - 04:00]

**[03:02]** uh but what makes us especially happy is

**[03:02]** uh but what makes us especially happy is here is um arena uh this benchmark

**[03:07]** here is um arena uh this benchmark

**[03:07]** here is um arena uh this benchmark uh this is uh which is closer to real

**[03:09]** uh this is uh which is closer to real

**[03:09]** uh this is uh which is closer to real user preference and on element arena gem

**[03:12]** user preference and on element arena gem

**[03:12]** user preference and on element arena gem 4.6 say it's time for number one

**[03:14]** 4.6 say it's time for number one

**[03:14]** 4.6 say it's time for number one together with GPD5 and the cost cross

**[03:18]** together with GPD5 and the cost cross

**[03:18]** together with GPD5 and the cost cross storage 4.5 and it's the only open

**[03:20]** storage 4.5 and it's the only open

**[03:20]** storage 4.5 and it's the only open source model here and so I'm very happy

**[03:24]** source model here and so I'm very happy

**[03:24]** source model here and so I'm very happy appreciate and I want to thank our

**[03:26]** appreciate and I want to thank our

**[03:26]** appreciate and I want to thank our developer who try to who try our model

**[03:29]** developer who try to who try our model

**[03:29]** developer who try to who try our model and votes for it so let's move to the CC

**[03:33]** and votes for it so let's move to the CC

**[03:33]** and votes for it so let's move to the CC bench

**[03:36]** bench

**[03:36]** bench so beside the user benchmark we also

**[03:39]** so beside the user benchmark we also

**[03:39]** so beside the user benchmark we also build our own data set called the CC

**[03:41]** build our own data set called the CC

**[03:42]** build our own data set called the CC bench Here we want to text agent style

**[03:44]** bench Here we want to text agent style

**[03:44]** bench Here we want to text agent style coding in real world not just iso lore

**[03:49]** coding in real world not just iso lore

**[03:49]** coding in real world not just iso lore problem. So we built a agent coding text

**[03:52]** problem. So we built a agent coding text

**[03:52]** problem. So we built a agent coding text platform based on the cloud code and on

**[03:55]** platform based on the cloud code and on

**[03:55]** platform based on the cloud code and on top of that we create CCB version 1.1.

**[03:58]** top of that we create CCB version 1.1.

**[03:58]** top of that we create CCB version 1.1. So compared with version one version one


### [04:00 - 05:00]

**[04:02]** So compared with version one version one

**[04:02]** So compared with version one version one uh the new version added 22 hard coding

**[04:05]** uh the new version added 22 hard coding

**[04:05]** uh the new version added 22 hard coding task and we statistically evaluate coco

**[04:09]** task and we statistically evaluate coco

**[04:09]** task and we statistically evaluate coco sonets a consonate 4 and g 4.5 the kim

**[04:13]** sonets a consonate 4 and g 4.5 the kim

**[04:13]** sonets a consonate 4 and g 4.5 the kim K2 and the versions 3.1 terminus

**[04:18]** K2 and the versions 3.1 terminus

**[04:18]** K2 and the versions 3.1 terminus in total citybench have 74 tasks is

**[04:22]** in total citybench have 74 tasks is

**[04:22]** in total citybench have 74 tasks is covering the front end development and

**[04:25]** covering the front end development and

**[04:25]** covering the front end development and internal tool development in the data

**[04:26]** internal tool development in the data

**[04:26]** internal tool development in the data analyze and also So algorithm

**[04:28]** analyze and also So algorithm

**[04:28]** analyze and also So algorithm implementation. So for every model we

**[04:32]** implementation. So for every model we

**[04:32]** implementation. So for every model we record the full agent trader query the

**[04:34]** record the full agent trader query the

**[04:34]** record the full agent trader query the planning st the call and code adds and

**[04:37]** planning st the call and code adds and

**[04:38]** planning st the call and code adds and execution the fully open source this

**[04:40]** execution the fully open source this

**[04:40]** execution the fully open source this benchmark. So you can check all the link

**[04:43]** benchmark. So you can check all the link

**[04:43]** benchmark. So you can check all the link later uh below in the hiring phase and

**[04:45]** later uh below in the hiring phase and

**[04:45]** later uh below in the hiring phase and JM 4.6 made a clear jump over June 4.5

**[04:49]** JM 4.6 made a clear jump over June 4.5

**[04:49]** JM 4.6 made a clear jump over June 4.5 and over uh over performance is called

**[04:52]** and over uh over performance is called

**[04:52]** and over uh over performance is called to call 4 with about 68.6% 6% win rate

**[04:57]** to call 4 with about 68.6% 6% win rate

**[04:57]** to call 4 with about 68.6% 6% win rate while being significant better than

**[04:59]** while being significant better than

**[04:59]** while being significant better than under open source baseline. So uh where


### [05:00 - 06:00]

**[05:02]** under open source baseline. So uh where

**[05:02]** under open source baseline. So uh where does the performance come from? A lot of

**[05:05]** does the performance come from? A lot of

**[05:05]** does the performance come from? A lot of uh let's talk about GM 4.6 training

**[05:08]** uh let's talk about GM 4.6 training

**[05:08]** uh let's talk about GM 4.6 training and in this uh we will start from the

**[05:13]** and in this uh we will start from the

**[05:13]** and in this uh we will start from the data v training design. First part is

**[05:15]** data v training design. First part is

**[05:16]** data v training design. First part is the general pre-training. So we start

**[05:19]** the general pre-training. So we start

**[05:19]** the general pre-training. So we start with about 15 billion uh 15 trillion

**[05:22]** with about 15 billion uh 15 trillion

**[05:22]** with about 15 billion uh 15 trillion tokens of the generate proposal data

**[05:25]** tokens of the generate proposal data

**[05:25]** tokens of the generate proposal data includes web page books uh acupedia and

**[05:29]** includes web page books uh acupedia and

**[05:29]** includes web page books uh acupedia and multilang multi uh multilingual content

**[05:32]** multilang multi uh multilingual content

**[05:32]** multilang multi uh multilingual content and so on. So this stage is about

**[05:35]** and so on. So this stage is about

**[05:35]** and so on. So this stage is about building a strong allrounder best model.

**[05:38]** building a strong allrounder best model.

**[05:38]** building a strong allrounder best model. The contest then here is 4,000 tokens

**[05:41]** The contest then here is 4,000 tokens

**[05:41]** The contest then here is 4,000 tokens and the next step is called the

**[05:43]** and the next step is called the

**[05:43]** and the next step is called the reasoning continue training. So on top

**[05:47]** reasoning continue training. So on top

**[05:47]** reasoning continue training. So on top of that base with about 7 trillion token

**[05:50]** of that base with about 7 trillion token

**[05:50]** of that base with about 7 trillion token of extra code and reasoning data. So

**[05:53]** of extra code and reasoning data. So

**[05:53]** of extra code and reasoning data. So it's part of this part of this counts

**[05:55]** it's part of this part of this counts

**[05:56]** it's part of this part of this counts for a high quality open source reports

**[05:57]** for a high quality open source reports

**[05:58]** for a high quality open source reports and another part is math science and


### [06:00 - 07:00]

**[06:01]** and another part is math science and

**[06:01]** and another part is math science and context program with four stepbystep

**[06:03]** context program with four stepbystep

**[06:03]** context program with four stepbystep reasoning.

**[06:05]** reasoning.

**[06:05]** reasoning. Then we come to the mid training. So we

**[06:08]** Then we come to the mid training. So we

**[06:08]** Then we come to the mid training. So we move to ripple label codes uh include

**[06:11]** move to ripple label codes uh include

**[06:11]** move to ripple label codes uh include that multiple files issues and pull

**[06:14]** that multiple files issues and pull

**[06:14]** that multiple files issues and pull request and the difference from the same

**[06:17]** request and the difference from the same

**[06:17]** request and the difference from the same project and all these packed into one

**[06:19]** project and all these packed into one

**[06:19]** project and all these packed into one long contains and the goal is to teach

**[06:22]** long contains and the goal is to teach

**[06:22]** long contains and the goal is to teach the model to following the close file

**[06:25]** the model to following the close file

**[06:25]** the model to following the close file and understand the chains and to also

**[06:29]** and understand the chains and to also

**[06:29]** and understand the chains and to also understand the pro square chains and

**[06:32]** understand the pro square chains and

**[06:32]** understand the pro square chains and read the real project structure end to

**[06:34]** read the real project structure end to

**[06:34]** read the real project structure end to end. So at this stage we stand the

**[06:36]** end. So at this stage we stand the

**[06:36]** end. So at this stage we stand the content to 32,000

**[06:39]** content to 32,000

**[06:39]** content to 32,000 and the model can basically see the key

**[06:42]** and the model can basically see the key

**[06:42]** and the model can basically see the key file of a medium size ripple on one

**[06:45]** file of a medium size ripple on one

**[06:45]** file of a medium size ripple on one shot.

**[06:47]** shot.

**[06:47]** shot. Then is a synetic reasoning data. We

**[06:50]** Then is a synetic reasoning data. We

**[06:50]** Then is a synetic reasoning data. We added about 500 billion token of synetic

**[06:53]** added about 500 billion token of synetic

**[06:53]** added about 500 billion token of synetic reasoning data. So it cover map science

**[06:56]** reasoning data. So it cover map science

**[06:56]** reasoning data. So it cover map science and algorithm with experience thinking

**[06:58]** and algorithm with experience thinking

**[06:58]** and algorithm with experience thinking trace. So it's mean the lay of the


### [07:00 - 08:00]

**[07:00]** trace. So it's mean the lay of the

**[07:00]** trace. So it's mean the lay of the groundwork of future agent behavior like

**[07:04]** groundwork of future agent behavior like

**[07:04]** groundwork of future agent behavior like breaking down the task refle uh

**[07:06]** breaking down the task refle uh

**[07:06]** breaking down the task refle uh reflecting on the mistake and doing

**[07:08]** reflecting on the mistake and doing

**[07:08]** reflecting on the mistake and doing longchain reasoning. Uh the next step is

**[07:11]** longchain reasoning. Uh the next step is

**[07:11]** longchain reasoning. Uh the next step is the long content and agent data. Uh

**[07:14]** the long content and agent data. Uh

**[07:14]** the long content and agent data. Uh finally we use about 100 billion token

**[07:17]** finally we use about 100 billion token

**[07:17]** finally we use about 100 billion token of a long content and agent data. Here

**[07:19]** of a long content and agent data. Here

**[07:19]** of a long content and agent data. Here the secret then is now pushed further to

**[07:22]** the secret then is now pushed further to

**[07:22]** the secret then is now pushed further to 180 uh 20 uh 128,000 for GM 4.6 is

**[07:27]** 180 uh 20 uh 128,000 for GM 4.6 is

**[07:27]** 180 uh 20 uh 128,000 for GM 4.6 is 200,000. So the model can handle four

**[07:30]** 200,000. So the model can handle four

**[07:30]** 200,000. So the model can handle four documents and the whole data uh code

**[07:33]** documents and the whole data uh code

**[07:33]** documents and the whole data uh code base and very long chart at the same

**[07:35]** base and very long chart at the same

**[07:35]** base and very long chart at the same time we feed lots of agent chery. So

**[07:38]** time we feed lots of agent chery. So

**[07:38]** time we feed lots of agent chery. So include that multi-step two calls the

**[07:40]** include that multi-step two calls the

**[07:40]** include that multi-step two calls the search and the code execution extra. So

**[07:45]** search and the code execution extra. So

**[07:45]** search and the code execution extra. So uh in this space improve the model long

**[07:47]** uh in this space improve the model long

**[07:48]** uh in this space improve the model long content capability and the aging

**[07:49]** content capability and the aging

**[07:49]** content capability and the aging capability.

**[07:51]** capability.

**[07:51]** capability. Also in this slide we introduce slide

**[07:54]** Also in this slide we introduce slide

**[07:54]** Also in this slide we introduce slide and it's our reinforcement learning

**[07:56]** and it's our reinforcement learning

**[07:56]** and it's our reinforcement learning framework and based on eston inference

**[07:59]** framework and based on eston inference

**[07:59]** framework and based on eston inference stack uh in practice uh we design in


### [08:00 - 09:00]

**[08:05]** stack uh in practice uh we design in

**[08:05]** stack uh in practice uh we design in house training framework here and we

**[08:07]** house training framework here and we

**[08:07]** house training framework here and we also open source it uh we found that the

**[08:10]** also open source it uh we found that the

**[08:10]** also open source it uh we found that the different task need very different

**[08:12]** different task need very different

**[08:12]** different task need very different system design

**[08:15]** system design

**[08:15]** system design for short reasoning task like the math

**[08:17]** for short reasoning task like the math

**[08:17]** for short reasoning task like the math or the code completion. So the best

**[08:19]** or the code completion. So the best

**[08:19]** or the code completion. So the best setup is clocked uh with the average

**[08:23]** setup is clocked uh with the average

**[08:23]** setup is clocked uh with the average agriculture. So we train inference in

**[08:26]** agriculture. So we train inference in

**[08:26]** agriculture. So we train inference in the same GPU. So after one batch update

**[08:28]** the same GPU. So after one batch update

**[08:28]** the same GPU. So after one batch update wave. So the next batch immediately

**[08:31]** wave. So the next batch immediately

**[08:31]** wave. So the next batch immediately sample for the latest policy. the

**[08:33]** sample for the latest policy. the

**[08:33]** sample for the latest policy. the screens the most of GPU memory and

**[08:35]** screens the most of GPU memory and

**[08:35]** screens the most of GPU memory and compute and but for agent task and for

**[08:39]** compute and but for agent task and for

**[08:39]** compute and but for agent task and for example the real software engineering uh

**[08:43]** example the real software engineering uh

**[08:43]** example the real software engineering uh usually have many steps like for example

**[08:46]** usually have many steps like for example

**[08:46]** usually have many steps like for example open the browser and hit uh backend API

**[08:49]** open the browser and hit uh backend API

**[08:49]** open the browser and hit uh backend API and for the external response um extra

**[08:53]** and for the external response um extra

**[08:53]** and for the external response um extra so if we force every worker to stay in

**[08:56]** so if we force every worker to stay in

**[08:56]** so if we force every worker to stay in the sameness the forces the get dragged

**[08:59]** the sameness the forces the get dragged

**[08:59]** the sameness the forces the get dragged down by the service field and GPU


### [09:00 - 10:00]

**[09:03]** down by the service field and GPU

**[09:03]** down by the service field and GPU So in slide we decide he agriculture to

**[09:06]** So in slide we decide he agriculture to

**[09:06]** So in slide we decide he agriculture to support both uh

**[09:10]** support both uh

**[09:10]** support both uh and secret model. If you look at the

**[09:13]** and secret model. If you look at the

**[09:13]** and secret model. If you look at the diagramraph the blue part is meatron

**[09:16]** diagramraph the blue part is meatron

**[09:16]** diagramraph the blue part is meatron batch training engine w for data buffer

**[09:19]** batch training engine w for data buffer

**[09:19]** batch training engine w for data buffer and opposite ways and the green pause is

**[09:22]** and opposite ways and the green pause is

**[09:22]** and opposite ways and the green pause is high throughout intervention coaster. So

**[09:25]** high throughout intervention coaster. So

**[09:25]** high throughout intervention coaster. So with a routine of dispatch request and

**[09:28]** with a routine of dispatch request and

**[09:28]** with a routine of dispatch request and in the middle the data buffer act like

**[09:30]** in the middle the data buffer act like

**[09:30]** in the middle the data buffer act like the share nist systems. So one side

**[09:33]** the share nist systems. So one side

**[09:33]** the share nist systems. So one side connect training and other side

**[09:35]** connect training and other side

**[09:35]** connect training and other side differential agent environments for

**[09:37]** differential agent environments for

**[09:37]** differential agent environments for regular reinforcement learning cost. We

**[09:39]** regular reinforcement learning cost. We

**[09:39]** regular reinforcement learning cost. We keep training and in uh inference on the

**[09:41]** keep training and in uh inference on the

**[09:41]** keep training and in uh inference on the same GPU pool using with a sim mode and

**[09:44]** same GPU pool using with a sim mode and

**[09:44]** same GPU pool using with a sim mode and dynamic sampling instant update and the

**[09:47]** dynamic sampling instant update and the

**[09:47]** dynamic sampling instant update and the maximum throughputs. Once we switch

**[09:49]** maximum throughputs. Once we switch

**[09:49]** maximum throughputs. Once we switch reach to complete agent task we move to

**[09:52]** reach to complete agent task we move to

**[09:52]** reach to complete agent task we move to a decouple and synchroniz mode. So the

**[09:55]** a decouple and synchroniz mode. So the

**[09:55]** a decouple and synchroniz mode. So the row outside port talks directly to real

**[09:58]** row outside port talks directly to real

**[09:58]** row outside port talks directly to real environments and just regenerate

**[09:59]** environments and just regenerate

**[09:59]** environments and just regenerate tractory and write them into the buffer


### [10:00 - 11:00]

**[10:02]** tractory and write them into the buffer

**[10:02]** tractory and write them into the buffer and then the training side consume the

**[10:04]** and then the training side consume the

**[10:04]** and then the training side consume the data in own space up the model and uh

**[10:09]** data in own space up the model and uh

**[10:09]** data in own space up the model and uh periodically push new way.

**[10:13]** periodically push new way.

**[10:14]** periodically push new way. So the nice thing is even if some tasks

**[10:16]** So the nice thing is even if some tasks

**[10:16]** So the nice thing is even if some tasks super slow they don't block the whole

**[10:19]** super slow they don't block the whole

**[10:19]** super slow they don't block the whole training pipeline. So on top of that we

**[10:22]** training pipeline. So on top of that we

**[10:22]** training pipeline. So on top of that we have done a branch of efficiency

**[10:24]** have done a branch of efficiency

**[10:24]** have done a branch of efficiency optimization

**[10:25]** optimization

**[10:25]** optimization [Music]

**[10:26]** [Music]

**[10:26]** [Music] like the main chain still run flow 16 uh

**[10:31]** like the main chain still run flow 16 uh

**[10:31]** like the main chain still run flow 16 uh stability but after each policy update

**[10:34]** stability but after each policy update

**[10:34]** stability but after each policy update we do blockwise FDA cronization on the

**[10:37]** we do blockwise FDA cronization on the

**[10:37]** we do blockwise FDA cronization on the latest ways and send FPA version through

**[10:40]** latest ways and send FPA version through

**[10:40]** latest ways and send FPA version through our work. So the most expensive part the

**[10:43]** our work. So the most expensive part the

**[10:44]** our work. So the most expensive part the data generation and running FDA with

**[10:46]** data generation and running FDA with

**[10:46]** data generation and running FDA with much higher output while training this

**[10:49]** much higher output while training this

**[10:49]** much higher output while training this keep BF BF16 precision. So in practice

**[10:53]** keep BF BF16 precision. So in practice

**[10:53]** keep BF BF16 precision. So in practice we will get the benefit both accuracy

**[10:55]** we will get the benefit both accuracy

**[10:56]** we will get the benefit both accuracy and speed in this framework.


### [11:00 - 12:00]

**[11:03]** Now let's zoom in reasonal ISO and this

**[11:03]** Now let's zoom in reasonal ISO and this slide with some plots. So the first one

**[11:06]** slide with some plots. So the first one

**[11:06]** slide with some plots. So the first one is about the two-stage curriculum we

**[11:08]** is about the two-stage curriculum we

**[11:08]** is about the two-stage curriculum we use. We don't change all the fixed data

**[11:11]** use. We don't change all the fixed data

**[11:11]** use. We don't change all the fixed data set from start to finish. Instead, we

**[11:13]** set from start to finish. Instead, we

**[11:13]** set from start to finish. Instead, we use a two-stage difficulty curriculum.

**[11:15]** use a two-stage difficulty curriculum.

**[11:15]** use a two-stage difficulty curriculum. In stage one, we use medium difficulty

**[11:18]** In stage one, we use medium difficulty

**[11:18]** In stage one, we use medium difficulty problem. In each batch, some arrive in

**[11:21]** problem. In each batch, some arrive in

**[11:21]** problem. In each batch, some arrive in some room. So, the rewards have various

**[11:23]** some room. So, the rewards have various

**[11:24]** some room. So, the rewards have various in the grinding are meaningful. All the

**[11:26]** in the grinding are meaningful. All the

**[11:26]** in the grinding are meaningful. All the model get stronger with which you

**[11:29]** model get stronger with which you

**[11:29]** model get stronger with which you extremely hard problem in stage two. But

**[11:32]** extremely hard problem in stage two. But

**[11:32]** extremely hard problem in stage two. But with 512 samples, you can still

**[11:35]** with 512 samples, you can still

**[11:35]** with 512 samples, you can still occasionally get a correct solution. So

**[11:37]** occasionally get a correct solution. So

**[11:38]** occasionally get a correct solution. So you can see on the pause the blue curve

**[11:40]** you can see on the pause the blue curve

**[11:40]** you can see on the pause the blue curve is our method after switching to hard

**[11:42]** is our method after switching to hard

**[11:42]** is our method after switching to hard problem the curve is keep going up.

**[11:45]** problem the curve is keep going up.

**[11:45]** problem the curve is keep going up. However use the uh median difficulty the

**[11:47]** However use the uh median difficulty the

**[11:47]** However use the uh median difficulty the way uh is not on the red curve. The next

**[11:51]** way uh is not on the red curve. The next

**[11:51]** way uh is not on the red curve. The next picture is about a single stage

**[11:54]** picture is about a single stage

**[11:54]** picture is about a single stage reinforcement learning as 64,000 tokens.

**[11:58]** reinforcement learning as 64,000 tokens.

**[11:58]** reinforcement learning as 64,000 tokens. Some previous works such as multi-stage


### [12:00 - 13:00]

**[12:00]** Some previous works such as multi-stage

**[12:00]** Some previous works such as multi-stage reason uh reinforcement.

**[12:03]** reason uh reinforcement.

**[12:03]** reason uh reinforcement. for is that uh for example is uh 16 then

**[12:07]** for is that uh for example is uh 16 then

**[12:07]** for is that uh for example is uh 16 then 32 then 48 and finally 6 64 but we found

**[12:11]** 32 then 48 and finally 6 64 but we found

**[12:12]** 32 then 48 and finally 6 64 but we found that for model that is already been

**[12:14]** that for model that is already been

**[12:14]** that for model that is already been trained with 64,000 token uh SFT those

**[12:20]** trained with 64,000 token uh SFT those

**[12:20]** trained with 64,000 token uh SFT those shorter IO strange actually make you

**[12:22]** shorter IO strange actually make you

**[12:22]** shorter IO strange actually make you forget it long content ability so

**[12:24]** forget it long content ability so

**[12:24]** forget it long content ability so average upper listings and the finals

**[12:28]** average upper listings and the finals

**[12:28]** average upper listings and the finals 64k token stage can't fully recover the

**[12:31]** 64k token stage can't fully recover the

**[12:31]** 64k token stage can't fully recover the loss

**[12:32]** loss

**[12:32]** loss So the red curve here is our approach.

**[12:35]** So the red curve here is our approach.

**[12:35]** So the red curve here is our approach. We start directly with 40 uh 64,000

**[12:40]** We start directly with 40 uh 64,000

**[12:40]** We start directly with 40 uh 64,000 uh token and train in one single stage

**[12:43]** uh token and train in one single stage

**[12:43]** uh token and train in one single stage re is clearly outperform than the blue

**[12:47]** re is clearly outperform than the blue

**[12:47]** re is clearly outperform than the blue middle multi-stage curve. Uh

**[12:51]** middle multi-stage curve. Uh

**[12:51]** middle multi-stage curve. Uh the the picture below is about the code.

**[12:55]** the the picture below is about the code.

**[12:55]** the the picture below is about the code. So on the left bottom we complain two

**[12:58]** So on the left bottom we complain two

**[12:58]** So on the left bottom we complain two ways of committing the laws for code. So


### [13:00 - 14:00]

**[13:01]** ways of committing the laws for code. So

**[13:01]** ways of committing the laws for code. So the blue one is classic sequence means

**[13:03]** the blue one is classic sequence means

**[13:03]** the blue one is classic sequence means loss is sequence has one loss value and

**[13:07]** loss is sequence has one loss value and

**[13:07]** loss is sequence has one loss value and the red one is our token w means loss

**[13:10]** the red one is our token w means loss

**[13:10]** the red one is our token w means loss which average over token instead of

**[13:12]** which average over token instead of

**[13:12]** which average over token instead of sequence. The token w version converts

**[13:15]** sequence. The token w version converts

**[13:15]** sequence. The token w version converts faster and most steadily and it reduce

**[13:18]** faster and most steadily and it reduce

**[13:18]** faster and most steadily and it reduce the chances to generate very short

**[13:21]** the chances to generate very short

**[13:21]** the chances to generate very short template answer just to get the rewards.

**[13:24]** template answer just to get the rewards.

**[13:24]** template answer just to get the rewards. And the right you can see the data.

**[13:27]** And the right you can see the data.

**[13:27]** And the right you can see the data. uh we do get a science reinforcement

**[13:30]** uh we do get a science reinforcement

**[13:30]** uh we do get a science reinforcement learning on GPQA demons and the

**[13:34]** learning on GPQA demons and the

**[13:34]** learning on GPQA demons and the messaging almost opposite of more data

**[13:37]** messaging almost opposite of more data

**[13:37]** messaging almost opposite of more data is better. The red curve red curve is

**[13:40]** is better. The red curve red curve is

**[13:40]** is better. The red curve red curve is trained only the small set of expert

**[13:43]** trained only the small set of expert

**[13:43]** trained only the small set of expert verify but high quality multiple choice

**[13:47]** verify but high quality multiple choice

**[13:47]** verify but high quality multiple choice question and the blue curve use mixed

**[13:49]** question and the blue curve use mixed

**[13:50]** question and the blue curve use mixed quality data. So this result that a

**[13:52]** quality data. So this result that a

**[13:52]** quality data. So this result that a small blood clean data set gives much

**[13:56]** small blood clean data set gives much

**[13:56]** small blood clean data set gives much better performance. So for scientific

**[13:59]** better performance. So for scientific

**[13:59]** better performance. So for scientific reasoning data quality really matters


### [14:00 - 15:00]

**[14:02]** reasoning data quality really matters

**[14:02]** reasoning data quality really matters more than raw size.

**[14:06]** more than raw size.

**[14:06]** more than raw size. After talking about J 4.6 language model

**[14:09]** After talking about J 4.6 language model

**[14:09]** After talking about J 4.6 language model we move to the multimodel.

**[14:16]** J 4.5

**[14:16]** J 4.5 supports the both image and video

**[14:19]** supports the both image and video

**[14:19]** supports the both image and video understanding. It is our latest visual

**[14:21]** understanding. It is our latest visual

**[14:21]** understanding. It is our latest visual understanding model and go and on

**[14:24]** understanding model and go and on

**[14:24]** understanding model and go and on grounding and the image understanding

**[14:26]** grounding and the image understanding

**[14:26]** grounding and the image understanding benchmark it shows strong performance

**[14:29]** benchmark it shows strong performance

**[14:29]** benchmark it shows strong performance and the clear advantages over other open

**[14:31]** and the clear advantages over other open

**[14:31]** and the clear advantages over other open source model release around the same

**[14:33]** source model release around the same

**[14:33]** source model release around the same time.

**[14:35]** time.

**[14:35]** time. So agriculturally you have the three

**[14:37]** So agriculturally you have the three

**[14:37]** So agriculturally you have the three main PS here

**[14:41]** main PS here

**[14:41]** main PS here the one is a version transforming coord

**[14:45]** the one is a version transforming coord

**[14:45]** the one is a version transforming coord and then it's like with MLP projector

**[14:48]** and then it's like with MLP projector

**[14:48]** and then it's like with MLP projector and the finally is 4.5 base model at the

**[14:52]** and the finally is 4.5 base model at the

**[14:52]** and the finally is 4.5 base model at the coordinates. So we're trying hard to

**[14:54]** coordinates. So we're trying hard to

**[14:54]** coordinates. So we're trying hard to keep the virtual input as original as

**[14:57]** keep the virtual input as original as

**[14:57]** keep the virtual input as original as possible. So the model can see the image

**[14:59]** possible. So the model can see the image

**[14:59]** possible. So the model can see the image negative resolution and accept ratio


### [15:00 - 16:00]

**[15:02]** negative resolution and accept ratio

**[15:02]** negative resolution and accept ratio instead of focusing everything into a

**[15:04]** instead of focusing everything into a

**[15:04]** instead of focusing everything into a fixed square. So this matter a lot of us

**[15:07]** fixed square. So this matter a lot of us

**[15:07]** fixed square. So this matter a lot of us screenshot and also long vertical image

**[15:10]** screenshot and also long vertical image

**[15:10]** screenshot and also long vertical image and the pawn point slides. So looking

**[15:12]** and the pawn point slides. So looking

**[15:12]** and the pawn point slides. So looking for the video we also insert a time

**[15:15]** for the video we also insert a time

**[15:15]** for the video we also insert a time index token after each time basically

**[15:18]** index token after each time basically

**[15:18]** index token after each time basically telling model this is the friend C and

**[15:21]** telling model this is the friend C and

**[15:21]** telling model this is the friend C and this is the second T and they help it

**[15:23]** this is the second T and they help it

**[15:23]** this is the second T and they help it understand the temporal order and

**[15:25]** understand the temporal order and

**[15:25]** understand the temporal order and reience which is crucial for action

**[15:28]** reience which is crucial for action

**[15:28]** reience which is crucial for action understanding and step by step uh

**[15:30]** understanding and step by step uh

**[15:30]** understanding and step by step uh producer.

**[15:32]** producer.

**[15:32]** producer. Uh we also use a method uh as we

**[15:35]** Uh we also use a method uh as we

**[15:35]** Uh we also use a method uh as we researched before co uh in coke agent.

**[15:38]** researched before co uh in coke agent.

**[15:38]** researched before co uh in coke agent. Now the GUI agent capability is also

**[15:40]** Now the GUI agent capability is also

**[15:40]** Now the GUI agent capability is also support on GM 4.5 B. So you can like uh

**[15:45]** support on GM 4.5 B. So you can like uh

**[15:45]** support on GM 4.5 B. So you can like uh it can also help you to control the

**[15:46]** it can also help you to control the

**[15:46]** it can also help you to control the computer and also like the website to

**[15:49]** computer and also like the website to

**[15:49]** computer and also like the website to control uh you can use the mouse or the

**[15:53]** control uh you can use the mouse or the

**[15:53]** control uh you can use the mouse or the keyboard touching and to communicate

**[15:56]** keyboard touching and to communicate

**[15:56]** keyboard touching and to communicate with your uh browser also computer or

**[15:59]** with your uh browser also computer or

**[15:59]** with your uh browser also computer or mobile environments.


### [16:00 - 17:00]

**[16:02]** mobile environments.

**[16:02]** mobile environments. So how to use G 4.6 or G 4.5 V model.

**[16:07]** So how to use G 4.6 or G 4.5 V model.

**[16:07]** So how to use G 4.6 or G 4.5 V model. The first one is using a open source

**[16:09]** The first one is using a open source

**[16:10]** The first one is using a open source weight. Uh as we know this both these

**[16:12]** weight. Uh as we know this both these

**[16:12]** weight. Uh as we know this both these tool is open source. So you can use the

**[16:15]** tool is open source. So you can use the

**[16:15]** tool is open source. So you can use the echelon or v or other framework to

**[16:18]** echelon or v or other framework to

**[16:18]** echelon or v or other framework to inference it. Uh along with the weights

**[16:22]** inference it. Uh along with the weights

**[16:22]** inference it. Uh along with the weights on the release day we already had

**[16:24]** on the release day we already had

**[16:24]** on the release day we already had achelon and the vlm integrated ready and

**[16:27]** achelon and the vlm integrated ready and

**[16:27]** achelon and the vlm integrated ready and we also work with many third party open

**[16:29]** we also work with many third party open

**[16:29]** we also work with many third party open source frameworks like the llama factory

**[16:31]** source frameworks like the llama factory

**[16:31]** source frameworks like the llama factory or ms swift. So thank you to this

**[16:34]** or ms swift. So thank you to this

**[16:34]** or ms swift. So thank you to this community there you have you can choose

**[16:36]** community there you have you can choose

**[16:36]** community there you have you can choose uh any that framework you want and to

**[16:39]** uh any that framework you want and to

**[16:39]** uh any that framework you want and to try our model but

**[16:42]** try our model but

**[16:42]** try our model but the GM uh GM 4.6 model is a large model

**[16:45]** the GM uh GM 4.6 model is a large model

**[16:46]** the GM uh GM 4.6 model is a large model with like more than 35 uh 355

**[16:51]** with like more than 35 uh 355

**[16:51]** with like more than 35 uh 355 billion parameter. So if you don't have

**[16:53]** billion parameter. So if you don't have

**[16:53]** billion parameter. So if you don't have that 100 or like and other uh GPUs

**[16:58]** that 100 or like and other uh GPUs

**[16:58]** that 100 or like and other uh GPUs there's an easier way to uh use our


### [17:00 - 18:00]

**[17:01]** there's an easier way to uh use our

**[17:02]** there's an easier way to uh use our model. So in this slide we show the

**[17:03]** model. So in this slide we show the

**[17:04]** model. So in this slide we show the deploy uh command of using Helon or the

**[17:07]** deploy uh command of using Helon or the

**[17:07]** deploy uh command of using Helon or the VLM. Here

**[17:09]** VLM. Here

**[17:09]** VLM. Here the next slide uh we can use the GM on

**[17:13]** the next slide uh we can use the GM on

**[17:13]** the next slide uh we can use the GM on the Z. AI uh Z.AI AI. This is a website

**[17:17]** the Z. AI uh Z.AI AI. This is a website

**[17:17]** the Z. AI uh Z.AI AI. This is a website and you can try your uh directly

**[17:21]** and you can try your uh directly

**[17:22]** and you can try your uh directly and you can use the writing code you can

**[17:24]** and you can use the writing code you can

**[17:24]** and you can use the writing code you can using to generate powerpoints and so on.

**[17:28]** using to generate powerpoints and so on.

**[17:28]** using to generate powerpoints and so on. And in this uh demo is uh using

**[17:33]** And in this uh demo is uh using

**[17:33]** And in this uh demo is uh using one command to write the Google

**[17:35]** one command to write the Google

**[17:35]** one command to write the Google searching in our dat

**[17:38]** searching in our dat

**[17:38]** searching in our dat uh demo. So you can just uh communicate

**[17:41]** uh demo. So you can just uh communicate

**[17:41]** uh demo. So you can just uh communicate with it

**[17:43]** with it

**[17:43]** with it and also GM is famous in coding

**[17:47]** and also GM is famous in coding

**[17:47]** and also GM is famous in coding capability.

**[17:48]** capability.

**[17:48]** capability. So we also provides the GM coding plan

**[17:51]** So we also provides the GM coding plan

**[17:52]** So we also provides the GM coding plan which connect GM with tools and other

**[17:55]** which connect GM with tools and other

**[17:55]** which connect GM with tools and other plugins that cloud code or other coding

**[17:59]** plugins that cloud code or other coding

**[17:59]** plugins that cloud code or other coding developer uh develop tools and to


### [18:00 - 19:00]

**[18:02]** developer uh develop tools and to

**[18:02]** developer uh develop tools and to provide a very strong coding assistant

**[18:05]** provide a very strong coding assistant

**[18:05]** provide a very strong coding assistant experience. We also have a short demo

**[18:08]** experience. We also have a short demo

**[18:08]** experience. We also have a short demo video that uh show how to replace Yodi

**[18:12]** video that uh show how to replace Yodi

**[18:12]** video that uh show how to replace Yodi model in a cocoa livea with gem 4.6 here

**[18:16]** model in a cocoa livea with gem 4.6 here

**[18:16]** model in a cocoa livea with gem 4.6 here and you can uh see the you can watch

**[18:19]** and you can uh see the you can watch

**[18:19]** and you can uh see the you can watch this on YouTube

**[18:31]** beyond today talk where regularly host

**[18:31]** beyond today talk where regularly host events both online and offline. So

**[18:34]** events both online and offline. So

**[18:34]** events both online and offline. So whenever we release a new model we

**[18:36]** whenever we release a new model we

**[18:36]** whenever we release a new model we usually run a several community session

**[18:38]** usually run a several community session

**[18:38]** usually run a several community session afterwards as the first one there is AMA

**[18:42]** afterwards as the first one there is AMA

**[18:42]** afterwards as the first one there is AMA in the Reddit and we also have some uh

**[18:45]** in the Reddit and we also have some uh

**[18:46]** in the Reddit and we also have some uh we also have some offline and onsite uh

**[18:50]** we also have some offline and onsite uh

**[18:50]** we also have some offline and onsite uh techn uh tech technology sharing so you

**[18:52]** techn uh tech technology sharing so you

**[18:52]** techn uh tech technology sharing so you can join us

**[18:55]** can join us

**[18:55]** can join us the final uh slide is some important

**[18:58]** the final uh slide is some important

**[18:58]** the final uh slide is some important link you may to know uh is about website


### [19:00 - 20:00]

**[19:03]** link you may to know uh is about website

**[19:03]** link you may to know uh is about website as I as I mentioned mentioned before to

**[19:05]** as I as I mentioned mentioned before to

**[19:05]** as I as I mentioned mentioned before to try GM model as ZAI and also our API on

**[19:10]** try GM model as ZAI and also our API on

**[19:10]** try GM model as ZAI and also our API on here then we also provide GM 4.6 six

**[19:13]** here then we also provide GM 4.6 six

**[19:13]** here then we also provide GM 4.6 six technical uh technical board and J4.5

**[19:17]** technical uh technical board and J4.5

**[19:17]** technical uh technical board and J4.5 tech reports. Uh you can check it and

**[19:21]** tech reports. Uh you can check it and

**[19:21]** tech reports. Uh you can check it and you want to join our community here is

**[19:23]** you want to join our community here is

**[19:23]** you want to join our community here is the discord link and also the GitHub

**[19:26]** the discord link and also the GitHub

**[19:26]** the discord link and also the GitHub link is below with the open source model

**[19:29]** link is below with the open source model

**[19:29]** link is below with the open source model including the readme to how to deploy on

**[19:32]** including the readme to how to deploy on

**[19:32]** including the readme to how to deploy on the open source method. That's all of

**[19:35]** the open source method. That's all of

**[19:35]** the open source method. That's all of today. Thank you very much.


