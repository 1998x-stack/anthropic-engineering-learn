---
title: "Document Agents Workflow Automation Guide | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/automate-workflows-with-document-agents-a-complete-tutorial-to-building-context-aware-AI"
category: "document-processing"
---

Content



- [ Step 1: Install Dependencies and Set Up API Keys  ](#step-1-install-dependencies-and-set-up-api-keys)
- [ Step 2: Create and Connect to Your LlamaParse Index  ](#step-2-create-and-connect-to-your-llamaparse-index)
- [ Step 3: Test Your Index with Basic Retrieval  ](#step-3-test-your-index-with-basic-retrieval)
- [ Step 4: Add an LLM and Create a Query Engine  ](#step-4-add-an-llm-and-create-a-query-engine)
- [ Step 5: Build Tools for Your Agent  ](#step-5-build-tools-for-your-agent)
- [ Step 6: Create Your Agent with Workflows  ](#step-6-create-your-agent-with-workflows)
- [ Step 7: Test with a Complex, Real-World Question  ](#step-7-test-with-a-complex-real-world-question)
- [ Key Features Demonstrated  ](#key-features-demonstrated)
- [ Conclusion: From Static PDFs to Intelligent Agents  ](#conclusion-from-static-pdfs-to-intelligent-agents)



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







 Enterprise documents—like bank statements, contracts, and disclosures—are dense, complex, and often packed with valuable information that&#39;s difficult to access at scale. Traditional document processing tools struggle to go beyond basic extraction.



 With LlamaParse Index, we&#39;re enabling a new paradigm: seamlessly parse and index unstructured documents, retrieve relevant context, and plug it directly into AI agents using LlamaIndex&#39;s open-source agentic framework. In this tutorial, we&#39;ll walk through how to set up your first LlamaParse Index and use it in a fully functional AI agent.



 We&#39;ll be working with a challenging real-world dataset: a collection of deposit account disclosures and rate agreements from JPMorgan Chase.



 The goal? Build an agent that can intelligently reason over the documents to answer complex banking questions—like calculating overdraft fees based on user behavior.



 👉 You can follow along in the [official documentation](https://docs.cloud.llamaindex.ai/llamacloud/how_to/getting-started-with-index)



 🎥 Or watch the [video tutorial](https://youtu.be/fx4SeNc3RZE?feature=shared)



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



##  **Step 1: Install Dependencies and Set Up API Keys**



 Start by installing the required dependencies:



sh






```
!pip install llama-index-indices-managed-llama-cloud llama-index-llms-anthropic llama-index-core
```
    You&#39;ll need two API keys to get started:


-  **LLAMACLOUD_API_KEY** - to access your LlamaParse index
  -  **ANTHROPIC_API_KEY** - to access Claude for powering your agent



##  **Step 2: Create and Connect to Your LlamaParse Index**



 First, create your index in the LlamaParse dashboard by uploading your documents (Chase account PDFs in this case). Then connect to it using the LlamaIndex SDK:



python






```
from llama_index.indices.managed.llama_cloud import LlamaParseIndex

index = LlamaParseIndex(
    name="demo-video-index-1",
    project_name="Demo Project",
    organization_id="your-organization-id",
    api_key=LLAMACLOUD_API_KEY
)
```


##  **Step 3: Test Your Index with Basic Retrieval**

  Verify that your index is working by running a basic retrieval test:



python






```
query = "What is the monthly service fee for Chase Total Checking"
nodes = index.as_retriever().retrieve(query)

print("Found " + str(len(nodes)) + " nodes")
for node in nodes:
    print(f"Node ID: {node.node.id_}")
    print(f"Score: {node.score}")
    print(f"File Name: {node.node.metadata.get('file_name')}")
    print(f"Page Label: {node.node.metadata.get('page_label')}")
    print("-" * 20)
```
    This returns raw *nodes*—chunks of document text from relevant pages—but no final answer yet. To get actual answers, we need to integrate an LLM.



##  **Step 4: Add an LLM and Create a Query Engine**



 Integrate Claude Sonnet 4 as your language model:



python






```
from llama_index.llms.anthropic import Anthropic

llm = Anthropic(
    api_key=ANTHROPIC_API_KEY,
    model="claude-sonnet-4-20250514",
)
```
    Create a query engine and ask the same question:



python






```
engine = index.as_query_engine(llm=llm)
response = engine.query(query)
print(response)
```
    Output:



>  The monthly service fee for Chase Total Checking is $12 (increasing to $15, effective August 24, 2025).



 This is basic RAG (retrieval-augmented generation). Now let&#39;s build a more sophisticated agent.



##  **Step 5: Build Tools for Your Agent**



 Create tools that your agent can use:



 1.** A simple calculator tool:**



python






```
Output:

> The monthly service fee for Chase Total Checking is $12 (increasing to $15, effective August 24, 2025).
>

This is basic RAG (retrieval-augmented generation). Now let's build a more sophisticated agent.

## **Step 5: Build Tools for Your Agent**

Create tools that your agent can use:

1. **A simple calculator tool:**
```
    2. **A query tool for the Chase documents:**



python






```
from llama_index.core.tools import QueryEngineTool

jpmorgan = QueryEngineTool.from_defaults(
    query_engine=engine,
    name="JPMorganChaseTool",
    description="Query documents about JP Morgan Chase bank rates, fees and procedures",
)
```


##  **Step 6: Create Your Agent with Workflows**

  Use LlamaIndex&#39;s FunctionAgent with the Workflows abstraction:



python






```
from llama_index.core.agent.workflow import FunctionAgent

workflow = FunctionAgent(
    tools=[add, jpmorgan],
    llm=llm,
    system_prompt="You are an expert in JP Morgan Chase banking fees and procedures"
)
```


##  **Step 7: Test with a Complex, Real-World Question**

  Now test the agent with a compound scenario that requires multiple document lookups and calculations:



python






```
from llama_index.core.agent.workflow import (
    AgentOutput,
    ToolCallResult,
)

handler = workflow.run("""You have a Chase Total Checking account with $25 in your balance on
Monday morning. Throughout Monday, you make a $15 grocery purchase (debit card),
write a $20 check that gets cashed, and have a $25 automatic utility bill payment (ACH)
that processes. On Tuesday, you request a rush replacement for your lost debit card and
place a stop payment on another check over the phone with a banker. What is the total
amount in fees you would be charged, and when would each fee be assessed?""")

# Stream the agent's reasoning process
async for event in handler.stream_events():
    if isinstance(event, AgentOutput):
        for tool_call in event.tool_calls:
            print("-" * 20)
            print("Tool called: " + tool_call.tool_name)
            print("Tool arguments:")
            for key, value in tool_call.tool_kwargs.items():
                print(f"  {key}: {value}")
            print("-" * 10)
    elif isinstance(event, ToolCallResult):
        print("Tool output: ", event.tool_output)

print(str(await handler))
```
    The agent intelligently:


-  **Queries overdraft policies** to understand when fees apply
  -  **Looks up replacement card fees** for rush delivery
  -  **Finds stop payment fees** for phone requests
  -  **Calculates total fees** using the add tool
  -  **Provides a detailed breakdown** with timing



##  **Key Features Demonstrated**



 **Smart Document Retrieval**: The agent doesn&#39;t just search—it understands context and retrieves relevant information from multiple document sections.



 **Multi-Step Reasoning**: It breaks down complex scenarios into component parts, querying different aspects of the banking policies.



 **Tool Integration**: Seamlessly combines document retrieval with calculations and business logic.



 **Streaming Execution**: You can observe the agent&#39;s thought process in real-time, seeing each tool call and reasoning step.



##  **Conclusion: From Static PDFs to Intelligent Agents**



 This tutorial demonstrates how LlamaParse and LlamaIndex transform dense, unstructured documents into actionable insights automatically. By indexing real-world data and connecting it to an event-driven, tool-using agent, you go far beyond traditional document search or basic RAG pipelines.



 The result is a system that can:


-  **Reason** across multiple document sections
  -  **Calculate** complex scenarios with precision
  -  **Adapt** its queries based on context
  -  **Explain** its reasoning transparently



 This approach works for any domain with complex documents—legal contracts, technical manuals, regulatory filings, medical records, and more.



 💡 **Want to try it yourself?**



 Check out the [complete documentation](https://docs.cloud.llamaindex.ai/llamacloud/how_to/getting-started-with-index) and [video walkthrough](https://youtu.be/Trsu_NJIfnw).



 **Ready to build your own document agents?** Start with your first LlamaParse index today and let us know how you&#39;re using agents built with LlamaIndex—we&#39;d love to feature your use case.