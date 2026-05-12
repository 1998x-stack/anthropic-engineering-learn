---
title: "Introducing OpenTelemetry support for LangSmith"
author: "LangChain Accounts"
date: "2024-12-09"
url: "https://www.langchain.com/blog/opentelemetry-langsmith"
---

Company AnnouncementsLangSmithPartner

# Introducing OpenTelemetry support for LangSmith

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamDecember 9, 2024![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)5min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbae3157c432b84a72abf9_Youtube-and-Blog-Self-Serve-Components--2-.png)LangSmith now supports ingesting traces in OpenTelemetry format, an open standard for distributed tracing and observability. [OpenTelemetry](https://opentelemetry.io/docs/what-is-opentelemetry/?ref=blog.langchain.com) allows developers to instrument and export telemetry data  across a wide range of programming languages, frameworks, and monitoring tools for broad interoperability.

With this update, LangSmith’s API layer can now accept OpenTelemetry traces directly. You can point any supported OpenTelemetry exporter to the LangSmith OTEL endpoint, and your traces will be ingested and fully accessible within LangSmith — giving a complete view of your application’s performance with unified [LLM monitoring](https://www.langchain.com/articles/llm-monitoring-observability) and system telemetry.

## **OpenTelemetry semantic conventions**

OpenTelemetry defines [semantic conventions](https://opentelemetry.io/docs/concepts/semantic-conventions/?ref=blog.langchain.com) for attribute names and data across various use cases. For example, there are semantic conventions for databases, messaging systems, and protocols such as HTTP or gRPC. For LangSmith, we specifically care about semantic conventions for generative AI.  As this area is new, there are a few existing conventions, but new official standards are still being developed.

We now support traces in the [OpenLLMetry](https://github.com/traceloop/openllmetry?ref=blog.langchain.com) format, a semantic convention and implementation that enables out-of-the-box instrumentation for a range of LLM models, vector databases, and common LLM frameworks.  Data must be sent with the OpenLLMetry semantic convention; you can then configure an OpenTelemetry-compatible SDK to point to LangSmith’s OTEL endpoint to ingest traces into LangSmith.

We plan to support accepting traces via other semantic conventions such as the [OpenTelemetry Gen AI semantic convention](https://opentelemetry.io/docs/specs/semconv/gen-ai/?ref=blog.langchain.com) as they evolve.

Below, we’ll walk through a few different ways to get started.

## **Getting started with an OpenTelemetry based client**

This example covers using the off the shelf OpenTelemetry Python client. Note that this approach would work with any OpenTelemetry compatible SDK in the language of your choice.  

First, install Python dependencies:

`pip install openai
pip install opentelemetry-sdk
pip install opentelemetry-exporter-otlp
`

Next, configure your environment variables for OpenTelemetry:

`OTEL_EXPORTER_OTLP_ENDPOINT=https://api.smith.langchain.com/otel
OTEL_EXPORTER_OTLP_HEADERS=&quot;x-api-key=&lt;your langsmith api key&gt;,LANGSMITH_PROJECT=&lt;project name&gt;&quot;
`

Then run the following code which calls `openai` and wraps that with a span along with the required attributes:

`from openai import OpenAI
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
)
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter

client = OpenAI()
otlp_exporter = OTLPSpanExporter()
trace.set_tracer_provider(TracerProvider())
trace.get_tracer_provider().add_span_processor(
    BatchSpanProcessor(otlp_exporter)
)
tracer = trace.get_tracer(__name__)

def call_openai():
    model = &quot;gpt-4o-mini&quot;
    with tracer.start_as_current_span(&quot;call_open_ai&quot;) as span:
        span.set_attribute(&quot;langsmith.span.kind&quot;, &quot;LLM&quot;)
        span.set_attribute(&quot;langsmith.metadata.user_id&quot;, &quot;user_123&quot;)
        span.set_attribute(&quot;gen_ai.system&quot;, &quot;OpenAI&quot;)
        span.set_attribute(&quot;gen_ai.request.model&quot;, model)
        span.set_attribute(&quot;llm.request.type&quot;, &quot;chat&quot;)

        messages = [
            {&quot;role&quot;: &quot;system&quot;, &quot;content&quot;: &quot;You are a helpful assistant.&quot;},
            {
                &quot;role&quot;: &quot;user&quot;,
                &quot;content&quot;: &quot;Write a haiku about recursion in programming.&quot;
            }
        ]

        for i, message in enumerate(messages):
            span.set_attribute(f&quot;gen_ai.prompt.{i}.content&quot;, str(message[&quot;content&quot;]))
            span.set_attribute(f&quot;gen_ai.prompt.{i}.role&quot;, str(message[&quot;role&quot;]))

        completion = client.chat.completions.create(
            model=model,
            messages=messages
        )

        span.set_attribute(&quot;gen_ai.response.model&quot;, completion.model)
        span.set_attribute(&quot;gen_ai.completion.0.content&quot;, str(completion.choices[0].message.content))
        span.set_attribute(&quot;gen_ai.completion.0.role&quot;, &quot;assistant&quot;)
        span.set_attribute(&quot;gen_ai.usage.prompt_tokens&quot;, completion.usage.prompt_tokens)
        span.set_attribute(&quot;gen_ai.usage.completion_tokens&quot;, completion.usage.completion_tokens)
        span.set_attribute(&quot;gen_ai.usage.total_tokens&quot;, completion.usage.total_tokens)

        return completion.choices[0].message

if __name__ == &quot;__main__&quot;:
    call_openai()
`

You should see a trace in your LangSmith dashboard like [this one](https://smith.langchain.com/public/4f2890b1-f105-44aa-a6cf-c777dcc27a37/r?ref=blog.langchain.com).

For more information, see the [documentation](https://docs.smith.langchain.com/observability/how_to_guides/tracing/trace_with_opentelemetry?ref=blog.langchain.com).

## **Getting started with Traceloop SDK**

This example covers sending tracing using the OpenLLMetry SDK from Traceloop, which supports a wide range of integrations of models, vector databases, and frameworks out of the box.

To get started, follow these steps. First, install the OpenLLMetry Traceloop SDK:

`pip install traceloop-sdk`

Set up your environment variables:

`TRACELOOP_BASE_URL=https://api.smith.langchain.com/otel
TRACELOOP_HEADERS=x-api-key=&lt;your_api_key&gt;`

Then initialize the SDK:

`from traceloop.sdk import Traceloop
Traceloop.init()`

Here is a complete example using an OpenAI chat completion:

`import os
from openai import OpenAI
from traceloop.sdk import Traceloop

client = OpenAI(api_key=os.getenv(&quot;OPENAI_API_KEY&quot;))
Traceloop.init()

completion = client.chat.completions.create(
    model=&quot;gpt-4o-mini&quot;,
    messages=[
        {&quot;role&quot;: &quot;system&quot;, &quot;content&quot;: &quot;You are a helpful assistant.&quot;},
        {
            &quot;role&quot;: &quot;user&quot;,
            &quot;content&quot;: &quot;Write a haiku about recursion in programming.&quot;
        }
    ]
)

print(completion.choices[0].message)
`

 You should see a trace in your LangSmith dashboard like [this one](https://smith.langchain.com/public/106f5bed-edca-4357-91a5-80089252c9ed/r?ref=blog.langchain.com).

For more information, see the [documentation](https://docs.smith.langchain.com/observability/how_to_guides/tracing/trace_with_opentelemetry?ref=blog.langchain.com#logging-traces-with-the-traceloop-sdk).

## **Getting started with Vercel AI SDK**

We support the Vercel AI SDK integration using a client side trace exporter that is defined by the LangSmith library. To use this integration: first, install the AI SDK package:

`npm install ai @ai-sdk/openai zod`

Next, configure your environment:

`export LANGCHAIN_TRACING_V2=true
export LANGCHAIN_API_KEY=&lt;your-api-key&gt;
# The below examples use the OpenAI API, though it&#x27;s not necessary in general
export OPENAI_API_KEY=&lt;your-openai-api-key&gt;`

First, create an *instrumentation.js* file in your project root. Learn more about how to setup OpenTelemetry instrumentation within your Next.js app [here](https://nextjs.org/docs/app/api-reference/file-conventions/instrumentation?ref=blog.langchain.com).

`import { registerOTel } from &quot;@vercel/otel&quot;;
import { AISDKExporter } from &quot;langsmith/vercel&quot;;
export function register() {
  registerOTel({
    serviceName: &quot;langsmith-vercel-ai-sdk-example&quot;,
    traceExporter: new AISDKExporter(),
  });
}`

Afterwards, add the experimental_telemetry argument to your AI SDK calls that you want to trace. For convenience, we&#x27;ve included the AISDKExporter.getSettings() method which appends additional metadata for LangSmith.

`import { AISDKExporter } from &quot;langsmith/vercel&quot;;
import { streamText } from &quot;ai&quot;;
import { openai } from &quot;@ai-sdk/openai&quot;;
await streamText({
  model: openai(&quot;gpt-4o-mini&quot;),
  prompt: &quot;Write a vegetarian lasagna recipe for 4 people.&quot;,
  experimental_telemetry: AISDKExporter.getSettings(),
});`

You should see a trace in your LangSmith dashboard [like this one](https://smith.langchain.com/public/a9d9521a-4f97-4843-b1e2-b87c3a125503/r?ref=blog.langchain.com).

For more information, see the LangSmith documentation for the [Vercel AI SDK integration](https://docs.smith.langchain.com/observability/how_to_guides/tracing/trace_with_vercel_ai_sdk?ref=blog.langchain.com).

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc07193192cebc73980fd3_logo%20and%20title%20-%2020%20characters%20max%20(6).png)PartnerDeep Agents

#### Building a company due diligence agent with Deep Agents, LangSmith and Parallel

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01c6959ca5fd924ab432_MattHarris.jpg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01b812793b72539057d5_nick%20headshot.jpeg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd2d50cd0f84dacf92e7b_ProfilePic.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd29baf4c28709e2566a7_headshot.jpg)Matt HarrisNick MartitschSrimanth TangedipalliKaran SinghMay 8, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)9min[](/blog/building-a-company-due-diligence-agent-with-deep-agents-langsmith-and-parallel)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef82f01e90bfdf3e83a25e_Blog-02.png)Company Announcements

#### Interrupt Preview: Meet the MC

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Becca WengApril 28, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/interrupt-preview-meet-the-mc)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef96ff74c638e982ff68c6_86%20(1).png)Agent ArchitectureLangSmithOpen Source

#### How LangSmith and LangChain OSS Help You Meet EU AI Act Requirements

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0003a1af368dfae13c23c_jacob-talbot.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Jacob TalbotBecca WengApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/langsmith-langchain-oss-eu-ai-act)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)