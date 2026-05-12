---
title: "ChatGPT Knowledge Cutoff: What Builders Should Do | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/chatgpts-knowledge-is-two-year-s-old-what-to-do-if-you-re-building-applications-72ceacde135c"
category: "general"
---

Follow us on


 -  [


](https://github.com/run-llama/)
 -  [

](https://discord.com/invite/eN6D2HQ4aX)
 -  [


](https://twitter.com/llama_index)
 -  [


](https://www.linkedin.com/company/91154103/)
 -  [


](https://www.youtube.com/@LlamaIndex)







It’s official: as of today, ChatGPT’s knowledge cutoff is 2 years old.

>

Happy 2nd birthday to ChatGPT&#39;s knowledge cutoff! 🎂 [pic.twitter.com/O1cgRPSP3l](https://t.co/O1cgRPSP3l)

&mdash; Yi Ding -- prod/acc (@yi_ding) [September 1, 2023](https://twitter.com/yi_ding/status/1697589370222711081?ref_src=twsrc%5Etfw)



# Why doesn’t OpenAI just update it?

There are some fundamental reasons for this: training new LLMs is an expensive — at least tens of millions of dollars — and not guaranteed process. Cleaning new data sets for training is also expensive.



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



# What should I do if I’m building an application that needs more recent data?

You may be tempted to just send ChatGPT the entire wikipedia pages for 2022 and 2023: [https://en.wikipedia.org/wiki/2022](https://en.wikipedia.org/wiki/2022) You’ll soon run into two limits: 1. there is a limit on the number of words you can send to a large language model (LLM). This is called the “context window.” 2. LLM APIs charge you by the word, so the more you send it, the more expensive your API calls become.

The standard technique is one called “Retrieval Augmented Generation” or RAG. What it is, boiled down very simply, is a process of searching for the right context, giving that context to the LLM, and then getting better results back.

>

What’s Retrieval Augmented Generation? Search, Give, Get.

For those of us coming from a traditional software development background RAG can sound intimidating, but it really is a simple concept:

Search for the relevant data
Give the data to GPT
Get a better response

Of course,…

&mdash; Yi Ding -- prod/acc (@yi_ding) [July 28, 2023](https://twitter.com/yi_ding/status/1684765549929332736?ref_src=twsrc%5Etfw)



At [LlamaIndex](https://llamaindex.ai) we are the RAG experts, but there is a whole community of open source projects that are tackling this problem. We have integrated with over 20 open source vector databases and there are other open source tools like LangChain, Semantic Kernel, DSPy, Axilla and others (put your favorites in the comments!) that are attacking the problem in different ways.

Another technique is called fine tuning. Here, you essentially create a new custom model on top of an existing LLM. While LlamaIndex does support fine tuning, it often requires much more work and data:

>

We are big fans of fine tuning and custom models but knowing when to use RAG and when to use fine tuning, and how to use them in combination, is essential.

Watch this space! [https://t.co/vTpWauhj3C](https://t.co/vTpWauhj3C)

&mdash; LlamaIndex 🦙 (@llama_index) [August 18, 2023](https://twitter.com/llama_index/status/1692570383201812710?ref_src=twsrc%5Etfw)



# What if I don’t need more recent data?

That’s totally OK! Not every application needs data that’s more recent than 2021. Before LlamaIndex, I worked on an open source reading education tool, and phonics have definitely not changed in the last two years. If you’re building something to write bedtime stories (❤️ Kidgeni [https://kidgeni.com/](https://kidgeni.com/)) or raps (check out TextFX! [https://textfx.withgoogle.com/](https://textfx.withgoogle.com/)) your application

# What if I just want to use ChatGPT with more recent information?

There are a lot of chatbots that use Retrieval Augmented Generation currently. A few of the ones I’ve personally tried are Metaphor [https://metaphor.systems/](https://metaphor.systems/), Perplexity [https://www.perplexity.ai/](https://www.perplexity.ai/) and Medisearch [https://medisearch.io/](https://medisearch.io/), and of course Google Bard and BingGPT.