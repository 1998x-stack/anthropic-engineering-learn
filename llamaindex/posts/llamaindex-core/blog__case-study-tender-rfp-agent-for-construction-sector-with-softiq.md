---
title: "Tender RFP Agent Case Study For Construction | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/case-study-tender-rfp-agent-for-construction-sector-with-softiq"
category: "llamaindex-core"
---

Content



- [ Challenges  ](#challenges)
- [ Solution: Agent for Tender Analysis  ](#solution-agent-for-tender-analysis)
- [ Why Choose LlamaIndex?  ](#why-choose-llamaindex)
- [ Results and Market Impact  ](#results-and-market-impact)
- [ Other LLM-Based Innovations by SoftIQ  ](#other-llm-based-innovations-by-softiq)
- [ Looking Ahead  ](#looking-ahead)



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



 [SOFTIQ](https://softiq.io/), headquartered in Poland, operates across Germany, the UK, and the Scandinavian markets, with a strong focus on public projects in Poland. With over 300 employees, 60% of whom are developers, the company has established itself as a trusted partner for major institutions. Recently, SOFTIQ has ventured into the realm of LLM-based applications, led by Adam Marszowski, to bring innovative solutions to both internal and client-facing use cases. Their latest production application is an RFP analyzing agent that revolutionizes public sector tender workflows in Poland&#39;s construction sector.



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



###  Challenges



 Public sector construction tenders in Poland are a [US$7b market](https://ezamowienia.gov.pl/pl/dane-ogolne-o-zamowieniach/), with over 17,000 contracts awarded in 2024. The construction industry in Poland faces significant challenges when analyzing public sector tenders:


-  **Business challenges:**
 **Identifying opportunities**: the traditional method of finding tenders to bid for is based on keyword matching, an inaccurate process that results in processing irrelevant tenders
  -  **Processing**: non-standardized, lengthy tender documents take anywhere from 2 hours to several days to review and extract key information
  -  **Risk Assessment and Reporting**: Generating detailed reports with executive summaries and identifying potential risks is time-consuming, and you need to follow very specific workflows.

    -  **Technical challenges:**
 **Scale:** Poland’s [public tenders platform](https://ezamowienia.gov.pl/pl/) presents thousands of unstructured documents, often over a hundred pages long each, to process
  -  **Parsing:** Converting these documents into a format suitable for semantic search and AI-driven analysis is difficult
  -  **Multimodality:** Documents often have images such as blueprints containing a wealth of relevant information — easy for human readers but harder for AI to understand




###  Solution: Agent for Tender Analysis



 SoftIQ developed an agent as a SaaS app, [Przetargi.io](http://Przetargi.io), using LlamaIndex Workflows tailored to the construction industry. This agent addresses the complexities of tender analysis with:


-  **Advanced Document Ingestion**: LlamaIndex facilitates seamless processing of lengthy tender documents, extracting relevant sections for analysis.
  -  **Semantic chunking**: Chunk the document without losing hierarchical information in terms of document layout. This is crucial in the report generation phase.
  -  **Automated Report Generation**: Produces 20-30 page reports that include executive summaries, risk assessments, and recommendations.
  -  **Prompt Engineering and Chain of Thought Reasoning**: Each section of an RFP report follows a specific business process, which has been encapsulated into LlamaIndex Workflows. Thus the reports it outputs mimic the output from manual processes previously used by construction companies and align with industry expectations.



###  Why Choose LlamaIndex?



 The SoftIQ team have deployed multiple production apps with LlamaIndex with great results, stemming from several advantages:


-  **Out-of-the-Box Features**:
 Ready-made document chunking, embedding, and querying capabilities
  -  Seamless integration for RAG (Retrieval-Augmented Generation) workflows including both semantic search and metadata search
  -  Multimodal parsing makes handling image data a breeze

    -  **Ease of Integration**:
 Minimal friction setting up with [Przetargi.io](http://przetargi.io/)’s existing data pipelines.

    -  **Scale**
 LlamaIndex easily handles workloads of tens of thousands of documents spanning millions of pages of data




###  Results and Market Impact



 [Przetargi.io](http://przetargi.io/) streamlines tender analysis for construction companies, reducing the time and effort required for tender analysis. The application serves a vast market of construction companies participating in tenders, creating significant value in the Polish construction sector. Key results included:


-  **Enhanced accuracy**: in addition to saving time processing tenders, accuracy of tender selection improved significantly, resulting in **less wasted effort** on irrelevant tenders compared to traditional keyword-based approaches.
  -  **Client efficiency gains**: clients save anywhere from 3 hours to multiple days per tender, depending on the complexity and length of the documentation. On average, tender analysis time fell to **less than 10 minutes.** One pilot client went from **3 tenders per day per employee to 20-30 tenders per day per employee.**
  -  **Rapid development:** LlamaIndex’s simple indexing logic and vector store connections **saved an estimated 2 months of development time**.



###  Other LLM-Based Innovations by SoftIQ



 In addition to the construction tenders agent, SoftIQ has developed many other innovate LLM-powered applications, including:


-  **Helpdesk Chatbot** Originally created for internal use, now deployed with a major Polish public institution assisting 1000s of support agents.
  -  **Tender Analysis for Other Sectors** Analyzes tenders in software and lighting industries, tailored for specific client needs.
  -  **Recruitment Tools** AI-powered tools to both generate resumés across languages and a resumé analysis platform that matches candidates to job offers and open positions.



###  Looking Ahead



 By partnering with LlamaIndex, SOFTIQ has set a new standard for tender analysis in the construction sector and many other domains, showcasing the transformative potential of LLM-based solutions.


-  Learn more about [LlamaParse](https://www.llamaindex.ai/enterprise), the turn-key enterprise solution from LlamaIndex
  -  Read up on [Workflows](https://docs.llamaindex.ai/en/stable/understanding/workflows/), the core building block of agentic solutions in LlamaIndex
  -  [Get in touch with us](https://www.llamaindex.ai/contact) to see where LlamaIndex can take your company!