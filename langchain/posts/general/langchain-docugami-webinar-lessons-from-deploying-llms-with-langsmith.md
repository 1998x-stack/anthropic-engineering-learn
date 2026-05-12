---
title: "LangChain + Docugami Webinar: Lessons from Deploying LLMs with LangSmith"
author: "LangChain Accounts"
date: "2023-09-20"
url: "https://www.langchain.com/blog/langchain-docugami-webinar-lessons-from-deploying-llms-with-langsmith"
---

PartnerLangSmith

# LangChain + Docugami Webinar: Lessons from Deploying LLMs with LangSmith

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamSeptember 20, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)3min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb165a2e6df4d389b0085_5-social--28-.png)*Editor&#x27;s Note: This post was written in collaboration with the *[*Docugami*](https://www.docugami.com/?ref=blog.langchain.com)* team. We recently did a webinar with them and *[*Rechat*](https://rechat.com/ai/?ref=blog.langchain.com)* to talk about what it actually requires to get an LLM application into production. You can find the recording of the webinar *[*here*](https://www.youtube.com/watch?v=ll-Xit_Khq0&amp;ref=blog.langchain.com)*–and this post provides a helpful overview of what they discussed and dives even deeper on their learnings. *

At Docugami we have been using, training or fine-tuning language models for multiple years in our mission to transform documents to data. We initially started using smaller models for text completion and OCR correction, as well as pretraining for sequence labeling tasks. As these models have exploded in size and complexity, we have continued to invest in this space with question answering and Retrieval Augmented Generation (RAG) using our unique approach with the Document XML Knowledge Graph.

We chose from the beginning to host the language models in our cloud to ensure customer data confidentiality.

We started using LangChain very early, impressed with the expressive API and vibrant community. The LangChain[ Docugami Loader](https://python.langchain.com/docs/integrations/document_loaders/docugami?ref=blog.langchain.com) was added in May, and we continue to be amazed by the responsiveness of the LangChain team as they incorporate community feedback and continue to grow the LangChain framework.

Yesterday, we were super happy to share our learnings with the community in an [educational webinar](https://www.youtube.com/watch?v=ll-Xit_Khq0&amp;ref=blog.langchain.com) hosted by LangChain. Our goal was to share some of the real-world challenges we have encountered with LLMs in production and how we are using LangChain, and especially the new[ LangSmith (beta)](https://www.langchain.com/langsmith?ref=blog.langchain.com) tool, in our LLMOps flow.

If you missed the webinar, no problem! Here is a summary of the key points we covered:

1.       ***Real documents are more than flat text:*** We described in detail how Docugami structurally chunks documents (Scanned PDF, Digital PDF, DOCX, DOC) and stitches together the complex reading orders including tables and multi-column flows. We discussed how humans create documents to be readable by other humans, including visual and structural cues that contain semantic meaning which is often missed by text-only systems.

2.       ***Documents are Knowledge Graphs: ***We briefly showed some examples of the hierarchical Document XML Knowledge Graph produced by Docugami. It contains deep hierarchies, custom semantic labels on nodes and all the complex relationships that can be expressed semantically using the XML Data Model. We showed through code how RAG using Docugami’s XML Knowledge Graph leads to more accurate results that cannot be achieved with simple linear chunking.

3.       ***Building Complex Chains with the LangChain Expression Language:*** Real-world chains can get complicated with parallel branches, output parsers, few shot examples, conditional sub-chains, and more. We walked through a quick example with SQL generation, with agent-like fixup for invalid SQL. We discussed how you can step through these complex chains in the LangSmith tool, and shared some example traces.

4.       ***Debugging Complex Chain Failures in Production: ***Things go wrong for various reasons when LLMs are deployed in production. It could be something as simple as a context length overflow, or something more subtle like an output parser throwing exceptions in some edge cases. We shared some tips to make your run traces in LangSmith more debuggable.

5.       ***Docugami’s end to end LLM Ops with LangChain + LangSmith:*** Finally, we summarized our overall flow to deploy models, monitor them under real customer use, identify problematic runs, and then fix up these runs (manually as well as with help from other LLMs offline). This is a nascent area, where we are excited to work with LangSmith to improve the tooling given our previous experience running similar model ops for other (non-LLM) machine learning models.

The slides (including links to code samples and LangSmith traces) are [here](https://rebrand.ly/docugami_langsmith?ref=blog.langchain.com).

You can also watch the webinar here.

We are excited to see what you build with LangChain and Docugami. Tag us @docugami on twitter to share your results and experience, or just reach out[ https://www.docugami.com/contact-us](https://www.docugami.com/contact-us?ref=blog.langchain.com)

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc07193192cebc73980fd3_logo%20and%20title%20-%2020%20characters%20max%20(6).png)PartnerDeep Agents

#### Building a company due diligence agent with Deep Agents, LangSmith and Parallel

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01c6959ca5fd924ab432_MattHarris.jpg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01b812793b72539057d5_nick%20headshot.jpeg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd2d50cd0f84dacf92e7b_ProfilePic.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd29baf4c28709e2566a7_headshot.jpg)Matt HarrisNick MartitschSrimanth TangedipalliKaran SinghMay 8, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)9min[](/blog/building-a-company-due-diligence-agent-with-deep-agents-langsmith-and-parallel)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef96ff74c638e982ff68c6_86%20(1).png)Agent ArchitectureLangSmithOpen Source

#### How LangSmith and LangChain OSS Help You Meet EU AI Act Requirements

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0003a1af368dfae13c23c_jacob-talbot.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Jacob TalbotBecca WengApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/langsmith-langchain-oss-eu-ai-act)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e251cee3c69c0b64e26c79_case-study-16_9%20(1).png)Case StudiesLangSmith

#### How Credit Genie used Insights Agent to improve their AI financial assistant

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e251111d491175462a384c_david-li.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e25199461e789ce4b875a7_jeffrey-ngai.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e2518d5b449e720f9f295a_goyo-lozano-palacio.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e2515f9f57e45d15dbd331_charles-yuan.png)David LiJeffrey NgaiGoyo Lozano PalacioCharles YuanApril 20, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)5min[](/blog/credit-genie-insights-agent-financial-assistant)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)