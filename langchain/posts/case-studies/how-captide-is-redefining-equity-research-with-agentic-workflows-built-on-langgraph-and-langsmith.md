---
title: "How Captide is redefining equity research with agentic workflows running on LangGraph Platform"
author: "LangChain Accounts"
date: "2025-01-20"
url: "https://www.langchain.com/blog/how-captide-is-redefining-equity-research-with-agentic-workflows-built-on-langgraph-and-langsmith"
---

Case StudiesLangGraphLangSmith

# How Captide is redefining equity research with agentic workflows running on LangGraph Platform

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamJanuary 20, 2025![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)3min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbae0ef72d73b2dc00ec06_Case-study---captide---ghost.png)[Captide’s platform](https://www.captide.co/?ref=blog.langchain.com) transforms how investment research teams work with financial data. By automating the extraction of insights and metrics from regulatory filings and investor relations documents, analysts can create customized datasets and analyses with extreme efficiency. At the heart of this innovation is their commitment to NLP workflows and its strategic integration of LangGraph and LangSmith, hosted on [LangGraph Platform](https://langchain-ai.github.io/langgraph/concepts/langgraph_platform/?ref=blog.langchain.com).

## Redefining Financial Analysis with NLP Workflows

By allowing users to articulate complex analysis tasks in natural language, [Captide](https://www.captide.co/?ref=blog.langchain.com) simplifies the process of extracting financial metrics, creating customized datasets, and uncovering contextual insights. Once the user defines their analysis tasks, Captide’s agents take over, orchestrating the entire data retrieval and processing pipeline from a big corpus of financial documents.

This seamless transition from query to actionable results redefines efficiency in financial analysis. It provides unmatched flexibility to extract company-specific metrics and insights, overcoming the fixed-schema limitations of legacy platforms, while analyzing exponentially larger volumes of investments.

To achieve this, Captide relies on the capabilities of LangGraph and LangSmith, ensuring precision, scalability, and reliable outputs that align with the stringent standards of the financial industry.

## Using LangGraph for parallel processing and structured outputs

💡

LangGraph has become indispensable in Captide’s technological stack.

The framework’s intuitive design has streamlined development, reducing the complexity of tracking agent workflows while enhancing operational efficiency. With LangGraph, Captide’s team can manage complex agentic processes, such as parallel document processing and creation of structured outputs with ease.

For example, when analyzing vast troves of regulatory filings, LangGraph’s parallel processing capabilities come into play. Multiple agents work simultaneously to execute ticker-specific vector store queries, retrieve relevant documents, and grade each document chunks. This approach not only minimizes latency but also eliminates the need to complicate the codebase with asynchronous functions.

The platform’s ability to generate structured outputs is another highlight. By leveraging LangGraph’s [trustcall](https://github.com/hinthornw/trustcall?ref=blog.langchain.com) python library, Captide ensures that users can request table outputs with their custom schemas to structure metrics found in distinct documents. Trustcall makes the output adhere strictly to predefined JSON schemas, an essential requirement for Captide’s features. This guarantees consistency and reliability, even when dealing with the most complex document sets.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbae0ff72d73b2dc00ec7e_Screenshot-2025-01-20-at-18.00.51.png)

Captide’s adoption of LangGraph Studio and CLI further enhances its development workflow. By running agents locally and integrating outputs with LangSmith, the team has created an efficient environment where rapid iterations and testing are the norm.

## Integrating LangSmith for Real-Time Insights and Improvement

For Captide, real-time monitoring and iterative enhancement are non-negotiable.

💡

LangSmith provides Captide with a robust suite of tools to track agent performance, evaluate outputs, and gather invaluable user feedback as soon as tasks are run.

Captide’s integration of LangSmith allows for precise monitoring of agent workflows, with detailed traces that highlight response times, error rates, and operational costs. This visibility ensures that the platform maintains its high standards of performance and reliability.

LangSmith has also been crucial when incorporating thumbs-up and thumbs-down options within the platform where users can directly rate the quality of outputs. This feedback is collected and analyzed, creating a growing dataset that helps refine agent behavior and improve system performance over time. With LangSmith’s evaluation tools, this feedback loop enables Captide to identify trends, address weaknesses, and continuously enhance the user experience.

## Deploying on LangGraph Platform

When LangChain launched [LangGraph Platform](https://langchain-ai.github.io/langgraph/concepts/langgraph_platform/?ref=blog.langchain.com) this summer, it was a no-brainer to deploy their cutting-edge agents on it.

With Captide&#x27;s agent built on LangGraph, it was a one-click deploy to get production-ready API endpoints for interacting with the agent. This includes endpoints for streaming as well as for getting the state of the thread at any point in time.

LangGraph Platform also contains LangGraph Studio, an IDE for visualizing and interacting with the agent once deployed. It also seamlessly integrates with LangSmith, which was a crucial part of Captide&#x27;s workflow.

For these reasons, it was an easy decision to adopt LangGraph Platform.

## Looking Ahead: The Future of Financial Analysis

As Captide continues to redefine financial analysis, its integration with LangChain remains a driving force behind its progress. The platform is poised to expand its NLP capabilities, focusing on state management and self-validation loops to enhance accuracy and reliability further.

Captide is not just transforming how financial analysts work but also setting a new standard for the industry. Built on the capabilities of LangGraph and LangSmith, Captide is paving the way for a smarter, more effective future in financial analysis.

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69efb41ab2584d1733d866c5_case-study-madrigal.png)Case Studies

#### How Madrigal Built a Flexible and Scalable Multi-Agent Research and Intelligence Platform for Pharma with LangChain and LangSmith

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69efba6c52ebbc1e377743b4_Parth.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69efba87c585b65247366c20_Ron.png)Parth PatelRon FilippoApril 29, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)11min[](/blog/customers-madrigal)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef96ff74c638e982ff68c6_86%20(1).png)Agent ArchitectureLangSmithOpen Source

#### How LangSmith and LangChain OSS Help You Meet EU AI Act Requirements

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0003a1af368dfae13c23c_jacob-talbot.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Jacob TalbotBecca WengApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/langsmith-langchain-oss-eu-ai-act)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e251cee3c69c0b64e26c79_case-study-16_9%20(1).png)Case StudiesLangSmith

#### How Credit Genie used Insights Agent to improve their AI financial assistant

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e251111d491175462a384c_david-li.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e25199461e789ce4b875a7_jeffrey-ngai.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e2518d5b449e720f9f295a_goyo-lozano-palacio.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e2515f9f57e45d15dbd331_charles-yuan.png)David LiJeffrey NgaiGoyo Lozano PalacioCharles YuanApril 20, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)5min[](/blog/credit-genie-insights-agent-financial-assistant)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)