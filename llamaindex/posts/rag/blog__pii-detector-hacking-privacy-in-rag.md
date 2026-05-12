---
title: "PII Detector for RAG: Presidio Masking Guide | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/pii-detector-hacking-privacy-in-rag"
category: "rag"
---

Content



- [ PII: What? Why?  ](#pii-what-why)
- [ PII in RAG  ](#pii-in-rag)
- [ Model  ](#model)
- [ Vector Database  ](#vector-database)
- [ Introducing: Presidio  ](#introducing-presidio)
- [ How Does Presidio Work?  ](#how-does-presidio-work)
- [ LlamaIndex Post Processors  ](#llamaindex-post-processors)
- [ Integrating Presidio with LlamaIndex  ](#integrating-presidio-with-llamaindex)
- [ Test and Benchmark  ](#test-and-benchmark)
- [ How It Ended  ](#how-it-ended)
- [ Update  ](#update)



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







 A couple of days ago at the DataStax HQ, I had the chance to participate at the LlamaIndex RAG-A-THON. Over the span of the weekend, we had to implement a solution that leverages Retrieval Augmented Generation (RAG) technique.



 Because of my background in cybersecurity, I was leaning towards the security pitfalls and obstacles of the RAG technique. One of the first things that came to mind was the fact that a lot of the unstructured data used is unsanitized and can contain sensitive data.



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



##  PII: What? Why?



 PII stands for Personally Identifiable Information. It refers to any information that can be used to identify a specific individual.
This can be names, addresses, phone numbers, email addresses, social security numbers, and financial information.



 There are a couple of reasons why handling PIIs is important:


-  **Privacy:** PII often includes sensitive and private details (like addresses), so protecting it preserves customers’ privacy.
  -  **Identity Theft:** PII can also lead to identity theft (e.g. one’s social security number gets compromised).
  -  **Legal Compliance:** Protecting PII is also the law. Many countries and regions have enacted laws and regulations that require organizations to protect PII. GDPR (General Data Protection Regulation) in the EU or HIPAA (Health Insurance Portability and Accountability Act) in the United States govern the way we handle PII.
  -  **Trust and Reputation:** A data breach or mishandling of PII will severely damage one’s reputation and trust.
  -  **Financial Security:** PII may include financial information, such as credit card numbers and banking details. Compromised PII can lead to fraudulent transactions.
  -  **National Security Concerns:** All of the above are crucial in sovereign environments.



##  PII in RAG



 Everything listed is applicable to almost all applications leveraging RAG. Remember that the RAG technique contains two components — the model and the vector database. For this reason, each of these components need to address PII.



###  Model



 Language models, are trained on large datasets that may contain real-world data, potentially including PII and customer data. When the models generate text, there is a risk that they’ll produce content that includes PII. This is even more crucial if you’re creating a multi-tenant application, and you want to prevent data leak. This risk can be mitigated by either filtering or anonymizing the response. Training the models on anonymized data that is stripped of any sensitive information is the better approach to prevent leaks of PII.



###  Vector Database



 Vector databases, just like regular databases should not persist sensitive information plainly. This kind of information should only be persisted using encryption, hashing, salt and access controls. Having said that, one should also make sure that the similarity search returned by the Database won’t retrieve personal data.



 On top of that, various regulations such as GDPR and HIPAA still apply here. So, if the original data contain PII, you might need to add another instance in Europe or any additional region in accordance with regulations. Persisted data should be encrypted or hashed (and additionally salted).



##  Introducing: Presidio



 [Presidio](https://microsoft.github.io/presidio/) is an open-source library maintained by Microsoft (see our [GitHub](https://github.com/microsoft/presidio) repo). It’s derived from the Latin word praesidium which means “protection” or garrison.


-  It enables organizations to preserve privacy using a unified SDK.
  -  It provides fast ***identification*** and ***anonymization*** modules for private entities in text and images such as credit card numbers, names, locations, social security numbers, bitcoin wallets, US phone numbers, financial data and more.



 *Disclaimer: Nothing is bulletproof. It’s your responsibility to make sure sensitive data is anonymized.*



###  How Does Presidio Work?


-  **Predefined** or **custom PII recognizers** leverage *Named Entity Recognition (NER)*, *regular expressions*, *rule-based logic* and *checksum* (e.g. bitcoin address validation).
  -  It’s extensible, so you can add your own entities and your own detection mechanisms.
  -  It’s customizable, so you can create your own anonymizers, and exclude/include certain entities (e.g. exclude anonymization of geographical locations).

  ![](https://cdn.sanity.io/images/7m9jw85w/production/4419e1afaa5eab8c15eb7b3ba750166298158a67-853x480.gif)

###  LlamaIndex Post Processors



 There was already some PII integration using NER models and LLMs! These were implemented as post processors that run in the end of the pipeline:



python






```
from llama_index.postprocessor import NERPIINodePostprocessor
from llama_index import ServiceContext
from llama_index.schema import TextNode

text = """
My name is Roey Ben Chaim and my credit card number is 4095-2609-9393-4932.
My email is robo@presidio.site and I live in Amsterdam.
Have you been to a Pálmi Einarsson concert before?
What is the limit for card 4158112277712? My IBAN is GB90YNTU67299444055881.
What's your last name? Bob, it's Bob.
My great great grandfather was called Yulan Peres,
and my great great grandmother was called Jennifer Holst
I can't browse to your site, keep getting address 179.177.214.91 blocked error
Just posted a photo https://www.FilmFranchise.dk/
"""

node = TextNode(text=text)

service_context = ServiceContext.from_defaults()
processor = NERPIINodePostprocessor(service_context=service_context)

from llama_index.schema import NodeWithScore

new_nodes = processor.postprocess_nodes([NodeWithScore(node=node)])
print(new_nodes[0].node.get_text())
```
    Running the above code resulted in the following:



text






```
My name is [PER_12] and my credit card number is 4095-2609-9393-4932.
My email is robo@presidio.site and I live in [LOC_123].
Have you been to a [PER_153] concert before?
What is the limit for card 4158112277712? My IBAN is GB90YNTU67299444055881.
What's your last name? [PER_286], it's [PER_286].
My great great grandfather was called [PER_339],
and my great great grandmother was called [PER_395]
I can't browse to your site, keep getting address 179.177.214.91 blocked error
Just posted a photo https://www.[ORG_521].dk/
```
    As can be seen in this example, while NER models do a decent job in detecting PII, they might miss some entities such as IBAN code, credit card numbers, emails, medical license and more.



 Presidio detects more out of the box entities than traditional models. This is possible because Presidio leverages a couple of methods in detecting PII — from NER models to regular expressions and rule-based logic.



##  Integrating Presidio with LlamaIndex



 I ended up integrating ***PresidioPIINodePostprocessor*** that got the text as an input and masked it. Doing this was possible using Presidio’s analyzer and anonymizer:



python






```
from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine

analyzer = AnalyzerEngine(supported_languages=["en"])
results = analyzer.analyze(text=text, language='en')
engine = AnonymizerEngine()
new_text = engine.anonymize(text=text, analyzer_results=results)
```
    This was pretty fun and simple. However, given the input text “Alice and Bob are friends”, the output would be: “&lt;PERSON&gt; and &lt;PERSON&gt; are friends”. I could not have that.



 So, I added a counter and mapped the original values with the masked values, making sure that whenever an entity was seen again, the previously asked value was used:



python






```
def anonymize_function(origin, entity_type):
    nonlocal pii_counter
    nonlocal inverted_mapping
    nonlocal mapping
    if entity_type not in inverted_mapping:
        inverted_mapping[entity_type] = {}
    typed_mapping = inverted_mapping[entity_type]
    if origin in typed_mapping:
        return typed_mapping[origin]
    new_value = f"&#x3C;{entity_type}_{pii_counter}>"
    typed_mapping[origin] = new_value
    mapping[new_value]=origin
    pii_counter+=1
    return typed_mapping[origin]

from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import OperatorConfig

analyzer = AnalyzerEngine(supported_languages=["en"])
results = analyzer.analyze(text=text, language='en')
engine = AnonymizerEngine()
new_text = engine.anonymize(text=text, analyzer_results=results,
                            operators={"DEFAULT": OperatorConfig("custom",
                            params={"lambda": anonymize_function})})
```
    *Note: Currently presidio doesn’t contain the entity type as an input parameter in the lambda function, so I had to add this functionality.*



##  Test and Benchmark



 Once this was all up and running, I was able to call the newly added presidio post processor with the text from the previous run:



python






```
from llama_index.postprocessor import PresidioPIINodePostprocessor
from llama_index import ServiceContext
from llama_index.schema import TextNode

text = """
My name is Roey Ben Chaim and my credit card number is 4095-2609-9393-4932.
My email is robo@presidio.site and I live in Amsterdam.
Have you been to a Pálmi Einarsson concert before?
What is the limit for card 4158112277712? My IBAN is GB90YNTU67299444055881.
What's your last name? Bob, it's Bob.
My great great grandfather was called Yulan Peres,
and my great great grandmother was called Jennifer Holst
I can't browse to your site, keep getting address 179.177.214.91 blocked error
Just posted a photo https://www.FilmFranchise.dk/
"""

node = TextNode(text=text)

service_context = ServiceContext.from_defaults()
processor = PresidioPIINodePostprocessor(service_context=service_context)

from llama_index.schema import NodeWithScore

new_nodes = processor.postprocess_nodes([NodeWithScore(node=node)])
print(new_nodes[0].node.get_text())
```
    Running the above code resulted in the following:



text






```
My name is &#x3C;PERSON_12> and my credit card number is &#x3C;CREDIT_CARD_11>.
My email is &#x3C;EMAIL_ADDRESS_10> and I live in &#x3C;LOCATION_9>.
Have you been to a &#x3C;PERSON_8> concert before?
What is the limit for card &#x3C;CREDIT_CARD_7>? My IBAN is &#x3C;IBAN_CODE_6>.
What's your last name? &#x3C;PERSON_5>, it's &#x3C;PERSON_5>.
My great great grandfather was called &#x3C;PERSON_4>,
and my great great grandmother was called &#x3C;PERSON_3>
I can't browse to your site, keep getting address &#x3C;IP_ADDRESS_2> blocked error
Just posted a photo &#x3C;URL_1>
```
    Overall Presidio detected 12 entities while the other NER solution detected 8. Notice that credit card numbers, email address, IBAN, IP address and the URL (at least some of it) weren’t detected.



 I was curious to see how the parsing of these strings would work on the LLM, so I populated the index and queried the following:



python






```
from llama_index import VectorStoreIndex

index = VectorStoreIndex([n.node for n in new_nodes])
response = index.as_query_engine().query(
    "What is my name?"
)
print(response)
```
    Which resulted in:



text






```
Your name is &#x3C;PERSON_12>.
```


##  How It Ended

  Anyway, this project won the 3rd place (in the continuous track) in the RAG-A-THON.

  ![](https://cdn.sanity.io/images/7m9jw85w/production/797baae5afc6b105c6dae1764a326fbaed14dfbd-1400x1475.webp)

 Note: this picture doesn’t contain PII



###  Update



 Presidio is now fully integrated into LlamaIndex as a post processor, follow this [notebook](https://github.com/run-llama/llama_index/blob/ff51e2cbf9815a44ebade9a1382216435d7f4bc8/docs/examples/node_postprocessor/PII.ipynb#L289) to learn how to use Presidio for PII masking. The next steps would be to add more customization and anonymization options.