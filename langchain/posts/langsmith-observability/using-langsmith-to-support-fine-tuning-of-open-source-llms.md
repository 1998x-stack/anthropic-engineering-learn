---
title: "Using LangSmith to Support Fine-tuning"
author: "LangChain Accounts"
date: "2023-08-23"
url: "https://www.langchain.com/blog/using-langsmith-to-support-fine-tuning-of-open-source-llms"
---

LangSmithTutorials &amp; How-Tos

# Using LangSmith to Support Fine-tuning

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamAugust 23, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)9min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1a8a2e6df4d389b2723_6Icr9fARMmTjTHqTzK8z_DSC_0123.jpeg)

### Summary

We created a guide for fine-tuning and evaluating LLMs **using LangSmith for dataset management and evaluation**. We did this both with an open source LLM on CoLab and HuggingFace for model training, as well as OpenAI&#x27;s new finetuning service. As a test case, we fine-tuned LLaMA2-7b-chat and `gpt-3.5-turbo` for an extraction task (knowledge graph triple extraction) using training data exported from LangSmith and also evaluated the results using LangSmith. The CoLab guide is [here](https://colab.research.google.com/drive/1tpywvzwOS74YndNXhI8NUaEfPeqOc7ub?usp=sharing&amp;ref=blog.langchain.com).

### Context

Interest in fine-tuning has grown rapidly over the past few weeks. This can largely be attributed to two causes.

First, the open source LLM ecosystem has grown remarkably, progressing from open source LLMs that [lagged the state-of-the-art (SOTA) by a wide margin](https://cameronrwolfe.substack.com/p/the-history-of-open-source-llms-early?ref=blog.langchain.com) to near-SOTA (e.g., Llama-2) LLMs that [can be run on consumer laptops](https://python.langchain.com/docs/guides/local_llms?ref=blog.langchain.com) in ~1 year! The drivers of this progress include [increasingly large corpus of training](https://cameronrwolfe.substack.com/p/the-history-of-open-source-llms-better?ref=blog.langchain.com) data (x-axis, below) and fine-tuning (y-axis) for [instruction-following](https://openai.com/research/instruction-following?ref=blog.langchain.com) and better-human-[aligned](https://mlabonne.github.io/blog/posts/Fine_Tune_Your_Own_Llama_2_Model_in_a_Colab_Notebook.html?ref=blog.langchain.com) responses. Performant open source base models offer benefits such as cost savings (e.g., for [token-intensive tasks](https://twitter.com/RLanceMartin/status/1691492119855390720?s=20&amp;ref=blog.langchain.com)), privacy, and - with fine tuning - the opportunity to [exceed](https://www.anyscale.com/blog/fine-tuning-llama-2-a-comprehensive-case-study-for-tailoring-models-to-unique-applications?ref=blog.langchain.com) SOTA LLMs with much smaller open source for highly specific tasks.

Second, the leading LLM provider, OpenAI, [has released](https://openai.com/blog/gpt-3-5-turbo-fine-tuning-and-api-updates?ref=blog.langchain.com) fine-tuning support for `gpt-3.5-turbo` (and other models). Previously, fine-tuning was only available for older models. These models were not nearly as capable as newer models, meaning even after fine-tuning, they often weren&#x27;t competitive with GPT-3.5 and few-shot examples. Now that newer models can be fine-tuned, many expect this to change.

[Some](https://twitter.com/ajratner/status/1693320931744292902?s=20&amp;ref=blog.langchain.com) [have](https://www.youtube.com/watch?v=zjM2-_cFupo&amp;ref=blog.langchain.com) [argued](https://www.youtube.com/watch?v=1StidE83-Xs&amp;&amp;ref=blog.langchain.com) that organizations may opt for many specialist fine-tuned LLMs derived from open source base models over a single massive generalist model. With this and libraries such as [HuggingFace](https://huggingface.co/blog/llama2?ref=blog.langchain.com) to support fine-tuning in mind, you may be curious about when and how to fine-tune. This guide provides an overview and shows how LangSmith can support the process.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1a9a2e6df4d389b2765_image-11.png)

### When to fine-tune

LLMs can learn new knowledge in at least two ways: weight updates (e.g., pre-training or fine-tuning) or prompting (e.g., retrieval augmented generation, RAG). Model weights are like long-term memory whereas the prompt is like short-term memory. This [OpenAI cookbook](https://github.com/openai/openai-cookbook/blob/main/examples/Question_answering_using_embeddings.ipynb?ref=blog.langchain.com) has a useful analogy: *When you fine-tune a model, it&#x27;s like studying for an exam one week away. When you insert knowledge into the prompt (e.g., via retrieval), it&#x27;s like taking an exam with open notes.*

With this in mind, fine-tuning is [not](https://github.com/openai/openai-cookbook/blob/main/examples/Question_answering_using_embeddings.ipynb?ref=blog.langchain.com) [advised](https://www.glean.com/blog/lessons-and-learnings-from-building-an-enterprise-ready-ai-assistant?ref=blog.langchain.com) for teaching an LLM new knowledge or factual recall; this [talk](https://www.youtube.com/live/hhiLw5Q_UFg?feature=share&amp;ref=blog.langchain.com) from John Schulman of OpenAI notes that fine-tuning can increase hallucinations. Fine-tuning is better suited for teaching specialized tasks, but it [should be](https://twitter.com/rachel_l_woods/status/1692577254914638340?s=20&amp;ref=blog.langchain.com) [considered](https://twitter.com/transitive_bs/status/1643017583917174784?s=20&amp;ref=blog.langchain.com) [relative to prompting or RAG](https://twitter.com/karpathy/status/1655994367033884672?s=20&amp;ref=blog.langchain.com). As discussed [here](https://twitter.com/karpathy/status/1655994367033884672?ref=blog.langchain.com), fine-tuning can be helpful for well-defined tasks with ample examples and / or LLMs that lack the in-context learning capacity for few-shot prompting. This Anyscale [blog](https://www.anyscale.com/blog/fine-tuning-is-for-form-not-facts?ref=blog.langchain.com) summarizes these points well: *fine-tuning is for form, not facts*.

### How to fine-tune

There’s a number of helpful LLaMA fine-tuning recipes that have been released for tasks such as [chat](https://huggingface.co/datasets/mlabonne/guanaco-llama2-1k?ref=blog.langchain.com) using a [subset](https://huggingface.co/datasets/mlabonne/guanaco-llama2-1k?ref=blog.langchain.com) of the [OpenAssistant corpus](https://paperswithcode.com/dataset/oasst1?ref=blog.langchain.com) in [HuggingFace](https://github.com/huggingface/trl/blob/main/examples/scripts/sft_trainer.py?ref=blog.langchain.com). Notably, these work on a single CoLab GPU, which makes the workflow accessible. However, two of the largest remaining pain points in fine-tuning are dataset collection / cleaning and evaluation. Below we show how LangSmith can be used to help address both of these (green, below).

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1a9a2e6df4d389b275d_image-12.png)

### Task

Tasks like [classification / tagging or extraction](https://twitter.com/ajratner/status/1693320931744292902?s=20&amp;ref=blog.langchain.com) are well-suited for fine-tuning; Anyscale [reported](https://www.anyscale.com/blog/fine-tuning-llama-2-a-comprehensive-case-study-for-tailoring-models-to-unique-applications?ref=blog.langchain.com) promising results (exceeding GPT4) by fine-tuning LLaMA 7B and 13B LLMs on extraction, text-to-SQL, and QA. As a test case, we chose extraction of knowledge triples of the form (subject, relation, object) from text: the subject and object are entities and the relation is a property or connection between them. Triples can then be used to build [knowledge graphs](http://ai.stanford.edu/blog/introduction-to-knowledge-graphs/?ref=blog.langchain.com), databases that store information about entities and their relationships. We built an public [Streamlit app](https://auto-graph.streamlit.app/?ref=blog.langchain.com) for triple extraction from user input text to explore the capacity of LLMs (GPT3.5 or 4) to extract triples with function calling. In parallel, we fine-tuned LLaMA2-7b-chat and [GPT-3.5](https://openai.com/blog/gpt-3-5-turbo-fine-tuning-and-api-updates?ref=blog.langchain.com) for this task using [public](https://github.com/dair-iitd/CaRB?ref=blog.langchain.com) [datasets](https://github.com/gkiril/benchie?ref=blog.langchain.com).

### Dataset

**Dataset collection and cleaning is often a challenging task in training LLMs.** When a project is set up in LangSmith, generations are automatically logged, making it easy to get a large quantity of data. LangSmith offers a [queryable interface](https://docs.smith.langchain.com/evaluation/datasets?ref=blog.langchain.com) so you can use user feedback filters, tags, and other metrics to [select for poor quality cases](https://docs.smith.langchain.com/tracing/use-cases/export-runs/local?ref=blog.langchain.com#complex-query-list-all-runs-that-started-after-a-specific-timestamp-and-either-have-error-not-equal-to-null-or-a-correctness-feedback-score-equal-to-0), correct the outputs in the app, and save to datasets that you can use to improve the results of your model (see below).

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1a9a2e6df4d389b2754_image-13.png)

As an example, we created LangSmith train and test datasets from knowledge graph triples in the public [BenchIE](https://github.com/gkiril/benchie?ref=blog.langchain.com) and [CarbIE](https://blog.langchain.com/318c3ea1b6e442a7a8240acacb9c8a80?pvs=25) datasets; we converted them to a shared JSON format with each triplet represented as {s: subject, object: object, relation: relationship} and randomly split the combined data to into a  train set of ~1500 labeled sentences and a test set of 100 sentences. The [CoLab](https://colab.research.google.com/drive/1tpywvzwOS74YndNXhI8NUaEfPeqOc7ub?usp=sharing&amp;ref=blog.langchain.com) shows how to easily load LangSmith datasets. Once loaded, we create instructions for fine-tuning using the system prompt below and [LLaMA instruction tokens](https://huggingface.co/blog/llama2?ref=blog.langchain.com#how-to-prompt-llama-2) (as done [here](https://huggingface.co/datasets/mlabonne/guanaco-llama2-1k?ref=blog.langchain.com)):

`&quot;you are a model tasked with extracting knowledge graph triples from given text. &quot;
&quot;The triples consist of:\n&quot;
&quot;- \&quot;s\&quot;: the subject, which is the main entity the statement is about.\n&quot;
&quot;- \&quot;object\&quot;: the object, which is the entity or concept that the subject is related to.\n&quot;
&quot;- \&quot;relation\&quot;: the relationship between the subject and the object. &quot;
&quot;Given an input sentence, output the triples that represent the knowledge contained in the sentence.&quot;`

### Quantization

As shown in the excellent guide [here](https://mlabonne.github.io/blog/posts/Fine_Tune_Your_Own_Llama_2_Model_in_a_Colab_Notebook.html?ref=blog.langchain.com), we fine-tune a 7B parameter LLaMA chat model. We want to do this on a single GPU (HuggingFace guide [here](https://huggingface.co/docs/transformers/perf_train_gpu_one?ref=blog.langchain.com#anatomy-of-models-memory)), which presents a challenge: if each parameter is 32 bits, a 7B parameter LLaMA2 model will occupy [28GB](https://finbarr.ca/how-is-llama-cpp-possible/?ref=blog.langchain.com), which exceeds the VRAM of a T4 (16GB). To address this, we [quantize](https://www.youtube.com/watch?v=TPcXVJ1VSRI&amp;ref=blog.langchain.com) the model parameters, which means binning the values (e.g., to 16 values in the case of 4 bit quantization), which reduces the memory required to store the model (7B * 4 bits / parameter =3.5GB) ~[8](https://finbarr.ca/how-is-llama-cpp-possible/?ref=blog.langchain.com)-fold.

### **LoRA and qLoRA**

With the model in memory, we still need a way to fine-tune within the constraint of the remaining GPU resources. For this, parameter-efficient fine-tuning (PEFT) is a common approach: [LoRA](https://arxiv.org/abs/2106.09685?ref=blog.langchain.com) freezes the pre-trained model weights and injects trainable rank decomposition matrices into each layer of the model architecture (see [here](https://rentry.org/llm-training?ref=blog.langchain.com#low-rank-adaptation-lora_1)), reducing the number of trainable parameters for fine-tuning (e.g., [~1% of the total model](https://www.youtube.com/watch?v=TPcXVJ1VSRI&amp;ref=blog.langchain.com)). [qLoRA](https://arxiv.org/abs/2305.14314?ref=blog.langchain.com) extends this by freezing *quantized* weights. During fine-tuning frozen weights are [de-quantized](https://www.youtube.com/watch?v=TPcXVJ1VSRI&amp;ref=blog.langchain.com) for forward and backward passes, but *only* the (small set of) LoRA adapters are saved in memory, reducing fine-tuned model footprint.

### Training

We started with a pre-trained LLaMA-7b chat model `llama-2-7b-chat-hf` and fine-tuned on the ~1500 instructions in [CoLab](https://colab.research.google.com/drive/1tpywvzwOS74YndNXhI8NUaEfPeqOc7ub?usp=sharing&amp;ref=blog.langchain.com#scrollTo=v1tOYeVGtQKJ) on an A100. For training configuration, we used LLaMA fine-tuning parameters from [here](https://mlabonne.github.io/blog/posts/Fine_Tune_Your_Own_Llama_2_Model_in_a_Colab_Notebook.html?ref=blog.langchain.com): BitsAndBytes loads the base model with 4-bit precision but forward and backward passes are in fp16. We use [Supervised Fine-Tuning](https://huggingface.co/docs/trl/main/en/sft_trainer?ref=blog.langchain.com) (SFT) for fine-tuning on our instructions, which is quite fast (&lt; 15 minutes) on an A100 for this small data volume.

### OpenAI Finetuning

To fine-tune OpenAI&#x27;s GPT-3.5-turbo chat model, we selected 50 examples from the training dataset and converted them to a list of chat messages in the expected format:

`{
    &quot;messages&quot;: [
        {
            &quot;role&quot;: &quot;user&quot;,
            &quot;content&quot;: &quot;Extract triplets from the following sentence:\n\n{sentence}&quot;},
        {
            &quot;role&quot;: &quot;assistant&quot;,
            &quot;content&quot;: &quot;{triples}&quot;
        },
        ...
    ]
}
`

Since the base model is so broadly capable, we don&#x27;t need much data to achieve the desired behavior. The training data is meant to steer the model to always generate the correct format and style rather than to teach it substantial information.  As we will see in the evaluation section below, the 50 training examples were sufficient to get the model to predict triplets in the correct format each time.

We uploaded the fine-tuning data to via the `openai` SDK and used the resulting model directly in LangChain&#x27;s `ChatOpenAI` class. The fine-tuned model can be used directly:

`from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(model=&quot;ft:gpt-3.5-turbo-0613:{openaiOrg}::{modelId}&quot;)
`

The whole process took only a few minutes and required no code changes in our chain, apart from removing the need to add in few-shot examples in the prompt template. We then benchmarked this model against the others to quantify its performance. You can see an example of the whole process in our [CoLab](https://colab.research.google.com/drive/1YCyDHPSl0d_ULubCVshrP5hLqUCorr7d?usp=sharing&amp;ref=blog.langchain.com) notebook.

### Evaluation

We evaluated each model using LangSmith, applying an LLM (GPT-4) evaluator to grade each prediction, which is instructed to identify factual discrepancies between the labels and the predicted triplets. This penalized results when it predicts triplets that are not present in the label or when the prediction fails to include a triplet, but it will be lenient if the exact wording of the object or relation differs in a non-meaningful way. The evaluator grades results on a scale from 0-100. We ran the evaluations in [CoLab](https://colab.research.google.com/drive/1tpywvzwOS74YndNXhI8NUaEfPeqOc7ub?usp=sharing&amp;ref=blog.langchain.com) to easily configure our custom evaluator and chains to test.

The table below shows the evaluation results for the llama base chat model and the fine-tuned variant. For comparison, we also benchmarked 3 chains using OpenAI’s chat models: `gpt-3.5-turbo` using a few-shot prompt, a `gpt-3.5-turbo` model [fine-tuned](https://openai.com/blog/gpt-3-5-turbo-fine-tuning-and-api-updates?ref=blog.langchain.com) on 50 training data points, and a few-shot `gpt-4` chain:

- Few-shot prompting of GPT-4 performs the best
- Fine-tuned GPT-3.5 is the runner up
- Fine-tuned LLaMA-7b-chat exceeds the performance of GPT-3.5
- And fine-tuned LLaMA-7b-chat is ~29% better than baseline LLaMA-7b-chat

Fine-tuned llama-2

Base llama-2 chat model

few-shot gpt-3.5-turbo

finetuned gpt-3.5-turbo

few-shot gpt-4

Score

49%

38%

40%

56%

59%

### Analysis

We use LangSmith to characterize common failure modes and better understand where the fine-tuned model behaves better than the base model. By filtering for low-scored predictions, we can see cases where baseline LLaMA-7b-chat comically hallucinates:  in the below case the LLM thinks that the subject is Homer Simpson and casually answers outside the scope of the desired format ([here](https://smith.langchain.com/public/8c1c5381-e176-4838-927b-763dfc7cd395/r?ref=blog.langchain.com)). The fine-tuned LLaMA-7b-chat ([here](https://smith.langchain.com/public/ad215bba-22ab-46aa-9e02-c6614525d092/r?ref=blog.langchain.com)) gets much closer to the reference (ground truth).

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1a9a2e6df4d389b2758_image-14.png)Example of the base model hallucinating by inferring too much information from its pretrained knowledge.

Even with few-shot examples, the baseline LLaMA-7b-chat has a tendency to answer in an informal chit-chat style ([here](https://smith.langchain.com/public/80fa28ef-830f-487f-a6b6-07977db69c4a/r?ref=blog.langchain.com)).

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1a9a2e6df4d389b2760_image-15.png)The base llama model often injects narrative even when not asked.

In contrast, the fine-tuned model tends to generate text ([here](https://smith.langchain.com/public/f02a9156-e1f1-4274-8b77-d883cf45955c/r?ref=blog.langchain.com)) that is aligned with the desired answer format and refrains from adding unwanted dialog.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1a9a2e6df4d389b276c_image-16.png)

The fine-tuned model still had instances where it failed to generate the desired content. In the example below ([link](https://smith.langchain.com/public/bdd7df30-177e-4e19-a280-8cd6173f002c/r?ref=blog.langchain.com)) the model repeated the instructions instead of generating the extracted results. This could be fixed with various approach such as different decoding parameters (or using logit biasing), more instructions, a larger base model (e.g., 13b), or improved instructions (prompt engineering).

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1a9a2e6df4d389b2768_image-19.png)The fine-tuned model occasionally become repetitive.

We can contrast the above few-shot prompted GPT-4 below ([link](https://smith.langchain.com/public/26ad7f19-9bf7-4236-8a3e-d910f099f14e/r?ref=blog.langchain.com)), which is able to extract reasonable triplets without fine-tuning on the training dataset.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1a9a2e6df4d389b276f_image-20.png)

### Conclusion

We can distill a few central lessons:

- **LangSmith can help address pain points in the fine-tuning workflow, such as data collection, evaluation, and inspection of results. **We show how LangSmith makes it easy to collect and load datasets as well as run evaluations and inspect specific generations.
- **RAG or few-shot prompting **[**should**](https://twitter.com/rachel_l_woods/status/1692577254914638340?s=20&amp;ref=blog.langchain.com)** **[**be**](https://www.tidepool.so/2023/08/17/why-you-probably-dont-need-to-fine-tune-an-llm/?ref=blog.langchain.com)** **[**considered**](https://twitter.com/karpathy/status/1655994367033884672?s=20&amp;ref=blog.langchain.com)** carefully before jumping to more challenging and costly fine-tuning. **Few-shot prompting GPT-4 actually performs better than all of our fine-tuned variants.
- **Fine-tuning small open source models on well-defined tasks can outperform much larger generalist models.** Just as Anyscale and other have reported [previously](https://www.anyscale.com/blog/fine-tuning-llama-2-a-comprehensive-case-study-for-tailoring-models-to-unique-applications?ref=blog.langchain.com), we see that a fine-tuned LLaMA2-chat-7B model exceeds the performance of a much larger generalist LLM (GPT-3.5-turbo).
- **There are numerous levers to improve fine-tuning performance, most notably careful task definition and dataset curation. **Some works, such as [LIMA](https://arxiv.org/abs/2305.11206?ref=blog.langchain.com), have reported impressive performance by fine-tuning LLaMA on as few as 1000 instruction that were selected for high quality. Further data collection / cleaning, using a larger base model (e.g., LLaMA 13B), and scaling up with GPU services for fine-tuning ([Lambda Labs](https://lambdalabs.com/?ref=blog.langchain.com), [Modal](https://modal.com/?ref=blog.langchain.com), [Vast.ai](http://vast.ai/?ref=blog.langchain.com), [Mosaic](https://www.mosaicml.com/?ref=blog.langchain.com), [Anyscale](https://www.anyscale.com/blog/fine-tuning-llama-2-a-comprehensive-case-study-for-tailoring-models-to-unique-applications?ref=blog.langchain.com), etc) are all foreseeable ways to improve these results.

Overall, these results (and the linked [CoLab](https://colab.research.google.com/drive/1tpywvzwOS74YndNXhI8NUaEfPeqOc7ub?usp=sharing&amp;ref=blog.langchain.com#scrollTo=pCf_83Q62_Nl)) provide a quick recipe for fine-tuning open source LLMs using LangSmith a tool to help with the full workflow.

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef96ff74c638e982ff68c6_86%20(1).png)Agent ArchitectureLangSmithOpen Source

#### How LangSmith and LangChain OSS Help You Meet EU AI Act Requirements

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0003a1af368dfae13c23c_jacob-talbot.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Jacob TalbotBecca WengApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/langsmith-langchain-oss-eu-ai-act)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e251cee3c69c0b64e26c79_case-study-16_9%20(1).png)Case StudiesLangSmith

#### How Credit Genie used Insights Agent to improve their AI financial assistant

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e251111d491175462a384c_david-li.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e25199461e789ce4b875a7_jeffrey-ngai.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e2518d5b449e720f9f295a_goyo-lozano-palacio.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e2515f9f57e45d15dbd331_charles-yuan.png)David LiJeffrey NgaiGoyo Lozano PalacioCharles YuanApril 20, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)5min[](/blog/credit-genie-insights-agent-financial-assistant)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e113adb98acef39fe4aa32_Reusable-evaluators.png)Observability &amp; EvalsLangSmith

#### Reusable Evaluators and Evaluator Templates in LangSmith

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0006d57fa417eb9caf388_catherine-qiao.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0003a1af368dfae13c23c_jacob-talbot.png)Catherine QiaoJacob TalbotApril 16, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/reusable-langsmith-evaluator-templates)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)