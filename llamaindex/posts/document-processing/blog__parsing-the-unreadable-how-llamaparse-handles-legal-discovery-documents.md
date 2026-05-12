---
title: "Parsing the Unreadable: How LlamaParse Handles Legal Discovery Documents"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/parsing-the-unreadable-how-llamaparse-handles-legal-discovery-documents"
category: "document-processing"
---

Content



- [ Discovery Documents Are Difficult to Parse  ](#discovery-documents-are-difficult-to-parse)
- [ The Documents Aren&#39;t Just Text  ](#the-documents-arent-just-text)
- [ What LlamaParse Brings to This Problem  ](#what-llamaparse-brings-to-this-problem)
- [ Setting Up LlamaParse for a Discovery Document Pipeline  ](#setting-up-llamaparse-for-a-discovery-document-pipeline)
- [ The Downstream Difference Good Parsing Makes  ](#the-downstream-difference-good-parsing-makes)
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



   7



 If you&#39;ve ever worked with legal documents, you might know that during litigation, one of the most time-consuming phases is called discovery (thank you [Suits](https://www.imdb.com/title/tt1632701/) for making it so that I know what this means)! This is the process where both sides in a lawsuit are required to hand over relevant documents to each other. In practice, this means lawyers sifting through tens of thousands, sometimes hundreds of thousands, of files looking for the pieces of evidence that matter, a burden the U.S. federal court system itself has heard described as a [&quot;nightmare&quot; and a &quot;morass&quot;](https://www.uscourts.gov/file/document/e-discovery-today-fault-lies-not-our-rules).



 To make this manageable, legal firms rely on dedicated eDiscovery platforms [like Relativity, Everlaw, and DISCO](https://www.gartner.com/reviews/market/e-discovery-software). These tools are built for exactly this workflow: ingesting large document productions, indexing them, and letting legal teams search, tag, and filter down to the documents that actually matter for a case.



 The problem is that for any of that to work well, the documents need to be parsed correctly first. And the documents they&#39;re handed are, often (and often by design), hard to work with.



##  Discovery Documents Are Difficult to Parse



 When documents are produced during discovery, the other side doesn&#39;t exactly go out of their way to make them easy to read. Files are typically scanned, not exported as native PDFs. Scans come in at low resolutions, in black and white, various rotations etc. The receiving party gets a flat image that&#39;s technically a PDF, but contains very little of the structured information you&#39;d hope to extract from it.



 The result is a mountain of documents that are nominally searchable but practically aren&#39;t. Traditional OCR tools struggle at low resolutions. When OCR does extract text, spacing errors are common: the letters might be there, but &quot;settlement&quot; comes out as &quot;s ettl em ent&quot; and your regex query finds nothing. Semantic search doesn&#39;t exist in most of the older systems legal firms rely on today. So lawyers end up writing regex queries to run against the document set. They get back a list of results (if the OCR cooperated at all) and work from there.



 This is slow, fragile, and misses an enormous category of content entirely: anything visual.



##  The Documents Aren&#39;t Just Text



 Consider what a discovery production actually contains. Yes, there are emails and memos. But there are also:


-  Photographs (potentially of people, places, or evidence of physical harm)
  -  PowerPoint presentations with embedded charts and graphics
  -  Tables buried in scanned reports
  -  Handwritten annotations on printed documents



 None of these are handled well by text-based search. If you&#39;re looking for evidence that someone misrepresented data in a slide deck, no regex query is going to surface that chart for you. If you need to go through all documents that contain photographs of a specific person, you&#39;d need someone to manually tag every document that has a photo in it before you can even begin filtering.



 This is where the parser matters at the foundation. If you&#39;re building a search or classification system on top of discovery documents, what you extract at ingestion time determines everything about what you can find later.



##  What LlamaParse Brings to This Problem



 LlamaParse is a document parsing tool built specifically to handle the kinds of documents that break simpler tools. It also uses multimodal models under the hood, which means it doesn&#39;t just extract text. It understands the visual layout of a page ([see the “items” output in the API if you’re interested](https://developers.llamaindex.ai/python/cloud/llamaparse/basics/retrieving-results/#content-fields)), can describe images and charts, and handles the structural complexity of tables and mixed-content documents.



 For legal discovery, this unlocks a few things that traditional OCR pipelines can&#39;t offer.



 First, it handles low-quality scans significantly better. LlamaParse uses vision models to interpret page content rather than relying purely on pixel-level text recognition. A page that comes in blurry, skewed, or at low DPI can still yield usable, structured output.



 Second, it preserves and surfaces visual content. When a page contains a photograph, LlamaParse can describe what&#39;s in it. When a page contains a chart, it can extract the data or describe what the chart represents. This is the difference between a document being invisible to your search system and being fully indexed.



 Third, you can guide its behavior with custom parsing instructions. Discovery documents often follow predictable patterns: case numbers in headers, specific formatting for deposition exhibits, certain kinds of tables. You can tell LlamaParse exactly what to look for and how to structure the output.



##  Setting Up LlamaParse for a Discovery Document Pipeline



 Let me walk through how you&#39;d actually configure this. Start by installing the `llama-cloud`  package and setting your API key, which you can get from [cloud.llamaindex.ai](https://cloud.llamaindex.ai/api-key):



bash






```
pip install llama-cloud
```
     python






```
import os
from llama_cloud import AsyncLlamaCloud

os.environ["LLAMA_CLOUD_API_KEY"] = "llx-..."

client = AsyncLlamaCloud()
```





 The LlamaParse API works in two steps: you first upload the file, then kick off a parse job. The `expand`  parameter tells LlamaParse which output views to return. For a discovery pipeline, you&#39;ll typically want `&quot;markdown&quot;`  for LLM-friendly structured text, `&quot;text&quot;`  for plain page-by-page content, and `&quot;items&quot;`  when you need the structured layout tree (useful for detecting tables and figures):



python






```
# Upload the document
file_obj = await client.files.create(
    file="./discovery_batch/doc_001.pdf",
    purpose="parse",
)

# Parse it
result = await client.parsing.parse(
    file_id=file_obj.id,
    tier="agentic",
    version="latest",
    expand=["markdown", "text", "items"],
)

# Access the output
for page in result.markdown.pages:
    print(page.markdown)
```





 For discovery documents specifically, you&#39;ll almost always want to step up to `tier=&quot;agentic_plus&quot;` . The higher tier is optimized for complex layouts and visual content, and the high-res OCR we use for all our tiers makes a meaningful difference on degraded scans:



python






```
result = await client.parsing.parse(
    file_id=file_obj.id,
    tier="agentic_plus",
    version="latest",
    expand=["markdown", "text", "items"],
)
```
    Now, the feature I&#39;d point you toward is `custom_prompt` . This lets you provide natural language guidance about what kinds of documents you&#39;re dealing with and what matters most in the output. For legal discovery, something like this goes a long way:



python






```
parsing_instruction = """
These are legal discovery documents produced during litigation.
They may be scanned at low resolution and appear in black and white.

For each document, please:
- Extract all visible text, correcting for common OCR artifacts like broken spacing
- Identify and describe any photographs, noting whether they contain images of people
- Extract data from any tables or charts, including chart titles and axis labels
- Note the presence of handwritten annotations separately from printed text
- Preserve any visible case numbers, bates numbers, or exhibit markers
"""

result = await client.parsing.parse(
    file_id=file_obj.id,
    tier="agentic_plus",
    version="latest",
    expand=["markdown", "text", "items"],
    output_options={
        "markdown": {
            "tables": {"output_tables_as_markdown": True}
        }
    },
    agentic_options={
		    "custom_prompt": parsing_instruction
    },
)

for page in result.markdown.pages:
    print(page.markdown[:500])
```





 The `custom_prompt`  field accepts plain English. You&#39;re essentially briefing the model on what it&#39;s looking at and what to pay attention to, the same way you&#39;d brief a junior associate before handing them a box of files.



##  The Downstream Difference Good Parsing Makes



 It&#39;s worth being direct about something: no parsing tool makes discovery easy. The volume of documents involved in major litigation is huge, and even with good tooling, review is painstaking work. What better parsing does is reduce the number of relevant documents that fall through the cracks.



 If your search index is built on extracted text that&#39;s full of OCR errors, semantic search will only go so far. Your embeddings will be noisy and your recall will suffer. If your classification system has never seen the photograph in document 47,823, it can&#39;t tell you whether that photograph is relevant. The quality of everything downstream depends on what happened at the point of ingestion.



 LlamaParse is most valuable here as the foundation layer. You&#39;re not asking it to do legal reasoning. You&#39;re asking it to make documents legible and structured enough that the systems built on top of it can do their jobs.



##  Getting Started



 If you want to try this out with your own documents, you can sign up to [LlamaParse](https://cloud.llamaindex.ai/) and get a free tier of pages to experiment with. The [LlamaParse documentation](https://developers.llamaindex.ai/python/cloud/llamaparse/) covers the full API, including all the parsing tiers and output options.