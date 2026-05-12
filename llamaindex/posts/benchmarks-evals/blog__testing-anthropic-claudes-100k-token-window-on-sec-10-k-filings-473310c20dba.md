---
title: "Testing Anthropic Claude’s 100k-token window on SEC 10-K Filings"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/testing-anthropic-claudes-100k-token-window-on-sec-10-k-filings-473310c20dba"
category: "benchmarks-evals"
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







Anthropic’s [100K Context Window](https://www.anthropic.com/index/100k-context-windows) expansion, just released yesterday, has taken the AI community by storm. A 100k token limit is approximately 75k words (~3x GPT4–32k’s context window, ~25x that of GPT-3.5/ChatGPT); this means that you can now fit 300 pages of text in a *single *inference call*.*



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



One of the core use cases highlighted in the Anthropic blog is [analyzing an SEC 10-K filing](https://vimeo.com/825669443); the model is capable of ingesting the entire report, and producing answers to different questions.

Coincidentally, we [published a tutorial](https://medium.com/@jerryjliu98/how-unstructured-and-llamaindex-can-help-bring-the-power-of-llms-to-your-own-data-3657d063e30d) a few months ago showing how LlamaIndex + Unstructured + GPT3 could help you perform different queries over UBER SEC 10-k filings. LlamaIndex provides a comprehensive toolkit to help manage external data on top of any LLM with limited context windows, and we show that we can execute a diverse range of queries, from questions over a single document to comparing sections across documents.

How well does Anthropic’s 100k model do over UBER SEC 10-k filings? Moreover, how well does it do *without *the help of any of LlamaIndex’s more advanced data structures? In this blog we show the performance of Anthropic’s model on different queries, using the simplest data structure available: the list index.

# High-Level Findings

Where Anthropic’s 100k model does well:

- **Holistic understanding of the data (kind of, after some prompt tuning): **Anthropic’s model does demonstrate an impressive capability to synthesize insights across the entire context window to answer the question at hand (assuming we set `response_mode="tree_summarize"` , see below). It can miss details though; see below!
- **Latency: **This one was surprising to us. Anthropic’s model is able to crunch an entire UBER 10-k filing in ~60–90 seconds, which seems long but is much faster than repeated API calls to GPT-3 (which when added up can take minutes).

Where Anthropic’s 100k model doesn’t do well:

- **Cost: **This one is obvious. Every query we ran processed hundreds of thousands of tokens. At [$11 per million tokens for Claude-v1](https://console.anthropic.com/account/pricing), this equates to $1 per query, which can quickly add up.
- **Reasoning over more complicated prompts: **Anthropic’s model demonstrated a surprising lack of ability to understand our refine prompt for [“create-and-refine” response synthesis](https://gpt-index.readthedocs.io/en/latest/how_to/query/response_synthesis.html#refine), returning incorrect/irrelevant results. We ended up switching to [“tree summarization” instead](https://gpt-index.readthedocs.io/en/latest/how_to/query/response_synthesis.html#tree-summarize). See below for results.

# Overview of Methodology

We want to test the capabilities of Anthropic’s 100K model on top of UBER 10-k filings from 2019–2022. We also want to do this while using as little retrieval/synthesis constructs as possible. This means no embeddings, and no fancy retrieval mechanisms.

Ideally, we can directly insert an entire 10-k filing (or even all four 10-k filings) into the prompt. However, we found that a single UBER 10-k filing actually consists of ~**160k tokens, which is greater than the 100k context window. **This means that we still have to chunk up each filing!

We end up using our [list index data structure ](https://gpt-index.readthedocs.io/en/latest/guides/primer/index_guide.html#querying)— we split each text up into massive ~100k token chunks, and use our **response synthesis strategies** to synthesize an answer across multiple chunks.

![](/blog/images/1*tTrOruM4jPOIJh5YkDtOVA.png)

We run some queries over each filing as well as over multiple filings, similar to our original blog post. We report the results below.

# Tutorial Setup

Our data ingestion is the same as the LlamaIndex + Unstructured blog post. We use Unstructured’s HTML parser to parse the HTML DOM into nicely formatted text. We then create a Document object for each SEC filing.

You can access Unstructured data loaders on [LlamaHub](https://llamahub.ai/l/file-unstructured).

from llama_index import download_loader
from pathlib import Path

UnstructuredReader = download_loader("UnstructuredReader", refresh_cache=True)

loader = UnstructuredReader()
doc_set = {}
all_docs = []
years = [2022, 2021, 2020, 2019]
for year in years:
    year_doc = loader.load_data(file=Path(f'./data/UBER/UBER_{year}.html'), split_documents=False)[0]
    # insert year metadata into each year
    year_doc.extra_info = {"year": year}
    doc_set[year] = year_doc
    all_docs.append(year_doc)Next, we want to setup the Anthropic LLM. We’re using claude-v1 by default. We also want to manually define the new 100k-token input size within our `PromptHelper` object; this will help us figure out how to “compact” context into the input prompt space during response synthesis.

We set the `max_input_size` to 100k and the output length to 2048. We also set the context chunk size to a high value (95k, leaving some buffer room for rest of the prompt). Context will only be chunked if the number of tokens exceeds this limit.

from llama_index import PromptHelper, LLMPredictor, ServiceContext
from langchain.llms import Anthropic

# define prompt helper
# set maximum input size
max_input_size = 100000
# set number of output tokens
num_output = 2048
# set maximum chunk overlap
max_chunk_overlap = 20
prompt_helper = PromptHelper(max_input_size, num_output, max_chunk_overlap)

llm_predictor = LLMPredictor(llm=Anthropic(model="claude-v1.3-100k", temperature=0, max_tokens_to_sample=num_output))
service_context = ServiceContext.from_defaults(
    llm_predictor=llm_predictor, prompt_helper=prompt_helper,
    chunk_size_limit=95000
)

# Analyzing a Single Document

Let’s first analyze queries over a single document. We build a list index over the 2019 UBER 10-K:

list_index = GPTListIndex.from_documents([doc_set[2019]], service_context=service_context)
print(len(list_index.index_struct.nodes))As mentioned, the 10-K exceeds the 100k token limit, and so there are two nodes within the list index.

We then ask a query: “What were some of the biggest risk factors in 2019?”

Recall that there are two approaches within LlamaIndex for response synthesis across multiple nodes (where the total context exceeds the context window): a “create-and-refine” strategy, and a “tree summarize” strategy.

- **Create-and-Refine: **sequentially go through each retrieved `Node`. Use a Question-Answer Prompt for the first Node, and use a Refine Prompt for subsequent Nodes. Make a separate LLM call per Node.
- **Tree Summarize: **Given a set of `Node` objects and the query, recursively construct a tree using the Question Answer Prompt and return the root node as the response. Good for summarization purposes.

Claude-v1 100K does not do well with the “create-and-refine” strategy (which is the default).

# NOTE: the default create/refine approach does not give good answers
query = "What were some of the biggest risk factors in 2019?"
query_engine = list_index.as_query_engine(service_context=service_context)
response = query_engine.query(query)Here is the retrieved answer:

Original answer:

Some of the biggest risk factors for Uber in 2019 included:

• Regulatory challenges and uncertainty. Uber faced regulatory challenges and uncertainty in many markets, including restrictions on its products and services, caps on pricing, and licensing requirements. For example, California's AB5 law and other similar laws increased the risk of Drivers being classified as employees. Uber also faced regulatory scrutiny and bans in London, Barcelona, and other markets.

• Competition. The markets in which Uber operates are highly competitive, and Uber faced significant competition from well-established and low-cost alternatives in 2019. Competitors also aggressively competed for Drivers and consumers by offering significant incentives and discounts.

• Safety and security. There were risks related to the safety and security of Uber's platform, including risks from vehicle or scooter accidents, assaults, and other incidents. Uber released a safety report in 2019 detailing reports of sexual assaults on its platform which brought additional scrutiny.

• Financial performance and profitability. Uber continued to experience significant losses in 2019 as it invested in growth. There was no guarantee that Uber would achieve or sustain profitability in the future.

• Reliance on third parties. Uber relied on third parties for key elements of its business like cloud computing services, payment processing, and background checks. If these third parties failed to provide services or increased costs, it could adversely impact Uber's business.

• Macroeconomic conditions. Uber's business was sensitive to economic conditions and changes that impacted discretionary consumer spending. A decline in the economy could reduce demand for Uber's products and services.

• Reliance on Drivers and Restaurants. Uber's success depended on attracting and retaining enough Drivers and Restaurants to its platform. If Uber was unable to attract or retain enough Drivers and Restaurants, it could negatively impact its operations.

• Intellectual property. If Uber was unable to protect its intellectual property, or if third parties claimed Uber was infringing on their intellectual property, it could harm Uber's business. Uber relied on a combination of copyright, trademark, patent, and trade secret laws to establish its intellectual property rights.

Refined answer:

Some of the biggest risk factors for Uber in 2019 included:

• Regulatory challenges and uncertainty. Uber faced significant regulatory challenges in 2019, including AB5 in California which increased the risk of Drivers being classified as employees and regulatory scrutiny and temporary bans in London and other markets. These regulatory issues created uncertainty and posed risks to Uber's business model and financial results.

• Competition. The ridesharing and meal delivery markets are highly competitive, and competitors offered significant incentives and discounts to take market share from Uber in 2019. This competition could negatively impact Uber's growth and profitability.

• Safety and security. There were risks related to the safety and security of Uber's platform, including risks from vehicle or scooter accidents, assaults, and other incidents. Uber's safety report detailing sexual assault reports brought additional scrutiny and risks. Any failure to ensure safety could significantly damage Uber's reputation and business.

• Financial performance and profitability. Uber continued to experience substantial losses in 2019 due to investments in growth, and there was no guarantee of future profitability. Uber's path to profitability was uncertain, and failure to become profitable could threaten its business model and access to capital.

• Reliance on third parties. Uber relied on third parties for services like cloud computing, payment processing, and background checks. If these third parties failed to provide services or increased costs, it could negatively impact Uber's offerings, growth, and profitability.

• Macroeconomic conditions. Uber's business was sensitive to the economy and consumer discretionary spending. An economic downturn could reduce demand for Uber's offerings and threaten its growth and financial performance.

• Reliance on Drivers and Restaurants. Uber's success depended on attracting and retaining enough Drivers and Restaurants to support growth and meet consumer demand. Failure to attract or retain Drivers and Restaurants could significantly impact Uber's business.

• Intellectual property. Failure to protect intellectual property or infringement of others' intellectual property could damage Uber's competitive position and business. Uber relied on laws and policies to protect intellectual property, but monitoring infringement and unauthorized use was difficult.As shown, the answer contains the prompt within it; the point of the refine prompt was to produce just the refined answer, not produce both the original and refined answers.

For some reason, using the Tree Summarize strategy works much better.

# NOTE: tree_summarize gives better answers
query = "What were some of the biggest risk factors in 2019?"
query_engine = list_index.as_query_engine(service_context=service_context, response_mode="tree_summarize")
response = query_engine.query(query)Returned response:

• Regulatory challenges and uncertainty: Uber faced significant regulatory challenges and uncertainty in 2019, including AB5 in California which codified a new test for determining whether workers should be classified as employees or independent contractors. Uber also faced regulatory scrutiny and bans in other markets like London, UK. These regulatory issues created uncertainty and risk around Uber's business model and operations.

• Safety and security: Uber received negative publicity around safety incidents on its platform which could damage its brand and reputation. Uber released a safety report in 2019 on sexual assaults and other incidents which led to additional scrutiny. Safety and security risks remain an ongoing issue for Uber's business.

• Competition: The markets in which Uber competes are intensely competitive, and Uber faces competition from new and existing companies in the various segments it operates in like ridesharing, food delivery, and logistics. Increased competition could make it difficult for Uber to attract and retain platform users.

• Financial losses: Uber continued to experience significant losses from operations in 2019 as it invested in growth. Uber may not achieve or sustain profitability in the future which could negatively impact its business and stock price.

• Reliance on third-parties: Uber relies on third-party data centers, cloud computing services, and software which exposes it to risks if these third-parties experience any disruptions or interference. Any disruption of third-party services could negatively impact Uber's business.

• Macroeconomic conditions: Uber's business is sensitive to macroeconomic conditions, and any downturn could reduce discretionary consumer spending which would harm Uber's business. Issues like a recession, increased unemployment, or reduced consumer confidence could all potentially impact Uber's business.

• Reliance on Drivers and Restaurants: Uber's business depends on attracting and retaining Drivers and Restaurants to its platform. If Uber is unable to attract or maintain a critical mass of Drivers and Restaurants, its platform will become less appealing to platform users and its financial results would be adversely impacted.The answer is much better. It goes into details about the US-China trade war, slowing economic growth, Brexit, and more (keep in mind 2019 is pre-COVID).

## Token Usage and Latency

The document contains around ~170K tokens. For some reason, this number is not reflected on the Anthropic usage logs (the “Prompt Tokens” section seems capped at 10240). But the Prompt Length (in characters) is logged, as well as the model latency.

Given the pricing, ~170K tokens would be equivalent to $1.5–2 USD.

A query through one Uber SEC-10K takes around **150** **seconds**, including all LLM calls. This is actually a bit faster than repeated calls to ChatGPT/davinci. Each ChatGPT/davinci call (with the 4K token window maximized), empirically can take 6–10 seconds to complete → **125–250 seconds (**or more).

![](/blog/images/1*ESJ-8RYNzbjxaGeOzIGg8Q.png)

# Analyzing Multiple Documents

A popular example in our [previous blog post](https://medium.com/@jerryjliu98/how-unstructured-and-llamaindex-can-help-bring-the-power-of-llms-to-your-own-data-3657d063e30d) was showcasing that you could compare/contrast different documents with LlamaIndex graph structures.

We test whether we can do that here as well, by feeding in multiple SEC reports into Claude-v1 100k.

**Caveat: **Considering that one UBER SEC-10K filing doesn’t even fit in the context window, we’ll of course also need to implement response synthesis strategies in order to handle ingesting multiple 10K filings.

We build a list index over all 4 10K filings: 2019, 2020, 2021, and 2022.

list_index = GPTListIndex.from_documents(all_docs, service_context=service_context)
print(len(list_index.index_struct.nodes))We then ask our question using our Tree Summarize response mode.

query = "How are the risk factors changing across years? Compare/contrast the risk factors across the SEC filings."
query_engine = list_index.as_query_engine(response_mode="tree_summarize")
response = query_engine.query(query)The full answer is given below:

The risk factors disclosed in Uber's SEC filings have evolved over time based on Uber's business and industry changes. Some of the key differences in risk factors across the filings are:

2017 10-K:
- Focused heavily on risks related to negative publicity, competition, dependence on independent contractors, and regulatory challenges as Uber was still facing backlash from various PR crises and regulatory pushback.
- Also highlighted risks from intellectual property litigation given various IP disputes at the time.

2018 10-K:
- Added more risks related to autonomous vehicles as Uber ramped up its self-driving car efforts. Specifically called out risks from accidents, technical challenges, and competition in the AV space.
- Removed some risks related to negative publicity and PR crises as those issues had subsided. But added risks related to corporate culture and workplace environment given the Fowler scandal.

2019 10-K:
- Further expanded AV risks to include risks from partnerships and third party relationships as Uber relied more on partnerships with other companies like Toyota and Volvo.
- Added risks related to environmental regulations and climate change as those issues received more mainstream attention.
- Removed risks related to initial scaling challenges as Uber had matured as a company. But added risks related to growth into new offerings and markets as Uber expanded into freight shipping, scooters, etc.

In summary, Uber's risk factors have evolved to reflect the key issues and challenges facing the company at any point in time. The risks highlight both external factors like regulations as well as internal factors related to Uber's business, technology, and operations. The changes over time show how an innovative company's risks can shift quite quickly.

Some of the key trends in how the risk factors are changing include:

1. Risks related to negative publicity and PR crises decreased over time as those issues subsided, while risks related to other issues like AV technology, workplace culture, and new initiatives increased. This shows how Uber's risks evolved as the company matured.

2. Risks tend to increase in areas where Uber is actively investing or expanding into. For example, risks related to AVs, partnerships, and new mobility offerings increased as Uber ramped up efforts in those areas. This highlights how risk profiles change with a company's strategic priorities.

3. External risks like regulations and climate change were added as those issues gained more mainstream attention and importance. This shows how companies have to adapt their risk factors to account for changes in the overall business environment.

4. Certain foundational risks around competition, growth, and reliance on independent contractors persisted over time. But the specifics and details provided for those risks evolved based on Uber's current challenges and priorities. So while the themes remained, the risks were actively updated.

In summary, Uber's risk factors changed over time to provide more details on the company's priorities, challenges, partnerships, and external environment at any given point. But certain core risks inherent to Uber's business model have also remained consistently highlighted, demonstrating how those foundational risks are long-term in nature. The changes in risks over time provide a glimpse into how an innovative company's risk profile is constantly evolving.This response only contains risk refactor analysis over the 2019 10-K (which in turn contains risk refactors for 2017 and 2018). It does not contain the years from 2020 onwards. Part of this is potentially due to our tree summarize response synthesis strategy. Nevertheless, it shows that trying to naively “stuff” documents into big 100K token chunks with simple response synthesis strategies still does not produce the optimal answers.

## **Token Usage and Latency**

As expected, feeding all four documents into Anthropic necessitates many more chained LLM calls, which consumes way more tokens and takes a lot longer (on the order of 9–10 minutes).

![](/blog/images/1*grzQLc07RE9hP6zRiK2mNg.png)

# Conclusion

In general, the new 100K context window is incredibly exciting and offers developers a new mode of feeding in data into the LLM for different tasks/queries. It offers coherent analysis with a marginal token cost that is much cheaper than that of GPT-4.

That said, trying to maximize this context window with each inference call does come with tradeoffs in terms of latency and cost.

We look forward to doing more experiments/comparisons/thought pieces on top of Claude! Let us know your feedback.

## Resources

You can check out our [full Colab notebook here](https://colab.research.google.com/drive/1uuqvPI2_WNFMd7g-ahFoioSHV7ExB2GR?usp=sharing).