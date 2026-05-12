---
title: "Open Source Extraction Service"
author: "LangChain Accounts"
date: "2024-03-26"
url: "https://www.langchain.com/blog/open-source-extraction-service"
---

Agent Architecture

# Open Source Extraction Service

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamMarch 26, 2024![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)7min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaffcf3571add5bca9ff6_Extraction_blog-1.png)*Earlier this month we *[*announced*](https://blog.langchain.com/use-case-accelerant-extraction-service/)* our most recent OSS use-case accelerant: a service for extracting structured data from unstructured sources, such as text and PDF documents. Today we are exposing a hosted version of the service with a simple front end. The application is free to use, but is not intended for production workloads or sensitive data. The intent is to showcase what is possible in this category in 2024, and to help developers get a running start with their own applications.*

**Key Links:**

- **YouTube Walkthrough: **[**https://youtu.be/-FMUt3OARy0**](https://youtu.be/-FMUt3OARy0?ref=blog.langchain.com)
- **Hosted Extraction Service:  **[**https://extract.langchain.com/**](https://extract.langchain.com/?ref=blog.langchain.com)** **
- **GitHub Repo: **[**https://github.com/langchain-ai/langchain-extract**](https://github.com/langchain-ai/langchain-extract?ref=blog.langchain.com)

## Why now?

Structured data extraction has emerged as a valuable use case of large language models, which can reason through the ambiguities of unstructured text to coerce information into a desired schema. Model providers are increasingly supporting long context windows and function calling capabilities, both key features to data extraction. And we have recently improved LangChain’s [support for data extraction](https://python.langchain.com/docs/use_cases/extraction/?ref=blog.langchain.com), allowing developers to easily work with a variety of file types, schema formats, models, few-shot examples, and extraction methods (e.g., tool calling, JSON mode, or parsing). Hosting a reference application allows users to experiment with the latest tools for their own use-cases, and connect what they see to the underlying [OSS implementation](https://github.com/langchain-ai/langchain-extract?ref=blog.langchain.dev).

## Features

- Support for PDF, HTML, and text;
- Defining and persisting extractors with their own schema and custom instructions;
- Adding few-shot examples for in-context learning;
- Sharing extractors among users;
- Swapping LLM models;
- A [LangServe](https://python.langchain.com/docs/langserve?ref=blog.langchain.com) endpoint for the core extraction logic, allowing it to be plugged into your own Langchain workflows;
- A frontend that lets you define extraction schemas in natural language, share with other users, and test them on text or files (no support of few shot examples yet).

## Walkthrough

Let’s walk through an example, extracting financial data from a public company earnings call. Here we use the [prepared remarks from Uber’s Q4 2023 earnings call](https://s23.q4cdn.com/407969754/files/doc_earnings/2023/q4/transcript/Uber-Q4-23-Prepared-Remarks.pdf?ref=blog.langchain.com), which Uber investor relations makes available [online](https://investor.uber.com/news-events/default.aspx?ref=blog.langchain.com).

Most public companies host earnings calls, providing their management opportunities to discuss past financial results and future plans. Natural language transcripts of these calls may contain useful information, but often this information must first be extracted from the document and arranged into a structured form so that it can be analyzed or compared across time periods and other companies.

Let’s first grab the PDF:

`import requests

pdf_url = &quot;https://s23.q4cdn.com/407969754/files/doc_earnings/2023/q4/transcript/Uber-Q4-23-Prepared-Remarks.pdf&quot;

# Get PDF bytes
pdf_response = requests.get(pdf_url)
assert(pdf_response.status_code == 200)
pdf_bytes = pdf_response.content`

Next, we will generate a unique identifier for ourselves. Our application does not manage users or include legitimate authentication. Access to extractors, few-shot examples, and other artifacts is controlled via this ID. Consider it secret, and don’t lose it!

`from uuid import uuid4

user_id = str(uuid4())
headers = {&quot;x-key&quot;: user_id}`

We next specify the schema of what we intend to extract. Here we specify a record of financial data. We allow the LLM to infer various attributes, such as the time period for the record. Here we use Pydantic for readability, but ultimately the service relies on JSON schema.

`from pydantic import BaseModel, Field

class FinancialData(BaseModel):
    name: str = Field(..., description=&quot;Name of the financial figure, such as revenue.&quot;)
    value: float = Field(..., description=&quot;Nominal earnings in local currency.&quot;)
    scale: str = Field(..., description=&quot;Scale of figure, such as MM, B, or percent.&quot;)
    period_start: str = Field(..., description=&quot;The start of the time period in ISO format.&quot;)
    period_duration: int = Field(..., description=&quot;Duration of period, in months&quot;)
    evidence: str = Field(..., description=&quot;Verbatim sentence of text where figure was found.&quot;)`

Note that we include an evidence attribute, which provides context for the predictions and supports downstream verification of the results.

Once we&#x27;ve defined our schema, we create an extractor by posting it to the application:

`url = &quot;https://extract-server-f34kggfazq-uc.a.run.app&quot;

data = {
    &quot;user_id&quot;: user_id,
    &quot;description&quot;: &quot;Financial revenues and other figures.&quot;,
    &quot;schema&quot;: FinancialData.schema(),
    &quot;instruction&quot;: (
        &quot;Extract standard financial figures, specifically earnings and &quot;
        &quot;revenue figures. Only extract historical facts, not estimates or guidance.&quot;
    )
}

response = requests.post(f&quot;{url}/extractors&quot;, json=data, headers=headers)
extractor = response.json()`

We’ve posted the extractor, which we can now access using its unique ID. We can now try the extractor on our PDF:

`result = requests.post(
    f&quot;{url}/extract&quot;,
    data={&quot;extractor_id&quot;: extractor[&quot;uuid&quot;], &quot;model_name&quot;: &quot;gpt-3.5-turbo&quot;},
    files={&quot;file&quot;: pdf_bytes},
    headers=headers,
)

result.json()`

And we get back:

`{&#x27;data&#x27;: [{&#x27;name&#x27;: &#x27;Adjusted EBITDA&#x27;,
   &#x27;scale&#x27;: &#x27;million&#x27;,
   &#x27;value&#x27;: 1300,
   &#x27;evidence&#x27;: &#x27;These strong top-line trends, combined with continued rigor on costs, translated to $1.3 billion in Adjusted EBITDA and $652 million in GAAP operating income.&#x27;,
   &#x27;period_start&#x27;: &#x27;2023-10-01&#x27;,
   &#x27;period_duration&#x27;: 3},
  {&#x27;name&#x27;: &#x27;GAAP operating income&#x27;,
   &#x27;scale&#x27;: &#x27;million&#x27;,
   &#x27;value&#x27;: 652,
   &#x27;evidence&#x27;: &#x27;These strong top-line trends, combined with continued rigor on costs, translated to $1.3 billion in Adjusted EBITDA and $652 million in GAAP operating income.&#x27;,
   &#x27;period_start&#x27;: &#x27;2023-10-01&#x27;,
   &#x27;period_duration&#x27;: 3},
  {&#x27;name&#x27;: &#x27;Revenue&#x27;,
   &#x27;scale&#x27;: &#x27;billion&#x27;,
   &#x27;value&#x27;: 9.9,
   &#x27;evidence&#x27;: &#x27;We grew our revenue by 13% YoY on a constant-currency basis to $9.9 billion.&#x27;,
   &#x27;period_start&#x27;: &#x27;2023-10-01&#x27;,
   &#x27;period_duration&#x27;: 3},
  {&#x27;name&#x27;: &#x27;Adjusted EBITDA&#x27;,
   &#x27;scale&#x27;: &#x27;$&#x27;,
   &#x27;value&#x27;: 1.26,
   &#x27;evidence&#x27;: &#x27;We expect Adjusted EBITDA of $1.26 billion to $1.34 billion.&#x27;,
   &#x27;period_start&#x27;: &#x27;2023-01-01&#x27;,
   &#x27;period_duration&#x27;: 12},
  {&#x27;name&#x27;: &#x27;Adjusted EBITDA&#x27;,
   &#x27;scale&#x27;: &#x27;$&#x27;,
   &#x27;value&#x27;: 1.34,
   &#x27;evidence&#x27;: &#x27;We expect Adjusted EBITDA of $1.26 billion to $1.34 billion.&#x27;,
   &#x27;period_start&#x27;: &#x27;2023-01-01&#x27;,
   &#x27;period_duration&#x27;: 12}]}`

Note that the formatting of the result has deviated in some ways from the descriptions in the schema– for example, we output “million” and “billion” instead of “MM” or “B” as instructed. Different models will struggle with this to varying degrees. Before reaching for a larger model, a judicious choice of few-shot examples can often be an efficient way to clarify our intent. Let’s add one to our extractor:

`examples = [
    {
        &quot;text&quot;: &quot;In 2022, Revenue was $1 million and EBIT was $2M.&quot;,
        &quot;output&quot;: [
            FinancialData(
                name=&quot;revenue&quot;,
                value=1,
                scale=&quot;MM&quot;,
                period_start=&quot;2022-01-01&quot;,
                period_duration=12,
                evidence=&quot;In 2022, Revenue was $1 million and EBIT was $2M.&quot;,
            ).dict(),
            FinancialData(
                name=&quot;ebit&quot;,
                value=2,
                scale=&quot;MM&quot;,
                period_start=&quot;2022-01-01&quot;,
                period_duration=12,
                evidence=&quot;In 2022, Revenue was $1 million and EBIT was $2M.&quot;,
            ).dict()
        ],
    },
]

responses = []
for example in examples:
    create_request = {
        &quot;extractor_id&quot;: extractor[&quot;uuid&quot;],
        &quot;content&quot;: example[&quot;text&quot;],
        &quot;output&quot;: example[&#x27;output&#x27;],
    }
    response = requests.post(f&quot;{url}/examples&quot;, json=create_request, headers=headers)
    responses.append(response)
`

Here we add a single example that contains two records, with updated casing for the “name” field and formatting of the “scale” field. Re-running the extraction on the document, we recover the intended formatting:

`result = requests.post(
    f&quot;{url}/extract&quot;,
    data={&quot;extractor_id&quot;: extractor[&quot;uuid&quot;], &quot;model_name&quot;: &quot;gpt-3.5-turbo&quot;},
    files={&quot;file&quot;: pdf_bytes},
    headers=headers,
)

result.json()
`

And we get:

`{&#x27;data&#x27;: [{&#x27;name&#x27;: &#x27;adjusted ebitda&#x27;,
   &#x27;scale&#x27;: &#x27;MM&#x27;,
   &#x27;value&#x27;: 1300.0,
   &#x27;evidence&#x27;: &#x27;These strong top-line trends, combined with continued rigor on costs, translated to $1.3 billion in Adjusted EBITDA and $652 million in GAAP operating income.&#x27;,
   &#x27;period_start&#x27;: &#x27;2023-10-01&#x27;,
   &#x27;period_duration&#x27;: 3},
  {&#x27;name&#x27;: &#x27;gaap operating income&#x27;,
   &#x27;scale&#x27;: &#x27;MM&#x27;,
   &#x27;value&#x27;: 652.0,
   &#x27;evidence&#x27;: &#x27;These strong top-line trends, combined with continued rigor on costs, translated to $1.3 billion in Adjusted EBITDA and $652 million in GAAP operating income.&#x27;,
   &#x27;period_start&#x27;: &#x27;2023-10-01&#x27;,
   &#x27;period_duration&#x27;: 3},
  {&#x27;name&#x27;: &#x27;gross bookings&#x27;,
   &#x27;scale&#x27;: &#x27;B&#x27;,
   &#x27;value&#x27;: 37.6,
   &#x27;evidence&#x27;: &#x27;Gross Bookings growth accelerated to 21% YoY on a constant-currency basis (23% excluding Freight), as we generated Gross Bookings of $37.6 billion.&#x27;,
   &#x27;period_start&#x27;: &#x27;2023-10-01&#x27;,
   &#x27;period_duration&#x27;: 3},
  {&#x27;name&#x27;: &#x27;revenue&#x27;,
   &#x27;scale&#x27;: &#x27;B&#x27;,
   &#x27;value&#x27;: 9.9,
   &#x27;evidence&#x27;: &#x27;We grew our revenue by 13% YoY on a constant-currency basis to $9.9 billion.&#x27;,
   &#x27;period_start&#x27;: &#x27;2023-10-01&#x27;,
   &#x27;period_duration&#x27;: 3},
  {&#x27;name&#x27;: &#x27;adjusted ebitda&#x27;,
   &#x27;scale&#x27;: &#x27;B&#x27;,
   &#x27;value&#x27;: 1.3,
   &#x27;evidence&#x27;: &#x27;We expect Adjusted EBITDA of $1.26 billion to $1.34 billion.&#x27;,
   &#x27;period_start&#x27;: &#x27;2023-01-01&#x27;,
   &#x27;period_duration&#x27;: 12}],
 &#x27;content_too_long&#x27;: False}`

### LangServe client

A final note: because we’ve hosted the core extraction logic with LangServe, we can access it via the [RemoteRunnable](https://python.langchain.com/docs/langserve?ref=blog.langchain.com#client) interface and plug it into larger chains and agent workflows.

The [runnable](https://python.langchain.com/docs/expression_language/interface?ref=blog.langchain.com) can be invoked in the usual way:

`from langserve import RemoteRunnable

runnable = RemoteRunnable(f&quot;{url}/extract_text/&quot;)
response = runnable.invoke(
    {
        &quot;text&quot;: &quot;Our 2023 revenue was $100.&quot;,
        &quot;schema&quot;: FinancialData.schema(),
    }
)
print(response)`

And we get:

`{&#x27;data&#x27;: [{&#x27;name&#x27;: &#x27;revenue&#x27;,
   &#x27;value&#x27;: 100,
   &#x27;scale&#x27;: &#x27;$&#x27;,
   &#x27;period_start&#x27;: &#x27;2023-01-01&#x27;,
   &#x27;period_duration&#x27;: 12,
   &#x27;evidence&#x27;: &#x27;Our 2023 revenue was $100.&#x27;}]}`

Or below, we incorporate it into a retrieval scenario. Here, instead of extracting directly on the input, we index some documents and treat the input as a search query. Searching for “rev”, below, will retrieve a document containing revenue and restrict the extraction to it:

`from operator import itemgetter

from langchain_community.vectorstores import FAISS
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import OpenAIEmbeddings

doc_contents = [&quot;Our 2023 revenue was $100&quot;, &quot;Our Q1 profit was $10 in 2023.&quot;]
vectorstore = FAISS.from_texts(doc_contents, embedding=OpenAIEmbeddings())
retriever = vectorstore.as_retriever()

larger_runnable = (
    {
        &quot;text&quot;: itemgetter(&quot;text&quot;) | retriever | (lambda docs: docs[0].page_content),  # fetch content of top doc,
        &quot;schema&quot;: itemgetter(&quot;schema&quot;),
    }
    | runnable
)
larger_runnable.invoke({&quot;text&quot;: &quot;rev&quot;, &quot;schema&quot;: FinancialData.schema()})`

Which yields:

`{&#x27;data&#x27;: [{&#x27;name&#x27;: &#x27;revenue&#x27;,
   &#x27;value&#x27;: 100,
   &#x27;scale&#x27;: &#x27;$&#x27;,
   &#x27;period_start&#x27;: &#x27;2023-01-01&#x27;,
   &#x27;period_duration&#x27;: 12,
   &#x27;evidence&#x27;: &#x27;Our 2023 revenue was $100&#x27;}]}`

We are excited to see what extraction workflows you build, and welcome both feedback on and contributions to LangChain’s extraction capabilities!

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69f20536df00c0eb15eab1d3_blue-77%20characters%20max.png)Deep AgentsAgent ArchitectureOpen Source

#### Tuning Deep Agents to Work Well with Different Models

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcefac505b6b48827abf84_vivek-trivedy.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcf032ce65a32e276a4d0a_mason-daugherty.png)Vivek TrivedyMason DaughertyApril 29, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)5min[](/blog/tuning-deep-agents-different-models)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef96ff74c638e982ff68c6_86%20(1).png)Agent ArchitectureLangSmithOpen Source

#### How LangSmith and LangChain OSS Help You Meet EU AI Act Requirements

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0003a1af368dfae13c23c_jacob-talbot.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Jacob TalbotBecca WengApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/langsmith-langchain-oss-eu-ai-act)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e23754937c2f749d12bb0b_76%20(1).png)Agent ArchitecturePartner

#### Agentic Engineering: How Swarms of AI Agents Are Redefining Software Engineering

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e234176723e6111407b935_renuka-kumar.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e23427e77d2631610e5d62_Prashanth-Ramagopal.png)Renuka KumarPrashanth RamagopalApril 17, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)11min[](/blog/agentic-engineering-redefining-software-engineering)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)