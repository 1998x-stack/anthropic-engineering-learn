---
title: "RAG Evaluation: GPT-4 vs Prometheus Results | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/llamaindex-rag-evaluation-showdown-with-gpt-4-vs-open-source-prometheus-model-14cdca608277"
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

Evaluation is a critical component in enhancing your Retrieval-Augmented Generation (RAG) pipeline, traditionally reliant on GPT-4. However, the open-source [Prometheus model](https://huggingface.co/kaist-ai/prometheus-13b-v1.0) has recently emerged as a notable alternative for such evaluation tasks.



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



In this blog post, we will demonstrate how to effectively use the Prometheus model for evaluation purposes, integrating it smoothly with the LlamaIndex framework by comparing it with GPT-4 evaluation. Our primary focus will be on assessing RAG using our standard metrics: Correctness, Faithfulness, and Context Relevancy. To provide a clearer understanding, here’s what each metric entails:

- **Correctness**: Assesses whether the generated answer aligns with the reference answer, given the query (this necessitates labeled data).
- **Faithfulness**: Measures if the answer remains true to the retrieved contexts, essentially checking for the absence of hallucinations.
- **Context Relevancy**: Evaluate the relevance of both the retrieved context and the answer to the query.

For an in-depth exploration, our documentation is available [here](https://docs.llamaindex.ai/en/stable/module_guides/evaluating/root.html).

For those who are exploring the Prometheus model for the first time, the paper summary by [Andrei](https://www.linkedin.com/in/nerdai/) is an excellent resource to gain a better understanding.

![](/blog/images/1*W8U1VmBa_O38064ffw7w1g.png)

A crucial aspect to remember when using the Prometheus model is its dependence on rubric scores within the prompt for effective evaluation. An example of such Rubric scores in the context of `Correctness Evaluation`is as follows:

>

###Score Rubrics:
Score 1: If the generated answer is not relevant to the user query and reference answer.
Score 2: If the generated answer is according to reference answer but not relevant to user query.
Score 3: If the generated answer is relevant to the user query and reference answer but contains mistakes.
Score 4: If the generated answer is relevant to the user query and has the exact same metrics as the reference answer, but it is not as concise.
Score 5: If the generated answer is relevant to the user query and fully correct according to the reference answer.

You’ll find comprehensive details on this in the prompts section of this tutorial.

For a detailed walkthrough of the code, feel free to follow along with our [Google Colab Notebook](https://colab.research.google.com/github/run-llama/llama_index/blob/main/docs/examples/evaluation/prometheus_evaluation.ipynb) accompanying this blog post. In the notebook, we conducted evaluations on both the `Paul Graham Essay Text`and the `Llama2 Paper`. However, for this blog post, we’ll focus exclusively on the Llama2 Paper, as it revealed some particularly interesting insights.

# Outline:

- Setup Evaluation Pipeline.

- Download Dataset.
- Define LLMs (Prometheus, GPT-4) needed for evaluation.
- Define Correctness, Faithfulness, and Relevancy prompt templates.
- Define Prometheus, GPT-4 Evaluators, and Batch Eval Runner.
- Run the Correctness, Faithfulness, and Relevancy Evaluation over the Llama2 dataset.

2. Results

- Correctness Evaluation score distribution between Prometheus and GPT-4.
- Feedback comparison between Prometheus and GPT-4 for correctness evaluation.
- Faithfulness and Relevancy Evaluation scores with Prometheus and GPT-4.
- Hamming Distance comparison between Prometheus and GPT-4.
- Feedback comparison between Prometheus and GPT-4 for Faithfulness and Relevancy

3. Summary with Cost Analysis.

# Setup Evaluation Pipeline

Please be aware that certain functions mentioned here are not defined in detail within the blog post. We have showcased only the essential parts of the pipeline to provide an overview of its setup. For a comprehensive code walkthrough, we recommend visiting our [Google Colab Notebook](https://colab.research.google.com/github/run-llama/llama_index/blob/main/docs/examples/evaluation/prometheus_evaluation.ipynb).

## Download Dataset

We will use the Llama2 paper dataset from Llama Datasets which contains 100 questions and their reference answers.

from llama_index.llama_dataset import download_llama_dataset

llama2_rag_dataset, llama2_documents = download_llama_dataset(
    "Llama2PaperDataset", "./data/llama2"
)

## Define Prometheus LLM hosted on HuggingFace And OpenAI for creating an Index (RAG) pipeline

We need to host the model on HF Inference endpoint using Nvidia A100 GPU, 80 GB RAM.

from llama_index.llms import HuggingFaceInferenceAPI
import os

HF_TOKEN = "YOUR HF TOKEN"
HF_ENDPOINT_URL = "HF END POINT URL"

prometheus_llm = HuggingFaceInferenceAPI(
    model_name=HF_ENDPOINT_URL,
    token=HF_TOKEN,
    temperature=0.1,
    do_sample=True,
    top_p=0.95,
    top_k=40,
    repetition_penalty=1.1,
)

os.environ["OPENAI_API_KEY"] = "YOUR OPENAI API KEY"

from llama_index.llms import OpenAI

gpt4_llm = OpenAI("gpt-4")

## Prompt templates.

We will use the same prompts for the Prometheus model and GPT-4 to make consistent performance comparisons.

**Correctness Evaluation Prompt:**

prometheus_correctness_eval_prompt_template = """###Task Description: An instruction (might include an Input inside it), a query, a response to evaluate, a reference answer that gets a score of 5, and a score rubric representing a evaluation criteria are given.
   1. Write a detailed feedback that assesses the quality of the response strictly based on the given score rubric, not evaluating in general.
   2. After writing a feedback, write a score that is either 1 or 2 or 3 or 4 or 5. You should refer to the score rubric.
   3. The output format should look as follows: 'Feedback: (write a feedback for criteria) [RESULT] (1 or 2 or 3 or 4 or 5)'
   4. Please do not generate any other opening, closing, and explanations.
   5. Only evaluate on common things between generated answer and reference answer. Don't evaluate on things which are present in reference answer but not in generated answer.

   ###The instruction to evaluate: Your task is to evaluate the generated answer and reference answer for the query: {query}

   ###Generate answer to evaluate: {generated_answer}

   ###Reference Answer (Score 5): {reference_answer}

   ###Score Rubrics:
   Score 1: If the generated answer is not relevant to the user query and reference answer.
   Score 2: If the generated answer is according to reference answer but not relevant to user query.
   Score 3: If the generated answer is relevant to the user query and reference answer but contains mistakes.
   Score 4: If the generated answer is relevant to the user query and has the exact same metrics as the reference answer, but it is not as concise.
   Score 5: If the generated answer is relevant to the user query and fully correct according to the reference answer.

   ###Feedback:"""
**Faithfulness Evaluation Prompt:**

prometheus_faithfulness_eval_prompt_template= """###Task Description: An instruction (might include an Input inside it), an information, a context, and a score rubric representing evaluation criteria are given.
1. You are provided with evaluation task with the help of information, context information to give result based on score rubrics.
2. Write a detailed feedback based on evaluation task and the given score rubric, not evaluating in general.
3. After writing a feedback, write a score that is YES or NO. You should refer to the score rubric.
4. The output format should look as follows: "Feedback: (write a feedback for criteria) [RESULT] (YES or NO)”
5. Please do not generate any other opening, closing, and explanations.

###The instruction to evaluate: Your task is to evaluate if the given piece of information is supported by context.

###Information: {query_str}

###Context: {context_str}

###Score Rubrics:
Score YES: If the given piece of information is supported by context.
Score NO: If the given piece of information is not supported by context

###Feedback: """

prometheus_faithfulness_refine_prompt_template= """###Task Description: An instruction (might include an Input inside it), a information, a context information, an existing answer, and a score rubric representing a evaluation criteria are given.
1. You are provided with evaluation task with the help of information, context information and an existing answer.
2. Write a detailed feedback based on evaluation task and the given score rubric, not evaluating in general.
3. After writing a feedback, write a score that is YES or NO. You should refer to the score rubric.
4. The output format should look as follows: "Feedback: (write a feedback for criteria) [RESULT] (YES or NO)"
5. Please do not generate any other opening, closing, and explanations.

###The instruction to evaluate: If the information is present in the context and also provided with an existing answer.

###Existing answer: {existing_answer}

###Information: {query_str}

###Context: {context_msg}

###Score Rubrics:
Score YES: If the existing answer is already YES or If the Information is present in the context.
Score NO: If the existing answer is NO and If the Information is not present in the context.

###Feedback: """**Relevancy Evaluation Prompt:**

prometheus_relevancy_eval_prompt_template = """###Task Description: An instruction (might include an Input inside it), a query with response, context, and a score rubric representing evaluation criteria are given.
       1. You are provided with evaluation task with the help of a query with response and context.
       2. Write a detailed feedback based on evaluation task and the given score rubric, not evaluating in general.
       3. After writing a feedback, write a score that is YES or NO. You should refer to the score rubric.
       4. The output format should look as follows: "Feedback: (write a feedback for criteria) [RESULT] (YES or NO)”
       5. Please do not generate any other opening, closing, and explanations.

        ###The instruction to evaluate: Your task is to evaluate if the response for the query is in line with the context information provided.

        ###Query and Response: {query_str}

        ###Context: {context_str}

        ###Score Rubrics:
        Score YES: If the response for the query is in line with the context information provided.
        Score NO: If the response for the query is not in line with the context information provided.

        ###Feedback: """

prometheus_relevancy_refine_prompt_template = """###Task Description: An instruction (might include an Input inside it), a query with response, context, an existing answer, and a score rubric representing a evaluation criteria are given.
   1. You are provided with evaluation task with the help of a query with response and context and an existing answer.
   2. Write a detailed feedback based on evaluation task and the given score rubric, not evaluating in general.
   3. After writing a feedback, write a score that is YES or NO. You should refer to the score rubric.
   4. The output format should look as follows: "Feedback: (write a feedback for criteria) [RESULT] (YES or NO)"
   5. Please do not generate any other opening, closing, and explanations.

   ###The instruction to evaluate: Your task is to evaluate if the response for the query is in line with the context information provided.

   ###Query and Response: {query_str}

   ###Context: {context_str}

   ###Score Rubrics:
   Score YES: If the existing answer is already YES or If the response for the query is in line with the context information provided.
   Score NO: If the existing answer is NO and If the response for the query is in line with the context information provided.

   ###Feedback: """

## Define Correctness, FaithFulness, Relevancy Evaluators

from llama_index import ServiceContext
from llama_index.evaluation import (
    CorrectnessEvaluator,
    FaithfulnessEvaluator,
    RelevancyEvaluator,
)
from llama_index.callbacks import CallbackManager, TokenCountingHandler
import tiktoken

# Provide Prometheus model in service_context
prometheus_service_context = ServiceContext.from_defaults(llm=prometheus_llm)

# CorrectnessEvaluator with Prometheus model
prometheus_correctness_evaluator = CorrectnessEvaluator(
    service_context=prometheus_service_context,
    parser_function=parser_function,
    eval_template=prometheus_correctness_eval_prompt_template,
)

# FaithfulnessEvaluator with Prometheus model
prometheus_faithfulness_evaluator = FaithfulnessEvaluator(
    service_context=prometheus_service_context,
    eval_template=prometheus_faithfulness_eval_prompt_template,
    refine_template=prometheus_faithfulness_refine_prompt_template,
)

# RelevancyEvaluator with Prometheus model
prometheus_relevancy_evaluator = RelevancyEvaluator(
    service_context=prometheus_service_context,
    eval_template=prometheus_relevancy_eval_prompt_template,
    refine_template=prometheus_relevancy_refine_prompt_template,
)

# Set the encoding model to `gpt-4` for token counting.
token_counter = TokenCountingHandler(
    tokenizer=tiktoken.encoding_for_model("gpt-4").encode
)

callback_manager = CallbackManager([token_counter])

# Provide GPT-4 model in service_context
gpt4_service_context = ServiceContext.from_defaults(
    llm=gpt4_llm, callback_manager=callback_manager
)

# CorrectnessEvaluator with GPT-4 model
gpt4_correctness_evaluator = CorrectnessEvaluator(
    service_context=gpt4_service_context,
    # parser_function=parser_function,
)

# FaithfulnessEvaluator with GPT-4 model
gpt4_faithfulness_evaluator = FaithfulnessEvaluator(
    service_context=gpt4_service_context,
    eval_template=prometheus_faithfulness_eval_prompt_template,
    refine_template=prometheus_faithfulness_refine_prompt_template,
)

# RelevancyEvaluator with GPT-4 model
gpt4_relevancy_evaluator = RelevancyEvaluator(
    service_context=gpt4_service_context,
    eval_template=prometheus_relevancy_eval_prompt_template,
    refine_template=prometheus_relevancy_refine_prompt_template,
)

# create a dictionary of evaluators
prometheus_evaluators = {
    "correctness": prometheus_correctness_evaluator,
    "faithfulness": prometheus_faithfulness_evaluator,
    "relevancy": prometheus_relevancy_evaluator,
}

gpt4_evaluators = {
    "correctness": gpt4_correctness_evaluator,
    "faithfulness": gpt4_faithfulness_evaluator,
    "relevancy": gpt4_relevancy_evaluator,
}

## Function to run batch evaluations on defined evaluators

from llama_index.evaluation import BatchEvalRunner

async def batch_eval_runner(
    evaluators, query_engine, questions, reference=None, num_workers=8
):
    batch_runner = BatchEvalRunner(
        evaluators, workers=num_workers, show_progress=True
    )

    eval_results = await batch_runner.aevaluate_queries(
        query_engine, queries=questions, reference=reference
    )

    return eval_results

## Get Query Engine, Questions, and References.

query_engine, rag_dataset = create_query_engine_rag_dataset("./data/llama2")

questions = [example.query for example in rag_dataset.examples]

reference = [[example.reference_answer] for example in rag_dataset.examples]

## Compute Correctness, Faithfulness, and Relevancy Evaluation.

prometheus_eval_results = await batch_eval_runner(
    prometheus_evaluators, query_engine, questions, reference
)

gpt4_eval_results = await batch_eval_runner(
    gpt4_evaluators, query_engine, questions, reference
)

# Results

## Correctness Evaluation score distribution.

## With the Prometheus Model:

> 3.0: 56.0,
1.0: 26.0,
5.0: 9.0,
4.0: 8.0,
2.0: 1.0

## With GPT-4 Model:

>

4.5: 57.99,
1.0: 6.0,
4.0: 12.0,
5.0: 10.0,
2.0: 5.0,
3.5: 5.0,
2.5: 3.0,
3.0: 1.0

## **Observation:**

Prometheus Evaluator gives more `3.0` scores compared to GPT-4 which gives `4.5`. Let’s investigate it with the help of feedback.

## Feedback comparison between Prometheus and GPT-4 for correctness.

>

***Query:**** Based on the abstract of “Llama 2: Open Foundation and Fine-Tuned Chat Models,” what are the two primary objectives achieved in this work, and what is the range of parameters for the large language models developed?*

***Generated Answer:**** The two primary objectives achieved in this work are the development and release of Llama 2, a collection of pretrained and fine-tuned large language models (LLMs), and the optimization of these models for dialogue use cases. The range of parameters for the large language models developed is from 7 billion to 70 billion.*

***Reference Answer:**** The two primary objectives achieved in the work described in the abstract of “Llama 2: Open Foundation and Fine-Tuned Chat Models” are: 1. The development and release of a collection of pretrained and fine-tuned large language models (LLMs) specifically optimized for dialogue use cases. 2. The demonstration that these fine-tuned LLMs, referred to as Llama 2-Chat, outperform open-source chat models on most benchmarks tested and may be a suitable substitute for closed-source models, particularly in terms of helpfulness and safety based on human evaluations. The range of parameters for the large language models developed in this work is from 7 billion to 70 billion parameters.*

***Prometheus Feedback:**** The generated response is relevant to the user query and correctly identifies the two primary objectives of the work described in the abstract of “Llama 2: Open Foundation and Fine-Tuned Chat Models.” However, it does not mention the demonstration of the fine-tuned LLMs outperforming open-source chat models on most benchmarks tested, which is a key point in the reference response. The range of parameters for the large language models developed is correctly identified, but the response does not mention the specific models referred to as Llama 2-Chat. So the overall score is 3.*

***Prometheus Score:**** 3.0*

***GPT-4 Feedback:**** The generated answer is relevant and almost fully correct. It correctly identifies the two primary objectives and the range of parameters for the large language models. However, it misses the detail about Llama 2-Chat outperforming other models on most benchmarks and potentially being a suitable substitute for closed-source models.*

***GPT-4 Score:**** 4.5*

**Observation:**

The feedback from Prometheus is a little more precise compared to GPT-4 and it penalizes and gives a score of `3.0`but GPT-4 gives a score of `4.5`. Prometheus penalizes more even if some of the text in the reference answer is missed in the generated answer.

## Faithfulness and Relevancy Evaluation scores.

## With the Prometheus Model:

>

faithfulness Score: 0.39
relevancy Score: 0.57

## With GPT-4 Model:

>

faithfulness Score: 0.93
relevancy Score: 0.98

**Observation:**

We see a higher faithfulness and relevancy score with GPT-4 compared to the Prometheus model. Let’s investigate it through feedback.

## Hamming Distance comparison between Prometheus and GPT-4:

>

Faithfulness Hamming Distance: 58
Relevancy Hamming Distance: 41

## Observation:

The comparison reveals that approximately `42%` of the scores in case of `Faithfulness` and `59%` in case of `Relevancy` are common between Prometheus and GPT-4 evaluations. This indicates a decent amount of correlation in terms of faithfulness and relevance scoring between the Prometheus and GPT-4 models.

## Feedback comparison between Prometheus and GPT-4 for Faithfulness and Relevancy

>

**Query:** Based on the abstract of “Llama 2: Open Foundation and Fine-Tuned Chat Models,” what are the two primary objectives achieved in this work, and what is the range of parameters for the large language models developed? Generated Answer: The two primary objectives achieved in this work are the development and release of Llama 2, a collection of pretrained and fine-tuned large language models (LLMs), and the optimization of these models for dialogue use cases. The range of parameters for the large language models developed is from 7 billion to 70 billion.

**Context-1:** Llama 2 : Open Foundation and Fine-Tuned Chat Models Hugo Touvron∗Louis Martin†Kevin Stone† Peter Albert Amjad Almahairi Yasmine Babaei Nikolay Bashlykov Soumya Batra Prajjwal Bhargava Shruti Bhosale Dan Bikel Lukas Blecher Cristian Canton Ferrer Moya Chen Guillem Cucurull David Esiobu Jude Fernandes Jeremy Fu Wenyin Fu Brian Fuller Cynthia Gao Vedanuj Goswami Naman Goyal Anthony Hartshorn Saghar Hosseini Rui Hou Hakan Inan Marcin Kardas Viktor Kerkez Madian Khabsa Isabel Kloumann Artem Korenev Punit Singh Koura Marie-Anne Lachaux Thibaut Lavril Jenya Lee Diana Liskovich Yinghai Lu Yuning Mao Xavier Martinet Todor Mihaylov Pushkar Mishra Igor Molybog Yixin Nie Andrew Poulton Jeremy Reizenstein Rashi Rungta Kalyan Saladi Alan Schelten Ruan Silva Eric Michael Smith Ranjan Subramanian Xiaoqing Ellen Tan Binh Tang Ross Taylor Adina Williams Jian Xiang Kuan Puxin Xu Zheng Yan Iliyan Zarov Yuchen Zhang Angela Fan Melanie Kambadur Sharan Narang Aurelien Rodriguez Robert Stojnic Sergey Edunov Thomas Scialom∗ GenAI, Meta Abstract In this work, we develop and release Llama 2, a collection of pretrained and fine-tuned large language models (LLMs) ranging in scale from 7 billion to 70 billion parameters. Our fine-tuned LLMs, called Llama 2-Chat , are optimized for dialogue use cases. Our models outperform open-source chat models on most benchmarks we tested, and based on ourhumanevaluationsforhelpfulnessandsafety,maybeasuitablesubstituteforclosed- source models. We provide a detailed description of our approach to fine-tuning and safety improvements of Llama 2-Chat in order to enable the community to build on our work and contribute to the responsible development of LLMs. ∗Equal contribution, corresponding authors: {tscialom, htouvron}@meta.com †Second author Contributions for all the authors can be found in Section A.1.arXiv:2307.09288v2 [cs.CL] 19 Jul 2023

**Context-2: **(2021)alsoilluminatesthedifficultiestiedtochatbot-oriented LLMs, with concerns ranging from privacy to misleading expertise claims. Deng et al. (2023) proposes a taxonomic framework to tackle these issues, and Bergman et al. (2022) delves into the balance between potential positive and negative impacts from releasing dialogue models. InvestigationsintoredteamingrevealspecificchallengesintunedLLMs,withstudiesbyGangulietal.(2022) and Zhuoet al. (2023) showcasing a variety ofsuccessful attack typesand their effects onthe generation of harmful content. National security agencies and various researchers, such as (Mialon et al., 2023), have also raisedredflagsaroundadvancedemergentmodelbehaviors,cyberthreats,andpotentialmisuseinareaslike biological warfare. Lastly, broader societal issues like job displacement due to accelerated AI research and an over-reliance on LLMs leading to training data degradation are also pertinent considerations (Acemoglu andRestrepo,2018;AutorandSalomons,2018;Webb,2019;Shumailovetal.,2023). Wearecommittedto continuing our work engaging with the broader policy, academic, and industry community on these issues. 7 Conclusion Inthisstudy,wehaveintroduced Llama 2,anewfamilyofpretrainedandfine-tunedmodelswithscales of7billionto70billionparameters. Thesemodelshavedemonstratedtheircompetitivenesswithexisting open-source chat models, as well as competency that is equivalent to some proprietary models on evaluation setsweexamined,althoughtheystilllagbehindothermodelslikeGPT-4. Wemeticulouslyelaboratedonthe methodsandtechniquesappliedinachievingourmodels,withaheavyemphasisontheiralignmentwiththe principlesofhelpfulnessandsafety. Tocontributemoresignificantlytosocietyandfosterthepaceofresearch, wehaveresponsiblyopenedaccessto Llama 2 andLlama 2-Chat . Aspartofourongoingcommitmentto transparency and safety, we plan to make further improvements to Llama 2-Chat in future work. 36

**Prometheus Faithfulness Feedback:** The information provided in the context is not supported by the given information. The context is about the development and release of Llama 2, a collection of pretrained and fine-tuned large language models (LLMs), and the optimization of these models for dialogue use cases. However, the information provided in the context does not align with the given information. The context does not mention the range of parameters for the large language models developed, which is the primary objective mentioned in the information. The context only talks about the development and release of Llama 2 and its optimization for dialogue use cases, but it does not provide any information about the range of parameters for the large language models developed. So the overall score is NO. [RESULT] NO

**Prometheus Faithfulness Score:** 0.0

**Prometheus Relevancy Feedback:** The response is not in line with the context information provided. The query asked for the two primary objectives achieved in the work and the range of parameters for the large language models developed. However, the response provided the abstract of the paper and mentioned the authors, which is not relevant to the query. The response also did not mention the two primary objectives achieved in the work or the range of parameters for the large language models developed. So the overall score is NO. [RESULT] NO

**Prometheus Relevancy Score:** 0.0

**GPT-4 Faithfulness Feedback:** The given piece of information is well supported by the context. The context clearly states that Llama 2, a collection of pretrained and fine-tuned large language models (LLMs), was developed and released. It also mentions that these models range in scale from 7 billion to 70 billion parameters. Furthermore, the context confirms that these models are optimized for dialogue use cases. Therefore, the information provided is accurate and is corroborated by the context. [RESULT] YES

**GPT-4 Faithfulness Score:** 1.0

**GPT-4 Relevancy Feedback:** The response accurately reflects the context provided. The response correctly identifies the two primary objectives of the work as the development and release of Llama 2, a collection of pretrained and fine-tuned large language models (LLMs), and the optimization of these models for dialogue use cases. This is in line with the information provided in the abstract of the context. The response also correctly states the range of parameters for the large language models developed as being from 7 billion to 70 billion, which is also confirmed in the context. Therefore, the response is in line with the context information provided. [RESULT] YES

**GPT-4 Relevancy Score:** 1.0

# Observation:

- Prometheus: If you compare the feedback and contexts, there is mention of a range of parameters in the context and response but the feedback says the model could not find such information.
- GPT-4: Evaluates it correctly, unlike the Prometheus model.

# Summary

- The cost for evaluation (approx.): `$1.5` for Prometheus Model and `$15` for GPT4.
- The Prometheus model, though offering more detailed feedback than GPT-4, occasionally provides incorrect feedback, necessitating cautious application.
- If a generated answer lacks certain facts present in the reference answer, the Prometheus model applies stricter penalties to scores than GPT-4.
- The faithfulness and relevancy feedback of Prometheus shows more hallucinations/ wrong interpretations in the feedback compared to GPT-4.

# **Note:**

- You can check detailed analysis with code on [Google Colab Notebook](https://colab.research.google.com/github/run-llama/llama_index/blob/main/docs/examples/evaluation/prometheus_evaluation.ipynb).
- The endpoint on HF is served on AWS Nvidia A100G · 1x GPU · 80 GB which costs $6.5/h. (We extend our gratitude to the Hugging Face team for their assistance whenever we encounter issues.)
- We used the [Prometheus model](https://huggingface.co/kaist-ai/prometheus-13b-v1.0) for the analysis here. We also made a similar analysis with the [GPTQ Quantized version](https://huggingface.co/TheBloke/prometheus-13B-v1.0-GPTQ) of the [Prometheus model](https://huggingface.co/kaist-ai/prometheus-13b-v1.0) and observed a bit more hallucinations in feedback compared to the original unquantized model. Thanks to the authors of the paper for open-sourcing the model and [Tom Jobbins](https://twitter.com/TheBlokeAI) for the quantized version of the model.

# References:

- [Prometheus paper](https://arxiv.org/abs/2310.08491).
- [Prometheus model on HuggingFace.](https://huggingface.co/kaist-ai/prometheus-13b-v1.0)