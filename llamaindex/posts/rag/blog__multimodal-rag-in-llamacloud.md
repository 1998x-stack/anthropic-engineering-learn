---
title: "Multimodal RAG Guide: Index Text + Images | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/multimodal-rag-in-llamacloud"
category: "rag"
---

Content



- [ The Future of Document RAG is Multimodal  ](#the-future-of-document-rag-is-multimodal)
- [ LlamaParse Multimodal Feature Overview  ](#llamaparse-multimodal-feature-overview)
- [ Real-World Example: Analyzing Corporate Presentations  ](#real-world-example-analyzing-corporate-presentations)
- [ 1. Create a Multimodal Index  ](#1-create-a-multimodal-index)
- [ 2. Integrate the Index into Your Code  ](#2-integrate-the-index-into-your-code)
- [ 3. Set Up Multimodal Retrieval  ](#3-set-up-multimodal-retrieval)
- [ 4. Build a Custom Multimodal Query Engine  ](#4-build-a-custom-multimodal-query-engine)
- [ 5. Query Your Multimodal Index  ](#5-query-your-multimodal-index)
- [ Getting Started  ](#getting-started)



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







 We&#39;re excited to announce the launch of multimodal capabilities in LlamaParse, our enterprise RAG platform. This new feature enables developers to build fully multimodal RAG pipelines in minutes, over a broad range of document types - from investor slide decks to insurance contracts to research reports.



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



##  The Future of Document RAG is Multimodal



 Many documents in the wild not only contain text, but also complex visual elements like images, charts, and diagrams. Traditional RAG systems tend to focus solely on text. This leads to decreased document understanding, lower quality responses, and increased hallucination rates.



 Multimodal LLMs and RAG systems can address these complexities - multimodal LLMs like Pixtral, Sonnet 3.5, and GPT-4o are increasingly better at document understanding. Our customers have asked us for these capabilities for advanced knowledge assistant use cases, like generating structured reports with both charts and images.



 Yet these systems are complex to setup and productionize. An ideal multimodal pipeline not only extracts images into text, but also stores native image chunks that are indexed along with text chunks. This allows the LLM to take in both retrieved text and images as input during the synthesis phase. Doing this well requires clever algorithms around parsing, indexing, and retrieval and infrastructure to serve both text and images. We have notebooks in both the [core LlamaIndex repo](https://docs.llamaindex.ai/en/stable/examples/multi_modal/gpt4v_multi_modal_retrieval/) and [LlamaParse](https://github.com/run-llama/llama_parse) to help you build multimodal RAG setups, but they contain a lot of code, are optimized for a small number of local files, and avoid system-level complexities of how to scale this indexing to production.



 LlamaParse’s new multimodal feature let you build a full multimodal RAG pipeline in minutes. Index both text and image chunks. Retrieve both text and images and provide those as sources in the response.



##  LlamaParse Multimodal Feature Overview



 At a high-level, our multimodal feature lets you build a RAG pipeline that can index and retrieve both text and image chunks. You can easily validate your pipeline through our chat interface (see below images), or plug it into your application through an API.

  ![](https://cdn.sanity.io/images/7m9jw85w/production/d2082e29b3b52d6f893a15517648b2f4952d18d6-1388x1008.png)    ![](https://cdn.sanity.io/images/7m9jw85w/production/12c54e7823e41610329de0051234b03cf8d2c05a-1398x1005.png)

 **Key Benefits**


-  **Reduced Time to Value**: Activating multimodal indexing is as simple as clicking a toggle when creating a RAG index.
  -  **High Performance over Unstructured Data**: Achieve superior retrieval quality across text and images in complex documents like PDFs and PowerPoints.
  -  **Comprehensive Understanding**: Leverage both textual and visual information for more accurate and context-aware AI responses.
  -  **Simplified Data Integration**: Easily incorporate diverse data types into your RAG pipeline without extensive preprocessing.



##  Real-World Example: Analyzing Corporate Presentations



 To demonstrate the effectiveness of multimodal RAG, let&#39;s consider a real-world example using a [ConocoPhillips investor presentation](https://static.conocophillips.com/files/2023-conocophillips-aim-presentation.pdf). Let&#39;s walk through the process:



###  1. Create a Multimodal Index



 First, create a new LlamaParse Index and enable the Multi-Modal Indexing option. This feature automatically generates and stores page screenshots alongside the extracted text, allowing for both text and image retrieval.

  ![](https://cdn.sanity.io/images/7m9jw85w/production/aac83d58705788b39a686601da4650c0c98254dd-1277x263.png)

###  2. Integrate the Index into Your Code



 Once your index is created, you can easily integrate it into your Python code:



python






```
from llama_index.indices.managed.llama_cloud import LlamaParseIndex

index = LlamaParseIndex(
    name="&#x3C;index_name>",
    project_name="&#x3C;project_name>",
    organization_id="...",
    api_key="llx-..."
)
```


###  3. Set Up Multimodal Retrieval

  To enable multimodal retrieval, create a retriever that can handle both text and image nodes:



python






```
retriever = index.as_retriever(retrieve_image_nodes=True)
```


###  4. Build a Custom Multimodal Query Engine

  To fully leverage the power of multimodal RAG, we recommend creating a custom query engine that can take full advantage of this multimodal retriever. It will separate the text and image nodes from the retriever, and feed them into a multimodal model through our multimodal LLM abstraction:







python






```
from llama_index.core.query_engine import CustomQueryEngine
from llama_index.multi_modal_llms.openai import OpenAIMultiModal

class MultimodalQueryEngine(CustomQueryEngine):
		"""Custom multimodal Query Engine.

    Takes in a retriever to retrieve a set of document nodes.
    Also takes in a prompt template and multimodal model.

    """

    qa_prompt: PromptTemplate
    retriever: BaseRetriever
    multi_modal_llm: OpenAIMultiModal

    def __init__(self, qa_prompt: Optional[PromptTemplate] = None, **kwargs) -> None:
        """Initialize."""
        super().__init__(qa_prompt=qa_prompt or QA_PROMPT, **kwargs)

    def custom_query(self, query_str: str):
        # retrieve text nodes
        nodes = self.retriever.retrieve(query_str)
        img_nodes = [n for n in nodes if isinstance(n.node, ImageNode)]
        text_nodes = [n for n in nodes if isinstance(n.node, TextNode)]

        # create context string from text nodes, dump into the prompt
        context_str = "\\n\\n".join(
            [r.get_content(metadata_mode=MetadataMode.LLM) for r in nodes]
        )
        fmt_prompt = self.qa_prompt.format(context_str=context_str, query_str=query_str)

        # synthesize an answer from formatted text and images
        llm_response = self.multi_modal_llm.complete(
            prompt=fmt_prompt,
            image_documents=[n.node for n in img_nodes],
        )
        return Response(
            response=str(llm_response),
            source_nodes=nodes,
            metadata={"text_nodes": text_nodes, "image_nodes": img_nodes},
        )

        return response

query_engine = MultimodalQueryEngine(
   retriever=retriever, multi_modal_llm=gpt_4o
)
```





 **Note:** We’re hoping to make this experience a one-liner - stay tuned!



###  5. Query Your Multimodal Index



 Now you&#39;re ready to query your multimodal index and receive responses that incorporate both textual and visual information:



 response = query_engine.query(&quot;Tell me about the diverse geographies which represent the production bases&quot;)
print(str(response))




 When asked about the company&#39;s diverse production bases, our multimodal RAG system provides a comprehensive response:



 &quot;The diverse geographies representing the production bases for ConocoPhillips include:


-  Lower 48 (United States)
  -  Canada
  -  Alaska
  -  EMENA (Europe, Middle East, and North Africa)
  -  Asia Pacific



 This information is derived from both the text and images provided in the presentation, showcasing how our system integrates multiple data types to provide a complete answer.&quot;



##  Getting Started



 Point LlamaParse at your bucket of unstructured files; let us handle the rest so that you can focus on application logic. Sign up for a LlamaParse account at [https://cloud.llamaindex.ai/](https://cloud.llamaindex.ai/) - we’re letting lots of people off the waitlist.



 We have a great reference notebook here to help you get [started](https://github.com/run-llama/llamacloud-demo/blob/main/examples/multimodal/getting_started_mm.ipynb).



 If you&#39;re looking to adopt LlamaParse in an enterprise setting, [come talk to us](https://www.llamaindex.ai/contact).