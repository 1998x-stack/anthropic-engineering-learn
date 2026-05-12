---
title: "LlamaIndex + Metaphor Integration: How-To Guide | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/llamaindex-metaphor-towards-automating-knowledge-work-with-llms-5520a32efa2f"
category: "llamaindex-core"
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







(co-authored by Jerry Liu, CEO of LlamaIndex, Jeffrey Wang, co-founder at Metaphor, and Adam Hoffman, Software Engineer at Hypotenuse Labs)



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



We’re incredibly excited to launch an [integration](https://llamahub.ai/l/tools-metaphor) between LlamaIndex and [Metaphor](https://platform.metaphor.systems/): combine the capabilities of LlamaIndex data agents with Metaphor as a *native *LLM search tool to enable knowledge workers capable of answering any question over any data, no matter how recent or complex.

We provide a deeper overview of Metaphor and the LlamaIndex integration below. We also walk through our [example notebook](https://github.com/emptycrown/llama-hub/blob/main/llama_hub/tools/notebooks/metaphor.ipynb) to showcase how they can be combined.

# Background/Context

State-of-the art large language models (LLMs) such as ChatGPT, GPT-4, Claude 2 have incredible reasoning capabilities that unlock a wide variety of use cases — from insight extraction to question-answering to general workflow automation. Yet they are limited in their abilities to retrieve contextually relevant information. A popular stack that has emerged is to setup a retrieval-augmented generation (RAG) system, which combines LLMs with external storage solutions over a static knowledge source. Frameworks such as LlamaIndex provide a variety of tools to setup both simple and complex RAG systems.

Yet even this is not the complete picture. LLMs should ideally be able to dynamically search and retrieve information from the external world, not just depend on a static source of knowledge. This would allow them to fulfill a more general set of tasks and not only perform search/retrieval, but perform actions as well.

To do this well, we need two core components:

- General abstractions that allow LLMs to intelligently perform various tasks over your data, in both a “read” and “write” fashion
- A good search engine tailored for LLM use

LlamaIndex [data agent abstractions](https://medium.com/llamaindex-blog/data-agents-eed797d7972f) help to satisfy the first core component. A complete data agent consists of both a reasoning loop as well as a set of Tools. These tools can be interfaces for search/retrieval or more generally any external API. Given a query, the agent will execute its reasoning loop and dynamically figure out the set of Tools it will need to fulfill the task at hand.

Data agents have access to a rich set of Tools offered on [LlamaHub](https://llamahub.ai/) — these range from Gmail API, to a SQL db API, to a basic tool in the form of Bing search. We’ve shown that they are capable of e2e tasks from [sending emails](https://github.com/emptycrown/llama-hub/blob/main/llama_hub/tools/notebooks/gmail.ipynb), [scheduling meetings](https://github.com/emptycrown/llama-hub/blob/main/llama_hub/tools/notebooks/google_calendar.ipynb), to automating [custom support insight extraction](https://github.com/emptycrown/llama-hub/blob/main/llama_hub/tools/notebooks/shopify.ipynb). Yet there has never been a tool tailored for LLM use.

# Overview of Metaphor

The Metaphor API is designed to connect your LLM to the internet. It allows you to perform fully neural, highly semantic searches over the Internet and also get clean, HTML content from the results.

Metaphor was trained to predict links on the internet, given how people talk about things on the Internet. For example, someone might post about a great article they read like this:

>

Found an amazing article I read about the history of Rome’s architecture: [LINK]

By training a model to predict these links given how people talk about them, the end result is a totally different way to search the internet — *search as if you’re about to share the link you want*. While a little unintuitive at first, searching this way can return extremely high quality results. But for the purposes of LlamaIndex, you won’t need to worry about this because by default, queries will be converted into Metaphor prompts.

Why would you use Metaphor Search over Bing/Google? There are 3 main reasons:

- You can search fully semantically, for instance with feelings or complex descriptors.
- You can search only for the type of entity that you want. Companies, articles, people.
- You can find content that Google simply doesn’t surface well, maybe because keywords aren’t the right tool or maybe just because Google doesn’t care about returning good results for that type of content.

To learn more, you can read the full Metaphor API [blog post](https://platform.metaphor.systems/blog/building-search-for-the-post-chatgpt-world).

# Integration Details

The [Metaphor Tool Spec in LlamaHub](https://llamahub.ai/l/tools-metaphor) is an API interface that consists of 5 tools that an agent can use.

- **Search: **The entrypoint to Metaphor — allows an agent to pass a natural language query that will then be passed to the Metaphor search engine. This endpoint also contains some additional parameters, such as the number of results, domains to include/exclude, and a date filter.
- **Retrieve Documents: **This will retrieve the content of a set of documents given IDs. These ids are returned as part of the results from the search endpoint above.
- **Search and Retrieve Documents: **This is a convenience endpoint that combines the functionality of `search` and `retrieve_documents`.
- **Find Similar: **This directly calls an endpoint offered by Metaphor, which will return a list of documents similar to a given URL.
- **Current Date: **This is a convenience function that returns the current date. On its own it is unrelated to Metaphor’s API, but may be called beforehand to figure out the right date filters to pass to some of Metaphor’s endpoints.

In the next section, let’s walk through how a data agent can make use of these endpoints through various use cases.

# Example Walkthrough

Let’s walk through our example notebook showing how LlamaIndex data agents can be used with Metaphor.

**Testing the Metaphor Tools**

The first step is to import the Metaphor tool spec.

# Set up Metaphor tool
from llama_hub.tools.metaphor.base import MetaphorToolSpec
metaphor_tool = MetaphorToolSpec(
api_key='your-key',
)
# convert tool spec to a list of tools
metaphor_tool_list = metaphor_tool.to_tool_list()
for tool in metaphor_tool_list:
print(tool.metadata.name)In this walkthrough, we make use of all of the tools. But you’re free to pick and choose to use specific tools if you want to define a more custom workflow and restrict the agent action space.

We can play around with the set of tools before defining our agent. All of our Metaphor tools make use of the `AutoPrompt` option where Metaphor will pass a query through an LLM to refine and improve the query.

Example input:

metaphor_tool.search('machine learning transformers', num_results=3)Example output:

[{'title': 'On the potential of Transformers in Reinforcement Learning',
'url': 'https://lorenzopieri.com/rl_transformers/',
'id': 'ysJlYSgeGW3l4zyOBoSGcg'},
{'title': 'Transformers: Attention in Disguise',
'url': 'https://www.mihaileric.com/posts/transformers-attention-in-disguise/',
'id': 'iEYMai5rS9k0hN5_BH0VZg'},
{'title': 'Transformers in Computer Vision: Farewell Convolutions!',
'url': 'https://towardsdatascience.com/transformers-in-computer-vision-farewell-convolutions-f083da6ef8ab?gi=a1d0a9a2896c',
'id': 'kX1Z89DdjSvBrH1S1XLvwg'}]The notebook also contains examples of us playing around with the other endpoints: `retrieve_documents`, `find_similar`, `search_and_retrieve_documents`.

**Setting up an OpenAI Function Calling Agent with Metaphor**

We can create an agent with access to all of the above tools and start testing it out:

from llama_index.agent import OpenAIAgent
# We don't give the Agent our unwrapped retrieve document tools, instead passing the wrapped tools
agent = OpenAIAgent.from_tools(
  metaphor_tool_list,
  verbose=True,
)That’s it in terms of setup! Let’s try giving an example query:

print(agent.chat('What are the best restaurants in toronto?"))We walk through the execution trace of this agent to see how it is interacting with the Metaphor tool.

=== Calling Function ===
Calling function: search with args: {
  "query": "best restaurants in Toronto"
}
[Metaphor Tool] Autoprompt string: Here's a link to the best restaurant in Toronto:
Got output: [{'title': 'Via Allegro Ristorante - Toronto Fine Dining Restaurant', 'url': 'https://viaallegroristorante.com/', 'id': 'EVlexzJh-lzkVr4tb2y_qw'}, {'title': 'The Senator – Home', 'url': 'https://thesenator.com/', 'id': 'dA3HVr5P8E0Bs7nH2gH7ZQ'}, {'title': 'Home - The Rushton', 'url': 'https://therushton.com/', 'id': '6Je-igG-i-ApqISC5XXmGQ'}, {'title': 'Location', 'url': 'https://osteriagiulia.ca/', 'id': 'HjP5c54vqb3n3UNa3HevSA'}, {'title': 'StockYards | Stockyards Toronto', 'url': 'https://www.thestockyards.ca/', 'id': 'Pffz-DQlOepqVgKQDmW5Ig'}, {'title': 'Select A Restaurant', 'url': 'https://www.torontopho.com/', 'id': 'DiQ1hU1gmrIzpKnOaVvZmw'}, {'title': 'Home | Kit Kat Italian Bar &amp;amp; Grill', 'url': 'http://www.kitkattoronto.com/', 'id': 'kdAcLioBgnwzuHyd0rWS1w'}, {'title': 'La Fenice', 'url': 'https://www.lafenice.ca/', 'id': 'M-LHQZP6V40V81fqLFAQxQ'}, {'title': 'Le Phénix', 'url': 'https://www.lephenixto.com/', 'id': 'spCTcFr0GHlFUTzyngfRVw'}, {'title': 'ITALIAN, INSPIRED.', 'url': 'https://figotoronto.com/', 'id': 'OvBcTqEo1tCSywr4ATptCg'}]
========================
Here are some of the best restaurants in Toronto:

1. [Via Allegro Ristorante](https://viaallegroristorante.com/)
2. [The Senator](https://thesenator.com/)
3. [The Rushton](https://therushton.com/)
4. [Osteria Giulia](https://osteriagiulia.ca/)
5. [Stockyards](https://www.thestockyards.ca/)
6. [Toronto Pho](https://www.torontopho.com/)
7. [Kit Kat Italian Bar &amp;amp; Grill](http://www.kitkattoronto.com/)
8. [La Fenice](https://www.lafenice.ca/)
9. [Le Phénix](https://www.lephenixto.com/)
10. [Figo](https://figotoronto.com/)

You can visit their websites for more information. Enjoy your dining experience in Toronto!The execution trace shows that the agent is simply calling the `search` endpoint with “best restaurants in Toronto”, and returning that as a list of dictionaries representing the search results.

Note that we can ask a followup question as well:

print(agent.chat('tell me more about Osteria Giulia'))And we get the following result (note: we truncate some of the intermediate output):

=== Calling Function ===
Calling function: retrieve_documents with args: {
"ids": ["HjP5c54vqb3n3UNa3HevSA"]
}
Got output: […]
========================
Osteria Giulia is a restaurant located at 134 Avenue Road in Toronto, Ontario. You can contact them at 416.964.8686 or via email at info@osteriagiulia.ca (for general inquiries only, no reservation requests via email).
The restaurant's operating hours are from Monday to Saturday, from 5:00pm to 11:00pm. On Sundays, the restaurant is available for private bookings.
Parking is available on Avenue Road and Davenport Road.
You can follow Osteria Giulia on Instagram [@osteriagiulia](https://www.instagram.com/osteriagiulia). They also have a sister restaurant called Giulietta, which you can visit at [giu.ca](https://giu.ca) or on Instagram [@giulietta972](https://www.instagram.com/giulietta972).
Please note that the information provided is based on the available document and may be subject to change. It is recommended to visit their official website or contact them directly for the most up-to-date information.Since “Osteria Giulia” is in the agent conversation history, the agent now knows to call the `retrieve` endpoint to return more information about the relevant search result.

**Advanced: Avoiding Context Window Issues**

One issue with using `retrieve` is that the content can be quite long. If the content is naively appended to the conversation history and dumped into the LLM context window, then we may run into context window limitations.

LlamaIndex offers tool abstractions to help deal with this. Our `LoadAndSearchToolSpec` wraps any given tool that may return a large amount of data, and it splits it into two tools: a load tool that will dynamically store the data in an index, and a search tool that allows for search over that index.

On the Metaphor side, this is also where we define a `search_and_retrieve_documents` endpoint that combines `search` and `retrieve`. This allows the agent to make a single query to retrieve a large number of documents, which when combined with the `LoadAndSearchToolSpec` will get directly stored within an index. If the agent were to call `search` and `retrieve` separately, then it would both take longer and consume more tokens to write the search results to conversation history, and then passing that into the prompt again to call `retrieve` over all document IDs.

Creating the `LoadAndSearchToolSpec`:

from llama_index.tools.tool_spec.load_and_search.base import LoadAndSearchToolSpec
# The search_and_retrieve_documents tool is the third in the tool list, as seen above
wrapped_retrieve = LoadAndSearchToolSpec.from_defaults(
  metaphor_tool_list[2],
)Now let’s walk through a full execution example:

# Just pass the wrapped tools and the get_date utility
agent = OpenAIAgent.from_tools(
  [*wrapped_retrieve.to_tool_list(), metaphor_tool_list[4]],
  verbose=True,
)
print(agent.chat('Can you summarize everything published in the last month regarding news on superconductors'))The output here shows that the agent calls multiple tools in succession to get the right answer.

=== Calling Function ===
Calling function: current_date with args: {}
Got output: 2023-08-20
========================
=== Calling Function ===
Calling function: search_and_retrieve_documents with args: {
  "query": "superconductors",
  "start_published_date": "2023-07-20",
  "end_published_date": "2023-08-20"
}
[Metaphor Tool] Autoprompt: "Here is an interesting article about superconductors:
Got output: Content loaded! You can now search the information using read_search_and_retrieve_documents
========================
=== Calling Function ===
Calling function: read_search_and_retrieve_documents with args: {
  "query": "superconductors"
}
Got output:
Superconductors are materials that can perfectly conduct electricity. They are used in a variety of applications, such as particle accelerators, nuclear fusion devices, MRI machines, and maglev trains. However, so far, no superconductor has been proven to work at ambient pressures and temperatures. On July 22, scientists in South Korea published research claiming to have solved this problem with a material called LK-99, which has an electrical resistivity that drops to near zero at 30 degrees Celsius (86 degrees Fahrenheit).
========================
In the last month, there have been developments in the field of superconductors. Scientists in South Korea have published research on a material called LK-99, which has the ability to conduct electricity with near-zero resistance at a temperature of 30 degrees Celsius (86 degrees Fahrenheit). This breakthrough could potentially lead to the development of superconductors that work at ambient pressures and temperatures, opening up new possibilities for various applications such as particle accelerators, nuclear fusion devices, MRI machines, and maglev trains.The agent used the `get_date` tool to determine the current month, and then applied the filters in Metaphor based on publication date when calling `search`. It then loaded the documents using `retrieve_documents` and read them using `read_retrieve_documents`.

# Conclusion

As shown above, the integration between LlamaIndex data agents + Metaphor search has the potential to bypass existing limitations with LLMs and even RAG systems. We’re excited to continue exploring this further in future blog posts.

We encourage you to play around with the notebook — make sure to check it out!

**Resources:**

- Notebook: [https://github.com/emptycrown/llama-hub/blob/main/llama_hub/tools/notebooks/metaphor.ipynb](https://github.com/emptycrown/llama-hub/blob/main/llama_hub/tools/notebooks/metaphor.ipynb)
- LlamaHub: [https://llamahub.ai/l/tools-metaphor](https://llamahub.ai/l/tools-metaphor)
- Metaphor: [https://platform.metaphor.systems/](https://platform.metaphor.systems/)
- Metaphor API Docs: [https://docs.metaphor.systems/](https://docs.metaphor.systems/)