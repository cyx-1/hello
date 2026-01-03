# Information Retrieval from the Ground Up - Philipp Krenn, Elastic

**Video URL:** https://www.youtube.com/watch?v=4Xe_iMYxBQc

---

## Full Transcript

### [00:00 - 01:00]

**[00:16]** Let's get going. Audio is okay for

**[00:16]** Let's get going. Audio is okay for everybody. I have some slight feedback,

**[00:19]** everybody. I have some slight feedback,

**[00:19]** everybody. I have some slight feedback, but I'll try to manage. I hope it's okay

**[00:21]** but I'll try to manage. I hope it's okay

**[00:21]** but I'll try to manage. I hope it's okay for you. Um, hi, I'm Phillip. Uh, let's

**[00:25]** for you. Um, hi, I'm Phillip. Uh, let's

**[00:25]** for you. Um, hi, I'm Phillip. Uh, let's talk a bit about retrieval. I'll show

**[00:27]** talk a bit about retrieval. I'll show

**[00:27]** talk a bit about retrieval. I'll show you some retrieval from the ground up.

**[00:29]** you some retrieval from the ground up.

**[00:29]** you some retrieval from the ground up. We'll keep it pretty hands-on. Um, you

**[00:32]** We'll keep it pretty hands-on. Um, you

**[00:32]** We'll keep it pretty hands-on. Um, you will have a chance to follow along and

**[00:33]** will have a chance to follow along and

**[00:33]** will have a chance to follow along and do everything that I show you as well. I

**[00:35]** do everything that I show you as well. I

**[00:35]** do everything that I show you as well. I have like a demo instance that you can

**[00:37]** have like a demo instance that you can

**[00:37]** have like a demo instance that you can use. Um, or you can just watch me. Um,

**[00:40]** use. Um, or you can just watch me. Um,

**[00:40]** use. Um, or you can just watch me. Um, if you have any questions, ask at any

**[00:43]** if you have any questions, ask at any

**[00:43]** if you have any questions, ask at any moment. If anything is too small to

**[00:45]** moment. If anything is too small to

**[00:45]** moment. If anything is too small to reach, shout and we'll try to make it

**[00:46]** reach, shout and we'll try to make it

**[00:46]** reach, shout and we'll try to make it larger. Uh, we'll try to adjust as we go

**[00:49]** larger. Uh, we'll try to adjust as we go

**[00:49]** larger. Uh, we'll try to adjust as we go along. So

**[00:51]** along. So

**[00:51]** along. So I guess we're not over rag yet, but uh

**[00:54]** I guess we're not over rag yet, but uh

**[00:54]** I guess we're not over rag yet, but uh rag is a thing and we'll focus on the R

**[00:58]** rag is a thing and we'll focus on the R

**[00:58]** rag is a thing and we'll focus on the R in rag, the retrieval augmented

**[00:59]** in rag, the retrieval augmented

**[00:59]** in rag, the retrieval augmented generation. We'll just focus on the


### [01:00 - 02:00]

**[01:01]** generation. We'll just focus on the

**[01:01]** generation. We'll just focus on the retrieval. Um just let's see where we

**[01:05]** retrieval. Um just let's see where we

**[01:05]** retrieval. Um just let's see where we are with retrieval. Um quick show of

**[01:08]** are with retrieval. Um quick show of

**[01:08]** are with retrieval. Um quick show of hands, who has done rag before?

**[01:11]** hands, who has done rag before?

**[01:11]** hands, who has done rag before? Okay, that's about half or so. Um who

**[01:13]** Okay, that's about half or so. Um who

**[01:13]** Okay, that's about half or so. Um who has done anything with vector search and

**[01:16]** has done anything with vector search and

**[01:16]** has done anything with vector search and rag?

**[01:18]** rag?

**[01:18]** rag? Do I need vector search for rag or can I

**[01:20]** Do I need vector search for rag or can I

**[01:20]** Do I need vector search for rag or can I do do anything else?

**[01:27]** Yeah. Yeah. So you can do anything. Um

**[01:27]** Yeah. Yeah. So you can do anything. Um retrieval is actually a very old thing.

**[01:30]** retrieval is actually a very old thing.

**[01:30]** retrieval is actually a very old thing. Um depending on how you define it, it

**[01:32]** Um depending on how you define it, it

**[01:32]** Um depending on how you define it, it might be 50, 70, whatever years old.

**[01:34]** might be 50, 70, whatever years old.

**[01:34]** might be 50, 70, whatever years old. Retrieval is just getting the right

**[01:36]** Retrieval is just getting the right

**[01:36]** Retrieval is just getting the right context to the generation. I'll ignore

**[01:39]** context to the generation. I'll ignore

**[01:39]** context to the generation. I'll ignore all the generation for today. We'll keep

**[01:40]** all the generation for today. We'll keep

**[01:40]** all the generation for today. We'll keep it very simple. We'll just focus on the

**[01:42]** it very simple. We'll just focus on the

**[01:42]** it very simple. We'll just focus on the retrieval part of getting the right

**[01:43]** retrieval part of getting the right

**[01:43]** retrieval part of getting the right information in um partially from the old

**[01:47]** information in um partially from the old

**[01:47]** information in um partially from the old stuff like the classics. Uh but we'll

**[01:49]** stuff like the classics. Uh but we'll

**[01:49]** stuff like the classics. Uh but we'll get to some new things as well as we go

**[01:51]** get to some new things as well as we go

**[01:51]** get to some new things as well as we go along. Um who has done keyword search

**[01:54]** along. Um who has done keyword search

**[01:54]** along. Um who has done keyword search before just that is fewer than vector

**[01:58]** before just that is fewer than vector

**[01:58]** before just that is fewer than vector search I feel like. um which is um which


### [02:00 - 03:00]

**[02:01]** search I feel like. um which is um which

**[02:01]** search I feel like. um which is um which almost reminds me of like 15 years ago

**[02:03]** almost reminds me of like 15 years ago

**[02:03]** almost reminds me of like 15 years ago or so when no SQL came up like more

**[02:05]** or so when no SQL came up like more

**[02:06]** or so when no SQL came up like more people had done MongoDB radius whatever

**[02:07]** people had done MongoDB radius whatever

**[02:07]** people had done MongoDB radius whatever else um rather than SQL that has changed

**[02:10]** else um rather than SQL that has changed

**[02:10]** else um rather than SQL that has changed again um I think it will be kind of

**[02:12]** again um I think it will be kind of

**[02:12]** again um I think it will be kind of similar for retrieval um the way I would

**[02:17]** similar for retrieval um the way I would

**[02:17]** similar for retrieval um the way I would vector search um is a feature of

**[02:19]** vector search um is a feature of

**[02:19]** vector search um is a feature of retrieval only one of multiple features

**[02:22]** retrieval only one of multiple features

**[02:22]** retrieval only one of multiple features or many features that you want in

**[02:24]** or many features that you want in

**[02:24]** or many features that you want in retrieval and we'll see a bit why and

**[02:26]** retrieval and we'll see a bit why and

**[02:26]** retrieval and we'll see a bit why and how and we'll we'll dive into those

**[02:27]** how and we'll we'll dive into those

**[02:27]** how and we'll we'll dive into those details um So, I work for Elastic, the

**[02:29]** details um So, I work for Elastic, the

**[02:29]** details um So, I work for Elastic, the company behind Elastic Search. We're the

**[02:31]** company behind Elastic Search. We're the

**[02:32]** company behind Elastic Search. We're the most downloaded, deployed, whatever else

**[02:35]** most downloaded, deployed, whatever else

**[02:35]** most downloaded, deployed, whatever else search engine. We do vector search, we

**[02:37]** search engine. We do vector search, we

**[02:37]** search engine. We do vector search, we do keyword search, we do hybrid search.

**[02:39]** do keyword search, we do hybrid search.

**[02:39]** do keyword search, we do hybrid search. Um, we'll dive into various examples.

**[02:41]** Um, we'll dive into various examples.

**[02:41]** Um, we'll dive into various examples. Everything that I will show you um works

**[02:44]** Everything that I will show you um works

**[02:44]** Everything that I will show you um works well, the query language is elastic

**[02:46]** well, the query language is elastic

**[02:46]** well, the query language is elastic search, but if you use anything built on

**[02:49]** search, but if you use anything built on

**[02:49]** search, but if you use anything built on Apache Lucine, everything behaves very

**[02:51]** Apache Lucine, everything behaves very

**[02:51]** Apache Lucine, everything behaves very similarly. If you use something that is

**[02:53]** similarly. If you use something that is

**[02:53]** similarly. If you use something that is a clone or close uh to lucine like

**[02:56]** a clone or close uh to lucine like

**[02:56]** a clone or close uh to lucine like anything built on uh tent TV or anything

**[02:59]** anything built on uh tent TV or anything

**[02:59]** anything built on uh tent TV or anything like that it will be very similar the


### [03:00 - 04:00]

**[03:01]** like that it will be very similar the

**[03:01]** like that it will be very similar the found keyword search and vector search

**[03:04]** found keyword search and vector search

**[03:04]** found keyword search and vector search will apply broadly everywhere. Um so

**[03:08]** will apply broadly everywhere. Um so

**[03:08]** will apply broadly everywhere. Um so let's get going. U we'll keep this

**[03:09]** let's get going. U we'll keep this

**[03:09]** let's get going. U we'll keep this pretty hands-on. Um who remembers in

**[03:11]** pretty hands-on. Um who remembers in

**[03:11]** pretty hands-on. Um who remembers in Star Wars when he's making that hand

**[03:13]** Star Wars when he's making that hand

**[03:13]** Star Wars when he's making that hand gesture. Um what is the quote?

**[03:20]** These are not the droids you're looking

**[03:20]** These are not the droids you're looking for. Um, we'll keep this relatively Star

**[03:23]** for. Um, we'll keep this relatively Star

**[03:23]** for. Um, we'll keep this relatively Star Wars uh based. Um, feel free to come in

**[03:27]** Wars uh based. Um, feel free to come in

**[03:27]** Wars uh based. Um, feel free to come in and filter on the sides. So, whatever.

**[03:28]** and filter on the sides. So, whatever.

**[03:28]** and filter on the sides. So, whatever. Um, I'm afraid we have I think one chair

**[03:31]** Um, I'm afraid we have I think one chair

**[03:31]** Um, I'm afraid we have I think one chair over there otherwise and one down there

**[03:34]** over there otherwise and one down there

**[03:34]** over there otherwise and one down there otherwise it's getting a bit

**[03:37]** otherwise it's getting a bit

**[03:37]** otherwise it's getting a bit full. Um, okay. Let's look at this uh of

**[03:41]** full. Um, okay. Let's look at this uh of

**[03:41]** full. Um, okay. Let's look at this uh of what these are not the droids you're

**[03:42]** what these are not the droids you're

**[03:42]** what these are not the droids you're looking for uh does for search. And I

**[03:44]** looking for uh does for search. And I

**[03:44]** looking for uh does for search. And I will start kind of like with the classic

**[03:46]** will start kind of like with the classic

**[03:46]** will start kind of like with the classic approach. Keyword search or lexical

**[03:48]** approach. Keyword search or lexical

**[03:48]** approach. Keyword search or lexical search is like you search for the words

**[03:50]** search is like you search for the words

**[03:50]** search is like you search for the words that you have stored and we want to find

**[03:53]** that you have stored and we want to find

**[03:53]** that you have stored and we want to find what is relevant in our examples. Um if

**[03:56]** what is relevant in our examples. Um if

**[03:56]** what is relevant in our examples. Um if you want to follow along um there is a


### [04:00 - 05:00]

**[04:00]** you want to follow along um there is a

**[04:00]** you want to follow along um there is a gist which has all the code that I'm

**[04:02]** gist which has all the code that I'm

**[04:02]** gist which has all the code that I'm showing you. It's at elastai.engineer.

**[04:06]** showing you. It's at elastai.engineer.

**[04:06]** showing you. It's at elastai.engineer. Um

**[04:07]** Um

**[04:07]** Um there is one important thing. It's I

**[04:10]** there is one important thing. It's I

**[04:10]** there is one important thing. It's I have one shared instance basically for

**[04:12]** have one shared instance basically for

**[04:12]** have one shared instance basically for everybody. So you can all just use this

**[04:14]** everybody. So you can all just use this

**[04:14]** everybody. So you can all just use this without signing up for any accounts or

**[04:16]** without signing up for any accounts or

**[04:16]** without signing up for any accounts or anything. So this is just a cloud

**[04:17]** anything. So this is just a cloud

**[04:17]** anything. So this is just a cloud instance um that you can use. There is

**[04:20]** instance um that you can use. There is

**[04:20]** instance um that you can use. There is my handle um is in the index name. If

**[04:24]** my handle um is in the index name. If

**[04:24]** my handle um is in the index name. If you don't want to fight and overwrite

**[04:26]** you don't want to fight and overwrite

**[04:26]** you don't want to fight and overwrite each other's data, reply replace that

**[04:28]** each other's data, reply replace that

**[04:28]** each other's data, reply replace that with your unique handle or something

**[04:30]** with your unique handle or something

**[04:30]** with your unique handle or something that is specific to you because

**[04:31]** that is specific to you because

**[04:31]** that is specific to you because otherwise you will all work on the same

**[04:33]** otherwise you will all work on the same

**[04:33]** otherwise you will all work on the same index and kind of like overwrite each

**[04:35]** index and kind of like overwrite each

**[04:35]** index and kind of like overwrite each other's data. You can also just watch me

**[04:37]** other's data. You can also just watch me

**[04:37]** other's data. You can also just watch me if you don't have a computer handy

**[04:39]** if you don't have a computer handy

**[04:39]** if you don't have a computer handy that's fine. Um but if you want to

**[04:41]** that's fine. Um but if you want to

**[04:41]** that's fine. Um but if you want to follow along elasti.engineer

**[04:44]** follow along elasti.engineer

**[04:44]** follow along elasti.engineer there will be a gist. And it will have

**[04:46]** there will be a gist. And it will have

**[04:46]** there will be a gist. And it will have the connection string like there's a URL

**[04:48]** the connection string like there's a URL

**[04:48]** the connection string like there's a URL and then the credentials are workshop

**[04:50]** and then the credentials are workshop

**[04:50]** and then the credentials are workshop workshop if you go in to login it will

**[04:52]** workshop if you go in to login it will

**[04:52]** workshop if you go in to login it will say login with elastic search that's

**[04:54]** say login with elastic search that's

**[04:54]** say login with elastic search that's where you use workshop workshop then

**[04:56]** where you use workshop workshop then

**[04:56]** where you use workshop workshop then you'll be able to login and you can just

**[04:59]** you'll be able to login and you can just

**[04:59]** you'll be able to login and you can just run all the queries that I'm showing you


### [05:00 - 06:00]

**[05:01]** run all the queries that I'm showing you

**[05:01]** run all the queries that I'm showing you can try out stuff um if you have any

**[05:03]** can try out stuff um if you have any

**[05:03]** can try out stuff um if you have any questions shout I have a couple of

**[05:05]** questions shout I have a couple of

**[05:05]** questions shout I have a couple of colleagues dispersed in the room so um

**[05:07]** colleagues dispersed in the room so um

**[05:08]** colleagues dispersed in the room so um if we have too many questions we'll

**[05:09]** if we have too many questions we'll

**[05:09]** if we have too many questions we'll somehow divide and conquer um so let's

**[05:12]** somehow divide and conquer um so let's

**[05:12]** somehow divide and conquer um so let's get going and see what we have here Um,

**[05:16]** get going and see what we have here Um,

**[05:16]** get going and see what we have here Um, and I'll show you most of the stuff

**[05:17]** and I'll show you most of the stuff

**[05:17]** and I'll show you most of the stuff live. Um,

**[05:20]** live. Um,

**[05:20]** live. Um, I think this is large enough in the back

**[05:22]** I think this is large enough in the back

**[05:22]** I think this is large enough in the back row. If it's not large enough for

**[05:23]** row. If it's not large enough for

**[05:23]** row. If it's not large enough for anybody, shout and we'll see how much

**[05:25]** anybody, shout and we'll see how much

**[05:25]** anybody, shout and we'll see how much larger I can make this. Um,

**[05:29]** larger I can make this. Um,

**[05:29]** larger I can make this. Um, and let me turn off the Wi-Fi and hope

**[05:32]** and let me turn off the Wi-Fi and hope

**[05:32]** and let me turn off the Wi-Fi and hope that my wired connection is good enough.


### [06:00 - 07:00]

**[06:23]** Okay, this is no good.

**[06:24]** Okay, this is no good. Out you go.

**[06:31]** Okay, hardest problem of the day solved.

**[06:31]** Okay, hardest problem of the day solved. We have network. Um, okay. So, we have

**[06:35]** We have network. Um, okay. So, we have

**[06:35]** We have network. Um, okay. So, we have the sentence, these are not the droids

**[06:37]** the sentence, these are not the droids

**[06:37]** the sentence, these are not the droids you're looking for. And we'll start with

**[06:38]** you're looking for. And we'll start with

**[06:38]** you're looking for. And we'll start with the classic keyword or lexical search

**[06:40]** the classic keyword or lexical search

**[06:40]** the classic keyword or lexical search like what happens behind the scenes. So

**[06:42]** like what happens behind the scenes. So

**[06:42]** like what happens behind the scenes. So what you generally want to do is you

**[06:44]** what you generally want to do is you

**[06:44]** what you generally want to do is you basically want to extract the individual

**[06:46]** basically want to extract the individual

**[06:46]** basically want to extract the individual words and then make them searchable. Um

**[06:49]** words and then make them searchable. Um

**[06:49]** words and then make them searchable. Um so here I'm not storing anything. I'm

**[06:51]** so here I'm not storing anything. I'm

**[06:51]** so here I'm not storing anything. I'm just looking at like how would that look

**[06:53]** just looking at like how would that look

**[06:53]** just looking at like how would that look like if I stored something. I'm using

**[06:54]** like if I stored something. I'm using

**[06:54]** like if I stored something. I'm using this underscore analyze endpoint uh to

**[06:57]** this underscore analyze endpoint uh to

**[06:57]** this underscore analyze endpoint uh to sh to see um what I will actually store


### [07:00 - 08:00]

**[07:01]** sh to see um what I will actually store

**[07:01]** sh to see um what I will actually store in the background to make then

**[07:02]** in the background to make then

**[07:02]** in the background to make then searchable. So if these are not the

**[07:04]** searchable. So if these are not the

**[07:04]** searchable. So if these are not the droids you're looking for and you see

**[07:06]** droids you're looking for and you see

**[07:06]** droids you're looking for and you see these are m not m the droids you are

**[07:12]** these are m not m the droids you are

**[07:12]** these are m not m the droids you are looking for

**[07:15]** looking for

**[07:15]** looking for in western languages the first step that

**[07:17]** in western languages the first step that

**[07:17]** in western languages the first step that hap or every time or everywhere the

**[07:20]** hap or every time or everywhere the

**[07:20]** hap or every time or everywhere the first step that h happens is the

**[07:21]** first step that h happens is the

**[07:21]** first step that h happens is the tokenization in western languages it's

**[07:23]** tokenization in western languages it's

**[07:23]** tokenization in western languages it's pretty simple it's normally any white

**[07:25]** pretty simple it's normally any white

**[07:25]** pretty simple it's normally any white spaces and punctuation marks where you

**[07:26]** spaces and punctuation marks where you

**[07:26]** spaces and punctuation marks where you just break out the individual tokens um

**[07:29]** just break out the individual tokens um

**[07:29]** just break out the individual tokens um especially Asian languages are a bit

**[07:31]** especially Asian languages are a bit

**[07:31]** especially Asian languages are a bit more complicated around that but we'll

**[07:33]** more complicated around that but we'll

**[07:33]** more complicated around that but we'll gloss over that for today. And we have a

**[07:36]** gloss over that for today. And we have a

**[07:36]** gloss over that for today. And we have a couple of interesting pieces of

**[07:37]** couple of interesting pieces of

**[07:38]** couple of interesting pieces of information here. So we have the token.

**[07:39]** information here. So we have the token.

**[07:39]** information here. So we have the token. So these um is the first token. We have

**[07:42]** So these um is the first token. We have

**[07:42]** So these um is the first token. We have the start offset and the end offset. Um

**[07:45]** the start offset and the end offset. Um

**[07:46]** the start offset and the end offset. Um why would I need a start and an end

**[07:47]** why would I need a start and an end

**[07:47]** why would I need a start and an end offset? Why would extract and then store

**[07:50]** offset? Why would extract and then store

**[07:50]** offset? Why would extract and then store that potentially?

**[07:51]** that potentially?

**[07:51]** that potentially? Any guesses? Yeah.

**[07:55]** Any guesses? Yeah.

**[07:55]** Any guesses? Yeah. Yes. Especially if you have a longer

**[07:57]** Yes. Especially if you have a longer

**[07:57]** Yes. Especially if you have a longer text, you would want to have that

**[07:58]** text, you would want to have that

**[07:58]** text, you would want to have that highlighting feature that you want to

**[07:59]** highlighting feature that you want to


### [08:00 - 09:00]

**[08:00]** highlighting feature that you want to say um this is where my hit actually

**[08:02]** say um this is where my hit actually

**[08:02]** say um this is where my hit actually was. So if I'm searching for these,

**[08:04]** was. So if I'm searching for these,

**[08:04]** was. So if I'm searching for these, which is maybe not a great word, uh but

**[08:05]** which is maybe not a great word, uh but

**[08:06]** which is maybe not a great word, uh but you would very easily be able to

**[08:07]** you would very easily be able to

**[08:07]** you would very easily be able to highlight where you had actually the

**[08:08]** highlight where you had actually the

**[08:08]** highlight where you had actually the match. And the trick that you're doing

**[08:11]** match. And the trick that you're doing

**[08:11]** match. And the trick that you're doing in search generally what differentiates

**[08:13]** in search generally what differentiates

**[08:13]** in search generally what differentiates it from a database is a database just

**[08:15]** it from a database is a database just

**[08:15]** it from a database is a database just stores what you give it and then does

**[08:17]** stores what you give it and then does

**[08:17]** stores what you give it and then does basically almost everything at query or

**[08:19]** basically almost everything at query or

**[08:20]** basically almost everything at query or search time. versus a search engine does

**[08:22]** search time. versus a search engine does

**[08:22]** search time. versus a search engine does a lot of the work at ingestion or when

**[08:24]** a lot of the work at ingestion or when

**[08:24]** a lot of the work at ingestion or when you store the data. So we break out the

**[08:26]** you store the data. So we break out the

**[08:26]** you store the data. So we break out the individual tokens. Um we calculate these

**[08:29]** individual tokens. Um we calculate these

**[08:29]** individual tokens. Um we calculate these offsets and store them. So whenever we

**[08:31]** offsets and store them. So whenever we

**[08:31]** offsets and store them. So whenever we have a match afterwards we never need to

**[08:33]** have a match afterwards we never need to

**[08:33]** have a match afterwards we never need to reanalyze the actual text which could

**[08:35]** reanalyze the actual text which could

**[08:35]** reanalyze the actual text which could potentially be multiple pages long. Um

**[08:37]** potentially be multiple pages long. Um

**[08:37]** potentially be multiple pages long. Um but we could just highlight where we

**[08:39]** but we could just highlight where we

**[08:39]** but we could just highlight where we have that match because we have

**[08:40]** have that match because we have

**[08:40]** have that match because we have extracted those positions. Um we have a

**[08:43]** extracted those positions. Um we have a

**[08:43]** extracted those positions. Um we have a position. Why would I want to store the

**[08:45]** position. Why would I want to store the

**[08:45]** position. Why would I want to store the position with the text that I have?

**[08:52]** Yeah.

**[08:52]** Yeah. uh yeah annotation. So the the main use

**[08:54]** uh yeah annotation. So the the main use

**[08:54]** uh yeah annotation. So the the main use case uh that you have is if you have

**[08:56]** case uh that you have is if you have

**[08:56]** case uh that you have is if you have these positions and later on we'll

**[08:58]** these positions and later on we'll

**[08:58]** these positions and later on we'll briefly look at if you want to look for

**[08:59]** briefly look at if you want to look for


### [09:00 - 10:00]

**[09:00]** briefly look at if you want to look for a phrase if you want to look for this

**[09:01]** a phrase if you want to look for this

**[09:01]** a phrase if you want to look for this word followed by that word. Um so you

**[09:04]** word followed by that word. Um so you

**[09:04]** word followed by that word. Um so you could then just look for all the text

**[09:06]** could then just look for all the text

**[09:06]** could then just look for all the text that contain these words but then you

**[09:08]** that contain these words but then you

**[09:08]** that contain these words but then you could also just compare the positions

**[09:09]** could also just compare the positions

**[09:09]** could also just compare the positions and basically look for n plus1 etc. And

**[09:12]** and basically look for n plus1 etc. And

**[09:12]** and basically look for n plus1 etc. And you never need to look at the string

**[09:14]** you never need to look at the string

**[09:14]** you never need to look at the string again, but you can just look at the

**[09:15]** again, but you can just look at the

**[09:15]** again, but you can just look at the positions to figure out like this was

**[09:17]** positions to figure out like this was

**[09:17]** positions to figure out like this was one continuous phrase even if you have

**[09:19]** one continuous phrase even if you have

**[09:19]** one continuous phrase even if you have broken it out into the individual

**[09:21]** broken it out into the individual

**[09:21]** broken it out into the individual tokens. Um, most of the things that we

**[09:24]** tokens. Um, most of the things that we

**[09:24]** tokens. Um, most of the things that we see here is alpha num for alpha numeric.

**[09:28]** see here is alpha num for alpha numeric.

**[09:28]** see here is alpha num for alpha numeric. An alternative would be synonyms. We'll

**[09:30]** An alternative would be synonyms. We'll

**[09:30]** An alternative would be synonyms. We'll skip over synonym definition because

**[09:31]** skip over synonym definition because

**[09:31]** skip over synonym definition because it's not fun to define tons of synonyms.

**[09:34]** it's not fun to define tons of synonyms.

**[09:34]** it's not fun to define tons of synonyms. Uh, but this is all the things that we

**[09:36]** Uh, but this is all the things that we

**[09:36]** Uh, but this is all the things that we are storing here in the background. You

**[09:38]** are storing here in the background. You

**[09:38]** are storing here in the background. You can also customize this analysis and

**[09:40]** can also customize this analysis and

**[09:40]** can also customize this analysis and that is one of the the features again of

**[09:42]** that is one of the the features again of

**[09:42]** that is one of the the features again of full text search and lexical searches

**[09:45]** full text search and lexical searches

**[09:45]** full text search and lexical searches that you pre-process a lot of the

**[09:46]** that you pre-process a lot of the

**[09:46]** that you pre-process a lot of the information to make that search

**[09:48]** information to make that search

**[09:48]** information to make that search afterwards faster. So here you can see

**[09:50]** afterwards faster. So here you can see

**[09:50]** afterwards faster. So here you can see I'm stripping out the HTML because

**[09:52]** I'm stripping out the HTML because

**[09:52]** I'm stripping out the HTML because nobody's going to search for this

**[09:54]** nobody's going to search for this

**[09:54]** nobody's going to search for this emphasis tag. Um I use a standard

**[09:56]** emphasis tag. Um I use a standard

**[09:56]** emphasis tag. Um I use a standard tokenizer um that breaks up for example


### [10:00 - 11:00]

**[10:00]** tokenizer um that breaks up for example

**[10:00]** tokenizer um that breaks up for example on dashes. You will see that

**[10:02]** on dashes. You will see that

**[10:02]** on dashes. You will see that alternatives would be whites space that

**[10:04]** alternatives would be whites space that

**[10:04]** alternatives would be whites space that you only break up on white spaces. Um, I

**[10:07]** you only break up on white spaces. Um, I

**[10:07]** you only break up on white spaces. Um, I lowerase everything, which is most of

**[10:10]** lowerase everything, which is most of

**[10:10]** lowerase everything, which is most of the times what you want because nobody

**[10:12]** the times what you want because nobody

**[10:12]** the times what you want because nobody searches in Google um with proper casing

**[10:14]** searches in Google um with proper casing

**[10:14]** searches in Google um with proper casing or at least maybe my parents, but nobody

**[10:17]** or at least maybe my parents, but nobody

**[10:17]** or at least maybe my parents, but nobody else searches uh with proper casing in

**[10:19]** else searches uh with proper casing in

**[10:19]** else searches uh with proper casing in in Google. Um, we remove stop words.

**[10:22]** in Google. Um, we remove stop words.

**[10:22]** in Google. Um, we remove stop words. We'll get to stop words in a moment. Um,

**[10:24]** We'll get to stop words in a moment. Um,

**[10:24]** We'll get to stop words in a moment. Um, and we do stemming with the snowball

**[10:27]** and we do stemming with the snowball

**[10:27]** and we do stemming with the snowball stemmer. What stemming is, it basically

**[10:29]** stemmer. What stemming is, it basically

**[10:29]** stemmer. What stemming is, it basically reduces a word down to the root. So you

**[10:31]** reduces a word down to the root. So you

**[10:31]** reduces a word down to the root. So you don't care about singular plural or like

**[10:33]** don't care about singular plural or like

**[10:33]** don't care about singular plural or like the flection of a verb anymore, but you

**[10:35]** the flection of a verb anymore, but you

**[10:35]** the flection of a verb anymore, but you really care more about the concept. So

**[10:39]** really care more about the concept. So

**[10:39]** really care more about the concept. So if I run through that analysis, does

**[10:41]** if I run through that analysis, does

**[10:42]** if I run through that analysis, does anybody want to guess what will remain

**[10:43]** anybody want to guess what will remain

**[10:43]** anybody want to guess what will remain of this phrase or which tokens will be

**[10:45]** of this phrase or which tokens will be

**[10:45]** of this phrase or which tokens will be extracted and what in what form?

**[10:56]** Not a lot will remain. Um,

**[10:56]** Not a lot will remain. Um, two.

**[10:59]** two.

**[10:59]** two. Yeah, close. Um, so we'll actually have


### [11:00 - 12:00]

**[11:03]** Yeah, close. Um, so we'll actually have

**[11:03]** Yeah, close. Um, so we'll actually have three. So we have droid, you and look.

**[11:07]** three. So we have droid, you and look.

**[11:07]** three. So we have droid, you and look. And you can see all the others were stop

**[11:10]** And you can see all the others were stop

**[11:10]** And you can see all the others were stop words which were removed. Um, the

**[11:13]** words which were removed. Um, the

**[11:13]** words which were removed. Um, the stemming reduced looking down to look

**[11:15]** stemming reduced looking down to look

**[11:15]** stemming reduced looking down to look because we don't care if it looks

**[11:17]** because we don't care if it looks

**[11:17]** because we don't care if it looks looking uh look. We just reduce it to

**[11:19]** looking uh look. We just reduce it to

**[11:20]** looking uh look. We just reduce it to the word stem. So we do this when we

**[11:22]** the word stem. So we do this when we

**[11:22]** the word stem. So we do this when we store the data. And by the way, when you

**[11:24]** store the data. And by the way, when you

**[11:24]** store the data. And by the way, when you search afterwards, um your text would

**[11:26]** search afterwards, um your text would

**[11:26]** search afterwards, um your text would run through the same analysis that you

**[11:28]** run through the same analysis that you

**[11:28]** run through the same analysis that you would have exact matches. So you don't

**[11:29]** would have exact matches. So you don't

**[11:30]** would have exact matches. So you don't need to do anything like a like search

**[11:31]** need to do anything like a like search

**[11:31]** need to do anything like a like search anymore in the future. So this will be

**[11:33]** anymore in the future. So this will be

**[11:33]** anymore in the future. So this will be much more performant uh than anything

**[11:35]** much more performant uh than anything

**[11:35]** much more performant uh than anything that you would do in a relational

**[11:36]** that you would do in a relational

**[11:36]** that you would do in a relational database because you have direct

**[11:38]** database because you have direct

**[11:38]** database because you have direct matches. And we'll look at the data

**[11:40]** matches. And we'll look at the data

**[11:40]** matches. And we'll look at the data structure behind it in a moment. But we

**[11:41]** structure behind it in a moment. But we

**[11:41]** structure behind it in a moment. But we what we get is uh droid u look um with

**[11:46]** what we get is uh droid u look um with

**[11:46]** what we get is uh droid u look um with the right positions. So, for example, if

**[11:47]** the right positions. So, for example, if

**[11:48]** the right positions. So, for example, if we searched for droid U, we could easily

**[11:50]** we searched for droid U, we could easily

**[11:50]** we searched for droid U, we could easily retrieve that because we have the

**[11:51]** retrieve that because we have the

**[11:51]** retrieve that because we have the positions. Um, even though that is a

**[11:54]** positions. Um, even though that is a

**[11:54]** positions. Um, even though that is a weird phrase. Um, do we start indexing

**[11:56]** weird phrase. Um, do we start indexing

**[11:56]** weird phrase. Um, do we start indexing at zero or one?


### [12:00 - 13:00]

**[12:05]** Zero. Yes, it's the only right way. Um,

**[12:05]** Zero. Yes, it's the only right way. Um, there discussion here. Um, so we we are

**[12:08]** there discussion here. Um, so we we are

**[12:08]** there discussion here. Um, so we we are the positions are based uh starting at

**[12:10]** the positions are based uh starting at

**[12:10]** the positions are based uh starting at zero and these are the tokens that are

**[12:12]** zero and these are the tokens that are

**[12:12]** zero and these are the tokens that are remaining. Um if you do this for a

**[12:15]** remaining. Um if you do this for a

**[12:15]** remaining. Um if you do this for a different language like you might hear

**[12:17]** different language like you might hear

**[12:17]** different language like you might hear I'm a native German speaker. Um this is

**[12:19]** I'm a native German speaker. Um this is

**[12:19]** I'm a native German speaker. Um this is the text in in German and you would uh

**[12:22]** the text in in German and you would uh

**[12:22]** the text in in German and you would uh if you use a German analyzer it would

**[12:24]** if you use a German analyzer it would

**[12:24]** if you use a German analyzer it would know the rules for German and then would

**[12:26]** know the rules for German and then would

**[12:26]** know the rules for German and then would analyze the text in the right way. So

**[12:28]** analyze the text in the right way. So

**[12:28]** analyze the text in the right way. So then you would have remaining droid s um

**[12:34]** then you would have remaining droid s um

**[12:34]** then you would have remaining droid s um anybody wants wants to guess what

**[12:35]** anybody wants wants to guess what

**[12:35]** anybody wants wants to guess what happens if I have the wrong language for

**[12:37]** happens if I have the wrong language for

**[12:37]** happens if I have the wrong language for a text.

**[12:45]** it will go very poorly because the so

**[12:45]** it will go very poorly because the so how how this works is basically you have

**[12:47]** how how this works is basically you have

**[12:47]** how how this works is basically you have rules for every single language is like

**[12:49]** rules for every single language is like

**[12:49]** rules for every single language is like what is the stop word how does stemming

**[12:51]** what is the stop word how does stemming

**[12:51]** what is the stop word how does stemming work if you apply the wrong rules you

**[12:53]** work if you apply the wrong rules you

**[12:54]** work if you apply the wrong rules you basically just get wrong stuff out so it

**[12:56]** basically just get wrong stuff out so it

**[12:56]** basically just get wrong stuff out so it will not um do what you want so what you

**[12:59]** will not um do what you want so what you

**[12:59]** will not um do what you want so what you get here is um like that this is an


### [13:00 - 14:00]

**[13:02]** get here is um like that this is an

**[13:02]** get here is um like that this is an article um but well in the in English

**[13:05]** article um but well in the in English

**[13:05]** article um but well in the in English the rule is an s at the end just gets

**[13:06]** the rule is an s at the end just gets

**[13:06]** the rule is an s at the end just gets stemmed away even though this doesn't

**[13:08]** stemmed away even though this doesn't

**[13:08]** stemmed away even though this doesn't make any sense so you apply the wrong

**[13:09]** make any sense so you apply the wrong

**[13:09]** make any sense so you apply the wrong rules um and you just produce

**[13:12]** rules um and you just produce

**[13:12]** rules um and you just produce pretty much garbage. Um, so don't do

**[13:14]** pretty much garbage. Um, so don't do

**[13:14]** pretty much garbage. Um, so don't do that. Um, just to give you another

**[13:16]** that. Um, just to give you another

**[13:16]** that. Um, just to give you another example, um,

**[13:18]** example, um,

**[13:18]** example, um, French, this is the same phrase in

**[13:20]** French, this is the same phrase in

**[13:20]** French, this is the same phrase in French. Um, and then you see, uh,

**[13:25]** French. Um, and then you see, uh,

**[13:25]** French. Um, and then you see, uh, and as are the words that are remaining

**[13:28]** and as are the words that are remaining

**[13:28]** and as are the words that are remaining in these examples. Otherwise, it works

**[13:30]** in these examples. Otherwise, it works

**[13:30]** in these examples. Otherwise, it works the same, but you need to have the right

**[13:32]** the same, but you need to have the right

**[13:32]** the same, but you need to have the right analysis for what you're doing.

**[13:33]** analysis for what you're doing.

**[13:33]** analysis for what you're doing. Otherwise, you'll just produce garbage.

**[13:35]** Otherwise, you'll just produce garbage.

**[13:35]** Otherwise, you'll just produce garbage. Um,

**[13:38]** Um,

**[13:38]** Um, a couple of things as we're going along.

**[13:40]** a couple of things as we're going along.

**[13:40]** a couple of things as we're going along. The stop word list by default which you

**[13:42]** The stop word list by default which you

**[13:42]** The stop word list by default which you could overwrite is relatively short.

**[13:44]** could overwrite is relatively short.

**[13:44]** could overwrite is relatively short. This is linguists have spent many years

**[13:47]** This is linguists have spent many years

**[13:47]** This is linguists have spent many years figuring out what are the right lists of

**[13:49]** figuring out what are the right lists of

**[13:49]** figuring out what are the right lists of stop words and you don't want to have

**[13:50]** stop words and you don't want to have

**[13:50]** stop words and you don't want to have too many or too few. Uh in English it's

**[13:52]** too many or too few. Uh in English it's

**[13:52]** too many or too few. Uh in English it's I always forget I think it's 33 or so.

**[13:55]** I always forget I think it's 33 or so.

**[13:55]** I always forget I think it's 33 or so. Um this is where you can find it in the

**[13:57]** Um this is where you can find it in the

**[13:57]** Um this is where you can find it in the source code. It's I don't want to say

**[13:58]** source code. It's I don't want to say

**[13:58]** source code. It's I don't want to say well hidden but it's not easy to find


### [14:00 - 15:00]

**[14:00]** well hidden but it's not easy to find

**[14:00]** well hidden but it's not easy to find either. Um so every language has like a

**[14:02]** either. Um so every language has like a

**[14:02]** either. Um so every language has like a list of stop words that are defined uh

**[14:04]** list of stop words that are defined uh

**[14:04]** list of stop words that are defined uh that will be automatically removed for.

**[14:06]** that will be automatically removed for.

**[14:06]** that will be automatically removed for. These are not the droids you are looking

**[14:08]** These are not the droids you are looking

**[14:08]** These are not the droids you are looking for. By accident, more or less we had a

**[14:11]** for. By accident, more or less we had a

**[14:11]** for. By accident, more or less we had a lot of stops and why not a lot remained

**[14:13]** lot of stops and why not a lot remained

**[14:13]** lot of stops and why not a lot remained here in the phrase. And then for all

**[14:14]** here in the phrase. And then for all

**[14:14]** here in the phrase. And then for all other languages, you will have a similar

**[14:16]** other languages, you will have a similar

**[14:16]** other languages, you will have a similar list um of stop words. Um

**[14:20]** list um of stop words. Um

**[14:20]** list um of stop words. Um should you always remove stop words?

**[14:34]** Yes. That is by the way another not is a

**[14:34]** Yes. That is by the way another not is a very good So I'm not sure if everybody

**[14:35]** very good So I'm not sure if everybody

**[14:35]** very good So I'm not sure if everybody heard that. Um the the comment was about

**[14:37]** heard that. Um the the comment was about

**[14:37]** heard that. Um the the comment was about not one important thing here. We're

**[14:39]** not one important thing here. We're

**[14:40]** not one important thing here. We're talking about lexical or keyword search

**[14:41]** talking about lexical or keyword search

**[14:42]** talking about lexical or keyword search which is dumb but scalable. Um it

**[14:46]** which is dumb but scalable. Um it

**[14:46]** which is dumb but scalable. Um it doesn't know understand if there is a

**[14:47]** doesn't know understand if there is a

**[14:47]** doesn't know understand if there is a droid or there's no droid. It's just

**[14:49]** droid or there's no droid. It's just

**[14:49]** droid or there's no droid. It's just defined as a stopard. It does just

**[14:51]** defined as a stopard. It does just

**[14:51]** defined as a stopard. It does just keyword matching. um that is in in

**[14:54]** keyword matching. um that is in in

**[14:54]** keyword matching. um that is in in vector search or anything with a machine

**[14:57]** vector search or anything with a machine

**[14:57]** vector search or anything with a machine learning model behind it will be a bit

**[14:58]** learning model behind it will be a bit

**[14:58]** learning model behind it will be a bit of a different story afterwards uh where


### [15:00 - 16:00]

**[15:00]** of a different story afterwards uh where

**[15:00]** of a different story afterwards uh where these things might make a difference but

**[15:02]** these things might make a difference but

**[15:02]** these things might make a difference but this is very simple because it just

**[15:04]** this is very simple because it just

**[15:04]** this is very simple because it just matches on similar strings basically um

**[15:07]** matches on similar strings basically um

**[15:07]** matches on similar strings basically um it doesn't understand the context it

**[15:08]** it doesn't understand the context it

**[15:08]** it doesn't understand the context it doesn't know what's going on that's why

**[15:10]** doesn't know what's going on that's why

**[15:10]** doesn't know what's going on that's why the linguist decided not this a good

**[15:12]** the linguist decided not this a good

**[15:12]** the linguist decided not this a good stop word um you could override that if

**[15:15]** stop word um you could override that if

**[15:15]** stop word um you could override that if for your specific use case this is not a

**[15:17]** for your specific use case this is not a

**[15:17]** for your specific use case this is not a good idea um

**[15:20]** good idea um

**[15:20]** good idea um always removing stops yes no maybe.

**[15:24]** always removing stops yes no maybe.

**[15:24]** always removing stops yes no maybe. So our favorite phrase is it depends

**[15:28]** So our favorite phrase is it depends

**[15:28]** So our favorite phrase is it depends and then you have to explain like what

**[15:31]** and then you have to explain like what

**[15:31]** and then you have to explain like what it depends on. So what it depends on is

**[15:33]** it depends on. So what it depends on is

**[15:33]** it depends on. So what it depends on is there are scenarios uh where removing

**[15:35]** there are scenarios uh where removing

**[15:35]** there are scenarios uh where removing all stop words does not give you the

**[15:37]** all stop words does not give you the

**[15:37]** all stop words does not give you the desired result and maybe you want to

**[15:39]** desired result and maybe you want to

**[15:39]** desired result and maybe you want to have like a text with and without stops.

**[15:41]** have like a text with and without stops.

**[15:41]** have like a text with and without stops. Like sometimes stop words are just like

**[15:43]** Like sometimes stop words are just like

**[15:43]** Like sometimes stop words are just like a lot of noise that blow up the index

**[15:45]** a lot of noise that blow up the index

**[15:45]** a lot of noise that blow up the index size and don't really add a lot of

**[15:46]** size and don't really add a lot of

**[15:46]** size and don't really add a lot of value. That's why we have defined them

**[15:48]** value. That's why we have defined them

**[15:48]** value. That's why we have defined them and try to remove them by default. Um

**[15:50]** and try to remove them by default. Um

**[15:50]** and try to remove them by default. Um but if you had for example to be or not

**[15:52]** but if you had for example to be or not

**[15:52]** but if you had for example to be or not to be these are all stop words. This

**[15:56]** to be these are all stop words. This

**[15:56]** to be these are all stop words. This would all be gone uh when you run it

**[15:58]** would all be gone uh when you run it

**[15:58]** would all be gone uh when you run it through analysis. Um so you it is tricky


### [16:00 - 17:00]

**[16:01]** through analysis. Um so you it is tricky

**[16:01]** through analysis. Um so you it is tricky to figure out like what is the right

**[16:03]** to figure out like what is the right

**[16:03]** to figure out like what is the right balance for stop words or what works for

**[16:05]** balance for stop words or what works for

**[16:05]** balance for stop words or what works for your use case but you might have

**[16:07]** your use case but you might have

**[16:07]** your use case but you might have unexpected surprises in all of this. Um

**[16:10]** unexpected surprises in all of this. Um

**[16:10]** unexpected surprises in all of this. Um okay we've seen the German examples. Um

**[16:14]** okay we've seen the German examples. Um

**[16:14]** okay we've seen the German examples. Um let's do some more queries. Um or let's

**[16:17]** let's do some more queries. Um or let's

**[16:17]** let's do some more queries. Um or let's actually store something. Um, so far we

**[16:20]** actually store something. Um, so far we

**[16:20]** actually store something. Um, so far we only pretended or we only looked at what

**[16:22]** only pretended or we only looked at what

**[16:22]** only pretended or we only looked at what would happen if we would store

**[16:23]** would happen if we would store

**[16:23]** would happen if we would store something. Now I'm actually creating an

**[16:26]** something. Now I'm actually creating an

**[16:26]** something. Now I'm actually creating an index. Again, if you're running this

**[16:28]** index. Again, if you're running this

**[16:28]** index. Again, if you're running this yourself, um, please use a different

**[16:30]** yourself, um, please use a different

**[16:30]** yourself, um, please use a different name than me. Um, just, uh, replace all

**[16:35]** name than me. Um, just, uh, replace all

**[16:35]** name than me. Um, just, uh, replace all my handle instances with your handle or

**[16:37]** my handle instances with your handle or

**[16:37]** my handle instances with your handle or whatever you want. Uh, since this is a

**[16:38]** whatever you want. Uh, since this is a

**[16:38]** whatever you want. Uh, since this is a shared instance, if we have too many

**[16:40]** shared instance, if we have too many

**[16:40]** shared instance, if we have too many collisions, I might jump to another

**[16:42]** collisions, I might jump to another

**[16:42]** collisions, I might jump to another instance that I have as a backup in the

**[16:43]** instance that I have as a backup in the

**[16:43]** instance that I have as a backup in the background. Uh but what I'm doing here

**[16:45]** background. Uh but what I'm doing here

**[16:45]** background. Uh but what I'm doing here is I'm creating my this analysis

**[16:48]** is I'm creating my this analysis

**[16:48]** is I'm creating my this analysis pipeline that I've looked at before like

**[16:49]** pipeline that I've looked at before like

**[16:49]** pipeline that I've looked at before like I'm throwing out the HTML. I use a

**[16:51]** I'm throwing out the HTML. I use a

**[16:51]** I'm throwing out the HTML. I use a standard tokenizer lowering stopwatch

**[16:54]** standard tokenizer lowering stopwatch

**[16:54]** standard tokenizer lowering stopwatch removal and stemming and then I I call

**[16:57]** removal and stemming and then I I call

**[16:57]** removal and stemming and then I I call this my analyzer and then I'm basically

**[16:59]** this my analyzer and then I'm basically


### [17:00 - 18:00]

**[17:00]** this my analyzer and then I'm basically applying this my analyzer on a field

**[17:02]** applying this my analyzer on a field

**[17:02]** applying this my analyzer on a field called uh quote. This we call this a

**[17:06]** called uh quote. This we call this a

**[17:06]** called uh quote. This we call this a mapping. It's kind of like the

**[17:07]** mapping. It's kind of like the

**[17:07]** mapping. It's kind of like the equivalent a schema in a relational

**[17:09]** equivalent a schema in a relational

**[17:09]** equivalent a schema in a relational database, but this defines how different

**[17:11]** database, but this defines how different

**[17:11]** database, but this defines how different fields behave. Um,

**[17:15]** fields behave. Um,

**[17:15]** fields behave. Um, okay. And somebody did not replace

**[17:18]** okay. And somebody did not replace

**[17:18]** okay. And somebody did not replace um

**[17:19]** um

**[17:20]** um the the query. Um,

**[17:23]** the the query. Um,

**[17:23]** the the query. Um, by the way, you need to keep user

**[17:26]** by the way, you need to keep user

**[17:26]** by the way, you need to keep user underscore. Um,

**[17:28]** underscore. Um,

**[17:28]** underscore. Um, let me let me quickly do this um

**[17:32]** let me let me quickly do this um

**[17:32]** let me let me quickly do this um myself.

**[17:35]** myself.

**[17:35]** myself. Oops.

**[17:37]** Oops.

**[17:38]** Oops. I should have seen this coming. Um,

**[17:46]** We want

**[17:46]** We want to replace

**[17:48]** to replace

**[17:48]** to replace and we'll use

**[17:51]** and we'll use

**[17:51]** and we'll use Oops.


### [18:00 - 19:00]

**[18:04]** Please don't copy that.

**[18:04]** Please don't copy that. Um, and I want to

**[18:23]** Let's try that again. Um,

**[18:23]** Let's try that again. Um, so we're creating our own index. Um, and

**[18:28]** so we're creating our own index. Um, and

**[18:28]** so we're creating our own index. Um, and now I just to double check I'll just

**[18:31]** now I just to double check I'll just

**[18:31]** now I just to double check I'll just again run this underscore analyze

**[18:34]** again run this underscore analyze

**[18:34]** again run this underscore analyze against this field that I've set up to

**[18:36]** against this field that I've set up to

**[18:36]** against this field that I've set up to just double check that I've set it up

**[18:38]** just double check that I've set it up

**[18:38]** just double check that I've set it up correctly. And now I'm actually starting

**[18:40]** correctly. And now I'm actually starting

**[18:40]** correctly. And now I'm actually starting to store documents. Um, bless you. Um,

**[18:43]** to store documents. Um, bless you. Um,

**[18:43]** to store documents. Um, bless you. Um, so we'll store these are not the droids

**[18:45]** so we'll store these are not the droids

**[18:45]** so we'll store these are not the droids you're looking for. Um, I have two

**[18:47]** you're looking for. Um, I have two

**[18:47]** you're looking for. Um, I have two others um that I'll index just so we

**[18:50]** others um that I'll index just so we

**[18:50]** others um that I'll index just so we have a bit more to search. Um, no, I am

**[18:53]** have a bit more to search. Um, no, I am

**[18:53]** have a bit more to search. Um, no, I am your father. Any guesses what will

**[18:55]** your father. Any guesses what will

**[18:55]** your father. Any guesses what will remain here.

**[18:58]** remain here.

**[18:58]** remain here. Father. Father. Yeah.


### [19:00 - 20:00]

**[19:03]** Father. Father. Yeah.

**[19:03]** Father. Father. Yeah. Okay. Let's let's try this out. Let me

**[19:05]** Okay. Let's let's try this out. Let me

**[19:05]** Okay. Let's let's try this out. Let me copy my

**[19:08]** copy my

**[19:08]** copy my This one actually has way fewer stoppers

**[19:10]** This one actually has way fewer stoppers

**[19:10]** This one actually has way fewer stoppers than you would expect. Uh let's quickly

**[19:13]** than you would expect. Uh let's quickly

**[19:13]** than you would expect. Uh let's quickly do this. Um

**[19:22]** since I didn't do the HTML removal,

**[19:22]** since I didn't do the HTML removal, let's take these out manually. So what

**[19:24]** let's take these out manually. So what

**[19:24]** let's take these out manually. So what you get is no, I am your father. And

**[19:28]** you get is no, I am your father. And

**[19:28]** you get is no, I am your father. And this was stupid because this was not

**[19:30]** this was stupid because this was not

**[19:30]** this was stupid because this was not what I wanted. We need to run this

**[19:32]** what I wanted. We need to run this

**[19:32]** what I wanted. We need to run this against the right analysis.

**[19:34]** against the right analysis.

**[19:34]** against the right analysis. Um,

**[19:45]** this happens when you copy paste. Okay.

**[19:45]** this happens when you copy paste. Okay. Um,

**[19:48]** Um,

**[19:48]** Um, uh,


### [20:00 - 21:00]

**[20:00]** sorry.

**[20:00]** sorry. And we'll do text.

**[20:10]** No, I think I've patched this back

**[20:10]** No, I think I've patched this back together. Okay, I am your father. So, no

**[20:13]** together. Okay, I am your father. So, no

**[20:13]** together. Okay, I am your father. So, no is the only stopper in this list.

**[20:14]** is the only stopper in this list.

**[20:14]** is the only stopper in this list. Actually, no was on the stop list. All

**[20:17]** Actually, no was on the stop list. All

**[20:17]** Actually, no was on the stop list. All the others are not. Um, okay. Let's try

**[20:21]** the others are not. Um, okay. Let's try

**[20:21]** the others are not. Um, okay. Let's try another one. Obi never told you what

**[20:24]** another one. Obi never told you what

**[20:24]** another one. Obi never told you what happened to your father.

**[20:27]** happened to your father.

**[20:27]** happened to your father. How many tokens will Obi-Wan be?

**[20:30]** How many tokens will Obi-Wan be?

**[20:30]** How many tokens will Obi-Wan be? Two. one.

**[20:38]** No, OB1 will will be two like OB1

**[20:38]** No, OB1 will will be two like OB1 because we used a default tokenizer or

**[20:40]** because we used a default tokenizer or

**[20:40]** because we used a default tokenizer or standard tokenizer. That one breaks up

**[20:42]** standard tokenizer. That one breaks up

**[20:42]** standard tokenizer. That one breaks up at dashes. If you had used another

**[20:44]** at dashes. If you had used another

**[20:44]** at dashes. If you had used another tokenizer like whitespace that would

**[20:46]** tokenizer like whitespace that would

**[20:46]** tokenizer like whitespace that would keep it together because that breaks up

**[20:48]** keep it together because that breaks up

**[20:48]** keep it together because that breaks up at white spaces. So there are various

**[20:50]** at white spaces. So there are various

**[20:50]** at white spaces. So there are various reasons why you want or would not want

**[20:52]** reasons why you want or would not want

**[20:52]** reasons why you want or would not want to do that. I don't want to go into all

**[20:53]** to do that. I don't want to go into all

**[20:53]** to do that. I don't want to go into all the details, but there are a lot of

**[20:55]** the details, but there are a lot of

**[20:55]** the details, but there are a lot of things to do right or wrong when you

**[20:57]** things to do right or wrong when you

**[20:57]** things to do right or wrong when you ingest the data which will then allow

**[20:58]** ingest the data which will then allow

**[20:58]** ingest the data which will then allow you to query the data in specific ways.


### [21:00 - 22:00]

**[21:01]** you to query the data in specific ways.

**[21:01]** you to query the data in specific ways. So for example, if you would have an

**[21:03]** So for example, if you would have an

**[21:03]** So for example, if you would have an email address,

**[21:10]** that one is also weirdly broken up. Like

**[21:10]** that one is also weirdly broken up. Like you might use like there's a dedicated

**[21:12]** you might use like there's a dedicated

**[21:12]** you might use like there's a dedicated tokenizer for URL email addresses. So

**[21:15]** tokenizer for URL email addresses. So

**[21:15]** tokenizer for URL email addresses. So depending on what type of data you have,

**[21:17]** depending on what type of data you have,

**[21:17]** depending on what type of data you have, you will need to process the data the

**[21:18]** you will need to process the data the

**[21:18]** you will need to process the data the right way because pretty much all the

**[21:20]** right way because pretty much all the

**[21:20]** right way because pretty much all the the smart pieces are kind of like adding

**[21:23]** the smart pieces are kind of like adding

**[21:23]** the smart pieces are kind of like adding here to make the search afterwards

**[21:25]** here to make the search afterwards

**[21:25]** here to make the search afterwards easier. Um so you can easily do that.

**[21:28]** easier. Um so you can easily do that.

**[21:28]** easier. Um so you can easily do that. Um, let's see. Let's index all my three

**[21:32]** Um, let's see. Let's index all my three

**[21:32]** Um, let's see. Let's index all my three documents so that we can actually search

**[21:34]** documents so that we can actually search

**[21:34]** documents so that we can actually search for them. Now, if I start searching

**[21:37]** for them. Now, if I start searching

**[21:37]** for them. Now, if I start searching droid,

**[21:39]** droid,

**[21:39]** droid, it should match. These are not the

**[21:40]** it should match. These are not the

**[21:40]** it should match. These are not the droids you're looking for. Yes or no?

**[21:43]** droids you're looking for. Yes or no?

**[21:43]** droids you're looking for. Yes or no? Because this one is singular and

**[21:45]** Because this one is singular and

**[21:45]** Because this one is singular and uppercase. And the droid that we stored

**[21:47]** uppercase. And the droid that we stored

**[21:47]** uppercase. And the droid that we stored was plural and lowerase. Will it match?

**[21:49]** was plural and lowerase. Will it match?

**[21:49]** was plural and lowerase. Will it match? Yes or no? Yes. Why?

**[21:57]** Uh, yes. We had the stemming. we have

**[21:57]** Uh, yes. We had the stemming. we have the lower casing and when we search so


### [22:00 - 23:00]

**[22:00]** the lower casing and when we search so

**[22:00]** the lower casing and when we search so we store the text it runs through this

**[22:02]** we store the text it runs through this

**[22:02]** we store the text it runs through this pipeline or the analysis um and for the

**[22:05]** pipeline or the analysis um and for the

**[22:05]** pipeline or the analysis um and for the search it does the same thing so it will

**[22:07]** search it does the same thing so it will

**[22:07]** search it does the same thing so it will lowerase the droid um it has stemmed

**[22:10]** lowerase the droid um it has stemmed

**[22:10]** lowerase the droid um it has stemmed down the droids in the text to droid and

**[22:12]** down the droids in the text to droid and

**[22:12]** down the droids in the text to droid and then we have an exact match um so what

**[22:15]** then we have an exact match um so what

**[22:16]** then we have an exact match um so what the the data structure behind the scene

**[22:18]** the the data structure behind the scene

**[22:18]** the the data structure behind the scene actually looks like

**[22:20]** actually looks like

**[22:20]** actually looks like the magic is kind of like in this

**[22:22]** the magic is kind of like in this

**[22:22]** the magic is kind of like in this so-called inverted index what the

**[22:23]** so-called inverted index what the

**[22:24]** so-called inverted index what the inverted index is is

**[22:27]** inverted index is is

**[22:27]** inverted index is is these are all the tokens that remained

**[22:29]** these are all the tokens that remained

**[22:29]** these are all the tokens that remained that I have extracted. I have

**[22:31]** that I have extracted. I have

**[22:31]** that I have extracted. I have alphabetically sorted them and they

**[22:33]** alphabetically sorted them and they

**[22:33]** alphabetically sorted them and they basically have a pointer and say in this

**[22:35]** basically have a pointer and say in this

**[22:35]** basically have a pointer and say in this document like with the ids one two three

**[22:37]** document like with the ids one two three

**[22:37]** document like with the ids one two three that I have stored we have how many

**[22:39]** that I have stored we have how many

**[22:40]** that I have stored we have how many occurrences like zero one um yeah

**[22:44]** occurrences like zero one um yeah

**[22:44]** occurrences like zero one um yeah nothing had two um and then we also know

**[22:48]** nothing had two um and then we also know

**[22:48]** nothing had two um and then we also know at which position they appeared. So

**[22:51]** at which position they appeared. So

**[22:51]** at which position they appeared. So search for droid. Now

**[22:53]** search for droid. Now

**[22:53]** search for droid. Now this is what I have stored. Um I will

**[22:56]** this is what I have stored. Um I will

**[22:56]** this is what I have stored. Um I will lowerase the droid to droid. I have an

**[22:58]** lowerase the droid to droid. I have an

**[22:58]** lowerase the droid to droid. I have an exact match here. Then I go through that

**[22:59]** exact match here. Then I go through that

**[22:59]** exact match here. Then I go through that list and see retrieve this document,


### [23:00 - 24:00]

**[23:01]** list and see retrieve this document,

**[23:01]** list and see retrieve this document, skip this one, skip this one. Um and at

**[23:03]** skip this one, skip this one. Um and at

**[23:04]** skip this one, skip this one. Um and at position four um you have that hit and

**[23:06]** position four um you have that hit and

**[23:06]** position four um you have that hit and then you could easily highlight that. So

**[23:07]** then you could easily highlight that. So

**[23:08]** then you could easily highlight that. So you have almost done all the hard work

**[23:09]** you have almost done all the hard work

**[23:09]** you have almost done all the hard work at ingestion and this retrieval

**[23:11]** at ingestion and this retrieval

**[23:11]** at ingestion and this retrieval afterwards will be very fast and

**[23:13]** afterwards will be very fast and

**[23:13]** afterwards will be very fast and efficient. That's the classic data

**[23:16]** efficient. That's the classic data

**[23:16]** efficient. That's the classic data structure for search. the inverted index

**[23:18]** structure for search. the inverted index

**[23:18]** structure for search. the inverted index where you have this alphabetic list uh

**[23:19]** where you have this alphabetic list uh

**[23:20]** where you have this alphabetic list uh of all the tokens that you've extracted

**[23:21]** of all the tokens that you've extracted

**[23:21]** of all the tokens that you've extracted to do that. Um and this will just be

**[23:24]** to do that. Um and this will just be

**[23:24]** to do that. Um and this will just be built in the background for you and

**[23:25]** built in the background for you and

**[23:25]** built in the background for you and that's how you can retrieve all of this.

**[23:27]** that's how you can retrieve all of this.

**[23:27]** that's how you can retrieve all of this. Um let's look at a few other um

**[23:32]** Um let's look at a few other um

**[23:32]** Um let's look at a few other um uh queries and how they behave. Um

**[23:36]** uh queries and how they behave. Um

**[23:36]** uh queries and how they behave. Um if I search for

**[23:38]** if I search for

**[23:38]** if I search for robot will I find anything?

**[23:43]** robot will I find anything?

**[23:43]** robot will I find anything? No, because there was no robot. Um there

**[23:46]** No, because there was no robot. Um there

**[23:46]** No, because there was no robot. Um there was a droid. Um we could now define a

**[23:49]** was a droid. Um we could now define a

**[23:50]** was a droid. Um we could now define a synonym and say like all uh droids are

**[23:53]** synonym and say like all uh droids are

**[23:53]** synonym and say like all uh droids are robots for example. Um

**[23:56]** robots for example. Um

**[23:56]** robots for example. Um who likes creating synonym lists?

**[23:59]** who likes creating synonym lists?


### [24:00 - 25:00]

**[24:00]** who likes creating synonym lists? Nobody anymore. Okay. No, normally I

**[24:02]** Nobody anymore. Okay. No, normally I

**[24:02]** Nobody anymore. Okay. No, normally I would have said that's the Stockholm

**[24:03]** would have said that's the Stockholm

**[24:03]** would have said that's the Stockholm syndrome because there's sometimes

**[24:04]** syndrome because there's sometimes

**[24:04]** syndrome because there's sometimes somebody who likes creating synonym

**[24:07]** somebody who likes creating synonym

**[24:07]** somebody who likes creating synonym lists because they've done that for so

**[24:08]** lists because they've done that for so

**[24:08]** lists because they've done that for so many years. Um but it got easier

**[24:10]** many years. Um but it got easier

**[24:10]** many years. Um but it got easier nowadays. Now you can use LLMs to

**[24:12]** nowadays. Now you can use LLMs to

**[24:12]** nowadays. Now you can use LLMs to generate your synonyms. So it can get a

**[24:14]** generate your synonyms. So it can get a

**[24:14]** generate your synonyms. So it can get a bit easier to create them, but they're

**[24:16]** bit easier to create them, but they're

**[24:16]** bit easier to create them, but they're still limited because you have always

**[24:17]** still limited because you have always

**[24:17]** still limited because you have always this mapping. Um, so with synonyms, you

**[24:20]** this mapping. Um, so with synonyms, you

**[24:20]** this mapping. Um, so with synonyms, you can expand the right way where it gets

**[24:22]** can expand the right way where it gets

**[24:22]** can expand the right way where it gets trickier if you have homonyms. Uh, if a

**[24:24]** trickier if you have homonyms. Uh, if a

**[24:24]** trickier if you have homonyms. Uh, if a word has multiple um, meanings like a

**[24:27]** word has multiple um, meanings like a

**[24:27]** word has multiple um, meanings like a bat could be the animal or it could be

**[24:29]** bat could be the animal or it could be

**[24:29]** bat could be the animal or it could be the thing you hit a ball with. Um, there

**[24:31]** the thing you hit a ball with. Um, there

**[24:32]** the thing you hit a ball with. Um, there it just gets trickier because there is

**[24:33]** it just gets trickier because there is

**[24:33]** it just gets trickier because there is there is no meaning behind the word or

**[24:35]** there is no meaning behind the word or

**[24:35]** there is no meaning behind the word or no context. So you just match strings.

**[24:37]** no context. So you just match strings.

**[24:37]** no context. So you just match strings. Um, and that is inherently limited. But

**[24:40]** Um, and that is inherently limited. But

**[24:40]** Um, and that is inherently limited. But like I said, it's dumb, but it scales

**[24:43]** like I said, it's dumb, but it scales

**[24:43]** like I said, it's dumb, but it scales very well and that's why it has been

**[24:45]** very well and that's why it has been

**[24:45]** very well and that's why it has been around for a long time and it does

**[24:47]** around for a long time and it does

**[24:47]** around for a long time and it does surprisingly well for many things

**[24:48]** surprisingly well for many things

**[24:48]** surprisingly well for many things because there's not a lot of things that

**[24:50]** because there's not a lot of things that

**[24:50]** because there's not a lot of things that are unexpected or that can go totally

**[24:52]** are unexpected or that can go totally

**[24:52]** are unexpected or that can go totally wrong. Um, now other things that you can

**[24:55]** wrong. Um, now other things that you can

**[24:55]** wrong. Um, now other things that you can do, you could do a a phrase search where

**[24:58]** do, you could do a a phrase search where

**[24:58]** do, you could do a a phrase search where you say, "I am your father." Um, will


### [25:00 - 26:00]

**[25:01]** you say, "I am your father." Um, will

**[25:01]** you say, "I am your father." Um, will this find anything?

**[25:04]** this find anything?

**[25:04]** this find anything? Yes. Yes. Because we had no I am your

**[25:08]** Yes. Yes. Because we had no I am your

**[25:08]** Yes. Yes. Because we had no I am your father. Um

**[25:11]** father. Um

**[25:11]** father. Um what happens if I say for example I am

**[25:17]** what happens if I say for example I am

**[25:17]** what happens if I say for example I am let's say I am not your father.

**[25:21]** let's say I am not your father.

**[25:21]** let's say I am not your father. Yes. No.

**[25:23]** Yes. No.

**[25:23]** Yes. No. No. Why? So you're right

**[25:37]** But you're right because the positions

**[25:37]** But you're right because the positions still don't match. Um, so the stop word

**[25:40]** still don't match. Um, so the stop word

**[25:40]** still don't match. Um, so the stop word not would be filtered out. Um, but it

**[25:43]** not would be filtered out. Um, but it

**[25:43]** not would be filtered out. Um, but it still doesn't match because the

**[25:44]** still doesn't match because the

**[25:44]** still doesn't match because the positions are off. Um,

**[25:47]** positions are off. Um,

**[25:47]** positions are off. Um, that is one of the things that sometimes

**[25:49]** that is one of the things that sometimes

**[25:49]** that is one of the things that sometimes can be confusing. So even if something

**[25:50]** can be confusing. So even if something

**[25:50]** can be confusing. So even if something is a stop and will be filtered out, uh,

**[25:52]** is a stop and will be filtered out, uh,

**[25:52]** is a stop and will be filtered out, uh, it doesn't work like that. Um one thing

**[25:55]** it doesn't work like that. Um one thing

**[25:55]** it doesn't work like that. Um one thing that you can do is though that the

**[25:57]** that you can do is though that the

**[25:57]** that you can do is though that the factor is called slop where you

**[25:59]** factor is called slop where you

**[25:59]** factor is called slop where you basically say if there is something


### [26:00 - 27:00]

**[26:01]** basically say if there is something

**[26:01]** basically say if there is something missing um it would still work. So I am

**[26:04]** missing um it would still work. So I am

**[26:04]** missing um it would still work. So I am your father and I am father with slop

**[26:08]** your father and I am father with slop

**[26:08]** your father and I am father with slop zero that's kind of like the implicit

**[26:09]** zero that's kind of like the implicit

**[26:09]** zero that's kind of like the implicit one um will not find anything. But if I

**[26:12]** one um will not find anything. But if I

**[26:12]** one um will not find anything. But if I say one then I basically say like there

**[26:14]** say one then I basically say like there

**[26:14]** say one then I basically say like there can be a one off in there like one word

**[26:16]** can be a one off in there like one word

**[26:16]** can be a one off in there like one word can be missing. Um

**[26:21]** can be missing. Um

**[26:21]** can be missing. Um uh

**[26:27]** however I am his father here. His would

**[26:27]** however I am his father here. His would not match. So this still will not work.

**[26:29]** not match. So this still will not work.

**[26:29]** not match. So this still will not work. Um the slop is really just to skip a

**[26:31]** Um the slop is really just to skip a

**[26:31]** Um the slop is really just to skip a word. Yeah. What about your father?

**[26:35]** word. Yeah. What about your father?

**[26:35]** word. Yeah. What about your father? I am your father.

**[26:45]** That will not work. How do

**[26:45]** That will not work. How do uh there you might need to do something

**[26:46]** uh there you might need to do something

**[26:46]** uh there you might need to do something like a synonym where you say slash um m

**[26:49]** like a synonym where you say slash um m

**[26:49]** like a synonym where you say slash um m gets replaced by m uh or we will need to

**[26:54]** gets replaced by m uh or we will need to

**[26:54]** gets replaced by m uh or we will need to have some more machine learning

**[26:55]** have some more machine learning

**[26:55]** have some more machine learning capabilities behind the scenes to to do

**[26:57]** capabilities behind the scenes to to do

**[26:57]** capabilities behind the scenes to to do stuff like that. Are there any libraries


### [27:00 - 28:00]

**[27:07]** like that? So what what is built in is

**[27:07]** like that? So what what is built in is generally a very simple set of rules. Um

**[27:10]** generally a very simple set of rules. Um

**[27:10]** generally a very simple set of rules. Um what you will need to do for things like

**[27:12]** what you will need to do for things like

**[27:12]** what you will need to do for things like this is normally you need a dictionary.

**[27:14]** this is normally you need a dictionary.

**[27:14]** this is normally you need a dictionary. Um the problem around these is they're

**[27:15]** Um the problem around these is they're

**[27:16]** Um the problem around these is they're normally not available for free or open

**[27:17]** normally not available for free or open

**[27:17]** normally not available for free or open source. Um funnily enough they're often

**[27:21]** source. Um funnily enough they're often

**[27:21]** source. Um funnily enough they're often coming out of uh university the

**[27:23]** coming out of uh university the

**[27:23]** coming out of uh university the dictionaries um because they have a lot

**[27:26]** dictionaries um because they have a lot

**[27:26]** dictionaries um because they have a lot of free labor the students. That's why

**[27:29]** of free labor the students. That's why

**[27:29]** of free labor the students. That's why the universities have been creating a

**[27:31]** the universities have been creating a

**[27:31]** the universities have been creating a lot of dictionaries but they often come

**[27:32]** lot of dictionaries but they often come

**[27:32]** lot of dictionaries but they often come out under the weirdest licenses that why

**[27:34]** out under the weirdest licenses that why

**[27:34]** out under the weirdest licenses that why they're not very widely available. But

**[27:36]** they're not very widely available. But

**[27:36]** they're not very widely available. But yes, there is a smarter or more powerful

**[27:39]** yes, there is a smarter or more powerful

**[27:39]** yes, there is a smarter or more powerful approach if you have a dictionary and

**[27:41]** approach if you have a dictionary and

**[27:41]** approach if you have a dictionary and you can do these things. Um, for

**[27:44]** you can do these things. Um, for

**[27:44]** you can do these things. Um, for example, um, one thing to to show is

**[27:46]** example, um, one thing to to show is

**[27:46]** example, um, one thing to to show is like, but maybe that's a good thing to

**[27:49]** like, but maybe that's a good thing to

**[27:49]** like, but maybe that's a good thing to to also mention. Um,

**[27:53]** to also mention. Um,

**[27:53]** to also mention. Um, you don't always get words out of the

**[27:55]** you don't always get words out of the

**[27:55]** you don't always get words out of the stemming. It's not a dictionary. It

**[27:57]** stemming. It's not a dictionary. It

**[27:57]** stemming. It's not a dictionary. It doesn't really get what you're doing. It

**[27:59]** doesn't really get what you're doing. It

**[27:59]** doesn't really get what you're doing. It just applies some rules. So for example


### [28:00 - 29:00]

**[28:01]** just applies some rules. So for example

**[28:01]** just applies some rules. So for example uh

**[28:03]** uh

**[28:03]** uh blackberry

**[28:05]** blackberry

**[28:05]** blackberry blackberry um h sorry blackberries I

**[28:09]** blackberry um h sorry blackberries I

**[28:09]** blackberry um h sorry blackberries I think that this will be stemmed down

**[28:11]** think that this will be stemmed down

**[28:11]** think that this will be stemmed down differently. Ah sorry I need English

**[28:14]** differently. Ah sorry I need English

**[28:14]** differently. Ah sorry I need English without English this will not work.

**[28:21]** So this will stem down to this weird

**[28:21]** So this will stem down to this weird word blackberry. Um and it will also

**[28:26]** word blackberry. Um and it will also

**[28:26]** word blackberry. Um and it will also stem down the singular to blackberry. So

**[28:28]** stem down the singular to blackberry. So

**[28:28]** stem down the singular to blackberry. So there's a rule that applies this uh but

**[28:31]** there's a rule that applies this uh but

**[28:31]** there's a rule that applies this uh but it's just a rule. It's not dictionary

**[28:32]** it's just a rule. It's not dictionary

**[28:32]** it's just a rule. It's not dictionary based. It's not very smart. Um and it

**[28:34]** based. It's not very smart. Um and it

**[28:34]** based. It's not very smart. Um and it only has some rules built in um that

**[28:37]** only has some rules built in um that

**[28:37]** only has some rules built in um that work for this, but you will definitely

**[28:38]** work for this, but you will definitely

**[28:38]** work for this, but you will definitely hit limits. Um

**[28:41]** hit limits. Um

**[28:41]** hit limits. Um the other thing, by the way, and why I

**[28:43]** the other thing, by the way, and why I

**[28:43]** the other thing, by the way, and why I picked Blackberry as an example, um you

**[28:45]** picked Blackberry as an example, um you

**[28:45]** picked Blackberry as an example, um you have some annoying languages like

**[28:47]** have some annoying languages like

**[28:47]** have some annoying languages like German, Korean, and others that compound

**[28:50]** German, Korean, and others that compound

**[28:50]** German, Korean, and others that compound nouns like Blackberry. Um where you have

**[28:53]** nouns like Blackberry. Um where you have

**[28:53]** nouns like Blackberry. Um where you have basically two words. um black would

**[28:55]** basically two words. um black would

**[28:55]** basically two words. um black would never find Blackberry in the simplest

**[28:57]** never find Blackberry in the simplest

**[28:57]** never find Blackberry in the simplest form because it's not a complete string.


### [29:00 - 30:00]

**[29:01]** form because it's not a complete string.

**[29:01]** form because it's not a complete string. There are various ways to work around

**[29:02]** There are various ways to work around

**[29:02]** There are various ways to work around that um that all come with their own

**[29:04]** that um that all come with their own

**[29:04]** that um that all come with their own downsides. Um and either you have a

**[29:06]** downsides. Um and either you have a

**[29:06]** downsides. Um and either you have a dictionary or you extract the so-called

**[29:08]** dictionary or you extract the so-called

**[29:08]** dictionary or you extract the so-called engrams. It's like group of words and

**[29:10]** engrams. It's like group of words and

**[29:10]** engrams. It's like group of words and then you mention group of words. Um but

**[29:12]** then you mention group of words. Um but

**[29:12]** then you mention group of words. Um but all of those are one of the many tools

**[29:15]** all of those are one of the many tools

**[29:15]** all of those are one of the many tools how we try to make this a bit better or

**[29:17]** how we try to make this a bit better or

**[29:17]** how we try to make this a bit better or smarter. But it all has limitations.

**[29:20]** smarter. But it all has limitations.

**[29:20]** smarter. But it all has limitations. I hope that answers the question and

**[29:22]** I hope that answers the question and

**[29:22]** I hope that answers the question and makes sense. Um so there are

**[29:24]** makes sense. Um so there are

**[29:24]** makes sense. Um so there are dictionaries but they're generally not

**[29:26]** dictionaries but they're generally not

**[29:26]** dictionaries but they're generally not free or not under an easy license

**[29:28]** free or not under an easy license

**[29:28]** free or not under an easy license available for some languages by the way.

**[29:30]** available for some languages by the way.

**[29:30]** available for some languages by the way. Um even the the stemmers are not freely

**[29:33]** Um even the the stemmers are not freely

**[29:33]** Um even the the stemmers are not freely available. I think there is a stemmer or

**[29:36]** available. I think there is a stemmer or

**[29:36]** available. I think there is a stemmer or analyzer for Hebrew. I think that has

**[29:39]** analyzer for Hebrew. I think that has

**[29:39]** analyzer for Hebrew. I think that has also like some commercial license or at

**[29:41]** also like some commercial license or at

**[29:41]** also like some commercial license or at least the you can't use it for free in

**[29:43]** least the you can't use it for free in

**[29:43]** least the you can't use it for free in commercial products. Um

**[29:47]** commercial products. Um

**[29:47]** commercial products. Um though licensing with machine learning

**[29:48]** though licensing with machine learning

**[29:48]** though licensing with machine learning models is also its own dark secret. Um

**[29:52]** models is also its own dark secret. Um

**[29:52]** models is also its own dark secret. Um yeah


### [30:00 - 31:00]

**[30:11]** yes and that is what an engram is doing.

**[30:11]** yes and that is what an engram is doing. Let me let me see if I can um

**[30:21]** an engram is normally a a word group

**[30:21]** an engram is normally a a word group normally a tri group. This is way too

**[30:23]** normally a tri group. This is way too

**[30:23]** normally a tri group. This is way too small. Um

**[30:26]** small. Um

**[30:26]** small. Um somehow I have weirdly overwritten my

**[30:29]** somehow I have weirdly overwritten my

**[30:29]** somehow I have weirdly overwritten my command plus so I can't use that. Let me

**[30:31]** command plus so I can't use that. Let me

**[30:31]** command plus so I can't use that. Let me make this slightly larger.

**[30:43]** Okay. Um here um we basically use one or

**[30:43]** Okay. Um here um we basically use one or two letters as word groups which which

**[30:45]** two letters as word groups which which

**[30:45]** two letters as word groups which which is way too small but uh just to um show

**[30:49]** is way too small but uh just to um show

**[30:49]** is way too small but uh just to um show the example and this is very hard to

**[30:50]** the example and this is very hard to

**[30:50]** the example and this is very hard to read. Let let me copy that over to my

**[30:52]** read. Let let me copy that over to my

**[30:52]** read. Let let me copy that over to my console that there you can um


### [31:00 - 32:00]

**[31:00]** there you can oops there you can see

**[31:00]** there you can oops there you can see this but this is a great question. Um so

**[31:03]** this but this is a great question. Um so

**[31:03]** this but this is a great question. Um so we'll use engram for quickf fox and then

**[31:07]** we'll use engram for quickf fox and then

**[31:07]** we'll use engram for quickf fox and then you can see the tokens that I extract

**[31:08]** you can see the tokens that I extract

**[31:08]** you can see the tokens that I extract here are the first letter the first two

**[31:11]** here are the first letter the first two

**[31:11]** here are the first letter the first two um the second the second and third etc.

**[31:14]** um the second the second and third etc.

**[31:14]** um the second the second and third etc. And you end up with a ton of tokens. The

**[31:17]** And you end up with a ton of tokens. The

**[31:17]** And you end up with a ton of tokens. The the downside is a you have to do more

**[31:19]** the downside is a you have to do more

**[31:19]** the downside is a you have to do more work when you store this. Um, B, it

**[31:22]** work when you store this. Um, B, it

**[31:22]** work when you store this. Um, B, it creates a lot of storage on disk because

**[31:24]** creates a lot of storage on disk because

**[31:24]** creates a lot of storage on disk because you extract so many different tokens and

**[31:26]** you extract so many different tokens and

**[31:26]** you extract so many different tokens and then your search will also be pretty

**[31:27]** then your search will also be pretty

**[31:27]** then your search will also be pretty expensive because normally you would at

**[31:30]** expensive because normally you would at

**[31:30]** expensive because normally you would at least do three like triagrams. Um, but

**[31:34]** least do three like triagrams. Um, but

**[31:34]** least do three like triagrams. Um, but even that creates a tons of tokens and

**[31:36]** even that creates a tons of tokens and

**[31:36]** even that creates a tons of tokens and the tons of matches and then you need to

**[31:37]** the tons of matches and then you need to

**[31:37]** the tons of matches and then you need to find the ones with the most matches and

**[31:39]** find the ones with the most matches and

**[31:39]** find the ones with the most matches and it works but a it is pretty expensive in

**[31:43]** it works but a it is pretty expensive in

**[31:43]** it works but a it is pretty expensive in disk but also query time. Um, and it

**[31:45]** disk but also query time. Um, and it

**[31:45]** disk but also query time. Um, and it might also create undesired results or

**[31:48]** might also create undesired results or

**[31:48]** might also create undesired results or results that are a bit unexpected for

**[31:49]** results that are a bit unexpected for

**[31:50]** results that are a bit unexpected for the end user. It is I would call it a

**[31:52]** the end user. It is I would call it a

**[31:52]** the end user. It is I would call it a it's it's again it's a very dumb tool

**[31:55]** it's it's again it's a very dumb tool

**[31:55]** it's it's again it's a very dumb tool that works reasonably well for some

**[31:57]** that works reasonably well for some

**[31:57]** that works reasonably well for some scenarios. Um, but it's only one of many

**[31:59]** scenarios. Um, but it's only one of many

**[31:59]** scenarios. Um, but it's only one of many potential factors. Um, what you could


### [32:00 - 33:00]

**[32:02]** potential factors. Um, what you could

**[32:02]** potential factors. Um, what you could potentially do is, and I I don't have a

**[32:05]** potentially do is, and I I don't have a

**[32:05]** potentially do is, and I I don't have a full example for that, but we could

**[32:06]** full example for that, but we could

**[32:06]** full example for that, but we could build it quickly. Um, what you would do

**[32:08]** build it quickly. Um, what you would do

**[32:08]** build it quickly. Um, what you would do in reality probably um you might store a

**[32:11]** in reality probably um you might store a

**[32:11]** in reality probably um you might store a text more than one ways. So you might

**[32:13]** text more than one ways. So you might

**[32:13]** text more than one ways. So you might store it like with stop words and

**[32:15]** store it like with stop words and

**[32:15]** store it like with stop words and without stop words and maybe with

**[32:17]** without stop words and maybe with

**[32:17]** without stop words and maybe with engrams and then you give a lower weight

**[32:20]** engrams and then you give a lower weight

**[32:20]** engrams and then you give a lower weight to the engrams and say like if I have an

**[32:22]** to the engrams and say like if I have an

**[32:22]** to the engrams and say like if I have an exact match then I want this first but

**[32:24]** exact match then I want this first but

**[32:24]** exact match then I want this first but if I don't have anything in the exact

**[32:26]** if I don't have anything in the exact

**[32:26]** if I don't have anything in the exact matches then I want to look into my

**[32:27]** matches then I want to look into my

**[32:27]** matches then I want to look into my engram list and then I want to kind of

**[32:29]** engram list and then I want to kind of

**[32:30]** engram list and then I want to kind of like take whatever is coming up next. Um

**[32:33]** like take whatever is coming up next. Um

**[32:33]** like take whatever is coming up next. Um so

**[32:35]** so

**[32:35]** so even keyword based search will be more

**[32:37]** even keyword based search will be more

**[32:37]** even keyword based search will be more complex if you combine different

**[32:38]** complex if you combine different

**[32:38]** complex if you combine different methods. Um,

**[32:40]** methods. Um,

**[32:40]** methods. Um, engrams are interesting, but again,

**[32:43]** engrams are interesting, but again,

**[32:43]** engrams are interesting, but again, they're a dumb but pretty heavy hammer.

**[32:45]** they're a dumb but pretty heavy hammer.

**[32:45]** they're a dumb but pretty heavy hammer. Use them with the right at the right

**[32:47]** Use them with the right at the right

**[32:47]** Use them with the right at the right scenario.

**[32:49]** scenario.

**[32:50]** scenario. This is by default one or two. Yes, but

**[32:53]** This is by default one or two. Yes, but

**[32:53]** This is by default one or two. Yes, but you you could redefine that. So, we can

**[32:56]** you you could redefine that. So, we can

**[32:56]** you you could redefine that. So, we can uh we can let me go back to the docs.

**[32:59]** uh we can let me go back to the docs.

**[32:59]** uh we can let me go back to the docs. The the engram you can uh say min and


### [33:00 - 34:00]

**[33:03]** The the engram you can uh say min and

**[33:03]** The the engram you can uh say min and max gram. If you set both to three, you

**[33:05]** max gram. If you set both to three, you

**[33:05]** max gram. If you set both to three, you would have triagrams. So it's always

**[33:07]** would have triagrams. So it's always

**[33:07]** would have triagrams. So it's always groups of three like

**[33:09]** groups of three like

**[33:09]** groups of three like 1 2 3 2 3 4 etc. Um you could also have

**[33:12]** 1 2 3 2 3 4 etc. Um you could also have

**[33:12]** 1 2 3 2 3 4 etc. Um you could also have something called edge engram where you

**[33:14]** something called edge engram where you

**[33:14]** something called edge engram where you expect that somebody types the first few

**[33:16]** expect that somebody types the first few

**[33:16]** expect that somebody types the first few letters right h and then you only start

**[33:18]** letters right h and then you only start

**[33:18]** letters right h and then you only start from the beginning but not in the middle

**[33:19]** from the beginning but not in the middle

**[33:19]** from the beginning but not in the middle of the word which sometimes avoids

**[33:22]** of the word which sometimes avoids

**[33:22]** of the word which sometimes avoids unexpected results and of course reduces

**[33:25]** unexpected results and of course reduces

**[33:25]** unexpected results and of course reduces the number of tokens um quite a bit. Um

**[33:28]** the number of tokens um quite a bit. Um

**[33:28]** the number of tokens um quite a bit. Um so somewhere in here um

**[33:33]** so somewhere in here um

**[33:33]** so somewhere in here um edge engram

**[33:40]** let's just copy that over so I won't

**[33:40]** let's just copy that over so I won't type and

**[33:43]** type and

**[33:43]** type and so here we have edge engram with quick

**[33:46]** so here we have edge engram with quick

**[33:46]** so here we have edge engram with quick and you can see it only does

**[33:49]** and you can see it only does

**[33:49]** and you can see it only does first and the first two letters but

**[33:51]** first and the first two letters but

**[33:51]** first and the first two letters but nothing else and in reality you would

**[33:53]** nothing else and in reality you would

**[33:53]** nothing else and in reality you would probably define this like 225 or more

**[33:55]** probably define this like 225 or more

**[33:56]** probably define this like 225 or more whatever else you want. Uh but here we

**[33:58]** whatever else you want. Uh but here we

**[33:58]** whatever else you want. Uh but here we only do from the start and nothing else.


### [34:00 - 35:00]

**[34:00]** only do from the start and nothing else.

**[34:00]** only do from the start and nothing else. Uh which reduces the tokens

**[34:02]** Uh which reduces the tokens

**[34:02]** Uh which reduces the tokens tremendously.

**[34:03]** tremendously.

**[34:03]** tremendously. But of course if you have black berry

**[34:06]** But of course if you have black berry

**[34:06]** But of course if you have black berry and you want to match the berry, you're

**[34:08]** and you want to match the berry, you're

**[34:08]** and you want to match the berry, you're out of luck.

**[34:17]** Anybody else? Anything else?

**[34:18]** Anybody else? Anything else? Sure.

**[34:28]** Yeah. So if you have multiple languages,

**[34:28]** Yeah. So if you have multiple languages, um do not mix them up. That will just

**[34:31]** um do not mix them up. That will just

**[34:31]** um do not mix them up. That will just create chaos. Uh because we'll get to

**[34:33]** create chaos. Uh because we'll get to

**[34:33]** create chaos. Uh because we'll get to that in a moment. But how keyword search

**[34:35]** that in a moment. But how keyword search

**[34:35]** that in a moment. But how keyword search works is basically word frequencies and

**[34:37]** works is basically word frequencies and

**[34:37]** works is basically word frequencies and it if you mix languages, it screws up

**[34:39]** it if you mix languages, it screws up

**[34:39]** it if you mix languages, it screws up all frequencies and statistics. Um so

**[34:42]** all frequencies and statistics. Um so

**[34:42]** all frequencies and statistics. Um so what you would do is either you would

**[34:44]** what you would do is either you would

**[34:44]** what you would do is either you would have um

**[34:48]** have um

**[34:48]** have um you could do two things uh to do um

**[34:52]** you could do two things uh to do um

**[34:52]** you could do two things uh to do um if you have English and Hebrew. Uh you

**[34:55]** if you have English and Hebrew. Uh you

**[34:55]** if you have English and Hebrew. Uh you could either do field English and then

**[34:59]** could either do field English and then

**[34:59]** could either do field English and then you would have


### [35:00 - 36:00]

**[35:07]** field uh whatever the abbreviation for

**[35:07]** field uh whatever the abbreviation for Hebrew is. um Hebrew uh oops

**[35:12]** Hebrew is. um Hebrew uh oops

**[35:12]** Hebrew is. um Hebrew uh oops and then you would have that and then

**[35:14]** and then you would have that and then

**[35:14]** and then you would have that and then you would need to define the right

**[35:15]** you would need to define the right

**[35:15]** you would need to define the right analyzer for that specific field but so

**[35:17]** analyzer for that specific field but so

**[35:17]** analyzer for that specific field but so you break it out either into different

**[35:19]** you break it out either into different

**[35:19]** you break it out either into different fields or you could even do different

**[35:20]** fields or you could even do different

**[35:20]** fields or you could even do different indices um and ideally we even have that

**[35:25]** indices um and ideally we even have that

**[35:26]** indices um and ideally we even have that built in um we have a language analyzer

**[35:28]** built in um we have a language analyzer

**[35:28]** built in um we have a language analyzer even if you just provide a couple of

**[35:29]** even if you just provide a couple of

**[35:29]** even if you just provide a couple of words it will guess or not guess it will

**[35:33]** words it will guess or not guess it will

**[35:33]** words it will guess or not guess it will infer the language um with a very high

**[35:36]** infer the language um with a very high

**[35:36]** infer the language um with a very high uh degree of certainty. Um especially

**[35:39]** uh degree of certainty. Um especially

**[35:39]** uh degree of certainty. Um especially Hebrew will be very easy to identify. If

**[35:41]** Hebrew will be very easy to identify. If

**[35:42]** Hebrew will be very easy to identify. If you have your own diiorits, it's easy.

**[35:43]** you have your own diiorits, it's easy.

**[35:43]** you have your own diiorits, it's easy. Um but even if you just throw random

**[35:45]** Um but even if you just throw random

**[35:45]** Um but even if you just throw random languages at it, it will have a very

**[35:47]** languages at it, it will have a very

**[35:47]** languages at it, it will have a very good chance like just with a few words

**[35:49]** good chance like just with a few words

**[35:49]** good chance like just with a few words to know this is this language and then

**[35:51]** to know this is this language and then

**[35:51]** to know this is this language and then you can treat it the right way.


### [36:00 - 37:00]

**[36:05]** good. Let's continue. Um so we have done

**[36:05]** good. Let's continue. Um so we have done all of these searches. Uh we have done

**[36:08]** all of these searches. Uh we have done

**[36:08]** all of these searches. Uh we have done slope. Uh one more thing before we get

**[36:11]** slope. Uh one more thing before we get

**[36:11]** slope. Uh one more thing before we get into the the relevance. One other very

**[36:14]** into the the relevance. One other very

**[36:14]** into the the relevance. One other very heavy hammer um that people often

**[36:17]** heavy hammer um that people often

**[36:17]** heavy hammer um that people often overuse is fuzziness. Uh so bless you.

**[36:21]** overuse is fuzziness. Uh so bless you.

**[36:21]** overuse is fuzziness. Uh so bless you. If you have a misspelling so I

**[36:24]** If you have a misspelling so I

**[36:24]** If you have a misspelling so I misspelled oban Kinoi. Uh we already

**[36:27]** misspelled oban Kinoi. Uh we already

**[36:27]** misspelled oban Kinoi. Uh we already know that this is broken out into two

**[36:29]** know that this is broken out into two

**[36:29]** know that this is broken out into two different words or tokens. um it will

**[36:31]** different words or tokens. um it will

**[36:31]** different words or tokens. um it will still match your oban because we have

**[36:33]** still match your oban because we have

**[36:33]** still match your oban because we have this fuzziness uh which uh allows edits.

**[36:37]** this fuzziness uh which uh allows edits.

**[36:37]** this fuzziness uh which uh allows edits. It's like a it's a Levenstein distance.

**[36:39]** It's like a it's a Levenstein distance.

**[36:39]** It's like a it's a Levenstein distance. So you can have one by default here. You

**[36:43]** So you can have one by default here. You

**[36:43]** So you can have one by default here. You could either give it an absolute value

**[36:45]** could either give it an absolute value

**[36:45]** could either give it an absolute value like you can have one edit which could

**[36:47]** like you can have one edit which could

**[36:47]** like you can have one edit which could be one character too much, too little or

**[36:50]** be one character too much, too little or

**[36:50]** be one character too much, too little or one character different. Uh you could

**[36:52]** one character different. Uh you could

**[36:52]** one character different. Uh you could set it to two or three. You can't do

**[36:55]** set it to two or three. You can't do

**[36:55]** set it to two or three. You can't do more because otherwise uh you match

**[36:57]** more because otherwise uh you match

**[36:57]** more because otherwise uh you match almost anything. Um, and auto will auto


### [37:00 - 38:00]

**[37:01]** almost anything. Um, and auto will auto

**[37:01]** almost anything. Um, and auto will auto is kind of smart because auto depending

**[37:03]** is kind of smart because auto depending

**[37:03]** is kind of smart because auto depending on how long the token that you're

**[37:05]** on how long the token that you're

**[37:05]** on how long the token that you're searching for is uh will set a specific

**[37:07]** searching for is uh will set a specific

**[37:07]** searching for is uh will set a specific value. Um, if you have zero to two

**[37:10]** value. Um, if you have zero to two

**[37:10]** value. Um, if you have zero to two characters, autofuzzness I think is one

**[37:12]** characters, autofuzzness I think is one

**[37:12]** characters, autofuzzness I think is one from um two to no zero to two characters

**[37:16]** from um two to no zero to two characters

**[37:16]** from um two to no zero to two characters is zero. Uh three to five characters is

**[37:19]** is zero. Uh three to five characters is

**[37:19]** is zero. Uh three to five characters is one and after that it's two. Um

**[37:23]** one and after that it's two. Um

**[37:23]** one and after that it's two. Um so you can match these. Um,

**[37:27]** so you can match these. Um,

**[37:27]** so you can match these. Um, will this one match?

**[37:43]** Yes. So, we have we have both of those

**[37:43]** Yes. So, we have we have both of those are misspelled.

**[37:56]** Yes, that is a bit of a gotcha. Um, so

**[37:56]** Yes, that is a bit of a gotcha. Um, so yes, you need to know the tokenizer. So

**[37:57]** yes, you need to know the tokenizer. So

**[37:58]** yes, you need to know the tokenizer. So we tokenize with standard. So it's two

**[37:59]** we tokenize with standard. So it's two

**[37:59]** we tokenize with standard. So it's two tokens and then the fitness applies per


### [38:00 - 39:00]

**[38:01]** tokens and then the fitness applies per

**[38:01]** tokens and then the fitness applies per token,

**[38:03]** token,

**[38:03]** token, which is another slightly surprising

**[38:05]** which is another slightly surprising

**[38:05]** which is another slightly surprising thing. Uh, but yes, that's how you end

**[38:06]** thing. Uh, but yes, that's how you end

**[38:06]** thing. Uh, but yes, that's how you end up here. Um, okay. Now,

**[38:12]** up here. Um, okay. Now,

**[38:12]** up here. Um, okay. Now, we could look at like the how the

**[38:14]** we could look at like the how the

**[38:14]** we could look at like the how the Levenstein distance works behind the

**[38:15]** Levenstein distance works behind the

**[38:15]** Levenstein distance works behind the scenes, but it's it's basically a

**[38:18]** scenes, but it's it's basically a

**[38:18]** scenes, but it's it's basically a Levenstein automaton. um which looks

**[38:21]** Levenstein automaton. um which looks

**[38:21]** Levenstein automaton. um which looks something like this. If you search for

**[38:22]** something like this. If you search for

**[38:22]** something like this. If you search for food and you have two edits, this is how

**[38:24]** food and you have two edits, this is how

**[38:24]** food and you have two edits, this is how the automaton would work in the

**[38:25]** the automaton would work in the

**[38:25]** the automaton would work in the background to figure out like what are

**[38:27]** background to figure out like what are

**[38:27]** background to figure out like what are all the possible permutations. Um it's a

**[38:29]** all the possible permutations. Um it's a

**[38:29]** all the possible permutations. Um it's a fancy algorithm uh that was I think

**[38:31]** fancy algorithm uh that was I think

**[38:31]** fancy algorithm uh that was I think pretty hard to implement. Uh but uh it's

**[38:33]** pretty hard to implement. Uh but uh it's

**[38:33]** pretty hard to implement. Uh but uh it's in uh lucine nowadays. Um okay, now

**[38:37]** in uh lucine nowadays. Um okay, now

**[38:38]** in uh lucine nowadays. Um okay, now let's talk about scoring. Uh one thing

**[38:39]** let's talk about scoring. Uh one thing

**[38:39]** let's talk about scoring. Uh one thing that you have seen that you don't have

**[38:41]** that you have seen that you don't have

**[38:41]** that you have seen that you don't have anywhere or in a non-arch engine or just

**[38:44]** anywhere or in a non-arch engine or just

**[38:44]** anywhere or in a non-arch engine or just in a database is like we have the scores

**[38:46]** in a database is like we have the scores

**[38:46]** in a database is like we have the scores like how well does this match? Um

**[38:49]** like how well does this match? Um

**[38:50]** like how well does this match? Um how does a score work here? Um

**[38:53]** how does a score work here? Um

**[38:53]** how does a score work here? Um let's look at the the details of that

**[38:55]** let's look at the the details of that

**[38:55]** let's look at the the details of that one.

**[38:58]** one.

**[38:58]** one. Um so the the basic algorithm which is


### [39:00 - 40:00]

**[39:00]** Um so the the basic algorithm which is

**[39:00]** Um so the the basic algorithm which is also most of us or pretty much all of us

**[39:02]** also most of us or pretty much all of us

**[39:02]** also most of us or pretty much all of us here um term frequency inverse document

**[39:05]** here um term frequency inverse document

**[39:06]** here um term frequency inverse document frequency or TF um it has been slightly

**[39:09]** frequency or TF um it has been slightly

**[39:09]** frequency or TF um it has been slightly tweaked like the new implementation is

**[39:11]** tweaked like the new implementation is

**[39:11]** tweaked like the new implementation is called BM25 which stands for best match

**[39:14]** called BM25 which stands for best match

**[39:14]** called BM25 which stands for best match and it's the 25th iteration of the best

**[39:16]** and it's the 25th iteration of the best

**[39:16]** and it's the 25th iteration of the best match algorithm. Um, so what they look

**[39:18]** match algorithm. Um, so what they look

**[39:18]** match algorithm. Um, so what they look like is, um, you have the term

**[39:21]** like is, um, you have the term

**[39:21]** like is, um, you have the term frequency. If I search for droid, how

**[39:23]** frequency. If I search for droid, how

**[39:23]** frequency. If I search for droid, how many times does Droid appear in the text

**[39:25]** many times does Droid appear in the text

**[39:25]** many times does Droid appear in the text that I'm looking for? Um, and it's

**[39:28]** that I'm looking for? Um, and it's

**[39:28]** that I'm looking for? Um, and it's basically the square root of that. So

**[39:30]** basically the square root of that. So

**[39:30]** basically the square root of that. So the assumption is, um, if a text

**[39:32]** the assumption is, um, if a text

**[39:32]** the assumption is, um, if a text contains droid once, this is the

**[39:34]** contains droid once, this is the

**[39:34]** contains droid once, this is the relevancy. If I have a text that

**[39:36]** relevancy. If I have a text that

**[39:36]** relevancy. If I have a text that contains droid 10 times, um, this is the

**[39:39]** contains droid 10 times, um, this is the

**[39:39]** contains droid 10 times, um, this is the relevancy. The tweak between TF, that

**[39:42]** relevancy. The tweak between TF, that

**[39:42]** relevancy. The tweak between TF, that one just keeps growing. uh BM25 says

**[39:45]** one just keeps growing. uh BM25 says

**[39:45]** one just keeps growing. uh BM25 says like once you hit like five droids in a

**[39:47]** like once you hit like five droids in a

**[39:47]** like once you hit like five droids in a text it doesn't really get much more

**[39:49]** text it doesn't really get much more

**[39:49]** text it doesn't really get much more relevant anymore. Um so it kind of like

**[39:51]** relevant anymore. Um so it kind of like

**[39:51]** relevant anymore. Um so it kind of like flattens out the curve. Um that is the

**[39:53]** flattens out the curve. Um that is the

**[39:53]** flattens out the curve. Um that is the idea of term frequency. Um the next

**[39:56]** idea of term frequency. Um the next

**[39:56]** idea of term frequency. Um the next thing is the inverse document frequency

**[39:59]** thing is the inverse document frequency

**[39:59]** thing is the inverse document frequency um which is almost the inverse curve.


### [40:00 - 41:00]

**[40:02]** um which is almost the inverse curve.

**[40:02]** um which is almost the inverse curve. The assumption here is over my entire

**[40:05]** The assumption here is over my entire

**[40:06]** The assumption here is over my entire text body. This is how often the term

**[40:09]** text body. This is how often the term

**[40:09]** text body. This is how often the term droid appears. So if a term is rare, it

**[40:12]** droid appears. So if a term is rare, it

**[40:12]** droid appears. So if a term is rare, it is much more relevant than if a term is

**[40:15]** is much more relevant than if a term is

**[40:15]** is much more relevant than if a term is uh very common. Then it's kind of like

**[40:17]** uh very common. Then it's kind of like

**[40:17]** uh very common. Then it's kind of like less relevant. Basically the assumption

**[40:18]** less relevant. Basically the assumption

**[40:18]** less relevant. Basically the assumption is rare is relevant and interesting.

**[40:21]** is rare is relevant and interesting.

**[40:21]** is rare is relevant and interesting. Very common is not very interesting

**[40:22]** Very common is not very interesting

**[40:22]** Very common is not very interesting anymore. Uh and then it's kind of like

**[40:24]** anymore. Uh and then it's kind of like

**[40:24]** anymore. Uh and then it's kind of like just uh works its curve out like that.

**[40:28]** just uh works its curve out like that.

**[40:28]** just uh works its curve out like that. Um and the final thing is uh the field

**[40:31]** Um and the final thing is uh the field

**[40:31]** Um and the final thing is uh the field length norm is like the shorter a field

**[40:34]** length norm is like the shorter a field

**[40:34]** length norm is like the shorter a field is and you have a match the more

**[40:36]** is and you have a match the more

**[40:36]** is and you have a match the more relevant it is which assumes like if you

**[40:39]** relevant it is which assumes like if you

**[40:39]** relevant it is which assumes like if you have a short title and your keyword

**[40:40]** have a short title and your keyword

**[40:40]** have a short title and your keyword appears there it's much more relevant

**[40:42]** appears there it's much more relevant

**[40:42]** appears there it's much more relevant than if there's a very long text body

**[40:43]** than if there's a very long text body

**[40:43]** than if there's a very long text body and your keyword or and you have a match

**[40:45]** and your keyword or and you have a match

**[40:45]** and your keyword or and you have a match there. Um and these are the three main

**[40:48]** there. Um and these are the three main

**[40:48]** there. Um and these are the three main components of uh TF. So let's take a

**[40:51]** components of uh TF. So let's take a

**[40:51]** components of uh TF. So let's take a look at how this looks like. Um

**[40:54]** look at how this looks like. Um

**[40:54]** look at how this looks like. Um you can make this a bit more

**[40:55]** you can make this a bit more

**[40:55]** you can make this a bit more complicated. um


### [41:00 - 42:00]

**[41:03]** you why something matches. Don't be

**[41:03]** you why something matches. Don't be confused by the or let me take that out

**[41:05]** confused by the or let me take that out

**[41:05]** confused by the or let me take that out for the first try. So I'm looking for

**[41:07]** for the first try. So I'm looking for

**[41:07]** for the first try. So I'm looking for father and I am uh no I am your father

**[41:10]** father and I am uh no I am your father

**[41:10]** father and I am uh no I am your father and Obi-Wan never told you what happened

**[41:13]** and Obi-Wan never told you what happened

**[41:13]** and Obi-Wan never told you what happened to your father. Um

**[41:15]** to your father. Um

**[41:15]** to your father. Um one is more relevant than the other. Why

**[41:17]** one is more relevant than the other. Why

**[41:17]** one is more relevant than the other. Why is the first one more relevant than the

**[41:19]** is the first one more relevant than the

**[41:19]** is the first one more relevant than the second one?

**[41:21]** second one?

**[41:21]** second one? Yeah. Term frequency is the same. both

**[41:24]** Yeah. Term frequency is the same. both

**[41:24]** Yeah. Term frequency is the same. both contain contain uh father ones. The uh

**[41:27]** contain contain uh father ones. The uh

**[41:27]** contain contain uh father ones. The uh inverse documentary frequency is also

**[41:30]** inverse documentary frequency is also

**[41:30]** inverse documentary frequency is also the same because we're looking for the

**[41:32]** the same because we're looking for the

**[41:32]** the same because we're looking for the same term. Uh the only difference is

**[41:33]** same term. Uh the only difference is

**[41:33]** same term. Uh the only difference is that the second one is longer than the

**[41:36]** that the second one is longer than the

**[41:36]** that the second one is longer than the first one. Um and that's why it's um

**[41:39]** first one. Um and that's why it's um

**[41:39]** first one. Um and that's why it's um more relevant here. Um so this is very

**[41:43]** more relevant here. Um so this is very

**[41:43]** more relevant here. Um so this is very simple and you can then if you're unsure

**[41:46]** simple and you can then if you're unsure

**[41:46]** simple and you can then if you're unsure why something is calculated in a

**[41:47]** why something is calculated in a

**[41:48]** why something is calculated in a specific way, you can add this explained

**[41:49]** specific way, you can add this explained

**[41:49]** specific way, you can add this explained true. Uh and then it will tell you all

**[41:52]** true. Uh and then it will tell you all

**[41:52]** true. Uh and then it will tell you all the the details of like okay we have

**[41:54]** the the details of like okay we have

**[41:54]** the the details of like okay we have father um and it then calculates

**[41:57]** father um and it then calculates

**[41:57]** father um and it then calculates basically all the different pieces of

**[41:58]** basically all the different pieces of

**[41:58]** basically all the different pieces of the formula for you and shows you how it


### [42:00 - 43:00]

**[42:00]** the formula for you and shows you how it

**[42:00]** the formula for you and shows you how it did the calculation. So you can debug

**[42:02]** did the calculation. So you can debug

**[42:02]** did the calculation. So you can debug that if you need to um but it's probably

**[42:05]** that if you need to um but it's probably

**[42:05]** that if you need to um but it's probably a bit too much output for the everyday

**[42:07]** a bit too much output for the everyday

**[42:07]** a bit too much output for the everyday use case. Um

**[42:10]** use case. Um

**[42:10]** use case. Um and then you can customize the score if

**[42:13]** and then you can customize the score if

**[42:13]** and then you can customize the score if you want to. Here I'm doing a a random

**[42:15]** you want to. Here I'm doing a a random

**[42:15]** you want to. Here I'm doing a a random score. So my two fathers this is a bit

**[42:18]** score. So my two fathers this is a bit

**[42:18]** score. So my two fathers this is a bit hard to show. um they will just be in

**[42:20]** hard to show. um they will just be in

**[42:20]** hard to show. um they will just be in random order because their score is here

**[42:22]** random order because their score is here

**[42:22]** random order because their score is here um randomly assigned. Um but you could

**[42:25]** um randomly assigned. Um but you could

**[42:25]** um randomly assigned. Um but you could do this more intelligently that you

**[42:27]** do this more intelligently that you

**[42:27]** do this more intelligently that you combine like the score and like if you

**[42:30]** combine like the score and like if you

**[42:30]** combine like the score and like if you have I don't know the margin that on a

**[42:32]** have I don't know the margin that on a

**[42:32]** have I don't know the margin that on a product that you sell or the rating that

**[42:34]** product that you sell or the rating that

**[42:34]** product that you sell or the rating that you include that in the rating somehow

**[42:35]** you include that in the rating somehow

**[42:35]** you include that in the rating somehow and you can build a custom score for

**[42:37]** and you can build a custom score for

**[42:37]** and you can build a custom score for things like that. Um so you can

**[42:39]** things like that. Um so you can

**[42:39]** things like that. Um so you can influence that any way you want. Um,

**[42:43]** influence that any way you want. Um,

**[42:43]** influence that any way you want. Um, one thing that I see every now and then

**[42:45]** one thing that I see every now and then

**[42:46]** one thing that I see every now and then that is a very bad idea and we'll skip

**[42:48]** that is a very bad idea and we'll skip

**[42:48]** that is a very bad idea and we'll skip this one because it's probably a bit too

**[42:50]** this one because it's probably a bit too

**[42:50]** this one because it's probably a bit too much. Um, this one, by the way, is the

**[42:53]** much. Um, this one, by the way, is the

**[42:53]** much. Um, this one, by the way, is the is the total formula that you can do or

**[42:55]** is the total formula that you can do or

**[42:55]** is the total formula that you can do or maybe I'll show you this parts that I

**[42:57]** maybe I'll show you this parts that I

**[42:57]** maybe I'll show you this parts that I skipped. What happens if you search for

**[42:58]** skipped. What happens if you search for

**[42:58]** skipped. What happens if you search for two terms and they're not the same? They


### [43:00 - 44:00]

**[43:01]** two terms and they're not the same? They

**[43:01]** two terms and they're not the same? They don't have the same relevancy. So, what

**[43:03]** don't have the same relevancy. So, what

**[43:03]** don't have the same relevancy. So, what the calculation behind the scenes

**[43:05]** the calculation behind the scenes

**[43:05]** the calculation behind the scenes basically looks like is let's say we

**[43:07]** basically looks like is let's say we

**[43:07]** basically looks like is let's say we search for um father. Father is very

**[43:10]** search for um father. Father is very

**[43:10]** search for um father. Father is very rare. That's why it's much more relevant

**[43:12]** rare. That's why it's much more relevant

**[43:12]** rare. That's why it's much more relevant than your your is pretty common. And

**[43:14]** than your your is pretty common. And

**[43:14]** than your your is pretty common. And then we have a document that contains

**[43:16]** then we have a document that contains

**[43:16]** then we have a document that contains your father. It's kind of like this

**[43:18]** your father. It's kind of like this

**[43:18]** your father. It's kind of like this exis. This is like the this will be the

**[43:20]** exis. This is like the this will be the

**[43:20]** exis. This is like the this will be the best match. But will a word will a

**[43:22]** best match. But will a word will a

**[43:22]** best match. But will a word will a document that only contains father be

**[43:24]** document that only contains father be

**[43:24]** document that only contains father be more relevant or only your intuitively

**[43:28]** more relevant or only your intuitively

**[43:28]** more relevant or only your intuitively the one with just father will be more

**[43:30]** the one with just father will be more

**[43:30]** the one with just father will be more relevant. But how does it calculate

**[43:32]** relevant. But how does it calculate

**[43:32]** relevant. But how does it calculate that? Um it basically calculates like

**[43:35]** that? Um it basically calculates like

**[43:35]** that? Um it basically calculates like this is the relevancy of father. um this

**[43:37]** this is the relevancy of father. um this

**[43:37]** this is the relevancy of father. um this is the ideal document and this is your

**[43:39]** is the ideal document and this is your

**[43:39]** is the ideal document and this is your and then it can looks like which one has

**[43:41]** and then it can looks like which one has

**[43:41]** and then it can looks like which one has the shorter angle and this is the one

**[43:43]** the shorter angle and this is the one

**[43:43]** the shorter angle and this is the one that is more relevant. Um so if you have

**[43:45]** that is more relevant. Um so if you have

**[43:45]** that is more relevant. Um so if you have a multi-term search um you can figure

**[43:49]** a multi-term search um you can figure

**[43:49]** a multi-term search um you can figure out which term is more relevant and how

**[43:50]** out which term is more relevant and how

**[43:50]** out which term is more relevant and how they are combined. Um and then you can

**[43:52]** they are combined. Um and then you can

**[43:52]** they are combined. Um and then you can also have the coordination factor which

**[43:54]** also have the coordination factor which

**[43:54]** also have the coordination factor which basically rewards documents containing

**[43:57]** basically rewards documents containing

**[43:57]** basically rewards documents containing more of the terms that you're searching

**[43:58]** more of the terms that you're searching

**[43:58]** more of the terms that you're searching for. So if you I'm searching for three


### [44:00 - 45:00]

**[44:00]** for. So if you I'm searching for three

**[44:00]** for. So if you I'm searching for three time terms like um you

**[44:04]** time terms like um you

**[44:04]** time terms like um you I am father whatever um if a document

**[44:08]** I am father whatever um if a document

**[44:08]** I am father whatever um if a document contains all three this will be the the

**[44:10]** contains all three this will be the the

**[44:10]** contains all three this will be the the formula that combines the scores of all

**[44:12]** formula that combines the scores of all

**[44:12]** formula that combines the scores of all three and multiplies it by three divided

**[44:14]** three and multiplies it by three divided

**[44:14]** three and multiplies it by three divided by three. If it only contains two of

**[44:16]** by three. If it only contains two of

**[44:16]** by three. If it only contains two of them it would only have the relevancy of

**[44:18]** them it would only have the relevancy of

**[44:18]** them it would only have the relevancy of 2/3 and with one one/3 and then you put

**[44:22]** 2/3 and with one one/3 and then you put

**[44:22]** 2/3 and with one one/3 and then you put it all together and this is the formula

**[44:23]** it all together and this is the formula

**[44:23]** it all together and this is the formula that happens behind the scenes and you

**[44:25]** that happens behind the scenes and you

**[44:25]** that happens behind the scenes and you don't have to do that in your head

**[44:26]** don't have to do that in your head

**[44:26]** don't have to do that in your head luckily.

**[44:28]** luckily.

**[44:28]** luckily. Cool. We have seen these um one thing

**[44:32]** Cool. We have seen these um one thing

**[44:32]** Cool. We have seen these um one thing that I or we see every now and then is

**[44:34]** that I or we see every now and then is

**[44:34]** that I or we see every now and then is that people try to translate the score

**[44:36]** that people try to translate the score

**[44:36]** that people try to translate the score into percentages.

**[44:38]** into percentages.

**[44:38]** into percentages. Um

**[44:40]** Um

**[44:40]** Um like you say this is a 100% score and

**[44:43]** like you say this is a 100% score and

**[44:43]** like you say this is a 100% score and this is only like a 50% match. Who wants

**[44:46]** this is only like a 50% match. Who wants

**[44:46]** this is only like a 50% match. Who wants to do that?

**[44:49]** to do that?

**[44:49]** to do that? Hopefully nobody. Uh because the lucine

**[44:51]** Hopefully nobody. Uh because the lucine

**[44:52]** Hopefully nobody. Uh because the lucine documentation is pretty explicit about

**[44:53]** documentation is pretty explicit about

**[44:53]** documentation is pretty explicit about that. um

**[44:56]** that. um

**[44:56]** that. um should not think about the problem in

**[44:57]** should not think about the problem in

**[44:57]** should not think about the problem in that way because it doesn't work. Um and


### [45:00 - 46:00]

**[45:00]** that way because it doesn't work. Um and

**[45:00]** that way because it doesn't work. Um and I'll show you why it doesn't work or how

**[45:02]** I'll show you why it doesn't work or how

**[45:02]** I'll show you why it doesn't work or how this breaks. Um let's take another

**[45:05]** this breaks. Um let's take another

**[45:05]** this breaks. Um let's take another example. Uh

**[45:14]** let's say we take this short text. These

**[45:14]** let's say we take this short text. These are my father's machines. I I think of a

**[45:17]** are my father's machines. I I think of a

**[45:17]** are my father's machines. I I think of a good Star Wars quote to use here, but

**[45:19]** good Star Wars quote to use here, but

**[45:19]** good Star Wars quote to use here, but bear with me. Um so what remains if I

**[45:21]** bear with me. Um so what remains if I

**[45:21]** bear with me. Um so what remains if I run this through my analyzer? my father

**[45:23]** run this through my analyzer? my father

**[45:23]** run this through my analyzer? my father machine. These are the three tokens that

**[45:26]** machine. These are the three tokens that

**[45:26]** machine. These are the three tokens that remain. Now I will store that you

**[45:29]** remain. Now I will store that you

**[45:29]** remain. Now I will store that you remember with the three tokens that we

**[45:30]** remember with the three tokens that we

**[45:30]** remember with the three tokens that we have stored. Um and if I search for my

**[45:33]** have stored. Um and if I search for my

**[45:33]** have stored. Um and if I search for my father machine um you might be inclined

**[45:37]** father machine um you might be inclined

**[45:37]** father machine um you might be inclined uh to say um this is um the perfect

**[45:42]** uh to say um this is um the perfect

**[45:42]** uh to say um this is um the perfect score.

**[45:44]** score.

**[45:44]** score. This is like a 100%.

**[45:46]** This is like a 100%.

**[45:46]** This is like a 100%. Agreed?

**[45:48]** Agreed?

**[45:48]** Agreed? because all the three tokens that I have

**[45:50]** because all the three tokens that I have

**[45:50]** because all the three tokens that I have stored in these are my father's machines

**[45:52]** stored in these are my father's machines

**[45:52]** stored in these are my father's machines um are there. So this must be like my

**[45:54]** um are there. So this must be like my

**[45:54]** um are there. So this must be like my perfect match. So it's 3.2 that would be

**[45:56]** perfect match. So it's 3.2 that would be

**[45:56]** perfect match. So it's 3.2 that would be 100%. The problem now is every time you


### [46:00 - 47:00]

**[46:00]** 100%. The problem now is every time you

**[46:00]** 100%. The problem now is every time you add or remove a document the statistics

**[46:02]** add or remove a document the statistics

**[46:02]** add or remove a document the statistics will change and your score will change.

**[46:04]** will change and your score will change.

**[46:04]** will change and your score will change. So if I delete that document um and I

**[46:06]** So if I delete that document um and I

**[46:06]** So if I delete that document um and I search the same thing again um I don't

**[46:09]** search the same thing again um I don't

**[46:09]** search the same thing again um I don't know what percentage this is now. Is

**[46:11]** know what percentage this is now. Is

**[46:11]** know what percentage this is now. Is this now the new 100% the best document

**[46:13]** this now the new 100% the best document

**[46:13]** this now the new 100% the best document or is this a 0 point or I don't know

**[46:15]** or is this a 0 point or I don't know

**[46:16]** or is this a 0 point or I don't know 20%. um how does this compare? Um and

**[46:20]** 20%. um how does this compare? Um and

**[46:20]** 20%. um how does this compare? Um and then you can play play funny tricks

**[46:23]** then you can play play funny tricks

**[46:23]** then you can play play funny tricks where these droids are my father's

**[46:24]** where these droids are my father's

**[46:24]** where these droids are my father's father's machines. Um and you can see I

**[46:27]** father's machines. Um and you can see I

**[46:27]** father's machines. Um and you can see I have a turn frequency of two for father

**[46:30]** have a turn frequency of two for father

**[46:30]** have a turn frequency of two for father here. So if I store that one then and

**[46:33]** here. So if I store that one then and

**[46:33]** here. So if I store that one then and then search it. Um

**[46:38]** then search it. Um

**[46:38]** then search it. Um is this now 100%? Is this now 110%. Um

**[46:41]** is this now 100%? Is this now 110%. Um

**[46:41]** is this now 100%? Is this now 110%. Um so don't try to translate uh scores into

**[46:44]** so don't try to translate uh scores into

**[46:44]** so don't try to translate uh scores into percentages.

**[46:46]** percentages.

**[46:46]** percentages. They're only relevant within one query.

**[46:48]** They're only relevant within one query.

**[46:48]** They're only relevant within one query. They're also not comparable across

**[46:49]** They're also not comparable across

**[46:49]** They're also not comparable across queries. They're really just sorting

**[46:51]** queries. They're really just sorting

**[46:51]** queries. They're really just sorting within one query. Um, to do that, um,

**[46:54]** within one query. Um, to do that, um,

**[46:54]** within one query. Um, to do that, um, okay, let me get rid of this one again.

**[46:57]** okay, let me get rid of this one again.

**[46:57]** okay, let me get rid of this one again. Now,

**[46:59]** Now,

**[46:59]** Now, we've seen the limitations uh of keyword


### [47:00 - 48:00]

**[47:01]** we've seen the limitations uh of keyword

**[47:02]** we've seen the limitations uh of keyword search. We don't want to define um our

**[47:05]** search. We don't want to define um our

**[47:05]** search. We don't want to define um our our synonyms. We might want to extract a

**[47:07]** our synonyms. We might want to extract a

**[47:07]** our synonyms. We might want to extract a bit more meaning. So, we'll we'll do

**[47:09]** bit more meaning. So, we'll we'll do

**[47:09]** bit more meaning. So, we'll we'll do some simple examples uh to extend. Um I

**[47:14]** some simple examples uh to extend. Um I

**[47:14]** some simple examples uh to extend. Um I will add uh from OpenAI text embedding

**[47:18]** will add uh from OpenAI text embedding

**[47:18]** will add uh from OpenAI text embedding small

**[47:20]** small

**[47:20]** small I'm basically connecting that inference

**[47:23]** I'm basically connecting that inference

**[47:23]** I'm basically connecting that inference API for text embeddings here in my

**[47:25]** API for text embeddings here in my

**[47:25]** API for text embeddings here in my instance um I have removed the API key

**[47:28]** instance um I have removed the API key

**[47:28]** instance um I have removed the API key you will need to use your own API key um

**[47:30]** you will need to use your own API key um

**[47:30]** you will need to use your own API key um if you want to use that but it is

**[47:31]** if you want to use that but it is

**[47:31]** if you want to use that but it is already configured um so let me pull up

**[47:35]** already configured um so let me pull up

**[47:35]** already configured um so let me pull up the inference services that we have here

**[47:37]** the inference services that we have here

**[47:37]** the inference services that we have here I have done or I have added two uh

**[47:42]** I have done or I have added two uh

**[47:42]** I have done or I have added two uh different models. Uh, one sparse, one

**[47:46]** different models. Uh, one sparse, one

**[47:46]** different models. Uh, one sparse, one dense. Let's go to these. Uh, by the

**[47:48]** dense. Let's go to these. Uh, by the

**[47:48]** dense. Let's go to these. Uh, by the way, if you try to do this, um, with

**[47:51]** way, if you try to do this, um, with

**[47:51]** way, if you try to do this, um, with 100% score, don't do this. Um,

**[47:55]** 100% score, don't do this. Um,

**[47:55]** 100% score, don't do this. Um, because it will just not work. Um, okay.


### [48:00 - 49:00]

**[48:00]** because it will just not work. Um, okay.

**[48:00]** because it will just not work. Um, okay. Not everybody has worked with dense

**[48:01]** Not everybody has worked with dense

**[48:01]** Not everybody has worked with dense vectors, right? Uh, so I have a couple

**[48:03]** vectors, right? Uh, so I have a couple

**[48:04]** vectors, right? Uh, so I have a couple of graphics coming back to our Star Wars

**[48:06]** of graphics coming back to our Star Wars

**[48:06]** of graphics coming back to our Star Wars theme, uh, just to look at how that

**[48:07]** theme, uh, just to look at how that

**[48:07]** theme, uh, just to look at how that works. So what you do with dense vectors

**[48:10]** works. So what you do with dense vectors

**[48:10]** works. So what you do with dense vectors is um we'll keep this very simple um

**[48:14]** is um we'll keep this very simple um

**[48:14]** is um we'll keep this very simple um this one just has a single uh dimension

**[48:17]** this one just has a single uh dimension

**[48:17]** this one just has a single uh dimension um and it has like the axis is pretty

**[48:19]** um and it has like the axis is pretty

**[48:19]** um and it has like the axis is pretty much like realistic Star Wars characters

**[48:21]** much like realistic Star Wars characters

**[48:21]** much like realistic Star Wars characters and cartoonish Star Wars characters and

**[48:24]** and cartoonish Star Wars characters and

**[48:24]** and cartoonish Star Wars characters and this one falls on the realistic side and

**[48:26]** this one falls on the realistic side and

**[48:26]** this one falls on the realistic side and that other one is just cartoonish and

**[48:29]** that other one is just cartoonish and

**[48:29]** that other one is just cartoonish and you have model behind the scenes that

**[48:31]** you have model behind the scenes that

**[48:31]** you have model behind the scenes that can rate those images and will figure

**[48:32]** can rate those images and will figure

**[48:32]** can rate those images and will figure out like where they fall. Um now in

**[48:36]** out like where they fall. Um now in

**[48:36]** out like where they fall. Um now in reality you will have more dimensions

**[48:38]** reality you will have more dimensions

**[48:38]** reality you will have more dimensions than one. Um and you will also have

**[48:40]** than one. Um and you will also have

**[48:40]** than one. Um and you will also have floating point precision. So it's not

**[48:42]** floating point precision. So it's not

**[48:42]** floating point precision. So it's not just like um minus one zero or one um

**[48:46]** just like um minus one zero or one um

**[48:46]** just like um minus one zero or one um but

**[48:49]** but

**[48:49]** but you will have more dimensions. So for

**[48:51]** you will have more dimensions. So for

**[48:51]** you will have more dimensions. So for example here I'm adding human and

**[48:53]** example here I'm adding human and

**[48:53]** example here I'm adding human and machine and in a realistic model you

**[48:55]** machine and in a realistic model you

**[48:55]** machine and in a realistic model you don't have like the dimensions are not

**[48:56]** don't have like the dimensions are not

**[48:56]** don't have like the dimensions are not labeled as nicely and clearly

**[48:58]** labeled as nicely and clearly

**[48:58]** labeled as nicely and clearly understandable. the machine has learned


### [49:00 - 50:00]

**[49:00]** understandable. the machine has learned

**[49:00]** understandable. the machine has learned what they represent but they're not

**[49:02]** what they represent but they're not

**[49:02]** what they represent but they're not representing an actual thing that you

**[49:03]** representing an actual thing that you

**[49:03]** representing an actual thing that you can extract like that. Um but in our

**[49:06]** can extract like that. Um but in our

**[49:06]** can extract like that. Um but in our simple example here now we can say this

**[49:08]** simple example here now we can say this

**[49:08]** simple example here now we can say this layer character um is

**[49:11]** layer character um is

**[49:11]** layer character um is realistic and a human versus um I don't

**[49:16]** realistic and a human versus um I don't

**[49:16]** realistic and a human versus um I don't know the dove waiter um is cartoonish

**[49:19]** know the dove waiter um is cartoonish

**[49:19]** know the dove waiter um is cartoonish and I don't know somewhere between human

**[49:21]** and I don't know somewhere between human

**[49:21]** and I don't know somewhere between human and machine um so this is the

**[49:23]** and machine um so this is the

**[49:24]** and machine um so this is the representation in the vector space and

**[49:25]** representation in the vector space and

**[49:26]** representation in the vector space and then you could have like I said you

**[49:27]** then you could have like I said you

**[49:27]** then you could have like I said you could have floatingoint values and then

**[49:28]** could have floatingoint values and then

**[49:28]** could have floatingoint values and then you can have different characters um and

**[49:31]** you can have different characters um and

**[49:32]** you can have different characters um and similar characters like both of those

**[49:33]** similar characters like both of those

**[49:33]** similar characters like both of those are human um without the hand, he's only

**[49:36]** are human um without the hand, he's only

**[49:36]** are human um without the hand, he's only like not quite as human anymore. So he's

**[49:38]** like not quite as human anymore. So he's

**[49:38]** like not quite as human anymore. So he's a bit lower down here. Um

**[49:41]** a bit lower down here. Um

**[49:41]** a bit lower down here. Um uh so he's a bit closer to the machines.

**[49:44]** uh so he's a bit closer to the machines.

**[49:44]** uh so he's a bit closer to the machines. Um so you can have all of your entities

**[49:47]** Um so you can have all of your entities

**[49:47]** Um so you can have all of your entities in this vector space and then if you

**[49:49]** in this vector space and then if you

**[49:49]** in this vector space and then if you search for something you could figure

**[49:51]** search for something you could figure

**[49:51]** search for something you could figure out like which characters are the

**[49:53]** out like which characters are the

**[49:53]** out like which characters are the closest uh to this one. And again in

**[49:55]** closest uh to this one. And again in

**[49:55]** closest uh to this one. And again in reality you will have hundreds of

**[49:58]** reality you will have hundreds of

**[49:58]** reality you will have hundreds of dimensions. uh it will be much harder to


### [50:00 - 51:00]

**[50:00]** dimensions. uh it will be much harder to

**[50:00]** dimensions. uh it will be much harder to say like uh these are the explicit

**[50:02]** say like uh these are the explicit

**[50:02]** say like uh these are the explicit things and this is why it works like

**[50:03]** things and this is why it works like

**[50:03]** things and this is why it works like that. Um it will depend on how good your

**[50:06]** that. Um it will depend on how good your

**[50:06]** that. Um it will depend on how good your model is uh in interpreting your data

**[50:09]** model is uh in interpreting your data

**[50:09]** model is uh in interpreting your data and extracting the right meaning from

**[50:10]** and extracting the right meaning from

**[50:10]** and extracting the right meaning from it. Um but that is the general idea of

**[50:15]** it. Um but that is the general idea of

**[50:15]** it. Um but that is the general idea of dense vector representation. You have

**[50:17]** dense vector representation. You have

**[50:17]** dense vector representation. You have your documents or sometimes it's like

**[50:19]** your documents or sometimes it's like

**[50:19]** your documents or sometimes it's like chunks of documents um that are

**[50:21]** chunks of documents um that are

**[50:21]** chunks of documents um that are represented in this vector space and

**[50:24]** represented in this vector space and

**[50:24]** represented in this vector space and then you try to find something that is

**[50:25]** then you try to find something that is

**[50:25]** then you try to find something that is close to it. uh for that. Um

**[50:29]** close to it. uh for that. Um

**[50:29]** close to it. uh for that. Um does that make sense for everybody or

**[50:31]** does that make sense for everybody or

**[50:31]** does that make sense for everybody or any specific questions?

**[50:37]** So it's a bit more opaque. I want to say

**[50:37]** So it's a bit more opaque. I want to say it's not quite as easy because you say

**[50:39]** it's not quite as easy because you say

**[50:39]** it's not quite as easy because you say like these five characters match these

**[50:41]** like these five characters match these

**[50:41]** like these five characters match these other five characters here. Um but you

**[50:44]** other five characters here. Um but you

**[50:44]** other five characters here. Um but you need to trust or evaluate that you have

**[50:46]** need to trust or evaluate that you have

**[50:46]** need to trust or evaluate that you have the right model to figure out how these

**[50:48]** the right model to figure out how these

**[50:48]** the right model to figure out how these things connect.

**[50:50]** things connect.

**[50:50]** things connect. So let's um see how that looks like.

**[50:54]** So let's um see how that looks like.

**[50:54]** So let's um see how that looks like. Um I have

**[50:58]** Um I have

**[50:58]** Um I have one dense vector model down here. We


### [51:00 - 52:00]

**[51:01]** one dense vector model down here. We

**[51:01]** one dense vector model down here. We have openAI embedding. Um this one is a

**[51:04]** have openAI embedding. Um this one is a

**[51:04]** have openAI embedding. Um this one is a very small model. It only has 128

**[51:07]** very small model. It only has 128

**[51:07]** very small model. It only has 128 dimensions. Um

**[51:09]** dimensions. Um

**[51:09]** dimensions. Um the results will not be great but it's

**[51:11]** the results will not be great but it's

**[51:11]** the results will not be great but it's actually for demonstrating uh it

**[51:14]** actually for demonstrating uh it

**[51:14]** actually for demonstrating uh it actually helpful. Uh so we'll see that

**[51:16]** actually helpful. Uh so we'll see that

**[51:16]** actually helpful. Uh so we'll see that the other model that we have and let me

**[51:19]** the other model that we have and let me

**[51:19]** the other model that we have and let me show you the output of that. So if I

**[51:21]** show you the output of that. So if I

**[51:21]** show you the output of that. So if I take my text, these are not the droids

**[51:22]** take my text, these are not the droids

**[51:22]** take my text, these are not the droids you're looking for. This is the

**[51:25]** you're looking for. This is the

**[51:25]** you're looking for. This is the representation. It's basically an array

**[51:27]** representation. It's basically an array

**[51:27]** representation. It's basically an array of floatingoint values uh that will be

**[51:29]** of floatingoint values uh that will be

**[51:30]** of floatingoint values uh that will be stored. And then you just look for

**[51:31]** stored. And then you just look for

**[51:31]** stored. And then you just look for similar floatingoint values. And then

**[51:33]** similar floatingoint values. And then

**[51:33]** similar floatingoint values. And then you have these are not the droids you're

**[51:35]** you have these are not the droids you're

**[51:35]** you have these are not the droids you're looking for here on the previous one.

**[51:43]** Dense text embedding. Um this one here

**[51:43]** Dense text embedding. Um this one here does sparse embedding. Sparse is the the

**[51:46]** does sparse embedding. Sparse is the the

**[51:46]** does sparse embedding. Sparse is the the main model used for that is called

**[51:48]** main model used for that is called

**[51:48]** main model used for that is called splade. Um our input of splade is we

**[51:52]** splade. Um our input of splade is we

**[51:52]** splade. Um our input of splade is we call it uh it's kind of like a slightly

**[51:55]** call it uh it's kind of like a slightly

**[51:55]** call it uh it's kind of like a slightly improved uh split but the concept is

**[51:57]** improved uh split but the concept is

**[51:57]** improved uh split but the concept is still the same. What you get is um you


### [52:00 - 53:00]

**[52:00]** still the same. What you get is um you

**[52:00]** still the same. What you get is um you take your

**[52:02]** take your

**[52:02]** take your you take your words and this is not just

**[52:04]** you take your words and this is not just

**[52:04]** you take your words and this is not just a TF. This is a learned representation

**[52:08]** a TF. This is a learned representation

**[52:08]** a TF. This is a learned representation where I take all of my tokens and then

**[52:11]** where I take all of my tokens and then

**[52:11]** where I take all of my tokens and then expand them and say like for this text

**[52:14]** expand them and say like for this text

**[52:14]** expand them and say like for this text um these are all the tokens that I think

**[52:16]** um these are all the tokens that I think

**[52:16]** um these are all the tokens that I think are relevant and this number here

**[52:18]** are relevant and this number here

**[52:18]** are relevant and this number here basically tells me how relevant they

**[52:20]** basically tells me how relevant they

**[52:20]** basically tells me how relevant they are. Um again not all of these make

**[52:24]** are. Um again not all of these make

**[52:24]** are. Um again not all of these make sense intuitively. Um and you might get

**[52:28]** sense intuitively. Um and you might get

**[52:28]** sense intuitively. Um and you might get some funky results for example with

**[52:30]** some funky results for example with

**[52:30]** some funky results for example with foreign languages. This currently only

**[52:31]** foreign languages. This currently only

**[52:31]** foreign languages. This currently only supports English. Um but these are all

**[52:35]** supports English. Um but these are all

**[52:35]** supports English. Um but these are all the terms that uh we have extracted

**[52:37]** the terms that uh we have extracted

**[52:38]** the terms that uh we have extracted normally. Um yeah you get like 100

**[52:41]** normally. Um yeah you get like 100

**[52:41]** normally. Um yeah you get like 100 something or so. Um so the the idea is

**[52:45]** something or so. Um so the the idea is

**[52:45]** something or so. Um so the the idea is that this text is represented by all of

**[52:47]** that this text is represented by all of

**[52:47]** that this text is represented by all of these tokens and the higher the score

**[52:49]** these tokens and the higher the score

**[52:49]** these tokens and the higher the score here the more uh important it is. And

**[52:52]** here the more uh important it is. And

**[52:52]** here the more uh important it is. And what you will do is you store that

**[52:53]** what you will do is you store that

**[52:53]** what you will do is you store that behind the scenes. when you search for

**[52:56]** behind the scenes. when you search for

**[52:56]** behind the scenes. when you search for something um you will generate a similar

**[52:58]** something um you will generate a similar

**[52:58]** something um you will generate a similar list and then you look for the ones that


### [53:00 - 54:00]

**[53:00]** list and then you look for the ones that

**[53:00]** list and then you look for the ones that have an overlap and you basically

**[53:02]** have an overlap and you basically

**[53:02]** have an overlap and you basically multiply the scores together and the

**[53:04]** multiply the scores together and the

**[53:04]** multiply the scores together and the ones with the highest values will then

**[53:06]** ones with the highest values will then

**[53:06]** ones with the highest values will then find the most relevant document.

**[53:09]** find the most relevant document.

**[53:09]** find the most relevant document. This is in so far interesting or nice

**[53:12]** This is in so far interesting or nice

**[53:12]** This is in so far interesting or nice because it's a bit easier to interpret.

**[53:14]** because it's a bit easier to interpret.

**[53:14]** because it's a bit easier to interpret. It's not just like long array of

**[53:16]** It's not just like long array of

**[53:16]** It's not just like long array of floatingoint values. Um sometimes these

**[53:20]** floatingoint values. Um sometimes these

**[53:20]** floatingoint values. Um sometimes these don't make sense. The main downside of

**[53:22]** don't make sense. The main downside of

**[53:22]** don't make sense. The main downside of this though is that it gets pretty

**[53:25]** this though is that it gets pretty

**[53:25]** this though is that it gets pretty expensive at query time because you

**[53:27]** expensive at query time because you

**[53:27]** expensive at query time because you store like a ton of different tokens

**[53:28]** store like a ton of different tokens

**[53:28]** store like a ton of different tokens here for this u when you retrieve it um

**[53:31]** here for this u when you retrieve it um

**[53:31]** here for this u when you retrieve it um the search query will generate a similar

**[53:34]** the search query will generate a similar

**[53:34]** the search query will generate a similar long list of terms and at if you have a

**[53:38]** long list of terms and at if you have a

**[53:38]** long list of terms and at if you have a large enough text body um a query might

**[53:41]** large enough text body um a query might

**[53:41]** large enough text body um a query might hit a very large percentage of your

**[53:43]** hit a very large percentage of your

**[53:43]** hit a very large percentage of your entire stored documents to with these

**[53:45]** entire stored documents to with these

**[53:45]** entire stored documents to with these ore matches because basically these are

**[53:48]** ore matches because basically these are

**[53:48]** ore matches because basically these are just a lot of ores that you combine

**[53:50]** just a lot of ores that you combine

**[53:50]** just a lot of ores that you combine calculate uh the score and then return

**[53:52]** calculate uh the score and then return

**[53:52]** calculate uh the score and then return the most or the the highest ranking

**[53:54]** the most or the the highest ranking

**[53:54]** the most or the the highest ranking results. Um so it's an interesting

**[53:57]** results. Um so it's an interesting

**[53:57]** results. Um so it's an interesting approach. It didn't gain as much

**[53:59]** approach. It didn't gain as much

**[53:59]** approach. It didn't gain as much traction as dense vector models, but it


### [54:00 - 55:00]

**[54:01]** traction as dense vector models, but it

**[54:01]** traction as dense vector models, but it can be as a first step or an easy and

**[54:03]** can be as a first step or an easy and

**[54:03]** can be as a first step or an easy and interpretable step. It can be a good

**[54:05]** interpretable step. It can be a good

**[54:06]** interpretable step. It can be a good starting point u to dive into the

**[54:07]** starting point u to dive into the

**[54:07]** starting point u to dive into the details here. Um

**[54:18]** uh so this these are not the droids

**[54:18]** uh so this these are not the droids looking for is basically represented by

**[54:21]** looking for is basically represented by

**[54:21]** looking for is basically represented by this embedding here.

**[54:24]** this embedding here.

**[54:24]** this embedding here. So it's like this entire list of of

**[54:27]** So it's like this entire list of of

**[54:27]** So it's like this entire list of of terms with these um yeah with this

**[54:30]** terms with these um yeah with this

**[54:30]** terms with these um yeah with this relevancy basically this is the

**[54:32]** relevancy basically this is the

**[54:32]** relevancy basically this is the representation of this string and then

**[54:35]** representation of this string and then

**[54:35]** representation of this string and then when I search for something I will

**[54:37]** when I search for something I will

**[54:37]** when I search for something I will generate a similar list and then I

**[54:39]** generate a similar list and then I

**[54:39]** generate a similar list and then I basically try to match the two together

**[54:41]** basically try to match the two together

**[54:41]** basically try to match the two together like for what is has the most or the

**[54:43]** like for what is has the most or the

**[54:43]** like for what is has the most or the highest matches here.

**[54:57]** Yes, we'll do that in a second. Um it

**[54:57]** Yes, we'll do that in a second. Um it it's a bit because um with the


### [55:00 - 56:00]

**[55:02]** it's a bit because um with the

**[55:02]** it's a bit because um with the um

**[55:04]** um

**[55:04]** um back it doesn't tell you exactly this is

**[55:06]** back it doesn't tell you exactly this is

**[55:06]** back it doesn't tell you exactly this is what matched. Uh but yes um so I will

**[55:09]** what matched. Uh but yes um so I will

**[55:09]** what matched. Uh but yes um so I will need to create a new index. Um this one

**[55:12]** need to create a new index. Um this one

**[55:12]** need to create a new index. Um this one keeps the configuration from before but

**[55:14]** keeps the configuration from before but

**[55:14]** keeps the configuration from before but I'm adding this semantic text for the

**[55:17]** I'm adding this semantic text for the

**[55:17]** I'm adding this semantic text for the the sparse model and the dense model.

**[55:21]** the sparse model and the dense model.

**[55:21]** the sparse model and the dense model. So I've created this one. U and now I'll

**[55:23]** So I've created this one. U and now I'll

**[55:23]** So I've created this one. U and now I'll just put three documents. I have my

**[55:26]** just put three documents. I have my

**[55:26]** just put three documents. I have my other index. Um as you can see here it

**[55:28]** other index. Um as you can see here it

**[55:28]** other index. Um as you can see here it says three documents were moved over. Um

**[55:31]** says three documents were moved over. Um

**[55:31]** says three documents were moved over. Um so we can then start searching here. And

**[55:33]** so we can then start searching here. And

**[55:34]** so we can then start searching here. And um if I look at that the first document

**[55:36]** um if I look at that the first document

**[55:36]** um if I look at that the first document is still these are not the droids you're

**[55:37]** is still these are not the droids you're

**[55:37]** is still these are not the droids you're looking for. You don't see like for the

**[55:40]** looking for. You don't see like for the

**[55:40]** looking for. You don't see like for the for keyword search you don't see the

**[55:42]** for keyword search you don't see the

**[55:42]** for keyword search you don't see the extracted tokens here. We also don't

**[55:44]** extracted tokens here. We also don't

**[55:44]** extracted tokens here. We also don't show you the the dense vector

**[55:46]** show you the the dense vector

**[55:46]** show you the the dense vector representation or the sparse vector

**[55:47]** representation or the sparse vector

**[55:47]** representation or the sparse vector representation. Those are just stored

**[55:49]** representation. Those are just stored

**[55:49]** representation. Those are just stored behind the scenes. um for querying, but

**[55:52]** behind the scenes. um for querying, but

**[55:52]** behind the scenes. um for querying, but there's no real point in retrieving them

**[55:54]** there's no real point in retrieving them

**[55:54]** there's no real point in retrieving them because you you're not going to do

**[55:55]** because you you're not going to do

**[55:55]** because you you're not going to do anything with that huge array of of

**[55:57]** anything with that huge array of of

**[55:57]** anything with that huge array of of dense vectors. Um it will just slow down

**[55:59]** dense vectors. Um it will just slow down

**[55:59]** dense vectors. Um it will just slow down your searches. Um you can look at the


### [56:00 - 57:00]

**[56:03]** your searches. Um you can look at the

**[56:03]** your searches. Um you can look at the the mapping and you can see um I'm

**[56:05]** the mapping and you can see um I'm

**[56:05]** the mapping and you can see um I'm basically copying my existing quote

**[56:08]** basically copying my existing quote

**[56:08]** basically copying my existing quote field to these other two that I can also

**[56:10]** field to these other two that I can also

**[56:10]** field to these other two that I can also search those. Okay. So if I look for

**[56:14]** search those. Okay. So if I look for

**[56:14]** search those. Okay. So if I look for machine on my original quote, will it

**[56:17]** machine on my original quote, will it

**[56:17]** machine on my original quote, will it find anything?

**[56:27]** no, because it only had these are not

**[56:27]** no, because it only had these are not the droids you're looking for. And this

**[56:28]** the droids you're looking for. And this

**[56:28]** the droids you're looking for. And this is still the keyword search.

**[56:33]** So, this is just a query from before

**[56:33]** So, this is just a query from before just to show you that yes, we're not

**[56:35]** just to show you that yes, we're not

**[56:35]** just to show you that yes, we're not matching anything because it only had

**[56:36]** matching anything because it only had

**[56:36]** matching anything because it only had these are not the droids you're looking

**[56:38]** these are not the droids you're looking

**[56:38]** these are not the droids you're looking for. But here, we're looking for

**[56:39]** for. But here, we're looking for

**[56:39]** for. But here, we're looking for machine. Um, it was still the keyword

**[56:41]** machine. Um, it was still the keyword

**[56:41]** machine. Um, it was still the keyword matching. Doesn't work, shouldn't work.

**[56:44]** matching. Doesn't work, shouldn't work.

**[56:44]** matching. Doesn't work, shouldn't work. That's exactly the result that we want

**[56:45]** That's exactly the result that we want

**[56:45]** That's exactly the result that we want out of this here. Um, now if I say else

**[56:49]** out of this here. Um, now if I say else

**[56:49]** out of this here. Um, now if I say else and I say machine,

**[56:52]** and I say machine,

**[56:52]** and I say machine, then it will match here. These are not

**[56:54]** then it will match here. These are not

**[56:54]** then it will match here. These are not the droids you're looking for. And you

**[56:55]** the droids you're looking for. And you

**[56:55]** the droids you're looking for. And you can see this one matches pretty well. I

**[56:57]** can see this one matches pretty well. I

**[56:58]** can see this one matches pretty well. I don't know at 0.9, but it also has some


### [57:00 - 58:00]

**[57:01]** don't know at 0.9, but it also has some

**[57:01]** don't know at 0.9, but it also has some overlap with no, I am your father. I

**[57:04]** overlap with no, I am your father. I

**[57:04]** overlap with no, I am your father. I mean, it is much lower in terms of

**[57:05]** mean, it is much lower in terms of

**[57:05]** mean, it is much lower in terms of relevance. Uh, but something had an

**[57:08]** relevance. Uh, but something had an

**[57:08]** relevance. Uh, but something had an overlap here. And only the the third

**[57:10]** overlap here. And only the the third

**[57:10]** overlap here. And only the the third document, um, Obi-Wan never told you

**[57:13]** document, um, Obi-Wan never told you

**[57:13]** document, um, Obi-Wan never told you what happened to your father. only that

**[57:15]** what happened to your father. only that

**[57:15]** what happened to your father. only that one is not in our results list at all.

**[57:17]** one is not in our results list at all.

**[57:17]** one is not in our results list at all. But there was something here. I don't

**[57:19]** But there was something here. I don't

**[57:19]** But there was something here. I don't know the expansion. We would need to

**[57:21]** know the expansion. We would need to

**[57:21]** know the expansion. We would need to basically run

**[57:25]** basically run

**[57:25]** basically run where was it? We would need to run uh

**[57:27]** where was it? We would need to run uh

**[57:27]** where was it? We would need to run uh this one here for all the strings and

**[57:30]** this one here for all the strings and

**[57:30]** this one here for all the strings and look then for the expansion of the query

**[57:32]** look then for the expansion of the query

**[57:32]** look then for the expansion of the query and then there would be some overlap and

**[57:33]** and then there would be some overlap and

**[57:34]** and then there would be some overlap and that's how we retrieve that one. Um

**[57:38]** that's how we retrieve that one. Um

**[57:38]** that's how we retrieve that one. Um threshold. You could define a threshold.

**[57:41]** threshold. You could define a threshold.

**[57:41]** threshold. You could define a threshold. Um, it will though depend. Um,

**[57:45]** Um, it will though depend. Um,

**[57:45]** Um, it will though depend. Um, let's see. Uh, these are not the droids

**[57:48]** let's see. Uh, these are not the droids

**[57:48]** let's see. Uh, these are not the droids you're looking for. Let's say if I

**[57:56]** say I'm not sure this will change

**[57:56]** say I'm not sure this will change anything.


### [58:00 - 59:00]

**[58:04]** I mean, the relevance here is still it's

**[58:04]** I mean, the relevance here is still it's still 10x or so. Um, but yeah, this one

**[58:08]** still 10x or so. Um, but yeah, this one

**[58:08]** still 10x or so. Um, but yeah, this one still

**[58:18]** terms you look for um the score just

**[58:18]** terms you look for um the score just totally jumps around. So it's a bit hard

**[58:20]** totally jumps around. So it's a bit hard

**[58:20]** totally jumps around. So it's a bit hard to define that threshold

**[58:23]** to define that threshold

**[58:23]** to define that threshold because here you can see in my previous

**[58:25]** because here you can see in my previous

**[58:25]** because here you can see in my previous query we might have said 0.2 is the

**[58:27]** query we might have said 0.2 is the

**[58:27]** query we might have said 0.2 is the cutoff point but now it's actually 0.4

**[58:30]** cutoff point but now it's actually 0.4

**[58:30]** cutoff point but now it's actually 0.4 even though it's not super relevant. So

**[58:32]** even though it's not super relevant. So

**[58:32]** even though it's not super relevant. So it might be a bit tricky uh or you might

**[58:34]** it might be a bit tricky uh or you might

**[58:34]** it might be a bit tricky uh or you might need to have a more dynamic threshold

**[58:36]** need to have a more dynamic threshold

**[58:36]** need to have a more dynamic threshold depending on how many terms you're

**[58:37]** depending on how many terms you're

**[58:37]** depending on how many terms you're looking for and uh what is a relevant

**[58:40]** looking for and uh what is a relevant

**[58:40]** looking for and uh what is a relevant result in the in a bigger picture. The

**[58:42]** result in the in a bigger picture. The

**[58:42]** result in the in a bigger picture. The assumption would be if you have hundreds

**[58:45]** assumption would be if you have hundreds

**[58:45]** assumption would be if you have hundreds of thousands or even millions of

**[58:47]** of thousands or even millions of

**[58:47]** of thousands or even millions of documents um you will probably not have

**[58:49]** documents um you will probably not have

**[58:49]** documents um you will probably not have that problem that anything that is so

**[58:52]** that problem that anything that is so

**[58:52]** that problem that anything that is so remotely connected will actually be in

**[58:54]** remotely connected will actually be in

**[58:54]** remotely connected will actually be in the top 10 or 20 or whatever list that

**[58:56]** the top 10 or 20 or whatever list that

**[58:56]** the top 10 or 20 or whatever list that you want to retrieve. Um so for large or

**[58:59]** you want to retrieve. Um so for large or


### [59:00 - 01:00:00]

**[59:00]** you want to retrieve. Um so for large or proper data sets this should be less of

**[59:01]** proper data sets this should be less of

**[59:01]** proper data sets this should be less of an issue. With my hello world example of

**[59:03]** an issue. With my hello world example of

**[59:03]** an issue. With my hello world example of three documents um it can be a bit

**[59:06]** three documents um it can be a bit

**[59:06]** three documents um it can be a bit misleading but yes you can have a cut

**[59:08]** misleading but yes you can have a cut

**[59:08]** misleading but yes you can have a cut off point if you figure out what for

**[59:10]** off point if you figure out what for

**[59:10]** off point if you figure out what for your data set and your queries is a good

**[59:12]** your data set and your queries is a good

**[59:12]** your data set and your queries is a good cutff point. You could define a cutff

**[59:14]** cutff point. You could define a cutff

**[59:14]** cutff point. You could define a cutff point. Sorry you have three documents

**[59:16]** point. Sorry you have three documents

**[59:16]** point. Sorry you have three documents only show.

**[59:19]** only show.

**[59:19]** only show. So

**[59:21]** So

**[59:21]** So the query gets expanded into I don't

**[59:22]** the query gets expanded into I don't

**[59:22]** the query gets expanded into I don't know those 100 tokens or whatever and

**[59:24]** know those 100 tokens or whatever and

**[59:24]** know those 100 tokens or whatever and then for those two there is some overlap

**[59:26]** then for those two there is some overlap

**[59:26]** then for those two there is some overlap but the third one just didn't have any

**[59:28]** but the third one just didn't have any

**[59:28]** but the third one just didn't have any overlap

**[59:30]** overlap

**[59:30]** overlap but I so we what okay we can we can do

**[59:32]** but I so we what okay we can we can do

**[59:32]** but I so we what okay we can we can do that it's just a bit tricky to figure

**[59:35]** that it's just a bit tricky to figure

**[59:35]** that it's just a bit tricky to figure out that the terms that has the overlook

**[59:37]** out that the terms that has the overlook

**[59:37]** out that the terms that has the overlook uh uh the overlap so we will need to

**[59:39]** uh uh the overlap so we will need to

**[59:39]** uh uh the overlap so we will need to take this one machine uh no I am your

**[59:42]** take this one machine uh no I am your

**[59:42]** take this one machine uh no I am your father let's take this one

**[59:46]** father let's take this one

**[59:46]** father let's take this one what you need to do is um to figure that

**[59:48]** what you need to do is um to figure that

**[59:48]** what you need to do is um to figure that one about I know actually we

**[59:51]** one about I know actually we

**[59:51]** one about I know actually we should be able Let me see.

**[59:54]** should be able Let me see.

**[59:54]** should be able Let me see. Um


### [01:00:00 - 01:01:00]

**[01:00:16]** It's a pretty long output

**[01:00:16]** It's a pretty long output somewhere. I was actually hoping that it

**[01:00:18]** somewhere. I was actually hoping that it

**[01:00:18]** somewhere. I was actually hoping that it will show me the term that has matched

**[01:00:20]** will show me the term that has matched

**[01:00:20]** will show me the term that has matched here. Okay, I see something.

**[01:00:27]** Okay, there's something puppet that

**[01:00:27]** Okay, there's something puppet that seems to be the overlap.

**[01:00:30]** seems to be the overlap.

**[01:00:30]** seems to be the overlap. How much sense that term expansion for

**[01:00:32]** How much sense that term expansion for

**[01:00:32]** How much sense that term expansion for the the store text and the query text

**[01:00:34]** the the store text and the query text

**[01:00:34]** the the store text and the query text makes is a bit of a different

**[01:00:36]** makes is a bit of a different

**[01:00:36]** makes is a bit of a different discussion. Uh but in here with that

**[01:00:38]** discussion. Uh but in here with that

**[01:00:38]** discussion. Uh but in here with that explained true, you can actually see how

**[01:00:40]** explained true, you can actually see how

**[01:00:40]** explained true, you can actually see how it matched and what happened behind the

**[01:00:42]** it matched and what happened behind the

**[01:00:42]** it matched and what happened behind the scenes. if you have any really hard or

**[01:00:44]** scenes. if you have any really hard or

**[01:00:44]** scenes. if you have any really hard or weird curious or something that is hard

**[01:00:46]** weird curious or something that is hard

**[01:00:46]** weird curious or something that is hard to explain to debug that. But the third

**[01:00:48]** to explain to debug that. But the third

**[01:00:48]** to explain to debug that. But the third one didn't match. Um now if I take the

**[01:00:52]** one didn't match. Um now if I take the

**[01:00:52]** one didn't match. Um now if I take the dense vector model with OpenAI and I

**[01:00:54]** dense vector model with OpenAI and I

**[01:00:54]** dense vector model with OpenAI and I search for machine, how many results do

**[01:00:56]** search for machine, how many results do

**[01:00:56]** search for machine, how many results do you expect to get back from this one?


### [01:01:00 - 01:02:00]

**[01:01:06]** 0 one two three.

**[01:01:06]** 0 one two three. Yes. Three. Y three.

**[01:01:10]** Yes. Three. Y three.

**[01:01:10]** Yes. Three. Y three. Yes. because there's always some match

**[01:01:12]** Yes. because there's always some match

**[01:01:12]** Yes. because there's always some match that is the other or let me run the

**[01:01:14]** that is the other or let me run the

**[01:01:14]** that is the other or let me run the query first.

**[01:01:17]** query first.

**[01:01:17]** query first. Um here these are not the droids you're

**[01:01:20]** Um here these are not the droids you're

**[01:01:20]** Um here these are not the droids you're looking for. This one is the first one.

**[01:01:22]** looking for. This one is the first one.

**[01:01:22]** looking for. This one is the first one. Um I don't think that this model is

**[01:01:24]** Um I don't think that this model is

**[01:01:24]** Um I don't think that this model is generally great because here the results

**[01:01:26]** generally great because here the results

**[01:01:26]** generally great because here the results are super close. It is I mean the the

**[01:01:28]** are super close. It is I mean the the

**[01:01:28]** are super close. It is I mean the the droids with the machines that is the

**[01:01:30]** droids with the machines that is the

**[01:01:30]** droids with the machines that is the first one but the score is super close

**[01:01:33]** first one but the score is super close

**[01:01:33]** first one but the score is super close to the second one which is no I am your

**[01:01:34]** to the second one which is no I am your

**[01:01:34]** to the second one which is no I am your father which feels pretty unrelated and

**[01:01:37]** father which feels pretty unrelated and

**[01:01:37]** father which feels pretty unrelated and uh Obi-Wan never told you what happened

**[01:01:38]** uh Obi-Wan never told you what happened

**[01:01:38]** uh Obi-Wan never told you what happened to your father. Even that one is still

**[01:01:41]** to your father. Even that one is still

**[01:01:41]** to your father. Even that one is still with a reasonably close score. Uh but

**[01:01:44]** with a reasonably close score. Uh but

**[01:01:44]** with a reasonably close score. Uh but why do we have those? Um

**[01:01:47]** why do we have those? Um

**[01:01:47]** why do we have those? Um because if we say what is the relevance

**[01:01:50]** because if we say what is the relevance

**[01:01:50]** because if we say what is the relevance uh I mean it's further away but it's

**[01:01:54]** uh I mean it's further away but it's

**[01:01:54]** uh I mean it's further away but it's always like there's always kind of like

**[01:01:56]** always like there's always kind of like

**[01:01:56]** always like there's always kind of like some angle to it even if the kind of

**[01:01:57]** some angle to it even if the kind of

**[01:01:58]** some angle to it even if the kind of like the angle here or depending on the

**[01:01:59]** like the angle here or depending on the

**[01:01:59]** like the angle here or depending on the the similarity calculation that you do


### [01:02:00 - 01:03:00]

**[01:02:02]** the similarity calculation that you do

**[01:02:02]** the similarity calculation that you do but it's still always related. There is

**[01:02:04]** but it's still always related. There is

**[01:02:04]** but it's still always related. There is no easy way to say something is totally

**[01:02:06]** no easy way to say something is totally

**[01:02:06]** no easy way to say something is totally unrelated. Um, that is by the way one

**[01:02:11]** unrelated. Um, that is by the way one

**[01:02:11]** unrelated. Um, that is by the way one good thing about keyword search where it

**[01:02:13]** good thing about keyword search where it

**[01:02:13]** good thing about keyword search where it was relatively easy to have a cut off

**[01:02:14]** was relatively easy to have a cut off

**[01:02:14]** was relatively easy to have a cut off point of things that are totally not

**[01:02:16]** point of things that are totally not

**[01:02:16]** point of things that are totally not relevant where you're not going to

**[01:02:17]** relevant where you're not going to

**[01:02:17]** relevant where you're not going to confuse your users versus here if you

**[01:02:20]** confuse your users versus here if you

**[01:02:20]** confuse your users versus here if you don't have great matches you might get

**[01:02:22]** don't have great matches you might get

**[01:02:22]** don't have great matches you might get almost it's not random but it's

**[01:02:25]** almost it's not random but it's

**[01:02:25]** almost it's not random but it's potentially it looks very unrelated to

**[01:02:27]** potentially it looks very unrelated to

**[01:02:27]** potentially it looks very unrelated to your end users what you might return

**[01:02:29]** your end users what you might return

**[01:02:29]** your end users what you might return just because it's very hard to show.

**[01:02:31]** just because it's very hard to show.

**[01:02:31]** just because it's very hard to show. Yes. Is it fair to say that the

**[01:02:35]** Yes. Is it fair to say that the

**[01:02:35]** Yes. Is it fair to say that the search for

**[01:02:44]** I I'm careful with worse because it's

**[01:02:44]** I I'm careful with worse because it's really a hello world example. So I don't

**[01:02:46]** really a hello world example. So I don't

**[01:02:46]** really a hello world example. So I don't take this as a quality measurement in

**[01:02:48]** take this as a quality measurement in

**[01:02:48]** take this as a quality measurement in any way. Um I I I'm yeah I mean the the

**[01:02:51]** any way. Um I I I'm yeah I mean the the

**[01:02:52]** any way. Um I I I'm yeah I mean the the OpenAI model with 128 dimensions is very

**[01:02:54]** OpenAI model with 128 dimensions is very

**[01:02:54]** OpenAI model with 128 dimensions is very few dimensions. I think it will probably

**[01:02:56]** few dimensions. I think it will probably

**[01:02:56]** few dimensions. I think it will probably be cheap but not give you great results

**[01:02:58]** be cheap but not give you great results

**[01:02:58]** be cheap but not give you great results necessarily. But don't use this as a


### [01:03:00 - 01:04:00]

**[01:03:00]** necessarily. But don't use this as a

**[01:03:00]** necessarily. But don't use this as a benchmark. I think it's just a a good

**[01:03:03]** benchmark. I think it's just a a good

**[01:03:03]** benchmark. I think it's just a a good way to see um that you this is now much

**[01:03:06]** way to see um that you this is now much

**[01:03:06]** way to see um that you this is now much harder because now you need to pick the

**[01:03:08]** harder because now you need to pick the

**[01:03:08]** harder because now you need to pick the right machine learning model uh to

**[01:03:10]** right machine learning model uh to

**[01:03:10]** right machine learning model uh to actually figure out what is a good match

**[01:03:12]** actually figure out what is a good match

**[01:03:12]** actually figure out what is a good match with keyword based search it was a bit

**[01:03:14]** with keyword based search it was a bit

**[01:03:14]** with keyword based search it was a bit of a different story there you need to

**[01:03:15]** of a different story there you need to

**[01:03:15]** of a different story there you need to pay more attention to like how do I

**[01:03:17]** pay more attention to like how do I

**[01:03:17]** pay more attention to like how do I tokenize and do I have the right

**[01:03:19]** tokenize and do I have the right

**[01:03:19]** tokenize and do I have the right language and do I do stemming or not

**[01:03:21]** language and do I do stemming or not

**[01:03:21]** language and do I do stemming or not stemming but most of that work is

**[01:03:23]** stemming but most of that work is

**[01:03:23]** stemming but most of that work is relatively I want to say almost

**[01:03:25]** relatively I want to say almost

**[01:03:25]** relatively I want to say almost algorithmic um and then you can figure

**[01:03:28]** algorithmic um and then you can figure

**[01:03:28]** algorithmic um and then you can figure that out and you configure it and then

**[01:03:29]** that out and you configure it and then

**[01:03:29]** that out and you configure it and then it's very predictable able at query

**[01:03:31]** it's very predictable able at query

**[01:03:31]** it's very predictable able at query time. Um versus with the dense vector

**[01:03:34]** time. Um versus with the dense vector

**[01:03:34]** time. Um versus with the dense vector representation,

**[01:03:35]** representation,

**[01:03:35]** representation, you really need to evaluate for the

**[01:03:37]** you really need to evaluate for the

**[01:03:37]** you really need to evaluate for the queries that you run and the data that

**[01:03:39]** queries that you run and the data that

**[01:03:39]** queries that you run and the data that you have like is that relevant and is an

**[01:03:41]** you have like is that relevant and is an

**[01:03:41]** you have like is that relevant and is an improvement or not. Um it's very easy to

**[01:03:44]** improvement or not. Um it's very easy to

**[01:03:44]** improvement or not. Um it's very easy to get going and just throw a dense vector

**[01:03:46]** get going and just throw a dense vector

**[01:03:46]** get going and just throw a dense vector model together. Um and you will match

**[01:03:48]** model together. Um and you will match

**[01:03:48]** model together. Um and you will match you will always match something that

**[01:03:51]** you will always match something that

**[01:03:51]** you will always match something that might be an advantage over the the

**[01:03:53]** might be an advantage over the the

**[01:03:53]** might be an advantage over the the lexical search where you don't have any

**[01:03:54]** lexical search where you don't have any

**[01:03:54]** lexical search where you don't have any matches which sometimes is there the

**[01:03:56]** matches which sometimes is there the

**[01:03:56]** matches which sometimes is there the problem that nothing comes back and you

**[01:03:57]** problem that nothing comes back and you

**[01:03:57]** problem that nothing comes back and you would want to have at least some

**[01:03:59]** would want to have at least some

**[01:03:59]** would want to have at least some results. Um here it might just be


### [01:04:00 - 01:05:00]

**[01:04:02]** results. Um here it might just be

**[01:04:02]** results. Um here it might just be unrelated.

**[01:04:03]** unrelated.

**[01:04:04]** unrelated. So that that can be tricky. Um the you

**[01:04:08]** So that that can be tricky. Um the you

**[01:04:08]** So that that can be tricky. Um the you want to have some results is by the way

**[01:04:10]** want to have some results is by the way

**[01:04:10]** want to have some results is by the way um a funny story that European

**[01:04:12]** um a funny story that European

**[01:04:12]** um a funny story that European e-commerce store once told me. They said

**[01:04:14]** e-commerce store once told me. They said

**[01:04:14]** e-commerce store once told me. They said they accidentally deleted I think

**[01:04:17]** they accidentally deleted I think

**[01:04:17]** they accidentally deleted I think twothirds of their data that they had

**[01:04:19]** twothirds of their data that they had

**[01:04:19]** twothirds of their data that they had for the products that you could buy. And

**[01:04:21]** for the products that you could buy. And

**[01:04:21]** for the products that you could buy. And then I asked them like okay so how much

**[01:04:23]** then I asked them like okay so how much

**[01:04:23]** then I asked them like okay so how much revenue did you lose because of that?

**[01:04:25]** revenue did you lose because of that?

**[01:04:26]** revenue did you lose because of that? And they said basically nothing because

**[01:04:28]** And they said basically nothing because

**[01:04:28]** And they said basically nothing because as long as you showed some somewhat

**[01:04:31]** as long as you showed some somewhat

**[01:04:31]** as long as you showed some somewhat relevant results quickly enough people

**[01:04:33]** relevant results quickly enough people

**[01:04:33]** relevant results quickly enough people would still buy that. So only if you

**[01:04:35]** would still buy that. So only if you

**[01:04:35]** would still buy that. So only if you have no results that's probably the

**[01:04:37]** have no results that's probably the

**[01:04:37]** have no results that's probably the worst. So, for an e-commerce store, you

**[01:04:39]** worst. So, for an e-commerce store, you

**[01:04:39]** worst. So, for an e-commerce store, you might want to show stuff a bit further

**[01:04:41]** might want to show stuff a bit further

**[01:04:41]** might want to show stuff a bit further out because people might still buy it.

**[01:04:43]** out because people might still buy it.

**[01:04:43]** out because people might still buy it. Uh, but it really depends on the I'm I'm

**[01:04:45]** Uh, but it really depends on the I'm I'm

**[01:04:45]** Uh, but it really depends on the I'm I'm coming to you in a moment. Uh, it really

**[01:04:47]** coming to you in a moment. Uh, it really

**[01:04:47]** coming to you in a moment. Uh, it really depends on your use case. E-commerce is

**[01:04:49]** depends on your use case. E-commerce is

**[01:04:49]** depends on your use case. E-commerce is kind of like one extreme where you want

**[01:04:51]** kind of like one extreme where you want

**[01:04:51]** kind of like one extreme where you want to show always something for people to

**[01:04:53]** to show always something for people to

**[01:04:53]** to show always something for people to buy. Um, if you have a database of legal

**[01:04:57]** buy. Um, if you have a database of legal

**[01:04:57]** buy. Um, if you have a database of legal cases or something like that, you

**[01:04:58]** cases or something like that, you

**[01:04:58]** cases or something like that, you probably don't want that approach. Uh,


### [01:05:00 - 01:06:00]

**[01:05:00]** probably don't want that approach. Uh,

**[01:05:00]** probably don't want that approach. Uh, because that will go horribly wrong. So,

**[01:05:01]** because that will go horribly wrong. So,

**[01:05:01]** because that will go horribly wrong. So, it is very domain specific. Um

**[01:05:05]** it is very domain specific. Um

**[01:05:05]** it is very domain specific. Um that's I think also the good thing about

**[01:05:07]** that's I think also the good thing about

**[01:05:07]** that's I think also the good thing about search because it keeps a lot of people

**[01:05:09]** search because it keeps a lot of people

**[01:05:09]** search because it keeps a lot of people employed because it's not an easy

**[01:05:10]** employed because it's not an easy

**[01:05:10]** employed because it's not an easy problem. It's it's almost job security

**[01:05:13]** problem. It's it's almost job security

**[01:05:13]** problem. It's it's almost job security because it depends much on the this is

**[01:05:15]** because it depends much on the this is

**[01:05:16]** because it depends much on the this is the data that you have and this is the

**[01:05:17]** the data that you have and this is the

**[01:05:17]** the data that you have and this is the query that people run and this is the

**[01:05:18]** query that people run and this is the

**[01:05:18]** query that people run and this is the expectation of what will happen and this

**[01:05:20]** expectation of what will happen and this

**[01:05:20]** expectation of what will happen and this is for this domain the right behavior.

**[01:05:23]** is for this domain the right behavior.

**[01:05:23]** is for this domain the right behavior. Um so there's no easy right or wrong

**[01:05:25]** Um so there's no easy right or wrong

**[01:05:26]** Um so there's no easy right or wrong with the checkbox. And the other thing

**[01:05:28]** with the checkbox. And the other thing

**[01:05:28]** with the checkbox. And the other thing is you might make if you tune it you

**[01:05:30]** is you might make if you tune it you

**[01:05:30]** is you might make if you tune it you might make it better for one case but

**[01:05:31]** might make it better for one case but

**[01:05:31]** might make it better for one case but worse for 20 others. That's why a robust

**[01:05:34]** worse for 20 others. That's why a robust

**[01:05:34]** worse for 20 others. That's why a robust abbreviation set is normally very

**[01:05:36]** abbreviation set is normally very

**[01:05:36]** abbreviation set is normally very important though very rare. Uh a lot of

**[01:05:39]** important though very rare. Uh a lot of

**[01:05:39]** important though very rare. Uh a lot of people yolo it. Um and you will see that

**[01:05:42]** people yolo it. Um and you will see that

**[01:05:42]** people yolo it. Um and you will see that in the results and for the e-commerce

**[01:05:43]** in the results and for the e-commerce

**[01:05:43]** in the results and for the e-commerce store it probably works well enough. Uh,

**[01:05:45]** store it probably works well enough. Uh,

**[01:05:45]** store it probably works well enough. Uh, sorry, you had a question.

**[01:05:55]** I have a very large

**[01:05:55]** I have a very large customer.


### [01:06:00 - 01:07:00]

**[01:06:09]** Yeah. So the the way we would do it in

**[01:06:10]** Yeah. So the the way we would do it in our product um is that you would

**[01:06:12]** our product um is that you would

**[01:06:12]** our product um is that you would probably have two different indices with

**[01:06:14]** probably have two different indices with

**[01:06:14]** probably have two different indices with different mappings. Yeah. But then it's

**[01:06:17]** different mappings. Yeah. But then it's

**[01:06:17]** different mappings. Yeah. But then it's not so upgrades.

**[01:06:36]** So there's no penalty for having a field

**[01:06:36]** So there's no penalty for having a field that's not

**[01:06:49]** No, that the problem is the data

**[01:06:49]** No, that the problem is the data structure like if the field is there. So

**[01:06:51]** structure like if the field is there. So

**[01:06:51]** structure like if the field is there. So the data structure that we build in the

**[01:06:52]** the data structure that we build in the

**[01:06:52]** the data structure that we build in the background is called H. And either we

**[01:06:55]** background is called H. And either we

**[01:06:55]** background is called H. And either we build the data structure or we don't

**[01:06:57]** build the data structure or we don't

**[01:06:57]** build the data structure or we don't build it.

**[01:06:59]** build it.

**[01:06:59]** build it. Yeah. So if you had 10 billion entries


### [01:07:00 - 01:08:00]

**[01:07:03]** Yeah. So if you had 10 billion entries

**[01:07:03]** Yeah. So if you had 10 billion entries in your vector

**[01:07:47]** You have to manage that

**[01:07:48]** You have to manage that complex technology.


### [01:09:00 - 01:10:00]

**[01:09:07]** So the the reason

**[01:09:07]** So the the reason the the reason why that is uh it's like

**[01:09:10]** the the reason why that is uh it's like

**[01:09:10]** the the reason why that is uh it's like merging so because you have the

**[01:09:12]** merging so because you have the

**[01:09:12]** merging so because you have the immutable segment structure in elastic

**[01:09:14]** immutable segment structure in elastic

**[01:09:14]** immutable segment structure in elastic search uh in HNSW you cannot easily

**[01:09:17]** search uh in HNSW you cannot easily

**[01:09:17]** search uh in HNSW you cannot easily merge you basically need to rebuild

**[01:09:19]** merge you basically need to rebuild

**[01:09:19]** merge you basically need to rebuild them. the one trick I forgot which

**[01:09:21]** them. the one trick I forgot which

**[01:09:21]** them. the one trick I forgot which version it was uh I'm not sure Dave if

**[01:09:23]** version it was uh I'm not sure Dave if

**[01:09:23]** version it was uh I'm not sure Dave if you remember I think it was even before

**[01:09:24]** you remember I think it was even before

**[01:09:24]** you remember I think it was even before 811 but basically if we do a merge we

**[01:09:27]** 811 but basically if we do a merge we

**[01:09:27]** 811 but basically if we do a merge we would take the the largest segment with

**[01:09:29]** would take the the largest segment with

**[01:09:29]** would take the the largest segment with not deleted documents and basically plop

**[01:09:31]** not deleted documents and basically plop

**[01:09:31]** not deleted documents and basically plop the new documents on top of them rather

**[01:09:33]** the new documents on top of them rather

**[01:09:33]** the new documents on top of them rather than starting from scratch from two HNSW

**[01:09:36]** than starting from scratch from two HNSW

**[01:09:36]** than starting from scratch from two HNSW data structures there's another

**[01:09:38]** data structures there's another

**[01:09:38]** data structures there's another optimization somewhere now in 9.0 zero

**[01:09:41]** optimization somewhere now in 9.0 zero

**[01:09:41]** optimization somewhere now in 9.0 zero that will make that a lot faster. So it

**[01:09:43]** that will make that a lot faster. So it

**[01:09:43]** that will make that a lot faster. So it really depends on the the version that

**[01:09:44]** really depends on the the version that

**[01:09:44]** really depends on the the version that you have and there are a couple of

**[01:09:46]** you have and there are a couple of

**[01:09:46]** you have and there are a couple of tricks that you can play. Uh but yeah

**[01:09:48]** tricks that you can play. Uh but yeah

**[01:09:48]** tricks that you can play. Uh but yeah that is one of the downsides of like the

**[01:09:51]** that is one of the downsides of like the

**[01:09:51]** that is one of the downsides of like the way immutable segments work and HNSW is

**[01:09:54]** way immutable segments work and HNSW is

**[01:09:54]** way immutable segments work and HNSW is built that you can't easily just merge

**[01:09:56]** built that you can't easily just merge

**[01:09:56]** built that you can't easily just merge it as easily together as other data

**[01:09:58]** it as easily together as other data

**[01:09:58]** it as easily together as other data structures. Uh because you really need

**[01:09:59]** structures. Uh because you really need

**[01:09:59]** structures. Uh because you really need to rebuild the HNSW data structure or


### [01:10:00 - 01:11:00]

**[01:10:02]** to rebuild the HNSW data structure or

**[01:10:02]** to rebuild the HNSW data structure or like take the largest one and then plop

**[01:10:04]** like take the largest one and then plop

**[01:10:04]** like take the largest one and then plop the other one in.

**[01:10:53]** Yeah. I feel like rag has been very

**[01:10:53]** Yeah. I feel like rag has been very heavily abused is or like the mental

**[01:10:56]** heavily abused is or like the mental

**[01:10:56]** heavily abused is or like the mental model I think started off as like you do

**[01:10:57]** model I think started off as like you do

**[01:10:57]** model I think started off as like you do retrieval and then you do the generation

**[01:10:59]** retrieval and then you do the generation

**[01:10:59]** retrieval and then you do the generation but you could do the generation earlier


### [01:11:00 - 01:12:00]

**[01:11:01]** but you could do the generation earlier

**[01:11:01]** but you could do the generation earlier on as well that you do the query

**[01:11:02]** on as well that you do the query

**[01:11:02]** on as well that you do the query rewriting and expanded query. Um, so I

**[01:11:06]** rewriting and expanded query. Um, so I

**[01:11:06]** rewriting and expanded query. Um, so I my favorite example for that is um

**[01:11:09]** my favorite example for that is um

**[01:11:10]** my favorite example for that is um you're looking for a recipe. You don't

**[01:11:12]** you're looking for a recipe. You don't

**[01:11:12]** you're looking for a recipe. You don't need to have the the LLM regenerate the

**[01:11:15]** need to have the the LLM regenerate the

**[01:11:16]** need to have the the LLM regenerate the recipe. You just want to find the

**[01:11:17]** recipe. You just want to find the

**[01:11:17]** recipe. You just want to find the recipe. But maybe you have a scenario

**[01:11:19]** recipe. But maybe you have a scenario

**[01:11:19]** recipe. But maybe you have a scenario where you forgot what the thing is

**[01:11:20]** where you forgot what the thing is

**[01:11:20]** where you forgot what the thing is called that you want to cook. And then

**[01:11:22]** called that you want to cook. And then

**[01:11:22]** called that you want to cook. And then you could use the LLM, for example, to

**[01:11:24]** you could use the LLM, for example, to

**[01:11:24]** you could use the LLM, for example, to tell you what you're looking for. Um,

**[01:11:26]** tell you what you're looking for. Um,

**[01:11:26]** tell you what you're looking for. Um, like you say like, oh, I'm looking for

**[01:11:27]** like you say like, oh, I'm looking for

**[01:11:27]** like you say like, oh, I'm looking for this Italian dish uh that has like these

**[01:11:31]** this Italian dish uh that has like these

**[01:11:31]** this Italian dish uh that has like these layers of pasta and then some meat in

**[01:11:33]** layers of pasta and then some meat in

**[01:11:33]** layers of pasta and then some meat in between. And then the LLM says like,

**[01:11:34]** between. And then the LLM says like,

**[01:11:34]** between. And then the LLM says like, "Oh, you're looking for lasagna." And

**[01:11:36]** "Oh, you're looking for lasagna." And

**[01:11:36]** "Oh, you're looking for lasagna." And then you basically do the generation

**[01:11:37]** then you basically do the generation

**[01:11:37]** then you basically do the generation first or a query rewriting um and then

**[01:11:41]** first or a query rewriting um and then

**[01:11:41]** first or a query rewriting um and then search and then get the results. As a

**[01:11:43]** search and then get the results. As a

**[01:11:43]** search and then get the results. As a very let's you explicit example here.

**[01:11:46]** very let's you explicit example here.

**[01:11:46]** very let's you explicit example here. Your example will look very different

**[01:11:47]** Your example will look very different

**[01:11:47]** Your example will look very different than probably smarter than my example.

**[01:11:50]** than probably smarter than my example.

**[01:11:50]** than probably smarter than my example. Uh but query writing is one um thing.

**[01:11:55]** Uh but query writing is one um thing.

**[01:11:55]** Uh but query writing is one um thing. There's also that this concept of hy

**[01:11:57]** There's also that this concept of hy

**[01:11:57]** There's also that this concept of hy where you your documents and your

**[01:11:59]** where you your documents and your

**[01:11:59]** where you your documents and your queries often look very different and


### [01:12:00 - 01:13:00]

**[01:12:01]** queries often look very different and

**[01:12:01]** queries often look very different and that you use an LLM to generate

**[01:12:03]** that you use an LLM to generate

**[01:12:03]** that you use an LLM to generate something from the query that looks more

**[01:12:04]** something from the query that looks more

**[01:12:04]** something from the query that looks more close like the do the documents that you

**[01:12:07]** close like the do the documents that you

**[01:12:07]** close like the do the documents that you have and then you match the documents

**[01:12:09]** have and then you match the documents

**[01:12:09]** have and then you match the documents together because they're more similar in

**[01:12:10]** together because they're more similar in

**[01:12:10]** together because they're more similar in structure. Um so there are all kinds of

**[01:12:12]** structure. Um so there are all kinds of

**[01:12:12]** structure. Um so there are all kinds of interesting things that you can do. Um

**[01:12:15]** interesting things that you can do. Um

**[01:12:15]** interesting things that you can do. Um like I said earlier that it depends is

**[01:12:17]** like I said earlier that it depends is

**[01:12:17]** like I said earlier that it depends is becoming a bigger and bigger factor. Uh

**[01:12:19]** becoming a bigger and bigger factor. Uh

**[01:12:19]** becoming a bigger and bigger factor. Uh but yeah, your use case is probably

**[01:12:21]** but yeah, your use case is probably

**[01:12:22]** but yeah, your use case is probably might be

**[01:12:24]** might be

**[01:12:24]** might be yeah maybe a multi retrieval where you

**[01:12:27]** yeah maybe a multi retrieval where you

**[01:12:27]** yeah maybe a multi retrieval where you figure out like oh you look I don't know

**[01:12:29]** figure out like oh you look I don't know

**[01:12:29]** figure out like oh you look I don't know I know the example from an e-commerce

**[01:12:32]** I know the example from an e-commerce

**[01:12:32]** I know the example from an e-commerce store where it's like I'm going to a

**[01:12:34]** store where it's like I'm going to a

**[01:12:34]** store where it's like I'm going to a theme party from the 1920s and give me

**[01:12:37]** theme party from the 1920s and give me

**[01:12:37]** theme party from the 1920s and give me some suggestions and then the LLM will

**[01:12:39]** some suggestions and then the LLM will

**[01:12:39]** some suggestions and then the LLM will need to figure out like what am I

**[01:12:40]** need to figure out like what am I

**[01:12:40]** need to figure out like what am I searching for and then it can retrieve

**[01:12:41]** searching for and then it can retrieve

**[01:12:41]** searching for and then it can retrieve the right items and rewrite the query

**[01:12:43]** the right items and rewrite the query

**[01:12:43]** the right items and rewrite the query and then actually give you proper

**[01:12:45]** and then actually give you proper

**[01:12:45]** and then actually give you proper suggestions. Uh but it's it's not just

**[01:12:48]** suggestions. Uh but it's it's not just

**[01:12:48]** suggestions. Uh but it's it's not just running a query anymore.

**[01:12:50]** running a query anymore.

**[01:12:50]** running a query anymore. Uh yeah.


### [01:13:00 - 01:14:00]

**[01:13:49]** Uh, definitely not necessarily. It's

**[01:13:49]** Uh, definitely not necessarily. It's It's an interesting question. It's that

**[01:13:51]** It's an interesting question. It's that

**[01:13:51]** It's an interesting question. It's that feels almost like a blast from the past.

**[01:13:53]** feels almost like a blast from the past.

**[01:13:53]** feels almost like a blast from the past. I remember like two or three years ago

**[01:13:55]** I remember like two or three years ago

**[01:13:55]** I remember like two or three years ago there was this big debate of like how

**[01:13:57]** there was this big debate of like how

**[01:13:57]** there was this big debate of like how many dimensions does each data store

**[01:13:59]** many dimensions does each data store

**[01:13:59]** many dimensions does each data store support and like how many dimensions


### [01:14:00 - 01:15:00]

**[01:14:00]** support and like how many dimensions

**[01:14:00]** support and like how many dimensions should you have and at first it looked

**[01:14:02]** should you have and at first it looked

**[01:14:02]** should you have and at first it looked like oh more dimensions is always better

**[01:14:04]** like oh more dimensions is always better

**[01:14:04]** like oh more dimensions is always better but then it turned out more dimensions

**[01:14:05]** but then it turned out more dimensions

**[01:14:05]** but then it turned out more dimensions are very expensive. Um so it really

**[01:14:08]** are very expensive. Um so it really

**[01:14:08]** are very expensive. Um so it really depends on the model and what you're

**[01:14:09]** depends on the model and what you're

**[01:14:09]** depends on the model and what you're trying to solve. Like if you can get

**[01:14:11]** trying to solve. Like if you can get

**[01:14:11]** trying to solve. Like if you can get away with fewer dimensions it's

**[01:14:12]** away with fewer dimensions it's

**[01:14:12]** away with fewer dimensions it's potentially much cheaper and faster. Um

**[01:14:15]** potentially much cheaper and faster. Um

**[01:14:15]** potentially much cheaper and faster. Um but it I don't think there is a a hard

**[01:14:17]** but it I don't think there is a a hard

**[01:14:17]** but it I don't think there is a a hard rule like maybe the model with more

**[01:14:20]** rule like maybe the model with more

**[01:14:20]** rule like maybe the model with more dimensions can express more uh in

**[01:14:23]** dimensions can express more uh in

**[01:14:23]** dimensions can express more uh in because it just has more data and then

**[01:14:25]** because it just has more data and then

**[01:14:25]** because it just has more data and then it will come in handy. Uh but maybe it's

**[01:14:27]** it will come in handy. Uh but maybe it's

**[01:14:27]** it will come in handy. Uh but maybe it's not necessary for your specific use case

**[01:14:28]** not necessary for your specific use case

**[01:14:28]** not necessary for your specific use case and then you're just wasting a lot of

**[01:14:29]** and then you're just wasting a lot of

**[01:14:30]** and then you're just wasting a lot of resources. I don't think there is a an

**[01:14:32]** resources. I don't think there is a an

**[01:14:32]** resources. I don't think there is a an easy answer to say like yes for this use

**[01:14:34]** easy answer to say like yes for this use

**[01:14:34]** easy answer to say like yes for this use case you need at least 4,000 dimensions.

**[01:14:37]** case you need at least 4,000 dimensions.

**[01:14:38]** case you need at least 4,000 dimensions. Um

**[01:14:39]** Um

**[01:14:39]** Um it will depend but it depends on the

**[01:14:41]** it will depend but it depends on the

**[01:14:41]** it will depend but it depends on the model um how many dimensions it will

**[01:14:43]** model um how many dimensions it will

**[01:14:43]** model um how many dimensions it will output and then maybe you have some

**[01:14:44]** output and then maybe you have some

**[01:14:44]** output and then maybe you have some quantization in the background to reduce

**[01:14:46]** quantization in the background to reduce

**[01:14:46]** quantization in the background to reduce that again or reduce the either the

**[01:14:48]** that again or reduce the either the

**[01:14:48]** that again or reduce the either the number of dimensions or the fidelity per

**[01:14:50]** number of dimensions or the fidelity per

**[01:14:50]** number of dimensions or the fidelity per dimension. Um

**[01:14:52]** dimension. Um

**[01:14:52]** dimension. Um so there are a lot of different

**[01:14:53]** so there are a lot of different

**[01:14:54]** so there are a lot of different trade-offs in that performance

**[01:14:55]** trade-offs in that performance

**[01:14:55]** trade-offs in that performance consideration but it will mostly rely on

**[01:14:57]** consideration but it will mostly rely on

**[01:14:57]** consideration but it will mostly rely on like how good does the model work for


### [01:15:00 - 01:16:00]

**[01:15:00]** like how good does the model work for

**[01:15:00]** like how good does the model work for the use case that you're trying to do.

**[01:15:28]** Yeah. So the that is one area. So I want

**[01:15:28]** Yeah. So the that is one area. So I want to say historically what you would do is

**[01:15:30]** to say historically what you would do is

**[01:15:30]** to say historically what you would do is um you would have a golden data set um

**[01:15:33]** um you would have a golden data set um

**[01:15:33]** um you would have a golden data set um and then you would know what people are

**[01:15:34]** and then you would know what people are

**[01:15:34]** and then you would know what people are searching for and then you would have

**[01:15:36]** searching for and then you would have

**[01:15:36]** searching for and then you would have human experts who rate your queries and

**[01:15:38]** human experts who rate your queries and

**[01:15:38]** human experts who rate your queries and then you run different queries against

**[01:15:39]** then you run different queries against

**[01:15:40]** then you run different queries against it and then you see like is it getting

**[01:15:41]** it and then you see like is it getting

**[01:15:41]** it and then you see like is it getting better or is it getting worse. Um now

**[01:15:45]** better or is it getting worse. Um now

**[01:15:45]** better or is it getting worse. Um now LLMs open a new opportunity where you

**[01:15:47]** LLMs open a new opportunity where you

**[01:15:47]** LLMs open a new opportunity where you might have with human experts in the

**[01:15:48]** might have with human experts in the

**[01:15:48]** might have with human experts in the loop uh to help them out a bit but they

**[01:15:51]** loop uh to help them out a bit but they

**[01:15:51]** loop uh to help them out a bit but they might be actually good at evaluating the

**[01:15:53]** might be actually good at evaluating the

**[01:15:53]** might be actually good at evaluating the results. Um so you almost nobody has

**[01:15:56]** results. Um so you almost nobody has

**[01:15:56]** results. Um so you almost nobody has like the golden data set and test

**[01:15:58]** like the golden data set and test

**[01:15:58]** like the golden data set and test against that. Um but you can either use


### [01:16:00 - 01:17:00]

**[01:16:01]** against that. Um but you can either use

**[01:16:01]** against that. Um but you can either use it look at the behavior of your end

**[01:16:03]** it look at the behavior of your end

**[01:16:03]** it look at the behavior of your end users and try to infer something from

**[01:16:05]** users and try to infer something from

**[01:16:05]** users and try to infer something from that. Um or you have an LLM that

**[01:16:08]** that. Um or you have an LLM that

**[01:16:08]** that. Um or you have an LLM that evaluates like what you have or you have

**[01:16:10]** evaluates like what you have or you have

**[01:16:10]** evaluates like what you have or you have a human together with an LLM evaluate uh

**[01:16:13]** a human together with an LLM evaluate uh

**[01:16:13]** a human together with an LLM evaluate uh the results. Uh so you you have various

**[01:16:16]** the results. Uh so you you have various

**[01:16:16]** the results. Uh so you you have various tools. Uh but again it's

**[01:16:20]** tools. Uh but again it's

**[01:16:20]** tools. Uh but again it's and it depends and it really not an easy

**[01:16:22]** and it depends and it really not an easy

**[01:16:22]** and it depends and it really not an easy question of saying like this is the

**[01:16:24]** question of saying like this is the

**[01:16:24]** question of saying like this is the right thing. Maybe you can get away with

**[01:16:25]** right thing. Maybe you can get away with

**[01:16:26]** right thing. Maybe you can get away with something simple. So the the classic

**[01:16:27]** something simple. So the the classic

**[01:16:27]** something simple. So the the classic approach I want to say is like you

**[01:16:30]** approach I want to say is like you

**[01:16:30]** approach I want to say is like you looked at the click stream of how your

**[01:16:31]** looked at the click stream of how your

**[01:16:31]** looked at the click stream of how your users behaved and then you saw like they

**[01:16:33]** users behaved and then you saw like they

**[01:16:33]** users behaved and then you saw like they clicked on the first or up to the third

**[01:16:35]** clicked on the first or up to the third

**[01:16:35]** clicked on the first or up to the third result. The result was potentially good

**[01:16:37]** result. The result was potentially good

**[01:16:37]** result. The result was potentially good and they didn't just go back and then

**[01:16:39]** and they didn't just go back and then

**[01:16:39]** and they didn't just go back and then click on something else but they they

**[01:16:40]** click on something else but they they

**[01:16:40]** click on something else but they they stuck on the page. Um if they don't

**[01:16:42]** stuck on the page. Um if they don't

**[01:16:42]** stuck on the page. Um if they don't click on anything and just leave it

**[01:16:44]** click on anything and just leave it

**[01:16:44]** click on anything and just leave it might be very bad. if they go to the

**[01:16:46]** might be very bad. if they go to the

**[01:16:46]** might be very bad. if they go to the second or third page, it might also not

**[01:16:47]** second or third page, it might also not

**[01:16:48]** second or third page, it might also not be great. So there are some quality

**[01:16:49]** be great. So there are some quality

**[01:16:49]** be great. So there are some quality signals that you can infer from that or

**[01:16:51]** signals that you can infer from that or

**[01:16:51]** signals that you can infer from that or you really look into the the quality

**[01:16:53]** you really look into the the quality

**[01:16:53]** you really look into the the quality aspect and try to evaluate like what

**[01:16:55]** aspect and try to evaluate like what

**[01:16:55]** aspect and try to evaluate like what people were doing and how how it

**[01:16:57]** people were doing and how how it

**[01:16:57]** people were doing and how how it behaves. Uh but you can make this from

**[01:16:59]** behaves. Uh but you can make this from

**[01:16:59]** behaves. Uh but you can make this from relatively simple to pretty complicated.


### [01:17:00 - 01:18:00]

**[01:17:23]** Okay, obviously if I search for dad with

**[01:17:24]** Okay, obviously if I search for dad with extension, uh it will find my father

**[01:17:25]** extension, uh it will find my father

**[01:17:26]** extension, uh it will find my father example. Um and this one here um will

**[01:17:30]** example. Um and this one here um will

**[01:17:30]** example. Um and this one here um will still again match my my droids um pretty

**[01:17:33]** still again match my my droids um pretty

**[01:17:33]** still again match my my droids um pretty much like the the opening AI example.

**[01:17:36]** much like the the opening AI example.

**[01:17:36]** much like the the opening AI example. One thing that I I wanted to to show you

**[01:17:38]** One thing that I I wanted to to show you

**[01:17:38]** One thing that I I wanted to to show you what is also happening behind the scenes

**[01:17:40]** what is also happening behind the scenes

**[01:17:40]** what is also happening behind the scenes here. This is a very long segment like

**[01:17:42]** here. This is a very long segment like

**[01:17:42]** here. This is a very long segment like it's it's a lot of information with

**[01:17:45]** it's it's a lot of information with

**[01:17:45]** it's it's a lot of information with different speakers. Um what I have

**[01:17:48]** different speakers. Um what I have

**[01:17:48]** different speakers. Um what I have created here though is we have um

**[01:17:51]** created here though is we have um

**[01:17:51]** created here though is we have um created multiple chunks behind the

**[01:17:54]** created multiple chunks behind the

**[01:17:54]** created multiple chunks behind the scenes. And if I search for that um

**[01:17:58]** scenes. And if I search for that um

**[01:17:58]** scenes. And if I search for that um I think looking for murder in the


### [01:18:00 - 01:19:00]

**[01:18:00]** I think looking for murder in the

**[01:18:00]** I think looking for murder in the Skywalk uh saga works pretty well here.

**[01:18:03]** Skywalk uh saga works pretty well here.

**[01:18:03]** Skywalk uh saga works pretty well here. It finds the document that I've

**[01:18:05]** It finds the document that I've

**[01:18:06]** It finds the document that I've retrieved, but it can also highlight.

**[01:18:08]** retrieved, but it can also highlight.

**[01:18:08]** retrieved, but it can also highlight. Um, so here I say, "Show me the fragment

**[01:18:10]** Um, so here I say, "Show me the fragment

**[01:18:10]** Um, so here I say, "Show me the fragment that actually matched best here." Um,

**[01:18:13]** that actually matched best here." Um,

**[01:18:13]** that actually matched best here." Um, and I if I search here for murder, it

**[01:18:17]** and I if I search here for murder, it

**[01:18:17]** and I if I search here for murder, it didn't find anything, but I think the

**[01:18:19]** didn't find anything, but I think the

**[01:18:19]** didn't find anything, but I think the term that it found was in this

**[01:18:22]** term that it found was in this

**[01:18:22]** term that it found was in this highlighted segment here, it found kill.

**[01:18:24]** highlighted segment here, it found kill.

**[01:18:24]** highlighted segment here, it found kill. And it was that one that was uh expanded

**[01:18:27]** And it was that one that was uh expanded

**[01:18:27]** And it was that one that was uh expanded here. Um so here I've broken up my long

**[01:18:30]** here. Um so here I've broken up my long

**[01:18:30]** here. Um so here I've broken up my long text field into multiple chunks and

**[01:18:32]** text field into multiple chunks and

**[01:18:32]** text field into multiple chunks and there are multiple strategies you do

**[01:18:34]** there are multiple strategies you do

**[01:18:34]** there are multiple strategies you do that by page, by paragraph, by sentence.

**[01:18:37]** that by page, by paragraph, by sentence.

**[01:18:37]** that by page, by paragraph, by sentence. Um you could do it overlapping or not

**[01:18:41]** Um you could do it overlapping or not

**[01:18:41]** Um you could do it overlapping or not overlapping. Um many strategies it will

**[01:18:44]** overlapping. Um many strategies it will

**[01:18:44]** overlapping. Um many strategies it will depend on how you want to retrieve what

**[01:18:46]** depend on how you want to retrieve what

**[01:18:46]** depend on how you want to retrieve what works best for your use case, but you

**[01:18:48]** works best for your use case, but you

**[01:18:48]** works best for your use case, but you want to kind of like reduce the context

**[01:18:51]** want to kind of like reduce the context

**[01:18:51]** want to kind of like reduce the context per element that you're matching because

**[01:18:53]** per element that you're matching because

**[01:18:53]** per element that you're matching because there's only so much context that a

**[01:18:54]** there's only so much context that a

**[01:18:54]** there's only so much context that a dense vector representation can hold.

**[01:18:56]** dense vector representation can hold.

**[01:18:56]** dense vector representation can hold. Um, so you want to chunk that up,

**[01:18:59]** Um, so you want to chunk that up,

**[01:18:59]** Um, so you want to chunk that up, especially if you have like a full book,


### [01:19:00 - 01:20:00]

**[01:19:00]** especially if you have like a full book,

**[01:19:00]** especially if you have like a full book, you want to break up those individual at

**[01:19:02]** you want to break up those individual at

**[01:19:02]** you want to break up those individual at least pages. Um, and then find the

**[01:19:04]** least pages. Um, and then find the

**[01:19:04]** least pages. Um, and then find the relevant part where the match is and

**[01:19:07]** relevant part where the match is and

**[01:19:07]** relevant part where the match is and then you can actually link back to that.

**[01:19:08]** then you can actually link back to that.

**[01:19:08]** then you can actually link back to that. Um, the point in this query here is also

**[01:19:11]** Um, the point in this query here is also

**[01:19:11]** Um, the point in this query here is also to show you I didn't define any chunks.

**[01:19:14]** to show you I didn't define any chunks.

**[01:19:14]** to show you I didn't define any chunks. Um, I didn't say like okay send this

**[01:19:17]** Um, I didn't say like okay send this

**[01:19:17]** Um, I didn't say like okay send this representation of a dense vector there

**[01:19:19]** representation of a dense vector there

**[01:19:19]** representation of a dense vector there and then when it comes back interpret

**[01:19:21]** and then when it comes back interpret

**[01:19:21]** and then when it comes back interpret again. Um, this is all happening behind

**[01:19:23]** again. Um, this is all happening behind

**[01:19:23]** again. Um, this is all happening behind the scenes just to make this easier. So

**[01:19:25]** the scenes just to make this easier. So

**[01:19:25]** the scenes just to make this easier. So the entire behavior here is still very

**[01:19:28]** the entire behavior here is still very

**[01:19:28]** the entire behavior here is still very similar to the keyword matching even

**[01:19:29]** similar to the keyword matching even

**[01:19:29]** similar to the keyword matching even though there's a lot more magic

**[01:19:31]** though there's a lot more magic

**[01:19:31]** though there's a lot more magic happening behind the scenes. Um just to

**[01:19:34]** happening behind the scenes. Um just to

**[01:19:34]** happening behind the scenes. Um just to keep that very simple. Um

**[01:19:44]** how does everybody feel about longer

**[01:19:44]** how does everybody feel about longer JSON queries?

**[01:19:47]** JSON queries?

**[01:19:47]** JSON queries? Um we'll see about alternatives and

**[01:19:48]** Um we'll see about alternatives and

**[01:19:48]** Um we'll see about alternatives and maybe we can make this a bit simpler

**[01:19:50]** maybe we can make this a bit simpler

**[01:19:50]** maybe we can make this a bit simpler again. Uh but let me show you one one

**[01:19:53]** again. Uh but let me show you one one

**[01:19:53]** again. Uh but let me show you one one more way of of looking at um we call

**[01:19:56]** more way of of looking at um we call

**[01:19:56]** more way of of looking at um we call them retriever. They're a more powerful

**[01:19:59]** them retriever. They're a more powerful

**[01:19:59]** them retriever. They're a more powerful mechanism to actually combine different


### [01:20:00 - 01:21:00]

**[01:20:02]** mechanism to actually combine different

**[01:20:02]** mechanism to actually combine different types of searches. Um combining

**[01:20:05]** types of searches. Um combining

**[01:20:05]** types of searches. Um combining different types of searches, let me get

**[01:20:07]** different types of searches, let me get

**[01:20:07]** different types of searches, let me get from my slides actually when we talk

**[01:20:09]** from my slides actually when we talk

**[01:20:09]** from my slides actually when we talk about combining searches and how this

**[01:20:11]** about combining searches and how this

**[01:20:11]** about combining searches and how this all plays together. Um, this is kind of

**[01:20:14]** all plays together. Um, this is kind of

**[01:20:14]** all plays together. Um, this is kind of my my little interactive map of what you

**[01:20:18]** my my little interactive map of what you

**[01:20:18]** my my little interactive map of what you do when you do retrieval or what you

**[01:20:19]** do when you do retrieval or what you

**[01:20:20]** do when you do retrieval or what you what your searches do. So, we started

**[01:20:23]** what your searches do. So, we started

**[01:20:23]** what your searches do. So, we started here in the the lexical keyword search

**[01:20:25]** here in the the lexical keyword search

**[01:20:26]** here in the the lexical keyword search and then we run a match query and we're

**[01:20:27]** and then we run a match query and we're

**[01:20:27]** and then we run a match query and we're matching these strings. Um, this often

**[01:20:32]** matching these strings. Um, this often

**[01:20:32]** matching these strings. Um, this often combined with some rank features um are

**[01:20:35]** combined with some rank features um are

**[01:20:35]** combined with some rank features um are often what we call full text search. The

**[01:20:37]** often what we call full text search. The

**[01:20:38]** often what we call full text search. The rank features could be either you

**[01:20:39]** rank features could be either you

**[01:20:39]** rank features could be either you extract a specific signal or it could

**[01:20:41]** extract a specific signal or it could

**[01:20:41]** extract a specific signal or it could also be something um however you

**[01:20:43]** also be something um however you

**[01:20:43]** also be something um however you influence that ranking. It could be like

**[01:20:45]** influence that ranking. It could be like

**[01:20:45]** influence that ranking. It could be like the margin on a product like how many

**[01:20:47]** the margin on a product like how many

**[01:20:47]** the margin on a product like how many people bought something, what the rating

**[01:20:49]** people bought something, what the rating

**[01:20:49]** people bought something, what the rating is. There are many different signals

**[01:20:51]** is. There are many different signals

**[01:20:51]** is. There are many different signals that you could ex in include like not

**[01:20:53]** that you could ex in include like not

**[01:20:53]** that you could ex in include like not just with the the match of the the text

**[01:20:55]** just with the the match of the the text

**[01:20:55]** just with the the match of the the text but any other signals that you want to

**[01:20:57]** but any other signals that you want to

**[01:20:57]** but any other signals that you want to combine uh for retrieving that. And then

**[01:20:59]** combine uh for retrieving that. And then

**[01:20:59]** combine uh for retrieving that. And then you have like full text search as a


### [01:21:00 - 01:22:00]

**[01:21:01]** you have like full text search as a

**[01:21:01]** you have like full text search as a whole. On top of that, I kept it kind of

**[01:21:05]** whole. On top of that, I kept it kind of

**[01:21:05]** whole. On top of that, I kept it kind of like to the side here. You might have a

**[01:21:07]** like to the side here. You might have a

**[01:21:07]** like to the side here. You might have a boolean filter where you have like a

**[01:21:10]** boolean filter where you have like a

**[01:21:10]** boolean filter where you have like a hard include or exclude of certain

**[01:21:12]** hard include or exclude of certain

**[01:21:12]** hard include or exclude of certain attributes. Um this does not contribute

**[01:21:15]** attributes. Um this does not contribute

**[01:21:15]** attributes. Um this does not contribute to the score. This is just like black

**[01:21:17]** to the score. This is just like black

**[01:21:17]** to the score. This is just like black and white. This is included or excluded.

**[01:21:20]** and white. This is included or excluded.

**[01:21:20]** and white. This is included or excluded. Whereas this here calculates the score

**[01:21:22]** Whereas this here calculates the score

**[01:21:22]** Whereas this here calculates the score for you how you match. And

**[01:21:26]** for you how you match. And

**[01:21:26]** for you how you match. And then this was kind of like the the

**[01:21:28]** then this was kind of like the the

**[01:21:28]** then this was kind of like the the algorithmic side. And then we have this

**[01:21:30]** algorithmic side. And then we have this

**[01:21:30]** algorithmic side. And then we have this machine learning the learn side or the

**[01:21:32]** machine learning the learn side or the

**[01:21:32]** machine learning the learn side or the semantic search uh where you have a

**[01:21:34]** semantic search uh where you have a

**[01:21:34]** semantic search uh where you have a model behind the scenes uh split into

**[01:21:38]** model behind the scenes uh split into

**[01:21:38]** model behind the scenes uh split into the dense vector um embeddings and the

**[01:21:40]** the dense vector um embeddings and the

**[01:21:40]** the dense vector um embeddings and the sparse vector embeddings um for vector

**[01:21:43]** sparse vector embeddings um for vector

**[01:21:44]** sparse vector embeddings um for vector search or learn sparse retrieval. I

**[01:21:46]** search or learn sparse retrieval. I

**[01:21:46]** search or learn sparse retrieval. I think those are the two common terms.

**[01:21:47]** think those are the two common terms.

**[01:21:47]** think those are the two common terms. Um,

**[01:21:49]** Um,

**[01:21:49]** Um, and the the interesting thing is all of

**[01:21:52]** and the the interesting thing is all of

**[01:21:52]** and the the interesting thing is all of these including the the sparse one,

**[01:21:55]** these including the the sparse one,

**[01:21:55]** these including the the sparse one, these are the the sparse vector

**[01:21:57]** these are the the sparse vector

**[01:21:57]** these are the the sparse vector representation in the background and

**[01:21:58]** representation in the background and

**[01:21:58]** representation in the background and only this one here is the dense vector


### [01:22:00 - 01:23:00]

**[01:22:00]** only this one here is the dense vector

**[01:22:00]** only this one here is the dense vector representation. Um, and then when you

**[01:22:05]** representation. Um, and then when you

**[01:22:05]** representation. Um, and then when you combine

**[01:22:07]** combine

**[01:22:07]** combine any any grouping down here to combine

**[01:22:10]** any any grouping down here to combine

**[01:22:10]** any any grouping down here to combine for one search, this is then what we

**[01:22:13]** for one search, this is then what we

**[01:22:13]** for one search, this is then what we would call hybrid search. Um even though

**[01:22:15]** would call hybrid search. Um even though

**[01:22:15]** would call hybrid search. Um even though there can be big discussions of like

**[01:22:17]** there can be big discussions of like

**[01:22:17]** there can be big discussions of like what is exactly hybrid search or not, I

**[01:22:19]** what is exactly hybrid search or not, I

**[01:22:19]** what is exactly hybrid search or not, I will definitely stick to the definition

**[01:22:20]** will definitely stick to the definition

**[01:22:20]** will definitely stick to the definition that as soon as you combine uh more than

**[01:22:23]** that as soon as you combine uh more than

**[01:22:23]** that as soon as you combine uh more than one type of search, it could be sparse

**[01:22:25]** one type of search, it could be sparse

**[01:22:25]** one type of search, it could be sparse and dense or it could be dense and

**[01:22:27]** and dense or it could be dense and

**[01:22:27]** and dense or it could be dense and keyword or maybe if you combine two

**[01:22:30]** keyword or maybe if you combine two

**[01:22:30]** keyword or maybe if you combine two dense vector uh searches. Um then search

**[01:22:34]** dense vector uh searches. Um then search

**[01:22:34]** dense vector uh searches. Um then search because you have multiple approaches and

**[01:22:36]** because you have multiple approaches and

**[01:22:36]** because you have multiple approaches and then you can either boost them together,

**[01:22:38]** then you can either boost them together,

**[01:22:38]** then you can either boost them together, you could do re-ranking which is

**[01:22:40]** you could do re-ranking which is

**[01:22:40]** you could do re-ranking which is becoming more and more popular. Um, one

**[01:22:42]** becoming more and more popular. Um, one

**[01:22:42]** becoming more and more popular. Um, one thing that we lean heavily into is RRF,

**[01:22:44]** thing that we lean heavily into is RRF,

**[01:22:44]** thing that we lean heavily into is RRF, which is reciprocal rank fusion. Uh,

**[01:22:47]** which is reciprocal rank fusion. Uh,

**[01:22:47]** which is reciprocal rank fusion. Uh, that doesn't rely on the score, but it

**[01:22:50]** that doesn't rely on the score, but it

**[01:22:50]** that doesn't rely on the score, but it relies on the position of each search

**[01:22:52]** relies on the position of each search

**[01:22:52]** relies on the position of each search mechanism. So, it basically says like

**[01:22:55]** mechanism. So, it basically says like

**[01:22:55]** mechanism. So, it basically says like the the lexical search had this document

**[01:22:57]** the the lexical search had this document

**[01:22:57]** the the lexical search had this document at position four and the dense vector


### [01:23:00 - 01:24:00]

**[01:23:00]** at position four and the dense vector

**[01:23:00]** at position four and the dense vector search had it at position two. And then

**[01:23:02]** search had it at position two. And then

**[01:23:02]** search had it at position two. And then it kind of like evens out the position

**[01:23:04]** it kind of like evens out the position

**[01:23:04]** it kind of like evens out the position and gives you an overall position by

**[01:23:05]** and gives you an overall position by

**[01:23:05]** and gives you an overall position by blending them together rather than

**[01:23:08]** blending them together rather than

**[01:23:08]** blending them together rather than looking at the individual scores because

**[01:23:09]** looking at the individual scores because

**[01:23:09]** looking at the individual scores because they might be totally different.

**[01:23:11]** they might be totally different.

**[01:23:12]** they might be totally different. So this is kind of like the the

**[01:23:14]** So this is kind of like the the

**[01:23:14]** So this is kind of like the the information retrieval map overall and we

**[01:23:17]** information retrieval map overall and we

**[01:23:17]** information retrieval map overall and we have okay we didn't do a lot of filters

**[01:23:19]** have okay we didn't do a lot of filters

**[01:23:19]** have okay we didn't do a lot of filters but I think filters are intuitively

**[01:23:21]** but I think filters are intuitively

**[01:23:21]** but I think filters are intuitively relatively clear that you just say like

**[01:23:23]** relatively clear that you just say like

**[01:23:23]** relatively clear that you just say like I'm only interested in users with this

**[01:23:25]** I'm only interested in users with this

**[01:23:25]** I'm only interested in users with this ID or whatever other criteria. It could

**[01:23:27]** ID or whatever other criteria. It could

**[01:23:27]** ID or whatever other criteria. It could be a geo based filter like only things

**[01:23:29]** be a geo based filter like only things

**[01:23:29]** be a geo based filter like only things within 10 kilometers or only products

**[01:23:31]** within 10 kilometers or only products

**[01:23:31]** within 10 kilometers or only products that came out in the last year. Um like

**[01:23:34]** that came out in the last year. Um like

**[01:23:34]** that came out in the last year. Um like a hard yes or no. um all the others will

**[01:23:38]** a hard yes or no. um all the others will

**[01:23:38]** a hard yes or no. um all the others will give you um uh a value for the relevance

**[01:23:41]** give you um uh a value for the relevance

**[01:23:41]** give you um uh a value for the relevance and then you can blend that potentially

**[01:23:43]** and then you can blend that potentially

**[01:23:43]** and then you can blend that potentially together to give you the overall

**[01:23:45]** together to give you the overall

**[01:23:45]** together to give you the overall results. That is kind of like the the

**[01:23:47]** results. That is kind of like the the

**[01:23:47]** results. That is kind of like the the total map of search.

**[01:23:57]** Uh yeah, for for signal um so we have

**[01:23:57]** Uh yeah, for for signal um so we have our own data structure for for these

**[01:23:59]** our own data structure for for these

**[01:23:59]** our own data structure for for these rank features. It could be for example


### [01:24:00 - 01:25:00]

**[01:24:01]** rank features. It could be for example

**[01:24:01]** rank features. It could be for example the I don't know the the rating of a

**[01:24:04]** the I don't know the the rating of a

**[01:24:04]** the I don't know the the rating of a book and then you combine um

**[01:24:09]** book and then you combine um

**[01:24:09]** book and then you combine um the the keyword match for I don't know

**[01:24:12]** the the keyword match for I don't know

**[01:24:12]** the the keyword match for I don't know you you search for um murder mysteries

**[01:24:16]** you you search for um murder mysteries

**[01:24:16]** you you search for um murder mysteries uh but then another feature would be um

**[01:24:19]** uh but then another feature would be um

**[01:24:19]** uh but then another feature would be um how well they are ranked and then you

**[01:24:21]** how well they are ranked and then you

**[01:24:21]** how well they are ranked and then you would see that or it could be your

**[01:24:23]** would see that or it could be your

**[01:24:23]** would see that or it could be your margin on the product or the stock you

**[01:24:26]** margin on the product or the stock you

**[01:24:26]** margin on the product or the stock you have available and you would want to

**[01:24:27]** have available and you would want to

**[01:24:27]** have available and you would want to show the products where you have more in

**[01:24:29]** show the products where you have more in

**[01:24:29]** show the products where you have more in Uh there can be or it might even be a

**[01:24:32]** Uh there can be or it might even be a

**[01:24:32]** Uh there can be or it might even be a simple like a click stream like what

**[01:24:33]** simple like a click stream like what

**[01:24:34]** simple like a click stream like what have people clicked before. There are a

**[01:24:35]** have people clicked before. There are a

**[01:24:35]** have people clicked before. There are a lot of different signals that you could

**[01:24:37]** lot of different signals that you could

**[01:24:37]** lot of different signals that you could include in all of this searching. Then

**[01:24:46]** any other questions or everybody good

**[01:24:46]** any other questions or everybody good for now? Yeah.


### [01:25:00 - 01:26:00]

**[01:25:05]** Yeah. So they are you would have to

**[01:25:05]** Yeah. So they are you would have to normalize them. They will be so

**[01:25:07]** normalize them. They will be so

**[01:25:07]** normalize them. They will be so depending on like if you have depending

**[01:25:09]** depending on like if you have depending

**[01:25:09]** depending on like if you have depending on the the comparison that you do for

**[01:25:12]** on the the comparison that you do for

**[01:25:12]** on the the comparison that you do for dense vectors it might be between uh

**[01:25:14]** dense vectors it might be between uh

**[01:25:14]** dense vectors it might be between uh zero and one but you saw that for the

**[01:25:16]** zero and one but you saw that for the

**[01:25:16]** zero and one but you saw that for the keyword search uh also depending on how

**[01:25:18]** keyword search uh also depending on how

**[01:25:18]** keyword search uh also depending on how many words I was searching for it might

**[01:25:20]** many words I was searching for it might

**[01:25:20]** many words I was searching for it might be much higher value. There is there's

**[01:25:22]** be much higher value. There is there's

**[01:25:22]** be much higher value. There is there's no really real ceiling for that. Um or

**[01:25:25]** no really real ceiling for that. Um or

**[01:25:25]** no really real ceiling for that. Um or you could add a boost and say like this

**[01:25:28]** you could add a boost and say like this

**[01:25:28]** you could add a boost and say like this field is 20 times more important than

**[01:25:30]** field is 20 times more important than

**[01:25:30]** field is 20 times more important than this other field. Um there is no real

**[01:25:32]** this other field. Um there is no real

**[01:25:32]** this other field. Um there is no real max value that you would have here. You

**[01:25:34]** max value that you would have here. You

**[01:25:34]** max value that you would have here. You could normalize the score and then

**[01:25:36]** could normalize the score and then

**[01:25:36]** could normalize the score and then basically say like I'll take like the

**[01:25:38]** basically say like I'll take like the

**[01:25:38]** basically say like I'll take like the highest value in this sub query as 100%

**[01:25:42]** highest value in this sub query as 100%

**[01:25:42]** highest value in this sub query as 100% and then reduce everything down by that

**[01:25:43]** and then reduce everything down by that

**[01:25:43]** and then reduce everything down by that factor and then I combine them. Maybe

**[01:25:46]** factor and then I combine them. Maybe

**[01:25:46]** factor and then I combine them. Maybe that works well. RF is a it's a very

**[01:25:49]** that works well. RF is a it's a very

**[01:25:49]** that works well. RF is a it's a very simple paper. I think it's like two

**[01:25:50]** simple paper. I think it's like two

**[01:25:50]** simple paper. I think it's like two pages. Um and it really just takes the

**[01:25:53]** pages. Um and it really just takes the

**[01:25:53]** pages. Um and it really just takes the different positions. I think it's 1

**[01:25:54]** different positions. I think it's 1

**[01:25:54]** different positions. I think it's 1 divided by 60, which is like a factor

**[01:25:57]** divided by 60, which is like a factor

**[01:25:57]** divided by 60, which is like a factor they figured out made sense, plus the

**[01:25:59]** they figured out made sense, plus the

**[01:25:59]** they figured out made sense, plus the position. Uh, and then you add the


### [01:26:00 - 01:27:00]

**[01:26:01]** position. Uh, and then you add the

**[01:26:01]** position. Uh, and then you add the scores or like the positions for each

**[01:26:03]** scores or like the positions for each

**[01:26:03]** scores or like the positions for each document together. And then that value

**[01:26:06]** document together. And then that value

**[01:26:06]** document together. And then that value gives you the overall position. Um, it's

**[01:26:09]** gives you the overall position. Um, it's

**[01:26:09]** gives you the overall position. Um, it's really just it doesn't look at the score

**[01:26:11]** really just it doesn't look at the score

**[01:26:11]** really just it doesn't look at the score anymore, but it blends the different

**[01:26:12]** anymore, but it blends the different

**[01:26:12]** anymore, but it blends the different positions together and like how they are

**[01:26:14]** positions together and like how they are

**[01:26:14]** positions together and like how they are interle and what should be first or

**[01:26:16]** interle and what should be first or

**[01:26:16]** interle and what should be first or second. And

**[01:26:18]** second. And

**[01:26:18]** second. And um, yeah.


### [01:27:00 - 01:28:00]

**[01:27:01]** I mean

**[01:27:01]** I mean feature vector will always be there

**[01:27:02]** feature vector will always be there

**[01:27:02]** feature vector will always be there because like if you are already using

**[01:27:03]** because like if you are already using

**[01:27:04]** because like if you are already using postgress it's very easy to add um I

**[01:27:05]** postgress it's very easy to add um I

**[01:27:06]** postgress it's very easy to add um I think then the question is like does it

**[01:27:07]** think then the question is like does it

**[01:27:07]** think then the question is like does it have all the features uh that you need

**[01:27:09]** have all the features uh that you need

**[01:27:09]** have all the features uh that you need for example

**[01:27:11]** for example

**[01:27:11]** for example postress doesn't even do BM25

**[01:27:13]** postress doesn't even do BM25

**[01:27:13]** postress doesn't even do BM25 um it has some matching but it's not the

**[01:27:15]** um it has some matching but it's not the

**[01:27:15]** um it has some matching but it's not the full BM25 algorithm because I don't

**[01:27:17]** full BM25 algorithm because I don't

**[01:27:17]** full BM25 algorithm because I don't think it keeps all the statistics um it

**[01:27:19]** think it keeps all the statistics um it

**[01:27:19]** think it keeps all the statistics um it will be a question of like scaling out

**[01:27:21]** will be a question of like scaling out

**[01:27:21]** will be a question of like scaling out postgress can be a problem and then just

**[01:27:23]** postgress can be a problem and then just

**[01:27:24]** postgress can be a problem and then just like the breadth of all the search

**[01:27:25]** like the breadth of all the search

**[01:27:25]** like the breadth of all the search features um if you only need vector

**[01:27:28]** features um if you only need vector

**[01:27:28]** features um if you only need vector search um I think my or our default

**[01:27:32]** search um I think my or our default

**[01:27:32]** search um I think my or our default question back to that is like do you

**[01:27:33]** question back to that is like do you

**[01:27:34]** question back to that is like do you really only need vector search um maybe

**[01:27:36]** really only need vector search um maybe

**[01:27:36]** really only need vector search um maybe for your use case but for many use cases

**[01:27:38]** for your use case but for many use cases

**[01:27:38]** for your use case but for many use cases you probably need hybrid search uh one

**[01:27:41]** you probably need hybrid search uh one

**[01:27:41]** you probably need hybrid search uh one area for example where vector search

**[01:27:44]** area for example where vector search

**[01:27:44]** area for example where vector search will not do great is like if somebody

**[01:27:46]** will not do great is like if somebody

**[01:27:46]** will not do great is like if somebody searches for like a brand because there

**[01:27:48]** searches for like a brand because there

**[01:27:48]** searches for like a brand because there is no easy representation in most models

**[01:27:52]** is no easy representation in most models

**[01:27:52]** is no easy representation in most models uh for the specific brand and it will be

**[01:27:53]** uh for the specific brand and it will be

**[01:27:53]** uh for the specific brand and it will be very hard to beat keyword search. So

**[01:27:55]** very hard to beat keyword search. So

**[01:27:55]** very hard to beat keyword search. So there will be very and also your users

**[01:27:58]** there will be very and also your users

**[01:27:58]** there will be very and also your users very angry they know you have this word

**[01:27:59]** very angry they know you have this word


### [01:28:00 - 01:29:00]

**[01:28:00]** very angry they know you have this word somewhere in your documents uh or in

**[01:28:01]** somewhere in your documents uh or in

**[01:28:01]** somewhere in your documents uh or in your data set but you don't give me the

**[01:28:03]** your data set but you don't give me the

**[01:28:03]** your data set but you don't give me the result back. Um so there are many

**[01:28:06]** result back. Um so there are many

**[01:28:06]** result back. Um so there are many scenarios where you probably want hybrid

**[01:28:08]** scenarios where you probably want hybrid

**[01:28:08]** scenarios where you probably want hybrid search or I feel like that's the we

**[01:28:10]** search or I feel like that's the we

**[01:28:10]** search or I feel like that's the we started two years ago we started with

**[01:28:12]** started two years ago we started with

**[01:28:12]** started two years ago we started with just vector search but I feel like the

**[01:28:14]** just vector search but I feel like the

**[01:28:14]** just vector search but I feel like the overall trend is coming more to hybrid

**[01:28:16]** overall trend is coming more to hybrid

**[01:28:16]** overall trend is coming more to hybrid search because you probably some sort of

**[01:28:19]** search because you probably some sort of

**[01:28:19]** search because you probably some sort of key um and then you want to have that

**[01:28:22]** key um and then you want to have that

**[01:28:22]** key um and then you want to have that combined probably with some model uh for

**[01:28:25]** combined probably with some model uh for

**[01:28:25]** combined probably with some model uh for the added benefit and extra text. Um but

**[01:28:29]** the added benefit and extra text. Um but

**[01:28:29]** the added benefit and extra text. Um but you often want the combination. It might

**[01:28:31]** you often want the combination. It might

**[01:28:31]** you often want the combination. It might also depend a bit on like the types of

**[01:28:33]** also depend a bit on like the types of

**[01:28:33]** also depend a bit on like the types of queries that your users run. So if your

**[01:28:35]** queries that your users run. So if your

**[01:28:35]** queries that your users run. So if your users run single word queries like I've

**[01:28:37]** users run single word queries like I've

**[01:28:37]** users run single word queries like I've done in my examples, that's often not

**[01:28:39]** done in my examples, that's often not

**[01:28:40]** done in my examples, that's often not really ideal for vector search because

**[01:28:41]** really ideal for vector search because

**[01:28:42]** really ideal for vector search because you live off like any machine learn

**[01:28:44]** you live off like any machine learn

**[01:28:44]** you live off like any machine learn because you live off extra context. Um

**[01:28:47]** because you live off extra context. Um

**[01:28:47]** because you live off extra context. Um so depending on that I've seen some

**[01:28:50]** so depending on that I've seen some

**[01:28:50]** so depending on that I've seen some people build searches where it's like if

**[01:28:52]** people build searches where it's like if

**[01:28:52]** people build searches where it's like if you search for one or two words they do

**[01:28:54]** you search for one or two words they do

**[01:28:54]** you search for one or two words they do keyword search but if you search for

**[01:28:55]** keyword search but if you search for

**[01:28:55]** keyword search but if you search for more they might fall over to vector

**[01:28:57]** more they might fall over to vector

**[01:28:57]** more they might fall over to vector search. So it depends a bit on the

**[01:28:58]** search. So it depends a bit on the

**[01:28:58]** search. So it depends a bit on the context what works. Um if you really


### [01:29:00 - 01:30:00]

**[01:29:01]** context what works. Um if you really

**[01:29:01]** context what works. Um if you really only need vector search um and PG vector

**[01:29:04]** only need vector search um and PG vector

**[01:29:04]** only need vector search um and PG vector is small enough uh to do all of that um

**[01:29:08]** is small enough uh to do all of that um

**[01:29:08]** is small enough uh to do all of that um and postquest is your primary data store

**[01:29:10]** and postquest is your primary data store

**[01:29:10]** and postquest is your primary data store then that's probably where you will do

**[01:29:11]** then that's probably where you will do

**[01:29:11]** then that's probably where you will do well uh but there are plenty of

**[01:29:13]** well uh but there are plenty of

**[01:29:13]** well uh but there are plenty of scenarios where that will or not all of

**[01:29:15]** scenarios where that will or not all of

**[01:29:15]** scenarios where that will or not all of those necessary boxes will be ticked.


### [01:30:00 - 01:31:00]

**[01:30:27]** But so you would create so it's one data

**[01:30:27]** But so you would create so it's one data set basically with thousands of files

**[01:30:28]** set basically with thousands of files

**[01:30:28]** set basically with thousands of files that all are chunked together and so one

**[01:30:30]** that all are chunked together and so one

**[01:30:30]** that all are chunked together and so one change would invalidate all of them or


### [01:31:00 - 01:32:00]

**[01:31:17]** maybe so

**[01:31:17]** maybe so I think the way we might solve it is

**[01:31:20]** I think the way we might solve it is

**[01:31:20]** I think the way we might solve it is that if you create the hash of the file

**[01:31:22]** that if you create the hash of the file

**[01:31:22]** that if you create the hash of the file and use that as the ID and you only use

**[01:31:25]** and use that as the ID and you only use

**[01:31:25]** and use that as the ID and you only use the operation create and it would reject

**[01:31:27]** the operation create and it would reject

**[01:31:28]** the operation create and it would reject any any duplicate rights, you would at

**[01:31:31]** any any duplicate rights, you would at

**[01:31:31]** any any duplicate rights, you would at least not ingest and and then create the

**[01:31:33]** least not ingest and and then create the

**[01:31:33]** least not ingest and and then create the vector representation again. Um it will

**[01:31:36]** vector representation again. Um it will

**[01:31:36]** vector representation again. Um it will still send it over again and it would

**[01:31:39]** still send it over again and it would

**[01:31:39]** still send it over again and it would need to get rejected. ID.

**[01:31:42]** need to get rejected. ID.

**[01:31:42]** need to get rejected. ID. Yes. If you if you have that doc ID and

**[01:31:44]** Yes. If you if you have that doc ID and

**[01:31:44]** Yes. If you if you have that doc ID and then you need to set the operation to

**[01:31:46]** then you need to set the operation to

**[01:31:46]** then you need to set the operation to just create and not uh update or upsert

**[01:31:49]** just create and not uh update or upsert

**[01:31:49]** just create and not uh update or upsert uh then it would just be rejected and

**[01:31:51]** uh then it would just be rejected and

**[01:31:51]** uh then it would just be rejected and you would only write it once.

**[01:31:54]** you would only write it once.

**[01:31:54]** you would only write it once. I'm not sure if that is a great use case

**[01:31:56]** I'm not sure if that is a great use case

**[01:31:56]** I'm not sure if that is a great use case or if you might want to keep like a I

**[01:31:58]** or if you might want to keep like a I

**[01:31:58]** or if you might want to keep like a I don't know an outside cache of like all

**[01:31:59]** don't know an outside cache of like all

**[01:31:59]** don't know an outside cache of like all the hashes that you've already had and


### [01:32:00 - 01:33:00]

**[01:32:01]** the hashes that you've already had and

**[01:32:01]** the hashes that you've already had and dduplicate it there. But that would be

**[01:32:03]** dduplicate it there. But that would be

**[01:32:03]** dduplicate it there. But that would be the elastic search solution of like

**[01:32:04]** the elastic search solution of like

**[01:32:04]** the elastic search solution of like using the the hash as the ID and then

**[01:32:07]** using the the hash as the ID and then

**[01:32:07]** using the the hash as the ID and then just writing to that.

**[01:32:14]** Okay. And although with create on the

**[01:32:14]** Okay. And although with create on the Yeah, that that is I think the intuitive

**[01:32:17]** Yeah, that that is I think the intuitive

**[01:32:17]** Yeah, that that is I think the intuitive or most native approach that we could

**[01:32:19]** or most native approach that we could

**[01:32:19]** or most native approach that we could offer for that. Yeah, I think there was

**[01:32:21]** offer for that. Yeah, I think there was

**[01:32:21]** offer for that. Yeah, I think there was some other question somewhere. Uh yeah.

**[01:32:51]** But uh from what I remember the default

**[01:32:51]** But uh from what I remember the default post full text search does not do full

**[01:32:53]** post full text search does not do full

**[01:32:53]** post full text search does not do full BM25. five, but it only does it doesn't

**[01:32:55]** BM25. five, but it only does it doesn't

**[01:32:55]** BM25. five, but it only does it doesn't have all the statistics, I think, from

**[01:32:56]** have all the statistics, I think, from

**[01:32:56]** have all the statistics, I think, from what I remember. Yeah.


### [01:33:00 - 01:34:00]

**[01:33:04]** Any other questions?

**[01:33:04]** Any other questions? Uh Joe, please go ahead.

**[01:33:15]** To to show now. Yeah. I mean, how much

**[01:33:15]** To to show now. Yeah. I mean, how much chase do you want to see?

**[01:33:18]** chase do you want to see?

**[01:33:18]** chase do you want to see? Um

**[01:33:52]** Yes. Um

**[01:33:52]** Yes. Um May maybe for before we dive into that

**[01:33:55]** May maybe for before we dive into that

**[01:33:55]** May maybe for before we dive into that be for everybody else like rescoring is

**[01:33:57]** be for everybody else like rescoring is

**[01:33:57]** be for everybody else like rescoring is like let's say we have a million

**[01:33:59]** like let's say we have a million

**[01:33:59]** like let's say we have a million documents and then we have one cheaper


### [01:34:00 - 01:35:00]

**[01:34:01]** documents and then we have one cheaper

**[01:34:01]** documents and then we have one cheaper way of retrieving them and we retrieve

**[01:34:03]** way of retrieving them and we retrieve

**[01:34:03]** way of retrieving them and we retrieve the top I don't know a thousand

**[01:34:05]** the top I don't know a thousand

**[01:34:05]** the top I don't know a thousand candidates and then we have a more

**[01:34:06]** candidates and then we have a more

**[01:34:06]** candidates and then we have a more expensive way but higher quality way of

**[01:34:09]** expensive way but higher quality way of

**[01:34:09]** expensive way but higher quality way of actually rescoring them then we will run

**[01:34:11]** actually rescoring them then we will run

**[01:34:11]** actually rescoring them then we will run this more expensive rescoring on just

**[01:34:13]** this more expensive rescoring on just

**[01:34:13]** this more expensive rescoring on just the top thousand uh to get our ultimate

**[01:34:16]** the top thousand uh to get our ultimate

**[01:34:16]** the top thousand uh to get our ultimate result list of of results but the the

**[01:34:20]** result list of of results but the the

**[01:34:20]** result list of of results but the the rescoring algorithm would be too

**[01:34:21]** rescoring algorithm would be too

**[01:34:21]** rescoring algorithm would be too expensive uh to run it across like the

**[01:34:23]** expensive uh to run it across like the

**[01:34:23]** expensive uh to run it across like the million documents that why you don't

**[01:34:25]** million documents that why you don't

**[01:34:25]** million documents that why you don't want to do that that's why you twostep

**[01:34:27]** want to do that that's why you twostep

**[01:34:27]** want to do that that's why you twostep process and that's why you might want to

**[01:34:30]** process and that's why you might want to

**[01:34:30]** process and that's why you might want to have the the rescoring so yes we have a

**[01:34:33]** have the the rescoring so yes we have a

**[01:34:33]** have the the rescoring so yes we have a you can in elastic search now you can do

**[01:34:34]** you can in elastic search now you can do

**[01:34:34]** you can in elastic search now you can do rescoring because it becomes more and

**[01:34:36]** rescoring because it becomes more and

**[01:34:36]** rescoring because it becomes more and more popular um I don't have a full

**[01:34:40]** more popular um I don't have a full

**[01:34:40]** more popular um I don't have a full example there but we do have like we do

**[01:34:43]** example there but we do have like we do

**[01:34:43]** example there but we do have like we do have a rescoring model built in by

**[01:34:45]** have a rescoring model built in by

**[01:34:45]** have a rescoring model built in by default now let me pull that up um

**[01:34:50]** default now let me pull that up um

**[01:34:50]** default now let me pull that up um not this one. So we have currently it's

**[01:34:53]** not this one. So we have currently it's

**[01:34:53]** not this one. So we have currently it's the the version one re-ranking but we

**[01:34:55]** the the version one re-ranking but we

**[01:34:55]** the the version one re-ranking but we have a built-in re-ranking uh model now

**[01:34:58]** have a built-in re-ranking uh model now

**[01:34:58]** have a built-in re-ranking uh model now as well. So for one of the tasks uh that


### [01:35:00 - 01:36:00]

**[01:35:01]** as well. So for one of the tasks uh that

**[01:35:01]** as well. So for one of the tasks uh that we can do um you can see here we have

**[01:35:04]** we can do um you can see here we have

**[01:35:04]** we can do um you can see here we have the other tasks like for example the

**[01:35:06]** the other tasks like for example the

**[01:35:06]** the other tasks like for example the dense text embedding now we have a

**[01:35:09]** dense text embedding now we have a

**[01:35:09]** dense text embedding now we have a reranking task that you can also call

**[01:35:13]** reranking task that you can also call

**[01:35:13]** reranking task that you can also call your question how do you express that

**[01:35:15]** your question how do you express that

**[01:35:15]** your question how do you express that okay

**[01:35:32]** reranking is good. Let me uh somehow my

**[01:35:32]** reranking is good. Let me uh somehow my keyboard binding is broken. This is very

**[01:35:34]** keyboard binding is broken. This is very

**[01:35:34]** keyboard binding is broken. This is very annoying.

**[01:35:43]** Okay. Um we rerank results. Let me see.

**[01:35:44]** Okay. Um we rerank results. Let me see. Somewhere here there should be so

**[01:35:46]** Somewhere here there should be so

**[01:35:46]** Somewhere here there should be so there's learn to rank. Um

**[01:35:50]** there's learn to rank. Um

**[01:35:50]** there's learn to rank. Um but it should not be the only one.

**[01:35:55]** but it should not be the only one.

**[01:35:55]** but it should not be the only one. This is what we want. Okay. We have our

**[01:35:57]** This is what we want. Okay. We have our

**[01:35:57]** This is what we want. Okay. We have our re-ranking model. Um,


### [01:36:00 - 01:37:00]

**[01:36:05]** unless Dave, you know from the top of

**[01:36:05]** unless Dave, you know from the top of your head where we have the right docs

**[01:36:06]** your head where we have the right docs

**[01:36:06]** your head where we have the right docs for this.

**[01:36:14]** Yeah, retrievers could find them.

**[01:36:14]** Yeah, retrievers could find them. Starting in 8.16


### [01:37:00 - 01:38:00]

**[01:37:32]** Yeah. So I think this is a simple

**[01:37:32]** Yeah. So I think this is a simple example like we have a standard match

**[01:37:34]** example like we have a standard match

**[01:37:34]** example like we have a standard match like this is will be very cheap and then

**[01:37:36]** like this is will be very cheap and then

**[01:37:36]** like this is will be very cheap and then we have the text simulated rarity

**[01:37:39]** we have the text simulated rarity

**[01:37:39]** we have the text simulated rarity reranker which uses our elastic reranker

**[01:37:43]** reranker which uses our elastic reranker

**[01:37:43]** reranker which uses our elastic reranker um that falls back to that model behind

**[01:37:44]** um that falls back to that model behind

**[01:37:44]** um that falls back to that model behind the scenes. Think about it. I was a

**[01:37:48]** the scenes. Think about it. I was a

**[01:37:48]** the scenes. Think about it. I was a function


### [01:38:00 - 01:39:00]

**[01:38:13]** of those results.

**[01:38:13]** of those results. structure.


### [01:39:00 - 01:40:00]

**[01:39:53]** Yeah. So the

**[01:39:53]** Yeah. So the just to give you the example of like I

**[01:39:55]** just to give you the example of like I

**[01:39:55]** just to give you the example of like I don't think I have a re-ranking example

**[01:39:57]** don't think I have a re-ranking example

**[01:39:57]** don't think I have a re-ranking example here but this one um


### [01:40:00 - 01:41:00]

**[01:40:00]** here but this one um

**[01:40:00]** here but this one um uses a classic keyword match uh for

**[01:40:03]** uses a classic keyword match uh for

**[01:40:04]** uses a classic keyword match uh for retriever and then we have we normalize

**[01:40:06]** retriever and then we have we normalize

**[01:40:06]** retriever and then we have we normalize here the score I think somebody else

**[01:40:08]** here the score I think somebody else

**[01:40:08]** here the score I think somebody else asked about the normal or we had a

**[01:40:10]** asked about the normal or we had a

**[01:40:10]** asked about the normal or we had a discussion about the normal normalizing

**[01:40:11]** discussion about the normal normalizing

**[01:40:11]** discussion about the normal normalizing we do a minmax normalizing we this with

**[01:40:14]** we do a minmax normalizing we this with

**[01:40:14]** we do a minmax normalizing we this with two um and then I use the openi

**[01:40:16]** two um and then I use the openi

**[01:40:16]** two um and then I use the openi embeddings with a again normalized with

**[01:40:20]** embeddings with a again normalized with

**[01:40:20]** embeddings with a again normalized with a weight of 1.5 5 and then they will get

**[01:40:23]** a weight of 1.5 5 and then they will get

**[01:40:23]** a weight of 1.5 5 and then they will get blended together and you you get the

**[01:40:25]** blended together and you you get the

**[01:40:25]** blended together and you you get the results that won't surprise you that

**[01:40:26]** results that won't surprise you that

**[01:40:26]** results that won't surprise you that these are not the droids you're looking

**[01:40:27]** these are not the droids you're looking

**[01:40:27]** these are not the droids you're looking for. If you search for uh droid and

**[01:40:29]** for. If you search for uh droid and

**[01:40:29]** for. If you search for uh droid and robot um will be by far the highest

**[01:40:32]** robot um will be by far the highest

**[01:40:32]** robot um will be by far the highest ranking document.

**[01:40:34]** ranking document.

**[01:40:34]** ranking document. You had a question somewhere. Yes.


### [01:41:00 - 01:42:00]

**[01:41:16]** I mean I I mean so in the first so we

**[01:41:16]** I mean I I mean so in the first so we would retrieve like X candidates and you

**[01:41:18]** would retrieve like X candidates and you

**[01:41:18]** would retrieve like X candidates and you could define the number of candidates

**[01:41:20]** could define the number of candidates

**[01:41:20]** could define the number of candidates and then we would run the reranking on

**[01:41:21]** and then we would run the reranking on

**[01:41:21]** and then we would run the reranking on top of those. So that it will be a

**[01:41:24]** top of those. So that it will be a

**[01:41:24]** top of those. So that it will be a trade-off for you like the larger the

**[01:41:26]** trade-off for you like the larger the

**[01:41:26]** trade-off for you like the larger the window is the the slower it will be but

**[01:41:28]** window is the the slower it will be but

**[01:41:28]** window is the the slower it will be but the potentially higher quality your

**[01:41:30]** the potentially higher quality your

**[01:41:30]** the potentially higher quality your overall results will be because you will

**[01:41:33]** overall results will be because you will

**[01:41:33]** overall results will be because you will just have everything in your data data

**[01:41:35]** just have everything in your data data

**[01:41:35]** just have everything in your data data data set that you can then rerank at the

**[01:41:37]** data set that you can then rerank at the

**[01:41:37]** data set that you can then rerank at the end of the day.

**[01:41:39]** end of the day.

**[01:41:39]** end of the day. Is that what you meant or you want

**[01:41:41]** Is that what you meant or you want

**[01:41:41]** Is that what you meant or you want something

**[01:41:43]** something

**[01:41:43]** something per node or Yeah.


### [01:42:00 - 01:43:00]

**[01:42:10]** Yeah, I don't think that's how we do it.

**[01:42:10]** Yeah, I don't think that's how we do it. So what what you can control here is

**[01:42:12]** So what what you can control here is

**[01:42:12]** So what what you can control here is like this is a window of like what you

**[01:42:14]** like this is a window of like what you

**[01:42:14]** like this is a window of like what you might retrieve and then we have the

**[01:42:16]** might retrieve and then we have the

**[01:42:16]** might retrieve and then we have the minimum score like a cut off point uh to

**[01:42:19]** minimum score like a cut off point uh to

**[01:42:19]** minimum score like a cut off point uh to throw out what might not be relevant

**[01:42:21]** throw out what might not be relevant

**[01:42:21]** throw out what might not be relevant anyway to to keep that a bit cheaper.

**[01:42:23]** anyway to to keep that a bit cheaper.

**[01:42:23]** anyway to to keep that a bit cheaper. That's what we have here.

**[01:42:26]** That's what we have here.

**[01:42:26]** That's what we have here. Um

**[01:42:32]** those are the retrievers. Uh and then

**[01:42:32]** those are the retrievers. Uh and then you could do the RF that I've explained

**[01:42:33]** you could do the RF that I've explained

**[01:42:33]** you could do the RF that I've explained where you blend results together. All of

**[01:42:35]** where you blend results together. All of

**[01:42:35]** where you blend results together. All of that is easy. Um, one final note, if you

**[01:42:40]** that is easy. Um, one final note, if you

**[01:42:40]** that is easy. Um, one final note, if you if you got tired of all the JSON, um,

**[01:42:44]** if you got tired of all the JSON, um,

**[01:42:44]** if you got tired of all the JSON, um, we have a new way of defining those

**[01:42:45]** we have a new way of defining those

**[01:42:45]** we have a new way of defining those queries as well. Um, where here we have

**[01:42:49]** queries as well. Um, where here we have

**[01:42:49]** queries as well. Um, where here we have a match operator like the one we've used

**[01:42:51]** a match operator like the one we've used

**[01:42:51]** a match operator like the one we've used all the time, uh, that you can use

**[01:42:52]** all the time, uh, that you can use

**[01:42:52]** all the time, uh, that you can use either on a keyword field, but it could

**[01:42:54]** either on a keyword field, but it could

**[01:42:54]** either on a keyword field, but it could also be either a dense or a sparse

**[01:42:56]** also be either a dense or a sparse

**[01:42:56]** also be either a dense or a sparse vector embedding and then you can just

**[01:42:58]** vector embedding and then you can just

**[01:42:58]** vector embedding and then you can just run a query on that and then just get


### [01:43:00 - 01:44:00]

**[01:43:00]** run a query on that and then just get

**[01:43:00]** run a query on that and then just get the the scores from that. So it is a

**[01:43:03]** the the scores from that. So it is a

**[01:43:03]** the the scores from that. So it is a pipe query language. It's a bit more

**[01:43:04]** pipe query language. It's a bit more

**[01:43:04]** pipe query language. It's a bit more like I don't know like a shell. Um but

**[01:43:06]** like I don't know like a shell. Um but

**[01:43:06]** like I don't know like a shell. Um but if you don't want to type all the JSON

**[01:43:08]** if you don't want to type all the JSON

**[01:43:08]** if you don't want to type all the JSON anymore, uh this is how you can do that.

**[01:43:10]** anymore, uh this is how you can do that.

**[01:43:10]** anymore, uh this is how you can do that. And here my screen size is a bit off. Uh

**[01:43:13]** And here my screen size is a bit off. Uh

**[01:43:13]** And here my screen size is a bit off. Uh but yeah, you get the the quote that we

**[01:43:15]** but yeah, you get the the quote that we

**[01:43:15]** but yeah, you get the the quote that we retrieved the speaker and the the score.

**[01:43:18]** retrieved the speaker and the the score.

**[01:43:18]** retrieved the speaker and the the score. Maybe maybe I'll take out the speaker to

**[01:43:21]** Maybe maybe I'll take out the speaker to

**[01:43:21]** Maybe maybe I'll take out the speaker to make this slightly more readable.

**[01:43:38]** Oh. Um,

**[01:43:38]** Oh. Um, this is you could write queries with a

**[01:43:41]** this is you could write queries with a

**[01:43:41]** this is you could write queries with a fraction of the JSON. Uh, this will also

**[01:43:43]** fraction of the JSON. Uh, this will also

**[01:43:43]** fraction of the JSON. Uh, this will also support funny things like joints. It

**[01:43:46]** support funny things like joints. It

**[01:43:46]** support funny things like joints. It doesn't have every single search feature

**[01:43:48]** doesn't have every single search feature

**[01:43:48]** doesn't have every single search feature yet. Uh, but it's getting pretty close.

**[01:43:50]** yet. Uh, but it's getting pretty close.

**[01:43:50]** yet. Uh, but it's getting pretty close. So, this is more like a closing out at

**[01:43:52]** So, this is more like a closing out at

**[01:43:52]** So, this is more like a closing out at the end. If you're tired of all the JSON

**[01:43:54]** the end. If you're tired of all the JSON

**[01:43:54]** the end. If you're tired of all the JSON queries, you don't have to write JSON

**[01:43:56]** queries, you don't have to write JSON

**[01:43:56]** queries, you don't have to write JSON queries anymore. Um

**[01:43:58]** queries anymore. Um

**[01:43:58]** queries anymore. Um this is nice both for like observability


### [01:44:00 - 01:45:00]

**[01:44:01]** this is nice both for like observability

**[01:44:01]** this is nice both for like observability use cases where you have like just like

**[01:44:03]** use cases where you have like just like

**[01:44:03]** use cases where you have like just like aggregations and things like that but

**[01:44:05]** aggregations and things like that but

**[01:44:05]** aggregations and things like that but it's also very helpful for full text

**[01:44:07]** it's also very helpful for full text

**[01:44:07]** it's also very helpful for full text search. Now um if you want to write

**[01:44:09]** search. Now um if you want to write

**[01:44:09]** search. Now um if you want to write different queries I think the main

**[01:44:10]** different queries I think the main

**[01:44:10]** different queries I think the main downside is that the language support in

**[01:44:13]** downside is that the language support in

**[01:44:13]** downside is that the language support in the different languages like Java etc is

**[01:44:15]** the different languages like Java etc is

**[01:44:15]** the different languages like Java etc is not very strong yet. You basically give

**[01:44:17]** not very strong yet. You basically give

**[01:44:17]** not very strong yet. You basically give it strings and then it gives you a

**[01:44:18]** it strings and then it gives you a

**[01:44:18]** it strings and then it gives you a result back that you need to parse out

**[01:44:20]** result back that you need to parse out

**[01:44:20]** result back that you need to parse out again. Uh so it is not as strongly typed

**[01:44:23]** again. Uh so it is not as strongly typed

**[01:44:23]** again. Uh so it is not as strongly typed on the client side yet as the other

**[01:44:24]** on the client side yet as the other

**[01:44:24]** on the client side yet as the other languages. Um

**[01:44:28]** languages. Um

**[01:44:28]** languages. Um any final questions? Yes.


### [01:45:00 - 01:46:00]

**[01:45:17]** I mean, we can make your life easier.

**[01:45:17]** I mean, we can make your life easier. It's it's just all behind one single uh

**[01:45:19]** It's it's just all behind one single uh

**[01:45:19]** It's it's just all behind one single uh query endpoint. So, you you could use

**[01:45:21]** query endpoint. So, you you could use

**[01:45:21]** query endpoint. So, you you could use the two different methods to retrieve.

**[01:45:23]** the two different methods to retrieve.

**[01:45:23]** the two different methods to retrieve. Um and then you could still rerank but

**[01:45:25]** Um and then you could still rerank but

**[01:45:25]** Um and then you could still rerank but all from one single query. So, you don't

**[01:45:28]** all from one single query. So, you don't

**[01:45:28]** all from one single query. So, you don't have to do it yourself. I mean, it's not

**[01:45:30]** have to do it yourself. I mean, it's not

**[01:45:30]** have to do it yourself. I mean, it's not like we want to stop you, but you don't

**[01:45:31]** like we want to stop you, but you don't

**[01:45:31]** like we want to stop you, but you don't have to and we can make your life a bit

**[01:45:33]** have to and we can make your life a bit

**[01:45:33]** have to and we can make your life a bit easier. Like, I'm just curious instead

**[01:45:35]** easier. Like, I'm just curious instead

**[01:45:35]** easier. Like, I'm just curious instead of just like

**[01:45:44]** I mean it's only one single query that

**[01:45:44]** I mean it's only one single query that you need to run and like one single

**[01:45:46]** you need to run and like one single

**[01:45:46]** you need to run and like one single round trip to the server that you need

**[01:45:47]** round trip to the server that you need

**[01:45:47]** round trip to the server that you need to do.

**[01:45:57]** I mean if you still need to do the

**[01:45:57]** I mean if you still need to do the retrieval like you you do the retrie

**[01:45:59]** retrieval like you you do the retrie

**[01:45:59]** retrieval like you you do the retrie like all the individual pieces are still


### [01:46:00 - 01:47:00]

**[01:46:01]** like all the individual pieces are still

**[01:46:01]** like all the individual pieces are still there. If you have two parts of the

**[01:46:02]** there. If you have two parts of the

**[01:46:02]** there. If you have two parts of the query, you will still retrieve those if

**[01:46:05]** query, you will still retrieve those if

**[01:46:05]** query, you will still retrieve those if that is the main cost and then you have

**[01:46:06]** that is the main cost and then you have

**[01:46:06]** that is the main cost and then you have the reranking. Um, so you're not getting

**[01:46:08]** the reranking. Um, so you're not getting

**[01:46:08]** the reranking. Um, so you're not getting out of those completely, but you can

**[01:46:10]** out of those completely, but you can

**[01:46:10]** out of those completely, but you can just do it in one single request that

**[01:46:12]** just do it in one single request that

**[01:46:12]** just do it in one single request that you send. We take care of all of that

**[01:46:14]** you send. We take care of all of that

**[01:46:14]** you send. We take care of all of that for you and then send you one result set

**[01:46:16]** for you and then send you one result set

**[01:46:16]** for you and then send you one result set back rather than sending more back to

**[01:46:17]** back rather than sending more back to

**[01:46:17]** back rather than sending more back to your application. So it

**[01:46:21]** your application. So it

**[01:46:21]** your application. So it it will potentially be a little less

**[01:46:22]** it will potentially be a little less

**[01:46:22]** it will potentially be a little less work on the elastic search, but it will

**[01:46:23]** work on the elastic search, but it will

**[01:46:24]** work on the elastic search, but it will mostly be less work on your application

**[01:46:25]** mostly be less work on your application

**[01:46:25]** mostly be less work on your application side.


### [01:47:00 - 01:48:00]

**[01:47:41]** Perfect. Thank you so much. I hope

**[01:47:41]** Perfect. Thank you so much. I hope everybody learned something. I will let

**[01:47:42]** everybody learned something. I will let

**[01:47:42]** everybody learned something. I will let the instance running for today or so so

**[01:47:45]** the instance running for today or so so

**[01:47:45]** the instance running for today or so so you can still play around with the

**[01:47:46]** you can still play around with the

**[01:47:46]** you can still play around with the queries if you feel like it. Uh thanks a

**[01:47:48]** queries if you feel like it. Uh thanks a

**[01:47:48]** queries if you feel like it. Uh thanks a lot for joining. If you want stickers,

**[01:47:50]** lot for joining. If you want stickers,

**[01:47:50]** lot for joining. If you want stickers, we have stickers up there. We also have

**[01:47:51]** we have stickers up there. We also have

**[01:47:51]** we have stickers up there. We also have a booth the next few days. come join and

**[01:47:54]** a booth the next few days. come join and

**[01:47:54]** a booth the next few days. come join and uh get some proper swag from us there.

**[01:47:56]** uh get some proper swag from us there.

**[01:47:56]** uh get some proper swag from us there. Um thank you. Uh see you around.


### [01:48:00 - 01:49:00]

**[01:48:00]** Um thank you. Uh see you around.

**[01:48:00]** Um thank you. Uh see you around. [Music]


