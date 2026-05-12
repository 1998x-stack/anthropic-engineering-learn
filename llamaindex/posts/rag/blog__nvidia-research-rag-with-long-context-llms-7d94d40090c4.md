---
title: "RAG With Long-Context LLMs: NVIDIA Study Guide | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/nvidia-research-rag-with-long-context-llms-7d94d40090c4"
category: "rag"
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







# Introduction

## Why Long Context Matters and How Retrieval Augmentation Steps In:

In the dynamic landscape of LLMs, two methods have gained traction and seem to be taking center stage: expanding the context window of Large Language Models (LLMs) and enhancing these models with retrieval capabilities. The continued evolution of GPU technology, coupled with breakthroughs in attention mechanisms, has given rise to long-context LLMs. Simultaneously, the concept of retrieval — where LLMs pick up only the most relevant context from a standalone retriever — promises a revolution in efficiency and speed.



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



In the midst of these evolving narratives, some interesting questions emerge:

- Retrieval-augmentation versus long context window, which one is better for downstream tasks?
- Can both methods be combined to get the best of both worlds?

To dissect these questions, in this blog post we turn to [NVIDIA’s recent study](https://arxiv.org/pdf/2310.03025v1.pdf), which harnesses the power of two powerful LLMs: the proprietary GPT — 43B and LLaMA2–70B, the research strives to provide actionable insights for AI practitioners.

## Prior Research and the NVIDIA Divergence:

Interestingly, while NVIDIA’s findings are interesting in many respects, Another recent work by [Bai et al. (2023)](https://arxiv.org/abs/2308.14508) also ventured into similar territory, although with differing outcomes.

Their work explored the impact of retrieval on long context LLMs, evaluating models like GPT-3.5-Turbo-16k and Llama2–7B-chat-4k. However, their findings diverge from NVIDIA’s in crucial ways. [Bai et al.](https://arxiv.org/abs/2308.14508) discerned that retrieval was beneficial only for the Llama2–7B-chat-4k with a 4K context window, but not for extended context models like GPT-3.5-Turbo-16k. One hypothesis for this difference centers on the challenges tied to experiments using black-box APIs and the smaller white-box LLMs they employed, which potentially had limited capability to integrate context through retrieval.

NVIDIA’s work distinguishes itself by tapping into much larger LLMs, yielding results that not only match top-tier models like ChatGPT-3.5 but even indicate further enhancements when incorporating retrieval methods.

# Models, Datasets, and Evaluation Metrics

## Large Language Models (LLMs) Explored:

The researchers delved deep into the potential of large language models for tasks like generative QA and summarization. Specifically, two models were the primary focus:

- **Nemo GPT-43B:** A proprietary 43 billion parameter model trained on 1.1T tokens, 70% of which were in English. This model was fed a rich diet of web archives, Wikipedia, Reddit, books, and more. It contains 48 layers and is trained using RoPE embeddings.
- **LLaMA2–70B:** A publicly available 70B parameter model trained on 2T tokens, primarily in English. It’s structured with 80 layers and also utilizes RoPE embeddings.

## Context Window Extension:

To enhance the models’ capability to process longer contexts, their initial 4K context window length was augmented. The GPT-43B was modified to handle 16K, while the LLaMA2–70B was expanded to both 16K and 32K, employing the position interpolation method.

## Instruction Tuning:

To optimize the LLMs for the tasks at hand, instruction tuning was implemented. A diverse dataset blend, comprising sources like Soda, ELI5, FLAN, and others, was created. A consistent format template was adopted for multi-turn dialogue training, and the models were meticulously fine-tuned to accentuate the answer segment.

## Retrieval Models Tested:

Three retrieval systems were put to the test:

- **Dragon:** A state-of-the-art dual encoder model for both supervised and zero-shot information retrieval.
- **Contriever:** Utilizes a basic contrastive learning framework and operates unsupervised.
- **OpenAI embedding:** The latest version was used, accepting a maximum input of 8,191 tokens.

The retrieval approach entailed segmenting each document into 300-word sections, encoding both questions and these chunks, and then merging the most pertinent chunks for response generation.

## Datasets Used for Evaluation:

The study employed seven diverse datasets, sourced from the Scroll benchmark and LongBench.

A snapshot of these datasets includes:

- **QMSum:** A query-based summarization dataset, QMSum consists of transcripts from diverse meetings and their corresponding summaries, built upon contextual queries.
- **Qasper:** A question-answering dataset centered on NLP papers, Qasper offers a mix of abstractive, extractive, yes/no, and unanswerable questions from the Semantic Scholar Open Research Corpus.
- **NarrativeQA:** Aimed at question-answering over entire books and movie scripts, NarrativeQA provides question-answer pairs created from summaries of these extensive sources.
- **QuALITY:** A multiple-choice question answering set based on stories and articles, QuALITY emphasizes thorough reading, with half the questions designed to be challenging and require careful consideration.
- **MuSiQue:** Designed for multi-hop reasoning in question answering, MuSiQue creates multi-hop questions from single-hop ones, emphasizing connected reasoning and minimizing shortcuts.
- **HotpotQA:** Based on Wikipedia, HotpotQA requires reading multiple supporting documents for reasoning. It features diverse questions and provides sentence-level support for answers.
- **MultiFieldQA-en:** Curated to test long-context understanding across fields, MFQA uses sources like legal documents and academic papers, with annotations done by Ph.D. students.

## Evaluation Metrics:

The research team used a wide range of metrics suited to each dataset. The geometric mean of ROUGE scores for QM, the exact matching (EM) score for QLTY, and F1 scores for others were the primary metrics.

# Results

- Baseline models without retrieval, having a 4K sequence length, performed poorly since valuable texts get truncated.
- With retrieval, performance for 4K models like LLaMA2–70B-4K and GPT-43B-4K significantly improved.
- HotpotQA, a multi-hop dataset, particularly benefits from longer sequence models.
- Models with longer contexts (16K, 32K) outperform their 4K counterparts even when fed the same evidence chunks.
- There exists a unique “U-shaped” performance curve for LLMs due to the `lost in the middle` phenomenon, making them better at utilizing information at the beginning or end of the input.
- The study presents a contrasting perspective to LongBench’s findings, emphasizing that retrieval is beneficial for models regardless of their context window size.

## Comparing to OpenAI Models:

- The LLaMA2–70B-32k model with retrieval surpasses the performance of GPT-3.5-turbo variants and is competitive with Davinci-003, underscoring its robustness in handling long context tasks.

## Comparison of Different Retrievers:

- Retrieval consistently enhances the performance across different retrievers.
- Public retrievers outperformed proprietary ones like OpenAI embeddings.

## Comparing with the number of retrieved chunks:

- The best performance is achieved by retrieving the top 5 or 10 chunks. Retrieving more, up to 20 chunks, doesn’t offer additional benefits and can even degrade performance.
- The deterioration in performance when adding more chunks could be due to the `lost-in-the-middle` phenomenon or the model being sidetracked by non-relevant information.

# Conclusion

As we delved deep into understanding how retrieval augmentation and long-context extension interact when applied to leading language models fine-tuned for long-context question-answering and summarization tasks. Here are some things to be noted:

- **Boost in Performance with Retrieval**: Implementing retrieval techniques significantly enhances the performance of both shorter 4K context language models and their longer 16K/32K context counterparts.
- **Efficiency of 4K Models with Retrieval**: 4K context language models, when combined with retrieval augmentation, can achieve performance levels similar to 16K long context models. Plus, they have the added advantage of being faster during the inference process.
- **Best Model Performance**: After enhancing with both context window extension and retrieval augmentation, the standout model, LLaMA2–70B-32k-ret (LLaMA2–70B-32k with retrieval), surpasses well-known models like GPT-3.5-turbo-16k and davinci-003.

# References:

- [Retrieval meets long context, large language models.](https://arxiv.org/pdf/2310.03025v1.pdf)
- [Longbench: A bilingual, multitask benchmark for long context understanding.](https://arxiv.org/abs/2308.14508)

We trust that this blog post on the review of the paper on retrieval augmentation with long-context LLMs has furnished you with meaningful insights. We’re keen to hear if your experiments align with our findings or present new perspectives — divergent results always make for interesting discussions and further exploration.