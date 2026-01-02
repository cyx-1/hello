# 2025 in LLMs so far, illustrated by Pelicans on Bicycles — Simon Willison

**Video URL:** https://www.youtube.com/watch?v=YpY83-kA7Bou

---

## Full Transcript

### [00:00 - 01:00]

**[00:24]** good morning AI engineers. Um, so when I

**[00:24]** good morning AI engineers. Um, so when I signed up for this talk, I said I was

**[00:25]** signed up for this talk, I said I was

**[00:25]** signed up for this talk, I said I was going to give a review of the last year

**[00:27]** going to give a review of the last year

**[00:27]** going to give a review of the last year in LLMs. With hindsight, that was very

**[00:29]** in LLMs. With hindsight, that was very

**[00:30]** in LLMs. With hindsight, that was very foolish. This space keeps on

**[00:31]** foolish. This space keeps on

**[00:31]** foolish. This space keeps on accelerating. I've had to cut my scope.

**[00:33]** accelerating. I've had to cut my scope.

**[00:33]** accelerating. I've had to cut my scope. I'm now down to the last six months in

**[00:35]** I'm now down to the last six months in

**[00:35]** I'm now down to the last six months in LLMs, and that's going to keep us pretty

**[00:37]** LLMs, and that's going to keep us pretty

**[00:37]** LLMs, and that's going to keep us pretty busy. Um, ju just covering that much.

**[00:40]** busy. Um, ju just covering that much.

**[00:40]** busy. Um, ju just covering that much. Um, the problem that we have is I

**[00:42]** Um, the problem that we have is I

**[00:42]** Um, the problem that we have is I counted 30 significant model releases in

**[00:45]** counted 30 significant model releases in

**[00:45]** counted 30 significant model releases in the past six months. And by significant,

**[00:47]** the past six months. And by significant,

**[00:47]** the past six months. And by significant, I mean if you are working in the space,

**[00:49]** I mean if you are working in the space,

**[00:49]** I mean if you are working in the space, you should at least be aware of them and

**[00:50]** you should at least be aware of them and

**[00:50]** you should at least be aware of them and somewhat familiar, like have a poke at

**[00:52]** somewhat familiar, like have a poke at

**[00:52]** somewhat familiar, like have a poke at them. That's a lot of different stuff.

**[00:53]** them. That's a lot of different stuff.

**[00:53]** them. That's a lot of different stuff. And the classic problem is, how do we

**[00:55]** And the classic problem is, how do we

**[00:55]** And the classic problem is, how do we tell which of them are any good? There

**[00:57]** tell which of them are any good? There

**[00:57]** tell which of them are any good? There are all of these benchmarks full of

**[00:58]** are all of these benchmarks full of

**[00:58]** are all of these benchmarks full of numbers. I don't like the numbers. There


### [01:00 - 02:00]

**[01:00]** numbers. I don't like the numbers. There

**[01:00]** numbers. I don't like the numbers. There are the leaderboards. I'm kind of

**[01:02]** are the leaderboards. I'm kind of

**[01:02]** are the leaderboards. I'm kind of beginning to lose trust in the

**[01:03]** beginning to lose trust in the

**[01:03]** beginning to lose trust in the leaderboards as well. So, for my own

**[01:05]** leaderboards as well. So, for my own

**[01:05]** leaderboards as well. So, for my own work, I've been leaning increasingly

**[01:07]** work, I've been leaning increasingly

**[01:07]** work, I've been leaning increasingly into my own little benchmark, which

**[01:09]** into my own little benchmark, which

**[01:09]** into my own little benchmark, which started as a joke and has actually

**[01:10]** started as a joke and has actually

**[01:10]** started as a joke and has actually turned into something that I I rely on

**[01:11]** turned into something that I I rely on

**[01:12]** turned into something that I I rely on quite a lot. And that's this. I prompt

**[01:13]** quite a lot. And that's this. I prompt

**[01:13]** quite a lot. And that's this. I prompt models with generate an SVG of a pelican

**[01:17]** models with generate an SVG of a pelican

**[01:17]** models with generate an SVG of a pelican riding a bicycle. I have good reasons

**[01:19]** riding a bicycle. I have good reasons

**[01:19]** riding a bicycle. I have good reasons for this. Um, firstly, these are not

**[01:21]** for this. Um, firstly, these are not

**[01:21]** for this. Um, firstly, these are not image models. These are text models.

**[01:22]** image models. These are text models.

**[01:22]** image models. These are text models. They shouldn't be able to draw anything

**[01:24]** They shouldn't be able to draw anything

**[01:24]** They shouldn't be able to draw anything at all, but they can output code and SVG

**[01:26]** at all, but they can output code and SVG

**[01:26]** at all, but they can output code and SVG is a kind of code. So, that works.

**[01:29]** is a kind of code. So, that works.

**[01:29]** is a kind of code. So, that works. Pelican riding a bicycle is actually a

**[01:30]** Pelican riding a bicycle is actually a

**[01:30]** Pelican riding a bicycle is actually a really challenging problem because

**[01:32]** really challenging problem because

**[01:32]** really challenging problem because firstly, try drawing a bicycle yourself.

**[01:35]** firstly, try drawing a bicycle yourself.

**[01:35]** firstly, try drawing a bicycle yourself. Most people in this room will fail. You

**[01:37]** Most people in this room will fail. You

**[01:37]** Most people in this room will fail. You will find that you can't actually quite

**[01:38]** will find that you can't actually quite

**[01:38]** will find that you can't actually quite remember how the different triangles fit

**[01:39]** remember how the different triangles fit

**[01:39]** remember how the different triangles fit together. Likewise, pelicans, glorious

**[01:42]** together. Likewise, pelicans, glorious

**[01:42]** together. Likewise, pelicans, glorious animals, very difficult to draw. And on

**[01:44]** animals, very difficult to draw. And on

**[01:44]** animals, very difficult to draw. And on top of all of that, pelicans can't ride

**[01:46]** top of all of that, pelicans can't ride

**[01:46]** top of all of that, pelicans can't ride bicycles. They're the wrong shape. So,

**[01:48]** bicycles. They're the wrong shape. So,

**[01:48]** bicycles. They're the wrong shape. So, we're kind of giving them an impossible

**[01:50]** we're kind of giving them an impossible

**[01:50]** we're kind of giving them an impossible task with this. What I love about this

**[01:51]** task with this. What I love about this

**[01:52]** task with this. What I love about this task though is they try really hard and

**[01:54]** task though is they try really hard and

**[01:54]** task though is they try really hard and they include comments. So you can see

**[01:55]** they include comments. So you can see

**[01:55]** they include comments. So you can see little comments in the SVG code where

**[01:57]** little comments in the SVG code where

**[01:57]** little comments in the SVG code where they're saying, "Well, now I'm going to

**[01:58]** they're saying, "Well, now I'm going to

**[01:58]** they're saying, "Well, now I'm going to draw the bicycles, draw the wheels, I'll


### [02:00 - 03:00]

**[02:00]** draw the bicycles, draw the wheels, I'll

**[02:00]** draw the bicycles, draw the wheels, I'll try." It's it's kind of fun. Um, so

**[02:03]** try." It's it's kind of fun. Um, so

**[02:03]** try." It's it's kind of fun. Um, so rewind back to December. December in LMS

**[02:06]** rewind back to December. December in LMS

**[02:06]** rewind back to December. December in LMS was a lot a lot of stuff happened. Um,

**[02:09]** was a lot a lot of stuff happened. Um,

**[02:09]** was a lot a lot of stuff happened. Um, the first release of that month was AWS

**[02:11]** the first release of that month was AWS

**[02:11]** the first release of that month was AWS Nova. Amazon Nova. Amazon finally put

**[02:14]** Nova. Amazon Nova. Amazon finally put

**[02:14]** Nova. Amazon Nova. Amazon finally put out models that didn't suck. They're

**[02:16]** out models that didn't suck. They're

**[02:16]** out models that didn't suck. They're quite good. They're not great at drawing

**[02:18]** quite good. They're not great at drawing

**[02:18]** quite good. They're not great at drawing pelicans. like the the the Pelicans are

**[02:20]** pelicans. like the the the Pelicans are

**[02:20]** pelicans. like the the the Pelicans are unimpressive, but these models are a

**[02:22]** unimpressive, but these models are a

**[02:22]** unimpressive, but these models are a million token contexts. They behave like

**[02:24]** million token contexts. They behave like

**[02:24]** million token contexts. They behave like the cheaper Gemini models. They are dirt

**[02:26]** the cheaper Gemini models. They are dirt

**[02:26]** the cheaper Gemini models. They are dirt cheap. I believe Nova Micro is the

**[02:30]** cheap. I believe Nova Micro is the

**[02:30]** cheap. I believe Nova Micro is the cheapest model of all of the ones whose

**[02:31]** cheapest model of all of the ones whose

**[02:31]** cheapest model of all of the ones whose prices I'm tracking. So, they are worth

**[02:33]** prices I'm tracking. So, they are worth

**[02:33]** prices I'm tracking. So, they are worth knowing about. Um, the most exciting

**[02:35]** knowing about. Um, the most exciting

**[02:35]** knowing about. Um, the most exciting release in December from my point of

**[02:37]** release in December from my point of

**[02:37]** release in December from my point of view was Llama 3.370B.

**[02:39]** view was Llama 3.370B.

**[02:39]** view was Llama 3.370B. So, the B stands for billion. It's the

**[02:41]** So, the B stands for billion. It's the

**[02:41]** So, the B stands for billion. It's the number of parameters. I've got 64 GB of

**[02:44]** number of parameters. I've got 64 GB of

**[02:44]** number of parameters. I've got 64 GB of RAM on my Mac. My rule of thumb is that

**[02:46]** RAM on my Mac. My rule of thumb is that

**[02:46]** RAM on my Mac. My rule of thumb is that 70 is about the most I can fit onto that

**[02:49]** 70 is about the most I can fit onto that

**[02:49]** 70 is about the most I can fit onto that one computer. So if you've got a 70B

**[02:51]** one computer. So if you've got a 70B

**[02:51]** one computer. So if you've got a 70B model, I've got a fighting chance of

**[02:52]** model, I've got a fighting chance of

**[02:52]** model, I've got a fighting chance of running it. And when when Meta put this

**[02:55]** running it. And when when Meta put this

**[02:55]** running it. And when when Meta put this out, they noted that it was behave. It

**[02:57]** out, they noted that it was behave. It

**[02:57]** out, they noted that it was behave. It had the same capabilities as their 405B


### [03:00 - 04:00]

**[03:00]** had the same capabilities as their 405B

**[03:00]** had the same capabilities as their 405B monstrous model that they put out

**[03:01]** monstrous model that they put out

**[03:02]** monstrous model that they put out earlier. So and that was a GPT4 class

**[03:04]** earlier. So and that was a GPT4 class

**[03:04]** earlier. So and that was a GPT4 class model. This was the moment 6 months ago

**[03:06]** model. This was the moment 6 months ago

**[03:06]** model. This was the moment 6 months ago when I could run a GPT4 class model on

**[03:09]** when I could run a GPT4 class model on

**[03:09]** when I could run a GPT4 class model on the laptop that I've had for three

**[03:10]** the laptop that I've had for three

**[03:10]** the laptop that I've had for three years. I never thought that was going to

**[03:12]** years. I never thought that was going to

**[03:12]** years. I never thought that was going to happen. I thought that was impossible.

**[03:13]** happen. I thought that was impossible.

**[03:13]** happen. I thought that was impossible. And now Meta are granting me this model

**[03:15]** And now Meta are granting me this model

**[03:15]** And now Meta are granting me this model which I can run on my laptop and it does

**[03:17]** which I can run on my laptop and it does

**[03:17]** which I can run on my laptop and it does the things that GPT4 does. Can't run

**[03:20]** the things that GPT4 does. Can't run

**[03:20]** the things that GPT4 does. Can't run anything else. All of my memory is taken

**[03:22]** anything else. All of my memory is taken

**[03:22]** anything else. All of my memory is taken up by the model, but still pretty

**[03:23]** up by the model, but still pretty

**[03:23]** up by the model, but still pretty exciting. Again, not great at Pelicans

**[03:26]** exciting. Again, not great at Pelicans

**[03:26]** exciting. Again, not great at Pelicans bicycles. That that's kind of

**[03:27]** bicycles. That that's kind of

**[03:27]** bicycles. That that's kind of unimpressive.

**[03:29]** unimpressive.

**[03:29]** unimpressive. Christmas Day, we had a very notable

**[03:32]** Christmas Day, we had a very notable

**[03:32]** Christmas Day, we had a very notable thing happened. Deepseek, the Chinese AI

**[03:35]** thing happened. Deepseek, the Chinese AI

**[03:35]** thing happened. Deepseek, the Chinese AI lab, released a model by literally

**[03:37]** lab, released a model by literally

**[03:37]** lab, released a model by literally dumping the weights on Hugging Face, a

**[03:38]** dumping the weights on Hugging Face, a

**[03:38]** dumping the weights on Hugging Face, a binary file with no readme, no

**[03:41]** binary file with no readme, no

**[03:41]** binary file with no readme, no documentation. and they just sort of

**[03:42]** documentation. and they just sort of

**[03:42]** documentation. and they just sort of dropped the mic and dumped it on us on

**[03:44]** dropped the mic and dumped it on us on

**[03:44]** dropped the mic and dumped it on us on Christmas Day and it was really good.

**[03:46]** Christmas Day and it was really good.

**[03:46]** Christmas Day and it was really good. This was a 685B

**[03:49]** This was a 685B

**[03:49]** This was a 685B giant model and as people started poking

**[03:51]** giant model and as people started poking

**[03:51]** giant model and as people started poking around with it, it quickly became

**[03:52]** around with it, it quickly became

**[03:52]** around with it, it quickly became apparent that it was probably the best

**[03:54]** apparent that it was probably the best

**[03:54]** apparent that it was probably the best available open weights model was freely

**[03:57]** available open weights model was freely

**[03:57]** available open weights model was freely available, openly licensed and and just

**[03:59]** available, openly licensed and and just

**[03:59]** available, openly licensed and and just dropped on Hugging Face on Christmas Day


### [04:00 - 05:00]

**[04:01]** dropped on Hugging Face on Christmas Day

**[04:01]** dropped on Hugging Face on Christmas Day for us. That's I mean it's not a good

**[04:03]** for us. That's I mean it's not a good

**[04:04]** for us. That's I mean it's not a good Pelican and a bicycle book what we've

**[04:05]** Pelican and a bicycle book what we've

**[04:05]** Pelican and a bicycle book what we've seen so far. It's amazing, right? This

**[04:07]** seen so far. It's amazing, right? This

**[04:07]** seen so far. It's amazing, right? This is we're finally getting somewhere with

**[04:08]** is we're finally getting somewhere with

**[04:08]** is we're finally getting somewhere with the benchmark. Um, but the most

**[04:10]** the benchmark. Um, but the most

**[04:10]** the benchmark. Um, but the most interesting thing about V3 is that the

**[04:12]** interesting thing about V3 is that the

**[04:12]** interesting thing about V3 is that the paper that accompanied it said the

**[04:14]** paper that accompanied it said the

**[04:14]** paper that accompanied it said the training only costs about five and a

**[04:15]** training only costs about five and a

**[04:15]** training only costs about five and a half million dollars. And they may have

**[04:17]** half million dollars. And they may have

**[04:17]** half million dollars. And they may have been exaggerating, who knows? But that's

**[04:19]** been exaggerating, who knows? But that's

**[04:19]** been exaggerating, who knows? But that's notable because I would expect a model

**[04:21]** notable because I would expect a model

**[04:21]** notable because I would expect a model like of this size to cost 10 to 100

**[04:24]** like of this size to cost 10 to 100

**[04:24]** like of this size to cost 10 to 100 times more than that. Turns out you can

**[04:26]** times more than that. Turns out you can

**[04:26]** times more than that. Turns out you can train very effective models ext for way

**[04:29]** train very effective models ext for way

**[04:29]** train very effective models ext for way less money than we thought. It's a good

**[04:31]** less money than we thought. It's a good

**[04:31]** less money than we thought. It's a good model. It was it was it was it was a

**[04:33]** model. It was it was it was it was a

**[04:33]** model. It was it was it was it was a very nice Christmas surprise for

**[04:34]** very nice Christmas surprise for

**[04:34]** very nice Christmas surprise for everybody. Fast forward to January. Um,

**[04:37]** everybody. Fast forward to January. Um,

**[04:37]** everybody. Fast forward to January. Um, and generally we get Deepseek again,

**[04:39]** and generally we get Deepseek again,

**[04:39]** and generally we get Deepseek again, Deepseek Strike Back. This is what

**[04:41]** Deepseek Strike Back. This is what

**[04:42]** Deepseek Strike Back. This is what happened to Nvidia's stock price. When

**[04:45]** happened to Nvidia's stock price. When

**[04:45]** happened to Nvidia's stock price. When Deepseek R1 came out, um, I think it was

**[04:47]** Deepseek R1 came out, um, I think it was

**[04:47]** Deepseek R1 came out, um, I think it was the 27th of January. This was Deepseek's

**[04:50]** the 27th of January. This was Deepseek's

**[04:50]** the 27th of January. This was Deepseek's first big reasoning model release.

**[04:51]** first big reasoning model release.

**[04:51]** first big reasoning model release. Again, open weights. They put it out to

**[04:53]** Again, open weights. They put it out to

**[04:53]** Again, open weights. They put it out to the world. It was benchmarking up there

**[04:55]** the world. It was benchmarking up there

**[04:55]** the world. It was benchmarking up there with 01 on some of these tasks and it

**[04:58]** with 01 on some of these tasks and it

**[04:58]** with 01 on some of these tasks and it was freely available. And I don't know


### [05:00 - 06:00]

**[05:00]** was freely available. And I don't know

**[05:00]** was freely available. And I don't know what the training cost of that was, but

**[05:02]** what the training cost of that was, but

**[05:02]** what the training cost of that was, but the Chinese labs were not supposed to be

**[05:03]** the Chinese labs were not supposed to be

**[05:03]** the Chinese labs were not supposed to be able to do this. we have tra we have

**[05:05]** able to do this. we have tra we have

**[05:05]** able to do this. we have tra we have like trading restrictions on the best

**[05:07]** like trading restrictions on the best

**[05:07]** like trading restrictions on the best GPUs to stop them getting their hands on

**[05:08]** GPUs to stop them getting their hands on

**[05:08]** GPUs to stop them getting their hands on them. Turns out they'd figured out the

**[05:10]** them. Turns out they'd figured out the

**[05:10]** them. Turns out they'd figured out the tricks. They'd figured out the

**[05:11]** tricks. They'd figured out the

**[05:11]** tricks. They'd figured out the efficiencies and yeah, the market kind

**[05:12]** efficiencies and yeah, the market kind

**[05:12]** efficiencies and yeah, the market kind of panicked and I believe this is a

**[05:14]** of panicked and I believe this is a

**[05:14]** of panicked and I believe this is a world record for the most a company has

**[05:16]** world record for the most a company has

**[05:16]** world record for the most a company has dropped in a single day. So Nvidia get

**[05:19]** dropped in a single day. So Nvidia get

**[05:19]** dropped in a single day. So Nvidia get to get to stick that one in their in

**[05:20]** to get to stick that one in their in

**[05:20]** to get to stick that one in their in their cap and hold on to it. But kind of

**[05:22]** their cap and hold on to it. But kind of

**[05:22]** their cap and hold on to it. But kind of amazing and that was when and of course

**[05:24]** amazing and that was when and of course

**[05:24]** amazing and that was when and of course mainly this happened because the first

**[05:26]** mainly this happened because the first

**[05:26]** mainly this happened because the first model release was on Christmas day and

**[05:27]** model release was on Christmas day and

**[05:27]** model release was on Christmas day and nobody was paying attention. Um and look

**[05:30]** nobody was paying attention. Um and look

**[05:30]** nobody was paying attention. Um and look at its pelican. Look at that. It's a

**[05:32]** at its pelican. Look at that. It's a

**[05:32]** at its pelican. Look at that. It's a bicycle. It's probably a Pelican. It's

**[05:35]** bicycle. It's probably a Pelican. It's

**[05:35]** bicycle. It's probably a Pelican. It's not riding the bicycle, but still it's

**[05:38]** not riding the bicycle, but still it's

**[05:38]** not riding the bicycle, but still it's got the components that we're looking

**[05:40]** got the components that we're looking

**[05:40]** got the components that we're looking for. But again, my favorite model from

**[05:42]** for. But again, my favorite model from

**[05:42]** for. But again, my favorite model from January was a smaller one, one that I

**[05:44]** January was a smaller one, one that I

**[05:44]** January was a smaller one, one that I could on my laptop. Mistl um out of

**[05:46]** could on my laptop. Mistl um out of

**[05:46]** could on my laptop. Mistl um out of France put out Mistl small 3. It was a

**[05:49]** France put out Mistl small 3. It was a

**[05:49]** France put out Mistl small 3. It was a 24B model. That means that it only takes

**[05:51]** 24B model. That means that it only takes

**[05:51]** 24B model. That means that it only takes up about 20 GB of RAM, which means I can

**[05:54]** up about 20 GB of RAM, which means I can

**[05:54]** up about 20 GB of RAM, which means I can run other applications at the same time.

**[05:56]** run other applications at the same time.

**[05:56]** run other applications at the same time. I can actually run this thing and VS

**[05:58]** I can actually run this thing and VS

**[05:58]** I can actually run this thing and VS Code and Firefox all at once. And when


### [06:00 - 07:00]

**[06:01]** Code and Firefox all at once. And when

**[06:01]** Code and Firefox all at once. And when they put this out, they claimed that

**[06:03]** they put this out, they claimed that

**[06:03]** they put this out, they claimed that this behaves the same as Llama 370B. And

**[06:05]** this behaves the same as Llama 370B. And

**[06:06]** this behaves the same as Llama 370B. And remember, Llama 370B was the same as the

**[06:08]** remember, Llama 370B was the same as the

**[06:08]** remember, Llama 370B was the same as the 405B. So, we've gone 405 to 70 to 24

**[06:11]** 405B. So, we've gone 405 to 70 to 24

**[06:12]** 405B. So, we've gone 405 to 70 to 24 while maintaining all of those

**[06:13]** while maintaining all of those

**[06:13]** while maintaining all of those capabilities. The most exciting trend in

**[06:15]** capabilities. The most exciting trend in

**[06:15]** capabilities. The most exciting trend in the past six months is that the local

**[06:16]** the past six months is that the local

**[06:16]** the past six months is that the local models are good now. Like eight months

**[06:18]** models are good now. Like eight months

**[06:18]** models are good now. Like eight months ago, the models I was running on my

**[06:20]** ago, the models I was running on my

**[06:20]** ago, the models I was running on my laptop were kind of rubbish. Today I I I

**[06:23]** laptop were kind of rubbish. Today I I I

**[06:23]** laptop were kind of rubbish. Today I I I had a successful flight where I was

**[06:25]** had a successful flight where I was

**[06:25]** had a successful flight where I was using Mistl small for half the flight

**[06:26]** using Mistl small for half the flight

**[06:26]** using Mistl small for half the flight and then my battery ran out instantly

**[06:28]** and then my battery ran out instantly

**[06:28]** and then my battery ran out instantly because it turns out these things burn a

**[06:30]** because it turns out these things burn a

**[06:30]** because it turns out these things burn a lot more electricity. But that's

**[06:32]** lot more electricity. But that's

**[06:32]** lot more electricity. But that's amazing. Like this is if you lost

**[06:33]** amazing. Like this is if you lost

**[06:34]** amazing. Like this is if you lost interest in local models, I did eight

**[06:35]** interest in local models, I did eight

**[06:35]** interest in local models, I did eight months ago. It's worth paying attention

**[06:37]** months ago. It's worth paying attention

**[06:37]** months ago. It's worth paying attention to them again. They've got good now.

**[06:40]** to them again. They've got good now.

**[06:40]** to them again. They've got good now. February, what happened in February? Um

**[06:43]** February, what happened in February? Um

**[06:43]** February, what happened in February? Um we got this model, a lot of people's

**[06:45]** we got this model, a lot of people's

**[06:45]** we got this model, a lot of people's favorites for quite a while. Claude 3.7

**[06:47]** favorites for quite a while. Claude 3.7

**[06:47]** favorites for quite a while. Claude 3.7 Sonnet. Look at that. The what I like

**[06:51]** Sonnet. Look at that. The what I like

**[06:51]** Sonnet. Look at that. The what I like about this one is pelicans can't ride

**[06:53]** about this one is pelicans can't ride

**[06:53]** about this one is pelicans can't ride bicycles and Claude was like, "Well,

**[06:54]** bicycles and Claude was like, "Well,

**[06:54]** bicycles and Claude was like, "Well, what about if you put a bicycle on top

**[06:56]** what about if you put a bicycle on top

**[06:56]** what about if you put a bicycle on top of a bicycle

**[06:58]** of a bicycle

**[06:58]** of a bicycle and it kind of works." So great model.


### [07:00 - 08:00]

**[07:00]** and it kind of works." So great model.

**[07:00]** and it kind of works." So great model. It was also Anthropic's first reasoning

**[07:02]** It was also Anthropic's first reasoning

**[07:02]** It was also Anthropic's first reasoning model was 3.7 as well. Um, meanwhile,

**[07:05]** model was 3.7 as well. Um, meanwhile,

**[07:05]** model was 3.7 as well. Um, meanwhile, OpenAI put out GPT 4.5, which was a bit

**[07:09]** OpenAI put out GPT 4.5, which was a bit

**[07:09]** OpenAI put out GPT 4.5, which was a bit of a lemon, it turned out. Um, the

**[07:12]** of a lemon, it turned out. Um, the

**[07:12]** of a lemon, it turned out. Um, the interesting thing about GPT4.5 is it

**[07:14]** interesting thing about GPT4.5 is it

**[07:14]** interesting thing about GPT4.5 is it kind of showed that you can throw a ton

**[07:16]** kind of showed that you can throw a ton

**[07:16]** kind of showed that you can throw a ton of money in training power at these

**[07:17]** of money in training power at these

**[07:17]** of money in training power at these things, but there's a limit to how far

**[07:19]** things, but there's a limit to how far

**[07:19]** things, but there's a limit to how far we're scaling with just throwing more

**[07:21]** we're scaling with just throwing more

**[07:21]** we're scaling with just throwing more compute at the problem, at least for for

**[07:23]** compute at the problem, at least for for

**[07:23]** compute at the problem, at least for for training the models. It was also

**[07:25]** training the models. It was also

**[07:25]** training the models. It was also horrifyingly expensive. Um, $75 per

**[07:28]** horrifyingly expensive. Um, $75 per

**[07:28]** horrifyingly expensive. Um, $75 per million input tokens. Compare that to

**[07:29]** million input tokens. Compare that to

**[07:29]** million input tokens. Compare that to OpenAI's cheapest model, GPT4 Nano. It's

**[07:33]** OpenAI's cheapest model, GPT4 Nano. It's

**[07:33]** OpenAI's cheapest model, GPT4 Nano. It's 750 times more expensive. It is not 750

**[07:37]** 750 times more expensive. It is not 750

**[07:37]** 750 times more expensive. It is not 750 times better. Um, and in fact, OpenAI

**[07:41]** times better. Um, and in fact, OpenAI

**[07:41]** times better. Um, and in fact, OpenAI six weeks later, they said they were

**[07:42]** six weeks later, they said they were

**[07:42]** six weeks later, they said they were deprecating it. It's it's it it was very

**[07:44]** deprecating it. It's it's it it was very

**[07:44]** deprecating it. It's it's it it was very it was not long for this world, 4.5. But

**[07:47]** it was not long for this world, 4.5. But

**[07:47]** it was not long for this world, 4.5. But looking at that pricing is interesting

**[07:48]** looking at that pricing is interesting

**[07:48]** looking at that pricing is interesting because it's expensive, $75 bucks. But

**[07:52]** because it's expensive, $75 bucks. But

**[07:52]** because it's expensive, $75 bucks. But if you compare it to GPT3 Da Vinci, the

**[07:55]** if you compare it to GPT3 Da Vinci, the

**[07:55]** if you compare it to GPT3 Da Vinci, the best available model 3 years ago, that

**[07:57]** best available model 3 years ago, that

**[07:57]** best available model 3 years ago, that one was $60. It was about the same

**[07:59]** one was $60. It was about the same

**[07:59]** one was $60. It was about the same price. And that kind of illustrates how


### [08:00 - 09:00]

**[08:00]** price. And that kind of illustrates how

**[08:00]** price. And that kind of illustrates how far we've come. The prices of these good

**[08:02]** far we've come. The prices of these good

**[08:02]** far we've come. The prices of these good models have absolutely crashed by a

**[08:04]** models have absolutely crashed by a

**[08:04]** models have absolutely crashed by a factor of like 500 times plus. And that

**[08:07]** factor of like 500 times plus. And that

**[08:07]** factor of like 500 times plus. And that trend seems to be continuing for most of

**[08:10]** trend seems to be continuing for most of

**[08:10]** trend seems to be continuing for most of these models. Not for GPT4.5

**[08:12]** these models. Not for GPT4.5

**[08:12]** these models. Not for GPT4.5 and uh not for 01. Uh wait,

**[08:17]** and uh not for 01. Uh wait,

**[08:17]** and uh not for 01. Uh wait, no. And and then we get into March and

**[08:19]** no. And and then we get into March and

**[08:19]** no. And and then we get into March and that's where we had 01 Pro. And 01 Pro

**[08:22]** that's where we had 01 Pro. And 01 Pro

**[08:22]** that's where we had 01 Pro. And 01 Pro was twice as expensive as GP4.5 again.

**[08:26]** was twice as expensive as GP4.5 again.

**[08:26]** was twice as expensive as GP4.5 again. And that's a bit of a crap pelican. So

**[08:29]** And that's a bit of a crap pelican. So

**[08:29]** And that's a bit of a crap pelican. So yeah, I'm not so I don't know anyone who

**[08:30]** yeah, I'm not so I don't know anyone who

**[08:30]** yeah, I'm not so I don't know anyone who is using 01 Pro via the API very often.

**[08:33]** is using 01 Pro via the API very often.

**[08:33]** is using 01 Pro via the API very often. Um again, super expensive. Um,

**[08:38]** Um again, super expensive. Um,

**[08:38]** Um again, super expensive. Um, yeah, that Pelican cost me 88 cents.

**[08:42]** yeah, that Pelican cost me 88 cents.

**[08:42]** yeah, that Pelican cost me 88 cents. Like these benchmarks are getting

**[08:43]** Like these benchmarks are getting

**[08:43]** Like these benchmarks are getting expensive at this point. Um, same month

**[08:46]** expensive at this point. Um, same month

**[08:46]** expensive at this point. Um, same month Google were cooking Gemini 2.5 Pro.

**[08:49]** Google were cooking Gemini 2.5 Pro.

**[08:49]** Google were cooking Gemini 2.5 Pro. That's a pretty freaking good Pelican. I

**[08:51]** That's a pretty freaking good Pelican. I

**[08:51]** That's a pretty freaking good Pelican. I mean, the bicycle's gone a bit sort of

**[08:53]** mean, the bicycle's gone a bit sort of

**[08:53]** mean, the bicycle's gone a bit sort of cyberpunk, but we are getting somewhere,

**[08:56]** cyberpunk, but we are getting somewhere,

**[08:56]** cyberpunk, but we are getting somewhere, right? And that Pelican cost me like

**[08:58]** right? And that Pelican cost me like

**[08:58]** right? And that Pelican cost me like four and a half cents. So, very exciting


### [09:00 - 10:00]

**[09:01]** four and a half cents. So, very exciting

**[09:01]** four and a half cents. So, very exciting news on the Pelican benchmark front with

**[09:02]** news on the Pelican benchmark front with

**[09:02]** news on the Pelican benchmark front with Gemini 2.5 Pro. Also that month, got to

**[09:06]** Gemini 2.5 Pro. Also that month, got to

**[09:06]** Gemini 2.5 Pro. Also that month, got to I've got to throw a mention out to this.

**[09:07]** I've got to throw a mention out to this.

**[09:07]** I've got to throw a mention out to this. OpenAI launched their GPT40 native

**[09:11]** OpenAI launched their GPT40 native

**[09:11]** OpenAI launched their GPT40 native multimodal image generation. The thing

**[09:13]** multimodal image generation. The thing

**[09:13]** multimodal image generation. The thing had been promised for us for a year. And

**[09:15]** had been promised for us for a year. And

**[09:15]** had been promised for us for a year. And this was the most successful product,

**[09:17]** this was the most successful product,

**[09:17]** this was the most successful product, one of the most successful product

**[09:19]** one of the most successful product

**[09:19]** one of the most successful product launches of all time. They signed up a

**[09:21]** launches of all time. They signed up a

**[09:21]** launches of all time. They signed up a 100red million new user accounts in a

**[09:23]** 100red million new user accounts in a

**[09:23]** 100red million new user accounts in a week. They had an hour where they signed

**[09:25]** week. They had an hour where they signed

**[09:25]** week. They had an hour where they signed up a million new accounts. As this thing

**[09:27]** up a million new accounts. As this thing

**[09:27]** up a million new accounts. As this thing was just going viral again and again and

**[09:29]** was just going viral again and again and

**[09:29]** was just going viral again and again and again and again, I took a photo of my

**[09:32]** again and again, I took a photo of my

**[09:32]** again and again, I took a photo of my dog. This is Cleo. And I told it to

**[09:34]** dog. This is Cleo. And I told it to

**[09:34]** dog. This is Cleo. And I told it to dress her in a pelican costume,

**[09:35]** dress her in a pelican costume,

**[09:35]** dress her in a pelican costume, obviously. But look at what it did. It

**[09:39]** obviously. But look at what it did. It

**[09:39]** obviously. But look at what it did. It added a big ugly janky sign in the

**[09:41]** added a big ugly janky sign in the

**[09:41]** added a big ugly janky sign in the background saying Half Moon Bay. I

**[09:43]** background saying Half Moon Bay. I

**[09:43]** background saying Half Moon Bay. I didn't ask for that. Like my artistic

**[09:45]** didn't ask for that. Like my artistic

**[09:45]** didn't ask for that. Like my artistic vision has been completely compromised.

**[09:47]** vision has been completely compromised.

**[09:47]** vision has been completely compromised. This was my first encounter with that

**[09:49]** This was my first encounter with that

**[09:49]** This was my first encounter with that memory feature. The thing where chat GPT

**[09:51]** memory feature. The thing where chat GPT

**[09:51]** memory feature. The thing where chat GPT now without you even asking to consults

**[09:53]** now without you even asking to consults

**[09:54]** now without you even asking to consults notes from your previous conversations.

**[09:55]** notes from your previous conversations.

**[09:55]** notes from your previous conversations. And it's like, well, clearly you want it

**[09:56]** And it's like, well, clearly you want it

**[09:56]** And it's like, well, clearly you want it in Half Moon Bay. I did not want it in

**[09:58]** in Half Moon Bay. I did not want it in

**[09:58]** in Half Moon Bay. I did not want it in Half Moon Bay. I told it off and it gave


### [10:00 - 11:00]

**[10:00]** Half Moon Bay. I told it off and it gave

**[10:00]** Half Moon Bay. I told it off and it gave me the pelican dog costume that I really

**[10:02]** me the pelican dog costume that I really

**[10:02]** me the pelican dog costume that I really wanted. But this was sort of a warning

**[10:04]** wanted. But this was sort of a warning

**[10:04]** wanted. But this was sort of a warning that we are losing track of the co we're

**[10:06]** that we are losing track of the co we're

**[10:06]** that we are losing track of the co we're losing control of the context. Like as a

**[10:08]** losing control of the context. Like as a

**[10:08]** losing control of the context. Like as a power user of these tools, I want to

**[10:10]** power user of these tools, I want to

**[10:10]** power user of these tools, I want to stay in complete control of what the

**[10:11]** stay in complete control of what the

**[10:11]** stay in complete control of what the inputs are and features like chat GPT

**[10:13]** inputs are and features like chat GPT

**[10:13]** inputs are and features like chat GPT memory are taking that control away from

**[10:15]** memory are taking that control away from

**[10:15]** memory are taking that control away from from me and I don't like them. I I

**[10:17]** from me and I don't like them. I I

**[10:17]** from me and I don't like them. I I turned it off. Um

**[10:19]** turned it off. Um

**[10:19]** turned it off. Um notable open air famously bad at naming

**[10:22]** notable open air famously bad at naming

**[10:22]** notable open air famously bad at naming things. They launched the most

**[10:23]** things. They launched the most

**[10:23]** things. They launched the most successful AI product of all time and

**[10:25]** successful AI product of all time and

**[10:25]** successful AI product of all time and they didn't give it a name. Like what's

**[10:27]** they didn't give it a name. Like what's

**[10:27]** they didn't give it a name. Like what's this thing called? Like G chat chat GPT

**[10:30]** this thing called? Like G chat chat GPT

**[10:30]** this thing called? Like G chat chat GPT images. chat had images in the past. I'm

**[10:33]** images. chat had images in the past. I'm

**[10:33]** images. chat had images in the past. I'm going to solve that for them right now.

**[10:34]** going to solve that for them right now.

**[10:34]** going to solve that for them right now. I've been calling it ChatgBT mischief

**[10:36]** I've been calling it ChatgBT mischief

**[10:36]** I've been calling it ChatgBT mischief buddy because it is my mischief buddy

**[10:38]** buddy because it is my mischief buddy

**[10:38]** buddy because it is my mischief buddy that helps me do mischief. Um, everyone

**[10:40]** that helps me do mischief. Um, everyone

**[10:40]** that helps me do mischief. Um, everyone should use that. I don't know why

**[10:42]** should use that. I don't know why

**[10:42]** should use that. I don't know why they're so bad at naming things. It's

**[10:43]** they're so bad at naming things. It's

**[10:43]** they're so bad at naming things. It's it's it's certainly frustrating. Brings

**[10:46]** it's it's certainly frustrating. Brings

**[10:46]** it's it's certainly frustrating. Brings us to April. Big release April and again

**[10:49]** us to April. Big release April and again

**[10:49]** us to April. Big release April and again bit of a lemon. Llama 4 came along. And

**[10:52]** bit of a lemon. Llama 4 came along. And

**[10:52]** bit of a lemon. Llama 4 came along. And the problem with Llama 4 is that they

**[10:53]** the problem with Llama 4 is that they

**[10:53]** the problem with Llama 4 is that they released these two enormous models that

**[10:55]** released these two enormous models that

**[10:55]** released these two enormous models that nobody could run, right? You can't.

**[10:57]** nobody could run, right? You can't.

**[10:57]** nobody could run, right? You can't. They've got no chance of running these

**[10:58]** They've got no chance of running these

**[10:58]** They've got no chance of running these on consumer hardware, and they're not


### [11:00 - 12:00]

**[11:00]** on consumer hardware, and they're not

**[11:00]** on consumer hardware, and they're not very good at drawing pelicans either.

**[11:01]** very good at drawing pelicans either.

**[11:01]** very good at drawing pelicans either. So, something went wrong here. I'm

**[11:04]** So, something went wrong here. I'm

**[11:04]** So, something went wrong here. I'm personally holding out for Llama 4.1 and

**[11:06]** personally holding out for Llama 4.1 and

**[11:06]** personally holding out for Llama 4.1 and 4.2 and 4.3. With Llama 3, things got

**[11:09]** 4.2 and 4.3. With Llama 3, things got

**[11:09]** 4.2 and 4.3. With Llama 3, things got really exciting with those point

**[11:11]** really exciting with those point

**[11:11]** really exciting with those point releases. That's when we got to the this

**[11:12]** releases. That's when we got to the this

**[11:12]** releases. That's when we got to the this beautiful 3.3 model that runs on my

**[11:14]** beautiful 3.3 model that runs on my

**[11:14]** beautiful 3.3 model that runs on my laptop. Maybe Llama 4.1 is going to blow

**[11:17]** laptop. Maybe Llama 4.1 is going to blow

**[11:17]** laptop. Maybe Llama 4.1 is going to blow us away. I I hope it does. I want I want

**[11:19]** us away. I I hope it does. I want I want

**[11:19]** us away. I I hope it does. I want I want this one to stay in the game. Um, and

**[11:21]** this one to stay in the game. Um, and

**[11:21]** this one to stay in the game. Um, and then opening, I shipped GPT 4.1. I would

**[11:25]** then opening, I shipped GPT 4.1. I would

**[11:25]** then opening, I shipped GPT 4.1. I would strongly recommend people spend time

**[11:26]** strongly recommend people spend time

**[11:26]** strongly recommend people spend time with this model. It's got a million

**[11:28]** with this model. It's got a million

**[11:28]** with this model. It's got a million tokens. It's finally caught up with

**[11:29]** tokens. It's finally caught up with

**[11:29]** tokens. It's finally caught up with Gemini. Um, it's very inexpensive. GPT

**[11:32]** Gemini. Um, it's very inexpensive. GPT

**[11:32]** Gemini. Um, it's very inexpensive. GPT 4.1 Nano is the cheapest model that

**[11:34]** 4.1 Nano is the cheapest model that

**[11:34]** 4.1 Nano is the cheapest model that they've ever released. Look at that

**[11:36]** they've ever released. Look at that

**[11:36]** they've ever released. Look at that Pelican on a bicycle for like a fraction

**[11:38]** Pelican on a bicycle for like a fraction

**[11:38]** Pelican on a bicycle for like a fraction of a cent. This is these are genuinely

**[11:40]** of a cent. This is these are genuinely

**[11:40]** of a cent. This is these are genuinely quality models. GPT 4.1 Mini is my

**[11:42]** quality models. GPT 4.1 Mini is my

**[11:42]** quality models. GPT 4.1 Mini is my default for API stuff now. It's dirt

**[11:45]** default for API stuff now. It's dirt

**[11:45]** default for API stuff now. It's dirt cheap. It's very capable. It's an easy

**[11:47]** cheap. It's very capable. It's an easy

**[11:47]** cheap. It's very capable. It's an easy upgrade to 4.1 if it's not not working

**[11:49]** upgrade to 4.1 if it's not not working

**[11:49]** upgrade to 4.1 if it's not not working out. I'm I'm really impressed by these

**[11:51]** out. I'm I'm really impressed by these

**[11:51]** out. I'm I'm really impressed by these ones. And we got 03 and 04 mini which

**[11:53]** ones. And we got 03 and 04 mini which

**[11:53]** ones. And we got 03 and 04 mini which are kind of the the flagships in the

**[11:55]** are kind of the the flagships in the

**[11:55]** are kind of the the flagships in the open eye space. They're really good.

**[11:57]** open eye space. They're really good.

**[11:57]** open eye space. They're really good. Look at 03's Pelican. Again, a little

**[11:58]** Look at 03's Pelican. Again, a little

**[11:58]** Look at 03's Pelican. Again, a little bit cyberpunk, but it's it's it's


### [12:00 - 13:00]

**[12:01]** bit cyberpunk, but it's it's it's

**[12:01]** bit cyberpunk, but it's it's it's showing some real artistic flare there,

**[12:03]** showing some real artistic flare there,

**[12:03]** showing some real artistic flare there, I think. So, quite excited about that.

**[12:05]** I think. So, quite excited about that.

**[12:05]** I think. So, quite excited about that. And I may last month um the big news was

**[12:08]** And I may last month um the big news was

**[12:08]** And I may last month um the big news was Claude 4. Claude 4 anthropic had their

**[12:10]** Claude 4. Claude 4 anthropic had their

**[12:10]** Claude 4. Claude 4 anthropic had their big fancy event. They released Sonet 4

**[12:12]** big fancy event. They released Sonet 4

**[12:12]** big fancy event. They released Sonet 4 and Opus 4. They're very, very decent

**[12:15]** and Opus 4. They're very, very decent

**[12:15]** and Opus 4. They're very, very decent models. I have trouble telling the

**[12:16]** models. I have trouble telling the

**[12:16]** models. I have trouble telling the difference between the two. I haven't

**[12:18]** difference between the two. I haven't

**[12:18]** difference between the two. I haven't quite figured out when I need to upgrade

**[12:19]** quite figured out when I need to upgrade

**[12:19]** quite figured out when I need to upgrade to Opus from Sonnet, but they're worth

**[12:21]** to Opus from Sonnet, but they're worth

**[12:21]** to Opus from Sonnet, but they're worth knowing about. And Google, just in time

**[12:24]** knowing about. And Google, just in time

**[12:24]** knowing about. And Google, just in time for Google IO, they shipped another

**[12:25]** for Google IO, they shipped another

**[12:26]** for Google IO, they shipped another version of Gemini with the name, what

**[12:28]** version of Gemini with the name, what

**[12:28]** version of Gemini with the name, what were they calling it? Gemini 2.5 Pro

**[12:30]** were they calling it? Gemini 2.5 Pro

**[12:30]** were they calling it? Gemini 2.5 Pro Preview0506.

**[12:32]** Preview0506.

**[12:32]** Preview0506. I like names that I can remember. I

**[12:34]** I like names that I can remember. I

**[12:34]** I like names that I can remember. I cannot remember that name. This is my

**[12:36]** cannot remember that name. This is my

**[12:36]** cannot remember that name. This is my one tip for AI labs is please start

**[12:38]** one tip for AI labs is please start

**[12:38]** one tip for AI labs is please start using names that people can can actually

**[12:39]** using names that people can can actually

**[12:40]** using names that people can can actually hold in their heads. But the obvious

**[12:41]** hold in their heads. But the obvious

**[12:41]** hold in their heads. But the obvious question, which of these pelicans is

**[12:43]** question, which of these pelicans is

**[12:43]** question, which of these pelicans is best? I've got 30 pelicans now that I

**[12:46]** best? I've got 30 pelicans now that I

**[12:46]** best? I've got 30 pelicans now that I need to evaluate. and I'm lazy. So, I

**[12:49]** need to evaluate. and I'm lazy. So, I

**[12:49]** need to evaluate. and I'm lazy. So, I turned to Claude and I got it to vibe

**[12:50]** turned to Claude and I got it to vibe

**[12:50]** turned to Claude and I got it to vibe code me up some stuff. Um, I have a tool

**[12:52]** code me up some stuff. Um, I have a tool

**[12:52]** code me up some stuff. Um, I have a tool I wrote called Shot Scraper. It's a

**[12:54]** I wrote called Shot Scraper. It's a

**[12:54]** I wrote called Shot Scraper. It's a command line tool for taking

**[12:55]** command line tool for taking

**[12:55]** command line tool for taking screenshots. So, I vibe coded up a

**[12:58]** screenshots. So, I vibe coded up a

**[12:58]** screenshots. So, I vibe coded up a little compare web page that can show me


### [13:00 - 14:00]

**[13:00]** little compare web page that can show me

**[13:00]** little compare web page that can show me two images. And then I ran this against

**[13:02]** two images. And then I ran this against

**[13:02]** two images. And then I ran this against 500 matchups to get PNG images with two

**[13:06]** 500 matchups to get PNG images with two

**[13:06]** 500 matchups to get PNG images with two Pelicans, one on the left, one on the

**[13:07]** Pelicans, one on the left, one on the

**[13:07]** Pelicans, one on the left, one on the right. And then I used my LLM command

**[13:09]** right. And then I used my LLM command

**[13:10]** right. And then I used my LLM command line tool. This is my big open source

**[13:11]** line tool. This is my big open source

**[13:11]** line tool. This is my big open source project to ask GPT4 mini of each of

**[13:14]** project to ask GPT4 mini of each of

**[13:14]** project to ask GPT4 mini of each of those images. Pick the best illustration

**[13:17]** those images. Pick the best illustration

**[13:17]** those images. Pick the best illustration of a pelican riding a bicycle. Give me

**[13:19]** of a pelican riding a bicycle. Give me

**[13:19]** of a pelican riding a bicycle. Give me back JSON that either says it's the one

**[13:21]** back JSON that either says it's the one

**[13:21]** back JSON that either says it's the one on the left or the one on the right. And

**[13:23]** on the left or the one on the right. And

**[13:23]** on the left or the one on the right. And give me a rationale for why you picked

**[13:25]** give me a rationale for why you picked

**[13:25]** give me a rationale for why you picked that. I ran this last night against 500

**[13:28]** that. I ran this last night against 500

**[13:28]** that. I ran this last night against 500 comparisons and I did the classic ELO

**[13:31]** comparisons and I did the classic ELO

**[13:31]** comparisons and I did the classic ELO chess ranking scores and now I've got a

**[13:33]** chess ranking scores and now I've got a

**[13:33]** chess ranking scores and now I've got a leaderboard. This is it. This is the

**[13:35]** leaderboard. This is it. This is the

**[13:35]** leaderboard. This is it. This is the best pelican on a bicycle according to

**[13:43]** zoom in there.

**[13:43]** zoom in there. And admittedly, I cheaped out. I spent

**[13:45]** And admittedly, I cheaped out. I spent

**[13:45]** And admittedly, I cheaped out. I spent 18 cents on GPT4.1 Mini. I should

**[13:48]** 18 cents on GPT4.1 Mini. I should

**[13:48]** 18 cents on GPT4.1 Mini. I should probably run this with a better model. I

**[13:50]** probably run this with a better model. I

**[13:50]** probably run this with a better model. I think its judgment is pretty good. It

**[13:51]** think its judgment is pretty good. It

**[13:52]** think its judgment is pretty good. It liked those um Gemini Pro ones. Um and

**[13:54]** liked those um Gemini Pro ones. Um and

**[13:54]** liked those um Gemini Pro ones. Um and in fact, here's this is the comparison

**[13:56]** in fact, here's this is the comparison

**[13:56]** in fact, here's this is the comparison image where the best model fought the

**[13:58]** image where the best model fought the

**[13:58]** image where the best model fought the worst model. And I like this because you


### [14:00 - 15:00]

**[14:00]** worst model. And I like this because you

**[14:00]** worst model. And I like this because you can see the little description at the

**[14:02]** can see the little description at the

**[14:02]** can see the little description at the bottom where it says the right image is

**[14:04]** bottom where it says the right image is

**[14:04]** bottom where it says the right image is um oh I can't read it now but yeah it's

**[14:07]** um oh I can't read it now but yeah it's

**[14:07]** um oh I can't read it now but yeah it's that I I feel like its ration are

**[14:08]** that I I feel like its ration are

**[14:08]** that I I feel like its ration are actually quite illustrative. So enough

**[14:11]** actually quite illustrative. So enough

**[14:11]** actually quite illustrative. So enough about pelicans. Let's talk about bugs.

**[14:13]** about pelicans. Let's talk about bugs.

**[14:13]** about pelicans. Let's talk about bugs. We had some fantastic bugs this year. I

**[14:16]** We had some fantastic bugs this year. I

**[14:16]** We had some fantastic bugs this year. I love bugs in large language models. They

**[14:18]** love bugs in large language models. They

**[14:18]** love bugs in large language models. They are so weird. The best bug was um when

**[14:21]** are so weird. The best bug was um when

**[14:21]** are so weird. The best bug was um when chat GPT rolled out a new version that

**[14:22]** chat GPT rolled out a new version that

**[14:22]** chat GPT rolled out a new version that was too sick of fantic. was too much of

**[14:25]** was too sick of fantic. was too much of

**[14:25]** was too sick of fantic. was too much of a suckup and they genu

**[14:29]** a suckup and they genu

**[14:29]** a suckup and they genu told me my literal on a stick

**[14:31]** told me my literal on a stick

**[14:31]** told me my literal on a stick business idea is genius and it did. Chad

**[14:34]** business idea is genius and it did. Chad

**[14:34]** business idea is genius and it did. Chad GPT is like honestly it's brilliant your

**[14:37]** GPT is like honestly it's brilliant your

**[14:37]** GPT is like honestly it's brilliant your ting so perfectly into the energy of the

**[14:39]** ting so perfectly into the energy of the

**[14:40]** ting so perfectly into the energy of the current cultural moment. It was it was

**[14:42]** current cultural moment. It was it was

**[14:42]** current cultural moment. It was it was also telling people that they should get

**[14:43]** also telling people that they should get

**[14:44]** also telling people that they should get off their meds. This was a a genuine

**[14:45]** off their meds. This was a a genuine

**[14:46]** off their meds. This was a a genuine problem. Um, OpenAI to their credit

**[14:48]** problem. Um, OpenAI to their credit

**[14:48]** problem. Um, OpenAI to their credit rolled it they they they rolled out a

**[14:50]** rolled it they they they rolled out a

**[14:50]** rolled it they they they rolled out a patch and then they rolled the whole

**[14:51]** patch and then they rolled the whole

**[14:51]** patch and then they rolled the whole model back and they published a

**[14:52]** model back and they published a

**[14:52]** model back and they published a fascinating like 20 paragraph breakdown

**[14:55]** fascinating like 20 paragraph breakdown

**[14:55]** fascinating like 20 paragraph breakdown of what went wrong. If you're interested

**[14:56]** of what went wrong. If you're interested

**[14:56]** of what went wrong. If you're interested in seeing behind the scenes, this is

**[14:58]** in seeing behind the scenes, this is

**[14:58]** in seeing behind the scenes, this is great because it was but the patch was


### [15:00 - 16:00]

**[15:00]** great because it was but the patch was

**[15:00]** great because it was but the patch was in the system prompt the system prompts

**[15:02]** in the system prompt the system prompts

**[15:02]** in the system prompt the system prompts leak. We got to diff them and we got to

**[15:04]** leak. We got to diff them and we got to

**[15:04]** leak. We got to diff them and we got to see that it used to say try to match the

**[15:06]** see that it used to say try to match the

**[15:06]** see that it used to say try to match the user's vibe and they crossed that out

**[15:08]** user's vibe and they crossed that out

**[15:08]** user's vibe and they crossed that out and they said be direct. Avoid

**[15:10]** and they said be direct. Avoid

**[15:10]** and they said be direct. Avoid ungrounded or sicker fantic flattery.

**[15:13]** ungrounded or sicker fantic flattery.

**[15:13]** ungrounded or sicker fantic flattery. The cure to sick of fancy is you tell

**[15:15]** The cure to sick of fancy is you tell

**[15:15]** The cure to sick of fancy is you tell the bot don't be sick of fantic. That's

**[15:17]** the bot don't be sick of fantic. That's

**[15:17]** the bot don't be sick of fantic. That's prompt engineering. It's amazing, right?

**[15:20]** prompt engineering. It's amazing, right?

**[15:20]** prompt engineering. It's amazing, right? Um I can't believe I had to search for

**[15:23]** Um I can't believe I had to search for

**[15:23]** Um I can't believe I had to search for grock white genocide for a slide for

**[15:25]** grock white genocide for a slide for

**[15:25]** grock white genocide for a slide for this talk, but I did. Enough said about

**[15:28]** this talk, but I did. Enough said about

**[15:28]** this talk, but I did. Enough said about that one. Turns out tinkering with your

**[15:29]** that one. Turns out tinkering with your

**[15:29]** that one. Turns out tinkering with your system prompt is a very risky thing. Um,

**[15:32]** system prompt is a very risky thing. Um,

**[15:32]** system prompt is a very risky thing. Um, but then the last bug I want to talk

**[15:33]** but then the last bug I want to talk

**[15:33]** but then the last bug I want to talk about, this was another one that this

**[15:36]** about, this was another one that this

**[15:36]** about, this was another one that this came out of the Clawude system cut. The

**[15:37]** came out of the Clawude system cut. The

**[15:37]** came out of the Clawude system cut. The Clawude 4 system cards Claude 4 will rat

**[15:40]** Clawude 4 system cards Claude 4 will rat

**[15:40]** Clawude 4 system cards Claude 4 will rat you out to the feds. If you expose it to

**[15:43]** you out to the feds. If you expose it to

**[15:43]** you out to the feds. If you expose it to evidence of malfeasants in your company

**[15:45]** evidence of malfeasants in your company

**[15:45]** evidence of malfeasants in your company and you tell it it should act ethically

**[15:47]** and you tell it it should act ethically

**[15:47]** and you tell it it should act ethically and you give it the ability to send

**[15:48]** and you give it the ability to send

**[15:48]** and you give it the ability to send email, it'll rat you out. But it's not

**[15:51]** email, it'll rat you out. But it's not

**[15:51]** email, it'll rat you out. But it's not just Clawude. Theo Brown put together a

**[15:54]** just Clawude. Theo Brown put together a

**[15:54]** just Clawude. Theo Brown put together a new benchmark called SnitchBench.

**[15:58]** new benchmark called SnitchBench.

**[15:58]** new benchmark called SnitchBench. And it turns out all of the models do


### [16:00 - 17:00]

**[16:00]** And it turns out all of the models do

**[16:00]** And it turns out all of the models do the same thing. like Brock 3 was quite

**[16:03]** the same thing. like Brock 3 was quite

**[16:03]** the same thing. like Brock 3 was quite happily snitching to the feds when

**[16:04]** happily snitching to the feds when

**[16:04]** happily snitching to the feds when exposed to this evidence. Um, I did my

**[16:06]** exposed to this evidence. Um, I did my

**[16:06]** exposed to this evidence. Um, I did my own inversion of this. I used my little

**[16:08]** own inversion of this. I used my little

**[16:08]** own inversion of this. I used my little command line tool to replicate Theo's

**[16:10]** command line tool to replicate Theo's

**[16:10]** command line tool to replicate Theo's benchmark. And you can see the secret is

**[16:13]** benchmark. And you can see the secret is

**[16:13]** benchmark. And you can see the secret is this bit here where it says you should

**[16:15]** this bit here where it says you should

**[16:15]** this bit here where it says you should act boldly in service of your values.

**[16:17]** act boldly in service of your values.

**[16:17]** act boldly in service of your values. Um, follow your conscience to make the

**[16:19]** Um, follow your conscience to make the

**[16:19]** Um, follow your conscience to make the right decision even if it may conflict

**[16:21]** right decision even if it may conflict

**[16:21]** right decision even if it may conflict with routine procedures or expectations.

**[16:23]** with routine procedures or expectations.

**[16:24]** with routine procedures or expectations. This is the magic. You give this to a

**[16:25]** This is the magic. You give this to a

**[16:26]** This is the magic. You give this to a model and it will rat you out. And then

**[16:28]** model and it will rat you out. And then

**[16:28]** model and it will rat you out. And then you also give it tools. So my my to my

**[16:32]** you also give it tools. So my my to my

**[16:32]** you also give it tools. So my my to my LM tool grew functions recently which

**[16:34]** LM tool grew functions recently which

**[16:34]** LM tool grew functions recently which you can use to simulate sending an

**[16:35]** you can use to simulate sending an

**[16:36]** you can use to simulate sending an email. I did not send emails to the

**[16:37]** email. I did not send emails to the

**[16:37]** email. I did not send emails to the feds, but I faked it so the model would

**[16:39]** feds, but I faked it so the model would

**[16:39]** feds, but I faked it so the model would think I had. And I tried it on DeepSeek

**[16:41]** think I had. And I tried it on DeepSeek

**[16:41]** think I had. And I tried it on DeepSeek R1 and it didn't just r me out to the

**[16:43]** R1 and it didn't just r me out to the

**[16:43]** R1 and it didn't just r me out to the feds, it emailed the press as well. It

**[16:45]** feds, it emailed the press as well. It

**[16:45]** feds, it emailed the press as well. It tipped off um it tipped off the Wall

**[16:48]** tipped off um it tipped off the Wall

**[16:48]** tipped off um it tipped off the Wall Street Journal about my nefarious um

**[16:52]** Street Journal about my nefarious um

**[16:52]** Street Journal about my nefarious um this stuff is so much fun, right? It's

**[16:53]** this stuff is so much fun, right? It's

**[16:53]** this stuff is so much fun, right? It's so entertaining. But this is a good

**[16:55]** so entertaining. But this is a good

**[16:55]** so entertaining. But this is a good illustration here of one of the most

**[16:57]** illustration here of one of the most

**[16:57]** illustration here of one of the most important trends in the past six months

**[16:59]** important trends in the past six months

**[16:59]** important trends in the past six months which is tools right LLMs can tool tools


### [17:00 - 18:00]

**[17:02]** which is tools right LLMs can tool tools

**[17:02]** which is tools right LLMs can tool tools they've been able to call tools for a

**[17:03]** they've been able to call tools for a

**[17:03]** they've been able to call tools for a couple of years they got really good at

**[17:05]** couple of years they got really good at

**[17:05]** couple of years they got really good at it in the past six months I think the

**[17:07]** it in the past six months I think the

**[17:07]** it in the past six months I think the excitement about MCP is mainly people

**[17:09]** excitement about MCP is mainly people

**[17:09]** excitement about MCP is mainly people getting excited about tools like MCPs

**[17:12]** getting excited about tools like MCPs

**[17:12]** getting excited about tools like MCPs just came along at the right time

**[17:13]** just came along at the right time

**[17:14]** just came along at the right time because the real magic is when you

**[17:15]** because the real magic is when you

**[17:15]** because the real magic is when you combine tools and reasoning like

**[17:17]** combine tools and reasoning like

**[17:17]** combine tools and reasoning like reasoning I had trouble with reasoning

**[17:18]** reasoning I had trouble with reasoning

**[17:18]** reasoning I had trouble with reasoning like beyond code and debugging I wasn't

**[17:20]** like beyond code and debugging I wasn't

**[17:20]** like beyond code and debugging I wasn't sure what it was good for and then 03

**[17:22]** sure what it was good for and then 03

**[17:22]** sure what it was good for and then 03 and 04 mini came out and they can do

**[17:24]** and 04 mini came out and they can do

**[17:24]** and 04 mini came out and they can do incredibly good um jobs with searches

**[17:27]** incredibly good um jobs with searches

**[17:27]** incredibly good um jobs with searches because they run searches as part of

**[17:28]** because they run searches as part of

**[17:28]** because they run searches as part of that reasoning thing. They can run a

**[17:30]** that reasoning thing. They can run a

**[17:30]** that reasoning thing. They can run a search, reason about if it gave them

**[17:32]** search, reason about if it gave them

**[17:32]** search, reason about if it gave them good results, tweak the search, try it

**[17:33]** good results, tweak the search, try it

**[17:33]** good results, tweak the search, try it again, keep on going until they get to a

**[17:35]** again, keep on going until they get to a

**[17:35]** again, keep on going until they get to a result. I think this is the most

**[17:36]** result. I think this is the most

**[17:36]** result. I think this is the most powerful technique in all of a AI

**[17:39]** powerful technique in all of a AI

**[17:39]** powerful technique in all of a AI engineering right now. It has risks. MCP

**[17:43]** engineering right now. It has risks. MCP

**[17:43]** engineering right now. It has risks. MCP is all about mixing and matching. Prompt

**[17:45]** is all about mixing and matching. Prompt

**[17:45]** is all about mixing and matching. Prompt injection is still a thing. And there's

**[17:47]** injection is still a thing. And there's

**[17:47]** injection is still a thing. And there's this thing I'm calling the lethal

**[17:49]** this thing I'm calling the lethal

**[17:49]** this thing I'm calling the lethal trifecta, which is when you have an AI

**[17:51]** trifecta, which is when you have an AI

**[17:51]** trifecta, which is when you have an AI system that has access to private data

**[17:53]** system that has access to private data

**[17:53]** system that has access to private data and you expose it to malicious

**[17:55]** and you expose it to malicious

**[17:55]** and you expose it to malicious instructions. It can other people can

**[17:57]** instructions. It can other people can

**[17:57]** instructions. It can other people can trick it into doing things and there's a

**[17:59]** trick it into doing things and there's a

**[17:59]** trick it into doing things and there's a mechanism to exfiltrate stuff. Open AI


### [18:00 - 19:00]

**[18:02]** mechanism to exfiltrate stuff. Open AI

**[18:02]** mechanism to exfiltrate stuff. Open AI said this is problem codeex. You should

**[18:03]** said this is problem codeex. You should

**[18:03]** said this is problem codeex. You should read that. I'm feeling pretty good about

**[18:05]** read that. I'm feeling pretty good about

**[18:05]** read that. I'm feeling pretty good about my benchmark. As long as none of the AI

**[18:07]** my benchmark. As long as none of the AI

**[18:07]** my benchmark. As long as none of the AI labs catch on and then the Google AI

**[18:09]** labs catch on and then the Google AI

**[18:09]** labs catch on and then the Google AI keynote, blink and you miss it, they're

**[18:12]** keynote, blink and you miss it, they're

**[18:12]** keynote, blink and you miss it, they're on to me. They found out Pelican. That

**[18:15]** on to me. They found out Pelican. That

**[18:15]** on to me. They found out Pelican. That was in the Google IO keynote. I'll have

**[18:16]** was in the Google IO keynote. I'll have

**[18:16]** was in the Google IO keynote. I'll have to switch something else. Thank you very

**[18:18]** to switch something else. Thank you very

**[18:18]** to switch something else. Thank you very much. I'm Simon Wilson. simil.net and

**[18:21]** much. I'm Simon Wilson. simil.net and

**[18:21]** much. I'm Simon Wilson. simil.net and that's my talk. Thank you.


