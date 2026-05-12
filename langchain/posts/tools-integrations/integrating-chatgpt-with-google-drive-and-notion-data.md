---
title: "Tavrn x LangChain: Integrating Noah: ChatGPT with Google Drive and Notion data"
author: "LangChain Accounts"
date: "2023-08-23"
url: "https://www.langchain.com/blog/integrating-chatgpt-with-google-drive-and-notion-data"
---

PartnerLangSmithOpen Source

# Tavrn x LangChain: Integrating Noah: ChatGPT with Google Drive and Notion data

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamAugust 23, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)3min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cf9af9e94af49e84c6276a_5-social--8-.webp)*Editor&#x27;s Note: This post was written in collaboration with the *[*Tavrn*](https://tavrn.art/?ref=producthunt)* team. They were able to build a new personal assistant app, *[*Noah*](https://www.producthunt.com/posts/noah?ref=blog.langchain.com)*, that&#x27;s highly personalized and highly context-aware using LangChain (with some interesting retrieval tactics) and LangSmith (for fine-tuning chains and prompts). *

ChatGPT is already an indispensable tool for many in the workplace. Its impressive general purpose performance makes it extremely versatile to assist in workflows ranging from creative brainstorming to coding. In order to get the best outputs from ChatGPT, users are familiar with the process of prompting - providing the chat with as much context and instructions as possible so the output is satisfactory.

The POV of this laborious user experience usually involves multiple rounds of copy/pasting of parts of multiple documents that contain relevant information to the prompt. Given that ChatGPT has no context whatsoever on the user or his work, the output quality highly depends on information the user provides.  For instance, if a user wants ChatGPT&#x27;s best help to prioritize which product features to build first, he will have to:

1. Find and open all documents that could potentially have useful context to ChatGPT (e.g. product meeting notes, user feedback reports, information about the product itself)

2. Read through each document, copy the relevant parts and paste on ChatGPT

3. Hope it all fits the character limit of ChatGPT and that he did not forget to include any important context

This inefficient, manual process of always having to supply the best context to ChatGPT prevents users from utilizing it for more complex use cases like the one illustrated above. We built Noah to resolve the context fetching problem and allow users to experience an AI copilot that always efficiently retrieves the best possible context to answer user queries.  

Simplicity and user-friendliness are core to Noah. We take care of all the heavy-lifting in the background. In just a few clicks, users can sync hundreds of files from their own Google Drive and Notion and start getting help from Noah.

Powered by LangChain, Noah unlocks a more powerful and relevant use of LLMs in the workplace: a personal AI assistant that provides help specifically to users and their work. In the product prioritization example above, Noah would take care of all three steps (finding relevant documents, selecting the most relevant parts in each document, adding each part to the LLM prompt) so the user&#x27;s sole input to the chat can be &quot;which product features should I prioritize?&quot;

To get started on Noah, users select the tools from which they would like to sync files.

After the tool is selected, users can either choose specific files or quickly select their 200 most recent files from Google Drive or Notion.

Once users select their files, Noah processes the documents using optimized, context-aware document loaders in addition to state-of-the-art embeddings models. We tried multiple forms of semantic chunking but LangChain&#x27;s CharacterTextSplitter with around 2,400 characters per chunk outperformed all the others for all types of documents - spreadsheets, documents, PDFs, slides.

Then, once a user asks a question, Noah fetches the most relevant content across multiple sources utilizing cosine similarity vector search and passes them to multi-chain LLM calls where the best possible answer is obtained. We also tried other forms of retrieval but cosine similarity substantially outperformed the others.

Langsmith was extra useful to us when fine-tuning which chains and prompts to use for the final user answer. Among the learnings, the optimal memory &quot;k&quot; parameter for ConversationBufferWindowMemory is 1 otherwise the answers get unreliable with so much historical context. Additionally, after the chunks are retrieved, we pass them into an intermediary, GPT-4 powered chain to filter out any conflicting information, *prioritizing more recent sources.  *

Finally, Noah provides the answer, with the appropriate sources cited.

To get started with Noah and boost your productivity, access [https://tavrn.art/noah](https://tavrn.art/noah?ref=blog.langchain.com).

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