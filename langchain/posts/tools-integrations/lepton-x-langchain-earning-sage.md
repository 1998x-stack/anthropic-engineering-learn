---
title: "Lepton x LangChain: Earning Sage, How to Transform AI into a Savvy CFO"
author: "LangChain Accounts"
date: "2023-07-24"
url: "https://www.langchain.com/blog/lepton-x-langchain-earning-sage"
---

Agent ArchitecturePartner

# Lepton x LangChain: Earning Sage, How to Transform AI into a Savvy CFO

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamJuly 24, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)5min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1f03c7fbd0a6275d9be_5-social--9.png)***Editor’s Note: This blog post was written in collaboration LeptonAI Team, an early ***[***LangSmith***](https://www.langchain.com/langsmith?ref=blog.langchain.com)*** BETA user. Lots of folks are talking about how best to finetune an open-source model for their specific use case, and LeptonAI has actually done that. We&#x27;re excited to share their journey and hope it can inform others.***

# Introduction

Have you ever thought about joining an earning call and asking questions to these CFOs? That used to be the privilege held by the investors from high-end investment banks such as JP Morgan, Goldman Sachs and Morgan Stanley.

Yet with the capability of LLM and proper techniques around it, not anymore.  And if you don’t feel like reading the whole post, feel free to try out a demo [here](https://earningsage.lepton.run/?ref=blog.langchain.com). This demo is created based on the [Apple Q2 2023 earning call](https://github.com/bobmayuze/Earning-Sage/blob/main/earning_reports/AAPL-89728-full.tsv?ref=blog.langchain.com).

Step into the realm where cutting-edge technology meets financial acumen, let’s dive deep into the transformative process of harnessing the capability of AI, and unveil the secrets to crafting an AI that speaks like a seasoned Chief Financial Officer (CFO), as demonstrated below.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1f03c7fbd0a6275d9c4_image.png)

# Problem Statement

To begin with, I would like to breakdown the challenge mentioned above into an abstraction, which hopefully can help you understand at an engineering level on what problem we are facing. In a nutshell, the problem looks like this:

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1f03c7fbd0a6275d9c8_image-1.png)

The problem we are facing here is to `organically` combine the original earning call transcript,  the text generation model ( mostly could be OpenAI ChatGPT 3.5) and the toolset(python, langchain, chroma, nothing fancy here) to mimic a CFO.

# Thought Through Process for solutions

## Starting with openAI

To begin with, I started with using ChatGPT 3.5 from open AI with [Langchain retrievalQA chain](https://python.langchain.com/docs/use_cases/question_answering/?ref=blog.langchain.com#quickstart), which is a pretty standard approach for anyone building out an application like this. With that being said, the solution now looks like this:

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1f03c7fbd0a6275d9d1_image-2.png)

Not surprisingly, ChatGPT 3.5 works quite well for questions simply enough, eg. `What&#x27;s covered in this earning call?`  . The open source tools works like a charm in terms of prototyping. It doesn’t take long to build up the first version of the product. Yet for questions bit more complicated, ChatGPT gives up very quick. You may check it out [here](https://smith.langchain.com/projects/p/4341d1f7-ac1b-416e-9400-20f89f393a5b/r/f721812f-f541-46c2-b80c-6b8ca51fa4ec?ref=blog.langchain.com) .

The full questions list with response from ChatGPT 3.5 is here

- [What&#x27;s covered in this earning call?](https://smith.langchain.com/public/dbac4723-5a7d-4c63-914d-90f651c2ad22/r?ref=blog.langchain.com)
- [What is the potential for further growth in the number of Apple devices per iPhone user?](https://smith.langchain.com/public/ecc37b09-8528-49be-b694-5f4d73258c80/r?ref=blog.langchain.com)
- [What is the Apple’s strategy over AI?](https://smith.langchain.com/public/e3d0b2da-b1cc-4e38-963c-d4607dc7278f/r?ref=blog.langchain.com)
- [What are the feedbacks on Apply Pay Later?](https://smith.langchain.com/public/a62fb0ac-91f4-4581-91f5-5266a5871d3a/r?ref=blog.langchain.com)

## Then I tried vanilla vicuna

Overheard from friends, and as an Open Source Developer ( worked on Jupyter Lab, yes, the notebook, but beyond notebook! 😅), I decided to try out Vicuna, an open-source chatbot trained by fine-tuning LLaMA on user-shared conversations collected from ShareGPT. With that being said, the solution now looks like this:

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1f03c7fbd0a6275d9ce_image-3.png)

The tricky part here is the first version of the product is built upon Langchain which is initially built upon OpenAI’s API. So as a lot of other prompt engineering frameworks. In this case, switching to another model is a lot of work in terms of compatibility issues. Eg. the other model may doesn’t have the same embedding api endpoint. or the tiktoken lib doesn’t support certain models.

Due to this problem, engineering team at [Lepton.AI](https://www.lepton.ai/?ref=blog.langchain.com) found a way to make the model compatible with the original OpenAI’s API endpoint, makes switching models for a LLM application much easier. The model service enable users to switch the model by simply altering the environment from

`OPENAI_API_BASE=https://api.openai.com/v1
OPENAI_API_KEY=YOUR_OPEN_API_KEY
`

to

`OPENAI_API_BASE=YOUR_DEPLOYMENT_URL
OPENAI_API_KEY=YOUR_LEPTON_AI_API_KEY
`

The result turns to be pretty solid at first glance, yet evaluation on the outputs is quite challenging. This is where [LangSmith](https://www.langchain.com/langsmith?ref=blog.langchain.com) comes in handy. It allows me to add four lines of code to alter the environment variables, and it could handle everything for me from there.

## Turns out the Fine Tuned model is even better

Even though the vanilla model works by not giving up so fast, it still doesn’t really talk quite like a CFO. That is saying the way it talks does not give me the feeling of actually attending an earning call surrounded by talents from top financial institutions.

Hence inspired by Vicuna, the fine-tuned model of llama, I decided to fine-tune a model that utilize data from the earning call question &amp; answer section. By collecting data from the earning transcripts, I managed to sample out quite a few earning calls. Then using TUNA, a model augmentation service that augment both the data and model, to create a model that’s more focused on earning call context. With that being said, the solution now looks like this:

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1f03c7fbd0a6275d9d4_image-4.png)

Here are few query result from the question list

- [What&#x27;s covered in this earning call?](https://smith.langchain.com/public/80e7f6b6-8ea7-41b9-b875-55781b1c1df8/r?ref=blog.langchain.com)
- [What is the potential for further growth in the number of Apple devices per iPhone user?](https://smith.langchain.com/public/7f14895a-d6e5-45b9-98bf-bc128954de45/r?ref=blog.langchain.com)
- [What is the Apple’s strategy over AI?](https://smith.langchain.com/public/a2a6d24b-fd46-46f4-9850-b414f0b716f0/r?ref=blog.langchain.com)
- [What are the feedbacks on Apply Pay Later?](https://smith.langchain.com/public/34555f2f-79a6-4532-bb0e-09727100c2a8/r?ref=blog.langchain.com)

Again, the only thing changed in my code is the `OPENAI_API_BASE` and everything works from there. By leveraging LangSmith, I get to compare the result more efficiently and share them to people who are interested in looking at it as demonstrated in this post multiple times.

# Conclusion

In conclusion, the integration of data and LLM techniques, such as data augmentation and fine-tuning, stands as a pivotal milestone in the development of AI applications. By combining vast and diverse datasets with the power of LLM, we unlock unprecedented potential, enabling AI systems to generate more accurate, context-aware, and coherent outputs. The synergy between data and LLM not only enhances the overall performance of AI applications but also opens up new avenues for innovation and discovery.

As we continue to refine and expand our understanding of this dynamic relationship, we embark upon a journey where the fusion of data-driven insights and advanced language models redefines what is possible, propelling us into an era of AI excellence and transforming the way we interact with technology. The future awaits, as we stride confidently toward a horizon where AI transcends expectations and becomes an indispensable asset in our quest for progress.

And for the tools mentioned above, both LangSmith and LeptonAI are still under closed beta, but feel free to sign up on the waitlist and give it a try. Feel free to shoot me an email at [uz@lepton.ai](mailto:uz@lepton.ai), I would love to hear from you on your thoughts!

# Related Links

- [LangSmith - A unified platform for debugging, testing, evaluating, and monitoring your LLM applications](https://smith.langchain.com/?ref=blog.langchain.com)
- [Lepton.AI - Build AI The Simple Way](http://lepton.ai/?ref=blog.langchain.com)
- [The code for this post - Feel free to use it](https://github.com/bobmayuze/Earning-Sage/tree/main?ref=blog.langchain.com)

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