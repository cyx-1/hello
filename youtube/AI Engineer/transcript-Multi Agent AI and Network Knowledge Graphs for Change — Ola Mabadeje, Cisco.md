# Multi Agent AI and Network Knowledge Graphs for Change — Ola Mabadeje, Cisco

**Video URL:** https://www.youtube.com/watch?v=m0dxZ-NDKHo

---

## Full Transcript

### [00:00 - 01:00]

**[00:17]** Good afternoon everyone. My name is Ola

**[00:17]** Good afternoon everyone. My name is Ola Mabad. I'm a product guy from Cisco. Um

**[00:21]** Mabad. I'm a product guy from Cisco. Um

**[00:21]** Mabad. I'm a product guy from Cisco. Um so my presentation is going to be a

**[00:23]** so my presentation is going to be a

**[00:23]** so my presentation is going to be a little more producty than techy, but um

**[00:26]** little more producty than techy, but um

**[00:26]** little more producty than techy, but um uh I think you're going to enjoy it. So

**[00:28]** uh I think you're going to enjoy it. So

**[00:28]** uh I think you're going to enjoy it. So um I've been at Cisco working on uh AI

**[00:32]** um I've been at Cisco working on uh AI

**[00:32]** um I've been at Cisco working on uh AI for the last three years and um I work

**[00:34]** for the last three years and um I work

**[00:34]** for the last three years and um I work in this group called outshift. So

**[00:36]** in this group called outshift. So

**[00:36]** in this group called outshift. So outshift is Cisco's incubation group. uh

**[00:39]** outshift is Cisco's incubation group. uh

**[00:39]** outshift is Cisco's incubation group. uh our charter is to help Cisco look at

**[00:41]** our charter is to help Cisco look at

**[00:41]** our charter is to help Cisco look at emerging technologies and see how this

**[00:43]** emerging technologies and see how this

**[00:43]** emerging technologies and see how this emerging technologies can help us

**[00:44]** emerging technologies can help us

**[00:44]** emerging technologies can help us accelerate the road maps of our

**[00:47]** accelerate the road maps of our

**[00:47]** accelerate the road maps of our traditional business units and uh so um

**[00:51]** traditional business units and uh so um

**[00:51]** traditional business units and uh so um by uh by training I'm an electrical

**[00:53]** by uh by training I'm an electrical

**[00:53]** by uh by training I'm an electrical engineer um dabbled into network

**[00:55]** engineer um dabbled into network

**[00:55]** engineer um dabbled into network engineering enjoyed it and I've been

**[00:58]** engineering enjoyed it and I've been

**[00:58]** engineering enjoyed it and I've been doing that for a while but over the last

**[00:59]** doing that for a while but over the last

**[00:59]** doing that for a while but over the last three years focused on AI um our group


### [01:00 - 02:00]

**[01:02]** three years focused on AI um our group

**[01:02]** three years focused on AI um our group also focuses on quantum technology so

**[01:04]** also focuses on quantum technology so

**[01:04]** also focuses on quantum technology so quantum networking is something that

**[01:06]** quantum networking is something that

**[01:06]** quantum networking is something that we're focused on and um if you want to

**[01:08]** we're focused on and um if you want to

**[01:08]** we're focused on and um if you want to learn more about what we do. Uh we're

**[01:10]** learn more about what we do. Uh we're

**[01:10]** learn more about what we do. Uh we're out shift at Cisco. Uh you can learn

**[01:12]** out shift at Cisco. Uh you can learn

**[01:12]** out shift at Cisco. Uh you can learn more about that. So uh for today we're

**[01:15]** more about that. So uh for today we're

**[01:15]** more about that. So uh for today we're going to dive into this uh real quick

**[01:17]** going to dive into this uh real quick

**[01:17]** going to dive into this uh real quick and um like I said I'm a product guy. So

**[01:19]** and um like I said I'm a product guy. So

**[01:19]** and um like I said I'm a product guy. So I usually start with my customers

**[01:21]** I usually start with my customers

**[01:21]** I usually start with my customers problems trying to understand what are

**[01:23]** problems trying to understand what are

**[01:23]** problems trying to understand what are they trying to solve for and then from

**[01:24]** they trying to solve for and then from

**[01:24]** they trying to solve for and then from that work backwards towards creating a

**[01:26]** that work backwards towards creating a

**[01:26]** that work backwards towards creating a solution for that. So as part of the

**[01:29]** solution for that. So as part of the

**[01:29]** solution for that. So as part of the process for us we usually go through

**[01:30]** process for us we usually go through

**[01:30]** process for us we usually go through this incubation phase where we ask

**[01:32]** this incubation phase where we ask

**[01:32]** this incubation phase where we ask customers a lot of questions and then we

**[01:34]** customers a lot of questions and then we

**[01:34]** customers a lot of questions and then we come up with prototypes we do a testing

**[01:36]** come up with prototypes we do a testing

**[01:36]** come up with prototypes we do a testing b testing and then we kind of deliver an

**[01:38]** b testing and then we kind of deliver an

**[01:38]** b testing and then we kind of deliver an MVP into a production environment and

**[01:41]** MVP into a production environment and

**[01:41]** MVP into a production environment and once we get product market fit that

**[01:44]** once we get product market fit that

**[01:44]** once we get product market fit that product graduates into the Cisco

**[01:45]** product graduates into the Cisco

**[01:45]** product graduates into the Cisco businesses so this customer had this

**[01:47]** businesses so this customer had this

**[01:47]** businesses so this customer had this issue they said when we do change

**[01:49]** issue they said when we do change

**[01:49]** issue they said when we do change management we have a lot of challenges

**[01:51]** management we have a lot of challenges

**[01:51]** management we have a lot of challenges with failures in production how can we

**[01:54]** with failures in production how can we

**[01:54]** with failures in production how can we reduce that can we use AI to reduce that

**[01:57]** reduce that can we use AI to reduce that

**[01:57]** reduce that can we use AI to reduce that problem. So we double clicked on that

**[01:58]** problem. So we double clicked on that

**[01:58]** problem. So we double clicked on that problem statement and we realized it was


### [02:00 - 03:00]

**[02:00]** problem statement and we realized it was

**[02:00]** problem statement and we realized it was a major problem across the industry. I

**[02:02]** a major problem across the industry. I

**[02:02]** a major problem across the industry. I won't go into the details here but it's

**[02:04]** won't go into the details here but it's

**[02:04]** won't go into the details here but it's a big problem. Now uh for us to solve

**[02:06]** a big problem. Now uh for us to solve

**[02:06]** a big problem. Now uh for us to solve the problem wanted to understand does AI

**[02:08]** the problem wanted to understand does AI

**[02:08]** the problem wanted to understand does AI really have a place here or it's just

**[02:10]** really have a place here or it's just

**[02:10]** really have a place here or it's just going to be rulebased automation to to

**[02:12]** going to be rulebased automation to to

**[02:12]** going to be rulebased automation to to solve this problem. And we looked at the

**[02:14]** solve this problem. And we looked at the

**[02:14]** solve this problem. And we looked at the workflow we realized that there are

**[02:16]** workflow we realized that there are

**[02:16]** workflow we realized that there are specific spots in the workflow where AI

**[02:18]** specific spots in the workflow where AI

**[02:18]** specific spots in the workflow where AI agents can actually help address a

**[02:20]** agents can actually help address a

**[02:20]** agents can actually help address a problem. And so we we kind of

**[02:22]** problem. And so we we kind of

**[02:22]** problem. And so we we kind of highlighted three, four and five where

**[02:23]** highlighted three, four and five where

**[02:23]** highlighted three, four and five where we believe that AI agents can help

**[02:26]** we believe that AI agents can help

**[02:26]** we believe that AI agents can help increase the value uh for customers and

**[02:28]** increase the value uh for customers and

**[02:28]** increase the value uh for customers and reduce the pain points that they were

**[02:29]** reduce the pain points that they were

**[02:29]** reduce the pain points that they were describing. And so we sat down together

**[02:32]** describing. And so we sat down together

**[02:32]** describing. And so we sat down together with the teams. We said let's figure out

**[02:33]** with the teams. We said let's figure out

**[02:34]** with the teams. We said let's figure out a solution for this. Um and so uh this

**[02:37]** a solution for this. Um and so uh this

**[02:37]** a solution for this. Um and so uh this solution consists of three big buckets.

**[02:39]** solution consists of three big buckets.

**[02:39]** solution consists of three big buckets. The first one is the fact that it's a it

**[02:41]** The first one is the fact that it's a it

**[02:41]** The first one is the fact that it's a it has to be natural language interface

**[02:43]** has to be natural language interface

**[02:43]** has to be natural language interface where network operations teams can

**[02:45]** where network operations teams can

**[02:45]** where network operations teams can actually interact with the system. So

**[02:47]** actually interact with the system. So

**[02:47]** actually interact with the system. So that's the first thing and not just

**[02:49]** that's the first thing and not just

**[02:49]** that's the first thing and not just engineers but also systems. So for

**[02:51]** engineers but also systems. So for

**[02:51]** engineers but also systems. So for example in our case we built this system

**[02:52]** example in our case we built this system

**[02:52]** example in our case we built this system to talk to an ITSM tool such as service

**[02:55]** to talk to an ITSM tool such as service

**[02:55]** to talk to an ITSM tool such as service now. So we actually have a agents on the

**[02:57]** now. So we actually have a agents on the

**[02:57]** now. So we actually have a agents on the service now side talking to agents on

**[02:59]** service now side talking to agents on

**[02:59]** service now side talking to agents on our side. Um the second piece of this is


### [03:00 - 04:00]

**[03:01]** our side. Um the second piece of this is

**[03:02]** our side. Um the second piece of this is the multi- aent system that sits within

**[03:03]** the multi- aent system that sits within

**[03:03]** the multi- aent system that sits within the within this application. So we have

**[03:05]** the within this application. So we have

**[03:06]** the within this application. So we have agents that are tasked at doing specific

**[03:07]** agents that are tasked at doing specific

**[03:08]** agents that are tasked at doing specific things. So an agent that is tasked as

**[03:09]** things. So an agent that is tasked as

**[03:09]** things. So an agent that is tasked as doing impact assessment doing testing

**[03:12]** doing impact assessment doing testing

**[03:12]** doing impact assessment doing testing doing uh reasoning around uh potential

**[03:15]** doing uh reasoning around uh potential

**[03:15]** doing uh reasoning around uh potential failures that could happen in the in the

**[03:16]** failures that could happen in the in the

**[03:16]** failures that could happen in the in the network. And then the third piece of

**[03:18]** network. And then the third piece of

**[03:18]** network. And then the third piece of this is where we're going to spend some

**[03:19]** this is where we're going to spend some

**[03:20]** this is where we're going to spend some of the time today, which is network

**[03:21]** of the time today, which is network

**[03:21]** of the time today, which is network knowledge graph. So we have a a the

**[03:23]** knowledge graph. So we have a a the

**[03:23]** knowledge graph. So we have a a the concept of a digital twin in this case.

**[03:25]** concept of a digital twin in this case.

**[03:25]** concept of a digital twin in this case. So what we're trying to do here is to

**[03:26]** So what we're trying to do here is to

**[03:26]** So what we're trying to do here is to build a twin of the actual production

**[03:28]** build a twin of the actual production

**[03:28]** build a twin of the actual production network. And that twin includes a

**[03:30]** network. And that twin includes a

**[03:30]** network. And that twin includes a knowledge graph plus a set of tools to

**[03:33]** knowledge graph plus a set of tools to

**[03:33]** knowledge graph plus a set of tools to execute test testing. And so um we're

**[03:36]** execute test testing. And so um we're

**[03:36]** execute test testing. And so um we're going to dive into that in a little bit.

**[03:38]** going to dive into that in a little bit.

**[03:38]** going to dive into that in a little bit. But before we go into that, I I we we

**[03:40]** But before we go into that, I I we we

**[03:40]** But before we go into that, I I we we had this challenge of okay, we want to

**[03:43]** had this challenge of okay, we want to

**[03:43]** had this challenge of okay, we want to build a representative representation of

**[03:45]** build a representative representation of

**[03:45]** build a representative representation of the actual network. How are we going to

**[03:47]** the actual network. How are we going to

**[03:47]** the actual network. How are we going to do this? Um because if you know

**[03:50]** do this? Um because if you know

**[03:50]** do this? Um because if you know networking pretty well, networking is a

**[03:52]** networking pretty well, networking is a

**[03:52]** networking pretty well, networking is a very complex uh technology. You have a

**[03:55]** very complex uh technology. You have a

**[03:55]** very complex uh technology. You have a variety of vendors in the customers

**[03:57]** variety of vendors in the customers

**[03:58]** variety of vendors in the customers environment, variety of devices,

**[03:59]** environment, variety of devices,

**[03:59]** environment, variety of devices, firewalls, switches, routers and so on.


### [04:00 - 05:00]

**[04:01]** firewalls, switches, routers and so on.

**[04:01]** firewalls, switches, routers and so on. And all of these different devices are

**[04:04]** And all of these different devices are

**[04:04]** And all of these different devices are spitting out data in different formats.

**[04:06]** spitting out data in different formats.

**[04:06]** spitting out data in different formats. So the challenge for us was how can we

**[04:08]** So the challenge for us was how can we

**[04:08]** So the challenge for us was how can we create a representation of this real

**[04:10]** create a representation of this real

**[04:10]** create a representation of this real world network using knowledge graphs in

**[04:13]** world network using knowledge graphs in

**[04:13]** world network using knowledge graphs in a data schema that can that can be

**[04:14]** a data schema that can that can be

**[04:14]** a data schema that can that can be understood by agents. And so the goal

**[04:17]** understood by agents. And so the goal

**[04:17]** understood by agents. And so the goal was for us to create this ingestion

**[04:18]** was for us to create this ingestion

**[04:18]** was for us to create this ingestion pipeline that can represent the network

**[04:20]** pipeline that can represent the network

**[04:20]** pipeline that can represent the network in such a way that agents can take the

**[04:22]** in such a way that agents can take the

**[04:22]** in such a way that agents can take the the right actions in a meaningful way

**[04:24]** the right actions in a meaningful way

**[04:24]** the right actions in a meaningful way and predictive way. And so for us to to

**[04:27]** and predictive way. And so for us to to

**[04:27]** and predictive way. And so for us to to kind of proceed with that we had this

**[04:29]** kind of proceed with that we had this

**[04:29]** kind of proceed with that we had this three big buckets of things to consider.

**[04:32]** three big buckets of things to consider.

**[04:32]** three big buckets of things to consider. So we we had to think about what are the

**[04:34]** So we we had to think about what are the

**[04:34]** So we we had to think about what are the data sources going to be. So if you

**[04:36]** data sources going to be. So if you

**[04:36]** data sources going to be. So if you again in networking there are

**[04:37]** again in networking there are

**[04:37]** again in networking there are controllers systems there the devices

**[04:39]** controllers systems there the devices

**[04:40]** controllers systems there the devices themselves there agents in the devices

**[04:41]** themselves there agents in the devices

**[04:42]** themselves there agents in the devices there are configuration management

**[04:43]** there are configuration management

**[04:43]** there are configuration management systems all of these things are all

**[04:45]** systems all of these things are all

**[04:45]** systems all of these things are all collecting data from the network or

**[04:47]** collecting data from the network or

**[04:47]** collecting data from the network or they'll have data about the network now

**[04:49]** they'll have data about the network now

**[04:49]** they'll have data about the network now when they spit out their data they're

**[04:51]** when they spit out their data they're

**[04:51]** when they spit out their data they're spitting it out in different languages

**[04:52]** spitting it out in different languages

**[04:52]** spitting it out in different languages yang JSON and so on another set of

**[04:55]** yang JSON and so on another set of

**[04:55]** yang JSON and so on another set of considerations to have and then in terms

**[04:57]** considerations to have and then in terms

**[04:57]** considerations to have and then in terms of how the data is actually coming out

**[04:59]** of how the data is actually coming out

**[04:59]** of how the data is actually coming out it could be coming out in term of


### [05:00 - 06:00]

**[05:00]** it could be coming out in term of

**[05:00]** it could be coming out in term of streaming telemetry it could be

**[05:01]** streaming telemetry it could be

**[05:01]** streaming telemetry it could be configuration files in JSON it could be

**[05:03]** configuration files in JSON it could be

**[05:03]** configuration files in JSON it could be some other form of of data

**[05:05]** some other form of of data

**[05:06]** some other form of of data How can we look at all of these three

**[05:07]** How can we look at all of these three

**[05:07]** How can we look at all of these three different considerations and be able to

**[05:09]** different considerations and be able to

**[05:09]** different considerations and be able to set come up with a set of requirements

**[05:10]** set come up with a set of requirements

**[05:10]** set come up with a set of requirements that allows us to actually build a

**[05:12]** that allows us to actually build a

**[05:12]** that allows us to actually build a system that that addresses the

**[05:14]** system that that addresses the

**[05:14]** system that that addresses the customer's pain point again and so um

**[05:16]** customer's pain point again and so um

**[05:16]** customer's pain point again and so um the team uh from a product side we had a

**[05:19]** the team uh from a product side we had a

**[05:19]** the team uh from a product side we had a set of requirements we we wanted a

**[05:20]** set of requirements we we wanted a

**[05:20]** set of requirements we we wanted a system that uh a knowledge graph that

**[05:23]** system that uh a knowledge graph that

**[05:23]** system that uh a knowledge graph that can have multimodel flexibility uh that

**[05:25]** can have multimodel flexibility uh that

**[05:25]** can have multimodel flexibility uh that means you can talk key value pairs you

**[05:28]** means you can talk key value pairs you

**[05:28]** means you can talk key value pairs you understand JSON files it understands uh

**[05:31]** understand JSON files it understands uh

**[05:31]** understand JSON files it understands uh relationships across different entities

**[05:33]** relationships across different entities

**[05:33]** relationships across different entities in a network. Second thing is

**[05:35]** in a network. Second thing is

**[05:35]** in a network. Second thing is performance. Uh if a if an engineer is

**[05:38]** performance. Uh if a if an engineer is

**[05:38]** performance. Uh if a if an engineer is querying a knowledge graph, we want to

**[05:40]** querying a knowledge graph, we want to

**[05:40]** querying a knowledge graph, we want to have instant access to the node

**[05:42]** have instant access to the node

**[05:42]** have instant access to the node information about the node no matter

**[05:44]** information about the node no matter

**[05:44]** information about the node no matter where the the location of that node is.

**[05:46]** where the the location of that node is.

**[05:46]** where the the location of that node is. That was important for our customers.

**[05:47]** That was important for our customers.

**[05:48]** That was important for our customers. The second thing was operational

**[05:49]** The second thing was operational

**[05:49]** The second thing was operational flexibility. So the schema has to be

**[05:50]** flexibility. So the schema has to be

**[05:50]** flexibility. So the schema has to be such that uh we can consolidate into one

**[05:53]** such that uh we can consolidate into one

**[05:53]** such that uh we can consolidate into one schema framework. Uh the fourth piece

**[05:55]** schema framework. Uh the fourth piece

**[05:55]** schema framework. Uh the fourth piece here is where the the the rag piece

**[05:58]** here is where the the the rag piece

**[05:58]** here is where the the the rag piece comes into place. So we've been hearing

**[05:59]** comes into place. So we've been hearing


### [06:00 - 07:00]

**[06:00]** comes into place. So we've been hearing a little about graph rag for for for a

**[06:01]** a little about graph rag for for for a

**[06:01]** a little about graph rag for for for a little bit today. uh we wanted this to

**[06:03]** little bit today. uh we wanted this to

**[06:03]** little bit today. uh we wanted this to be a system that has ability to have

**[06:05]** be a system that has ability to have

**[06:05]** be a system that has ability to have vector indexing in it so that when you

**[06:07]** vector indexing in it so that when you

**[06:07]** vector indexing in it so that when you want to do semantic searches at some

**[06:09]** want to do semantic searches at some

**[06:09]** want to do semantic searches at some point you can do that as well. And then

**[06:11]** point you can do that as well. And then

**[06:11]** point you can do that as well. And then in terms of just ecosystem uh um

**[06:13]** in terms of just ecosystem uh um

**[06:13]** in terms of just ecosystem uh um stability we want to make sure that when

**[06:15]** stability we want to make sure that when

**[06:15]** stability we want to make sure that when we put this in the customer's

**[06:16]** we put this in the customer's

**[06:16]** we put this in the customer's environments uh there's not there's not

**[06:18]** environments uh there's not there's not

**[06:18]** environments uh there's not there's not going to be a lot of heavy lifting

**[06:19]** going to be a lot of heavy lifting

**[06:19]** going to be a lot of heavy lifting that's going to be done by the customer

**[06:20]** that's going to be done by the customer

**[06:20]** that's going to be done by the customer to integrate with their systems and

**[06:22]** to integrate with their systems and

**[06:22]** to integrate with their systems and again it has to support multiple

**[06:23]** again it has to support multiple

**[06:23]** again it has to support multiple vendors. So these were the requirements

**[06:25]** vendors. So these were the requirements

**[06:25]** vendors. So these were the requirements from a product side and then our

**[06:26]** from a product side and then our

**[06:26]** from a product side and then our engineering teams kind of we started to

**[06:28]** engineering teams kind of we started to

**[06:28]** engineering teams kind of we started to consider some of the options on the

**[06:29]** consider some of the options on the

**[06:29]** consider some of the options on the table. uh neo forj obviously uh market

**[06:32]** table. uh neo forj obviously uh market

**[06:32]** table. uh neo forj obviously uh market leader uh and the various other open

**[06:33]** leader uh and the various other open

**[06:34]** leader uh and the various other open source tools. At the end of the day the

**[06:36]** source tools. At the end of the day the

**[06:36]** source tools. At the end of the day the engineering teams decided to kind of do

**[06:38]** engineering teams decided to kind of do

**[06:38]** engineering teams decided to kind of do uh some analysis around this. So I can

**[06:40]** uh some analysis around this. So I can

**[06:40]** uh some analysis around this. So I can I'm showing a table on the right hand

**[06:41]** I'm showing a table on the right hand

**[06:41]** I'm showing a table on the right hand side. It's not an exhaustive list of

**[06:43]** side. It's not an exhaustive list of

**[06:43]** side. It's not an exhaustive list of things that they considered but these

**[06:44]** things that they considered but these

**[06:44]** things that they considered but these were the things that they looked at that

**[06:46]** were the things that they looked at that

**[06:46]** were the things that they looked at that they wanted to see okay what is the

**[06:48]** they wanted to see okay what is the

**[06:48]** they wanted to see okay what is the right solution to address the

**[06:49]** right solution to address the

**[06:50]** right solution to address the requirements coming from product and um

**[06:53]** requirements coming from product and um

**[06:53]** requirements coming from product and um uh we they kind of we kind of all

**[06:55]** uh we they kind of we kind of all

**[06:55]** uh we they kind of we kind of all centered around the first two here no 4G

**[06:57]** centered around the first two here no 4G

**[06:57]** centered around the first two here no 4G and Arango DB but for historical reasons


### [07:00 - 08:00]

**[07:00]** and Arango DB but for historical reasons

**[07:00]** and Arango DB but for historical reasons the team decided to go with because we

**[07:02]** the team decided to go with because we

**[07:02]** the team decided to go with because we had some use cases that were in the

**[07:04]** had some use cases that were in the

**[07:04]** had some use cases that were in the security space uh that was kind of a

**[07:06]** security space uh that was kind of a

**[07:06]** security space uh that was kind of a recommendation system uh type of use

**[07:08]** recommendation system uh type of use

**[07:08]** recommendation system uh type of use cases that we wanted to kind of continue

**[07:10]** cases that we wanted to kind of continue

**[07:10]** cases that we wanted to kind of continue using and so um But we are still

**[07:12]** using and so um But we are still

**[07:12]** using and so um But we are still exploring the use of Neo forj for some

**[07:14]** exploring the use of Neo forj for some

**[07:14]** exploring the use of Neo forj for some of the use cases that are coming up as

**[07:15]** of the use cases that are coming up as

**[07:15]** of the use cases that are coming up as part of this project. So um we settled

**[07:19]** part of this project. So um we settled

**[07:19]** part of this project. So um we settled on on a DV for this and uh we eventually

**[07:22]** on on a DV for this and uh we eventually

**[07:22]** on on a DV for this and uh we eventually came up with a solution that looks like

**[07:23]** came up with a solution that looks like

**[07:23]** came up with a solution that looks like this. So we have this knowledge graph

**[07:24]** this. So we have this knowledge graph

**[07:24]** this. So we have this knowledge graph solution. This is an overview of it. Um

**[07:27]** solution. This is an overview of it. Um

**[07:27]** solution. This is an overview of it. Um on the left hand side we have all of the

**[07:29]** on the left hand side we have all of the

**[07:29]** on the left hand side we have all of the production environment. We have the

**[07:31]** production environment. We have the

**[07:31]** production environment. We have the controllers the the Splunk which is a

**[07:33]** controllers the the Splunk which is a

**[07:33]** controllers the the Splunk which is a sim system traffic telemetry coming in.

**[07:35]** sim system traffic telemetry coming in.

**[07:36]** sim system traffic telemetry coming in. All of them are coming into this

**[07:37]** All of them are coming into this

**[07:37]** All of them are coming into this ingestion service uh which is doing an

**[07:39]** ingestion service uh which is doing an

**[07:39]** ingestion service uh which is doing an ETL transforming all of this information

**[07:41]** ETL transforming all of this information

**[07:41]** ETL transforming all of this information into one schema open config. So open

**[07:44]** into one schema open config. So open

**[07:44]** into one schema open config. So open config schema is a schema that is

**[07:46]** config schema is a schema that is

**[07:46]** config schema is a schema that is designed around networking primarily and

**[07:49]** designed around networking primarily and

**[07:49]** designed around networking primarily and uh it helps us to because it there's a

**[07:50]** uh it helps us to because it there's a

**[07:50]** uh it helps us to because it there's a lot of documentation about it on the

**[07:52]** lot of documentation about it on the

**[07:52]** lot of documentation about it on the internet. So LM understand this very

**[07:54]** internet. So LM understand this very

**[07:54]** internet. So LM understand this very well. So um this setup is primarily a a

**[07:59]** well. So um this setup is primarily a a


### [08:00 - 09:00]

**[08:00]** well. So um this setup is primarily a a database of uh of uh networking

**[08:03]** database of uh of uh networking

**[08:03]** database of uh of uh networking information that has open config schema

**[08:05]** information that has open config schema

**[08:05]** information that has open config schema as a primary way for us to communicate

**[08:06]** as a primary way for us to communicate

**[08:06]** as a primary way for us to communicate with it. So uh natural language

**[08:08]** with it. So uh natural language

**[08:08]** with it. So uh natural language communication through an individual

**[08:10]** communication through an individual

**[08:10]** communication through an individual engineer or the agents that are actually

**[08:12]** engineer or the agents that are actually

**[08:12]** engineer or the agents that are actually interacting with that system. And so we

**[08:15]** interacting with that system. And so we

**[08:15]** interacting with that system. And so we built this in the form of layers. So uh

**[08:17]** built this in the form of layers. So uh

**[08:17]** built this in the form of layers. So uh if you if you're if you're into

**[08:19]** if you if you're if you're into

**[08:19]** if you if you're if you're into networking again um there is a set of

**[08:22]** networking again um there is a set of

**[08:22]** networking again um there is a set of entities in the network that you want to

**[08:23]** entities in the network that you want to

**[08:23]** entities in the network that you want to be able to interact with. Uh so we have

**[08:25]** be able to interact with. Uh so we have

**[08:25]** be able to interact with. Uh so we have layered this up in this way such that if

**[08:27]** layered this up in this way such that if

**[08:27]** layered this up in this way such that if uh there's a tool call or there's a

**[08:29]** uh there's a tool call or there's a

**[08:29]** uh there's a tool call or there's a decision to be made about a test for

**[08:32]** decision to be made about a test for

**[08:32]** decision to be made about a test for example let's say you want to do a test

**[08:33]** example let's say you want to do a test

**[08:33]** example let's say you want to do a test about uh configuration drift as an

**[08:36]** about uh configuration drift as an

**[08:36]** about uh configuration drift as an example um you don't need to go to all

**[08:38]** example um you don't need to go to all

**[08:38]** example um you don't need to go to all of the layers of the graph you just go

**[08:39]** of the layers of the graph you just go

**[08:39]** of the layers of the graph you just go straight down to the raw configuration

**[08:41]** straight down to the raw configuration

**[08:41]** straight down to the raw configuration file and be able to do your comp

**[08:42]** file and be able to do your comp

**[08:42]** file and be able to do your comp comparisons there. If you're trying to

**[08:44]** comparisons there. If you're trying to

**[08:44]** comparisons there. If you're trying to do like a test around reachability for

**[08:46]** do like a test around reachability for

**[08:46]** do like a test around reachability for example then you need a couple of layers

**[08:47]** example then you need a couple of layers

**[08:47]** example then you need a couple of layers maybe you need raw configuration layers

**[08:49]** maybe you need raw configuration layers

**[08:49]** maybe you need raw configuration layers data control data plane layers and

**[08:51]** data control data plane layers and

**[08:51]** data control data plane layers and control plane layers. So um it's

**[08:53]** control plane layers. So um it's

**[08:53]** control plane layers. So um it's structured in a way that when the agents

**[08:55]** structured in a way that when the agents

**[08:55]** structured in a way that when the agents are making their calls to this system uh

**[08:57]** are making their calls to this system uh

**[08:57]** are making their calls to this system uh they understand what the request is from

**[08:59]** they understand what the request is from

**[08:59]** they understand what the request is from the from the uh system and they're able


### [09:00 - 10:00]

**[09:02]** the from the uh system and they're able

**[09:02]** the from the uh system and they're able to actually go to the right layer to

**[09:03]** to actually go to the right layer to

**[09:03]** to actually go to the right layer to pick up the information that they need

**[09:05]** pick up the information that they need

**[09:05]** pick up the information that they need to ex to execute on it. So this is kind

**[09:07]** to ex to execute on it. So this is kind

**[09:07]** to ex to execute on it. So this is kind of a high level view of what the graph

**[09:09]** of a high level view of what the graph

**[09:09]** of a high level view of what the graph system looks like in layers. Now um I'm

**[09:13]** system looks like in layers. Now um I'm

**[09:13]** system looks like in layers. Now um I'm going to kind of switch gear switch

**[09:15]** going to kind of switch gear switch

**[09:15]** going to kind of switch gear switch gears now and go back to the system.

**[09:17]** gears now and go back to the system.

**[09:17]** gears now and go back to the system. Remember I described a system that had

**[09:19]** Remember I described a system that had

**[09:19]** Remember I described a system that had agents a knowledge graph and digital

**[09:21]** agents a knowledge graph and digital

**[09:21]** agents a knowledge graph and digital twin as well as natural language

**[09:23]** twin as well as natural language

**[09:23]** twin as well as natural language interface. So let's talk about the

**[09:24]** interface. So let's talk about the

**[09:24]** interface. So let's talk about the agentic layer and before I kind of talk

**[09:26]** agentic layer and before I kind of talk

**[09:26]** agentic layer and before I kind of talk about the specific agents in um in this

**[09:30]** about the specific agents in um in this

**[09:30]** about the specific agents in um in this system on this application we are

**[09:32]** system on this application we are

**[09:32]** system on this application we are looking at how we are going to build a

**[09:34]** looking at how we are going to build a

**[09:34]** looking at how we are going to build a system that is based on open standards

**[09:36]** system that is based on open standards

**[09:36]** system that is based on open standards for all of the internet and this is one

**[09:38]** for all of the internet and this is one

**[09:38]** for all of the internet and this is one of the challenge we have within Cisco.

**[09:40]** of the challenge we have within Cisco.

**[09:40]** of the challenge we have within Cisco. We we are looking at a system a a set of

**[09:43]** We we are looking at a system a a set of

**[09:43]** We we are looking at a system a a set of a collective open source collective that

**[09:45]** a collective open source collective that

**[09:45]** a collective open source collective that includes all of the partners we see down

**[09:47]** includes all of the partners we see down

**[09:47]** includes all of the partners we see down here. So we have uh outship by Cisco we

**[09:50]** here. So we have uh outship by Cisco we

**[09:50]** here. So we have uh outship by Cisco we have lang chain Galileo we have all of

**[09:52]** have lang chain Galileo we have all of

**[09:52]** have lang chain Galileo we have all of these uh members who are supporters of

**[09:54]** these uh members who are supporters of

**[09:54]** these uh members who are supporters of this uh of this collective and what we

**[09:56]** this uh of this collective and what we

**[09:56]** this uh of this collective and what we are trying to do is to set up a system

**[09:58]** are trying to do is to set up a system

**[09:58]** are trying to do is to set up a system that allows agents from across the


### [10:00 - 11:00]

**[10:01]** that allows agents from across the

**[10:01]** that allows agents from across the world. Uh so it's a big vision uh that

**[10:03]** world. Uh so it's a big vision uh that

**[10:03]** world. Uh so it's a big vision uh that they can talk to each other without

**[10:05]** they can talk to each other without

**[10:05]** they can talk to each other without having to do heavy lifting of

**[10:06]** having to do heavy lifting of

**[10:06]** having to do heavy lifting of reconstructing your agents every time

**[10:08]** reconstructing your agents every time

**[10:08]** reconstructing your agents every time you want to integrate them with another

**[10:09]** you want to integrate them with another

**[10:09]** you want to integrate them with another agent. So it consists of identity uh

**[10:12]** agent. So it consists of identity uh

**[10:12]** agent. So it consists of identity uh schema framework for defining an agent

**[10:14]** schema framework for defining an agent

**[10:14]** schema framework for defining an agent skills and capabilities the directory

**[10:16]** skills and capabilities the directory

**[10:16]** skills and capabilities the directory where you actually store this agent and

**[10:18]** where you actually store this agent and

**[10:18]** where you actually store this agent and then how you actually compose the agents

**[10:20]** then how you actually compose the agents

**[10:20]** then how you actually compose the agents both at the semantic layer and the

**[10:21]** both at the semantic layer and the

**[10:21]** both at the semantic layer and the synthetic layer and then how do you

**[10:23]** synthetic layer and then how do you

**[10:23]** synthetic layer and then how do you observe the agents in process all of

**[10:25]** observe the agents in process all of

**[10:25]** observe the agents in process all of these are part of this collective uh

**[10:27]** these are part of this collective uh

**[10:27]** these are part of this collective uh vision as as as a group and if you want

**[10:29]** vision as as as a group and if you want

**[10:29]** vision as as as a group and if you want to learn more about this is on

**[10:30]** to learn more about this is on

**[10:30]** to learn more about this is on agency.org RG and I also have a slide

**[10:33]** agency.org RG and I also have a slide

**[10:33]** agency.org RG and I also have a slide here that kind of talks about um there's

**[10:35]** here that kind of talks about um there's

**[10:35]** here that kind of talks about um there's real code actually that you can leverage

**[10:37]** real code actually that you can leverage

**[10:37]** real code actually that you can leverage today or if you want to contribute to

**[10:39]** today or if you want to contribute to

**[10:39]** today or if you want to contribute to the code uh you can actually go there

**[10:41]** the code uh you can actually go there

**[10:41]** the code uh you can actually go there there's a GitHub repo here that you can

**[10:42]** there's a GitHub repo here that you can

**[10:42]** there's a GitHub repo here that you can go to and and you can start to

**[10:44]** go to and and you can start to

**[10:44]** go to and and you can start to contribute or use use the use the data

**[10:47]** contribute or use use the use the data

**[10:47]** contribute or use use the use the data um there's documentation available as

**[10:48]** um there's documentation available as

**[10:48]** um there's documentation available as well and there's sample applications

**[10:49]** well and there's sample applications

**[10:49]** well and there's sample applications that allows you to actually see how this

**[10:51]** that allows you to actually see how this

**[10:51]** that allows you to actually see how this works in real life and uh u we know that

**[10:54]** works in real life and uh u we know that

**[10:54]** works in real life and uh u we know that there's MCP there's A2A all of these

**[10:56]** there's MCP there's A2A all of these

**[10:56]** there's MCP there's A2A all of these protocols are becoming uh very popular

**[10:58]** protocols are becoming uh very popular

**[10:58]** protocols are becoming uh very popular uh we also integrate all of these


### [11:00 - 12:00]

**[11:00]** uh we also integrate all of these

**[11:00]** uh we also integrate all of these protocols Because the goal again is not

**[11:02]** protocols Because the goal again is not

**[11:02]** protocols Because the goal again is not to uh create something that is bespoke.

**[11:04]** to uh create something that is bespoke.

**[11:04]** to uh create something that is bespoke. We want to make it open to everyone to

**[11:06]** We want to make it open to everyone to

**[11:06]** We want to make it open to everyone to be able to create agents and be able to

**[11:08]** be able to create agents and be able to

**[11:08]** be able to create agents and be able to make these agents work in production

**[11:09]** make these agents work in production

**[11:09]** make these agents work in production environments. So back to the specific

**[11:12]** environments. So back to the specific

**[11:12]** environments. So back to the specific application we're talking about based on

**[11:15]** application we're talking about based on

**[11:15]** application we're talking about based on this framework, we delivered this set of

**[11:17]** this framework, we delivered this set of

**[11:17]** this framework, we delivered this set of agents. Uh we built a set of agents as a

**[11:20]** agents. Uh we built a set of agents as a

**[11:20]** agents. Uh we built a set of agents as a group. So we have five agents right now

**[11:21]** group. So we have five agents right now

**[11:21]** group. So we have five agents right now as part of this application. Um there's

**[11:23]** as part of this application. Um there's

**[11:24]** as part of this application. Um there's an assistant agent that's kind of the

**[11:25]** an assistant agent that's kind of the

**[11:25]** an assistant agent that's kind of the planner that kind of orchestrates things

**[11:27]** planner that kind of orchestrates things

**[11:27]** planner that kind of orchestrates things across the glo across all of these agent

**[11:29]** across the glo across all of these agent

**[11:29]** across the glo across all of these agent agents. And then we have other agents

**[11:31]** agents. And then we have other agents

**[11:31]** agents. And then we have other agents that are all based on React reasoning

**[11:32]** that are all based on React reasoning

**[11:32]** that are all based on React reasoning loops. There's one particular agent I

**[11:34]** loops. There's one particular agent I

**[11:34]** loops. There's one particular agent I want to call out here, the query agent.

**[11:36]** want to call out here, the query agent.

**[11:36]** want to call out here, the query agent. This query agent is the one that

**[11:37]** This query agent is the one that

**[11:37]** This query agent is the one that actually interacts directly with the

**[11:39]** actually interacts directly with the

**[11:39]** actually interacts directly with the knowledge graph on a regular basis. Um

**[11:42]** knowledge graph on a regular basis. Um

**[11:42]** knowledge graph on a regular basis. Um we have to fine-tune this agent because

**[11:44]** we have to fine-tune this agent because

**[11:44]** we have to fine-tune this agent because um we initially started by doing a uh

**[11:47]** um we initially started by doing a uh

**[11:47]** um we initially started by doing a uh attempting to use rack to do some

**[11:50]** attempting to use rack to do some

**[11:50]** attempting to use rack to do some querying of the knowledge graph, but

**[11:51]** querying of the knowledge graph, but

**[11:51]** querying of the knowledge graph, but that was not working out well. So we

**[11:53]** that was not working out well. So we

**[11:53]** that was not working out well. So we decided that for immediate results,

**[11:55]** decided that for immediate results,

**[11:55]** decided that for immediate results, we're going to fine-tune it. And so we

**[11:56]** we're going to fine-tune it. And so we

**[11:56]** we're going to fine-tune it. And so we did some finetuning of of the of of this

**[11:59]** did some finetuning of of the of of this

**[11:59]** did some finetuning of of the of of this agent with some schema information as


### [12:00 - 13:00]

**[12:01]** agent with some schema information as

**[12:01]** agent with some schema information as well as example queries. And so that

**[12:03]** well as example queries. And so that

**[12:03]** well as example queries. And so that helped us to actually reduce two things.

**[12:05]** helped us to actually reduce two things.

**[12:05]** helped us to actually reduce two things. The number of tokens we were burning

**[12:07]** The number of tokens we were burning

**[12:07]** The number of tokens we were burning because every time we were before that

**[12:08]** because every time we were before that

**[12:08]** because every time we were before that the AQL queries were going through all

**[12:10]** the AQL queries were going through all

**[12:10]** the AQL queries were going through all of the layers of the knowledge graph and

**[12:12]** of the layers of the knowledge graph and

**[12:12]** of the layers of the knowledge graph and in a in a reasoning loop was consuming

**[12:14]** in a in a reasoning loop was consuming

**[12:14]** in a in a reasoning loop was consuming lots of tokens and taking a lot of time

**[12:16]** lots of tokens and taking a lot of time

**[12:16]** lots of tokens and taking a lot of time for it to result to return results.

**[12:18]** for it to result to return results.

**[12:18]** for it to result to return results. After fine-tuning, we saw a drastic

**[12:20]** After fine-tuning, we saw a drastic

**[12:20]** After fine-tuning, we saw a drastic reduction in number of tokens consumed

**[12:22]** reduction in number of tokens consumed

**[12:22]** reduction in number of tokens consumed as well as the amount of time it took to

**[12:24]** as well as the amount of time it took to

**[12:24]** as well as the amount of time it took to actually come back with the results. So

**[12:25]** actually come back with the results. So

**[12:25]** actually come back with the results. So that kind of helped us there. Um so um

**[12:28]** that kind of helped us there. Um so um

**[12:28]** that kind of helped us there. Um so um I'm going to kind of pause here. I'm

**[12:29]** I'm going to kind of pause here. I'm

**[12:29]** I'm going to kind of pause here. I'm talking a lot about there's a lot of

**[12:31]** talking a lot about there's a lot of

**[12:31]** talking a lot about there's a lot of slide wear here. I want to show a quick

**[12:33]** slide wear here. I want to show a quick

**[12:33]** slide wear here. I want to show a quick demo of what this actually looks like.

**[12:35]** demo of what this actually looks like.

**[12:35]** demo of what this actually looks like. So tying together everything from the

**[12:37]** So tying together everything from the

**[12:37]** So tying together everything from the natural language interface interaction

**[12:39]** natural language interface interaction

**[12:39]** natural language interface interaction with an ITSM system to how the agents

**[12:42]** with an ITSM system to how the agents

**[12:42]** with an ITSM system to how the agents interact to how that collects

**[12:43]** interact to how that collects

**[12:43]** interact to how that collects information from knowledge graph and

**[12:45]** information from knowledge graph and

**[12:45]** information from knowledge graph and delivers results to the customer. Okay.

**[12:48]** delivers results to the customer. Okay.

**[12:48]** delivers results to the customer. Okay. So um the scenario we have here is a a

**[12:51]** So um the scenario we have here is a a

**[12:51]** So um the scenario we have here is a a network engineer wants to make a change

**[12:53]** network engineer wants to make a change

**[12:53]** network engineer wants to make a change to a firewall rule. they have to do that

**[12:55]** to a firewall rule. they have to do that

**[12:55]** to a firewall rule. they have to do that to accommodate a new server into the

**[12:57]** to accommodate a new server into the

**[12:57]** to accommodate a new server into the network. No doubt. And so what they need

**[12:58]** network. No doubt. And so what they need

**[12:58]** network. No doubt. And so what they need to do is to first of all start from


### [13:00 - 14:00]

**[13:00]** to do is to first of all start from

**[13:00]** to do is to first of all start from ITSM. So the submit a ticket in uh in

**[13:03]** ITSM. So the submit a ticket in uh in

**[13:03]** ITSM. So the submit a ticket in uh in their in

**[13:05]** their in

**[13:05]** their in service now. Now our system here the the

**[13:09]** service now. Now our system here the the

**[13:09]** service now. Now our system here the the v the UI I'm showing you right here is

**[13:10]** v the UI I'm showing you right here is

**[13:10]** v the UI I'm showing you right here is the UI of the actual system we've built

**[13:12]** the UI of the actual system we've built

**[13:12]** the UI of the actual system we've built the application we built. We have

**[13:14]** the application we built. We have

**[13:14]** the application we built. We have ingested information about the uh

**[13:18]** ingested information about the uh

**[13:18]** ingested information about the uh tickets here in natural language and so

**[13:21]** tickets here in natural language and so

**[13:21]** tickets here in natural language and so the agents here are able to actually

**[13:22]** the agents here are able to actually

**[13:22]** the agents here are able to actually start to work on this. So I'm going to

**[13:23]** start to work on this. So I'm going to

**[13:24]** start to work on this. So I'm going to play a video here just to make it uh uh

**[13:26]** play a video here just to make it uh uh

**[13:26]** play a video here just to make it uh uh more relatable. So the first thing

**[13:28]** more relatable. So the first thing

**[13:28]** more relatable. So the first thing that's happening here is that these

**[13:30]** that's happening here is that these

**[13:30]** that's happening here is that these agents uh the first agent is asking that

**[13:33]** agents uh the first agent is asking that

**[13:33]** agents uh the first agent is asking that the inter for the for the information to

**[13:36]** the inter for the for the information to

**[13:36]** the inter for the for the information to be synthesized in a summarized way so

**[13:38]** be synthesized in a summarized way so

**[13:38]** be synthesized in a summarized way so that they can understand uh what to

**[13:40]** that they can understand uh what to

**[13:40]** that they can understand uh what to quickly do. The next action that has

**[13:42]** quickly do. The next action that has

**[13:42]** quickly do. The next action that has been asked here is for you to create an

**[13:44]** been asked here is for you to create an

**[13:44]** been asked here is for you to create an impact assessment. So impact assessment

**[13:46]** impact assessment. So impact assessment

**[13:46]** impact assessment. So impact assessment here just means that I want to

**[13:47]** here just means that I want to

**[13:47]** here just means that I want to understand. So will this change have any

**[13:49]** understand. So will this change have any

**[13:49]** understand. So will this change have any implications for me beyond the immediate

**[13:52]** implications for me beyond the immediate

**[13:52]** implications for me beyond the immediate uh target area and that's going to be

**[13:55]** uh target area and that's going to be

**[13:55]** uh target area and that's going to be summarized and we are now going to ask

**[13:57]** summarized and we are now going to ask

**[13:57]** summarized and we are now going to ask the agent that is responsible for this

**[13:59]** the agent that is responsible for this

**[13:59]** the agent that is responsible for this particular task to go and attach this


### [14:00 - 15:00]

**[14:01]** particular task to go and attach this

**[14:01]** particular task to go and attach this information into the ITSM ticket. So I'm

**[14:04]** information into the ITSM ticket. So I'm

**[14:04]** information into the ITSM ticket. So I'm going to say uh attach this information

**[14:07]** going to say uh attach this information

**[14:07]** going to say uh attach this information about the impact assessment into the

**[14:10]** about the impact assessment into the

**[14:10]** about the impact assessment into the ITSM ticket. So that's been done. Now

**[14:12]** ITSM ticket. So that's been done. Now

**[14:12]** ITSM ticket. So that's been done. Now the next step is to actually create a

**[14:13]** the next step is to actually create a

**[14:13]** the next step is to actually create a test plan. So test plan is one of the

**[14:15]** test plan. So test plan is one of the

**[14:15]** test plan. So test plan is one of the biggest problems that our customers are

**[14:17]** biggest problems that our customers are

**[14:17]** biggest problems that our customers are facing. Um they they run a lot of test

**[14:19]** facing. Um they they run a lot of test

**[14:19]** facing. Um they they run a lot of test but they miss out on the right test to

**[14:21]** but they miss out on the right test to

**[14:21]** but they miss out on the right test to run. So this agents are actually able to

**[14:23]** run. So this agents are actually able to

**[14:23]** run. So this agents are actually able to reason through a lot of information

**[14:25]** reason through a lot of information

**[14:25]** reason through a lot of information about test plans across the internet and

**[14:27]** about test plans across the internet and

**[14:27]** about test plans across the internet and based on the intent that was collected

**[14:29]** based on the intent that was collected

**[14:29]** based on the intent that was collected from the service now ticket is going to

**[14:31]** from the service now ticket is going to

**[14:31]** from the service now ticket is going to come up with a list of tests that you

**[14:33]** come up with a list of tests that you

**[14:33]** come up with a list of tests that you have to run to be able to make sure that

**[14:35]** have to run to be able to make sure that

**[14:35]** have to run to be able to make sure that this firewall rule change doesn't make a

**[14:37]** this firewall rule change doesn't make a

**[14:37]** this firewall rule change doesn't make a big impact or create problems in

**[14:39]** big impact or create problems in

**[14:39]** big impact or create problems in production environment. So as you can

**[14:40]** production environment. So as you can

**[14:40]** production environment. So as you can see here, this agent has gone ahead and

**[14:42]** see here, this agent has gone ahead and

**[14:42]** see here, this agent has gone ahead and actually listed all of the test cases

**[14:43]** actually listed all of the test cases

**[14:44]** actually listed all of the test cases that needs to be run and the expected

**[14:45]** that needs to be run and the expected

**[14:45]** that needs to be run and the expected results for each of the tests. So we're

**[14:47]** results for each of the tests. So we're

**[14:47]** results for each of the tests. So we're going to ask this agent to attach this

**[14:49]** going to ask this agent to attach this

**[14:50]** going to ask this agent to attach this information again back to the ITSM

**[14:51]** information again back to the ITSM

**[14:52]** information again back to the ITSM ticket because that's where the approval

**[14:54]** ticket because that's where the approval

**[14:54]** ticket because that's where the approval board needs to see this information

**[14:55]** board needs to see this information

**[14:55]** board needs to see this information before they implement before the

**[14:56]** before they implement before the

**[14:56]** before they implement before the approved implementation of this change

**[14:58]** approved implementation of this change

**[14:58]** approved implementation of this change in production environment. So we can see


### [15:00 - 16:00]

**[15:01]** in production environment. So we can see

**[15:01]** in production environment. So we can see here that that information has now been

**[15:02]** here that that information has now been

**[15:02]** here that that information has now been attached back by this agent to the ITSM

**[15:05]** attached back by this agent to the ITSM

**[15:05]** attached back by this agent to the ITSM tickets. So two separate systems but

**[15:06]** tickets. So two separate systems but

**[15:06]** tickets. So two separate systems but agents talking to each other. Now the

**[15:09]** agents talking to each other. Now the

**[15:09]** agents talking to each other. Now the next step is actually run a test on one

**[15:11]** next step is actually run a test on one

**[15:11]** next step is actually run a test on one of these test cases. So um in this case

**[15:14]** of these test cases. So um in this case

**[15:14]** of these test cases. So um in this case the configuration file that is going to

**[15:15]** the configuration file that is going to

**[15:15]** the configuration file that is going to be used to make the change in the

**[15:17]** be used to make the change in the

**[15:17]** be used to make the change in the firewall is sitting in the GitHub repo.

**[15:19]** firewall is sitting in the GitHub repo.

**[15:19]** firewall is sitting in the GitHub repo. And so we're going to do a pull request

**[15:20]** And so we're going to do a pull request

**[15:20]** And so we're going to do a pull request of that config file and going to take

**[15:23]** of that config file and going to take

**[15:23]** of that config file and going to take that information. So this is the GitHub

**[15:24]** that information. So this is the GitHub

**[15:24]** that information. So this is the GitHub repo where the where we're going to do a

**[15:26]** repo where the where we're going to do a

**[15:26]** repo where the where we're going to do a pull request. We're going to take the

**[15:28]** pull request. We're going to take the

**[15:28]** pull request. We're going to take the link for that pull request and paste it

**[15:29]** link for that pull request and paste it

**[15:30]** link for that pull request and paste it in the ticket

**[15:32]** in the ticket

**[15:32]** in the ticket and so that when the executor execution

**[15:34]** and so that when the executor execution

**[15:34]** and so that when the executor execution agent starts doing its job is actually

**[15:36]** agent starts doing its job is actually

**[15:36]** agent starts doing its job is actually going to pull from that and use it to

**[15:38]** going to pull from that and use it to

**[15:38]** going to pull from that and use it to run this test. So um at this moment we

**[15:41]** run this test. So um at this moment we

**[15:41]** run this test. So um at this moment we we have we're going to start running the

**[15:42]** we have we're going to start running the

**[15:42]** we have we're going to start running the test. We're going to ask this agent to

**[15:44]** test. We're going to ask this agent to

**[15:44]** test. We're going to ask this agent to go ahead and actually run the test and

**[15:47]** go ahead and actually run the test and

**[15:47]** go ahead and actually run the test and execute on this test. And so um I have

**[15:50]** execute on this test. And so um I have

**[15:50]** execute on this test. And so um I have attached the change sorry I don't have

**[15:52]** attached the change sorry I don't have

**[15:52]** attached the change sorry I don't have my glasses. I've attached my uh change

**[15:55]** my glasses. I've attached my uh change

**[15:55]** my glasses. I've attached my uh change candidates to the ticket. Can you go

**[15:58]** candidates to the ticket. Can you go

**[15:58]** candidates to the ticket. Can you go ahead and run the test? So what is going


### [16:00 - 17:00]

**[16:00]** ahead and run the test? So what is going

**[16:00]** ahead and run the test? So what is going to happen here is if you look on the

**[16:01]** to happen here is if you look on the

**[16:01]** to happen here is if you look on the right hand side of this screen here, a

**[16:03]** right hand side of this screen here, a

**[16:03]** right hand side of this screen here, a series of things are happening. The

**[16:04]** series of things are happening. The

**[16:04]** series of things are happening. The first thing is that the this agent

**[16:06]** first thing is that the this agent

**[16:06]** first thing is that the this agent called the executor agent goes looks at

**[16:08]** called the executor agent goes looks at

**[16:08]** called the executor agent goes looks at the test cases and then it goes into the

**[16:10]** the test cases and then it goes into the

**[16:10]** the test cases and then it goes into the knowledge graph and it's going to go

**[16:12]** knowledge graph and it's going to go

**[16:12]** knowledge graph and it's going to go ahead and actually do a snapshot of the

**[16:15]** ahead and actually do a snapshot of the

**[16:15]** ahead and actually do a snapshot of the most recent visual or most recent

**[16:17]** most recent visual or most recent

**[16:17]** most recent visual or most recent information about the network. is now

**[16:19]** information about the network. is now

**[16:19]** information about the network. is now going to take the pull request that it

**[16:21]** going to take the pull request that it

**[16:21]** going to take the pull request that it pulled from GitHub, the snapshot it just

**[16:24]** pulled from GitHub, the snapshot it just

**[16:24]** pulled from GitHub, the snapshot it just took from the knowledge graph. It's

**[16:26]** took from the knowledge graph. It's

**[16:26]** took from the knowledge graph. It's going to compute it together and then

**[16:28]** going to compute it together and then

**[16:28]** going to compute it together and then run all of the individual test one at a

**[16:30]** run all of the individual test one at a

**[16:30]** run all of the individual test one at a time. So we can see that it's running

**[16:31]** time. So we can see that it's running

**[16:31]** time. So we can see that it's running the test one test, test test one, test

**[16:33]** the test one test, test test one, test

**[16:33]** the test one test, test test one, test two, test three, test four. So all of

**[16:34]** two, test three, test four. So all of

**[16:34]** two, test three, test four. So all of this is happening in what we call a

**[16:36]** this is happening in what we call a

**[16:36]** this is happening in what we call a digital twin. So a digital twin again is

**[16:38]** digital twin. So a digital twin again is

**[16:38]** digital twin. So a digital twin again is a cons combination of the knowledge

**[16:40]** a cons combination of the knowledge

**[16:40]** a cons combination of the knowledge graph, a set of tools that you can use

**[16:42]** graph, a set of tools that you can use

**[16:42]** graph, a set of tools that you can use to run the test. So an an example of a

**[16:44]** to run the test. So an an example of a

**[16:44]** to run the test. So an an example of a tool here could be batfish or could be

**[16:46]** tool here could be batfish or could be

**[16:46]** tool here could be batfish or could be routnet or some other tools that you use

**[16:48]** routnet or some other tools that you use

**[16:48]** routnet or some other tools that you use for engineering purp for network

**[16:49]** for engineering purp for network

**[16:49]** for engineering purp for network engineering purposes. So once all of

**[16:51]** engineering purposes. So once all of

**[16:51]** engineering purposes. So once all of these tests are completed uh this tool

**[16:54]** these tests are completed uh this tool

**[16:54]** these tests are completed uh this tool actually is going to this agent is going

**[16:56]** actually is going to this agent is going

**[16:56]** actually is going to this agent is going to now generate a report about the test

**[16:57]** to now generate a report about the test

**[16:57]** to now generate a report about the test results. So um we give it some time to


### [17:00 - 18:00]

**[17:00]** results. So um we give it some time to

**[17:00]** results. So um we give it some time to run through this. It's still running the

**[17:01]** run through this. It's still running the

**[17:01]** run through this. It's still running the tests but when once it concludes all of

**[17:03]** tests but when once it concludes all of

**[17:03]** tests but when once it concludes all of the tests it's going to report actually

**[17:06]** the tests it's going to report actually

**[17:06]** the tests it's going to report actually uh the test results are. So which

**[17:07]** uh the test results are. So which

**[17:07]** uh the test results are. So which results which tests actually passed

**[17:09]** results which tests actually passed

**[17:09]** results which tests actually passed which ones failed. for the ones that

**[17:11]** which ones failed. for the ones that

**[17:11]** which ones failed. for the ones that have failed, he's going to make some

**[17:12]** have failed, he's going to make some

**[17:12]** have failed, he's going to make some recommendations on what you can do to go

**[17:14]** recommendations on what you can do to go

**[17:14]** recommendations on what you can do to go and fix the problem. Um um I'm going to

**[17:16]** and fix the problem. Um um I'm going to

**[17:16]** and fix the problem. Um um I'm going to skip to the front here to just quickly

**[17:18]** skip to the front here to just quickly

**[17:18]** skip to the front here to just quickly get this on uh done quickly because of

**[17:20]** get this on uh done quickly because of

**[17:20]** get this on uh done quickly because of time. Um so um it's attached the results

**[17:25]** time. Um so um it's attached the results

**[17:25]** time. Um so um it's attached the results to the ticket and this is the report

**[17:27]** to the ticket and this is the report

**[17:27]** to the ticket and this is the report that it's spitting out in terms of this

**[17:29]** that it's spitting out in terms of this

**[17:29]** that it's spitting out in terms of this is the report for the test that were

**[17:30]** is the report for the test that were

**[17:30]** is the report for the test that were run. So this execution agent actually

**[17:32]** run. So this execution agent actually

**[17:32]** run. So this execution agent actually created a report about all of the

**[17:34]** created a report about all of the

**[17:34]** created a report about all of the different test cases that were run by

**[17:36]** different test cases that were run by

**[17:36]** different test cases that were run by the system. So um very quick short demo

**[17:39]** the system. So um very quick short demo

**[17:39]** the system. So um very quick short demo here. Uh there's a lot of detail behind

**[17:41]** here. Uh there's a lot of detail behind

**[17:41]** here. Uh there's a lot of detail behind the scenes but I can answer some

**[17:42]** the scenes but I can answer some

**[17:42]** the scenes but I can answer some questions offline. Um the the the couple

**[17:45]** questions offline. Um the the the couple

**[17:45]** questions offline. Um the the the couple of things I want to leave us with is

**[17:46]** of things I want to leave us with is

**[17:46]** of things I want to leave us with is that uh before I go to the end of this

**[17:48]** that uh before I go to the end of this

**[17:48]** that uh before I go to the end of this uh is that evaluation is very critical

**[17:50]** uh is that evaluation is very critical

**[17:50]** uh is that evaluation is very critical here for us to be to able to understand

**[17:53]** here for us to be to able to understand

**[17:53]** here for us to be to able to understand how this delivers value to customers. Um

**[17:55]** how this delivers value to customers. Um

**[17:55]** how this delivers value to customers. Um we're looking at a variety of things

**[17:57]** we're looking at a variety of things

**[17:57]** we're looking at a variety of things here. So the agents themselves the

**[17:59]** here. So the agents themselves the

**[17:59]** here. So the agents themselves the knowledge graph digital twin and we're


### [18:00 - 19:00]

**[18:02]** knowledge graph digital twin and we're

**[18:02]** knowledge graph digital twin and we're looking at the what can we actually

**[18:04]** looking at the what can we actually

**[18:04]** looking at the what can we actually measure quantifiably. Now for the

**[18:06]** measure quantifiably. Now for the

**[18:06]** measure quantifiably. Now for the knowledge graph, we're looking at

**[18:07]** knowledge graph, we're looking at

**[18:07]** knowledge graph, we're looking at extrinsic

**[18:09]** extrinsic

**[18:09]** extrinsic metrics particularly not intrinsic ones

**[18:11]** metrics particularly not intrinsic ones

**[18:11]** metrics particularly not intrinsic ones because we want to map this back to the

**[18:12]** because we want to map this back to the

**[18:12]** because we want to map this back to the customer's use case. So this is the

**[18:15]** customer's use case. So this is the

**[18:15]** customer's use case. So this is the summary of the of what we see in terms

**[18:16]** summary of the of what we see in terms

**[18:16]** summary of the of what we see in terms of evaluation metrics. Um we are still

**[18:19]** of evaluation metrics. Um we are still

**[18:19]** of evaluation metrics. Um we are still learning this is a this is for for now

**[18:21]** learning this is a this is for for now

**[18:21]** learning this is a this is for for now it's it's an MVP u but what we are

**[18:24]** it's it's an MVP u but what we are

**[18:24]** it's it's an MVP u but what we are learning so far is that those two key

**[18:25]** learning so far is that those two key

**[18:25]** learning so far is that those two key building blocks the knowledge graph and

**[18:28]** building blocks the knowledge graph and

**[18:28]** building blocks the knowledge graph and the open framework for building agents

**[18:30]** the open framework for building agents

**[18:30]** the open framework for building agents is very critical for us to actually

**[18:31]** is very critical for us to actually

**[18:31]** is very critical for us to actually build a scalable system for our

**[18:33]** build a scalable system for our

**[18:33]** build a scalable system for our customers. And so, um, I'm going to

**[18:35]** customers. And so, um, I'm going to

**[18:36]** customers. And so, um, I'm going to stop. It's 8 seconds to go. Thank you

**[18:37]** stop. It's 8 seconds to go. Thank you

**[18:38]** stop. It's 8 seconds to go. Thank you for listening to me. And then if you

**[18:39]** for listening to me. And then if you

**[18:39]** for listening to me. And then if you have questions, I'll be out there.


