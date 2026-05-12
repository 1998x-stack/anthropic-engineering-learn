---
title: "Introducing End-to-End OpenTelemetry Support in LangSmith"
author: "LangChain Accounts"
date: "2025-03-27"
url: "https://www.langchain.com/blog/end-to-end-opentelemetry-langsmith"
---

Company AnnouncementsLangSmith

# Introducing End-to-End OpenTelemetry Support in LangSmith

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamMarch 26, 2025![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)4min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbadd157c432b84a7269fd_Theme-Fractal-Matrix--Format-Blog--Colour-Green--Text-Alignment-Centred--With-Image-Text-Only.png)Observability is critical for debugging and optimizing LLM applications — but until now, getting a complete view of your system meant juggling multiple tools and formats. Now, LangSmith offers full end-to-end OpenTelemetry support for applications built on LangChain and/or LangGraph.

With our OpenTelemetry (OTel) integration, you can standardize tracing across your stack and send traces to LangSmith — our testing &amp; observability platform for the agent lifecycle — or other observability platforms.

Previously, LangSmith supported OpenTelemetry as only a backend trace ingestion format. With this update, we’re completing the picture by adding native OpenTelemetry support directly into the LangSmith SDK.

## **Why OpenTelemetry for LLM applications?**

OpenTelemetry (OTel) is an open-source observability framework  that standardizes how telemetry data is collected, exported, and analyzed. As applications grow more complex and distributed, OpenTelemetry provides a consistent way to track performance, understand system behavior, and troubleshoot issues.

For LLM applications, observability presents unique challenges. Traditional application monitoring focuses on errors and compliance with expected behaviors — however, [LLM observability](https://www.langchain.com/articles/llm-monitoring-observability?ref=blog.langchain.com) requires understanding multi-step workflows and monitoring dynamic, stochastic outputs with complex [evaluation metrics](https://www.langchain.com/articles/llm-evaluation-metrics) that go beyond simple error rates.

OpenTelemetry addresses these challenges by providing a unified, vendor-neutral standard for instrumentation that works across different languages, frameworks, and backends.

## **How our OpenTelemetry Pipeline Works**

With this update, LangSmith now offers a complete OpenTelemetry pipeline for LLM applications:

- **LangChain instrumentation**: Automatically generate detailed traces from your LangChain or LangGraph applications
- **LangSmith SDK**: Convert and transport these traces through our SDK using OpenTelemetry&#x27;s standardized format
- **LangSmith platform**: Ingest and visualize traces in a powerful, LLM-specific observability dashboard

This end-to-end integration unlocks several key benefits:

- **Unified observability**: View your entire application stack—from LangChain components to underlying infrastructure—in a single, cohesive view
- **Distributed tracing**: Follow requests as they move through your microservices architecture, with context propagation ensuring that related spans are linked to the same trace
- **Interoperability**: Connect LangSmith with your existing observability tools and infrastructure through the OpenTelemetry standard, including platforms like Datadog, Grafana, and Jaeger.

With this integration, you can trace the complete execution path of your LLM applications, from the initial prompt to the final response, with detailed visibility into each step along the way.

## **Getting Started with OpenTelemetry in LangSmith**

### **1. Installation**[**​**](https://docs.smith.langchain.com/observability/how_to_guides/trace_langchain_with_otel?ref=blog.langchain.com#1-installation)

Install the LangSmith package with OpenTelemetry support:

`pip install &quot;langsmith[otel]&quot;
pip install langchain`

### **2. Enable the OpenTelemetry integration**[**​**](https://docs.smith.langchain.com/observability/how_to_guides/trace_langchain_with_otel?ref=blog.langchain.com#2-enable-the-opentelemetry-integration)

You can enable the OpenTelemetry integration by setting the LANGSMITH_OTEL_ENABLED environment variable:

`LANGSMITH_OTEL_ENABLED=true
LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT=https://api.smith.langchain.com
LANGSMITH_API_KEY=&lt;your_langsmith_api_key&gt;`

### **3. Create a LangChain application with tracing**[**​**](https://docs.smith.langchain.com/observability/how_to_guides/trace_langchain_with_otel?ref=blog.langchain.com#3-create-a-langchain-application-with-tracing)

Here&#x27;s a simple example showing how to use the OpenTelemetry integration with LangChain:

`import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# LangChain will automatically use OpenTelemetry to send traces to LangSmith
# because the LANGSMITH_OTEL_ENABLED environment variable is set

# Create a chain
prompt = ChatPromptTemplate.from_template(&quot;Tell me a joke about {topic}&quot;)
model = ChatOpenAI()
chain = prompt | model

# Run the chain
result = chain.invoke({&quot;topic&quot;: &quot;programming&quot;})
print(result.content)`

### **4. View the traces in LangSmith**[**​**](https://docs.smith.langchain.com/observability/how_to_guides/trace_langchain_with_otel?ref=blog.langchain.com#4-view-the-traces-in-langsmith)

Once your application runs, you&#x27;ll see the traces in your LangSmith dashboard [like this one](https://smith.langchain.com/public/a762af6c-b67d-4f22-90a0-728df16baeba/r?ref=blog.langchain.com).

## **Performance Considerations**

While our end-to-end OpenTelemetry support provides maximum flexibility and interoperability, it comes with slightly higher overhead compared to LangSmith’s native tracing format.

For users that are exclusively using LangSmith as their observability platform, we still recommend our native tracing format for optimal performance. It offers realtime tracing with pending runs, faster ingest speeds, and reduced memory overhead from the sdk.

The native LangSmith tracing format has been specifically designed for LLM applications and offers several key advantages. It features significantly reduced overhead with a lower computational and memory footprint compared to the more general-purpose OpenTelemetry format. Our native format is also custom-tailored for the unique data patterns and volumes found in LLM applications.

## **Try it today**

Ready to get started tracing your LangChain and LangGraph applications with OpenTelemetry? Check out our [full documentation](https://docs.smith.langchain.com/observability/how_to_guides/trace_langchain_with_otel?ref=blog.langchain.com) for more details and examples — and [try out LangSmith](https://smith.langchain.com/?ref=blog.langchain.com) for free if you haven&#x27;t already.

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef82f01e90bfdf3e83a25e_Blog-02.png)Company Announcements

#### Interrupt Preview: Meet the MC

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Becca WengApril 28, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/interrupt-preview-meet-the-mc)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef96ff74c638e982ff68c6_86%20(1).png)Agent ArchitectureLangSmithOpen Source

#### How LangSmith and LangChain OSS Help You Meet EU AI Act Requirements

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0003a1af368dfae13c23c_jacob-talbot.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Jacob TalbotBecca WengApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/langsmith-langchain-oss-eu-ai-act)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef66604a47f5049293bcf6_april-newsletter-blog.png)Company Announcements

#### April 2026: LangChain Newsletter

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/april-2026-langchain-newsletter)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)