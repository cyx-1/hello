# Rishabh Garg, Tesla Optimus — Challenges in High Performance Robotics Systems

**Video URL:** https://www.youtube.com/watch?v=bCGbuyv8PMk

---

## Full Transcript

### [00:00 - 01:00]

**[00:17]** Right. Good afternoon everyone and

**[00:17]** Right. Good afternoon everyone and really excited to be here today. Really

**[00:18]** really excited to be here today. Really

**[00:18]** really excited to be here today. Really exciting stuff so far. So many models,

**[00:20]** exciting stuff so far. So many models,

**[00:20]** exciting stuff so far. So many models, so many new ideas and today I want to

**[00:23]** so many new ideas and today I want to

**[00:24]** so many new ideas and today I want to talk about what happens between the

**[00:26]** talk about what happens between the

**[00:26]** talk about what happens between the controller and the wire. Now we have

**[00:28]** controller and the wire. Now we have

**[00:28]** controller and the wire. Now we have seen so many policies that work that

**[00:29]** seen so many policies that work that

**[00:29]** seen so many policies that work that control robots but again we that we need

**[00:32]** control robots but again we that we need

**[00:32]** control robots but again we that we need to get that data to the actuators we

**[00:34]** to get that data to the actuators we

**[00:34]** to get that data to the actuators we need to get that data from sensors and

**[00:36]** need to get that data from sensors and

**[00:36]** need to get that data from sensors and feed the whole system and what happens

**[00:38]** feed the whole system and what happens

**[00:38]** feed the whole system and what happens if your carefully crafted policy does

**[00:40]** if your carefully crafted policy does

**[00:40]** if your carefully crafted policy does not work as expected like is this issue

**[00:42]** not work as expected like is this issue

**[00:42]** not work as expected like is this issue in the policy or is it in the software

**[00:44]** in the policy or is it in the software

**[00:44]** in the policy or is it in the software system. So today we look at a lot of

**[00:46]** system. So today we look at a lot of

**[00:46]** system. So today we look at a lot of instances where the issue will look like

**[00:48]** instances where the issue will look like

**[00:48]** instances where the issue will look like it's the policy but it's actually the

**[00:49]** it's the policy but it's actually the

**[00:50]** it's the policy but it's actually the software system and along the way we'll

**[00:51]** software system and along the way we'll

**[00:52]** software system and along the way we'll try to design a very small toy robotics

**[00:54]** try to design a very small toy robotics

**[00:54]** try to design a very small toy robotics robot. So why this talk again? Well,

**[00:57]** robot. So why this talk again? Well,

**[00:57]** robot. So why this talk again? Well, robots are complex. So many systems, so

**[00:59]** robots are complex. So many systems, so

**[00:59]** robots are complex. So many systems, so many different software components, and


### [01:00 - 02:00]

**[01:01]** many different software components, and

**[01:01]** many different software components, and yet you're focused on like one big

**[01:04]** yet you're focused on like one big

**[01:04]** yet you're focused on like one big question. When things go wrong on the

**[01:06]** question. When things go wrong on the

**[01:06]** question. When things go wrong on the robot, when you don't see that motor

**[01:08]** robot, when you don't see that motor

**[01:08]** robot, when you don't see that motor move, what's the root cause? Is the

**[01:10]** move, what's the root cause? Is the

**[01:10]** move, what's the root cause? Is the policy that is not giving the command or

**[01:13]** policy that is not giving the command or

**[01:13]** policy that is not giving the command or is it the software system? And this is a

**[01:15]** is it the software system? And this is a

**[01:15]** is it the software system? And this is a question that I grapple almost every

**[01:16]** question that I grapple almost every

**[01:16]** question that I grapple almost every day. And so I want to talk about what

**[01:18]** day. And so I want to talk about what

**[01:18]** day. And so I want to talk about what I've seen so far and how to diagnose

**[01:21]** I've seen so far and how to diagnose

**[01:21]** I've seen so far and how to diagnose these issues on the robot. So let's go

**[01:23]** these issues on the robot. So let's go

**[01:23]** these issues on the robot. So let's go into the buildup. Let's try build a very

**[01:25]** into the buildup. Let's try build a very

**[01:25]** into the buildup. Let's try build a very small uh toy robotics general

**[01:26]** small uh toy robotics general

**[01:26]** small uh toy robotics general architecture, right? Like this is what a

**[01:27]** architecture, right? Like this is what a

**[01:27]** architecture, right? Like this is what a general robot would look like. You'd

**[01:29]** general robot would look like. You'd

**[01:29]** general robot would look like. You'd have some actuators, a CPU, maybe a

**[01:31]** have some actuators, a CPU, maybe a

**[01:31]** have some actuators, a CPU, maybe a hybrid accelerator and then a sensor.

**[01:34]** hybrid accelerator and then a sensor.

**[01:34]** hybrid accelerator and then a sensor. Perfect. Now, one of the most critical

**[01:36]** Perfect. Now, one of the most critical

**[01:36]** Perfect. Now, one of the most critical aspects is the communication protocol.

**[01:39]** aspects is the communication protocol.

**[01:39]** aspects is the communication protocol. So for our our talk, we'll use CAN. CAN

**[01:42]** So for our our talk, we'll use CAN. CAN

**[01:42]** So for our our talk, we'll use CAN. CAN is great. CAN is open source. Everyone

**[01:44]** is great. CAN is open source. Everyone

**[01:44]** is great. CAN is open source. Everyone can use CAN. It's cheap. It's

**[01:45]** can use CAN. It's cheap. It's

**[01:45]** can use CAN. It's cheap. It's affordable. And it has enough data rate

**[01:48]** affordable. And it has enough data rate

**[01:48]** affordable. And it has enough data rate and enough compatibility for a lot of

**[01:50]** and enough compatibility for a lot of

**[01:50]** and enough compatibility for a lot of components out there. So we'll stick to

**[01:52]** components out there. So we'll stick to

**[01:52]** components out there. So we'll stick to can and uh we'll see how that influence

**[01:54]** can and uh we'll see how that influence

**[01:54]** can and uh we'll see how that influence a lot of the design design decisions

**[01:55]** a lot of the design design decisions

**[01:56]** a lot of the design design decisions down the line. All right. So let's also

**[01:59]** down the line. All right. So let's also

**[01:59]** down the line. All right. So let's also start simple with the code. We'll start


### [02:00 - 03:00]

**[02:01]** start simple with the code. We'll start

**[02:01]** start simple with the code. We'll start with receiving the data giving that to

**[02:03]** with receiving the data giving that to

**[02:03]** with receiving the data giving that to the policy and basically sending it back

**[02:05]** the policy and basically sending it back

**[02:05]** the policy and basically sending it back out. Nothing nothing happening nothing

**[02:07]** out. Nothing nothing happening nothing

**[02:07]** out. Nothing nothing happening nothing fancy right. And let's assume that we

**[02:09]** fancy right. And let's assume that we

**[02:09]** fancy right. And let's assume that we have approximately 2 milliseconds for

**[02:11]** have approximately 2 milliseconds for

**[02:11]** have approximately 2 milliseconds for our policy. And this is what we should

**[02:15]** our policy. And this is what we should

**[02:15]** our policy. And this is what we should expect to see, right? Our loops running.

**[02:17]** expect to see, right? Our loops running.

**[02:17]** expect to see, right? Our loops running. Every 2 millisecond we are able to see

**[02:18]** Every 2 millisecond we are able to see

**[02:18]** Every 2 millisecond we are able to see our policy output. We read data. We send

**[02:20]** our policy output. We read data. We send

**[02:20]** our policy output. We read data. We send it out. Standard. But as soon as we

**[02:23]** it out. Standard. But as soon as we

**[02:23]** it out. Standard. But as soon as we deploy it on the robot, this is what

**[02:25]** deploy it on the robot, this is what

**[02:25]** deploy it on the robot, this is what happens. There's a gap. Every two

**[02:28]** happens. There's a gap. Every two

**[02:28]** happens. There's a gap. Every two milliseconds, there's a gap. Wait,

**[02:30]** milliseconds, there's a gap. Wait,

**[02:30]** milliseconds, there's a gap. Wait, what's going on? Well, let's look at the

**[02:32]** what's going on? Well, let's look at the

**[02:32]** what's going on? Well, let's look at the loop again. So, at the edge of the loop,

**[02:35]** loop again. So, at the edge of the loop,

**[02:35]** loop again. So, at the edge of the loop, we have question marks. We see that

**[02:36]** we have question marks. We see that

**[02:36]** we have question marks. We see that we're transmitting and receiving CAN

**[02:38]** we're transmitting and receiving CAN

**[02:38]** we're transmitting and receiving CAN data. So, let's look at the canvas.

**[02:40]** data. So, let's look at the canvas.

**[02:40]** data. So, let's look at the canvas. Maybe we'll find some hints there.

**[02:42]** Maybe we'll find some hints there.

**[02:42]** Maybe we'll find some hints there. Okay. So, let's say we have 100 bits per

**[02:45]** Okay. So, let's say we have 100 bits per

**[02:45]** Okay. So, let's say we have 100 bits per message and we have about 10 messages.

**[02:47]** message and we have about 10 messages.

**[02:47]** message and we have about 10 messages. Five to be sent out, five to be

**[02:49]** Five to be sent out, five to be

**[02:49]** Five to be sent out, five to be received. That gives us a total of

**[02:51]** received. That gives us a total of

**[02:51]** received. That gives us a total of thousand bits. And for a canvas that's

**[02:53]** thousand bits. And for a canvas that's

**[02:53]** thousand bits. And for a canvas that's operating at 1 megabit per second,

**[02:55]** operating at 1 megabit per second,

**[02:55]** operating at 1 megabit per second, that's about 0.1 milliseconds per

**[02:57]** that's about 0.1 milliseconds per

**[02:57]** that's about 0.1 milliseconds per message or 1 milliseconds for 10

**[02:59]** message or 1 milliseconds for 10

**[02:59]** message or 1 milliseconds for 10 message. You can see like how even a


### [03:00 - 04:00]

**[03:01]** message. You can see like how even a

**[03:01]** message. You can see like how even a small number of messages are saturating

**[03:03]** small number of messages are saturating

**[03:03]** small number of messages are saturating the canvas to the point that the loop

**[03:06]** the canvas to the point that the loop

**[03:06]** the canvas to the point that the loop time the how much our system takes to

**[03:07]** time the how much our system takes to

**[03:07]** time the how much our system takes to run is on the same order as the

**[03:09]** run is on the same order as the

**[03:09]** run is on the same order as the transmission time. And this explains the

**[03:11]** transmission time. And this explains the

**[03:12]** transmission time. And this explains the 1 millcond gap. So great, but then what

**[03:14]** 1 millcond gap. So great, but then what

**[03:14]** 1 millcond gap. So great, but then what to do about it? It's like it's almost

**[03:16]** to do about it? It's like it's almost

**[03:16]** to do about it? It's like it's almost unavoidable, right? we cannot go around

**[03:18]** unavoidable, right? we cannot go around

**[03:18]** unavoidable, right? we cannot go around this 1 millcond gap. Well, that's

**[03:21]** this 1 millcond gap. Well, that's

**[03:21]** this 1 millcond gap. Well, that's solution number one. We just accept the

**[03:23]** solution number one. We just accept the

**[03:23]** solution number one. We just accept the delay. Hopefully, it's 3 millonds and

**[03:25]** delay. Hopefully, it's 3 millonds and

**[03:25]** delay. Hopefully, it's 3 millonds and that's not too bad. But again, a system

**[03:27]** that's not too bad. But again, a system

**[03:27]** that's not too bad. But again, a system would not be high performance if we let

**[03:29]** would not be high performance if we let

**[03:29]** would not be high performance if we let that stop us. So, we'll multi thread and

**[03:31]** that stop us. So, we'll multi thread and

**[03:32]** that stop us. So, we'll multi thread and we'll pipeline. We'll try to figure out

**[03:34]** we'll pipeline. We'll try to figure out

**[03:34]** we'll pipeline. We'll try to figure out how we can work around that 1

**[03:35]** how we can work around that 1

**[03:35]** how we can work around that 1 milliseconds and see how we can sort of

**[03:37]** milliseconds and see how we can sort of

**[03:38]** milliseconds and see how we can sort of organize our tasks differently to still

**[03:40]** organize our tasks differently to still

**[03:40]** organize our tasks differently to still get that 2 millisecond loop time. So

**[03:42]** get that 2 millisecond loop time. So

**[03:42]** get that 2 millisecond loop time. So here we'll take a take a moment to pause

**[03:43]** here we'll take a take a moment to pause

**[03:43]** here we'll take a take a moment to pause and see that you know the loop it has

**[03:45]** and see that you know the loop it has

**[03:45]** and see that you know the loop it has multiple components broken down into

**[03:47]** multiple components broken down into

**[03:47]** multiple components broken down into three now TX px RX and the policy and

**[03:50]** three now TX px RX and the policy and

**[03:50]** three now TX px RX and the policy and we're running the communication in

**[03:51]** we're running the communication in

**[03:51]** we're running the communication in different thread and the policy in a

**[03:53]** different thread and the policy in a

**[03:53]** different thread and the policy in a different thread and now we'll see how

**[03:54]** different thread and now we'll see how

**[03:54]** different thread and now we'll see how we'll take the simple building block and

**[03:56]** we'll take the simple building block and

**[03:56]** we'll take the simple building block and stagger it so that we can actually

**[03:58]** stagger it so that we can actually

**[03:58]** stagger it so that we can actually achieve faster loop times and this is


### [04:00 - 05:00]

**[04:01]** achieve faster loop times and this is

**[04:01]** achieve faster loop times and this is it. So what we do we seed the policy the

**[04:04]** it. So what we do we seed the policy the

**[04:04]** it. So what we do we seed the policy the first time we get some data we feed it

**[04:06]** first time we get some data we feed it

**[04:06]** first time we get some data we feed it to the policy but before we conclude the

**[04:08]** to the policy but before we conclude the

**[04:08]** to the policy but before we conclude the policy we start receiving the next set

**[04:10]** policy we start receiving the next set

**[04:10]** policy we start receiving the next set of data and that's for the next

**[04:12]** of data and that's for the next

**[04:12]** of data and that's for the next iteration when the next iteration starts

**[04:14]** iteration when the next iteration starts

**[04:14]** iteration when the next iteration starts we transmit the data from the last

**[04:16]** we transmit the data from the last

**[04:16]** we transmit the data from the last policy and we continue the this

**[04:19]** policy and we continue the this

**[04:19]** policy and we continue the this iteration of this policy essentially we

**[04:21]** iteration of this policy essentially we

**[04:22]** iteration of this policy essentially we have parallelized our RX and TX but

**[04:24]** have parallelized our RX and TX but

**[04:24]** have parallelized our RX and TX but we're still receiving data for the same

**[04:26]** we're still receiving data for the same

**[04:26]** we're still receiving data for the same policy at the same cadence so this is

**[04:28]** policy at the same cadence so this is

**[04:28]** policy at the same cadence so this is great we might have solved our problems

**[04:32]** great we might have solved our problems

**[04:32]** great we might have solved our problems Let's move on. So, we deploy the system

**[04:34]** Let's move on. So, we deploy the system

**[04:34]** Let's move on. So, we deploy the system on the robot and now we see new

**[04:37]** on the robot and now we see new

**[04:37]** on the robot and now we see new problems. Our system is stuttering. Our

**[04:39]** problems. Our system is stuttering. Our

**[04:39]** problems. Our system is stuttering. Our actuators are making sounds like

**[04:41]** actuators are making sounds like

**[04:41]** actuators are making sounds like catching up or like we're seeing weird

**[04:43]** catching up or like we're seeing weird

**[04:43]** catching up or like we're seeing weird motions on the actuator. This has to be

**[04:45]** motions on the actuator. This has to be

**[04:45]** motions on the actuator. This has to be policy. There's no way this can be

**[04:47]** policy. There's no way this can be

**[04:47]** policy. There's no way this can be software. Well, let's investigate more.

**[04:50]** software. Well, let's investigate more.

**[04:50]** software. Well, let's investigate more. Let's get some more data from the

**[04:51]** Let's get some more data from the

**[04:51]** Let's get some more data from the canvas.

**[04:52]** canvas.

**[04:52]** canvas. So, again, like here we have our canvas

**[04:55]** So, again, like here we have our canvas

**[04:55]** So, again, like here we have our canvas again and we see our CPU, GPU, all our

**[04:58]** again and we see our CPU, GPU, all our

**[04:58]** again and we see our CPU, GPU, all our accelerators. And what we'll try to do


### [05:00 - 06:00]

**[05:00]** accelerators. And what we'll try to do

**[05:00]** accelerators. And what we'll try to do is get an external transceiver. These

**[05:02]** is get an external transceiver. These

**[05:02]** is get an external transceiver. These are again very cheap, very open source

**[05:04]** are again very cheap, very open source

**[05:04]** are again very cheap, very open source products that you can get anywhere. And

**[05:06]** products that you can get anywhere. And

**[05:06]** products that you can get anywhere. And we connect it to the canvas and we get

**[05:08]** we connect it to the canvas and we get

**[05:08]** we connect it to the canvas and we get data off the canvas. We take this data,

**[05:10]** data off the canvas. We take this data,

**[05:10]** data off the canvas. We take this data, we feed it to another host computer,

**[05:12]** we feed it to another host computer,

**[05:12]** we feed it to another host computer, let's say a laptop. And on there we can

**[05:14]** let's say a laptop. And on there we can

**[05:14]** let's say a laptop. And on there we can run utilities like can dump which will

**[05:16]** run utilities like can dump which will

**[05:16]** run utilities like can dump which will actually give you a timestamp data of

**[05:18]** actually give you a timestamp data of

**[05:18]** actually give you a timestamp data of what message was seen at what time. So

**[05:20]** what message was seen at what time. So

**[05:20]** what message was seen at what time. So once we get this raw data off the bus,

**[05:23]** once we get this raw data off the bus,

**[05:23]** once we get this raw data off the bus, we can start plotting it. And this is

**[05:25]** we can start plotting it. And this is

**[05:25]** we can start plotting it. And this is what we should expect that every 2

**[05:27]** what we should expect that every 2

**[05:27]** what we should expect that every 2 milliseconds we have a message on the

**[05:29]** milliseconds we have a message on the

**[05:29]** milliseconds we have a message on the bus that is being sent out right should

**[05:32]** bus that is being sent out right should

**[05:32]** bus that is being sent out right should be very nicely spaced and it should

**[05:34]** be very nicely spaced and it should

**[05:34]** be very nicely spaced and it should reach the actuators in time and this is

**[05:36]** reach the actuators in time and this is

**[05:36]** reach the actuators in time and this is if they see this on the bus we're really

**[05:38]** if they see this on the bus we're really

**[05:38]** if they see this on the bus we're really happy. Now what happens a lot of the

**[05:40]** happy. Now what happens a lot of the

**[05:40]** happy. Now what happens a lot of the times in systems is you'll not see this

**[05:42]** times in systems is you'll not see this

**[05:42]** times in systems is you'll not see this you'll see something like this here

**[05:45]** you'll see something like this here

**[05:45]** you'll see something like this here we'll see like between message number

**[05:46]** we'll see like between message number

**[05:46]** we'll see like between message number three and four there's almost no gap.

**[05:49]** three and four there's almost no gap.

**[05:49]** three and four there's almost no gap. What happened there? And between two and

**[05:51]** What happened there? And between two and

**[05:51]** What happened there? And between two and three there's four milliseconds of gap.

**[05:54]** three there's four milliseconds of gap.

**[05:54]** three there's four milliseconds of gap. It's almost like message number three

**[05:55]** It's almost like message number three

**[05:55]** It's almost like message number three was just late and four was on time and

**[05:58]** was just late and four was on time and

**[05:58]** was just late and four was on time and because of that we had this weird weird


### [06:00 - 07:00]

**[06:01]** because of that we had this weird weird

**[06:01]** because of that we had this weird weird jitter where the actuator would try to

**[06:03]** jitter where the actuator would try to

**[06:03]** jitter where the actuator would try to catch up or have try to command like try

**[06:05]** catch up or have try to command like try

**[06:05]** catch up or have try to command like try to follow two commands at the same time.

**[06:08]** to follow two commands at the same time.

**[06:08]** to follow two commands at the same time. Okay, same thing happened with seven and

**[06:09]** Okay, same thing happened with seven and

**[06:10]** Okay, same thing happened with seven and eight. So let's take a deeper look but

**[06:12]** eight. So let's take a deeper look but

**[06:12]** eight. So let's take a deeper look but first let's try plot this differently.

**[06:14]** first let's try plot this differently.

**[06:14]** first let's try plot this differently. So there's this plot called the cycle

**[06:16]** So there's this plot called the cycle

**[06:16]** So there's this plot called the cycle time plot and where what we plot here is

**[06:18]** time plot and where what we plot here is

**[06:18]** time plot and where what we plot here is the time since last message. time since

**[06:21]** the time since last message. time since

**[06:21]** the time since last message. time since last message is just a way to say like

**[06:24]** last message is just a way to say like

**[06:24]** last message is just a way to say like hey last message came in at 2

**[06:26]** hey last message came in at 2

**[06:26]** hey last message came in at 2 milliseconds interval this one should

**[06:27]** milliseconds interval this one should

**[06:27]** milliseconds interval this one should also come at 2 milliseconds so we should

**[06:29]** also come at 2 milliseconds so we should

**[06:29]** also come at 2 milliseconds so we should see a straight line around the 2

**[06:30]** see a straight line around the 2

**[06:30]** see a straight line around the 2 millisecond mark but here we see some

**[06:33]** millisecond mark but here we see some

**[06:33]** millisecond mark but here we see some messages jump at 4 milliseconds and the

**[06:35]** messages jump at 4 milliseconds and the

**[06:35]** messages jump at 4 milliseconds and the one after that comes to zero this is

**[06:38]** one after that comes to zero this is

**[06:38]** one after that comes to zero this is expected because if a message is delayed

**[06:40]** expected because if a message is delayed

**[06:40]** expected because if a message is delayed the cycle time for that would be late

**[06:42]** the cycle time for that would be late

**[06:42]** the cycle time for that would be late but then then for the next one it would

**[06:44]** but then then for the next one it would

**[06:44]** but then then for the next one it would be much closer to zero because that one

**[06:46]** be much closer to zero because that one

**[06:46]** be much closer to zero because that one was not late and the difference between

**[06:48]** was not late and the difference between

**[06:48]** was not late and the difference between the last message and the current one is

**[06:49]** the last message and the current one is

**[06:49]** the last message and the current one is basically nothing. Okay, so now we

**[06:52]** basically nothing. Okay, so now we

**[06:52]** basically nothing. Okay, so now we characterize the system. We know what's

**[06:54]** characterize the system. We know what's

**[06:54]** characterize the system. We know what's going on and we can start solving it.

**[06:57]** going on and we can start solving it.

**[06:57]** going on and we can start solving it. But this is what's going on with the TX

**[06:59]** But this is what's going on with the TX

**[06:59]** But this is what's going on with the TX side. So let's see. So we miss sending


### [07:00 - 08:00]

**[07:02]** side. So let's see. So we miss sending

**[07:02]** side. So let's see. So we miss sending the data and cued it. Why would that

**[07:04]** the data and cued it. Why would that

**[07:04]** the data and cued it. Why would that happen? Well, policies are not very real

**[07:07]** happen? Well, policies are not very real

**[07:07]** happen? Well, policies are not very real time. At times they can take longer,

**[07:09]** time. At times they can take longer,

**[07:09]** time. At times they can take longer, times they can take shorter. And what

**[07:11]** times they can take shorter. And what

**[07:11]** times they can take shorter. And what happens if a policy takes longer? Well,

**[07:13]** happens if a policy takes longer? Well,

**[07:13]** happens if a policy takes longer? Well, you miss the time when you're supposed

**[07:14]** you miss the time when you're supposed

**[07:14]** you miss the time when you're supposed to send it out. So all you can do is

**[07:17]** to send it out. So all you can do is

**[07:17]** to send it out. So all you can do is just cue it somewhere. you can store it,

**[07:18]** just cue it somewhere. you can store it,

**[07:18]** just cue it somewhere. you can store it, but that cannot be sent out anymore. And

**[07:21]** but that cannot be sent out anymore. And

**[07:21]** but that cannot be sent out anymore. And when the next iteration comes around,

**[07:23]** when the next iteration comes around,

**[07:23]** when the next iteration comes around, that's when you send both the last

**[07:25]** that's when you send both the last

**[07:25]** that's when you send both the last message and the current message. So

**[07:27]** message and the current message. So

**[07:27]** message and the current message. So you'll see two messages just go on the

**[07:28]** you'll see two messages just go on the

**[07:28]** you'll see two messages just go on the bus at the same time. And this can also

**[07:31]** bus at the same time. And this can also

**[07:31]** bus at the same time. And this can also happen if our TX and RX thread start

**[07:33]** happen if our TX and RX thread start

**[07:33]** happen if our TX and RX thread start desynchronizing. But this is one of the

**[07:35]** desynchronizing. But this is one of the

**[07:35]** desynchronizing. But this is one of the issues that is very commonly seen with

**[07:36]** issues that is very commonly seen with

**[07:36]** issues that is very commonly seen with like a multi-threaded system. And it's

**[07:38]** like a multi-threaded system. And it's

**[07:38]** like a multi-threaded system. And it's very important to have uh

**[07:39]** very important to have uh

**[07:39]** very important to have uh synchronization in the systems. But

**[07:41]** synchronization in the systems. But

**[07:41]** synchronization in the systems. But let's say we do synchronize it and we

**[07:44]** let's say we do synchronize it and we

**[07:44]** let's say we do synchronize it and we are able to fix our TX side. Well, we

**[07:47]** are able to fix our TX side. Well, we

**[07:47]** are able to fix our TX side. Well, we see some improvement. We don't see that

**[07:50]** see some improvement. We don't see that

**[07:50]** see some improvement. We don't see that like everything is solved. We see some

**[07:51]** like everything is solved. We see some

**[07:52]** like everything is solved. We see some improvement. Okay. But now this has to

**[07:54]** improvement. Okay. But now this has to

**[07:54]** improvement. Okay. But now this has to be policy. Our graphs are looking fine.

**[07:56]** be policy. Our graphs are looking fine.

**[07:56]** be policy. Our graphs are looking fine. Everything is on the bus is fine. This

**[07:58]** Everything is on the bus is fine. This

**[07:58]** Everything is on the bus is fine. This has to be policy. There's no way the

**[07:59]** has to be policy. There's no way the

**[07:59]** has to be policy. There's no way the systems. Well, there's one last one last


### [08:00 - 09:00]

**[08:01]** systems. Well, there's one last one last

**[08:01]** systems. Well, there's one last one last issue that we have to check and that is

**[08:05]** issue that we have to check and that is

**[08:05]** issue that we have to check and that is what happens if we desynchronize in the

**[08:06]** what happens if we desynchronize in the

**[08:06]** what happens if we desynchronize in the RX side. What happens if our thread is

**[08:09]** RX side. What happens if our thread is

**[08:09]** RX side. What happens if our thread is delayed? Well, now our policy will not

**[08:11]** delayed? Well, now our policy will not

**[08:11]** delayed? Well, now our policy will not get the new data and it'll work with the

**[08:13]** get the new data and it'll work with the

**[08:13]** get the new data and it'll work with the last data and because of that the output

**[08:16]** last data and because of that the output

**[08:16]** last data and because of that the output will also be based on the last data and

**[08:18]** will also be based on the last data and

**[08:18]** will also be based on the last data and so in policy number two or iteration

**[08:20]** so in policy number two or iteration

**[08:20]** so in policy number two or iteration number two we'll actually have an old

**[08:22]** number two we'll actually have an old

**[08:22]** number two we'll actually have an old command still like which is relatively

**[08:24]** command still like which is relatively

**[08:24]** command still like which is relatively older and in policy number three we'll

**[08:26]** older and in policy number three we'll

**[08:26]** older and in policy number three we'll directly jump we'll skip one of the data

**[08:28]** directly jump we'll skip one of the data

**[08:28]** directly jump we'll skip one of the data processings and because of that we'll

**[08:31]** processings and because of that we'll

**[08:31]** processings and because of that we'll see a sort of skip a catching up

**[08:32]** see a sort of skip a catching up

**[08:32]** see a sort of skip a catching up behavior on the motors which will sound

**[08:34]** behavior on the motors which will sound

**[08:34]** behavior on the motors which will sound like almost like a jitter.

**[08:36]** like almost like a jitter.

**[08:36]** like almost like a jitter. Okay, so how do we resolve these two

**[08:38]** Okay, so how do we resolve these two

**[08:38]** Okay, so how do we resolve these two things? Well, there are synchronization

**[08:40]** things? Well, there are synchronization

**[08:40]** things? Well, there are synchronization primitives looking you can wait

**[08:42]** primitives looking you can wait

**[08:42]** primitives looking you can wait conditional variables semifers. These

**[08:44]** conditional variables semifers. These

**[08:44]** conditional variables semifers. These are like very low-level system things

**[08:46]** are like very low-level system things

**[08:46]** are like very low-level system things that are widely used in robotics and

**[08:48]** that are widely used in robotics and

**[08:48]** that are widely used in robotics and should be used as well for this toy

**[08:49]** should be used as well for this toy

**[08:49]** should be used as well for this toy system. But again, if these are not

**[08:52]** system. But again, if these are not

**[08:52]** system. But again, if these are not available, which is sometimes the case

**[08:54]** available, which is sometimes the case

**[08:54]** available, which is sometimes the case like we're not working with Linux based

**[08:55]** like we're not working with Linux based

**[08:55]** like we're not working with Linux based system, we'll work with like a real-time

**[08:57]** system, we'll work with like a real-time

**[08:57]** system, we'll work with like a real-time OS or like a microcontroller where we

**[08:59]** OS or like a microcontroller where we

**[08:59]** OS or like a microcontroller where we may not have all these offers. We can


### [09:00 - 10:00]

**[09:01]** may not have all these offers. We can

**[09:01]** may not have all these offers. We can just add padding just have some cushion,

**[09:04]** just add padding just have some cushion,

**[09:04]** just add padding just have some cushion, right? like have some cushion so that if

**[09:06]** right? like have some cushion so that if

**[09:06]** right? like have some cushion so that if some desynchronization happens you still

**[09:08]** some desynchronization happens you still

**[09:08]** some desynchronization happens you still have the same RX going into the right

**[09:09]** have the same RX going into the right

**[09:10]** have the same RX going into the right policy and coming out the other way in

**[09:12]** policy and coming out the other way in

**[09:12]** policy and coming out the other way in like in a timely manner we don't miss

**[09:14]** like in a timely manner we don't miss

**[09:14]** like in a timely manner we don't miss messages okay perfect so this this this

**[09:18]** messages okay perfect so this this this

**[09:18]** messages okay perfect so this this this makes a system fairly robust fairly high

**[09:19]** makes a system fairly robust fairly high

**[09:19]** makes a system fairly robust fairly high performant but there are few other

**[09:21]** performant but there are few other

**[09:21]** performant but there are few other relative problems which will happen with

**[09:23]** relative problems which will happen with

**[09:23]** relative problems which will happen with a system like this which we should also

**[09:25]** a system like this which we should also

**[09:25]** a system like this which we should also talk about so let's talk about logging

**[09:28]** talk about so let's talk about logging

**[09:28]** talk about so let's talk about logging logging is benign right we just log that

**[09:30]** logging is benign right we just log that

**[09:30]** logging is benign right we just log that hey the message is coming in we want to

**[09:32]** hey the message is coming in we want to

**[09:32]** hey the message is coming in we want to just log that this is the data that we

**[09:34]** just log that this is the data that we

**[09:34]** just log that this is the data that we got this is the output it's fine right

**[09:36]** got this is the output it's fine right

**[09:36]** got this is the output it's fine right well if we log too much at some point we

**[09:38]** well if we log too much at some point we

**[09:38]** well if we log too much at some point we have to send those logs to disk and that

**[09:41]** have to send those logs to disk and that

**[09:41]** have to send those logs to disk and that is very costly imagine what happens if

**[09:43]** is very costly imagine what happens if

**[09:43]** is very costly imagine what happens if your main control loop starts logging

**[09:45]** your main control loop starts logging

**[09:45]** your main control loop starts logging and decides just one day that hey I'm

**[09:47]** and decides just one day that hey I'm

**[09:47]** and decides just one day that hey I'm done I'll just start putting this on the

**[09:49]** done I'll just start putting this on the

**[09:49]** done I'll just start putting this on the on the hard disk well your robot would

**[09:51]** on the hard disk well your robot would

**[09:51]** on the hard disk well your robot would stay frozen for 30 milliseconds as we

**[09:52]** stay frozen for 30 milliseconds as we

**[09:52]** stay frozen for 30 milliseconds as we saw on a Raspberry Pi with an SD card so

**[09:55]** saw on a Raspberry Pi with an SD card so

**[09:55]** saw on a Raspberry Pi with an SD card so well that's bad how do we fix that well

**[09:58]** well that's bad how do we fix that well

**[09:58]** well that's bad how do we fix that well we just throw more CPU at it we just add


### [10:00 - 11:00]

**[10:00]** we just throw more CPU at it we just add

**[10:00]** we just throw more CPU at it we just add another CPU and now all our logging is

**[10:02]** another CPU and now all our logging is

**[10:02]** another CPU and now all our logging is handled by that third CPU

**[10:04]** handled by that third CPU

**[10:04]** handled by that third CPU Cool. Okay. So now we have like we're

**[10:06]** Cool. Okay. So now we have like we're

**[10:06]** Cool. Okay. So now we have like we're seeing how multi-threaded is slowly

**[10:08]** seeing how multi-threaded is slowly

**[10:08]** seeing how multi-threaded is slowly getting baked into the system. How the

**[10:09]** getting baked into the system. How the

**[10:09]** getting baked into the system. How the robot is operating in a real-time

**[10:11]** robot is operating in a real-time

**[10:11]** robot is operating in a real-time deadline guarantee and how we are able

**[10:13]** deadline guarantee and how we are able

**[10:13]** deadline guarantee and how we are able to like avoid the pitfalls. Perfect.

**[10:16]** to like avoid the pitfalls. Perfect.

**[10:16]** to like avoid the pitfalls. Perfect. Let's talk about something a little more

**[10:17]** Let's talk about something a little more

**[10:17]** Let's talk about something a little more low-level again like microcontrollers.

**[10:19]** low-level again like microcontrollers.

**[10:20]** low-level again like microcontrollers. Microcontrollers are fairly simple and

**[10:22]** Microcontrollers are fairly simple and

**[10:22]** Microcontrollers are fairly simple and their logging doesn't actually go

**[10:23]** their logging doesn't actually go

**[10:23]** their logging doesn't actually go through a whole disk and file system

**[10:25]** through a whole disk and file system

**[10:25]** through a whole disk and file system way. They just log to some other

**[10:27]** way. They just log to some other

**[10:27]** way. They just log to some other peripheral that takes time. In fact, for

**[10:30]** peripheral that takes time. In fact, for

**[10:30]** peripheral that takes time. In fact, for you art, it can be on the order of

**[10:31]** you art, it can be on the order of

**[10:32]** you art, it can be on the order of millisecond depending on how much we're

**[10:33]** millisecond depending on how much we're

**[10:33]** millisecond depending on how much we're logging. So, here's an interesting

**[10:35]** logging. So, here's an interesting

**[10:35]** logging. So, here's an interesting problem. Let's say we drop a packet and

**[10:38]** problem. Let's say we drop a packet and

**[10:38]** problem. Let's say we drop a packet and we log that hey, we dropped the packet.

**[10:41]** we log that hey, we dropped the packet.

**[10:41]** we log that hey, we dropped the packet. Well, that log itself would take enough

**[10:43]** Well, that log itself would take enough

**[10:43]** Well, that log itself would take enough time that will drop the next packet and

**[10:45]** time that will drop the next packet and

**[10:45]** time that will drop the next packet and then you will keep drop because you drop

**[10:46]** then you will keep drop because you drop

**[10:46]** then you will keep drop because you drop the next packet, you log again. And so,

**[10:48]** the next packet, you log again. And so,

**[10:48]** the next packet, you log again. And so, basically, you just keep logging and you

**[10:50]** basically, you just keep logging and you

**[10:50]** basically, you just keep logging and you see a complete blackout on the canvas

**[10:53]** see a complete blackout on the canvas

**[10:53]** see a complete blackout on the canvas and it's very hard to debug like why am

**[10:55]** and it's very hard to debug like why am

**[10:55]** and it's very hard to debug like why am I getting logs and seeing packet drops

**[10:56]** I getting logs and seeing packet drops

**[10:56]** I getting logs and seeing packet drops but no data. So these are mysterious

**[10:58]** but no data. So these are mysterious

**[10:58]** but no data. So these are mysterious things that and in my experience like


### [11:00 - 12:00]

**[11:01]** things that and in my experience like

**[11:01]** things that and in my experience like it's really good to like know about the

**[11:02]** it's really good to like know about the

**[11:02]** it's really good to like know about the pitfalls beforehand before we dive in

**[11:04]** pitfalls beforehand before we dive in

**[11:04]** pitfalls beforehand before we dive in the system and really figure out that

**[11:06]** the system and really figure out that

**[11:06]** the system and really figure out that hey this can also be a problem just a

**[11:07]** hey this can also be a problem just a

**[11:08]** hey this can also be a problem just a log statement.

**[11:10]** log statement.

**[11:10]** log statement. Finally there's also priority inversion.

**[11:12]** Finally there's also priority inversion.

**[11:12]** Finally there's also priority inversion. So in the kernel in the Linux kernel

**[11:14]** So in the kernel in the Linux kernel

**[11:14]** So in the kernel in the Linux kernel there are ways in which data is received

**[11:16]** there are ways in which data is received

**[11:16]** there are ways in which data is received by the user process. It's not direct

**[11:18]** by the user process. It's not direct

**[11:18]** by the user process. It's not direct like it takes a while between the

**[11:19]** like it takes a while between the

**[11:19]** like it takes a while between the interrupt the kernel process handling

**[11:21]** interrupt the kernel process handling

**[11:21]** interrupt the kernel process handling and then it goes to the user process. In

**[11:23]** and then it goes to the user process. In

**[11:23]** and then it goes to the user process. In robotics, we tend to just boost the

**[11:25]** robotics, we tend to just boost the

**[11:25]** robotics, we tend to just boost the priority of all our processes so high

**[11:27]** priority of all our processes so high

**[11:27]** priority of all our processes so high that we start just blocking the kernel

**[11:30]** that we start just blocking the kernel

**[11:30]** that we start just blocking the kernel almost. Like if the kernel doesn't run,

**[11:32]** almost. Like if the kernel doesn't run,

**[11:32]** almost. Like if the kernel doesn't run, we won't get the data. But we're trying

**[11:34]** we won't get the data. But we're trying

**[11:34]** we won't get the data. But we're trying to get the data and we're blocking the

**[11:35]** to get the data and we're blocking the

**[11:35]** to get the data and we're blocking the very thing that will give us the data.

**[11:38]** very thing that will give us the data.

**[11:38]** very thing that will give us the data. Well, this is inversion in action. And

**[11:39]** Well, this is inversion in action. And

**[11:40]** Well, this is inversion in action. And it will see your system again drop out

**[11:41]** it will see your system again drop out

**[11:41]** it will see your system again drop out for like seconds almost at a time. So

**[11:44]** for like seconds almost at a time. So

**[11:44]** for like seconds almost at a time. So again, this is something we we fix by

**[11:46]** again, this is something we we fix by

**[11:46]** again, this is something we we fix by just making sure we know the parts of

**[11:47]** just making sure we know the parts of

**[11:48]** just making sure we know the parts of the pipeline. we fix the right

**[11:49]** the pipeline. we fix the right

**[11:49]** the pipeline. we fix the right priorities and we make sure that our

**[11:51]** priorities and we make sure that our

**[11:51]** priorities and we make sure that our whole system as a whole like it works

**[11:52]** whole system as a whole like it works

**[11:52]** whole system as a whole like it works together well. So this is how like

**[11:55]** together well. So this is how like

**[11:55]** together well. So this is how like software and robotics have to work

**[11:56]** software and robotics have to work

**[11:56]** software and robotics have to work together. We have to talk about hardware

**[11:58]** together. We have to talk about hardware

**[11:58]** together. We have to talk about hardware the various profiling the various


### [12:00 - 13:00]

**[12:00]** the various profiling the various

**[12:00]** the various profiling the various priority stuff and actually just take a

**[12:03]** priority stuff and actually just take a

**[12:03]** priority stuff and actually just take a recap from the top. So we went over

**[12:05]** recap from the top. So we went over

**[12:05]** recap from the top. So we went over pipeline. We saw how to reduce cycle

**[12:07]** pipeline. We saw how to reduce cycle

**[12:07]** pipeline. We saw how to reduce cycle time beat how the communication delays.

**[12:10]** time beat how the communication delays.

**[12:10]** time beat how the communication delays. We saw how synchronization can actually

**[12:12]** We saw how synchronization can actually

**[12:12]** We saw how synchronization can actually cause some unexpected jitter which are

**[12:14]** cause some unexpected jitter which are

**[12:14]** cause some unexpected jitter which are hard to diagnose. Could be the policy,

**[12:15]** hard to diagnose. Could be the policy,

**[12:16]** hard to diagnose. Could be the policy, could be the system. So we want to make

**[12:17]** could be the system. So we want to make

**[12:17]** could be the system. So we want to make sure that that doesn't happen. Logging

**[12:19]** sure that that doesn't happen. Logging

**[12:19]** sure that that doesn't happen. Logging strategies so that we don't block the

**[12:21]** strategies so that we don't block the

**[12:21]** strategies so that we don't block the system while we're trying to tell the

**[12:22]** system while we're trying to tell the

**[12:22]** system while we're trying to tell the user that hey this is happening. And

**[12:24]** user that hey this is happening. And

**[12:24]** user that hey this is happening. And finally priority inversion to avoid

**[12:26]** finally priority inversion to avoid

**[12:26]** finally priority inversion to avoid starvation. And that's how we start

**[12:28]** starvation. And that's how we start

**[12:28]** starvation. And that's how we start designing high performance robotic

**[12:29]** designing high performance robotic

**[12:29]** designing high performance robotic systems at least on a very basic level.

**[12:32]** systems at least on a very basic level.

**[12:32]** systems at least on a very basic level. And that's my talk for today. And thank

**[12:33]** And that's my talk for today. And thank

**[12:33]** And that's my talk for today. And thank you so much for being here listening.

**[12:37]** you so much for being here listening.

**[12:37]** you so much for being here listening. [Music]


