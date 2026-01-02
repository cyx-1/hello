# Backlog.md- Terminal Kanban Board for Managing Tasks with AI Agents — Alex Gavrilescu, Funstage

**Video URL:** https://www.youtube.com/watch?v=zMXKhhwiCIc

---

## Full Transcript

### [00:00 - 01:00]

**[00:02]** Have you ever had your agent working for

**[00:02]** Have you ever had your agent working for almost one hour only to understand that

**[00:05]** almost one hour only to understand that

**[00:05]** almost one hour only to understand that he went in the wrong direction or in the

**[00:08]** he went in the wrong direction or in the

**[00:08]** he went in the wrong direction or in the middle of something very important he

**[00:10]** middle of something very important he

**[00:10]** middle of something very important he ran out of context window? Me too.

**[00:13]** ran out of context window? Me too.

**[00:13]** ran out of context window? Me too. That's why in the last months I

**[00:15]** That's why in the last months I

**[00:15]** That's why in the last months I developed a workflow that consists in

**[00:18]** developed a workflow that consists in

**[00:18]** developed a workflow that consists in dividing a big feature into smaller

**[00:20]** dividing a big feature into smaller

**[00:20]** dividing a big feature into smaller markdown tasks.

**[00:23]** markdown tasks.

**[00:23]** markdown tasks. Hi, I'm Alex Gavesco and I'm going to

**[00:25]** Hi, I'm Alex Gavesco and I'm going to

**[00:26]** Hi, I'm Alex Gavesco and I'm going to present backlog MD, a tool for project

**[00:28]** present backlog MD, a tool for project

**[00:28]** present backlog MD, a tool for project management for AI agents and humans.

**[00:33]** management for AI agents and humans.

**[00:33]** management for AI agents and humans. Okay, let's start. So, have you ever

**[00:36]** Okay, let's start. So, have you ever

**[00:36]** Okay, let's start. So, have you ever seen a terminal cand board? Well, when I

**[00:39]** seen a terminal cand board? Well, when I

**[00:39]** seen a terminal cand board? Well, when I started working on backlog MD, I

**[00:41]** started working on backlog MD, I

**[00:41]** started working on backlog MD, I couldn't find any. So, I had to build it

**[00:44]** couldn't find any. So, I had to build it

**[00:44]** couldn't find any. So, I had to build it myself. We have a full comban board

**[00:47]** myself. We have a full comban board

**[00:47]** myself. We have a full comban board directly in your terminal. And here we

**[00:50]** directly in your terminal. And here we

**[00:50]** directly in your terminal. And here we can see our tasks for the current

**[00:53]** can see our tasks for the current

**[00:53]** can see our tasks for the current project. And we can actually see the

**[00:55]** project. And we can actually see the

**[00:56]** project. And we can actually see the details of the task directly in our

**[00:58]** details of the task directly in our

**[00:58]** details of the task directly in our terminal. We can see the description and


### [01:00 - 02:00]

**[01:01]** terminal. We can see the description and

**[01:01]** terminal. We can see the description and acceptance criterias of tasks that are

**[01:03]** acceptance criterias of tasks that are

**[01:03]** acceptance criterias of tasks that are still to be uh developed. We have the in

**[01:06]** still to be uh developed. We have the in

**[01:06]** still to be uh developed. We have the in progress and the done columns as well

**[01:09]** progress and the done columns as well

**[01:09]** progress and the done columns as well where we can see what has been

**[01:10]** where we can see what has been

**[01:10]** where we can see what has been implemented. In this case, we can see

**[01:13]** implemented. In this case, we can see

**[01:13]** implemented. In this case, we can see the acceptance criterias were

**[01:14]** the acceptance criterias were

**[01:14]** the acceptance criterias were implemented and someone left some

**[01:17]** implemented and someone left some

**[01:17]** implemented and someone left some implementation notes. But one of the

**[01:19]** implementation notes. But one of the

**[01:19]** implementation notes. But one of the features I always wanted to have in

**[01:21]** features I always wanted to have in

**[01:21]** features I always wanted to have in Backlog MD is the ability to move tasks

**[01:24]** Backlog MD is the ability to move tasks

**[01:24]** Backlog MD is the ability to move tasks between status columns and to reorder

**[01:27]** between status columns and to reorder

**[01:27]** between status columns and to reorder tasks within the same column. So let's

**[01:30]** tasks within the same column. So let's

**[01:30]** tasks within the same column. So let's build it with cloud code.

**[01:33]** build it with cloud code.

**[01:33]** build it with cloud code. Before we can build it with cloud code,

**[01:35]** Before we can build it with cloud code,

**[01:35]** Before we can build it with cloud code, we need to have clear requirements.

**[01:38]** we need to have clear requirements.

**[01:38]** we need to have clear requirements. This is important for humans but also

**[01:40]** This is important for humans but also

**[01:40]** This is important for humans but also for AI agents. So first thing to do is

**[01:44]** for AI agents. So first thing to do is

**[01:44]** for AI agents. So first thing to do is to we want to press M to toggle the move

**[01:46]** to we want to press M to toggle the move

**[01:46]** to we want to press M to toggle the move mode. Then the current task will be

**[01:48]** mode. Then the current task will be

**[01:48]** mode. Then the current task will be highlighted and we know which task is

**[01:51]** highlighted and we know which task is

**[01:51]** highlighted and we know which task is going to be moved. We can use the arrow

**[01:54]** going to be moved. We can use the arrow

**[01:54]** going to be moved. We can use the arrow keys up and down to move the task within

**[01:57]** keys up and down to move the task within

**[01:57]** keys up and down to move the task within the same column and change the its

**[01:58]** the same column and change the its

**[01:58]** the same column and change the its order. Or we can go left and right and


### [02:00 - 03:00]

**[02:02]** order. Or we can go left and right and

**[02:02]** order. Or we can go left and right and this will change the status of the task.

**[02:05]** this will change the status of the task.

**[02:05]** this will change the status of the task. If we press M or enter, we will commit

**[02:07]** If we press M or enter, we will commit

**[02:08]** If we press M or enter, we will commit this move. And if we want to cancel, we

**[02:10]** this move. And if we want to cancel, we

**[02:10]** this move. And if we want to cancel, we will press ask. And the user should be

**[02:13]** will press ask. And the user should be

**[02:13]** will press ask. And the user should be informed uh how this functionality works

**[02:16]** informed uh how this functionality works

**[02:16]** informed uh how this functionality works by showing the button in the footer.

**[02:20]** by showing the button in the footer.

**[02:20]** by showing the button in the footer. So let's have cloud actually implement

**[02:23]** So let's have cloud actually implement

**[02:23]** So let's have cloud actually implement the task uh uh the task. But first the

**[02:26]** the task uh uh the task. But first the

**[02:26]** the task uh uh the task. But first the task has to be created. So we tell given

**[02:30]** task has to be created. So we tell given

**[02:30]** task has to be created. So we tell given this requirements to create a task.

**[02:34]** this requirements to create a task.

**[02:34]** this requirements to create a task. Now clude the first thing that it will

**[02:37]** Now clude the first thing that it will

**[02:37]** Now clude the first thing that it will do is going to search for existing

**[02:39]** do is going to search for existing

**[02:39]** do is going to search for existing tasks.

**[02:41]** tasks.

**[02:41]** tasks. Actually the first thing that he does he

**[02:43]** Actually the first thing that he does he

**[02:43]** Actually the first thing that he does he needs to understand how backlog works

**[02:44]** needs to understand how backlog works

**[02:44]** needs to understand how backlog works and what is backlog because clude acts

**[02:47]** and what is backlog because clude acts

**[02:47]** and what is backlog because clude acts as a developer that has been re uh just

**[02:50]** as a developer that has been re uh just

**[02:50]** as a developer that has been re uh just on boarded on our project and needs to

**[02:52]** on boarded on our project and needs to

**[02:52]** on boarded on our project and needs to understand how our project works. So he

**[02:55]** understand how our project works. So he

**[02:55]** understand how our project works. So he first reads about backlog and then he

**[02:58]** first reads about backlog and then he

**[02:58]** first reads about backlog and then he reads about how to create tasks


### [03:00 - 04:00]

**[03:00]** reads about how to create tasks

**[03:00]** reads about how to create tasks correctly.

**[03:01]** correctly.

**[03:01]** correctly. Afterwards he creates the task. We can

**[03:04]** Afterwards he creates the task. We can

**[03:04]** Afterwards he creates the task. We can see here the task has been completed and

**[03:07]** see here the task has been completed and

**[03:07]** see here the task has been completed and now let's check uh what we what is

**[03:10]** now let's check uh what we what is

**[03:10]** now let's check uh what we what is there. So this is how it looks. Backlog

**[03:14]** there. So this is how it looks. Backlog

**[03:14]** there. So this is how it looks. Backlog empty tasks are stored as markdown files

**[03:16]** empty tasks are stored as markdown files

**[03:16]** empty tasks are stored as markdown files in your repository. We have a front

**[03:19]** in your repository. We have a front

**[03:19]** in your repository. We have a front matter section with meta task metadata

**[03:22]** matter section with meta task metadata

**[03:22]** matter section with meta task metadata such as task ID, title, labels and other

**[03:26]** such as task ID, title, labels and other

**[03:26]** such as task ID, title, labels and other metadata fields. We have the description

**[03:29]** metadata fields. We have the description

**[03:29]** metadata fields. We have the description and let's read if Claude uh actually

**[03:31]** and let's read if Claude uh actually

**[03:31]** and let's read if Claude uh actually understood why what is the purpose of

**[03:33]** understood why what is the purpose of

**[03:33]** understood why what is the purpose of this task.

**[03:35]** this task.

**[03:35]** this task. Add the move mode feature in the twoe

**[03:37]** Add the move mode feature in the twoe

**[03:38]** Add the move mode feature in the twoe comban board that allows users to

**[03:40]** comban board that allows users to

**[03:40]** comban board that allows users to interactively reorder tasks within

**[03:43]** interactively reorder tasks within

**[03:43]** interactively reorder tasks within columns and move tasks between status

**[03:46]** columns and move tasks between status

**[03:46]** columns and move tasks between status columns using keyboard navigation. This

**[03:49]** columns using keyboard navigation. This

**[03:49]** columns using keyboard navigation. This provides a more intuitive way to

**[03:51]** provides a more intuitive way to

**[03:51]** provides a more intuitive way to reorganize tasks without needing to use

**[03:54]** reorganize tasks without needing to use

**[03:54]** reorganize tasks without needing to use CLI commands or edit files directly. So

**[03:57]** CLI commands or edit files directly. So

**[03:57]** CLI commands or edit files directly. So we can confirm that cloud really

**[03:59]** we can confirm that cloud really

**[03:59]** we can confirm that cloud really understand why we want to build this


### [04:00 - 05:00]

**[04:02]** understand why we want to build this

**[04:02]** understand why we want to build this feature. The next section of backlog

**[04:04]** feature. The next section of backlog

**[04:04]** feature. The next section of backlog tasks is the acceptance criteria.

**[04:08]** tasks is the acceptance criteria.

**[04:08]** tasks is the acceptance criteria. And here we can have really clear uh

**[04:12]** And here we can have really clear uh

**[04:12]** And here we can have really clear uh acceptance criteria that define how the

**[04:16]** acceptance criteria that define how the

**[04:16]** acceptance criteria that define how the task the feature should behave and they

**[04:19]** task the feature should behave and they

**[04:19]** task the feature should behave and they should be testable and easily uh

**[04:22]** should be testable and easily uh

**[04:22]** should be testable and easily uh verifiable.

**[04:27]** This is uh this is the first review

**[04:27]** This is uh this is the first review point. This is the moment where you can

**[04:29]** point. This is the moment where you can

**[04:29]** point. This is the moment where you can actually understand if the AI agent has

**[04:32]** actually understand if the AI agent has

**[04:32]** actually understand if the AI agent has understood your intent and will do a

**[04:35]** understood your intent and will do a

**[04:35]** understood your intent and will do a good task.

**[04:38]** good task.

**[04:38]** good task. The next step is the implementation

**[04:40]** The next step is the implementation

**[04:40]** The next step is the implementation plan. So we want the AI agent to come up

**[04:44]** plan. So we want the AI agent to come up

**[04:44]** plan. So we want the AI agent to come up with an implementation plan because he

**[04:48]** with an implementation plan because he

**[04:48]** with an implementation plan because he must understand really well the

**[04:50]** must understand really well the

**[04:50]** must understand really well the description and the acceptance criteria.

**[04:53]** description and the acceptance criteria.

**[04:53]** description and the acceptance criteria. It can uh check the documentation and

**[04:57]** It can uh check the documentation and

**[04:57]** It can uh check the documentation and internet and search also the existing

**[04:59]** internet and search also the existing

**[04:59]** internet and search also the existing codebase to understand where to put this


### [05:00 - 06:00]

**[05:02]** codebase to understand where to put this

**[05:02]** codebase to understand where to put this feature

**[05:04]** feature

**[05:04]** feature and then at the end it will write an

**[05:06]** and then at the end it will write an

**[05:06]** and then at the end it will write an implementation plan. So let's have this

**[05:08]** implementation plan. So let's have this

**[05:08]** implementation plan. So let's have this done actually by cloud.

**[05:11]** done actually by cloud.

**[05:11]** done actually by cloud. So we give him the instruction to create

**[05:13]** So we give him the instruction to create

**[05:13]** So we give him the instruction to create an implementation plan according to

**[05:15]** an implementation plan according to

**[05:15]** an implementation plan according to backlog MD workflow for the task that he

**[05:17]** backlog MD workflow for the task that he

**[05:17]** backlog MD workflow for the task that he just it just created.

**[05:20]** just it just created.

**[05:20]** just it just created. So we wait a bit. Uh this will take some

**[05:24]** So we wait a bit. Uh this will take some

**[05:24]** So we wait a bit. Uh this will take some time. Of course he has to really uh find

**[05:27]** time. Of course he has to really uh find

**[05:27]** time. Of course he has to really uh find what files have to be edited. Maybe look

**[05:30]** what files have to be edited. Maybe look

**[05:30]** what files have to be edited. Maybe look up on the internet for some

**[05:31]** up on the internet for some

**[05:31]** up on the internet for some documentation and existing documentation

**[05:34]** documentation and existing documentation

**[05:34]** documentation and existing documentation in our project. In the meantime, let's

**[05:36]** in our project. In the meantime, let's

**[05:36]** in our project. In the meantime, let's explain how this works under the hood.

**[05:40]** explain how this works under the hood.

**[05:40]** explain how this works under the hood. So backlog MD uses uh an MCP server to

**[05:45]** So backlog MD uses uh an MCP server to

**[05:45]** So backlog MD uses uh an MCP server to expose information instructions for the

**[05:48]** expose information instructions for the

**[05:48]** expose information instructions for the M for the AI agents but also tools. The

**[05:51]** M for the AI agents but also tools. The

**[05:51]** M for the AI agents but also tools. The most important part is the resources. So

**[05:55]** most important part is the resources. So

**[05:55]** most important part is the resources. So this is a special feature of MCP that

**[05:57]** this is a special feature of MCP that

**[05:57]** this is a special feature of MCP that backlog MD uses to instruct the agents


### [06:00 - 07:00]

**[06:00]** backlog MD uses to instruct the agents

**[06:00]** backlog MD uses to instruct the agents how to use backlog MD. The first

**[06:02]** how to use backlog MD. The first

**[06:02]** how to use backlog MD. The first resource is the workflow overview. Here

**[06:05]** resource is the workflow overview. Here

**[06:05]** resource is the workflow overview. Here we're telling the AI agents what is

**[06:07]** we're telling the AI agents what is

**[06:07]** we're telling the AI agents what is backlog and what can be used for.

**[06:11]** backlog and what can be used for.

**[06:11]** backlog and what can be used for. And also this overview will present the

**[06:13]** And also this overview will present the

**[06:13]** And also this overview will present the next resources that are available which

**[06:15]** next resources that are available which

**[06:15]** next resources that are available which are the task creation guide letting the

**[06:18]** are the task creation guide letting the

**[06:18]** are the task creation guide letting the AI agents know how to create tasks and

**[06:21]** AI agents know how to create tasks and

**[06:21]** AI agents know how to create tasks and what fields are required and which ones

**[06:22]** what fields are required and which ones

**[06:22]** what fields are required and which ones are optional.

**[06:24]** are optional.

**[06:24]** are optional. the task execution guide. When an AI

**[06:27]** the task execution guide. When an AI

**[06:27]** the task execution guide. When an AI agents want to implement the task, what

**[06:29]** agents want to implement the task, what

**[06:29]** agents want to implement the task, what should be done at this point? Such as

**[06:32]** should be done at this point? Such as

**[06:32]** should be done at this point? Such as putting the task into in progress uh

**[06:34]** putting the task into in progress uh

**[06:34]** putting the task into in progress uh status and assigning the tasks to

**[06:36]** status and assigning the tasks to

**[06:36]** status and assigning the tasks to themsel. And the last guide is about

**[06:40]** themsel. And the last guide is about

**[06:40]** themsel. And the last guide is about completing a task and uh checking the

**[06:43]** completing a task and uh checking the

**[06:43]** completing a task and uh checking the acceptance criterias if they are all

**[06:45]** acceptance criterias if they are all

**[06:45]** acceptance criterias if they are all actually implemented correctly and

**[06:48]** actually implemented correctly and

**[06:48]** actually implemented correctly and checking all of the other requirements

**[06:50]** checking all of the other requirements

**[06:50]** checking all of the other requirements for the definition of done that we

**[06:52]** for the definition of done that we

**[06:52]** for the definition of done that we specified.

**[06:54]** specified.

**[06:54]** specified. And then how can agents use backlog?

**[06:57]** And then how can agents use backlog?

**[06:57]** And then how can agents use backlog? Well, via MCP tools. So backlog MD


### [07:00 - 08:00]

**[07:00]** Well, via MCP tools. So backlog MD

**[07:00]** Well, via MCP tools. So backlog MD server will expose certain tools for

**[07:03]** server will expose certain tools for

**[07:03]** server will expose certain tools for their agents so that they can run

**[07:05]** their agents so that they can run

**[07:05]** their agents so that they can run backlog commands directly and natively.

**[07:09]** backlog commands directly and natively.

**[07:09]** backlog commands directly and natively. For example, one of them is searching

**[07:11]** For example, one of them is searching

**[07:11]** For example, one of them is searching tasks. Before creating new task, AI

**[07:14]** tasks. Before creating new task, AI

**[07:14]** tasks. Before creating new task, AI agents should search if that task

**[07:16]** agents should search if that task

**[07:16]** agents should search if that task already exists.

**[07:19]** already exists.

**[07:19]** already exists. It should they should be able to view

**[07:21]** It should they should be able to view

**[07:21]** It should they should be able to view the details of these tasks. They should

**[07:23]** the details of these tasks. They should

**[07:23]** the details of these tasks. They should be able to create tasks and update tasks

**[07:27]** be able to create tasks and update tasks

**[07:27]** be able to create tasks and update tasks and update their acceptance criteria and

**[07:29]** and update their acceptance criteria and

**[07:29]** and update their acceptance criteria and put them into them.

**[07:31]** put them into them.

**[07:31]** put them into them. Okay, let's continue. Now, uh hopefully

**[07:36]** Okay, let's continue. Now, uh hopefully

**[07:36]** Okay, let's continue. Now, uh hopefully cloud finished creating the

**[07:37]** cloud finished creating the

**[07:37]** cloud finished creating the implementation plan. So, let's check

**[07:39]** implementation plan. So, let's check

**[07:39]** implementation plan. So, let's check what we have.

**[07:41]** what we have.

**[07:41]** what we have. So, we have an architecture overview. We

**[07:44]** So, we have an architecture overview. We

**[07:44]** So, we have an architecture overview. We have implementation steps and then he

**[07:47]** have implementation steps and then he

**[07:47]** have implementation steps and then he actually starts enumerating which files

**[07:50]** actually starts enumerating which files

**[07:50]** actually starts enumerating which files should be touched and modified and the

**[07:53]** should be touched and modified and the

**[07:54]** should be touched and modified and the how. And here we have the the second and

**[07:58]** how. And here we have the the second and

**[07:58]** how. And here we have the the second and most important review step. This is the


### [08:00 - 09:00]

**[08:00]** most important review step. This is the

**[08:00]** most important review step. This is the moment where a senior software engineer

**[08:03]** moment where a senior software engineer

**[08:03]** moment where a senior software engineer can really understand if the agent is

**[08:05]** can really understand if the agent is

**[08:05]** can really understand if the agent is going is the in the right direction. So

**[08:08]** going is the in the right direction. So

**[08:08]** going is the in the right direction. So it is very important at this point to

**[08:10]** it is very important at this point to

**[08:10]** it is very important at this point to double check if everything is all right.

**[08:12]** double check if everything is all right.

**[08:12]** double check if everything is all right. So now uh for the purpose of this

**[08:15]** So now uh for the purpose of this

**[08:15]** So now uh for the purpose of this presentation let's go directly to the

**[08:18]** presentation let's go directly to the

**[08:18]** presentation let's go directly to the implementation part.

**[08:21]** implementation part.

**[08:21]** implementation part. So for the execution we want to have the

**[08:23]** So for the execution we want to have the

**[08:23]** So for the execution we want to have the agent write the code for us. So Cloex

**[08:28]** agent write the code for us. So Cloex

**[08:28]** agent write the code for us. So Cloex or Gemini or Kuso they can all work with

**[08:31]** or Gemini or Kuso they can all work with

**[08:31]** or Gemini or Kuso they can all work with backlog MD and they should learn about

**[08:34]** backlog MD and they should learn about

**[08:34]** backlog MD and they should learn about the task the description the acceptance

**[08:36]** the task the description the acceptance

**[08:36]** the task the description the acceptance criteria and the plan

**[08:39]** criteria and the plan

**[08:40]** criteria and the plan and what does develop the feature means

**[08:42]** and what does develop the feature means

**[08:42]** and what does develop the feature means means implement all of the acceptance

**[08:44]** means implement all of the acceptance

**[08:44]** means implement all of the acceptance criterias and putting the task into done

**[08:47]** criterias and putting the task into done

**[08:47]** criterias and putting the task into done when the definition of done is

**[08:49]** when the definition of done is

**[08:49]** when the definition of done is fulfilled.

**[08:51]** fulfilled.

**[08:51]** fulfilled. So, let's have Claude actually implement

**[08:53]** So, let's have Claude actually implement

**[08:53]** So, let's have Claude actually implement it.

**[08:56]** it.

**[08:56]** it. This is going to take a while. So, we're

**[08:58]** This is going to take a while. So, we're

**[08:58]** This is going to take a while. So, we're going to pause this video and come back

**[08:59]** going to pause this video and come back

**[08:59]** going to pause this video and come back when Claude has finished and we're done.


### [09:00 - 10:00]

**[09:04]** when Claude has finished and we're done.

**[09:04]** when Claude has finished and we're done. Uh before checking um what Claude has

**[09:07]** Uh before checking um what Claude has

**[09:07]** Uh before checking um what Claude has implemented, let's have a quick review

**[09:10]** implemented, let's have a quick review

**[09:10]** implemented, let's have a quick review of the backlog workflow. So, as a human,

**[09:14]** of the backlog workflow. So, as a human,

**[09:14]** of the backlog workflow. So, as a human, I want to create tasks. I want to

**[09:17]** I want to create tasks. I want to

**[09:17]** I want to create tasks. I want to develop features in my project. So

**[09:19]** develop features in my project. So

**[09:19]** develop features in my project. So normally I could create task directly

**[09:22]** normally I could create task directly

**[09:22]** normally I could create task directly using backlog CLI commands but it is

**[09:25]** using backlog CLI commands but it is

**[09:25]** using backlog CLI commands but it is more convenient if we ask our AI agent

**[09:27]** more convenient if we ask our AI agent

**[09:27]** more convenient if we ask our AI agent to do it for us. So we can have a human

**[09:31]** to do it for us. So we can have a human

**[09:32]** to do it for us. So we can have a human description about what we want to

**[09:33]** description about what we want to

**[09:33]** description about what we want to implement and the AI agent will run the

**[09:36]** implement and the AI agent will run the

**[09:36]** implement and the AI agent will run the backlog commands to create the task and

**[09:38]** backlog commands to create the task and

**[09:38]** backlog commands to create the task and to fill the the sections that are

**[09:41]** to fill the the sections that are

**[09:41]** to fill the the sections that are needed. And when the task is created, we

**[09:45]** needed. And when the task is created, we

**[09:45]** needed. And when the task is created, we can tell an agent something as simple

**[09:47]** can tell an agent something as simple

**[09:47]** can tell an agent something as simple as, "Hey Claude, can you please

**[09:49]** as, "Hey Claude, can you please

**[09:49]** as, "Hey Claude, can you please implement task 316?"

**[09:52]** implement task 316?"

**[09:52]** implement task 316?" And he will do it.

**[09:54]** And he will do it.

**[09:54]** And he will do it. So let's see what Claude has

**[09:57]** So let's see what Claude has

**[09:57]** So let's see what Claude has implemented.

**[09:59]** implemented.

**[09:59]** implemented. So we have our terminal here with our


### [10:00 - 11:00]

**[10:02]** So we have our terminal here with our

**[10:02]** So we have our terminal here with our new comban board and we can immediately

**[10:04]** new comban board and we can immediately

**[10:04]** new comban board and we can immediately spot a new command M to move. So let's

**[10:08]** spot a new command M to move. So let's

**[10:08]** spot a new command M to move. So let's uh press this button.

**[10:12]** uh press this button.

**[10:12]** uh press this button. You can see the task has been

**[10:13]** You can see the task has been

**[10:13]** You can see the task has been highlighted and I can go up and down and

**[10:16]** highlighted and I can go up and down and

**[10:16]** highlighted and I can go up and down and the task is being moved. And we can also

**[10:20]** the task is being moved. And we can also

**[10:20]** the task is being moved. And we can also hopefully yes go to the new status

**[10:22]** hopefully yes go to the new status

**[10:22]** hopefully yes go to the new status column.

**[10:24]** column.

**[10:24]** column. So we can commit or we can cancel. Let's

**[10:27]** So we can commit or we can cancel. Let's

**[10:27]** So we can commit or we can cancel. Let's cancel because we don't want to move

**[10:29]** cancel because we don't want to move

**[10:29]** cancel because we don't want to move this task. But for example,

**[10:32]** this task. But for example,

**[10:32]** this task. But for example, let's try uh the task that has been just

**[10:35]** let's try uh the task that has been just

**[10:35]** let's try uh the task that has been just implemented. So this is the task 316.

**[10:40]** implemented. So this is the task 316.

**[10:40]** implemented. So this is the task 316. Let's say there was a problem and not

**[10:42]** Let's say there was a problem and not

**[10:42]** Let's say there was a problem and not everything has been implemented

**[10:44]** everything has been implemented

**[10:44]** everything has been implemented correctly. Let's move it back in

**[10:45]** correctly. Let's move it back in

**[10:45]** correctly. Let's move it back in progress.

**[10:55]** And it works. It has been successfully

**[10:55]** And it works. It has been successfully moved to in progress column. So this is

**[10:58]** moved to in progress column. So this is

**[10:58]** moved to in progress column. So this is an example of how you can use backlog MD


### [11:00 - 12:00]

**[11:00]** an example of how you can use backlog MD

**[11:00]** an example of how you can use backlog MD with your favorite AI agent and you can

**[11:03]** with your favorite AI agent and you can

**[11:03]** with your favorite AI agent and you can have a task implemented correctly

**[11:05]** have a task implemented correctly

**[11:06]** have a task implemented correctly according to your specs in few minutes.

**[11:08]** according to your specs in few minutes.

**[11:08]** according to your specs in few minutes. But why does this work so well? Having

**[11:11]** But why does this work so well? Having

**[11:11]** But why does this work so well? Having markdown tasks stored in your repo

**[11:14]** markdown tasks stored in your repo

**[11:14]** markdown tasks stored in your repo allows you to do a sort of context

**[11:16]** allows you to do a sort of context

**[11:16]** allows you to do a sort of context engineering which means you can define

**[11:19]** engineering which means you can define

**[11:19]** engineering which means you can define how much an AI agent should implement

**[11:22]** how much an AI agent should implement

**[11:22]** how much an AI agent should implement within a single task so that he doesn't

**[11:24]** within a single task so that he doesn't

**[11:24]** within a single task so that he doesn't run out of their context window and you

**[11:28]** run out of their context window and you

**[11:28]** run out of their context window and you know exactly what will be implemented

**[11:30]** know exactly what will be implemented

**[11:30]** know exactly what will be implemented and they don't implement extra features

**[11:32]** and they don't implement extra features

**[11:32]** and they don't implement extra features that are not wanted and since you we are

**[11:35]** that are not wanted and since you we are

**[11:35]** that are not wanted and since you we are using smaller atomic tasks if something

**[11:39]** using smaller atomic tasks if something

**[11:39]** using smaller atomic tasks if something goes wrong Um with each of these with

**[11:42]** goes wrong Um with each of these with

**[11:42]** goes wrong Um with each of these with any of these tasks you can roll back

**[11:45]** any of these tasks you can roll back

**[11:45]** any of these tasks you can roll back change the specs the acceptance criteria

**[11:48]** change the specs the acceptance criteria

**[11:48]** change the specs the acceptance criteria the description and ask the AI agent to

**[11:51]** the description and ask the AI agent to

**[11:51]** the description and ask the AI agent to start again from the implementation

**[11:52]** start again from the implementation

**[11:52]** start again from the implementation plan.

**[11:54]** plan.

**[11:54]** plan. The scope is well defined. So you can

**[11:57]** The scope is well defined. So you can

**[11:57]** The scope is well defined. So you can really define with using the acceptance


### [12:00 - 13:00]

**[12:00]** really define with using the acceptance

**[12:00]** really define with using the acceptance criteria what should be part of this

**[12:02]** criteria what should be part of this

**[12:02]** criteria what should be part of this feature and what should be not part of

**[12:04]** feature and what should be not part of

**[12:04]** feature and what should be not part of this feature. And the tests um if you

**[12:08]** this feature. And the tests um if you

**[12:08]** this feature. And the tests um if you run unit test they should also uh check

**[12:11]** run unit test they should also uh check

**[12:11]** run unit test they should also uh check if the acceptance criteria as are met

**[12:15]** if the acceptance criteria as are met

**[12:15]** if the acceptance criteria as are met and it will allow this three review uh

**[12:19]** and it will allow this three review uh

**[12:19]** and it will allow this three review uh process that I just showed to you. The

**[12:20]** process that I just showed to you. The

**[12:20]** process that I just showed to you. The first review checkpoint is after the

**[12:23]** first review checkpoint is after the

**[12:23]** first review checkpoint is after the task is created. You can check the

**[12:25]** task is created. You can check the

**[12:25]** task is created. You can check the description and the acceptance criteria

**[12:27]** description and the acceptance criteria

**[12:27]** description and the acceptance criteria if the agents understood your intent.

**[12:29]** if the agents understood your intent.

**[12:29]** if the agents understood your intent. Then you can review the implementation

**[12:32]** Then you can review the implementation

**[12:32]** Then you can review the implementation plan. You can see if the agent is going

**[12:35]** plan. You can see if the agent is going

**[12:35]** plan. You can see if the agent is going into the right direction and at the end

**[12:37]** into the right direction and at the end

**[12:37]** into the right direction and at the end you will review the code.

**[12:41]** you will review the code.

**[12:41]** you will review the code. You can also work on multiple tasks in

**[12:43]** You can also work on multiple tasks in

**[12:44]** You can also work on multiple tasks in parallel using git works

**[12:46]** parallel using git works

**[12:46]** parallel using git works given that there are no dependencies. So

**[12:49]** given that there are no dependencies. So

**[12:49]** given that there are no dependencies. So what is backlog?

**[12:51]** what is backlog?

**[12:51]** what is backlog? It's an open-source MIT CLI tool. It has

**[12:55]** It's an open-source MIT CLI tool. It has

**[12:55]** It's an open-source MIT CLI tool. It has a terminal user interface but also web

**[12:58]** a terminal user interface but also web

**[12:58]** a terminal user interface but also web interface.


### [13:00 - 14:00]

**[13:00]** interface.

**[13:00]** interface. AI agents can interact via CLI commands

**[13:03]** AI agents can interact via CLI commands

**[13:03]** AI agents can interact via CLI commands or via MCP. MCP is the preferred native

**[13:07]** or via MCP. MCP is the preferred native

**[13:07]** or via MCP. MCP is the preferred native way, but we also support CLI commands

**[13:10]** way, but we also support CLI commands

**[13:10]** way, but we also support CLI commands for legacy AI agents.

**[13:13]** for legacy AI agents.

**[13:14]** for legacy AI agents. It is crossplatform. It works on most

**[13:16]** It is crossplatform. It works on most

**[13:16]** It is crossplatform. It works on most famous operating systems

**[13:20]** famous operating systems

**[13:20]** famous operating systems and you don't need any extra APIs or

**[13:22]** and you don't need any extra APIs or

**[13:22]** and you don't need any extra APIs or tools or databases or accounts. As long

**[13:25]** tools or databases or accounts. As long

**[13:25]** tools or databases or accounts. As long as you uh host all of the tasks on your

**[13:28]** as you uh host all of the tasks on your

**[13:28]** as you uh host all of the tasks on your Git repository, you can share them with

**[13:30]** Git repository, you can share them with

**[13:30]** Git repository, you can share them with your team and all of the tasks are in

**[13:33]** your team and all of the tasks are in

**[13:33]** your team and all of the tasks are in sync, which means that backlog checks

**[13:35]** sync, which means that backlog checks

**[13:35]** sync, which means that backlog checks the status of a task even if this task

**[13:37]** the status of a task even if this task

**[13:37]** the status of a task even if this task has been updated on another branch.

**[13:45]** And most important part, backlog code

**[13:45]** And most important part, backlog code has been written 99% by AI agents. The

**[13:49]** has been written 99% by AI agents. The

**[13:49]** has been written 99% by AI agents. The only co only part of the project that I

**[13:51]** only co only part of the project that I

**[13:51]** only co only part of the project that I written myself were the instructions and

**[13:54]** written myself were the instructions and

**[13:54]** written myself were the instructions and the first three tasks.

**[13:57]** the first three tasks.

**[13:57]** the first three tasks. Thank you very much for your attention.

**[13:59]** Thank you very much for your attention.

**[13:59]** Thank you very much for your attention. If you want to know more about backlog


### [14:00 - 15:00]

**[14:01]** If you want to know more about backlog

**[14:01]** If you want to know more about backlog andd or experiment with it, you can

**[14:03]** andd or experiment with it, you can

**[14:04]** andd or experiment with it, you can visit backlog.mmd in your browser. If

**[14:07]** visit backlog.mmd in your browser. If

**[14:07]** visit backlog.mmd in your browser. If you have any comments, please reach out

**[14:09]** you have any comments, please reach out

**[14:10]** you have any comments, please reach out to me and I will be happy to help you on

**[14:13]** to me and I will be happy to help you on

**[14:13]** to me and I will be happy to help you on board uh with backlog MD. Bye.


