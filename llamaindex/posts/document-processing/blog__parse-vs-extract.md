---
title: "Parse vs Extract: Understanding Two Fundamental Approaches to Document Processing"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/parse-vs-extract"
category: "document-processing"
---

Content



- [ The Core Difference  ](#the-core-difference)
- [ Parsing: Document Transformation  ](#parsing-document-transformation)
- [ Extraction: Targeted Data Capture  ](#extraction-targeted-data-capture)
- [ When to Parse  ](#when-to-parse)
- [ Build Search and Q&amp;A Systems  ](#build-search-and-qanda-systems)
- [ Enable RAG (Retrieval Augmented Generation)  ](#enable-rag-retrieval-augmented-generation)
- [ Preserve Document Context (and layout)  ](#preserve-document-context-and-layout)
- [ When to Extract  ](#when-to-extract)
- [ Populate Databases and Systems  ](#populate-databases-and-systems)
- [ Automate Business Workflows  ](#automate-business-workflows)
- [ Process Forms and Standardized Documents  ](#process-forms-and-standardized-documents)
- [ Understanding the Relationship: Parsing Enables Extraction  ](#understanding-the-relationship-parsing-enables-extraction)
- [ Making the Choice  ](#making-the-choice)
- [ Implementation Examples with LlamaParse  ](#implementation-examples-with-llamaparse)
- [ LlamaParse: Built for Parsing  ](#llamaparse-built-for-parsing)
- [ LlamaExtract: Built for Extraction  ](#llamaextract-built-for-extraction)
- [ The Bottom Line  ](#the-bottom-line)



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



   50



 If you&#39;re building AI applications that work with documents, you&#39;ll inevitably face a critical decision: should you parse or extract? While these terms are often used interchangeably, they represent fundamentally different approaches to document processing, as well as different outcomes.



 Here&#39;s the critical distinction: **Parsing transforms documents into formats optimized for AI consumption, while extraction pulls specific, predefined data points into structured outputs.**



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



##  The Core Difference



###  Parsing: Document Transformation



 Parsing is the process of converting complex, unstructured documents into clean, structured representations that preserve the document&#39;s content and context while making it machine-readable.



 **What parsing does:**


-  Converts various formats (PDFs, Word docs, scanned images) into text or markdown
  -  Preserves document structure: headings, paragraphs, tables, lists
  -  Maintains relationships between elements (which table belongs to which section)
  -  Handles visual elements: images, charts, diagrams, equations
  -  Creates a comprehensive representation of the entire document
  -  Optimizes output for downstream processing by AI systems



 **Primary goal:** Make document content accessible and understandable to machines, particularly Large Language Models (LLMs), while retaining the full context and structure.



###  Extraction: Targeted Data Capture



 Extraction is the process of identifying and pulling specific pieces of information from documents based on predefined schemas or patterns, outputting only the data points you&#39;ve specified.



 **What extraction does:**


-  Identifies specific fields you define (dates, amounts, names, addresses)
  -  Returns only the requested information, not the full document
  -  Validates extracted data against expected types and formats
  -  Maps unstructured text to structured data models
  -  Outputs standardized formats (typically JSON) for downstream systems
  -  Discards everything except the target information



 **Primary goal:** Transform unstructured documents into structured, validated data records that feed databases, APIs, or business workflows.



##  When to Parse



 Choose parsing when you need to:



###  Build Search and Q&amp;A Systems



 You&#39;re creating systems where users ask natural language questions about document content. Parsing ensures the full context is available for retrieval.



 **Example scenario:** A legal research system where lawyers search across thousands of case documents using natural language queries. The system needs access to complete documents (not just extracted fields) to find relevant passages and provide accurate answers.



###  Enable RAG (Retrieval Augmented Generation)



 Your LLM needs document content as context to generate informed responses. Parsing converts documents into formats that can be embedded, indexed, and retrieved efficiently.



 **Example scenario:** A customer support chatbot that answers questions by referencing your product documentation, support tickets, and knowledge base articles. The LLM needs full context from these documents, not just extracted metadata.



###  Preserve Document Context (and layout)



 The relationships between different parts of the document matter. A table means different things depending on the section it appears in; a chart needs its caption and surrounding text to be interpretable.



 **Example scenario:** Analyzing scientific papers where tables, figures, and surrounding text must be understood together. Parsing maintains these relationships so an AI can properly interpret &quot;as shown in Figure 3&quot; or &quot;the results in Table 2 indicate.&quot;



##  When to Extract



 Choose extraction when you need to:



###  Populate Databases and Systems



 You&#39;re feeding structured data into databases, CRMs, ERPs, or other systems that require specific fields in specific formats.



 **Example scenario:** Processing thousands of invoices to populate your accounts payable system. You need invoice number, vendor name, date, line items, and total, nothing more. The full invoice content isn&#39;t useful; you need structured records.



json






```
{
  "invoice_number": "INV-2024-00123",
  "vendor_name": "Acme Corp",
  "due_date": "2024-03-15",
  "total_amount": 3456.78
}
```


###  Automate Business Workflows

  You&#39;re triggering actions based on document content: routing forms, flagging exceptions, updating records, or generating reports.



 **Example scenario:** HR application processing where resumes trigger different workflows based on extracted fields. Years of experience &gt;5 goes to senior roles, specific skills match to relevant teams, location determines office assignment.



###  Process Forms and Standardized Documents



 You&#39;re handling documents that follow similar patterns: invoices, receipts, applications, contracts, medical forms etc, where the same fields appear across many documents.



 **Example scenario:** Insurance claims processing where each claim form has standard fields (policy number, date of incident, claim amount, description). Extraction pulls these into your claims management system.



##  Understanding the Relationship: Parsing Enables Extraction



 Here&#39;s a critical insight that many developers miss: **extraction doesn&#39;t replace parsing, it builds on top of it.** Before you can extract specific fields from a document, something needs to parse that document first to make its content accessible.



 Extraction is actually the more complex operation. It requires parsing to happen first (to convert the raw document into readable text), then adds an additional layer of intelligence to identify, validate, and structure the specific fields you need. Think of parsing as the foundation and extraction as the specialized structure built on top.



 This means when you&#39;re &quot;just extracting,&quot; you&#39;re still parsing. You&#39;re just not keeping the full parsed output. The parsing step converts your PDF or scanned image into machine-readable content, then the extraction logic identifies your invoice number, date, and total amount within that parsed content.



##  Making the Choice



 The decision comes down to what you&#39;re optimizing for. Parse when you need flexibility and comprehensive understanding. Extract when you need efficiency and integration, you know exactly what fields you need and where they&#39;re going.



 Parse-only makes sense for exploratory applications where users ask open-ended questions. Extract-only (which still parses internally) works for high-volume form processing with consistent schemas. Most sophisticated systems do both: parse for intelligence, extract for integration.



##  Implementation Examples with LlamaParse



 LlamaParse provides purpose-built services for both approaches, demonstrating these concepts in practice:



###  LlamaParse: Built for Parsing



 LlamaParse is a AI-native parsing service that converts complex documents into formats easily digestible by LLMs:



python






```
from llama_cloud_services import LlamaParse
from llama_index.core import VectorStoreIndex

*# Parse documents for comprehensive understanding*
parser = LlamaParse(parse_mode="parse_page_with_agent")
documents = parser.parse(["report_q1.pdf", "report_q2.pdf"])

*# Create searchable index*
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()

*# Ask anything about the documents*
response = query_engine.query("Compare Q1 and Q2 revenue growth trends")
```
    LlamaParse handles complex layouts, tables, charts, and visual elements, making the full document content accessible to AI systems.



###  LlamaExtract: Built for Extraction



 LlamaExtract is a schema-based extraction service that pulls specific fields into validated JSON. Importantly, LlamaExtract runs LlamaParse in the background first to convert your document into machine-readable content, then applies extraction logic on top of that parsed output:



python






```
from llama_cloud_services import LlamaExtract
from pydantic import BaseModel, Field

*# Define exactly what you need*
class InvoiceSchema(BaseModel):
    invoice_number: str = Field(description="The unique invoice number"),
    vendor_name: str = Field(description="The vendor name"),
    total_amount: int = Field(description="Total amount of the invoice"),
    due_date: str = Field(description="Due date to be paid")

llama_extract = LlamaExtract()
extractor = llama_extract.create_agent(name="invoice-extractor", data_schema=InvoiceSchema)

*# LlamaExtract parses the document first, then extracts fields*
result = extractor.extract("invoice.pdf")
```




 This layered approach means you get the parsing quality of LlamaParse automatically applied, with extraction intelligence added on top. LlamaExtract ensures type-safe outputs that match your schema, making it ideal for feeding downstream systems.



##  The Bottom Line



 **Parse when you need understanding.** If users can ask unpredictable questions, when context matters, when you&#39;re enabling search and discovery: parse to preserve the full document intelligence.



 **Extract when you need data.** When you know exactly what fields you need, when you&#39;re feeding databases or workflows, when consistency and validation matter: extract to get structured, actionable information.



 **Use both when you need intelligence and integration.** Most sophisticated document processing systems combine parsing for flexibility and extraction for efficiency.



 The choice isn&#39;t about which approach is &quot;better.&quot; It&#39;s about matching your approach to your specific use case. Both are powerful tools in the document processing toolkit. Understanding when to use each is the key to building effective systems.



 **Ready to implement?** Whether you&#39;re building RAG applications, automating workflows, or doing both, understanding the parse vs. extract distinction will guide you toward the right architecture for your needs.