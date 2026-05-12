---
title: "LlamaParse Auto Mode: Cut Parsing Costs | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/optimize-parsing-costs-with-llamaparse-auto-mode"
category: "document-processing"
---

Content



- [ Intelligently select parsing modes  ](#intelligently-select-parsing-modes)
- [ Auto mode advantages  ](#auto-mode-advantages)
- [ Automatically rendering diagrams using Mermaid charts  ](#automatically-rendering-diagrams-using-mermaid-charts)
- [ Improved accuracy on table reading  ](#improved-accuracy-on-table-reading)
- [ Advanced chart conversion  ](#advanced-chart-conversion)
- [ Other auto mode features  ](#other-auto-mode-features)
- [ Available right now  ](#available-right-now)



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







 Our world-class document-parser, [LlamaParse](https://www.llamaindex.ai/llamaparse), is one of our most popular products for good reason: it&#39;s powerful, flexible, and incredibly accurate. One aspect of its flexibility is its many [parsing modes](https://docs.cloud.llamaindex.ai/llamaparse/output_modes/): you can choose fast mode for the fastest possible output, continuous mode for documents with tables that span multiple pages, or premium mode for the highest quality parsing possible.



 For long documents that interleave complex charts and images on some pages but are plain text on others this can present a challenge: you want the highest-quality output but you don&#39;t necessarily need advanced parsing on every page to get that. That&#39;s where our new [Auto Mode](https://docs.cloud.llamaindex.ai/llamaparse/output_modes/auto_mode) comes in.



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



##  Intelligently select parsing modes



 In Auto Mode, your document will by default be parsed in our standard parsing mode, but you can select one of a variety of triggers to switch to our advanced Premium parsing mode on a per-page basis. The available triggers include:


-  **Trigger on tables:** whenever a table-like structure is detected
  -  **Trigger on images:** Premium parsing on any page the contains an image
  -  **Trigger on text:** you can set a specific string that LlamaParse will search for and upgrade on, for instance you could upgrade for &quot;product details&quot; pages or &quot;summary results&quot; rather than triggering on every table.
  -  **Trigger on regular expression:** a more advanced form of triggering on text, you can get a regular expression as your matching condition, allowing you to search for multiple strings, patterns and more.



##  Auto mode advantages



 Auto-mode gets you all the advantages of Premium mode at lower cost by only triggering on the pages where it&#39;s necessary. That includes features like:



###  Automatically rendering diagrams using [Mermaid charts](https://mermaid.js.org/)



 In our [example notebook](https://github.com/run-llama/llama_parse/blob/main/examples/parsing_modes/demo_auto_mode.ipynb) you can see us convert this diagram:

  ![](https://cdn.sanity.io/images/7m9jw85w/production/ccb083e0e5fa302d6ebcc939042a259cdc6a32b7-1528x854.png)

 Into a Mermaid chart like this one:

  ![](https://cdn.sanity.io/images/7m9jw85w/production/87af4fa00df450e5907af4b3ef6855881b8e34c0-1858x486.png)

###  Improved accuracy on table reading



 Our original PDF has this table:

  ![](https://cdn.sanity.io/images/7m9jw85w/production/c6a3d88c017dd23a2344e3be0ab418739be77851-734x482.png)

 Which gets automatically converted into clean Markdown in auto mode:

  ![](https://cdn.sanity.io/images/7m9jw85w/production/0c87fe96c45e5e1e1a822e3cac104f0aac047c9a-854x920.png)

###  Advanced chart conversion



 Auto mode is also able to take this set of graphical charts:

  ![](https://cdn.sanity.io/images/7m9jw85w/production/ef8665630912448cee6df7ba51ac9517de52c747-1498x1888.png)

 And render them as a single, easy to read table in Markdown:

  ![](https://cdn.sanity.io/images/7m9jw85w/production/71a3064f4c9de4093756310c7c075c0c9d528304-1348x256.png)

###  Other auto mode features



 Our notebook is just a sample of what you get from automatic usage of Premium Mode, including:


-  LaTeX rendering of equations
  -  Lower hallucination rates
  -  Higher content retrieval rates
  -  Improved reading order



##  Available right now



 Auto Mode is already available! Check out our [example notebook](https://github.com/run-llama/llama_parse/blob/main/examples/parsing_modes/demo_auto_mode.ipynb) for an in-depth look at how to use it, read the [documentation](https://docs.cloud.llamaindex.ai/llamaparse/output_modes/auto_mode) or head on over to [LlamaParse](https://cloud.llamaindex.ai/) to sign up and get access today!