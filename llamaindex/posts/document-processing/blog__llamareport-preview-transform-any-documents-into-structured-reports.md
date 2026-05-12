---
title: "LlamaReport Preview: Structured Reports From Any Document | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/llamareport-preview-transform-any-documents-into-structured-reports"
category: "document-processing"
---

Content



- [ Report generation  ](#report-generation)
- [ What is LlamaReport?  ](#what-is-llamareport)
- [ Key Features  ](#key-features)
- [ Intelligent Document Processing  ](#intelligent-document-processing)
- [ Smart Planning Engine  ](#smart-planning-engine)
- [ LLM-Powered Report Editing  ](#llm-powered-report-editing)
- [ How It Works  ](#how-it-works)
- [ 1. Document Upload &amp; Template Definition  ](#1-document-upload-and-template-definition)
- [ 2. Plan Generation   ](#2-plan-generation)
- [ 3. Report Generation   ](#3-report-generation)
- [ 4. AI-Assisted Editing   ](#4-ai-assisted-editing)
- [ Developers First  ](#developers-first)
- [ Join the Waitlist  ](#join-the-waitlist)
- [ Coming Soon  ](#coming-soon)



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







 Today, we&#39;re thrilled to announce the beta release of LlamaReport, our new report generation tool that transforms how you create structured reports from your documents. Starting today, we&#39;re opening access to a select group of early users ahead of our general availability launch in early Q1.



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



##  Report generation



 Report generation represents the next frontier in AI-assisted knowledge work. As we explored in our [previous post](https://www.llamaindex.ai/blog/building-blocks-of-llm-report-generation-beyond-basic-rag), most RAG systems today focus on answering discrete questions - but the real value lies in producing the complete, structured documents that businesses rely on. Financial analysts need comprehensive company reports built from earnings calls and SEC filings. Management consultants need client-ready presentations synthesized from industry research. Technical teams need to generate and maintain product documentation and API guides.



 The challenge isn&#39;t just about finding relevant information; it&#39;s about transforming that information into polished, organization-ready documents. Today, even with advanced RAG systems, knowledge workers spend hours manually stitching together content, formatting documents, and ensuring consistency with organizational standards. This is where LlamaReport comes in.



##  What is LlamaReport?



 LlamaReport is an API-first solution that streamlines the entire report generation workflow. Upload your source documents and a template, and LlamaReport handles everything from parsing to final editing. What sets it apart is its incredibly flexible templating system - from simple markdown to detailed questionnaires, LlamaReport adapts to your needs.



##  Key Features



###  Intelligent Document Processing



 Uses LlamaParse document processing capabilities to get accurate information out of your documents.



###  Smart Planning Engine



 Creates a plan for how to generate a report using YOUR data and template as a starting point. Your input template can be anything — markdown, a simple prompt, a questionnaire with blank fields, and more.



 Human in the loop can be leveraged to edit a plan to be just right before generation.



###  LLM-Powered Report Editing



 Prompt the system to apply edits to your generated report. Rather than rewriting the entire report, LlamaReport will intelligently propose edits to individual parts of your report, and provide a justification for why those edits are needed.



##  How It Works



###  1. Document Upload &amp; Template Definition



 Your source documents are the knowledge that you want to reference in order to generate the content in a report.

  ![](https://cdn.sanity.io/images/7m9jw85w/production/d0245a091a0665dde5244978c00ff7786b3d5000-1568x1464.png)





 Your template is a definition of how you want the report to be written. This is flexible — your template can take many forms. A few examples are below:

  ![](https://cdn.sanity.io/images/7m9jw85w/production/db011eb9e9ee72c8eece87574c4f0b532293ce6b-1580x1636.png)





 Here’s some samples of templates we’ve found so far that work well:


-  markdown templates with instructions per section
  -  questionnaires with blank fields to fill in
  -  an example of an existing blog post (with additional template instructions describing how to parse that template)
  -  python docstring-style comments describing specific fields to extract for the report



 To help users get started, a few of these examples can be selected as a starting point!



###  2. Plan Generation



 Once your documents and template are loaded, a plan for how the report should be generated can be constructed. A plan consists of some string template, with queries mapped to string template variables.



 A plan consists of multiple blocks, which can have dependencies. These dependencies help generate the report content in an order that makes sense.

  ![](https://cdn.sanity.io/images/7m9jw85w/production/e50de62f9c3ea4073ee890a74506d78dc27dd01a-2998x1516.png)

###  3. Report Generation



 Once the plan is agreed upon, the report can be generated with the maximum amount of parallelization possible.

  ![](https://cdn.sanity.io/images/7m9jw85w/production/216d4bbb6b1951363186d06f67c357d819d21fe8-3006x1516.png)





###  4. AI-Assisted Editing



 With a generated report, you can prompt LlamaReport for further edits, which can be optionally applied to the report if you agree with them.

  ![](https://cdn.sanity.io/images/7m9jw85w/production/1210c1c77252992660cc94878d113d7d4552b5aa-3004x1630.png)





##  Developers First



 As part of the LlamaReport offering, we are also introducing a developer facing API. Using the same API that the LlamaReport UI is built with, developers can integrate LlamaReport into their existing workflows and systems.



 The API offers all the same functionality


-  report and plan generation
  -  llm-powered edits
  -  streaming event progress as actions take place



##  Join the Waitlist



 Join the [waitlist](https://docs.google.com/forms/d/e/1FAIpQLSey-D2AuIYOFN6aXc7j5RfZDtCURE9bpLf8jtQ7NXiMHm8LGw/viewform?usp=sf_link) now to be notified when the API and UI is generally available. We will be letting an initial set of users off the waitlist with high priority report generation use cases.



##  Coming Soon



 As we prepare for general availability in early Q1, we&#39;ll be:


-  Improving the quality of generated reports
  -  Adding more API-facing options, like token-level streaming
  -  Adding example templates/reports to help kickstart your development
  -  Releasing detailed documentation
  -  Publishing example notebooks and tutorials



 For enterprise inquiries or questions about the beta program, [reach out to our team](https://www.llamaindex.ai/contact).