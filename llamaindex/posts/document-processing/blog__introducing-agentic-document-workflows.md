---
title: "Agentic Document Workflows: A Practical Guide | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/introducing-agentic-document-workflows"
category: "document-processing"
---

Content



- [ Moving Beyond Basic RAG  ](#moving-beyond-basic-rag)
- [ Building Intelligent Document Agents  ](#building-intelligent-document-agents)
- [ Contract Review: Intelligent Compliance Analysis  ](#contract-review-intelligent-compliance-analysis)
- [ Patient Case Summaries: Contextual Understanding  ](#patient-case-summaries-contextual-understanding)
- [ Invoice Processing: Optimizing Business Operations  ](#invoice-processing-optimizing-business-operations)
- [ Auto Insurance Claims Processing: Structured Analysis Support  ](#auto-insurance-claims-processing-structured-analysis-support)
- [ Building Production-Ready Solutions  ](#building-production-ready-solutions)
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



   1



 We’re kicking off 2025 by introducing a new architecture for applying agents on top of your documents: Agentic Document Workflows (ADW). This architecture combines document processing, retrieval, structured outputs, and agentic orchestration to enable end-to-end knowledge work automation. It is a step beyond both traditional Intelligent Document Processing (IDP) and RAG paradigms, which are focused on small, isolated steps of extraction and question-answering respectively, and helps to fulfill the promise of agents in dramatically increasing knowledge productivity.

  ![](https://cdn.sanity.io/images/7m9jw85w/production/831d2c33d5305e136a48921209cea977e7f32663-1953x1013.png)

##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



##  Moving Beyond Basic RAG



 While RAG has emerged as a powerful pattern for grounding LLMs in enterprise data, many real-world document workflows require more sophisticated orchestration. Consider a typical contract review workflow: an analyst needs to extract key clauses, cross-reference regulatory requirements, identify potential risks, and generate compliance recommendations. This requires not just information retrieval, but structured reasoning and decision support.



 Traditional approaches often struggle with complex workflows that go beyond simple extraction or matching. In real organizations:


-  Documents don&#39;t exist in isolation - processes involve contracts, policies, emails, and forms working together
  -  Decisions span multiple steps - from data extraction to validation to approval to recommendations
  -  Context and state must be maintained across the entire process
  -  Multiple systems need to coordinate - parsers, retrievers, and business logic engines



 Agentic Document Workflows (ADW) address these challenges by treating documents as part of broader business processes. An ADW system can maintain state across steps, apply business rules, coordinate different components, and take actions based on document content - not just analyze it.



##  Building Intelligent Document Agents



 We&#39;ve developed a set of reference architectures that demonstrate how to combine LlamaParse&#39;s enterprise-grade parsing and retrieval capabilities with intelligent agents. Each architecture shows how to build systems that can understand context, maintain state, and drive multi-step processes.



 The core of each workflow is a document agent that orchestrates the entire process. These agents:


-  Extract and structure information from input documents using LlamaParse
  -  Maintain state about the document context and process stage
  -  Retrieve and analyze relevant reference materials from a knowledge base (LlamaParse)
  -  Generate actionable recommendations based on business rules



 By maintaining state throughout the process, agents can handle complex multi-step workflows that go beyond simple extraction or matching. This approach allows them to build deep context about the documents they&#39;re processing while coordinating between different system components.



 Let&#39;s explore this through some real-world sample use cases. These + other use cases are also directly available as notebook resources.



##  Contract Review: Intelligent Compliance Analysis



 The [contract review workflow](https://github.com/run-llama/llamacloud-demo/blob/main/examples/document_workflows/contract_review/contract_review.ipynb) showcases how document agents can perform sophisticated analysis across multiple documents. When analyzing a vendor agreement, the agent parses complex contract structures, identifies key clauses, and matches them against a knowledge base of regulatory requirements stored in LlamaParse.



 This allows it to surface potential compliance issues and provide structured recommendations about areas that require human review - such as non-standard terms, missing provisions, or clauses that may conflict with regulations. The system serves as an intelligent assistant, helping legal teams work more efficiently while keeping humans firmly in control of final decisions.



##  Patient Case Summaries: Contextual Understanding



 The exploding volume of healthcare documentation presents unique challenges that demonstrate the power of intelligent document processing to accelerate the work of physicians. Our [patient case summary agent](https://github.com/run-llama/llamacloud-demo/blob/main/examples/document_workflows/patient_case_summary/patient_case_summary.ipynb) doesn&#39;t just extract information from medical records, it can group related conditions, treatments and outcomes together, aiding diagnosis and treatment.



 The workflow can parse complex medical documents, including lab results and clinical notes, while maintaining the critical context of a patient&#39;s history. By matching this information against medical guidelines stored in LlamaParse, the agent can generate comprehensive case summaries that highlight key clinical insights for physician review.



##  Invoice Processing: Optimizing Business Operations



 Our [invoice processing workflow](https://github.com/run-llama/llamacloud-demo/blob/main/examples/document_workflows/invoice_payments/invoice_payments.ipynb) shows how intelligent agents can add business intelligence to routine tasks. The agent goes beyond basic data extraction to support optimization of payment timing based on vendor agreements and early payment discounts.



 Using LlamaParse to accurately extract line items and payment terms, combined with LlamaParse&#39;s retrieval capabilities, the agent can verify pricing against contracted rates and suggest optimal payment strategies. This transforms a simple document processing task into a tool for working capital optimization.



##  Auto Insurance Claims Processing: Structured Analysis Support



 Our [auto insurance claims workflow](https://github.com/run-llama/llamacloud-demo/blob/main/examples/document_workflows/auto_insurance_claims/auto_insurance_claims.ipynb) demonstrates how intelligent document processing can support—not replace—human decision-making in complex processes. The agent helps claims processors by organizing and structuring information from multiple documents: parsing incoming claims forms, matching relevant sections of policy documents, and presenting key details in a clear format.



 Importantly, the system is designed to augment human expertise, not make final decisions. It helps claims processors by surfacing relevant policy details and organizing information, while leaving all coverage and settlement decisions firmly in human hands. This showcases how AI can streamline processes while maintaining appropriate human oversight in sensitive domains.



##  Building Production-Ready Solutions



 Each of these examples is implemented as a detailed Jupyter notebook that you can run and adapt. The workflows demonstrate our approach to production-grade document processing: combining LlamaParse&#39;s advanced document understanding capabilities with LlamaParse&#39;s robust retrieval and our agentic framework.



 The notebooks show how to handle real-world complexities like error handling, validation, and scalability. They&#39;re designed to serve as starting points for your own implementations, with clear examples of how to customize the logic for your specific use cases.



##  Getting Started



 We&#39;re seeing enterprises across industries adopt these more advanced patterns beyond basic chatbots. Ready to start building? You can:


-  Explore our example implementations
 [Contract Review Workflow](https://github.com/run-llama/llamacloud-demo/blob/main/examples/document_workflows/contract_review/contract_review.ipynb)
  -  [Patient Case Summary Workflow](https://github.com/run-llama/llamacloud-demo/blob/main/examples/document_workflows/patient_case_summary/patient_case_summary.ipynb)
  -  [Invoice Processing Workflow](https://github.com/run-llama/llamacloud-demo/blob/main/examples/document_workflows/invoice_payments/invoice_payments.ipynb)
  -  [Invoice Unit Standardization Workflow](https://github.com/run-llama/llamacloud-demo/blob/main/examples/document_workflows/invoice_standardization/invoice_standardization.ipynb)
  -  [Invoice + SKU Matching Workflow](https://github.com/run-llama/llamacloud-demo/blob/main/examples/document_workflows/invoice_sku_product_catalog_matching/invoice_sku_product_catalog_matching.ipynb)
  -  [Auto Insurance Claims Workflow](https://github.com/run-llama/llamacloud-demo/blob/main/examples/document_workflows/auto_insurance_claims/auto_insurance_claims.ipynb)

    -  [Sign up for LlamaParse](https://cloud.llamaindex.ai/) to access enterprise-grade parsing and retrieval
  -  If you’re interested in building this in an enterprise setting, [come talk to us](https://www.llamaindex.ai/contact).
  -  Join our [Discord community](https://discord.gg/llamaindex) to discuss your use cases and get implementation support



 Over the coming weeks, we’ll be announcing a *lotd* of new feature releases and educational deep-dives that will allow you to build production agentic document workflows for an increasing number of use cases. Stay tuned!