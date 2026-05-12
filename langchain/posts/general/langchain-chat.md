---
title: "LangChain Chat"
author: "LangChain Accounts"
date: "2023-01-16"
url: "https://www.langchain.com/blog/langchain-chat"
---

Company AnnouncementsLangChain

# LangChain Chat

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamJanuary 16, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)7min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb273a83bd2fbf570e724_chatbanner.png)Today we’re excited to announce and showcase an open source chatbot specifically geared toward answering questions about LangChain’s documentation.

**Key Links**

- Deployed Chatbot:** **[chat.langchain.dev](https://chat.langchain.dev/?ref=blog.langchain.com)
- Deployed Chatbot on HuggingFace spaces: [huggingface.co/spaces/hwchase17/chat-langchain](https://huggingface.co/spaces/hwchase17/chat-langchain?ref=blog.langchain.com)
- Open source repo: [github.com/hwchase17/chat-langchain](https://github.com/hwchase17/chat-langchain?ref=blog.langchain.com)
- Next.js frontend: [github.com/zahidkhawaja/langchain-chat-nextjs](https://github.com/zahidkhawaja/langchain-chat-nextjs?ref=blog.langchain.com)

Huge shoutout to [Zahid Khawaja](https://twitter.com/chillzaza_?ref=blog.langchain.com) for collaborating with us on this. If you want this type of functionality for webpages in general, you should check out his browser extension: [Lucid](https://twitter.com/chillzaza_/status/1593739682013220865?s=20&amp;ref=blog.langchain.com).

If you like this and want a more advanced version of this for your codebase, you should check out [ClerkieAI](https://twitter.com/ClerkieAI?ref=blog.langchain.com). Their question answer bot is live on our [Discord](https://discord.gg/6adMQxSpJS?ref=blog.langchain.com).

## Overview

There have been a few other projects similar to this one in the past weeks (more on that below). However, we hope to share what we believe are unique insights, including:

- Document ingestion (what is and isn’t general)
- **How to make this work in a chatbot setting (important UX)**
- (Prompt Engineering) Tradeoff between speed and performance
- (Prompt Engineering) How to get it to cite sources
- (Prompt Engineering) Output format

Expanding on the bolded section, we believe the chatbot interface is an important UX (just see the success of ChatGPT!) and we think that is missing from other implementations.

## Motivation

Combining LLMs with external data has always been one of the core value props of LangChain. One of the first demo’s we ever made was a [Notion QA Bot](https://github.com/hwchase17/notion-qa?ref=blog.langchain.com), and [Lucid](https://twitter.com/chillzaza_/status/1594847151238037505?s=20&amp;ref=blog.langchain.com) quickly followed as a way to do this over the internet.

One of the pieces of external data we wanted to enable question-answering over was our [documentation](https://python.langchain.com/docs/get_started/introduction.html?ref=blog.langchain.com). We have a [growing Discord community](https://discord.gg/6adMQxSpJS?ref=blog.langchain.com), and want to provide fast and accurate support for all their questions. So this seemed like a perfect opportunity to utilize our own technology internally! We reached out to [Zahid](https://twitter.com/chillzaza_?ref=blog.langchain.com), an ML creator and LangChain enthusiast, to see if he would be willing to team up for this, and to our relief he said yes! And so we started building.

## Similar Work

For whatever reason, there was a lot of similar work done here in just the past week! Pretty much all of them followed the same pipeline, which can be condensed as follows:

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb267adb40d0919239e3b_ingest-1.png)Diagram of typical ingestion process

**Ingestion**:

- Take a set of proprietary documents
- Split them up into smaller chunks
- Create an embedding for each document

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb274a83bd2fbf570e759_screen-shot-2023-01-16-at-10.18.42-pm.png)Diagram of typical query process

**Query**:

- Create an embedding for the query
- Find the most similar documents in the embedding space
- Pass those documents, along with the original query, into a language model to generate an answer

**Some good other examples of this include**:

- [GitHub support bot (by Dagster)](https://dagster.io/blog/chatgpt-langchain?ref=blog.langchain.com) - probably the most similar to this in terms of the problem it’s trying to solve
- [Dr. Doc Search](https://github.com/namuan/dr-doc-search?ref=blog.langchain.com) - converse with a book (PDF)
- [Simon Willison on “Semantic Search Answers”](https://simonwillison.net/2023/Jan/13/semantic-search-answers/?ref=blog.langchain.com) - a good explanation of the some of the topics here
- [Ask My Book](https://askmybook.com/?ref=blog.langchain.com) - by Sahil Lavingia, maybe the example that kicked off this current craze

## Document Ingestion

We immediately faced a question: where exactly to get the data from. There were two options: the files in GitHub, or scraping from the internet. While some of the files in GitHub were in a nice format to work with (markdown and rst) we also had some less good for working with (.ipynb files, auto generated docs). For that reason we decided to go with scraping it from the internet.

After that, we faced a question of how to preprocess the html files. For this we initially did this in a generic way (just using Beautiful Soup to get all the text on the page). However, after using these results we found that some of the sidebar contents were creating bad results. As a visual example, in the picture below the two areas in red don’t really provide much new information.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb274a83bd2fbf570e763_rx-zmwshiju6ncmhij9jm7kzqpdbw9kpgmyttvsyhfa3pm1wvpnk3jmrt-1rwq079xvrlvor6gfcvlsswy96wspdnztfkkfam2kpiqvysn4rqc0a6q3wwhr5psz6z9cykldkeoazdllsiy9houk9je_uepqckmapzjrye4dz5m1dnswjkhu-zncw_9jjgg.png)A screenshot of the problematic sidebar contents.

When we inspected some of the bad results we were getting, we saw that often it was these pieces of information that were getting pulled and stuffed into the context. We fixed this by changing the parser to explicitly ignore those areas.

Although specific to this layout, we do believe this highlights the importance of being very intentional about what data you do (or do not) include as potential context. **While it may be easy to take a generic ingestion tool and use that as a way to get quickly started, doing deeper inspection and modifying your pipeline will probably be necessary to get better performance**.

## How to make this work in a chatbot setting

As mentioned before, we believe a chatbot setting is an important UX decision that:

- People find familiar (see the success of ChatGPT)
- Enable other key features (more on this below)

One of the key features that we wanted to make sure to include that we did not see being done a lot of other places is the ability to ask follow up questions. We believe this is [very important](https://twitter.com/johnvmcdonnell/status/1611860858497531905?s=20&amp;t=ThUtsd5V4xpSJPEC_4Kceg&amp;ref=blog.langchain.com) for any chat based interface. Most (all?) implementations out there primarily ignore this issue, and treat each question as independent. This breaks down when someone wants to ask a follow up question in a natural way, or refer to pieces of context in the prior questions or answers.

The primary way to do this in LangChain is with [memory](https://python.langchain.com/docs/modules/memory/?ref=blog.langchain.com) in a conversation chain. In the simplest implementation of this, the previous lines of conversation are added as context to the prompt. However, this breaks down a bit for our use case, as not only do we care about adding the conversational history to the prompt, but we also care about using it to determine which documents to fetch. If asking a follow up question, we need to know what that follow up question is about in order to fetch relevant documents.

**Therefore, we created a new chain that had the following steps:**

- Given a conversation history and a new question, create a single, standalone question
- Use that question in a normal [Vector Database Question Answer Chain](https://python.langchain.com/docs/modules/chains/popular/vector_db_qa?ref=blog.langchain.com).

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb267adb40d0919239e31_query.png)Diagram of our query process

We were a bit worried that using that question in the Vector Database Question Answer Chain would be lossy and lose some of the context, but we did not really observe any negative effects there.

In the process of getting to this solution, we tried a few other things with respect to fetching documents from the Vector Database that did not work nearly as well:

- Embedding the chat history + question together: once the chat history got long, would massively overly index on that if you were trying to change topics.
- Embedding the chat and question separately and then combining results: better than the above, but still pulled too much information about previous topics into context

## Prompt Engineering

When building a chatbot, delivering a good user experience is crucial. In our use case, there were a few important considerations:

- Each answer should include an official source to the [documentation](https://python.langchain.com/docs/get_started/introduction?ref=blog.langchain.com).
- If the answer includes code, it should be properly formatted as a code block.
- The chatbot should stay on topic and be upfront about not knowing an answer.

We were able to achieve all of this with the following [prompt](https://github.com/hwchase17/chat-langchain/blob/master/chain.py?ref=blog.langchain.com):

`You are an AI assistant for the open source library LangChain. The documentation is located at https://langchain.readthedocs.io.
You are given the following extracted parts of a long document and a question. Provide a conversational answer with a hyperlink to the documentation.
You should only use hyperlinks that are explicitly listed as a source in the context. Do NOT make up a hyperlink that is not listed.
If the question includes a request for code, provide a code block directly from the documentation.
If you don&#x27;t know the answer, just say &quot;Hmm, I&#x27;m not sure.&quot; Don&#x27;t try to make up an answer.
If the question is not about LangChain, politely inform them that you are tuned to only answer questions about LangChain.
Question: {question}
=========
{context}
=========
Answer in Markdown:`

This is prompt we&#x27;re currently using to return answers in Markdown with sources and code.

In this prompt, we’re requesting a response in **Markdown** format. This allows us to render the answer in a visually appealing format with proper headings, lists, links, and code blocks.

**Here’s how it looks on our Next.js frontend:**

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb274a83bd2fbf570e769_goodcodeexample.png)In this screenshot, the user requests a follow-up code example. As you can see, we’re able to provide a code example in a sensible format.

The hyperlink in each answer is constructed using the base URL to the documentation, which we’re providing upfront in our prompt. Since we scraped the documentation website in our data ingestion pipeline, we’re able to identify the path to the answer and combine it with the base URL to create a working link.

To keep the chatbot as accurate as possible, we keep the temperature at **0** and include instructions in the prompt to say “*Hmm, I’m not sure.*” if given a question with an unclear answer. To keep the conversation on topic, we also include instructions to decline questions that are not about LangChain.

**Striking a balance between speed and performance:**

- We began our testing with longer Markdown answers. Although the answer quality was great, the response times were slightly longer than desired.
- We spent a lot of time refining the prompt and experimenting with different keywords and sentence structures to improve performance.
- One method was to mention the *Markdown* keyword at the end of the prompt. For our use case, we were able to return formatted outputs with only a single mention of the keyword.
- Providing the base URL near the beginning of the prompt improved overall performance - it gives the model a working reference to create a final URL to include in the answer.
- We found that using the singular form, such as &quot;a hyperlink&quot; instead of &quot;hyperlinks&quot; and &quot;a code block&quot; instead of &quot;code blocks&quot;, improves response times.

## Future Work

We&#x27;re just getting started and we welcome feedback from the LangChain community. We can&#x27;t wait to introduce new features and improvements in the near future! Follow us on [Twitter](https://twitter.com/LangChainAI?ref=blog.langchain.com) for updates and checkout the [code](https://github.com/hwchase17/chat-langchain/blob/master/chain.py?ref=blog.langchain.com).

If you like this and want a more advanced version of this for your codebase, you should check out [ClerkieAI](https://twitter.com/ClerkieAI?ref=blog.langchain.com). Their question answer bot is live on our [Discord](https://discord.gg/6adMQxSpJS?ref=blog.langchain.com).

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef82f01e90bfdf3e83a25e_Blog-02.png)Company Announcements

#### Interrupt Preview: Meet the MC

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Becca WengApril 28, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/interrupt-preview-meet-the-mc)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef66604a47f5049293bcf6_april-newsletter-blog.png)Company Announcements

#### April 2026: LangChain Newsletter

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/april-2026-langchain-newsletter)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e122306b7173e8fad25030_81%20(1).png)LangChainPartner

#### A Developer’s First 10 Minutes: Secure LangChain Agents with Cisco AI Defense

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0e375654393ca0c125e00_siddhant-dash.png)Siddhant DashApril 16, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/secure-agents-cisco-ai-defense)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)