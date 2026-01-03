# Serving Voice AI at $1_hr- Open-source, LoRAs, Latency, Load Balancing - Neil Dwyer, Gabber

**Video URL:** https://www.youtube.com/watch?v=rD23-VZZHOo

---

## Full Transcript

### [00:00 - 01:00]

**[00:17]** I'm Neil. That's that's Jack in the in

**[00:17]** I'm Neil. That's that's Jack in the in the front there, but it's just me. Um,

**[00:19]** the front there, but it's just me. Um,

**[00:19]** the front there, but it's just me. Um, so yeah, we're really just going to talk

**[00:20]** so yeah, we're really just going to talk

**[00:20]** so yeah, we're really just going to talk about our experience um ho hosting

**[00:23]** about our experience um ho hosting

**[00:23]** about our experience um ho hosting Orpheus uh inference um for our real

**[00:26]** Orpheus uh inference um for our real

**[00:26]** Orpheus uh inference um for our real real time stack.

**[00:29]** real time stack.

**[00:29]** real time stack. So, I'm Neil um the CTO at a company

**[00:32]** So, I'm Neil um the CTO at a company

**[00:32]** So, I'm Neil um the CTO at a company called Gabber, small startup. Uh but I

**[00:34]** called Gabber, small startup. Uh but I

**[00:34]** called Gabber, small startup. Uh but I spent a lot of my career doing real-time

**[00:36]** spent a lot of my career doing real-time

**[00:36]** spent a lot of my career doing real-time media stuff. So, sending audio and video

**[00:38]** media stuff. So, sending audio and video

**[00:38]** media stuff. So, sending audio and video around the internet. Um started at a

**[00:40]** around the internet. Um started at a

**[00:40]** around the internet. Um started at a company called Bibo. Um was ultimately

**[00:42]** company called Bibo. Um was ultimately

**[00:42]** company called Bibo. Um was ultimately acquired by Amazon. But, uh there I was

**[00:45]** acquired by Amazon. But, uh there I was

**[00:45]** acquired by Amazon. But, uh there I was doing a lot of we did like a game

**[00:46]** doing a lot of we did like a game

**[00:46]** doing a lot of we did like a game streaming app kind of like OBS. Um built

**[00:49]** streaming app kind of like OBS. Um built

**[00:49]** streaming app kind of like OBS. Um built uh a lot of the streaming infrastructure

**[00:51]** uh a lot of the streaming infrastructure

**[00:51]** uh a lot of the streaming infrastructure there. Built a ML pipeline to watch

**[00:54]** there. Built a ML pipeline to watch

**[00:54]** there. Built a ML pipeline to watch people play video games. Um, so they

**[00:55]** people play video games. Um, so they

**[00:55]** people play video games. Um, so they would watch people play Fortnite and put

**[00:57]** would watch people play Fortnite and put

**[00:57]** would watch people play Fortnite and put some cool effects on the screen when

**[00:59]** some cool effects on the screen when

**[00:59]** some cool effects on the screen when when they got a kill or victory or


### [01:00 - 02:00]

**[01:00]** when they got a kill or victory or

**[01:00]** when they got a kill or victory or something. Um, so spent a lot of time in

**[01:02]** something. Um, so spent a lot of time in

**[01:02]** something. Um, so spent a lot of time in like the Gstreamer trenches and with

**[01:05]** like the Gstreamer trenches and with

**[01:05]** like the Gstreamer trenches and with WebRTC and RTMP and all that stuff. Um,

**[01:08]** WebRTC and RTMP and all that stuff. Um,

**[01:08]** WebRTC and RTMP and all that stuff. Um, took a detour, worked at Uber for a

**[01:09]** took a detour, worked at Uber for a

**[01:10]** took a detour, worked at Uber for a couple years. Uh, then left that. Um,

**[01:12]** couple years. Uh, then left that. Um,

**[01:12]** couple years. Uh, then left that. Um, did a multiplayer gaming uh, startup

**[01:15]** did a multiplayer gaming uh, startup

**[01:15]** did a multiplayer gaming uh, startup with my brother Jack here. Um, so doing

**[01:18]** with my brother Jack here. Um, so doing

**[01:18]** with my brother Jack here. Um, so doing basically trying to bring like AAA style

**[01:20]** basically trying to bring like AAA style

**[01:20]** basically trying to bring like AAA style multiplayer to to web games. So a lot of

**[01:22]** multiplayer to to web games. So a lot of

**[01:22]** multiplayer to to web games. So a lot of real and with voice and stuff too. So

**[01:23]** real and with voice and stuff too. So

**[01:23]** real and with voice and stuff too. So there's a lot of real-time media

**[01:26]** there's a lot of real-time media

**[01:26]** there's a lot of real-time media realtime um you know simulation kind of

**[01:28]** realtime um you know simulation kind of

**[01:28]** realtime um you know simulation kind of stuff there. Um and then yeah we uh

**[01:31]** stuff there. Um and then yeah we uh

**[01:31]** stuff there. Um and then yeah we uh didn't do super good job there and uh

**[01:34]** didn't do super good job there and uh

**[01:34]** didn't do super good job there and uh shut shut that company down and um we

**[01:36]** shut shut that company down and um we

**[01:36]** shut shut that company down and um we were using LiveKit. I made a LiveKit SDK

**[01:38]** were using LiveKit. I made a LiveKit SDK

**[01:38]** were using LiveKit. I made a LiveKit SDK and that uh segueed to me working at

**[01:41]** and that uh segueed to me working at

**[01:41]** and that uh segueed to me working at LiveKit. I think a lot of people

**[01:42]** LiveKit. I think a lot of people

**[01:42]** LiveKit. I think a lot of people probably heard of LiveKit in this room.

**[01:43]** probably heard of LiveKit in this room.

**[01:43]** probably heard of LiveKit in this room. Um and yeah the second half of my time

**[01:46]** Um and yeah the second half of my time

**[01:46]** Um and yeah the second half of my time at LiveKit I uh was spent doing the

**[01:48]** at LiveKit I uh was spent doing the

**[01:48]** at LiveKit I uh was spent doing the LiveKit agents platform. So that's like

**[01:50]** LiveKit agents platform. So that's like

**[01:50]** LiveKit agents platform. So that's like the platform that was kind of born out

**[01:52]** the platform that was kind of born out

**[01:52]** the platform that was kind of born out of um LiveKit's involvement with GPT

**[01:54]** of um LiveKit's involvement with GPT

**[01:54]** of um LiveKit's involvement with GPT boys. Um so yeah wrote the first line of

**[01:57]** boys. Um so yeah wrote the first line of

**[01:57]** boys. Um so yeah wrote the first line of code on that and worked on that. Um and

**[01:59]** code on that and worked on that. Um and

**[01:59]** code on that and worked on that. Um and then yeah left LiveKit and did another


### [02:00 - 03:00]

**[02:00]** then yeah left LiveKit and did another

**[02:00]** then yeah left LiveKit and did another startup with my brother um Gabber. Um so

**[02:03]** startup with my brother um Gabber. Um so

**[02:03]** startup with my brother um Gabber. Um so that's what we're doing now. So Gabber

**[02:06]** that's what we're doing now. So Gabber

**[02:06]** that's what we're doing now. So Gabber is real time uh infro for real time

**[02:08]** is real time uh infro for real time

**[02:08]** is real time uh infro for real time basically AI personas. Um so you know we

**[02:11]** basically AI personas. Um so you know we

**[02:11]** basically AI personas. Um so you know we have some core building blocks like

**[02:12]** have some core building blocks like

**[02:12]** have some core building blocks like voice memory um video inputs coming soon

**[02:15]** voice memory um video inputs coming soon

**[02:15]** voice memory um video inputs coming soon tool calling kind of like the usual

**[02:16]** tool calling kind of like the usual

**[02:16]** tool calling kind of like the usual suspects I guess but our focus is really

**[02:19]** suspects I guess but our focus is really

**[02:19]** suspects I guess but our focus is really on the consumer apps um you know we we

**[02:22]** on the consumer apps um you know we we

**[02:22]** on the consumer apps um you know we we see the like the replacing human use

**[02:24]** see the like the replacing human use

**[02:24]** see the like the replacing human use cases pretty often um like the call

**[02:27]** cases pretty often um like the call

**[02:27]** cases pretty often um like the call center use cases customer support AI SDR

**[02:30]** center use cases customer support AI SDR

**[02:30]** center use cases customer support AI SDR that that kind of stuff um but our

**[02:31]** that that kind of stuff um but our

**[02:32]** that that kind of stuff um but our interest is really in the the consumer

**[02:33]** interest is really in the the consumer

**[02:33]** interest is really in the the consumer space we think um these kind of like

**[02:36]** space we think um these kind of like

**[02:36]** space we think um these kind of like real-time synchronous AI experiences are

**[02:38]** real-time synchronous AI experiences are

**[02:38]** real-time synchronous AI experiences are going to be as ubiquous us as as

**[02:40]** going to be as ubiquous us as as

**[02:40]** going to be as ubiquous us as as websites and apps in the next kind of

**[02:42]** websites and apps in the next kind of

**[02:42]** websites and apps in the next kind of like two to five years. So that's our

**[02:43]** like two to five years. So that's our

**[02:43]** like two to five years. So that's our focus and we that's how we try and

**[02:46]** focus and we that's how we try and

**[02:46]** focus and we that's how we try and differentiate in terms of opinion into

**[02:48]** differentiate in terms of opinion into

**[02:48]** differentiate in terms of opinion into our product and our SDKs and APIs and

**[02:49]** our product and our SDKs and APIs and

**[02:49]** our product and our SDKs and APIs and stuff. Um

**[02:52]** stuff. Um

**[02:52]** stuff. Um uh here are some of the use cases we're

**[02:54]** uh here are some of the use cases we're

**[02:54]** uh here are some of the use cases we're seeing. Um these are also kind of like

**[02:55]** seeing. Um these are also kind of like

**[02:55]** seeing. Um these are also kind of like the usual suspects. AI girlfriends was

**[02:57]** the usual suspects. AI girlfriends was

**[02:57]** the usual suspects. AI girlfriends was the first one. um that is like uh I I'll


### [03:00 - 04:00]

**[03:01]** the first one. um that is like uh I I'll

**[03:01]** the first one. um that is like uh I I'll get to why that's the first one I guess

**[03:02]** get to why that's the first one I guess

**[03:02]** get to why that's the first one I guess but um other ones are like AI MPCs uh AI

**[03:06]** but um other ones are like AI MPCs uh AI

**[03:06]** but um other ones are like AI MPCs uh AI therapists AI personal trainers AI toys

**[03:09]** therapists AI personal trainers AI toys

**[03:09]** therapists AI personal trainers AI toys for kids I think that you saw that in a

**[03:10]** for kids I think that you saw that in a

**[03:10]** for kids I think that you saw that in a couple a couple sessions ago these use

**[03:12]** couple a couple sessions ago these use

**[03:12]** couple a couple sessions ago these use cases like we're seeing a lot of

**[03:13]** cases like we're seeing a lot of

**[03:13]** cases like we're seeing a lot of different use case and I saw it at

**[03:14]** different use case and I saw it at

**[03:14]** different use case and I saw it at LiveKit too and it got me really really

**[03:15]** LiveKit too and it got me really really

**[03:15]** LiveKit too and it got me really really excited about about this stuff but um AI

**[03:18]** excited about about this stuff but um AI

**[03:18]** excited about about this stuff but um AI girlfriends was was the first one mainly

**[03:20]** girlfriends was was the first one mainly

**[03:20]** girlfriends was was the first one mainly because um everything's so expensive um

**[03:24]** because um everything's so expensive um

**[03:24]** because um everything's so expensive um uh some some of these voice platforms

**[03:25]** uh some some of these voice platforms

**[03:25]** uh some some of these voice platforms it's you know end to end upwards of $5

**[03:28]** it's you know end to end upwards of $5

**[03:28]** it's you know end to end upwards of $5 an hour. Uh, and that doesn't really

**[03:30]** an hour. Uh, and that doesn't really

**[03:30]** an hour. Uh, and that doesn't really work for like 90% of the consumer

**[03:32]** work for like 90% of the consumer

**[03:32]** work for like 90% of the consumer consumer apps. Um, but AI girlfriends it

**[03:35]** consumer apps. Um, but AI girlfriends it

**[03:35]** consumer apps. Um, but AI girlfriends it works because like the users are paying

**[03:36]** works because like the users are paying

**[03:36]** works because like the users are paying like um it's like usually like a credit

**[03:38]** like um it's like usually like a credit

**[03:38]** like um it's like usually like a credit system like you buy credits and you use

**[03:40]** system like you buy credits and you use

**[03:40]** system like you buy credits and you use the app and uses credit. So they're more

**[03:42]** the app and uses credit. So they're more

**[03:42]** the app and uses credit. So they're more comfortable with that with that kind of

**[03:43]** comfortable with that with that kind of

**[03:44]** comfortable with that with that kind of spend. But most consumer use cases they

**[03:45]** spend. But most consumer use cases they

**[03:45]** spend. But most consumer use cases they need something pretty close to free. Um,

**[03:48]** need something pretty close to free. Um,

**[03:48]** need something pretty close to free. Um, so we knew that uh and at the time we

**[03:50]** so we knew that uh and at the time we

**[03:50]** so we knew that uh and at the time we were not hosting any any voice models.

**[03:52]** were not hosting any any voice models.

**[03:52]** were not hosting any any voice models. We we but we knew we had to uh we knew

**[03:54]** We we but we knew we had to uh we knew

**[03:54]** We we but we knew we had to uh we knew that the only way to really get this to

**[03:56]** that the only way to really get this to

**[03:56]** that the only way to really get this to to execute on our vision of putting

**[03:58]** to execute on our vision of putting

**[03:58]** to execute on our vision of putting these experiences everywhere we had to


### [04:00 - 05:00]

**[04:00]** these experiences everywhere we had to

**[04:00]** these experiences everywhere we had to start bringing more things in house and

**[04:01]** start bringing more things in house and

**[04:02]** start bringing more things in house and running on our own GPUs. Um so at the

**[04:05]** running on our own GPUs. Um so at the

**[04:05]** running on our own GPUs. Um so at the time open source there weren't a lot of

**[04:06]** time open source there weren't a lot of

**[04:06]** time open source there weren't a lot of good open source voice models. Um uh

**[04:09]** good open source voice models. Um uh

**[04:09]** good open source voice models. Um uh there were a lot of good ones for

**[04:10]** there were a lot of good ones for

**[04:10]** there were a lot of good ones for asynchronous uh use cases. So generating

**[04:13]** asynchronous uh use cases. So generating

**[04:13]** asynchronous uh use cases. So generating voice slower than real time. Um but

**[04:15]** voice slower than real time. Um but

**[04:15]** voice slower than real time. Um but there weren't any really good like

**[04:16]** there weren't any really good like

**[04:16]** there weren't any really good like real-time streaming ones until uh

**[04:19]** real-time streaming ones until uh

**[04:19]** real-time streaming ones until uh Orpheus. Uh Orpheus was the first really

**[04:21]** Orpheus. Uh Orpheus was the first really

**[04:21]** Orpheus. Uh Orpheus was the first really good one um that uh was kind of like

**[04:24]** good one um that uh was kind of like

**[04:24]** good one um that uh was kind of like ready to go. So um Orpheus came out and

**[04:26]** ready to go. So um Orpheus came out and

**[04:26]** ready to go. So um Orpheus came out and we're like, "Okay, this is our time to

**[04:27]** we're like, "Okay, this is our time to

**[04:27]** we're like, "Okay, this is our time to shine. Uh we immediately like put it on

**[04:29]** shine. Uh we immediately like put it on

**[04:29]** shine. Uh we immediately like put it on an H100. Um hosted it. Um went viral

**[04:33]** an H100. Um hosted it. Um went viral

**[04:33]** an H100. Um hosted it. Um went viral with Jack's tweet and uh got a ton of

**[04:35]** with Jack's tweet and uh got a ton of

**[04:35]** with Jack's tweet and uh got a ton of top top of funnel." Um and yeah, that

**[04:38]** top top of funnel." Um and yeah, that

**[04:38]** top top of funnel." Um and yeah, that was kind of like the starting point.

**[04:39]** was kind of like the starting point.

**[04:39]** was kind of like the starting point. It's like our our company. There's like

**[04:41]** It's like our our company. There's like

**[04:41]** It's like our our company. There's like before Orpheus and after Orpheus, our

**[04:42]** before Orpheus and after Orpheus, our

**[04:42]** before Orpheus and after Orpheus, our company kind of changed. Um so a little

**[04:45]** company kind of changed. Um so a little

**[04:45]** company kind of changed. Um so a little background on what Orpheus is. Uh it's a

**[04:47]** background on what Orpheus is. Uh it's a

**[04:47]** background on what Orpheus is. Uh it's a voice model, but it it started as a

**[04:49]** voice model, but it it started as a

**[04:49]** voice model, but it it started as a llama three billion. Um it was trained

**[04:52]** llama three billion. Um it was trained

**[04:52]** llama three billion. Um it was trained on uh pre-trained on like a 100,000

**[04:55]** on uh pre-trained on like a 100,000

**[04:55]** on uh pre-trained on like a 100,000 hours of uh voice uh data and text data

**[04:58]** hours of uh voice uh data and text data

**[04:58]** hours of uh voice uh data and text data as well to make sure it kepts its

**[04:59]** as well to make sure it kepts its

**[04:59]** as well to make sure it kepts its understanding of kind of like language.


### [05:00 - 06:00]

**[05:02]** understanding of kind of like language.

**[05:02]** understanding of kind of like language. Uh and and it was trained to output

**[05:04]** Uh and and it was trained to output

**[05:04]** Uh and and it was trained to output audio tokens. They're called snack

**[05:05]** audio tokens. They're called snack

**[05:05]** audio tokens. They're called snack tokens. So that's another open source

**[05:07]** tokens. So that's another open source

**[05:07]** tokens. So that's another open source project, Snack, which is a audio codec.

**[05:10]** project, Snack, which is a audio codec.

**[05:10]** project, Snack, which is a audio codec. Um

**[05:11]** Um

**[05:11]** Um and so it's trained to output the 24 kHz

**[05:13]** and so it's trained to output the 24 kHz

**[05:13]** and so it's trained to output the 24 kHz version of of snack tokens. Um those

**[05:16]** version of of snack tokens. Um those

**[05:16]** version of of snack tokens. Um those snack tokens are then decoded and then

**[05:18]** snack tokens are then decoded and then

**[05:18]** snack tokens are then decoded and then you get audio. You get 24 kilhertz

**[05:20]** you get audio. You get 24 kilhertz

**[05:20]** you get audio. You get 24 kilhertz audio. Um important thing to note here

**[05:22]** audio. Um important thing to note here

**[05:22]** audio. Um important thing to note here is it's about 85 snack tokens for one

**[05:25]** is it's about 85 snack tokens for one

**[05:25]** is it's about 85 snack tokens for one second of audio. So um Orpheus wherever

**[05:28]** second of audio. So um Orpheus wherever

**[05:28]** second of audio. So um Orpheus wherever you're hosting it, it has to it has to

**[05:30]** you're hosting it, it has to it has to

**[05:30]** you're hosting it, it has to it has to be uh a throughput of about 85. I mean

**[05:33]** be uh a throughput of about 85. I mean

**[05:33]** be uh a throughput of about 85. I mean you want like 90 to 100 tokens per

**[05:35]** you want like 90 to 100 tokens per

**[05:35]** you want like 90 to 100 tokens per second to keep up with real time.

**[05:37]** second to keep up with real time.

**[05:37]** second to keep up with real time. Otherwise you get gap gaps obviously in

**[05:39]** Otherwise you get gap gaps obviously in

**[05:39]** Otherwise you get gap gaps obviously in the audio and it sounds bad.

**[05:41]** the audio and it sounds bad.

**[05:41]** the audio and it sounds bad. Um, other things that were important to

**[05:43]** Um, other things that were important to

**[05:43]** Um, other things that were important to us because we're going after the

**[05:44]** us because we're going after the

**[05:44]** us because we're going after the consumer use cases, um, was cloning. Um,

**[05:48]** consumer use cases, um, was cloning. Um,

**[05:48]** consumer use cases, um, was cloning. Um, so our clones seem to be emotive and and

**[05:50]** so our clones seem to be emotive and and

**[05:50]** so our clones seem to be emotive and and high fidelity. Um, and oneshot cloning

**[05:52]** high fidelity. Um, and oneshot cloning

**[05:52]** high fidelity. Um, and oneshot cloning doesn't work that well. Um, that's more

**[05:55]** doesn't work that well. Um, that's more

**[05:55]** doesn't work that well. Um, that's more true for Orpheus because it only had

**[05:57]** true for Orpheus because it only had

**[05:57]** true for Orpheus because it only had 100,000 hours of pre-trained data. Um,

**[05:59]** 100,000 hours of pre-trained data. Um,


### [06:00 - 07:00]

**[06:00]** 100,000 hours of pre-trained data. Um, whereas I think some of the zeroot

**[06:02]** whereas I think some of the zeroot

**[06:02]** whereas I think some of the zeroot emergent behavior comes at at like a

**[06:04]** emergent behavior comes at at like a

**[06:04]** emergent behavior comes at at like a million plus hours. So, and we're

**[06:06]** million plus hours. So, and we're

**[06:06]** million plus hours. So, and we're scrappy. I think you can tell by like

**[06:08]** scrappy. I think you can tell by like

**[06:08]** scrappy. I think you can tell by like our design here. um that were like

**[06:10]** our design here. um that were like

**[06:10]** our design here. um that were like pretty scrappy, right? We weren't going

**[06:11]** pretty scrappy, right? We weren't going

**[06:11]** pretty scrappy, right? We weren't going to fill that gap. So um so we went with

**[06:15]** to fill that gap. So um so we went with

**[06:15]** to fill that gap. So um so we went with low rank fine tunes for our clones. Um

**[06:17]** low rank fine tunes for our clones. Um

**[06:17]** low rank fine tunes for our clones. Um so here's an example. So this is um a

**[06:20]** so here's an example. So this is um a

**[06:20]** so here's an example. So this is um a low rank fine tune. We have some better

**[06:22]** low rank fine tune. We have some better

**[06:22]** low rank fine tune. We have some better ones. This isn't like the best example,

**[06:23]** ones. This isn't like the best example,

**[06:23]** ones. This isn't like the best example, but they're customers. So I didn't want

**[06:24]** but they're customers. So I didn't want

**[06:24]** but they're customers. So I didn't want to put it in the thing here. So we just

**[06:26]** to put it in the thing here. So we just

**[06:26]** to put it in the thing here. So we just clone Jack's voice um like yesterday and

**[06:29]** clone Jack's voice um like yesterday and

**[06:29]** clone Jack's voice um like yesterday and use 16 rank alpha 32 basically all the

**[06:31]** use 16 rank alpha 32 basically all the

**[06:31]** use 16 rank alpha 32 basically all the projections. Um here's the source audio.

**[06:33]** projections. Um here's the source audio.

**[06:33]** projections. Um here's the source audio. Let's see if restart. We forgot to pick

**[06:35]** Let's see if restart. We forgot to pick

**[06:35]** Let's see if restart. We forgot to pick up our child from school. Oh.

**[06:39]** up our child from school. Oh.

**[06:39]** up our child from school. Oh. H the school called me in the middle of

**[06:41]** H the school called me in the middle of

**[06:42]** H the school called me in the middle of a meeting. Oops. Um so that's the

**[06:45]** a meeting. Oops. Um so that's the

**[06:45]** a meeting. Oops. Um so that's the source. Uh and then here's the result of

**[06:47]** source. Uh and then here's the result of

**[06:47]** source. Uh and then here's the result of a of a fine tune. So um let me manage

**[06:51]** a of a fine tune. So um let me manage

**[06:51]** a of a fine tune. So um let me manage expectations here. Um this was this was

**[06:54]** expectations here. Um this was this was

**[06:54]** expectations here. Um this was this was like

**[06:55]** like

**[06:55]** like pretty bad data like 10 10 minutes of

**[06:57]** pretty bad data like 10 10 minutes of

**[06:57]** pretty bad data like 10 10 minutes of data. You really want like 30 minutes.

**[06:59]** data. You really want like 30 minutes.

**[06:59]** data. You really want like 30 minutes. It was so I had to overfitit. So I


### [07:00 - 08:00]

**[07:01]** It was so I had to overfitit. So I

**[07:01]** It was so I had to overfitit. So I trained on like like five epics. Um it's

**[07:04]** trained on like like five epics. Um it's

**[07:04]** trained on like like five epics. Um it's pretty overfit, but you'll see it like

**[07:06]** pretty overfit, but you'll see it like

**[07:06]** pretty overfit, but you'll see it like still sounds okay.

**[07:08]** still sounds okay.

**[07:08]** still sounds okay. Hey,

**[07:09]** Hey,

**[07:09]** Hey, how are you?

**[07:12]** how are you?

**[07:12]** how are you? I'm kind of sick. This is a longer

**[07:14]** I'm kind of sick. This is a longer

**[07:14]** I'm kind of sick. This is a longer generation. Let's see if it sounds okay.

**[07:18]** generation. Let's see if it sounds okay.

**[07:18]** generation. Let's see if it sounds okay. Yeah. So, it's not bad. Um, you know, I

**[07:21]** Yeah. So, it's not bad. Um, you know, I

**[07:21]** Yeah. So, it's not bad. Um, you know, I my whole life or most my I'm the older

**[07:23]** my whole life or most my I'm the older

**[07:23]** my whole life or most my I'm the older brother, so most of my life, so I know

**[07:24]** brother, so most of my life, so I know

**[07:24]** brother, so most of my life, so I know his voice very well. Um, so, so it's

**[07:26]** his voice very well. Um, so, so it's

**[07:26]** his voice very well. Um, so, so it's draw it's jarring to me, but um, cool

**[07:28]** draw it's jarring to me, but um, cool

**[07:28]** draw it's jarring to me, but um, cool cool thing is like, yeah, it's trained

**[07:30]** cool thing is like, yeah, it's trained

**[07:30]** cool thing is like, yeah, it's trained to do these tokens, which is important

**[07:31]** to do these tokens, which is important

**[07:31]** to do these tokens, which is important for consumer. Um, uh, so and it's pretty

**[07:34]** for consumer. Um, uh, so and it's pretty

**[07:34]** for consumer. Um, uh, so and it's pretty emotive. like when it said I'm kind of

**[07:36]** emotive. like when it said I'm kind of

**[07:36]** emotive. like when it said I'm kind of sick, it sounded pretty sad. So, it

**[07:38]** sick, it sounded pretty sad. So, it

**[07:38]** sick, it sounded pretty sad. So, it picks up on the language cues as well.

**[07:41]** picks up on the language cues as well.

**[07:41]** picks up on the language cues as well. Um,

**[07:43]** Um,

**[07:43]** Um, other thing that's really important

**[07:44]** other thing that's really important

**[07:44]** other thing that's really important obviously for all voice use cases, not

**[07:46]** obviously for all voice use cases, not

**[07:46]** obviously for all voice use cases, not just um not just consumer, is latency.

**[07:49]** just um not just consumer, is latency.

**[07:49]** just um not just consumer, is latency. Um, so there's four things that really

**[07:51]** Um, so there's four things that really

**[07:51]** Um, so there's four things that really affect latency. Uh, time to first token

**[07:53]** affect latency. Uh, time to first token

**[07:53]** affect latency. Uh, time to first token is is one of them. Um, tokens per second

**[07:55]** is is one of them. Um, tokens per second

**[07:55]** is is one of them. Um, tokens per second is one of them. Um,

**[07:58]** is one of them. Um,

**[07:58]** is one of them. Um, I'll get into why that is later. Um but


### [08:00 - 09:00]

**[08:01]** I'll get into why that is later. Um but

**[08:01]** I'll get into why that is later. Um but what we found in network latency is

**[08:03]** what we found in network latency is

**[08:03]** what we found in network latency is another one but we found the the most uh

**[08:06]** another one but we found the the most uh

**[08:06]** another one but we found the the most uh biggest cause of latency was what we're

**[08:07]** biggest cause of latency was what we're

**[08:07]** biggest cause of latency was what we're calling head of line silence. Um this is

**[08:11]** calling head of line silence. Um this is

**[08:11]** calling head of line silence. Um this is somewhat specific to the Orpheus model.

**[08:12]** somewhat specific to the Orpheus model.

**[08:12]** somewhat specific to the Orpheus model. This isn't going to be true for all

**[08:13]** This isn't going to be true for all

**[08:13]** This isn't going to be true for all models. Um but head of line silence is

**[08:17]** models. Um but head of line silence is

**[08:17]** models. Um but head of line silence is basically that uh some somewhere in the

**[08:19]** basically that uh some somewhere in the

**[08:19]** basically that uh some somewhere in the finetune of Orpheus um the data had a

**[08:22]** finetune of Orpheus um the data had a

**[08:22]** finetune of Orpheus um the data had a lot of silence at the beginning um

**[08:24]** lot of silence at the beginning um

**[08:24]** lot of silence at the beginning um because it was voice actors that they

**[08:25]** because it was voice actors that they

**[08:25]** because it was voice actors that they hired and they train and they like took

**[08:27]** hired and they train and they like took

**[08:27]** hired and they train and they like took those scripts and train fine tune a

**[08:29]** those scripts and train fine tune a

**[08:29]** those scripts and train fine tune a model from it.

**[08:30]** model from it.

**[08:30]** model from it. Um, so this is like the default Orpheus

**[08:32]** Um, so this is like the default Orpheus

**[08:32]** Um, so this is like the default Orpheus voice uh or one of the ones that came

**[08:34]** voice uh or one of the ones that came

**[08:34]** voice uh or one of the ones that came with it called Tara and it has 600

**[08:36]** with it called Tara and it has 600

**[08:36]** with it called Tara and it has 600 milliseconds of latency at the

**[08:38]** milliseconds of latency at the

**[08:38]** milliseconds of latency at the beginning. And they probably had other

**[08:39]** beginning. And they probably had other

**[08:39]** beginning. And they probably had other good reasons for like adding silence at

**[08:41]** good reasons for like adding silence at

**[08:41]** good reasons for like adding silence at the beginning. Um, uh, but this is a

**[08:45]** the beginning. Um, uh, but this is a

**[08:45]** the beginning. Um, uh, but this is a lot, right? So 600 milliseconds of

**[08:47]** lot, right? So 600 milliseconds of

**[08:47]** lot, right? So 600 milliseconds of silence. Um, we actually found that Oh,

**[08:49]** silence. Um, we actually found that Oh,

**[08:49]** silence. Um, we actually found that Oh, so 600 milliseconds of silence. We're

**[08:52]** so 600 milliseconds of silence. We're

**[08:52]** so 600 milliseconds of silence. We're running on L40S machines as of now. Um,

**[08:56]** running on L40S machines as of now. Um,

**[08:56]** running on L40S machines as of now. Um, they can do about 100 tokens a second.

**[08:58]** they can do about 100 tokens a second.

**[08:58]** they can do about 100 tokens a second. So 600 milliseconds is uh almost half a


### [09:00 - 10:00]

**[09:01]** So 600 milliseconds is uh almost half a

**[09:01]** So 600 milliseconds is uh almost half a second of of silence. So even we're we

**[09:03]** second of of silence. So even we're we

**[09:03]** second of of silence. So even we're we are filtering out the silence like we're

**[09:04]** are filtering out the silence like we're

**[09:04]** are filtering out the silence like we're not just playing that audio back to the

**[09:06]** not just playing that audio back to the

**[09:06]** not just playing that audio back to the user. But because takes a while to

**[09:08]** user. But because takes a while to

**[09:08]** user. But because takes a while to generate those tokens, we're adding like

**[09:09]** generate those tokens, we're adding like

**[09:10]** generate those tokens, we're adding like basically half a second of of latency

**[09:12]** basically half a second of of latency

**[09:12]** basically half a second of of latency just on the on wasted compute pretty

**[09:14]** just on the on wasted compute pretty

**[09:14]** just on the on wasted compute pretty much. Um so yeah, even filtering out the

**[09:17]** much. Um so yeah, even filtering out the

**[09:17]** much. Um so yeah, even filtering out the silence, you're only like saving 10%

**[09:19]** silence, you're only like saving 10%

**[09:19]** silence, you're only like saving 10% there because you're just barely faster

**[09:20]** there because you're just barely faster

**[09:20]** there because you're just barely faster than real time. Um we're scrappy again,

**[09:22]** than real time. Um we're scrappy again,

**[09:22]** than real time. Um we're scrappy again, so we're running on L40s. Um, but what

**[09:26]** so we're running on L40s. Um, but what

**[09:26]** so we're running on L40s. Um, but what we found was interesting is that we

**[09:27]** we found was interesting is that we

**[09:27]** we found was interesting is that we could actually just fine-tune the

**[09:28]** could actually just fine-tune the

**[09:28]** could actually just fine-tune the silence away. So, um, this is an example

**[09:30]** silence away. So, um, this is an example

**[09:30]** silence away. So, um, this is an example of a clone that we did, a Laura

**[09:32]** of a clone that we did, a Laura

**[09:32]** of a clone that we did, a Laura fine-tune of a customer's clone, and the

**[09:34]** fine-tune of a customer's clone, and the

**[09:34]** fine-tune of a customer's clone, and the latency is is basically like 100

**[09:36]** latency is is basically like 100

**[09:36]** latency is is basically like 100 milliseconds like P50. Um, so much

**[09:39]** milliseconds like P50. Um, so much

**[09:39]** milliseconds like P50. Um, so much better like half a second basically for

**[09:41]** better like half a second basically for

**[09:41]** better like half a second basically for free.

**[09:43]** free.

**[09:43]** free. Uh, and that matters uh because these

**[09:45]** Uh, and that matters uh because these

**[09:45]** Uh, and that matters uh because these real-time you you kind of have a latency

**[09:47]** real-time you you kind of have a latency

**[09:47]** real-time you you kind of have a latency budget on the on the real-time

**[09:48]** budget on the on the real-time

**[09:48]** budget on the on the real-time application. So the way these work is

**[09:50]** application. So the way these work is

**[09:50]** application. So the way these work is you you know the human talks and then at

**[09:51]** you you know the human talks and then at

**[09:52]** you you know the human talks and then at some point you decide um is the human

**[09:54]** some point you decide um is the human

**[09:54]** some point you decide um is the human done talking? Those models are not

**[09:56]** done talking? Those models are not

**[09:56]** done talking? Those models are not perfect. So you typically add like a

**[09:57]** perfect. So you typically add like a

**[09:58]** perfect. So you typically add like a snooze period at the end of that. But


### [10:00 - 11:00]

**[10:00]** snooze period at the end of that. But

**[10:00]** snooze period at the end of that. But during that snooze period you can still

**[10:01]** during that snooze period you can still

**[10:01]** during that snooze period you can still do work. Um so what we do is we kick off

**[10:04]** do work. Um so what we do is we kick off

**[10:04]** do work. Um so what we do is we kick off the LLM. Um the way we have our Orpheus

**[10:07]** the LLM. Um the way we have our Orpheus

**[10:07]** the LLM. Um the way we have our Orpheus stack set up is we start generating

**[10:09]** stack set up is we start generating

**[10:09]** stack set up is we start generating audio after two sentences um or if it's

**[10:11]** audio after two sentences um or if it's

**[10:12]** audio after two sentences um or if it's done but two sentences typically uh

**[10:13]** done but two sentences typically uh

**[10:14]** done but two sentences typically uh which gives it enough context to like

**[10:15]** which gives it enough context to like

**[10:15]** which gives it enough context to like capture the emotions. Um, so all that to

**[10:18]** capture the emotions. Um, so all that to

**[10:18]** capture the emotions. Um, so all that to say is if we generate the first audio

**[10:20]** say is if we generate the first audio

**[10:20]** say is if we generate the first audio packet within that snooze period, then

**[10:21]** packet within that snooze period, then

**[10:22]** packet within that snooze period, then we're kind of like in the money on on

**[10:23]** we're kind of like in the money on on

**[10:23]** we're kind of like in the money on on latency in our latency budget. Um, now

**[10:25]** latency in our latency budget. Um, now

**[10:26]** latency in our latency budget. Um, now these endpointing models are going to

**[10:27]** these endpointing models are going to

**[10:27]** these endpointing models are going to get better. So, you know, that snooze

**[10:28]** get better. So, you know, that snooze

**[10:28]** get better. So, you know, that snooze period is going to go down to like half

**[10:30]** period is going to go down to like half

**[10:30]** period is going to go down to like half a second to a second is probably like

**[10:32]** a second to a second is probably like

**[10:32]** a second to a second is probably like the sweet spot, but one and a half

**[10:33]** the sweet spot, but one and a half

**[10:33]** the sweet spot, but one and a half seconds is um kind of the threshold I

**[10:35]** seconds is um kind of the threshold I

**[10:36]** seconds is um kind of the threshold I think for anything above that sounds

**[10:37]** think for anything above that sounds

**[10:37]** think for anything above that sounds pretty bad. Um, and anything kind of

**[10:39]** pretty bad. Um, and anything kind of

**[10:39]** pretty bad. Um, and anything kind of equal to or below that is like

**[10:41]** equal to or below that is like

**[10:41]** equal to or below that is like acceptable. Um, so yeah, that half a

**[10:44]** acceptable. Um, so yeah, that half a

**[10:44]** acceptable. Um, so yeah, that half a second mattered a lot because it gives

**[10:45]** second mattered a lot because it gives

**[10:45]** second mattered a lot because it gives our LLM more time to um create tokens

**[10:48]** our LLM more time to um create tokens

**[10:48]** our LLM more time to um create tokens and because we're letting customers

**[10:50]** and because we're letting customers

**[10:50]** and because we're letting customers bring their own LLMs, um, it's somewhat

**[10:52]** bring their own LLMs, um, it's somewhat

**[10:52]** bring their own LLMs, um, it's somewhat out of our control.

**[10:55]** out of our control.

**[10:55]** out of our control. Um, so the next big category here is

**[10:57]** Um, so the next big category here is

**[10:57]** Um, so the next big category here is infrastructure. Um, again, we're we're

**[10:59]** infrastructure. Um, again, we're we're

**[10:59]** infrastructure. Um, again, we're we're scrappy, so we really needed uh


### [11:00 - 12:00]

**[11:01]** scrappy, so we really needed uh

**[11:01]** scrappy, so we really needed uh something that um was robust and uh not

**[11:05]** something that um was robust and uh not

**[11:05]** something that um was robust and uh not too complicated. Um, and we needed batch

**[11:07]** too complicated. Um, and we needed batch

**[11:08]** too complicated. Um, and we needed batch inference. So we needed batch inference

**[11:09]** inference. So we needed batch inference

**[11:09]** inference. So we needed batch inference obviously to save money. So we need to

**[11:11]** obviously to save money. So we need to

**[11:11]** obviously to save money. So we need to run um multiple

**[11:13]** run um multiple

**[11:13]** run um multiple uh generations on in the same batch or

**[11:15]** uh generations on in the same batch or

**[11:15]** uh generations on in the same batch or in the on the same GPU concurrently and

**[11:18]** in the on the same GPU concurrently and

**[11:18]** in the on the same GPU concurrently and we also needed multiple Lauras uh to be

**[11:20]** we also needed multiple Lauras uh to be

**[11:20]** we also needed multiple Lauras uh to be running in the same batch on the same

**[11:22]** running in the same batch on the same

**[11:22]** running in the same batch on the same GPU. Um and we wanted one load balancer

**[11:25]** GPU. Um and we wanted one load balancer

**[11:25]** GPU. Um and we wanted one load balancer in front of everything. We're spinning

**[11:26]** in front of everything. We're spinning

**[11:26]** in front of everything. We're spinning up multiple different models for

**[11:27]** up multiple different models for

**[11:27]** up multiple different models for different languages. So we all wanted

**[11:29]** different languages. So we all wanted

**[11:29]** different languages. So we all wanted this just to sort of be like a black

**[11:30]** this just to sort of be like a black

**[11:30]** this just to sort of be like a black box. It just sort of worked. Um

**[11:33]** box. It just sort of worked. Um

**[11:33]** box. It just sort of worked. Um uh so VLM to the rescue supports all

**[11:36]** uh so VLM to the rescue supports all

**[11:36]** uh so VLM to the rescue supports all those things. Um so VLM um can do batch

**[11:41]** those things. Um so VLM um can do batch

**[11:41]** those things. Um so VLM um can do batch inference with Lauras which is really

**[11:43]** inference with Lauras which is really

**[11:43]** inference with Lauras which is really really awesome. Um this is unfortunately

**[11:46]** really awesome. Um this is unfortunately

**[11:46]** really awesome. Um this is unfortunately the FP16 model was slower than real time

**[11:48]** the FP16 model was slower than real time

**[11:48]** the FP16 model was slower than real time on L40s. It worked on H100 but it was

**[11:51]** on L40s. It worked on H100 but it was

**[11:51]** on L40s. It worked on H100 but it was slower than real time but again VLM to

**[11:53]** slower than real time but again VLM to

**[11:53]** slower than real time but again VLM to the rescue. Um they support FP8 dynamic

**[11:56]** the rescue. Um they support FP8 dynamic

**[11:56]** the rescue. Um they support FP8 dynamic quantization which requires basically

**[11:59]** quantization which requires basically

**[11:59]** quantization which requires basically zero work. Um it just works


### [12:00 - 13:00]

**[12:01]** zero work. Um it just works

**[12:01]** zero work. Um it just works automatically. It does all the um

**[12:03]** automatically. It does all the um

**[12:04]** automatically. It does all the um scaling and everything automatically. So

**[12:05]** scaling and everything automatically. So

**[12:05]** scaling and everything automatically. So you don't have to like train the

**[12:07]** you don't have to like train the

**[12:07]** you don't have to like train the calibration data into uh your own quant.

**[12:10]** calibration data into uh your own quant.

**[12:10]** calibration data into uh your own quant. It just works. Um and it's amazing. So

**[12:12]** It just works. Um and it's amazing. So

**[12:12]** It just works. Um and it's amazing. So that brought us up to 105 tokens a

**[12:14]** that brought us up to 105 tokens a

**[12:14]** that brought us up to 105 tokens a second on the non-fineetune uh voices

**[12:17]** second on the non-fineetune uh voices

**[12:17]** second on the non-fineetune uh voices and 95 tokens a second on the Laura uh

**[12:21]** and 95 tokens a second on the Laura uh

**[12:21]** and 95 tokens a second on the Laura uh voices with a batch of 10. Um which is

**[12:24]** voices with a batch of 10. Um which is

**[12:24]** voices with a batch of 10. Um which is we're yeah well well in the money uh in

**[12:26]** we're yeah well well in the money uh in

**[12:26]** we're yeah well well in the money uh in terms of margins and things like that.

**[12:27]** terms of margins and things like that.

**[12:28]** terms of margins and things like that. So that's nice. Um, party infrastructure

**[12:31]** So that's nice. Um, party infrastructure

**[12:31]** So that's nice. Um, party infrastructure is is of course load balancing. Um, so

**[12:33]** is is of course load balancing. Um, so

**[12:33]** is is of course load balancing. Um, so you know, Lauras are depending on what

**[12:35]** you know, Lauras are depending on what

**[12:36]** you know, Lauras are depending on what your hyperparameters are. Uh, they're

**[12:38]** your hyperparameters are. Uh, they're

**[12:38]** your hyperparameters are. Uh, they're between 100 and 200 megabytes. Um, so

**[12:41]** between 100 and 200 megabytes. Um, so

**[12:41]** between 100 and 200 megabytes. Um, so you want to make sure you end up on a

**[12:42]** you want to make sure you end up on a

**[12:42]** you want to make sure you end up on a server that has a Laura in memory and

**[12:44]** server that has a Laura in memory and

**[12:44]** server that has a Laura in memory and and and things like that. We also wanted

**[12:45]** and and things like that. We also wanted

**[12:45]** and and things like that. We also wanted to support um, so that's where like

**[12:47]** to support um, so that's where like

**[12:48]** to support um, so that's where like sticky session comes in here. Um,

**[12:51]** sticky session comes in here. Um,

**[12:51]** sticky session comes in here. Um, uh, and yeah, latency low, I guess. Um,

**[12:53]** uh, and yeah, latency low, I guess. Um,

**[12:54]** uh, and yeah, latency low, I guess. Um, but we also wanted to support streaming

**[12:55]** but we also wanted to support streaming

**[12:55]** but we also wanted to support streaming input. Um, uh, mainly because the LM

**[12:58]** input. Um, uh, mainly because the LM

**[12:58]** input. Um, uh, mainly because the LM often, you know, might not be done by


### [13:00 - 14:00]

**[13:00]** often, you know, might not be done by

**[13:00]** often, you know, might not be done by the time you want to start producing

**[13:01]** the time you want to start producing

**[13:01]** the time you want to start producing audio, but we also wanted to support

**[13:03]** audio, but we also wanted to support

**[13:03]** audio, but we also wanted to support arbitrarily long um, generation. So like

**[13:05]** arbitrarily long um, generation. So like

**[13:06]** arbitrarily long um, generation. So like storytelling, things like that. Um, so

**[13:08]** storytelling, things like that. Um, so

**[13:08]** storytelling, things like that. Um, so we we have um, so that that's another

**[13:10]** we we have um, so that that's another

**[13:10]** we we have um, so that that's another reason why uh, it I guess this load

**[13:13]** reason why uh, it I guess this load

**[13:13]** reason why uh, it I guess this load balancing problem is interesting because

**[13:14]** balancing problem is interesting because

**[13:14]** balancing problem is interesting because you want to make sure you end up on the

**[13:15]** you want to make sure you end up on the

**[13:15]** you want to make sure you end up on the same GPU across the whole session. Uh so

**[13:19]** same GPU across the whole session. Uh so

**[13:19]** same GPU across the whole session. Uh so we went with a pretty much like a buy

**[13:21]** we went with a pretty much like a buy

**[13:21]** we went with a pretty much like a buy the book consistent hash ring setup. Um

**[13:24]** the book consistent hash ring setup. Um

**[13:24]** the book consistent hash ring setup. Um so if you've seen hash rings before this

**[13:26]** so if you've seen hash rings before this

**[13:26]** so if you've seen hash rings before this is not that interesting but basically

**[13:28]** is not that interesting but basically

**[13:28]** is not that interesting but basically the way it works is you hash the servers

**[13:30]** the way it works is you hash the servers

**[13:30]** the way it works is you hash the servers um multiple times. So you want it called

**[13:32]** um multiple times. So you want it called

**[13:32]** um multiple times. So you want it called virtual node so it distributes around

**[13:34]** virtual node so it distributes around

**[13:34]** virtual node so it distributes around this hash ring um and then when you know

**[13:37]** this hash ring um and then when you know

**[13:37]** this hash ring um and then when you know generation starts you hash that with the

**[13:38]** generation starts you hash that with the

**[13:38]** generation starts you hash that with the same hashing algorithm you pick the

**[13:41]** same hashing algorithm you pick the

**[13:41]** same hashing algorithm you pick the nearest server to that and it just

**[13:43]** nearest server to that and it just

**[13:43]** nearest server to that and it just works. And the reason this is chosen is

**[13:45]** works. And the reason this is chosen is

**[13:45]** works. And the reason this is chosen is because you can like remove a server and

**[13:47]** because you can like remove a server and

**[13:47]** because you can like remove a server and it it doesn't um re reload balance like

**[13:50]** it it doesn't um re reload balance like

**[13:50]** it it doesn't um re reload balance like everything. It just only a few um I

**[13:53]** everything. It just only a few um I

**[13:53]** everything. It just only a few um I guess migrations so needed. Um the other

**[13:56]** guess migrations so needed. Um the other

**[13:56]** guess migrations so needed. Um the other nice thing about this strategy is if a

**[13:58]** nice thing about this strategy is if a

**[13:58]** nice thing about this strategy is if a clone gets very popular um it's pretty


### [14:00 - 15:00]

**[14:01]** clone gets very popular um it's pretty

**[14:01]** clone gets very popular um it's pretty easy to handle that. You can just uh

**[14:03]** easy to handle that. You can just uh

**[14:03]** easy to handle that. You can just uh append um to the Laura. So you can just

**[14:05]** append um to the Laura. So you can just

**[14:05]** append um to the Laura. So you can just the more popular Laura is, you can just

**[14:07]** the more popular Laura is, you can just

**[14:07]** the more popular Laura is, you can just add it to more servers and upscale and

**[14:09]** add it to more servers and upscale and

**[14:10]** add it to more servers and upscale and downscale that uh very elegantly without

**[14:12]** downscale that uh very elegantly without

**[14:12]** downscale that uh very elegantly without really a ton of engineering work.

**[14:15]** really a ton of engineering work.

**[14:15]** really a ton of engineering work. Um so yeah, at the high level it looks

**[14:18]** Um so yeah, at the high level it looks

**[14:18]** Um so yeah, at the high level it looks something like this. Um we have our

**[14:19]** something like this. Um we have our

**[14:19]** something like this. Um we have our WebRTC backend that kind of like

**[14:21]** WebRTC backend that kind of like

**[14:21]** WebRTC backend that kind of like terminates the client connections. Then

**[14:23]** terminates the client connections. Then

**[14:23]** terminates the client connections. Then we use websockets um to our GPUs and

**[14:26]** we use websockets um to our GPUs and

**[14:26]** we use websockets um to our GPUs and then the GPUs are talking to Reddus.

**[14:28]** then the GPUs are talking to Reddus.

**[14:28]** then the GPUs are talking to Reddus. Reddus is not the best um the best

**[14:31]** Reddus is not the best um the best

**[14:31]** Reddus is not the best um the best choice. Uh but if we scale beyond

**[14:33]** choice. Uh but if we scale beyond

**[14:33]** choice. Uh but if we scale beyond needing Reddus for this kind of thing,

**[14:35]** needing Reddus for this kind of thing,

**[14:35]** needing Reddus for this kind of thing, um we can just solve that with piles of

**[14:38]** um we can just solve that with piles of

**[14:38]** um we can just solve that with piles of money, I guess. Um but yeah, the way it

**[14:41]** money, I guess. Um but yeah, the way it

**[14:41]** money, I guess. Um but yeah, the way it works here is you uh start a session.

**[14:43]** works here is you uh start a session.

**[14:43]** works here is you uh start a session. The WebRTC backend just connects to any

**[14:45]** The WebRTC backend just connects to any

**[14:45]** The WebRTC backend just connects to any GPU, then it asks uh Reddus, hey, what

**[14:49]** GPU, then it asks uh Reddus, hey, what

**[14:49]** GPU, then it asks uh Reddus, hey, what GPU is this request supposed to be on?

**[14:51]** GPU is this request supposed to be on?

**[14:51]** GPU is this request supposed to be on? And then it just proxies it with another

**[14:53]** And then it just proxies it with another

**[14:53]** And then it just proxies it with another TCP connection to the correct GPU. Um,

**[14:55]** TCP connection to the correct GPU. Um,

**[14:55]** TCP connection to the correct GPU. Um, which is fine because these GPUs are in

**[14:56]** which is fine because these GPUs are in

**[14:56]** which is fine because these GPUs are in the same data center, private

**[14:58]** the same data center, private

**[14:58]** the same data center, private networking. Um, so low latency, TCP,


### [15:00 - 16:00]

**[15:01]** networking. Um, so low latency, TCP,

**[15:01]** networking. Um, so low latency, TCP, that's totally fine with within the same

**[15:02]** that's totally fine with within the same

**[15:02]** that's totally fine with within the same network. Um, so that's that's pretty

**[15:05]** network. Um, so that's that's pretty

**[15:06]** network. Um, so that's that's pretty much it. I mean, the conclusion here is,

**[15:08]** much it. I mean, the conclusion here is,

**[15:08]** much it. I mean, the conclusion here is, you know, we're we're pretty scrappy.

**[15:09]** you know, we're we're pretty scrappy.

**[15:09]** you know, we're we're pretty scrappy. Um, and we were able to host voice

**[15:12]** Um, and we were able to host voice

**[15:12]** Um, and we were able to host voice models on GPUs and handle that

**[15:14]** models on GPUs and handle that

**[15:14]** models on GPUs and handle that infrastructure, so you can, too. Um,

**[15:16]** infrastructure, so you can, too. Um,

**[15:16]** infrastructure, so you can, too. Um, open source is there. And, um, yeah, it

**[15:19]** open source is there. And, um, yeah, it

**[15:20]** open source is there. And, um, yeah, it I think it's going to unlock a ton of

**[15:21]** I think it's going to unlock a ton of

**[15:21]** I think it's going to unlock a ton of cool use cases. Um, shout outs, uh,

**[15:24]** cool use cases. Um, shout outs, uh,

**[15:24]** cool use cases. Um, shout outs, uh, shout out Swix. Um, he's a supporter of

**[15:26]** shout out Swix. Um, he's a supporter of

**[15:26]** shout out Swix. Um, he's a supporter of ours. Um, and obviously put put this on

**[15:29]** ours. Um, and obviously put put this on

**[15:29]** ours. Um, and obviously put put this on or half half of half of it, I guess.

**[15:31]** or half half of half of it, I guess.

**[15:31]** or half half of half of it, I guess. But, uh, Swix is awesome. We love him.

**[15:33]** But, uh, Swix is awesome. We love him.

**[15:33]** But, uh, Swix is awesome. We love him. Um, Canopy Labs, uh, who created

**[15:35]** Um, Canopy Labs, uh, who created

**[15:35]** Um, Canopy Labs, uh, who created Orpheus. Um, haven't met them. Would

**[15:37]** Orpheus. Um, haven't met them. Would

**[15:37]** Orpheus. Um, haven't met them. Would love to if they're here. Um, uh, and

**[15:39]** love to if they're here. Um, uh, and

**[15:39]** love to if they're here. Um, uh, and then just free open source software in

**[15:41]** then just free open source software in

**[15:41]** then just free open source software in general, right? Canopy Labs is built on

**[15:43]** general, right? Canopy Labs is built on

**[15:43]** general, right? Canopy Labs is built on Llama, which is and and Snack. So, it's

**[15:45]** Llama, which is and and Snack. So, it's

**[15:45]** Llama, which is and and Snack. So, it's this whole ecosystem is greater than the

**[15:47]** this whole ecosystem is greater than the

**[15:47]** this whole ecosystem is greater than the sum of its parts, I guess. And um

**[15:49]** sum of its parts, I guess. And um

**[15:49]** sum of its parts, I guess. And um LiveKit, we're a LiveKit alum, so love

**[15:53]** LiveKit, we're a LiveKit alum, so love

**[15:53]** LiveKit, we're a LiveKit alum, so love those guys. And our WebRTC infra is

**[15:55]** those guys. And our WebRTC infra is

**[15:55]** those guys. And our WebRTC infra is built on them. Um and then VLM uh um

**[15:58]** built on them. Um and then VLM uh um

**[15:58]** built on them. Um and then VLM uh um notable open source project.


### [16:00 - 17:00]

**[16:01]** notable open source project.

**[16:01]** notable open source project. And yeah, that's it.


