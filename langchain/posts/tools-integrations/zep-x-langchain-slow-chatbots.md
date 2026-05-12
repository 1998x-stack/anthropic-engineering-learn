---
title: "Zep x LangChain: Diagnosing and Fixing Slow Chatbots"
author: "LangChain Accounts"
date: "2023-07-26"
url: "https://www.langchain.com/blog/zep-x-langchain-slow-chatbots"
---

Agent ArchitecturePartner

# Zep x LangChain: Diagnosing and Fixing Slow Chatbots

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamJuly 26, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)6min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1e503935dbc92e083c1_5-social--5.png)***Editor’s Note: This blog post was written in collaboration with ***[***Zep***](https://www.getzep.com/?ref=blog.langchain.com)***, an early ***[***LangSmith***](https://www.langchain.com/langsmith?ref=blog.langchain.com)*** BETA user. We&#x27;ve fielded a lot of questions about the latency of LangChain applications - where it comes from, how to improve. This is a FANTASTIC walkthrough of how LangSmith allows you to easily diagnose the causes of latency in your app, and how different components of the LangChain ecosystem (in this case, Zep) can be used to improve it.***

## Summary

Poor chatbot response times can result in frustrated users and customer churn. LangChain’s new LangSmith service makes it simple and easy to understand what’s causing latency in an LLM app. In this article, we use LangSmith to diagnose a poorly performing LangChain app and demonstrate how we improved performance by an order of magnitude using the [Zep](https://www.getzep.com/?ref=blog.langchain.com) memory store.

**Source code for this article: https://github.com/getzep/zep-by-example/tree/main/langchain/python/langsmith-latency**

If you’ve ever waited several seconds for a web page to load and decided to click elsewhere, you’re not alone. Much has been written about the effect of slow websites and their [impact on user engagement and conversion rates](https://www.thinkwithgoogle.com/consumer-insights/consumer-trends/mobile-site-load-time-statistics/?ref=blog.langchain.com). Chatbot response times are no different. While responding too quickly may [shove the user into an uncanny valley](https://www.researchgate.net/publication/324949980_Faster_Is_Not_Always_Better_Understanding_the_Effect_of_Dynamic_Response_Delays_in_Human-Chatbot_Interaction?ref=blog.langchain.com), responding slowly is problematic, too. Users will become [frustrated and less likely to use your service again](https://link.springer.com/article/10.1007/s12599-022-00755-x?ref=blog.langchain.com). They may also view the [chatbot as unfair and be unwilling to share personal information](https://pubsonline.informs.org/doi/10.1287/isre.2021.1015?ref=blog.langchain.com).

Unfortunately, it&#x27;s pretty easy to build a slow chatbot. Between multiple chains, high LLM latency, and enriching prompts with chat histories, summaries, and results from vector databases, a lot can impact how fast your bot responds.

Instrumenting and profiling your application can be challenging and very time-consuming. LangChain’s new [LangSmith service](https://blog.langchain.com/announcing-langsmith/) does this fantastically and without any need to manually instrument your app. In this article, I will walk you through an example chatbot application that while simple, is not dissimilar to one you might be building.

## My Chatbot is sooo slow

I’ve built a Chatbot app using LangChain, and my users are unhappy and churning.

The users would like to carry on a conversation with the bot and have it not forget the context and details of prior messages in a conversation. So, when building the bot, I used a LangChain memory class. I’m also using a Retriever, backed by Chroma’s vector database, to recall relevant messages from the distant past. In the future, I might also use a Retriever to ground my app with business documents. Like many Langchain developers, I’ve used OpenAI’s APIs for LLM completion and document embeddings.

Using the memory instance and retriever, my chain will inject the chat history into the prompt sent to the LLM. LLM context windows are limited, and large prompts cost more and take longer for an LLM to respond to. I, therefore, don’t want to send the entire chat history to the LLM. Instead, I’d like to limit this to the most recent messages and have my chain summarize messages in the more distant past. The prompt will look something like this:

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1e703935dbc92e083ee_5j_ac7k8ivgn4lzwteuaq-dw5hsqozsm6-ggu1vsd6f01lzbcdmglszz_jlj3xfiwmyuxmskunwdwvhy3y72cbxj7xyf7kdtbvcgxcwqftlg-eapfn39fr_aizd3vajzqwewm-winlkaj6q1q6rz-ly.png)To make the above happen, I’m using LangChain’s ConversationSummaryBufferMemory and VectorStoreRetrieverMemory classes.

## LangSmith to the rescue

As mentioned, my chat app is too slow, and my users are churning. I really want to get to the bottom of why this is happening. In the past, I’d have to instrument the app in many different places to capture the timings of various operations, a time-consuming and tricky undertaking. Luckily, the LangChain team has already instrumented the LangChain codebase for us, and LangSmith makes it simple to understand the performance of your app. All I have to do is configure my LangSmith API key and add several descriptive tags to my code.

For my investigation, I put together a simple test suite using 30 messages, 20 of which are preloaded into the LangChain memory class and 10 of which I use in the experiment itself. Each run of the experiment passes these 10 messages to the chain. I do this five times so that I can understand experimental variance.

The results in LangSmith are below. Each run of 10 messages has a unique name and is the parent to several chain runs.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1e703935dbc92e083e2_xqj9ehnyopewvq0gs_rzaezmhl9xnuv2gwt5dmmpymw2kexpaod0urd3osfs6qccq56oq0fhlo7spo3iwroz3vs5gsbez390klehgj64o4twkltlnh1mx6dvizbmsycmu304nyz-4rkkh0nbuatnlaw.png)

Latency is clearly visible in the LangSmith UI with poor latency marked in red. I can easily drill down into each run of the experiment to better understand why this is occurring. All experiment runs are slow, with a mean of over 7-13s to respond to each message. One of the runs is a significant outlier.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1e703935dbc92e083f9_qjbb8t_xlcsu3nxvtdrejtmgy_imgcg5jh6evxplx4uadke_uoue4qrk9ykcernzdoabuuwo3h0xwcsfzh-vrvlguco_18s1ns8d6fsgjhyr8m6ty9ueqgk8u7d4zt5sfenrmkjelcjccd7ouoa2v3s.png)

Drilling into that chain, I see a poor response time from the OpenAI API, taking over 5 minutes to respond to the request. It’s possible that the initial request failed and there were retries. Unfortunately, the OpenAI API can sometimes see rate-limiting and high variance in latency.

Let’s put aside the outlier and work to understand why each message turn of our chatbot is slow. I noticed that the majority of the time my chain spends responding to my users is the result of the ConversationSummaryBufferMemory’s summarization chain. For an arbitrarily selected response turn, summarization takes almost 6s of the 7s total response time. And this occurs every single time our chatbot runs. That’s not good.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1e703935dbc92e083f1_h6vqgn6llg_2v3wz33sf6zhsd9qc-6ldelu-q5wcdxkezufesw5hn6hhxv7vgloqpobxnxydtwkmt5lbouloqw5ipgxscnh8grexkcyykaed7m4zwt5qa70knozsbqiyxjudi0tkpk1evb4atseboyy.png)

## Using Zep as an alternative memory service

[Zep is an open source long-term memory store](https://docs.getzep.com/?ref=blog.langchain.com) that persists, summarizes, embeds, indexes, and enriches LLM app / chatbot histories. Importantly, Zep is fast. Summarization, embedding, and message enrichment all happen asynchronously, outside of the chat loop. It also supports stateless app architectures as chat histories are not held in memory, unlike ConversationSummaryBufferMemory and many other LangChain memory classes.

Zep’s ZepMemory and ZepRetriever classes are shipped in the LangChain codebase for Python and JS and are drop-in replacements for LangChain’s native classes. Rerunning the experiment with Zep is super simple. I installed the Zep server using Zep’s docker-compose setup and modified my code.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1e703935dbc92e083e5_swgcqmt6vubpvnsht4cxgg04x_tlszardhetksmhykf39u1tp8fqcdjgqvs-6nbe-lyewfauyvlcpoy0ftxllq20xgdr4tzz7pv9tjh5jtcl8uwnpqjwewcg-j0apteumnnczs_mezapkffi-ismgvu.png)

I also don’t need to use a separate vector database for semantically retrieving historical chat memories. Zep automatically embeds and indexes messages.

The results in LangSmith are below. The total chain runtime for each experiment run is down to ~16 seconds, almost entirely explained by OpenAI API latency. Zep generates summaries in the background, which are automatically added by the ZepMemory instance to my prompt alongside the most recent chat history.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1e703935dbc92e083f6_zxodv4ltg4nku2afxgyihi2xtwngmvr4wrcnmu6afa2ghvl18vuf6vhsaznurupu7lqofth0ttnjc4zpntxkvuu-hrhogoaplvzzmnlbo7z-rcm5kgy_8f-tbew4hv0ogiqdktmbdnayda-81_19sni.png)

There’s an outlier chain run: OpenAI’s API spikey latency strikes again!

Let’s take a more quantitative look at the data. First comparing the distribution of run times, p95 and p99 for each experiment. There were 5 experiments, and we ran them for both chains using the ConversationSummaryBufferMemory and ZepMemory. The chart below uses a log scale for latency. As we saw above, Zep’s runtimes were an order of magnitude lower.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1e603935dbc92e083da_iw3ur79ba5tt96idpk827k2v9wvflqg_wphplbb025joadd4qjk9s2sv5q_upbqc5urotayx4iev0f_qlcmiidh4lp_3th1e2lnzssxjag4fdxeiisx9sm78rlelswjgg8tjddynszp3vffewyoh0-y.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1e603935dbc92e083dd_screenshot-2023-07-24-at-8.03.08-am.png)

For good measure, I also analyzed the impact of the VectorStoreRetrieverMemory on the app’s response time below.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1e703935dbc92e083e8_2ob69ctdslgbmyd1ls8ddn9f8fmg9kaioplhrjrbewt1arb-zopqgy9ojuctnhopu15mhcc0nn3n7mgklz-vvhx2ikc5vl7d6tkgf-pdflwoqfdpzownsrhasldjr9aegqmbyjtku3odakaf84hdcu4.png)

While certainly not as problematic as the ConversationSummaryBufferMemory, the VectorStoreRetrieverMemory and OpenAI for embeddings were still far slower than using the ZepRetriever. Zep can be configured to use a SentenceTransformer embedding model running in the Zep service, which [offers far lower latency than calling out to the OpenAI embedding service](https://www.getzep.com/text-embedding-latency-a-semi-scientific-look/?ref=blog.langchain.com).

##
Summing it all up

I’ve demonstrated how to diagnose LangChain chatbot app latency issues using the new LangSmith service. The culprit here was the ConversationSummaryBufferMemory implementation, which I easily swapped out with Zep, seeing a magnitude-level improvement in latency. LangSmith is a great platform for more than just diagnosing latency issues, with tools for testing and evaluating the correctness of chains and more.

## Experimental Setup

I ran all tests on my Apple M1 Pro 14” 16GB RAM. For the Zep results, I ran the standard Zep v0.8.1 docker-compose setup with Docker configured for 4GB RAM and 4 cores.

The LLM used for all tests was OpenAI’s gpt-3.5-turbo and for embeddings, I used the OpenAI text-embedding-ada-002 model. For software, I used LangChain 0.0.239, ChromaDB 0.4.2, and Python 3.11.

All tests were run 5 times consecutively. All runs started with a new vector DB collection or index created from historical conversations. There was a short cooling-off period between runs.

## Next Steps

- [Sign up](https://smith.langchain.com/?ref=blog.langchain.com) for the LangSmith beta
- Get setup with Zep using the [Quick Start Guide](https://docs.getzep.com/deployment/quickstart/?ref=blog.langchain.com)

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc07193192cebc73980fd3_logo%20and%20title%20-%2020%20characters%20max%20(6).png)PartnerDeep Agents

#### Building a company due diligence agent with Deep Agents, LangSmith and Parallel

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01c6959ca5fd924ab432_MattHarris.jpg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01b812793b72539057d5_nick%20headshot.jpeg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd2d50cd0f84dacf92e7b_ProfilePic.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd29baf4c28709e2566a7_headshot.jpg)Matt HarrisNick MartitschSrimanth TangedipalliKaran SinghMay 8, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)9min[](/blog/building-a-company-due-diligence-agent-with-deep-agents-langsmith-and-parallel)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69f20536df00c0eb15eab1d3_blue-77%20characters%20max.png)Deep AgentsAgent ArchitectureOpen Source

#### Tuning Deep Agents to Work Well with Different Models

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcefac505b6b48827abf84_vivek-trivedy.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcf032ce65a32e276a4d0a_mason-daugherty.png)Vivek TrivedyMason DaughertyApril 29, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)5min[](/blog/tuning-deep-agents-different-models)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef96ff74c638e982ff68c6_86%20(1).png)Agent ArchitectureLangSmithOpen Source

#### How LangSmith and LangChain OSS Help You Meet EU AI Act Requirements

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0003a1af368dfae13c23c_jacob-talbot.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Jacob TalbotBecca WengApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/langsmith-langchain-oss-eu-ai-act)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)