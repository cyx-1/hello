# Evals Are Not Unit Tests — Ido Pesok, Vercel v0

**Video URL:** https://www.youtube.com/watch?v=L8OoYeDI_ls

---

## Full Transcript

### [00:00 - 01:00]

**[00:17]** My name is Ido. I'm an engineer at

**[00:17]** My name is Ido. I'm an engineer at Verscell working on Vzero.

**[00:20]** Verscell working on Vzero.

**[00:20]** Verscell working on Vzero. If you don't know, Vzero is a full stack

**[00:23]** If you don't know, Vzero is a full stack

**[00:23]** If you don't know, Vzero is a full stack Vibe coding platform. It's the easiest

**[00:26]** Vibe coding platform. It's the easiest

**[00:26]** Vibe coding platform. It's the easiest and fastest way to prototype, build on

**[00:28]** and fastest way to prototype, build on

**[00:28]** and fastest way to prototype, build on the web, and express new ideas. Uh, here

**[00:31]** the web, and express new ideas. Uh, here

**[00:31]** the web, and express new ideas. Uh, here are some examples of cool things people

**[00:33]** are some examples of cool things people

**[00:33]** are some examples of cool things people have built and shared on Twitter.

**[00:35]** have built and shared on Twitter.

**[00:35]** have built and shared on Twitter. And to catch you up, we recently just

**[00:37]** And to catch you up, we recently just

**[00:37]** And to catch you up, we recently just launched GitHub sync, so you can now

**[00:39]** launched GitHub sync, so you can now

**[00:39]** launched GitHub sync, so you can now push generated code to GitHub directly

**[00:41]** push generated code to GitHub directly

**[00:41]** push generated code to GitHub directly from VZO. You can also uh automatically

**[00:44]** from VZO. You can also uh automatically

**[00:44]** from VZO. You can also uh automatically pull changes from GitHub into your chat,

**[00:47]** pull changes from GitHub into your chat,

**[00:47]** pull changes from GitHub into your chat, and furthermore, switch branches and

**[00:48]** and furthermore, switch branches and

**[00:48]** and furthermore, switch branches and open PRs to collaborate with your team.

**[00:52]** open PRs to collaborate with your team.

**[00:52]** open PRs to collaborate with your team. I'm very excited to announce we recently

**[00:53]** I'm very excited to announce we recently

**[00:54]** I'm very excited to announce we recently crossed 100 million messages sent and

**[00:57]** crossed 100 million messages sent and

**[00:57]** crossed 100 million messages sent and we're really excited to keep growing

**[00:58]** we're really excited to keep growing

**[00:58]** we're really excited to keep growing from here.


### [01:00 - 02:00]

**[01:00]** from here.

**[01:00]** from here. So my goal of this talk is for it to be

**[01:03]** So my goal of this talk is for it to be

**[01:03]** So my goal of this talk is for it to be an introduction to eval specifically at

**[01:05]** an introduction to eval specifically at

**[01:05]** an introduction to eval specifically at the application layer. You may be used

**[01:07]** the application layer. You may be used

**[01:07]** the application layer. You may be used to eval layer which is what the research

**[01:10]** to eval layer which is what the research

**[01:10]** to eval layer which is what the research labs will site in model releases but

**[01:13]** labs will site in model releases but

**[01:13]** labs will site in model releases but this will be a focus on what do evals

**[01:15]** this will be a focus on what do evals

**[01:15]** this will be a focus on what do evals mean for your users, your apps and your

**[01:18]** mean for your users, your apps and your

**[01:18]** mean for your users, your apps and your data. The model's now in the wild, out

**[01:20]** data. The model's now in the wild, out

**[01:20]** data. The model's now in the wild, out of the lab, and it needs to work for

**[01:22]** of the lab, and it needs to work for

**[01:22]** of the lab, and it needs to work for your use case. And to do this, I have a

**[01:24]** your use case. And to do this, I have a

**[01:24]** your use case. And to do this, I have a story. Uh, it's a story about this app

**[01:27]** story. Uh, it's a story about this app

**[01:27]** story. Uh, it's a story about this app called Fruit Letter Counter. And if the

**[01:30]** called Fruit Letter Counter. And if the

**[01:30]** called Fruit Letter Counter. And if the name didn't already give it away, all it

**[01:32]** name didn't already give it away, all it

**[01:32]** name didn't already give it away, all it is is an app that counts the letters in

**[01:34]** is is an app that counts the letters in

**[01:34]** is is an app that counts the letters in fruit.

**[01:36]** fruit.

**[01:36]** fruit. So, the vision is we'll make a logo with

**[01:38]** So, the vision is we'll make a logo with

**[01:38]** So, the vision is we'll make a logo with Chachi BT. Uh, there might be product

**[01:41]** Chachi BT. Uh, there might be product

**[01:41]** Chachi BT. Uh, there might be product market fit already because everyone on X

**[01:43]** market fit already because everyone on X

**[01:43]** market fit already because everyone on X is dying to know the number of letters

**[01:44]** is dying to know the number of letters

**[01:44]** is dying to know the number of letters in fruit. If you didn't get it, it's a

**[01:46]** in fruit. If you didn't get it, it's a

**[01:46]** in fruit. If you didn't get it, it's a joke on the how many Rs are in a

**[01:48]** joke on the how many Rs are in a

**[01:48]** joke on the how many Rs are in a strawberry prompt. Uh we'll have Vzero

**[01:51]** strawberry prompt. Uh we'll have Vzero

**[01:51]** strawberry prompt. Uh we'll have Vzero make all the UI and backend and then we

**[01:53]** make all the UI and backend and then we

**[01:53]** make all the UI and backend and then we can ship.

**[01:55]** can ship.

**[01:55]** can ship. So we had Vzero write the code. It it

**[01:57]** So we had Vzero write the code. It it

**[01:57]** So we had Vzero write the code. It it used uh AI SDK to do the stream text


### [02:00 - 03:00]

**[02:00]** used uh AI SDK to do the stream text

**[02:00]** used uh AI SDK to do the stream text call and what do you know? It worked

**[02:02]** call and what do you know? It worked

**[02:02]** call and what do you know? It worked first try. GPT 4.1 said three. And not

**[02:05]** first try. GPT 4.1 said three. And not

**[02:05]** first try. GPT 4.1 said three. And not only did it say three once, I even

**[02:07]** only did it say three once, I even

**[02:07]** only did it say three once, I even tested it twice and it worked both times

**[02:09]** tested it twice and it worked both times

**[02:10]** tested it twice and it worked both times in a row. So from there we're good to

**[02:13]** in a row. So from there we're good to

**[02:13]** in a row. So from there we're good to ship, right? Let's launch on Twitter.

**[02:15]** ship, right? Let's launch on Twitter.

**[02:15]** ship, right? Let's launch on Twitter. Want to know how many letters are in a

**[02:16]** Want to know how many letters are in a

**[02:16]** Want to know how many letters are in a fruit? Just launched fruit

**[02:18]** fruit? Just launched fruit

**[02:18]** fruit? Just launched fruit lettercounter.io.

**[02:20]** lettercounter.io.

**[02:20]** lettercounter.io. The.com andai were taken. Um, and yeah,

**[02:25]** The.com andai were taken. Um, and yeah,

**[02:25]** The.com andai were taken. Um, and yeah, everything was going great. We launched

**[02:27]** everything was going great. We launched

**[02:27]** everything was going great. We launched and deployed on versell. We had fluid

**[02:29]** and deployed on versell. We had fluid

**[02:29]** and deployed on versell. We had fluid compute on until we suddenly get this

**[02:30]** compute on until we suddenly get this

**[02:30]** compute on until we suddenly get this tweet. John said, "I asked how many Rs

**[02:34]** tweet. John said, "I asked how many Rs

**[02:34]** tweet. John said, "I asked how many Rs in Strawberry and it said two." So, of

**[02:38]** in Strawberry and it said two." So, of

**[02:38]** in Strawberry and it said two." So, of course, I just tested it twice. How is

**[02:40]** course, I just tested it twice. How is

**[02:40]** course, I just tested it twice. How is this even possible? Um, but I think you

**[02:42]** this even possible? Um, but I think you

**[02:42]** this even possible? Um, but I think you get where I'm going with this, which is

**[02:44]** get where I'm going with this, which is

**[02:44]** get where I'm going with this, which is that by nature, LMS can be very

**[02:47]** that by nature, LMS can be very

**[02:47]** that by nature, LMS can be very unreliable. And this principle scales

**[02:50]** unreliable. And this principle scales

**[02:50]** unreliable. And this principle scales from a small letter counting app all the

**[02:52]** from a small letter counting app all the

**[02:52]** from a small letter counting app all the way to the biggest AI apps in the world.

**[02:55]** way to the biggest AI apps in the world.

**[02:55]** way to the biggest AI apps in the world. The reason why it's so important to

**[02:57]** The reason why it's so important to

**[02:57]** The reason why it's so important to recognize this is because no one is

**[02:58]** recognize this is because no one is

**[02:58]** recognize this is because no one is going to use something that doesn't


### [03:00 - 04:00]

**[03:00]** going to use something that doesn't

**[03:00]** going to use something that doesn't work. It's literally unusable. Um, and

**[03:03]** work. It's literally unusable. Um, and

**[03:03]** work. It's literally unusable. Um, and this is a significant challenge when

**[03:04]** this is a significant challenge when

**[03:04]** this is a significant challenge when you're building AI apps. So, I have a

**[03:07]** you're building AI apps. So, I have a

**[03:07]** you're building AI apps. So, I have a funny meme here, but basically AI apps

**[03:09]** funny meme here, but basically AI apps

**[03:09]** funny meme here, but basically AI apps have this unique property. They're very

**[03:11]** have this unique property. They're very

**[03:11]** have this unique property. They're very like demo savvy. You'll demo it, it

**[03:13]** like demo savvy. You'll demo it, it

**[03:13]** like demo savvy. You'll demo it, it looks super good, you'll show it to your

**[03:15]** looks super good, you'll show it to your

**[03:15]** looks super good, you'll show it to your co-workers and then you ship to prod and

**[03:17]** co-workers and then you ship to prod and

**[03:17]** co-workers and then you ship to prod and then suddenly hallucinations come and

**[03:19]** then suddenly hallucinations come and

**[03:19]** then suddenly hallucinations come and get you. Um, so we always have this in

**[03:22]** get you. Um, so we always have this in

**[03:22]** get you. Um, so we always have this in in the back of our head when we're

**[03:23]** in the back of our head when we're

**[03:24]** in the back of our head when we're building

**[03:25]** building

**[03:25]** building back to where we were. Let's actually

**[03:27]** back to where we were. Let's actually

**[03:27]** back to where we were. Let's actually not give up, right? We actually want to

**[03:29]** not give up, right? We actually want to

**[03:29]** not give up, right? We actually want to solve this for our users. We want to

**[03:30]** solve this for our users. We want to

**[03:30]** solve this for our users. We want to make a really good fruit letter counting

**[03:32]** make a really good fruit letter counting

**[03:32]** make a really good fruit letter counting app. So you might say, how do we make

**[03:35]** app. So you might say, how do we make

**[03:35]** app. So you might say, how do we make reliable software that uses LLMs? Our

**[03:38]** reliable software that uses LLMs? Our

**[03:38]** reliable software that uses LLMs? Our initial uh prompt was a simple question,

**[03:40]** initial uh prompt was a simple question,

**[03:40]** initial uh prompt was a simple question, right? But maybe we can try prompt

**[03:42]** right? But maybe we can try prompt

**[03:42]** right? But maybe we can try prompt engineering. Maybe we can add some chain

**[03:43]** engineering. Maybe we can add some chain

**[03:43]** engineering. Maybe we can add some chain of thought, something else to make it

**[03:45]** of thought, something else to make it

**[03:45]** of thought, something else to make it more reliable. So, we spend all night

**[03:47]** more reliable. So, we spend all night

**[03:47]** more reliable. So, we spend all night working on this new prompt. Uh you're an

**[03:50]** working on this new prompt. Uh you're an

**[03:50]** working on this new prompt. Uh you're an exuberant fruitloving AI on an epic

**[03:52]** exuberant fruitloving AI on an epic

**[03:52]** exuberant fruitloving AI on an epic quest dot dot dot. Uh and this time we

**[03:55]** quest dot dot dot. Uh and this time we

**[03:55]** quest dot dot dot. Uh and this time we actually tested it 10 times in a row on

**[03:57]** actually tested it 10 times in a row on

**[03:57]** actually tested it 10 times in a row on ChachiBT. And it worked every single


### [04:00 - 05:00]

**[04:00]** ChachiBT. And it worked every single

**[04:00]** ChachiBT. And it worked every single time. 10 times in a row. It's amazing.

**[04:02]** time. 10 times in a row. It's amazing.

**[04:02]** time. 10 times in a row. It's amazing. So, we ship and everything was going

**[04:05]** So, we ship and everything was going

**[04:05]** So, we ship and everything was going great until

**[04:07]** great until

**[04:07]** great until John tweeted on me again and he said, "I

**[04:10]** John tweeted on me again and he said, "I

**[04:10]** John tweeted on me again and he said, "I asked how many Rs are in strawberry,

**[04:12]** asked how many Rs are in strawberry,

**[04:12]** asked how many Rs are in strawberry, banana, pineapple, mango, kiwi, dragon

**[04:14]** banana, pineapple, mango, kiwi, dragon

**[04:14]** banana, pineapple, mango, kiwi, dragon fruit, apple, raspberry, and it said

**[04:16]** fruit, apple, raspberry, and it said

**[04:16]** fruit, apple, raspberry, and it said five."

**[04:19]** five."

**[04:19]** five." So, we failed John again. Um, although

**[04:21]** So, we failed John again. Um, although

**[04:21]** So, we failed John again. Um, although this example is pretty simple, but this

**[04:23]** this example is pretty simple, but this

**[04:23]** this example is pretty simple, but this is actually what will happen when you

**[04:24]** is actually what will happen when you

**[04:24]** is actually what will happen when you start deploying to production. You'll

**[04:26]** start deploying to production. You'll

**[04:26]** start deploying to production. You'll get users that come up with queries you

**[04:28]** get users that come up with queries you

**[04:28]** get users that come up with queries you could have never imagined and you

**[04:30]** could have never imagined and you

**[04:30]** could have never imagined and you actually have to start up thinking about

**[04:31]** actually have to start up thinking about

**[04:31]** actually have to start up thinking about how do we solve it.

**[04:34]** how do we solve it.

**[04:34]** how do we solve it. And an interesting thing if you think

**[04:35]** And an interesting thing if you think

**[04:35]** And an interesting thing if you think about it is 95% of our app works 100% of

**[04:39]** about it is 95% of our app works 100% of

**[04:39]** about it is 95% of our app works 100% of the time. We can have unit tests for

**[04:41]** the time. We can have unit tests for

**[04:41]** the time. We can have unit tests for every single function end to end test

**[04:42]** every single function end to end test

**[04:42]** every single function end to end test for the off the login the sign out it

**[04:45]** for the off the login the sign out it

**[04:45]** for the off the login the sign out it will all work but it's that most crucial

**[04:47]** will all work but it's that most crucial

**[04:47]** will all work but it's that most crucial 5% that can fail on us. So let's improve

**[04:50]** 5% that can fail on us. So let's improve

**[04:50]** 5% that can fail on us. So let's improve it.

**[04:52]** it.

**[04:52]** it. Now to visualize this I have a diagram

**[04:54]** Now to visualize this I have a diagram

**[04:54]** Now to visualize this I have a diagram for you. Hopefully you can see the code.

**[04:56]** for you. Hopefully you can see the code.

**[04:56]** for you. Hopefully you can see the code. Uh maybe I need to make my screen

**[04:57]** Uh maybe I need to make my screen

**[04:57]** Uh maybe I need to make my screen brighter. Can you see the code? I don't


### [05:00 - 06:00]

**[05:00]** brighter. Can you see the code? I don't

**[05:00]** brighter. Can you see the code? I don't know. Okay. Um

**[05:04]** know. Okay. Um

**[05:04]** know. Okay. Um Okay. Well, we'll come back to this. But

**[05:06]** Okay. Well, we'll come back to this. But

**[05:06]** Okay. Well, we'll come back to this. But basically, we're going to start building

**[05:08]** basically, we're going to start building

**[05:08]** basically, we're going to start building evals. And to visualize this, I have a

**[05:11]** evals. And to visualize this, I have a

**[05:11]** evals. And to visualize this, I have a basketball court. So, today's day one of

**[05:13]** basketball court. So, today's day one of

**[05:13]** basketball court. So, today's day one of the NBA finals. I don't know if you

**[05:15]** the NBA finals. I don't know if you

**[05:15]** the NBA finals. I don't know if you care. Um you don't need to know much

**[05:16]** care. Um you don't need to know much

**[05:16]** care. Um you don't need to know much about basketball, but just know that

**[05:18]** about basketball, but just know that

**[05:18]** about basketball, but just know that someone is trying to throw a ball in the

**[05:20]** someone is trying to throw a ball in the

**[05:20]** someone is trying to throw a ball in the basket. And here the basket is the

**[05:22]** basket. And here the basket is the

**[05:22]** basket. And here the basket is the glowing golden cir uh glowing golden

**[05:24]** glowing golden cir uh glowing golden

**[05:24]** glowing golden cir uh glowing golden circle. So blue will represent a shot

**[05:27]** circle. So blue will represent a shot

**[05:27]** circle. So blue will represent a shot make and red will represent a shot miss.

**[05:31]** make and red will represent a shot miss.

**[05:31]** make and red will represent a shot miss. And one property to consider is that the

**[05:33]** And one property to consider is that the

**[05:33]** And one property to consider is that the farther away your shot is from the

**[05:35]** farther away your shot is from the

**[05:35]** farther away your shot is from the basket the harder it is. Uh another

**[05:38]** basket the harder it is. Uh another

**[05:38]** basket the harder it is. Uh another property is that the court has

**[05:39]** property is that the court has

**[05:39]** property is that the court has boundaries. So this blue dot although

**[05:41]** boundaries. So this blue dot although

**[05:41]** boundaries. So this blue dot although the shot goes in it's out of your uh out

**[05:43]** the shot goes in it's out of your uh out

**[05:43]** the shot goes in it's out of your uh out of the court. So it doesn't really count

**[05:45]** of the court. So it doesn't really count

**[05:45]** of the court. So it doesn't really count in the game. Let's start plotting our

**[05:47]** in the game. Let's start plotting our

**[05:47]** in the game. Let's start plotting our data. So here we have a question. How

**[05:50]** data. So here we have a question. How

**[05:50]** data. So here we have a question. How many Rs in strawberry? This after our

**[05:53]** many Rs in strawberry? This after our

**[05:53]** many Rs in strawberry? This after our new prompt will probably work. So, we'll

**[05:55]** new prompt will probably work. So, we'll

**[05:55]** new prompt will probably work. So, we'll label it blue. Um, and we'll put it

**[05:57]** label it blue. Um, and we'll put it

**[05:57]** label it blue. Um, and we'll put it close to the basket because it's pretty

**[05:59]** close to the basket because it's pretty

**[05:59]** close to the basket because it's pretty easy. However, how many Rs are in that


### [06:00 - 07:00]

**[06:00]** easy. However, how many Rs are in that

**[06:00]** easy. However, how many Rs are in that big array? We'll label it red. And we'll

**[06:03]** big array? We'll label it red. And we'll

**[06:03]** big array? We'll label it red. And we'll put it farther away from the basket.

**[06:06]** put it farther away from the basket.

**[06:06]** put it farther away from the basket. Hopefully, you can see that. Maybe we

**[06:08]** Hopefully, you can see that. Maybe we

**[06:08]** Hopefully, you can see that. Maybe we can make it a little bit brighter. But

**[06:10]** can make it a little bit brighter. But

**[06:10]** can make it a little bit brighter. But this is the data part of our eval.

**[06:12]** this is the data part of our eval.

**[06:12]** this is the data part of our eval. Basically, you're trying to collect uh

**[06:14]** Basically, you're trying to collect uh

**[06:14]** Basically, you're trying to collect uh what what prompts your users are asking.

**[06:16]** what what prompts your users are asking.

**[06:16]** what what prompts your users are asking. And you want to just store this over

**[06:18]** And you want to just store this over

**[06:18]** And you want to just store this over time and keep building it and store

**[06:20]** time and keep building it and store

**[06:20]** time and keep building it and store where these points are on your court.

**[06:23]** where these points are on your court.

**[06:23]** where these points are on your court. Two more prompts I want to bring up is

**[06:24]** Two more prompts I want to bring up is

**[06:24]** Two more prompts I want to bring up is like what if someone says how many Rs

**[06:26]** like what if someone says how many Rs

**[06:26]** like what if someone says how many Rs are in strawberry, pineapple, dragon

**[06:27]** are in strawberry, pineapple, dragon

**[06:28]** are in strawberry, pineapple, dragon fruit, mango after we replace all the

**[06:30]** fruit, mango after we replace all the

**[06:30]** fruit, mango after we replace all the vowels with Rs, right? Insane prompt,

**[06:34]** vowels with Rs, right? Insane prompt,

**[06:34]** vowels with Rs, right? Insane prompt, but still technically in our domain. Uh

**[06:37]** but still technically in our domain. Uh

**[06:37]** but still technically in our domain. Uh so we'll we'll label it as red all the

**[06:39]** so we'll we'll label it as red all the

**[06:39]** so we'll we'll label it as red all the way down there. U but a funny one is

**[06:41]** way down there. U but a funny one is

**[06:41]** way down there. U but a funny one is like how many syllables are in carrot?

**[06:44]** like how many syllables are in carrot?

**[06:44]** like how many syllables are in carrot? So this we'll call it out of bounds,

**[06:46]** So this we'll call it out of bounds,

**[06:46]** So this we'll call it out of bounds, right? This no none of our users are

**[06:47]** right? This no none of our users are

**[06:48]** right? This no none of our users are actually going to ask. Um it's not part

**[06:49]** actually going to ask. Um it's not part

**[06:49]** actually going to ask. Um it's not part of our app, so no one is going to care.

**[06:53]** of our app, so no one is going to care.

**[06:53]** of our app, so no one is going to care. Um I hope you can see the code, but

**[06:56]** Um I hope you can see the code, but

**[06:56]** Um I hope you can see the code, but basically when you're making evout,

**[06:58]** basically when you're making evout,

**[06:58]** basically when you're making evout, here's how you can think about it. Your


### [07:00 - 08:00]

**[07:00]** here's how you can think about it. Your

**[07:00]** here's how you can think about it. Your data is the point on the court. Your

**[07:02]** data is the point on the court. Your

**[07:02]** data is the point on the court. Your shot or in this case in brain trust,

**[07:04]** shot or in this case in brain trust,

**[07:04]** shot or in this case in brain trust, they call it a task is the way you shoot

**[07:06]** they call it a task is the way you shoot

**[07:06]** they call it a task is the way you shoot the ball towards the basket. And your

**[07:08]** the ball towards the basket. And your

**[07:08]** the ball towards the basket. And your score is basically a check of did it go

**[07:10]** score is basically a check of did it go

**[07:10]** score is basically a check of did it go in the basket or did it not go in the

**[07:12]** in the basket or did it not go in the

**[07:12]** in the basket or did it not go in the basket.

**[07:13]** basket.

**[07:13]** basket. To make good evals, you must understand

**[07:16]** To make good evals, you must understand

**[07:16]** To make good evals, you must understand your court. This is the most important

**[07:17]** your court. This is the most important

**[07:17]** your court. This is the most important step.

**[07:20]** step.

**[07:20]** step. And you have to be careful of falling

**[07:21]** And you have to be careful of falling

**[07:21]** And you have to be careful of falling into some traps. First is the out-of-

**[07:23]** into some traps. First is the out-of-

**[07:23]** into some traps. First is the out-of- bounds traps. Don't spend time making

**[07:26]** bounds traps. Don't spend time making

**[07:26]** bounds traps. Don't spend time making emails for your data your users don't

**[07:28]** emails for your data your users don't

**[07:28]** emails for your data your users don't care about. You have enough problems, I

**[07:30]** care about. You have enough problems, I

**[07:30]** care about. You have enough problems, I promise you, of problem uh queries that

**[07:32]** promise you, of problem uh queries that

**[07:32]** promise you, of problem uh queries that your users do care about. So be careful

**[07:35]** your users do care about. So be careful

**[07:35]** your users do care about. So be careful not try and be productive and you know

**[07:37]** not try and be productive and you know

**[07:37]** not try and be productive and you know you're making a lot of evals but they're

**[07:39]** you're making a lot of evals but they're

**[07:39]** you're making a lot of evals but they're not really applicable to your app. And

**[07:41]** not really applicable to your app. And

**[07:41]** not really applicable to your app. And another visualization is don't have a

**[07:43]** another visualization is don't have a

**[07:43]** another visualization is don't have a concentrated set of points. When you

**[07:45]** concentrated set of points. When you

**[07:45]** concentrated set of points. When you really understand your core you're going

**[07:47]** really understand your core you're going

**[07:47]** really understand your core you're going to understand you know where the

**[07:48]** to understand you know where the

**[07:48]** to understand you know where the boundaries are and you want to make sure

**[07:49]** boundaries are and you want to make sure

**[07:49]** boundaries are and you want to make sure you you test across the entire court.

**[07:53]** you you test across the entire court.

**[07:53]** you you test across the entire court. Uh a lot of people have been talking

**[07:54]** Uh a lot of people have been talking

**[07:54]** Uh a lot of people have been talking about this today but to collect as much

**[07:56]** about this today but to collect as much

**[07:56]** about this today but to collect as much data as possible here are some uh things

**[07:58]** data as possible here are some uh things

**[07:58]** data as possible here are some uh things you can do. First is collect thumbs up


### [08:00 - 09:00]

**[08:00]** you can do. First is collect thumbs up

**[08:00]** you can do. First is collect thumbs up thumbs down data. This can be noisy but

**[08:03]** thumbs down data. This can be noisy but

**[08:03]** thumbs down data. This can be noisy but it also can be really really good signal

**[08:05]** it also can be really really good signal

**[08:05]** it also can be really really good signal as to where your app is struggling.

**[08:07]** as to where your app is struggling.

**[08:07]** as to where your app is struggling. Another thing is if you have

**[08:08]** Another thing is if you have

**[08:08]** Another thing is if you have observability which is highly

**[08:09]** observability which is highly

**[08:10]** observability which is highly recommended you can just read through

**[08:11]** recommended you can just read through

**[08:11]** recommended you can just read through random samples in your log in your logs.

**[08:14]** random samples in your log in your logs.

**[08:14]** random samples in your log in your logs. Um although users might not be you know

**[08:16]** Um although users might not be you know

**[08:16]** Um although users might not be you know giving you signal but if you take like a

**[08:18]** giving you signal but if you take like a

**[08:18]** giving you signal but if you take like a hundred random samples and go through it

**[08:19]** hundred random samples and go through it

**[08:19]** hundred random samples and go through it like once a week you'll get a really un

**[08:21]** like once a week you'll get a really un

**[08:21]** like once a week you'll get a really un good understanding of what your users

**[08:24]** good understanding of what your users

**[08:24]** good understanding of what your users and how your users are using the

**[08:25]** and how your users are using the

**[08:25]** and how your users are using the product. Uh if you have community forums

**[08:28]** product. Uh if you have community forums

**[08:28]** product. Uh if you have community forums these are also great. People will often

**[08:29]** these are also great. People will often

**[08:29]** these are also great. People will often report issues they're having with the

**[08:31]** report issues they're having with the

**[08:31]** report issues they're having with the LLM and also X and Twitter are also

**[08:34]** LLM and also X and Twitter are also

**[08:34]** LLM and also X and Twitter are also great but can be noisy. And there really

**[08:36]** great but can be noisy. And there really

**[08:36]** great but can be noisy. And there really is no shortcut here. You really have to

**[08:39]** is no shortcut here. You really have to

**[08:39]** is no shortcut here. You really have to do the work and understand what your

**[08:40]** do the work and understand what your

**[08:40]** do the work and understand what your court looks like. So here is actually

**[08:44]** court looks like. So here is actually

**[08:44]** court looks like. So here is actually what if you are doing a good job of

**[08:46]** what if you are doing a good job of

**[08:46]** what if you are doing a good job of understanding your court and a good job

**[08:47]** understanding your court and a good job

**[08:47]** understanding your court and a good job of building your data set. This is what

**[08:49]** of building your data set. This is what

**[08:49]** of building your data set. This is what it should look like. You should know the

**[08:50]** it should look like. You should know the

**[08:50]** it should look like. You should know the boundaries. You should be testing in

**[08:52]** boundaries. You should be testing in

**[08:52]** boundaries. You should be testing in your boundaries and you should

**[08:53]** your boundaries and you should

**[08:53]** your boundaries and you should understand where your system is has blue

**[08:56]** understand where your system is has blue

**[08:56]** understand where your system is has blue and verse where it has red. So here it's

**[08:59]** and verse where it has red. So here it's

**[08:59]** and verse where it has red. So here it's really easy to tell, okay, maybe next


### [09:00 - 10:00]

**[09:01]** really easy to tell, okay, maybe next

**[09:01]** really easy to tell, okay, maybe next week we need to prioritize uh the team

**[09:03]** week we need to prioritize uh the team

**[09:03]** week we need to prioritize uh the team to work on that bottom right corner.

**[09:05]** to work on that bottom right corner.

**[09:05]** to work on that bottom right corner. This is something where a lot of users

**[09:07]** This is something where a lot of users

**[09:07]** This is something where a lot of users are struggling and we can really do a

**[09:09]** are struggling and we can really do a

**[09:09]** are struggling and we can really do a good job on flipping the tiles from red

**[09:11]** good job on flipping the tiles from red

**[09:11]** good job on flipping the tiles from red to blue.

**[09:17]** Another thing you can do and I hope I

**[09:17]** Another thing you can do and I hope I really hope you can see but you want to

**[09:20]** really hope you can see but you want to

**[09:20]** really hope you can see but you want to put constants in data variables in the

**[09:23]** put constants in data variables in the

**[09:23]** put constants in data variables in the task. So just like in math or

**[09:25]** task. So just like in math or

**[09:25]** task. So just like in math or programming, you want to factor

**[09:27]** programming, you want to factor

**[09:27]** programming, you want to factor constants so it improves clarity, reuse,

**[09:29]** constants so it improves clarity, reuse,

**[09:29]** constants so it improves clarity, reuse, and generalizations.

**[09:31]** and generalizations.

**[09:32]** and generalizations. If you have, let's say you want to test

**[09:33]** If you have, let's say you want to test

**[09:34]** If you have, let's say you want to test your system prompt, right? Keep the

**[09:35]** your system prompt, right? Keep the

**[09:36]** your system prompt, right? Keep the constant data that all that your users

**[09:37]** constant data that all that your users

**[09:37]** constant data that all that your users are going to ask. So for example, how

**[09:39]** are going to ask. So for example, how

**[09:39]** are going to ask. So for example, how many RS and strawberry that goes in the

**[09:40]** many RS and strawberry that goes in the

**[09:40]** many RS and strawberry that goes in the data that's a constant. It's never going

**[09:42]** data that's a constant. It's never going

**[09:42]** data that's a constant. It's never going to change throughout your app. But what

**[09:44]** to change throughout your app. But what

**[09:44]** to change throughout your app. But what you're going to test is in that task,

**[09:46]** you're going to test is in that task,

**[09:46]** you're going to test is in that task, you're going to try different system

**[09:47]** you're going to try different system

**[09:47]** you're going to try different system prompts. You might try different

**[09:48]** prompts. You might try different

**[09:48]** prompts. You might try different pre-processing, different rag, and

**[09:50]** pre-processing, different rag, and

**[09:50]** pre-processing, different rag, and that's what you want to put in your task

**[09:51]** that's what you want to put in your task

**[09:52]** that's what you want to put in your task section. This way your app actually

**[09:54]** section. This way your app actually

**[09:54]** section. This way your app actually scales and you never have to let's say

**[09:55]** scales and you never have to let's say

**[09:56]** scales and you never have to let's say when you change your system prompt redo

**[09:57]** when you change your system prompt redo

**[09:57]** when you change your system prompt redo all your data and this is a really nice

**[09:59]** all your data and this is a really nice

**[09:59]** all your data and this is a really nice feature of brain trust. Um and if you


### [10:00 - 11:00]

**[10:02]** feature of brain trust. Um and if you

**[10:02]** feature of brain trust. Um and if you don't know AI SDK actually offers a

**[10:05]** don't know AI SDK actually offers a

**[10:05]** don't know AI SDK actually offers a thing called middleware and it's a

**[10:07]** thing called middleware and it's a

**[10:07]** thing called middleware and it's a really good abstraction to put basically

**[10:09]** really good abstraction to put basically

**[10:10]** really good abstraction to put basically all your logic of pre-processing. So rag

**[10:12]** all your logic of pre-processing. So rag

**[10:12]** all your logic of pre-processing. So rag system prompt you can put in here etc.

**[10:14]** system prompt you can put in here etc.

**[10:14]** system prompt you can put in here etc. And you can now share this between your

**[10:17]** And you can now share this between your

**[10:17]** And you can now share this between your actual API route that's doing the

**[10:18]** actual API route that's doing the

**[10:18]** actual API route that's doing the completion and your evals. So, if you

**[10:20]** completion and your evals. So, if you

**[10:20]** completion and your evals. So, if you think about the court, the basketball

**[10:21]** think about the court, the basketball

**[10:21]** think about the court, the basketball court as if we're doing we're going like

**[10:23]** court as if we're doing we're going like

**[10:23]** court as if we're doing we're going like basketball practice and we're trying to

**[10:25]** basketball practice and we're trying to

**[10:25]** basketball practice and we're trying to practice our system ac across different

**[10:27]** practice our system ac across different

**[10:27]** practice our system ac across different models. Um, you want your practice to be

**[10:30]** models. Um, you want your practice to be

**[10:30]** models. Um, you want your practice to be as similar as possible to the real game.

**[10:32]** as similar as possible to the real game.

**[10:32]** as similar as possible to the real game. That's what makes a good practice. So,

**[10:34]** That's what makes a good practice. So,

**[10:34]** That's what makes a good practice. So, you want to share the pretty much the

**[10:36]** you want to share the pretty much the

**[10:36]** you want to share the pretty much the exact same code between evals and what

**[10:38]** exact same code between evals and what

**[10:38]** exact same code between evals and what you're actually running.

**[10:40]** you're actually running.

**[10:40]** you're actually running. Now, I want to talk a little bit about

**[10:42]** Now, I want to talk a little bit about

**[10:42]** Now, I want to talk a little bit about scores, which is the last step of the

**[10:44]** scores, which is the last step of the

**[10:44]** scores, which is the last step of the eval. The unfortunate thing is it does

**[10:47]** eval. The unfortunate thing is it does

**[10:47]** eval. The unfortunate thing is it does vary greatly depending on your domain.

**[10:50]** vary greatly depending on your domain.

**[10:50]** vary greatly depending on your domain. So in this case it's like super simple.

**[10:52]** So in this case it's like super simple.

**[10:52]** So in this case it's like super simple. Uh you're just checking if you know the

**[10:54]** Uh you're just checking if you know the

**[10:54]** Uh you're just checking if you know the output contains the correct number of

**[10:56]** output contains the correct number of

**[10:56]** output contains the correct number of letters. But maybe if you're doing

**[10:58]** letters. But maybe if you're doing

**[10:58]** letters. But maybe if you're doing writing a task like writing that's very


### [11:00 - 12:00]

**[11:00]** writing a task like writing that's very

**[11:00]** writing a task like writing that's very very difficult. Um

**[11:03]** very difficult. Um

**[11:03]** very difficult. Um from principles you want to actually

**[11:04]** from principles you want to actually

**[11:04]** from principles you want to actually lean towards deterministic scoring and

**[11:06]** lean towards deterministic scoring and

**[11:06]** lean towards deterministic scoring and pass fail. This is because when you're

**[11:08]** pass fail. This is because when you're

**[11:08]** pass fail. This is because when you're doing debugging, uh, you're going to get

**[11:10]** doing debugging, uh, you're going to get

**[11:10]** doing debugging, uh, you're going to get a ton of input and logs and you want to

**[11:13]** a ton of input and logs and you want to

**[11:13]** a ton of input and logs and you want to make it as easy as possible for you to

**[11:15]** make it as easy as possible for you to

**[11:15]** make it as easy as possible for you to actually figure out what's going wrong.

**[11:16]** actually figure out what's going wrong.

**[11:16]** actually figure out what's going wrong. So, if you're sh if you're building if

**[11:18]** So, if you're sh if you're building if

**[11:18]** So, if you're sh if you're building if you're overengineering your score, it

**[11:20]** you're overengineering your score, it

**[11:20]** you're overengineering your score, it might be very difficult to share with

**[11:21]** might be very difficult to share with

**[11:21]** might be very difficult to share with your team and distribute across

**[11:23]** your team and distribute across

**[11:23]** your team and distribute across different teams uh, your evals because

**[11:25]** different teams uh, your evals because

**[11:25]** different teams uh, your evals because no one will understand how these things

**[11:27]** no one will understand how these things

**[11:27]** no one will understand how these things are getting scored. Keep your scores as

**[11:29]** are getting scored. Keep your scores as

**[11:29]** are getting scored. Keep your scores as simple as possible. Um, and a good

**[11:32]** simple as possible. Um, and a good

**[11:32]** simple as possible. Um, and a good question to ask yourself is when you're

**[11:33]** question to ask yourself is when you're

**[11:33]** question to ask yourself is when you're looking at the data, what am I looking

**[11:35]** looking at the data, what am I looking

**[11:35]** looking at the data, what am I looking for to see if this failed? Right? So

**[11:37]** for to see if this failed? Right? So

**[11:37]** for to see if this failed? Right? So with Vzero, we're looking for if the

**[11:39]** with Vzero, we're looking for if the

**[11:39]** with Vzero, we're looking for if the code didn't work. Um, but maybe for

**[11:41]** code didn't work. Um, but maybe for

**[11:41]** code didn't work. Um, but maybe for writing, you're looking for a certain

**[11:43]** writing, you're looking for a certain

**[11:43]** writing, you're looking for a certain linguistics.

**[11:44]** linguistics.

**[11:44]** linguistics. Ask yourself that question and write the

**[11:46]** Ask yourself that question and write the

**[11:46]** Ask yourself that question and write the code that looks for you. Um, there are

**[11:48]** code that looks for you. Um, there are

**[11:48]** code that looks for you. Um, there are some cases where it's so hard to write

**[11:50]** some cases where it's so hard to write

**[11:50]** some cases where it's so hard to write the code that you may need to do human

**[11:52]** the code that you may need to do human

**[11:52]** the code that you may need to do human review and that's okay. At the end of

**[11:55]** review and that's okay. At the end of

**[11:55]** review and that's okay. At the end of the day, you want to build your core and

**[11:56]** the day, you want to build your core and

**[11:56]** the day, you want to build your core and you want to collect signal even if you

**[11:58]** you want to collect signal even if you

**[11:58]** you want to collect signal even if you need you must do human human review to


### [12:00 - 13:00]

**[12:00]** need you must do human human review to

**[12:00]** need you must do human human review to get the correct signal. Don't worry at

**[12:02]** get the correct signal. Don't worry at

**[12:02]** get the correct signal. Don't worry at the if you do the correct practice, it

**[12:04]** the if you do the correct practice, it

**[12:04]** the if you do the correct practice, it will pay off in the long run and you'll

**[12:06]** will pay off in the long run and you'll

**[12:06]** will pay off in the long run and you'll get better results for your users.

**[12:09]** get better results for your users.

**[12:09]** get better results for your users. One trick you can do for scoring is

**[12:12]** One trick you can do for scoring is

**[12:12]** One trick you can do for scoring is don't be scared to like add a little bit

**[12:13]** don't be scared to like add a little bit

**[12:14]** don't be scared to like add a little bit of extra um prompt to your to the

**[12:17]** of extra um prompt to your to the

**[12:17]** of extra um prompt to your to the original prompt. So for example, here we

**[12:18]** original prompt. So for example, here we

**[12:18]** original prompt. So for example, here we can say output your final answer uh in

**[12:21]** can say output your final answer uh in

**[12:21]** can say output your final answer uh in these answer tags. What this will do is

**[12:23]** these answer tags. What this will do is

**[12:23]** these answer tags. What this will do is basically make it very easy for you to

**[12:25]** basically make it very easy for you to

**[12:25]** basically make it very easy for you to do string matching um and etc. Whereas

**[12:28]** do string matching um and etc. Whereas

**[12:28]** do string matching um and etc. Whereas in production you don't really want this

**[12:30]** in production you don't really want this

**[12:30]** in production you don't really want this but yeah you can do some little twe

**[12:32]** but yeah you can do some little twe

**[12:32]** but yeah you can do some little twe tweaks to your prompts so that scoring

**[12:34]** tweaks to your prompts so that scoring

**[12:34]** tweaks to your prompts so that scoring is easier.

**[12:36]** is easier.

**[12:36]** is easier. Another thing we really highly recommend

**[12:38]** Another thing we really highly recommend

**[12:38]** Another thing we really highly recommend is add evals to your CI. So brain trust

**[12:41]** is add evals to your CI. So brain trust

**[12:41]** is add evals to your CI. So brain trust is really nice because you can get these

**[12:42]** is really nice because you can get these

**[12:42]** is really nice because you can get these eval reports. Um so it'll run your e

**[12:45]** eval reports. Um so it'll run your e

**[12:45]** eval reports. Um so it'll run your e your task across all your data and then

**[12:47]** your task across all your data and then

**[12:47]** your task across all your data and then it will give you this uh report at the

**[12:49]** it will give you this uh report at the

**[12:49]** it will give you this uh report at the end for the improvements and

**[12:51]** end for the improvements and

**[12:51]** end for the improvements and regressions. Assume my colleague made a

**[12:53]** regressions. Assume my colleague made a

**[12:53]** regressions. Assume my colleague made a PR that changes a bit of the prompt. We

**[12:55]** PR that changes a bit of the prompt. We

**[12:55]** PR that changes a bit of the prompt. We want to know like how did it do across

**[12:57]** want to know like how did it do across

**[12:57]** want to know like how did it do across the court, right? Visualize like did it

**[12:58]** the court, right? Visualize like did it

**[12:58]** the court, right? Visualize like did it change more tiles from red to blue?


### [13:00 - 14:00]

**[13:00]** change more tiles from red to blue?

**[13:00]** change more tiles from red to blue? Maybe now our prompt fixed one part but

**[13:03]** Maybe now our prompt fixed one part but

**[13:03]** Maybe now our prompt fixed one part but it broke the other part of our app. Um

**[13:05]** it broke the other part of our app. Um

**[13:05]** it broke the other part of our app. Um so this is a really useful report to

**[13:07]** so this is a really useful report to

**[13:07]** so this is a really useful report to have when you're doing PRs.

**[13:10]** have when you're doing PRs.

**[13:10]** have when you're doing PRs. So yeah, going back this this is the

**[13:12]** So yeah, going back this this is the

**[13:12]** So yeah, going back this this is the summary of the talk. You want to make

**[13:14]** summary of the talk. You want to make

**[13:14]** summary of the talk. You want to make your evals a a core of your data. And

**[13:18]** your evals a a core of your data. And

**[13:18]** your evals a a core of your data. And this you can treat it like practice.

**[13:20]** this you can treat it like practice.

**[13:20]** this you can treat it like practice. Your model is basically going to

**[13:21]** Your model is basically going to

**[13:21]** Your model is basically going to practice. Maybe you want to switch

**[13:23]** practice. Maybe you want to switch

**[13:23]** practice. Maybe you want to switch players, right? When you switch models,

**[13:24]** players, right? When you switch models,

**[13:24]** players, right? When you switch models, you can see how a different player is

**[13:26]** you can see how a different player is

**[13:26]** you can see how a different player is going to perform in your practice. But

**[13:27]** going to perform in your practice. But

**[13:28]** going to perform in your practice. But this gives you such a good understanding

**[13:29]** this gives you such a good understanding

**[13:29]** this gives you such a good understanding of how your system is doing when you

**[13:31]** of how your system is doing when you

**[13:31]** of how your system is doing when you change things like maybe your rag or

**[13:33]** change things like maybe your rag or

**[13:34]** change things like maybe your rag or your system prompt. And you can now go

**[13:35]** your system prompt. And you can now go

**[13:35]** your system prompt. And you can now go to your colleague and say, "Hey, this

**[13:37]** to your colleague and say, "Hey, this

**[13:37]** to your colleague and say, "Hey, this actually did help our app, right?"

**[13:39]** actually did help our app, right?"

**[13:39]** actually did help our app, right?" Because improvement without measurement

**[13:42]** Because improvement without measurement

**[13:42]** Because improvement without measurement is limited and imprecise. And eval give

**[13:45]** is limited and imprecise. And eval give

**[13:45]** is limited and imprecise. And eval give you the clarity you need to

**[13:46]** you the clarity you need to

**[13:46]** you the clarity you need to systematically improve your app.

**[13:50]** systematically improve your app.

**[13:50]** systematically improve your app. When you do that, you're going to get

**[13:52]** When you do that, you're going to get

**[13:52]** When you do that, you're going to get better reliability and quality, higher

**[13:54]** better reliability and quality, higher

**[13:54]** better reliability and quality, higher conversion and retention, and you also

**[13:56]** conversion and retention, and you also

**[13:56]** conversion and retention, and you also get to do just spend less time on

**[13:58]** get to do just spend less time on

**[13:58]** get to do just spend less time on support and ops, right? Because your

**[13:59]** support and ops, right? Because your

**[13:59]** support and ops, right? Because your evals, your practice environment will


### [14:00 - 15:00]

**[14:01]** evals, your practice environment will

**[14:01]** evals, your practice environment will take care of that for you. Uh, and if

**[14:03]** take care of that for you. Uh, and if

**[14:03]** take care of that for you. Uh, and if you're wondering about how I built all

**[14:05]** you're wondering about how I built all

**[14:05]** you're wondering about how I built all these court diagrams, I actually just

**[14:06]** these court diagrams, I actually just

**[14:06]** these court diagrams, I actually just used Vzero and it made me some app that

**[14:08]** used Vzero and it made me some app that

**[14:08]** used Vzero and it made me some app that I just added these shots made and missed

**[14:11]** I just added these shots made and missed

**[14:11]** I just added these shots made and missed in uh the basket. So, yeah, thank you

**[14:14]** in uh the basket. So, yeah, thank you

**[14:14]** in uh the basket. So, yeah, thank you very much. I hope you learned a little

**[14:15]** very much. I hope you learned a little

**[14:15]** very much. I hope you learned a little bit about evals. Thank you.

**[14:18]** bit about evals. Thank you.

**[14:18]** bit about evals. Thank you. So, we do have some time for some

**[14:20]** So, we do have some time for some

**[14:20]** So, we do have some time for some questions. There are two mics, one over

**[14:22]** questions. There are two mics, one over

**[14:22]** questions. There are two mics, one over here, one over there. Um, we can take

**[14:25]** here, one over there. Um, we can take

**[14:25]** here, one over there. Um, we can take two or three of those, please, if

**[14:27]** two or three of those, please, if

**[14:27]** two or three of those, please, if anybody's interested in asking.

**[14:29]** anybody's interested in asking.

**[14:29]** anybody's interested in asking. We have one over there.

**[14:32]** We have one over there.

**[14:32]** We have one over there. Um, mic five, please.

**[14:36]** Um, mic five, please.

**[14:36]** Um, mic five, please. Or you can repeat the question as well

**[14:38]** Or you can repeat the question as well

**[14:38]** Or you can repeat the question as well if you don't mind.

**[14:44]** Yeah. Yeah. You can think of it. It's

**[14:44]** Yeah. Yeah. You can think of it. It's really like practice. Like maybe your a

**[14:47]** really like practice. Like maybe your a

**[14:47]** really like practice. Like maybe your a basketball player will like, you know,

**[14:49]** basketball player will like, you know,

**[14:49]** basketball player will like, you know, in general score like 90% but they might

**[14:51]** in general score like 90% but they might

**[14:51]** in general score like 90% but they might miss more shots here or there. If you

**[14:53]** miss more shots here or there. If you

**[14:53]** miss more shots here or there. If you run it like we do it like we run every

**[14:55]** run it like we do it like we run every

**[14:55]** run it like we do it like we run every day at least. Um and then we get a good

**[14:57]** day at least. Um and then we get a good

**[14:57]** day at least. Um and then we get a good sense of like where are we actually like


### [15:00 - 16:00]

**[15:00]** sense of like where are we actually like

**[15:00]** sense of like where are we actually like failing? Did we have some regression? Um

**[15:02]** failing? Did we have some regression? Um

**[15:02]** failing? Did we have some regression? Um so yeah, running it like pre daily or at

**[15:04]** so yeah, running it like pre daily or at

**[15:04]** so yeah, running it like pre daily or at least in some schedule will give you a

**[15:05]** least in some schedule will give you a

**[15:05]** least in some schedule will give you a good idea. I was thinking what if you

**[15:07]** good idea. I was thinking what if you

**[15:07]** good idea. I was thinking what if you ran like you know the same question

**[15:09]** ran like you know the same question

**[15:09]** ran like you know the same question through it five times, right? It's like

**[15:11]** through it five times, right? It's like

**[15:11]** through it five times, right? It's like like what's the percentage? just making

**[15:13]** like what's the percentage? just making

**[15:13]** like what's the percentage? just making it four out of five or you know five

**[15:15]** it four out of five or you know five

**[15:15]** it four out of five or you know five right. So it's definitely like as you go

**[15:17]** right. So it's definitely like as you go

**[15:17]** right. So it's definitely like as you go further away like the harder questions

**[15:19]** further away like the harder questions

**[15:19]** further away like the harder questions get like


