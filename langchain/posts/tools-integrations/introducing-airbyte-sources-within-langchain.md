---
title: "Introducing Airbyte sources within LangChain"
author: "LangChain Accounts"
date: "2023-08-22"
url: "https://www.langchain.com/blog/introducing-airbyte-sources-within-langchain"
---

Company AnnouncementsLangSmithObservability &amp; Evals

# Introducing Airbyte sources within LangChain

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamAugust 22, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)4min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1ab3fe3e9a95a55f111_5-social--7-.png)*Editor&#x27;s Note: This post was written in collaboration with the *[*Airbyte*](https://airbyte.com/?ref=blog.langchain.com)* team. They&#x27;ve made it really easy to connect even more data sources to LangChain as document loaders.*

It’s now possible to utilize the Airbyte sources for [Gong](https://python.langchain.com/docs/integrations/document_loaders/airbyte_gong?ref=blog.langchain.com), [Hubspot](https://python.langchain.com/docs/integrations/document_loaders/airbyte_hubspot?ref=blog.langchain.com), [Salesforce](https://python.langchain.com/docs/integrations/document_loaders/airbyte_salesforce?ref=blog.langchain.com), [Shopify](https://python.langchain.com/docs/integrations/document_loaders/airbyte_shopify?ref=blog.langchain.com), [Stripe](https://python.langchain.com/docs/integrations/document_loaders/airbyte_stripe?ref=blog.langchain.com), [Typeform](https://python.langchain.com/docs/integrations/document_loaders/airbyte_typeform?ref=blog.langchain.com) and [Zendesk Support](https://python.langchain.com/docs/integrations/document_loaders/airbyte_zendesk_support?ref=blog.langchain.com) directly within your LangChain-based application, implemented as [document loaders](https://python.langchain.com/docs/modules/data_connection/document_loaders/?ref=blog.langchain.com).

For example, to load the Stripe invoices for a user, you can use the AirbyteStripeLoader. Installing it is super simple, when you have LangChain installed locally you only need to install the source you are interested in, and you are ready to go:

`pip install airbyte-source-stripe`

After that, simply import the loader and pass in configuration and the stream you want to load:

`from langchain.document_loaders.airbyte import AirbyteStripeLoader
config = {
  &quot;client_secret&quot;: &quot;&lt;secret key&gt;&quot;,
  &quot;account_id&quot;: &quot;&lt;account id&gt;&quot;,
  &quot;start_date&quot;: &quot;&lt;date from which to start retrieving records from in ISO format, e.g. 2020-10-20T00:00:00Z&gt;&quot;
}
loader = AirbyteStripeLoader(config=config, stream_name=&quot;invoices&quot;)
documents = loader.load()
# use documents in vector store or otherwise
`

## Why does this matter?

This is the beginning of making Airbyte’s [300+ sources](http://docs.airbyte.com/integrations?ref=blog.langchain.com) available as document loaders in LangChain.

Airbyte can move data from just about any source to your warehouse or vector database to power your LLM use case (check out this[ tutorial](https://airbyte.com/tutorials/chat-with-your-data-using-openai-pinecone-airbyte-and-langchain?ref=blog.langchain.com) for setting up such a data pipeline!). This is normally done by using Airbyte Cloud or a local Airbyte instance, setting up a connection, and running it on a schedule (or via API trigger) to make sure your data stays fresh.

But if you are just getting started and are running everything locally, using a full Airbyte instance (including the UI, scheduling service, scale-out capabilities, etc..) may be overkill.

With this release, it’s easier than ever to run any Python-based source in LangChain directly within your Python runtime - no need to spin up an Airbyte instance or make API calls to Airbyte Cloud.

## Moving between hosted and embedded Airbyte

As it’s the same code running under the hood, every Airbyte-built loader is compatible with the respective source in the Airbyte service. This means it’s trivial to lift your embedded loading pipeline into your self-hosted Airbyte installation or your Airbyte Cloud instance. The shape of the configuration object and the records is 100% compatible.

Running syncs on hosted Airbyte means:

- UI to keep track of running pipelines
- Alerting on failing syncs
- Easily running pipelines on a schedule

Running syncs with LangChain loaders means:

- No overhead for running yet another service
- Full control over timing and pipeline execution

## Mapping Airbyte records to LangChain documents

By default, each record gets mapped to a Document as part of the loader, with all the various fields in the record becoming the metadata of the record. The text portion of the document is left as an empty string. You can pass in a record handler to customize this behavior to build the text part of a record depending on the data:

`def handle_record(record, id):
    return Document(page_content=record.data[&quot;title&quot;], metadata=record.data)
loader = AirbyteGongLoader(config=config, record_handler=handle_record, stream_name=&quot;calls&quot;)`

## Incremental loads

Since your python application is basically acting as the Airbyte platform, you have full control over how the “sync” is executed. For example you can still benefit from [incremental syncs](https://glossary.airbyte.com/term/incremental-synchronization/?ref=blog.langchain.com) if your stream supports it by accessing the “last_state” property of the loader. This allows you to load only documents that changed since the last time you loaded, allowing you to update an existing vector database effectively:

`import airbyte_cdk.models.airbyte_protocol import AirbyteMessage
with open(&#x27;stripe_sync_checkpoint.json&#x27;, &#x27;wb&#x27;) as file:
    file.write(loader.last_state.json())

// ... later
with open(&#x27;stripe_sync_checkpoint.json&#x27;, &#x27;r&#x27;) as file:
    current_state = AirbyteStateMessage.parse_raw(file.read())
incremental_loader = AirbyteStripeLoader(config=config, stream_name=&quot;invoices&quot;, state=current_state)
new_docs = incremental_loader.load()
`

## Custom sources

For now, the following Airbyte sources are available as pip packages (with more to come):

- [Gong](https://python.langchain.com/docs/integrations/document_loaders/airbyte_gong?ref=blog.langchain.com) pip install airbyte-source-gong
- [Hubspot](https://python.langchain.com/docs/integrations/document_loaders/airbyte_hubspot?ref=blog.langchain.com) pip install airbyte-source-hubspot
- [Salesforce](https://python.langchain.com/docs/integrations/document_loaders/airbyte_salesforce?ref=blog.langchain.com) pip install airbyte-source-salesforce
- [Shopify](https://python.langchain.com/docs/integrations/document_loaders/airbyte_shopify?ref=blog.langchain.com) pip install airbyte-source-shopify
- [Stripe](https://python.langchain.com/docs/integrations/document_loaders/airbyte_stripe?ref=blog.langchain.com) pip install airbyte-source-stripe
- [Typeform](https://python.langchain.com/docs/integrations/document_loaders/airbyte_typeform?ref=blog.langchain.com) pip install airbyte-source-typeform
- [Zendesk Support](https://python.langchain.com/docs/integrations/document_loaders/airbyte_zendesk_support?ref=blog.langchain.com) pip install airbyte-source-zendesk-support

However, if you have implemented your own custom Airbyte sources, it’s also possible to integrate them by using the AirbyteCDKLoader base class that works with the Source interface of the Airbyte CDK:

`from langchain.document_loaders.airbyte import AirbyteCDKLoader
from my_source.source import MyCustomSource # plug in your own source here
config = {
   # your custom configuration
}
loader = AirbyteCDKLoader(source_class=MyCustomSource, config=config, stream_name=&quot;my-stream&quot;)`

You can also install sources from the main Airbyte repository by installing directly via git - for example, to fetch the Github source, simply run

`pip install &quot;source_github@git+https://github.com/airbytehq/airbyte.git@master#subdirectory=airbyte-integrations/connectors/source-github&quot;`

After that, the source is available to be plucked into the AirbyteCDKLoader:

`from source_github.source import SourceGithub
issues_loader = AirbyteCDKLoader(source_class=SourceGithub, config=config, stream_name=&quot;issues&quot;)`

Check out [the connector development documentation](https://docs.airbyte.com/connector-development/?ref=blog.langchain.com) for how to get started writing your own sources - it’s easy to get started with them and will allow you to move from local embedded loaders to using a hosted Airbyte instance seamlessly depending on your needs.

## Any questions? We would love to hear from you

If you are interested in leveraging Airbyte to ship data to your LLM-based applications, [please take a moment](https://docs.google.com/forms/d/e/1FAIpQLSduobMZwbqiFlPxsWDG-hrBw6NLYMDu_7zRfo4j7AsaO1QtfQ/viewform?usp=sf_link&amp;_gl=1*m4v6ic*_ga*MTM4ODAyNjg4NS4xNjY5ODkyNDQ1*_ga_HDBMVFQGBH*MTY5MjM2MzY0Ni45NS4xLjE2OTIzNjU2NDUuMC4wLjA.&amp;ref=blog.langchain.com) to fill out our survey so we can make sure to prioritize the most important features.

If you have questions or are interested in other existing sources being exposed as loaders this way, do not hesitate to reach out on our [community slack channel](https://airbyte.com/community/community?ref=blog.langchain.com) or in the [Airbyte channel](https://discord.com/channels/1038097195422978059/1131406672972218430?ref=blog.langchain.com) on the LangChain discord server.

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