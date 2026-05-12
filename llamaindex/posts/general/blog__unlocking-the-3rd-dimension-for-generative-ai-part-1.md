---
title: "3D Generative AI for Engineers: Text-to-CAD Guide | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/unlocking-the-3rd-dimension-for-generative-ai-part-1"
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







It would be an understatement to say that generative AI has been taking the world by storm over the past couple of years. While text (1D) and image (2D) models are reaching a level of quality that is truly transforming the way we create digital content, the same cannot be said for 3D models.



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



3D generative AI has made significant strides in creating 3D digital assets, with techniques such as Neural Radiance Fields (NeRFs) showing promising results for applications such as video game development. However, the limitations of current generative AI technologies become apparent when it comes to applications beyond the digital realm, especially in the context of engineering and manufacturing. After spending more than 2 years actively engaged with the state-of-the-art tools for 3D generative AI, I personally have not been able to generate a single model that I would actually want to have manufactured into a physical object.

To put it simply: the current state of 3D generative AI is not very useful for engineers.

## The Motivation Behind neThing.xyz

Our mission at [polySpectra](https://polyspectra.com/) is to help engineers make their ideas real. The key insight that led to the invention of [neThing.xyz](http://nething.xyz/) (pronounced “anything dot x,y,z”) was that AI is actually quite good at writing code, and by training a “codegen” AI on domain specific languages for “code CAD”, our AI can produce code that can be rapidly converted into 3D CAD models.

For some quick context, AI code generation tools are now achieving ~95% evaluation benchmarks against human programmers. At the current pace, I wouldn’t be surprised if an AI hits 100% in the next three weeks. ([See this leaderboard](https://paperswithcode.com/sota/code-generation-on-humaneval) for more details.)

In 3D modeling, there is a growing buzz around “code CAD” — a term that signifies a paradigm shift in how we approach computer-aided design. Unlike traditional graphical CAD interfaces, which rely heavily on visual tools and manual user input, code CAD leverages programming to create and manipulate 3D models. This approach offers a more direct and potentially more powerful method for generating complex designs, as it allows for precision and automation that can be difficult to achieve with mouse-driven interfaces.

 A testament to the rising prominence of code CAD was its debut this month in the Too Tall Toby speed CAD competition. In the second match of the video below, [Jern](https://github.com/jdegenstein/) competes using the code CAD package [Build123d](https://build123d.readthedocs.io/en/latest/), against “Mr. Alex” who is using the traditional CAD tool SolidWorks.

*

[(Jump to 1:18 for competition-grade Code CAD!)](https://www.youtube.com/watch?v=-coWKJhwQbM&t=4666s)

So my idea was simple: if AI can code, and code can CAD, why can’t AI CAD?*

## Why RAG?

Trying to create a 3D generative AI with this code generation approach led us to confront a significant challenge: the need for incredibly long prompts to provide the AI with enough context about our code CAD domain-specific languages. This was essential for it to stand any chance of producing working code, let alone something useful.

I first studied Retrieval-Augmented Generation (RAG) under the tutelage of Mayo Oshin. ([Check out his RAG course!](https://maven.com/ai-chat-with-data/chatgpt-your-data)). I knew that RAG was going to be a necessary part of the strategy for making neThing.xyz “smarter”, and through Mayo’s course I had the opportunity to meet Jerry Liu and ask him some questions about the more nuanced elements of retrieval.

The initial version of neThing.xyz was ok, but I really had to wrangle the LLM: each query involved about 10,000 tokens. So if a user asks for “a box”, it is not 2 input tokens I’m paying for, it is 10,002 tokens. I knew I needed a more scalable approach…

## Enter the RAG-a-thon

The announcement of the “[RAG-a-thon](https://rag-a-thon.devpost.com/)” presented the perfect opportunity to quickly integrate RAG into neThing.xyz. For those familiar with the whirlwind nature of hackathons, you’ll understand when I say that time always seems to be in shorter supply than anticipated, often leading one to overestimate what can be accomplished. (For me, I usually overestimate what I can achieve by 3–10x!) With this in mind, I tried to set a modest goal for the weekend: add LlamaIndex to neThing.xyz.

My ultimate aim was to leverage LlamaIndex to dramatically expand the corpus of documentation available to neThing.xyz. But in the theme of setting a low bar, I started by just breaking down my very large system prompt into a set of documents that LlamaIndex could retrieve from AstraDB, bringing back only the most relevant example code for a given user’s query.

With significant assistance from Logan Markewich from the LlamaIndex team, I managed to implement RAG via LlamaIndex and AstraDB in a single day. This immediately reduced the average number of tokens per user query from about 10,000 to roughly 2,000. The impact of this was huge, resulting in an 80% cost reduction in our OpenAI bill in just one day — a change that was incredibly meaningful for us as a small business.

While I am personally passionate about the myriad ways in which RAG can make LLMs smarter, I want to emphasize the immediate ROI that RAG provided. By simply reorganizing the same set of information for retrieval through LlamaIndex, we achieved significant cost savings with minimal effort. As an entrepreneur, an 80% reduction in costs with just eight hours of work is a deal I’d take any day of the week.

On the final Sunday of the RAG-a-thon, I dedicated most of my time to ensuring that my demo would function correctly. The “demo gods” blessed me that day: I won first place in the “continuous innovation” track!

## Examples of neThing.xyz in Action:

Text:

Curves:

Threads:

Pipes:

Lattices:

## What’s Next?

My goal with neThing.xyz is to make the best 3D generative AI for engineers, with a focus on “text-to-CAD”. This is a really hard problem, and I shared some of these challenges with LlamaIndex in our recent webinar, and in more detail on [Wevolver](https://www.wevolver.com/article/teaching-ai-cad-is-hard).

Our key objectives are to make neThing.xyz faster, smarter, and cheaper. We are leveraging LlamaIndex to orchestrate the entire RAG pipeline, and we are really excited about the amazing pace of developments in this open source community.

*What would it take to get a part like this from a natural language prompt?*

Honestly, I don’t know how to do it.

We are just getting things off the ground and I would be tremendously excited to have you join our community. Our AI will only ever be as smart as the sum of the community that trained it, and we are excited to see what you will create!

Please give [neThing.xyz](https://nething.xyz/) a try today and share your honest feedback with us via our [new community forum](https://forum.nething.xyz/). Your input will play a crucial role in our ongoing development efforts, helping us to refine and improve the tool.

Make it real.

Raymond

P.S. — *This article is titled Part 1 for a reason. What do you want to see in Part 2? Tell me below!*