---
title: "Airbyte Sources in LlamaIndex: Setup Guide | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/introducing-airbyte-sources-within-llamaindex-42209071722f"
category: "llamaindex-core"
---

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







Authored by Joe Reuter, Software Engineer at Airbyte

(cross-posted from the Airbyte blog; check it out [here](https://airbyte.com/blog/introducing-airbyte-sources-within-llamaindex)!)

# Content

It’s now possible to utilize the Airbyte sources for [Gong](https://llamahub.ai/l/airbyte_gong), [Hubspot](https://llamahub.ai/l/airbyte_hubspot), [Salesforce](https://llamahub.ai/l/airbyte_salesforce), [Shopify](https://llamahub.ai/l/airbyte_shopify), [Stripe](https://llamahub.ai/l/airbyte_stripe), [Typeform](https://llamahub.ai/l/airbyte_typeform) and [Zendesk Support](https://llamahub.ai/l/airbyte_zendesk_support) directly within your LlamaIndex-based application, implemented as [data loaders](https://gpt-index.readthedocs.io/en/latest/core_modules/data_modules/connector/usage_pattern.html).



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



For example, to load the Stripe invoices for a user, you can use the AirbyteStripeLoader. Installing it is super simple, when you have LlamaIndex installed locally you only need to install the source you are interested in, and you are ready to go:

pip install airbyte-source-stripe
pip install llama-hubAfter that, simply download the loader and pass in configuration and the stream you want to load:

from llama_hub.airbyte_stripe.base import AirbyteStripeReader

config = {
  "client_secret": "&amp;lt;secret key&amp;gt;",
  "account_id": "&amp;lt;account id&amp;gt;",
  "start_date": "&amp;lt;date from which to start retrieving records from in ISO format, e.g. 2020–10–20T00:00:00Z&amp;gt;"
}
reader = AirbyteStripeReader(config=config)
documents = reader.load_data(stream_name="invoices")

# Why does this matter?

This is the beginning of making Airbyte’s [300+ sources](http://docs.airbyte.com/integrations) available as data loaders in LlamaHub.

Airbyte can move data from just about any source to your warehouse or vector database to power your LLM use case (check out this[ tutorial](https://airbyte.com/tutorials/chat-with-your-data-using-openai-pinecone-airbyte-and-langchain) for setting up such a data pipeline!). This is normally done by using Airbyte Cloud or a local Airbyte instance, setting up a connection, and running it on a schedule (or via API trigger) to make sure your data stays fresh.

But if you are just getting started and are running everything locally, using a full Airbyte instance (including the UI, scheduling service, scale-out capabilities, etc..) may be overkill.

With this release, it’s easier than ever to run any Python-based source in LlamaIndex directly within your Python runtime — no need to spin up an Airbyte instance or make API calls to Airbyte Cloud.

# Moving between hosted and embedded Airbyte

Since the same code is running under the hood, every Airbyte-built loader is compatible with the respective source in the Airbyte service. This means it’s trivial to lift your embedded loading pipeline into your self-hosted Airbyte installation or your Airbyte Cloud instance. The schema of the loader configuration object and that of the output records is 100% compatible.

Running syncs on hosted Airbyte means:

- UI to keep track of running pipelines
- Event notifications including alerting on failing syncs or running post-sync operations
- Easily running pipelines on a schedule
- Scale-out capabilities
- API to power programmatic use cases
- Out-of-the-box state management of your connections
- Support
- And more

Running syncs with LlamaIndex loaders means:

- No overhead for running yet another service
- Full control over timing and pipeline execution

# Combining Airbyte loaders with indices and query engines

As Airbyte loaders are behaving like regular loaders, they can easily be combined with all LlamaIndex utilities to build powerful LLM-based applications:

relevant_keys = ["customer_name", "total", "currency"]
reader = AirbyteStripeReader(
    config=strip_config,
    record_handler=lambda record, id: Document(
        doc_id=id,
        text=record.data["description"] or "",
        extra_info={
            key: record.data[key] for key in relevant_keys if key in record.data
        },
    ),
)

index = ListIndex.from_documents(reader.load_data(stream_name="invoices"))
query_engine = index.as_query_engine()
question = input("What do you want to know about your customers?")
print(query_engine.query(question))

# Incremental loads

Since your python application is basically acting as the Airbyte platform, you have full control over how the “sync” is executed. For example you can still benefit from [incremental syncs](https://glossary.airbyte.com/term/incremental-synchronization/) if your stream supports it by accessing the “last_state” property of the loader. This allows you to load only documents that changed since the last time you loaded, allowing you to update an existing vector database effectively:

import airbyte_cdk.models.airbyte_protocol import AirbyteMessage
with open('stripe_sync_checkpoint.json', 'w') as file:
  file.write(reader.last_state.json())

# later
with open('stripe_sync_checkpoint.json', 'r') as file:
  current_state = AirbyteStateMessage.parse_raw(file.read())
new_docs = reader.load_data(stream_name="invoices", state=current_state)

# Mapping Airbyte records to LlamaIndex documents

By default, each record gets mapped to a Document as part of the loader, with all the various fields in the record becoming a part of the `extra_info` property of the Document (the `extra_info` represents structured metadata for each document) . The text portion of the document is set to the JSON representation of the record. By default, any metadata defined on the Document will be concatenated with the text in downstream modules, so all the fields in the record will be used for embedding and synthesis purposes within a LlamaIndex app. You can pass in a record handler to customize this behavior to build the text part of a record depending on the data:

def handle_record(record, id):
  return Document(doc_id=id, text=record.data["title"], extra_info=record.data)
reader = AirbyteGongReader(config=gong_config, record_handler=handle_record)

# Custom sources

For now, the following Airbyte sources are available as pip packages (with more to come):

- [Gong](https://llamahub.ai/l/airbyte_gong) pip install airbyte-source-gong
- [Hubspot](https://llamahub.ai/l/airbyte_hubspot) pip install airbyte-source-hubspot
- [Salesforce](https://llamahub.ai/l/airbyte_salesforce) pip install airbyte-source-salesforce
- [Shopify](https://llamahub.ai/l/airbyte_shopify) pip install airbyte-source-shopify
- [Stripe](https://llamahub.ai/l/airbyte_stripe) pip install airbyte-source-stripe
- [Typeform](https://llamahub.ai/l/airbyte_typeform) pip install airbyte-source-typeform
- [Zendesk Support](https://llamahub.ai/l/airbyte_zendesk_support) pip install airbyte-source-zendesk-support

However, if you have implemented your own custom Airbyte sources, it’s also possible to integrate them by using the AirbyteCDKReader base class that works with the Source interface of the Airbyte CDK:

from llama_index import download_loader
from my_source.source import MyCustomSource # plug in your own source here
AirbyteCDKReader = download_loader(AirbyteCDKReader)
config = {
  # your custom configuration
}
reader = AirbyteCDKReader(source_class=MyCustomSource, config=config)
documents = reader.load_data(stream_name="my-stream")You can also install sources from the main Airbyte repository by installing directly via git — for example, to fetch the Github source, simply run

pip install "source_github@git+https://github.com/airbytehq/airbyte.git@master#subdirectory=airbyte-integrations/connectors/source-github"After that, the source is available to be plucked into the AirbyteCDKLoader:

from source_github.source import SourceGithub
issues_loader = AirbyteCDKReader(source_class=SourceGithub, config=config)
documents = reader.load_data(stream_name="issues")Check out [the connector development documentation](https://docs.airbyte.com/connector-development/) for how to get started writing your own sources — it’s easy to get started with them and will allow you to move from local embedded loaders to using a hosted Airbyte instance seamlessly depending on your needs.

# Any questions? We would love to hear from you

If you are interested in leveraging Airbyte to ship data to your LLM-based applications, [please take a moment](https://docs.google.com/forms/d/e/1FAIpQLSduobMZwbqiFlPxsWDG-hrBw6NLYMDu_7zRfo4j7AsaO1QtfQ/viewform?usp=sf_link&amp;_gl=1*m4v6ic*_ga*MTM4ODAyNjg4NS4xNjY5ODkyNDQ1*_ga_HDBMVFQGBH*MTY5MjM2MzY0Ni45NS4xLjE2OTIzNjU2NDUuMC4wLjA.) to fill out our survey so we can make sure to prioritize the most important features.

If you have questions or are interested in other existing sources being exposed as loaders this way, do not hesitate to reach out on our [community slack channel](https://airbyte.com/community/community) or in the [integrations channel](https://discord.com/channels/1059199217496772688/1100459663696334968) on the LlamaIndex discord server.