---
title: "Llama Datasets: Benchmark RAG Pipelines Fast | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/introducing-llama-datasets-aadb9994ad9e"
category: "benchmarks-evals"
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







(Authors: Andrei Fajardo and Jerry Liu @ LlamaIndex)

Today we’re excited to introduce **Llama Datasets **🦙 📝— a set of community-contributed datasets that allow users to easily benchmark their RAG pipelines for different use cases. A dataset consists of both question-answer pairs as well as source context. To use them, download them from LlamaHub; then evaluate your RAG pipeline using the dataset + a set of evaluation metrics.



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



We’re launching with an initial set of 10 evaluation datasets and we’ll be adding more! We’ve also made it super easy to contribute your own dataset — upload your source documents + QA pairs (generated manually or synthetically).

# Context

A big problem in building production RAG is evaluation. Unlike traditional software systems, LLM systems (and ML systems more generally) are stochastic black-boxes designed to model noisy real-world signals. This means that developers can’t easily define unit tests that assert deterministic behavior — there may always be an input that causes an error. Because developers don’t quite know what goes out given what goes in, they need to define an **evaluation dataset** that’s reflective of their production use cases, and evaluate their system over this dataset using a set of **evaluation metrics**.

We’ve presented [extensively on this topic ](https://docs.google.com/presentation/d/1wtlEJC6SXLsoGkDdCkxC-Y_V8bvyYsi9Ozh59VMI22I/edit?usp=sharing)— every AI engineer should setup evaluation before trying to optimize their LLM or RAG application with advanced techniques.

But we’ve increasingly found that defining the **right evaluation dataset is hard and use-case dependent**. Evaluating over academic benchmarks, like BEIR and HotpotQA oftentimes fail to generalize to specific use cases. Certain parameters that work well on certain data domains (e.g. SEC filings) may fail on others (e.g. research papers).

That’s what inspired us to create Llama Datasets. Instead of being prescriptive on the data you must use, we’ve decided to create a hub where you can easily pick and choose the right datasets for your use case!

Llama Datasets on LlamaHub![](/blog/images/1*-bRp8qQiVW69YA7dn2m75w.png)

# Overview

Today’s launch includes the set of Llama Datasets on [LlamaHub](https://llamahub.ai/), an accompanying `RagEvaluatorPack` to help compute metrics over a dataset, as well as accompanying dataset abstractions that you can also use on their own.

- To use a Llama Dataset, download it off LlamaHub and run our `RagEvaluatorPack` (or run your own evaluation modules).
- To generate a Llama Dataset, define a `LabelledRagDataset` with a set of `LabelledRagDataExample`objects.
- To contribute a Llama Dataset, submit a “data card” to LlamaHub and upload your raw dataset files to our `llama_datasets` repository.

Check out the below sections for a walkthrough over an example dataset.

We’re launching with 10 initial datasets:

- [Blockchain Solana Dataset](https://llamahub.ai/l/llama_datasets-blockchain_solana)
- [Coda Help Desk Dataset (with Braintrust)](https://llamahub.ai/l/llama_datasets-braintrust_coda)
- [FinanceBench Dataset (Patronus AI)](https://llamahub.ai/l/llama_datasets-patronus_financebench)
- [Paul Graham Essay Dataset](https://llamahub.ai/l/llama_datasets-paul_graham_essay)
- [Llama 2 Paper Dataset](https://llamahub.ai/l/llama_datasets-llama2_paper)
- [Uber/Lyft 2021 10K Filings Dataset](https://llamahub.ai/l/llama_datasets-10k-uber_2021)
- [Mini Truthful QA Dataset (Arize AI)](https://llamahub.ai/l/llama_datasets-mini_truthfulqa)
- [Mini Squad V2 Dataset (Arize AI)](https://llamahub.ai/l/llama_datasets-mini_squadv2)
- [Origin of COVID-19](https://llamahub.ai/l/llama_datasets-origin_of_covid19)
- [LLM Survey Paper Dataset](https://llamahub.ai/l/llama_datasets-eval_llm_survey_paper)

Example Llama Dataset page![](/blog/images/1*VZFR7UsNreOkGeuoSM9E9w.png)

# Example Walkthrough

Let’s walk through the different steps of using/contributing a Llama Dataset.

## 1. Downloading and Using a Llama Dataset

[Follow the full notebook here.](https://github.com/run-llama/llama_index/blob/main/docs/examples/llama_dataset/downloading_llama_datasets.ipynb)

Downloading a dataset is simple, do the following command (here we download Paul Graham).

from llama_index.llama_dataset import download_llama_dataset

# download and install dependencies
rag_dataset, documents = download_llama_dataset(
    "PaulGrahamEssayDataset", "./paul_graham"
)This downloads a `rag_dataset` which contains the QA pairs (+ reference context), and `documents` which is the source document corpus.

Let’s inspect the `rag_dataset` with `to_pandas()` :

Sample rows from `rag_dataset`![](/blog/images/1*9jidJEHRj2o7K4iGaoEoxQ.png)

Generating predictions over the RAG dataset is straightforward. You can easily plug in any query engine into `amake_predictions_with` :

from llama_index import VectorStoreIndex

# a basic RAG pipeline, uses service context defaults
index = VectorStoreIndex.from_documents(documents=documents)
query_engine = index.as_query_engine()

# generate prediction dataset
prediction_dataset = await rag_dataset.amake_predictions_with(
    query_engine=query_engine, show_progress=True
)The `prediction_dataset` is a `RagPredictionDataset` object that looks like the following:

Prediction Dataset![](/blog/images/1*bVy23rFFv6wDb5r1Q8Ffuw.png)

Given the `rag_dataset` and `prediction_dataset` , you can use our evaluation modules to measure performance across a variety of metrics (e.g. faithfulness, correctness, relevancy).

for example, prediction in tqdm.tqdm(
    zip(rag_dataset.examples, prediction_dataset.predictions)
):
    correctness_result = judges["correctness"].evaluate(
        query=example.query,
        response=prediction.response,
        reference=example.reference_answer,
    )To eliminate the boilerplate of writing all these evaluation modules, we’ve also provided a LlamaPack that will do all this for you!

from llama_index.llama_pack import download_llama_pack

RagEvaluatorPack = download_llama_pack("RagEvaluatorPack", "./pack")
rag_evaluator = RagEvaluatorPack(
    query_engine=query_engine, rag_dataset=rag_dataset
)
benchmark_df = await rag_evaluator.arun()

## 2. Generating a Llama Dataset

[Follow the full notebook here.](https://github.com/run-llama/llama_index/blob/main/docs/examples/llama_dataset/labelled-rag-datasets.ipynb)

You can use our `LabelledRagDataExample` and `LabelledRagDataset` abstractions to create your own dataset.

Here’s an example of adding an example manually.

from llama_index.llama_dataset import (
    LabelledRagDataExample,
    CreatedByType,
    CreatedBy,
)

# constructing a LabelledRagDataExample
query = "This is a test query, is it not?"
query_by = CreatedBy(type=CreatedByType.AI, model_name="gpt-4")
reference_answer = "Yes it is."
reference_answer_by = CreatedBy(type=CreatedByType.HUMAN)
reference_contexts = ["This is a sample context"]

rag_example = LabelledRagDataExample(
    query=query,
    query_by=query_by,
    reference_contexts=reference_contexts,
    reference_answer=reference_answer,
    reference_answer_by=reference_answer_by,
)from llama_index.llama_dataset.rag import LabelledRagDataset

rag_dataset = LabelledRagDataset(examples=[rag_example, rag_example_2])You can also synthetically generate a dataset over any document corpus with GPT-4:

# generate questions against chunks
from llama_index.llama_dataset.generator import RagDatasetGenerator
from llama_index.llms import OpenAI
from llama_index import ServiceContext

# set context for llm provider
gpt_4_context = ServiceContext.from_defaults(
    llm=OpenAI(model="gpt-4", temperature=0.3)
)

# instantiate a DatasetGenerator
dataset_generator = RagDatasetGenerator.from_documents(
    documents,
    service_context=gpt_4_context,
    num_questions_per_chunk=2,  # set the number of questions per nodes
    show_progress=True,
)

## 3. Contributing a Llama Dataset

We’ve provided a [ready-made submission notebook template here ](https://github.com/run-llama/llama_index/blob/main/docs/examples/llama_dataset/ragdataset_submission_template.ipynb)— just fill in the blanks with your dataset!

If you’re interested in contributing a dataset, we’d love to feature it! You just need to follow these steps:

- **Create the dataset:** To create a `LabelledRagDataset` , you can create it from scratch either manually or with synthetically generated examples, or create it from an existing dataset.
- **Generate a baseline evaluation dataset:** Benchmark a basic top-k RAG pipeline over your dataset, and report the numbers. This will serve as a point of reference for others. You can use the `RagEvaluatorPack` for this purpose.
- **Prepare the dataset card ( **`**card.json**`** ) and **`**README.md**`** : **These will be shown on the LlamaHub page for this dataset. If you want to auto-generate this given some inputs, check out our `[LlamaDatasetMetadata](https://llamahub.ai/l/llama_packs-llama_dataset_metadata)`LlamaPack.
- Submit a PR into `llama-hub` to register the `LlamaDataset` .
- Submit a PR into `llama-datasets` to upload the `LlamaDataset` and its source files.

You can follow all of these steps in our [notebook template above](https://github.com/run-llama/llama_index/blob/main/docs/examples/llama_dataset/ragdataset_submission_template.ipynb) — simply substitute your own data.

# Conclusion

We’d love for you to check out our datasets and let us know your feedback! We’d love your contributions as well.

## Resources

Here are the resources mentioned in the blog post.

- [Llama Datasets on LlamaHub](https://llamahub.ai/) (make sure to select “Llama Datasets” from the dropdown)
- [Downloading a Llama Dataset Notebook](https://github.com/run-llama/llama_index/blob/main/docs/examples/llama_dataset/downloading_llama_datasets.ipynb)
- [Creating a Llama Dataset Notebook](https://github.com/run-llama/llama_index/blob/main/docs/examples/llama_dataset/labelled-rag-datasets.ipynb)
- [Contributing a Llama Dataset Notebook Template](https://github.com/run-llama/llama_index/blob/main/docs/examples/llama_dataset/ragdataset_submission_template.ipynb)
- [README on Contributing a Llama Dataset](https://github.com/run-llama/llama-hub#how-to-add-a-llama-dataset)