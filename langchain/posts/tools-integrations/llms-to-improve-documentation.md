---
title: "Analyzing User Interactions with LLMs to Improve our Documentation"
author: "LangChain Accounts"
date: "2023-07-13"
url: "https://www.langchain.com/blog/llms-to-improve-documentation"
---

Company AnnouncementsLangChain

# Analyzing User Interactions with LLMs to Improve our Documentation

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamJuly 13, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)3min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1feba9d0fc72378084c_photo-1450101499163-c8848c66ca85.jpeg)

### Introduction

We&#x27;re strongly committed to consistently enhancing our [documentation](https://python.langchain.com/docs/get_started/introduction.html?ref=blog.langchain.com) and its navigability. Using [Mendable](https://www.mendable.ai/?ref=blog.langchain.com), a AI-enabled chat application, users can search our documentation using keywords or questions. Over time, Mendable has collected a large dataset of questions that highlights areas for documentation improvement.

### Challenge

Distilling common themes from tens of thousands of questions per month is a significant challenge. Manual labeling can be effective, but is slow and laborious. [Statistical methods](https://en.wikipedia.org/wiki/Latent_Dirichlet_allocation?ref=blog.langchain.com) can analyze word distributions to infer common topics, but may not capture the semantic richness and context of the questions.

### Proposal

LLMs can help us [summarize](https://www.youtube.com/watch?v=qaPMdcCqtWk&amp;ref=blog.langchain.com)  and identify documentation gaps from the questions collected by [Mendable](https://www.mendable.ai/?ref=blog.langchain.com). We experimented with two methods to pass large question datasets to an LLM: 1) Group similar questions via clustering before summarizing each group and 2) Apply a map-reduce approach that splits questions into small segments, summarizes each, and then combines them into a final synthesis.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1ffba9d0fc723780858_summary.png)Approaches for summarizing large datasets of user questions

There are tradeoffs between the approaches, which we wanted to examine:

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1ffba9d0fc723780854_tradeoffs.png)Trade-offs between clustering and map-reduce

### Results

We tested an end-to-end LLM summarization pipeline that uses [LangChain’s map-reduce chain](https://python.langchain.com/docs/modules/chains/popular/summarize?ref=blog.langchain.com) to split questions into groups based on the context window of either [GPT-3.5-16k](https://openai.com/blog/function-calling-and-other-api-updates?ref=blog.langchain.com) (16k tokens) or [Claude-2](https://www.anthropic.com/index/claude-2?ref=blog.langchain.com) (100k tokens), summarize each (map), and then distill the group summaries into a final synthesis (reduce).

We also tested [k-Means clustering](https://en.wikipedia.org/wiki/K-means_clustering?ref=blog.langchain.com) of embedded questions followed by [GPT-4](https://openai.com/research/gpt-4?ref=blog.langchain.com) to summarize each cluster, an approach [similar to what OpenAI](https://github.com/openai/openai-cookbook/blob/main/examples/Clustering.ipynb?ref=blog.langchain.com) reported in one of their cookbooks. For consistency, we use the same input dataset as map-reduce.

We open sourced the notebooks and the data (see repo [here](https://github.com/mendableai/QA_clustering?ref=blog.langchain.com)) so that this analysis can be reproduced. [Here](https://docs.google.com/spreadsheets/d/1z-LakOhgP7Oskf29Q3nmud0e6fQqjraSAmFrvI_5UGM/edit?usp=sharing&amp;ref=blog.langchain.com) is a sheet with detailed results, which we summarize in the table below; we asked both methods to summarize the major question themes being asked by users with a proportion of questions that fall into each bucket:

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1ffba9d0fc72378085d_table-1.png)Distribution of question themes summarized in different experiments

Specific themes can be interrogated using alternative summarization prompts; for example, using map-reduce was can ask the reduce stage to return top questions on a specific theme (e.g., data processing). For example, using this reduce prompt:

`The following is a list of summaries for questions entered into a Q+A system:
{question_summaries}

Take these and distill it into a final, consolidated list with:
(1) the top 10 question related to loading, processing, and manipulating different types of data and documents.
(2) estimate the proportion of each question
`

We get granular thematic breakdown of the Top 10 Questions Related to Loading, Processing, and Manipulating Different Types of Data and Documents:

`1. &quot;How can I load a PDF file and split it into chunks using langchain?&quot; - 15%`
2. &quot;How do I load and process a CSV file using Langchain?&quot; - 12%
3. &quot;How do I use the &#x27;readfiletool&#x27; to load a text file?&quot; - 11%
4. &quot;How do I use Langchain to summarize a PDF document using the LLM model?&quot; - 10%
5. &quot;What are the different data loaders available in Langchain, and how do I choose the right one for my use case?&quot; - 9%
6. &quot;How do I load and process multiple PDFs?&quot; - 9%
7. &quot;How do I load all documents in a folder?&quot; - 8%
8. &quot;How do I split a string into a list of words in Python?&quot; - 8%
9. &quot;How do I load and process HTML content using BeautifulSoup?&quot; - 8%
10. &quot;How can I add metadata to the Pinecone upsert?&quot; - 10%
`

To get better diagnostic analysis of the cost, we use soon-to-launch LangChain tooling to compare diagnostics (token usage, etc) for the approaches. For example, we quantify token usage, which shows that map-reduce indeed has higher cost:

- ~500k tokens
- ~80k tokens (~8k / cluster with 10 clusters)

### Summary

As expected, there are trade-offs between the approaches. Map-Reduce provides high customizability because questions can be split into arbitrarily granular groups and summarized with tunable map-reduce prompts. However, the cost may be considerably higher as noted by token usage. Clustering risks information loss due to hand-tuning (e.g., of the cluster number) in the preprocessing stage, but it offers lower cost and may be a sensible way to quickly compressive very large datasets prior to more granular (and high cost) LLM summarization. The thoughtful union of these two methods offers considerable promise for addressing this challenge.

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