---
title: "You.com x LangChain"
author: "LangChain Accounts"
date: "2023-10-18"
url: "https://www.langchain.com/blog/you-com-x-langchain"
---

Case StudiesLangChain

# You.com x LangChain

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamOctober 18, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)4min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb118b02f04cb69c58d69_Screenshot-2023-10-17-at-9.38.23-AM.png)**Editor&#x27;s Note: the following is a guest blog post from our friends at You.com. We&#x27;ve seen a lot of interesting use cases around interacting with the internet, and we&#x27;re always looking for new tools to highlight to our community that can help do that. So when You.com mentioned they would releasing an API access to their search engine - the same one they use to power their **[**AI assistant**](https://about.you.com/category/ai-tools/youchat/?ref=blog.langchain.com)** - we jumped at the opportunity to help them highlight this.**

**This blog post walks through some results highlighting the efficacy of the You.com search API. These results are based off of the below notebook, so you can follow along there:**

- [**Notebook**](https://colab.research.google.com/github/You-OpenSource/You-API-Examples/blob/main/blogpost_final.ipynb?ref=blog.langchain.com)

### YouRetriever

We are excited to announce the release of YouRetriever, the easiest way to get access to the [You.com](http://you.com/?ref=blog.langchain.com) Search API. The [You.com](http://you.com/?ref=blog.langchain.com) Search API is designed by LLMs for LLMs with an emphasis on Retrieval Augmented Generation (RAG) applications. We evaluate our API on a number of datasets to benchmark performance of LLMs in the RAG-QA setting and use these benchmarks to guide the optimization of our search systems.

In this blog post we will compare and contrast the You.com Search API with the Google Search API as well as give the reader the tools to evaluate LLMs in the RAG-QA setting. We will evaluate our retriever performance on [Hotpot QA](https://github.com/hotpotqa/hotpot?ref=blog.langchain.com) using the `RetrievalQA` Chain. Hotpot is a dataset which is comprised of a question, answer, and context. The context can vary in relevance to the question/answer with a special &quot;distractor&quot; setting where the LLM needs to not be distracted by certain misleading text within the context. In this experiment we will be removing the context from the dataset and replacing it with text snippets which come back from the search APIs. In this sense the entire internet is the distractor text since the APIs are responsible for finding the answer to the question across the entire internet not just within the list of snippets supplied in the dataset. We call this the &quot;web distractor&quot; setting for evaluating search APIs with respect to their performance being used in conjunction with an LLM.

### Retrieval

The first thing you will notice about our text snippets is that we provide larger text snippets when we can and will soon have the option for specifying the amount of text you want returned from a single snippet to the entire page. Let&#x27;s ask it about the greatest pinball player ever, Keith Elwin.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb119b02f04cb69c58d81_Screenshot-2023-10-18-at-8.57.15-AM.png)

You can see that even with the default settings we return 27 text snippets about the great Keith and some of the documents contain a decent amount of text. This makes our search API especially powerful for LLMs operating in the RAG-QA setting.

However, these 27 text snippets can be a lot for a language model to work with. We can use the models with longer context windows as one workaround. There are a few options you can employ here if you don&#x27;t want to use a smaller context window model. The first is the cap the number of documents you feed from our API to the LLM. The other option is to use the [map_reduce chain](https://python.langchain.com/docs/modules/chains/document/map_reduce?ref=blog.langchain.com) type. The map_reduce chain type takes larger chunks of text and breaks them down to make them digestible by the LLM. This does mean that you will need to make multiple calls to the LLM which will mean slower run-time but you&#x27;ll be able to process all the data returned from the `YouRetriever`.

### Evaluation

In order to evaluate, we&#x27;ll use the HotPotQA dataset. We load this up from the [Huggingface dataset](https://huggingface.co/datasets/hotpot_qa?ref=blog.langchain.com) using the datasets library. We use the fullwiki setting here instead of the distractor but as we said before, we&#x27;ll be using our own context powered by the search APIs instead of what comes off the shelf.

Let&#x27;s take a sample from Hotpot QA and compare our search API with one of the current alternatives in LangChain, the `GoogleSearchAPIWrapper`. This isn&#x27;t a retriever in LangChain but it only takes a small amount of code to make an analog retriever. All we need to do is implement the `_get_relevant_documents` method of the abstract base class `BaseRetriever`. We should note here, that you could easily repeat this experiment and swap in another web search API like Bing. First let&#x27;s create a small utility for the existing wrapper.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb119b02f04cb69c58d89_Screenshot-2023-10-17-at-9.36.13-AM.png)

As you can see Google gives us much less information to feed into our LLM. While in both cases we requested results from 10 web results, the You.com Search API will attempt to give multiple text snippets per web result. To further demonstrate, we can now get predictions from the exact same LLM so we do our best to isolate the experiment to evaluating the search APIs.

Now we can use these two search methods and get predictions from the LLM using each search API&#x27;s results. It&#x27;s important to remember that at this point we have done everything we can to ensure the only thing we&#x27;re testing is the quality of search results for use by an LLM to answer these questions.

We use the F1 score function from the hotpot repository to ensure we are as close to the evaluation setting that was presented in the paper.

On the sample of data that we run over, we get the following results:

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb119b02f04cb69c58d84_Screenshot-2023-10-17-at-9.37.31-AM.png)

### In Conclusion

As you can see, the You.com Search API heavily out-performs Google on this small subset of data. Please stay tuned as You.com will be releasing a much larger search study in the weeks to come. If you would like to be an early access partner of ours please email [api@you.com](#) with your background, use case, and expected daily call volume.

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69efb41ab2584d1733d866c5_case-study-madrigal.png)Case Studies

#### How Madrigal Built a Flexible and Scalable Multi-Agent Research and Intelligence Platform for Pharma with LangChain and LangSmith

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69efba6c52ebbc1e377743b4_Parth.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69efba87c585b65247366c20_Ron.png)Parth PatelRon FilippoApril 29, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)11min[](/blog/customers-madrigal)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e251cee3c69c0b64e26c79_case-study-16_9%20(1).png)Case StudiesLangSmith

#### How Credit Genie used Insights Agent to improve their AI financial assistant

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e251111d491175462a384c_david-li.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e25199461e789ce4b875a7_jeffrey-ngai.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e2518d5b449e720f9f295a_goyo-lozano-palacio.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e2515f9f57e45d15dbd331_charles-yuan.png)David LiJeffrey NgaiGoyo Lozano PalacioCharles YuanApril 20, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)5min[](/blog/credit-genie-insights-agent-financial-assistant)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e122306b7173e8fad25030_81%20(1).png)LangChainPartner

#### A Developer’s First 10 Minutes: Secure LangChain Agents with Cisco AI Defense

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0e375654393ca0c125e00_siddhant-dash.png)Siddhant DashApril 16, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/secure-agents-cisco-ai-defense)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)