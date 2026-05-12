---
title: "LlamaParse Premium Mode: Key Features &amp; Results | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/introducing-llamaparse-premium"
category: "document-processing"
---

Content



- [ Key Features  ](#key-features)
- [ Results  ](#results)
- [ Table  ](#table)
- [ Equation  ](#equation)
- [ Reading Order  ](#reading-order)
- [ Next Steps  ](#next-steps)



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



   1



 LlamaParse is the best document parser on the market for your context-augmented LLM application. Since we launched it in February, we’ve crossed 50 million pages processed and 1M+ downloads on PyPi. It is capable of crunching any document - PDF, Powerpoint, Excel. We’ve also launched a wide range of different modes, ranging from a fast/accurate mode optimized for efficient but accurate text+table processing, to multimodal modes leveraging the latest multimodal models for understanding complex visual documents, like investor slide decks and product manuals.



 A tradeoff is that our fast/accurate modes are fantastic for parsing long text and tables but not as good for visual content, and our multimodal mode is fantastic for visual content but not as good for text/tables.



 Today you get the best of both worlds with **LlamaParse Premium Mode.** Premium mode leverages state-of-the-art multimodal models and heuristic text parsing techniques to extract text from the most complex documents, outperforming vanilla models like Sonnet-3.5. This lets users build context-augmented RAG/agent applications with even higher accuracy and lower hallucination rates.



 Try it out [today](https://cloud.llamaindex.ai/).



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



##  Key Features



 LlamaParse Premium comes with the following bells and whistles:


-  Outputs all content, from text to tables to images, into well-structured markdown
  -  Translates diagrams into [Mermaid format](https://github.com/mermaid-js/mermaid) ( between `mermaid and`  tags)
  -  Translates equations into LateX
  -  Big reduction in missing content
  -  Captions all images (between [ and ] tags)
  -  Much better heading/subheading determination than Accurate mode.



 Existing LlamaParse features, like using parsing instructions to “prompt” the parser, and webhooks to directly sync parsed data to your application, are all available with LlamaParse Premium.



##  Results



 Let’s see some examples in action showcasing LlamaParse Premium mode on complex document properties: tables, diagrams, and reading order.



 For some of these examples, we compare with raw GPT-4o and text mode.



###  Table



 Current multimodal models struggle to extract out long tables from images without hallucinations. LlamaParse Premium is able to bypass these hallucinations.



 Here is our usual caltrain schedule sample, where our Premium mode nailed it!



 **Source**:


  ![](https://cdn.sanity.io/images/7m9jw85w/production/28fa9da4b36b012eba83b4d0808e3e8e3e44d9dd-2550x3300.png)

 **GPT-4o**

  ![](https://cdn.sanity.io/images/7m9jw85w/production/6bb87db59ded846f269034ad4e97f18ca3317dc4-2550x3300.png)

 **LlamaParse Sonnet**



 Almost perfect but the model missed some heading, hallucinate one value.

  ![](https://cdn.sanity.io/images/7m9jw85w/production/36c53433a1c2450bc384df4a53c0c2c371ce3158-2550x3300.png)

 **LlamaParse Premium**

  ![](https://cdn.sanity.io/images/7m9jw85w/production/17c7704c368c826721533835f0128d511101416a-2550x3300.png)

 **Diagram**



 LlamaParse Premium outputs diagrams in Mermaid, creating a compact representation for LLMs to understand.



 This allow your RAG pipeline to answer quest on diagram in document. Here is a sample financial organization corporate structure:

  ![](https://cdn.sanity.io/images/7m9jw85w/production/a285b7d3c213b4a9f004416660d30d2a796cd59e-3507x2480.png)

 Rendered Mermaid Diagram:

  ![](https://cdn.sanity.io/images/7m9jw85w/production/a42201a5fcf2fa8103351c8c8bc47a81bb95cb0f-2962x906.png)

###  Equation



 LlamaParse Premium outputs equations as LateX between $$ symbols.



 Sample input:





  ![](https://cdn.sanity.io/images/7m9jw85w/production/69e67a45da64b3749dc321b969e25780f6f27b8d-1550x328.png)

 Outputted markdown





  ![](https://cdn.sanity.io/images/7m9jw85w/production/c1fbeaf7f0888ff8528c36e80091bd215b759bd1-1988x524.png)

 Rendered Markdown

  ![](https://cdn.sanity.io/images/7m9jw85w/production/e469d41834d1226f6b4abe19e7a89dc12bb7014b-1848x450.png)





###  Reading Order



 Multimodal models are very good at identifying document reading order out of the box, but tend to hallucinate over the text itself. On the other hand, traditional parsing approaches are fine at parsing text but fail to grasp complex order.



 LlamaParse premium preserves both. Here is the Xanax UK notice. While LlamaParse Premium missed the bottom table along with all our baselines, it outperformed both our accurate mode (better reading order, no missing content) and gpt-4o (all content is factually the content of the doc).



 **Source:**

  ![](https://cdn.sanity.io/images/7m9jw85w/production/ddc13f326a88f29843ac9aab080d1bd8e4d0d3d6-1968x1771.png)

 **Accurate mode:** There are reading order issues where the different columns are mixed up.

  ![](https://cdn.sanity.io/images/7m9jw85w/production/10b2eecdbfa6b49dd69ff5258ce6d6c6e42003a2-1969x1772.png)

 **GPT-4o:** The reading order is plausible and retains the 4 column structure but the content is hallucinated

  ![](https://cdn.sanity.io/images/7m9jw85w/production/92552d64dae64964b0656b2fda311f9ebdc6e571-1968x1771.png)

 **Sonnet 3.5:** The reading order is plausible and retains the 4 column structure but the content is hallucinated (although less than GPT4o)

  ![](https://cdn.sanity.io/images/7m9jw85w/production/468dcb9a79d769e65e16c05dd4da41827c662c1e-1968x1771.png)

 **Premium mode:** Resolves both reading order and hallucination issues. Unfortunately it misses the last table.

  ![](https://cdn.sanity.io/images/7m9jw85w/production/559577e37cfd3939bf2edf5218a8e4a286d62dbc-1969x1771.png)

 As a result, your RAG pipeline can better answer questions over these data types compared to competing solutions.



 We’ve already shown the power of good parsing for good RAG, for instance in our [multimodal](https://github.com/run-llama/llama_parse/blob/main/examples/multimodal/multimodal_rag_slide_deck.ipynb) [notebooks](https://github.com/run-llama/llama_parse/blob/main/examples/multimodal/claude_parse.ipynb). We encourage you to try out LlamaParse Premium over your complex documents and see how RAG response quality compares to baseline parsing approaches over complex data.



##  Next Steps



 LlamaParse Premium Mode operates on top of the latest multimodal models - this means that as multimodal model capabilities get better (from Sonnet-3.5 to Pixtral, o1, and more), LlamaParse Premium is better. We are of course still actively maintaining and improving our other parsing modes.



 It is currently available at 7.5c a page. **Note:** This is a bit higher than our default parsing mode, so if you’re trying it out for the first time, try out a small document first!



 You can try LlamaParse Premium today. Signup for an account and access the parsing playground here: [https://cloud.llamaindex.ai/parse](https://cloud.llamaindex.ai/parse). You can either directly view the parsed results in our parsing playground or directly toggle the setting through our [LlamaParse SDK](https://github.com/run-llama/llama_parse).



 LlamaParse Premium is integrated within LlamaParse, our enterprise RAG platform. If you&#39;re interested in using this in an enterprise setting, [come talk to us](https://www.llamaindex.ai/contact).