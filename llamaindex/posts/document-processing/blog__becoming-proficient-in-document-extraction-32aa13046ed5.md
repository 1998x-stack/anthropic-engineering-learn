---
title: "Document Extraction Guide: Zephyr 7B + LlamaIndex | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/becoming-proficient-in-document-extraction-32aa13046ed5"
category: "document-processing"
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



   23



##
  **Introduction**

  In the domain of document handling, accurately extracting crucial information
  from images has posed an enduring obstacle. Despite Optical Character
  Recognition (OCR) advancements in converting images to editable text, it faces
  numerous intricacies with diverse document formats and quality. Here enters
  Zephyr 7b LLM, a pioneering remedy that, coupled with LlamaIndex, directly
  addresses these hurdles, heralding a transformative era in image-based
  document extraction.



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



  ![](/blog/images/1*JFum54ZY63bo7QfJOKi1WQ.png)

    Source:
    [Zephyr-llama-index](https://corca.substack.com/p/top-llm-papers-of-the-week-95e?utm_source=profile&amp;utm_medium=reader2)


##
  **The OCR Dilemma: Obstacles and Constraints Optical Character**

Recognition (OCR), though potent, faces impediments such as:

  -
    **Diverse Document Formats**: Documents exhibit intricate
    layouts, fonts, and structures, posing challenges for traditional OCR to
    precisely interpret and extract information.


  -
    **Quality and Clarity**: Images with low resolution,
    blurriness, or skewed angles hinder OCR’s accuracy in deciphering text.


  -
    **Handwritten and Cursive Content**: OCR often struggles with
    handwritten text or cursive fonts, resulting in errors or incomplete
    extraction.


  -
    **Multilingual Complexity**: Processing documents in multiple
    languages poses a challenge for OCR systems lacking proficiency in
    recognizing and extracting varied linguistic content.


  ![](/blog/images/1*Wjgk1UrzmpXz83skj2TxpQ.png)
  Source: Created by Author using MidJourney

##
  **Zephyr 7b LLM: Narrowing the Divide**

  Zephyr 7b LLM revolutionizes the landscape by tackling these inherent
  constraints of OCR technology:

  -
    **Advanced Machine Learning Algorithms:**


  Employing state-of-the-art machine learning algorithms, Zephyr 7b LLM
  undergoes extensive training with diverse document formats and languages. This
  equips it to adapt and learn from various document structures, resulting in
  heightened accuracy and robust extraction capabilities.

  **2. Contextual Comprehension:**

  Diverging from conventional OCR, Zephyr 7b LLM doesn’t merely identify
  individual characters; it comprehends the context in which these characters
  exist. This contextual understanding significantly reduces errors, ensuring
  precise extraction even from intricate document layouts.

  **3. Adaptive Image Processing:**

  The fusion with LlamaIndex amplifies Zephyr 7b LLM’s ability to handle images
  of varying resolutions or qualities. Leveraging adaptive image processing
  techniques, it rectifies distortions, enhances clarity, and optimizes images
  for meticulous OCR analysis.

  **4. Multilingual Proficiency:**

  Zephyr 7b LLM surpasses language barriers. Its multilingual proficiency
  facilitates seamless content extraction from documents in various languages,
  extending global accessibility for businesses dealing with multilingual
  documentation.

  ![](/blog/images/1*1DVGFV2TzRGzsbKfb54zwQ.png)
  Source: Created by Author using MidJourney

##
  **Implementation of Code**

  The collaboration between Zephyr 7b LLM and LlamaIndex signifies a pivotal
  transformation in document extraction. By merging Zephyr’s advanced OCR
  capabilities with LlamaIndex’s image enhancement and data organization
  features, this integration presents a comprehensive solution:

  -
    **Augmented Precision**: The fusion of Zephyr’s machine
    learning expertise and LlamaIndex’s image enhancement markedly heightens the
    accuracy of extracted data, diminishing errors and enhancing overall
    efficiency.


  -
    **Efficient Workflow**: Users experience an optimized workflow,
    enabling swift extraction and conversion of image-based documents into
    structured, actionable data, facilitating expedited decision-making
    processes.


  -
    **Adaptability Across Document Varieties**: This integration
    empowers users to handle diverse document formats and languages
    effortlessly, granting access to previously challenging document types for
    extraction and analysis.


  ![](/blog/images/1*m3B-1XOL6t_5nojWWOBtgw.png)
  Source: Image created by Author using MidJourney

  **Step 1: Install and Import Libraries**

!pip install llama-index transformers accelerate sentencepiece bitsandbytes -q

  **Step 2: Load the Model**

import torch
from transformers import BitsAndBytesConfig
from llama_index.prompts import PromptTemplate
from llama_index.llms import HuggingFaceLLM

quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_use_double_quant=True,
)

def messages_to_prompt(messages):
  prompt = ""
  for message in messages:
    if message.role == 'system':
      prompt += f"&lt;|system|&gt;\n{message.content}&lt;/s&gt;\n"
    elif message.role == 'user':
      prompt += f"&lt;|user|&gt;\n{message.content}&lt;/s&gt;\n"
    elif message.role == 'assistant':
      prompt += f"&lt;|assistant|&gt;\n{message.content}&lt;/s&gt;\n"

  # ensure we start with a system prompt, insert blank if needed
  if not prompt.startswith("&lt;|system|&gt;\n"):
    prompt = "&lt;|system|&gt;\n&lt;/s&gt;\n" + prompt

  # add final assistant prompt
  prompt = prompt + "&lt;|assistant|&gt;\n"

  return prompt

llm = HuggingFaceLLM(
    model_name="HuggingFaceH4/zephyr-7b-alpha",
    tokenizer_name="HuggingFaceH4/zephyr-7b-alpha",
    query_wrapper_prompt=PromptTemplate("&lt;|system|&gt;\n&lt;/s&gt;\n&lt;|user|&gt;\n{query_str}&lt;/s&gt;\n&lt;|assistant|&gt;\n"),
    context_window=3900,
    max_new_tokens=2000,
    model_kwargs={"quantization_config": quantization_config},
    # tokenizer_kwargs={},
    generate_kwargs={"temperature": 0.7, "top_k": 50, "top_p": 0.95},
    messages_to_prompt=messages_to_prompt,
    device_map="auto",
)
from llama_index import ServiceContext, set_global_service_context

service_context = ServiceContext.from_defaults(llm=llm, embed_model="local:BAAI/bge-small-en-v1.5")
set_global_service_context(service_context)

  **Step 3: Storing your index**

from llama_index import SimpleDirectoryReader, VectorStoreIndex
from llama_index.readers.file.base import (
    DEFAULT_FILE_READER_CLS,
    ImageReader,
)
from llama_index.response.notebook_utils import (
    display_response,
    display_image,
)
from llama_index.indices.query.query_transform.base import (
    ImageOutputQueryTransform,
)

filename_fn = lambda filename: {"file_name": filename}

llama_reader = SimpleDirectoryReader(
    input_dir="/content/llama",
    file_metadata=filename_fn,
)
llama_documents = llama_reader.load_data()

llama_index = VectorStoreIndex.from_documents(llama_documents)

  **Step 4: Query **[**Transformations**](https://github.com/andysingal/CV_public/tree/main/zephyr-7b-alpha)

from llama_index.query_engine import TransformQueryEngine

query_engine = llama_index.as_query_engine(similarity_top_k=2)
query_engine = TransformQueryEngine(
    query_engine, query_transform=ImageOutputQueryTransform(width=400)
)
llama_response = query_engine.query(
    "Show an image to illustrate how tree index works and explain briefly",
)

display_response(llama_response)

#Output
Final Response: I am not capable of displaying images. however, i can provide you with an explanation of how tree index works.

tree index is a data structure that organizes data in a hierarchical manner, similar to a tree. it is commonly used in databases to improve query performance.

when querying a tree index, the process involves traversing from the root node down to the leaf nodes. the number of child nodes chosen per parent node is determined by the child_branch_factor parameter.

for example, if child_branch_factor=1, a query will choose one child node given a parent node. if child_branch_factor=2, a query will choose two child nodes per parent.

the following image illustrates how a tree index works:

! Tree Index Example

in this example, the tree index is built from a set of nodes (which become leaf nodes in this tree). when querying this index, the process involves traversing from the root node down to the leaf nodes. for instance, if we want to find a specific node with the value "x", we would start at the root node and follow the left branch (since "x" is less than "a") to the next level. we would then follow the left branch again to reach the leaf node with the value "x".

i hope this helps clarify how tree index works!

  **Step 5: Lets read the **[**receipts**](https://github.com/andysingal/CV_public/tree/main/zephyr-7b-alpha)

from llama_index.readers.file.base import DEFAULT_FILE_READER_CLS
from llama_index.readers.file.image_reader import ImageReader

image_parser =ImageReader(
    keep_image=True,
    parse_text=True
    )
file_extractor = DEFAULT_FILE_READER_CLS
file_extractor.update({
    ".jpg": image_parser,
    ".png": image_parser,
    ".jpeg": image_parser,
    })

receipt_reader = SimpleDirectoryReader(
    input_dir="/content/data",
    file_metadata=filename_fn,
    file_extractor=file_extractor,
)
receipt_documents = receipt_reader.load_data()
print(len(receipt_documents))

#Output
3
receipts_index = VectorStoreIndex.from_documents(receipt_documents)

from llama_index.query_engine import TransformQueryEngine
query_engine = receipts_index.as_query_engine()

receipts_response = query_engine.query(
    "When was the last time I went to RESTAURANT and how much did I spend? this data is in your latest vector index.",
)

display_response(receipts_response)

# Output
Final Response: Based on the given context information, the last time the querying individual went to RESTAURANT was on July 5, 2019, and they spent $164.00.

## Conclusion

  In summary, the fusion of Zephyr 7b LLM and LlamaIndex initiates a new chapter
  in image-based document extraction. Beyond addressing OCR’s inherent
  challenges, it enhances the precision and efficiency of data extraction from
  images, fostering improved productivity and decision-making in
  document-focused workflows.

“Stay connected and support my work through various platforms:

  -
    [GitHub](https://medium.com/u/8df3bf3c40ae): For
    all my open-source projects and Notebooks, you can visit my GitHub profile
    at
    [https://github.com/andysingal](https://github.com/andysingal). If you find my content valuable, don’t hesitate to leave a star.


  -
    Patreon: If you’d like to provide additional support, you can consider
    becoming a patron on my Patreon page at
    [https://www.patreon.com/AndyShanu](https://www.patreon.com/AndyShanu).


  -
    [Medium](https://medium.com/u/504c7870fdb6): You
    can read my latest articles and insights on Medium at
    [https://medium.com/@andysingal](https://medium.com/@andysingal).


  -
    [The Kaggle](https://medium.com/u/29b47aa8cce3):
    Check out my Kaggle profile for data science and machine learning projects
    at
    [https://www.kaggle.com/alphasingal](https://www.kaggle.com/alphasingal).


  -
    [Hugging Face](https://medium.com/u/b1574f0c6c5e):
    For natural language processing and AI-related projects, you can explore my
    Huggingface profile at
    [https://huggingface.co/Andyrasika](https://huggingface.co/Andyrasika).


  -
    YouTube: To watch my video content, visit my YouTube channel at
    [https://www.youtube.com/@andy111007](https://www.youtube.com/@andy111007).


  -
    LinkedIn: To stay updated on my latest projects and posts, you can follow me
    on LinkedIn. Here is the link to my profile:
    [https://www.linkedin.com/in/ankushsingal/."](https://www.linkedin.com/in/ankushsingal/.%22)


  Requests and questions: If you have a project in mind that you’d like me to
  work on or if you have any questions about the concepts I’ve explained, don’t
  hesitate to let me know. I’m always looking for new ideas for future Notebooks
  and I love helping to resolve any doubts you might have.

  Remember, each “Like”, “Share”, and “Star” greatly contributes to my work and
  motivates me to continue producing more quality content. Thank you for your
  support!

  If you enjoyed this story, feel free
  [to subscribe](https://medium.com/@andysingal)
  to Medium, and you will get notifications when my new articles will be
  published, as well as full access to thousands of stories from other authors.

Resource:

  -
    [Data used for above code](https://github.com/andysingal/CV_public/tree/main/zephyr-7b-alpha)


  -
    [llama-index](https://gpt-index.readthedocs.io/en/stable/)