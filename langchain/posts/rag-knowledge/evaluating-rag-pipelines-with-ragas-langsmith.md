---
title: "Evaluating RAG pipelines with Ragas + LangSmith"
author: "LangChain Accounts"
date: "2023-08-24"
url: "https://www.langchain.com/blog/evaluating-rag-pipelines-with-ragas-langsmith"
---

Tutorials &amp; How-TosPartnerLangSmith

# Evaluating RAG pipelines with Ragas + LangSmith

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamAugust 23, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)10min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb19744d72d975256f167_5-social--9-.png)*Editor&#x27;s Note: This post was written in collaboration with the *[*Ragas*](https://github.com/explodinggradients/ragas?ref=blog.langchain.com)* team. One of the things we think and talk about a lot at LangChain is how the industry will evolve to identify new monitoring and evaluation metrics that evolve beyond traditional ML ops metrics. Ragas is an exciting new framework that helps developers evaluate QA pipelines in new ways. This post shows how LangSmith and Ragas can be a powerful combination for teams that want to build reliable LLM apps.*

> How important evals are to the team is a major differentiator between folks rushing out hot garbage and those seriously building products in the space.

This [HackerNews comment](https://news.ycombinator.com/item?id=36789901&amp;ref=blog.langchain.com) emphasizes the importance of having a robust eval strategy when taking your application from a cool demo to a production-ready product. This is especially true when building LLM applications because of the underlying stochastic nature of the models powering them. You can easily build really impressive LLM applications with a few short training and verifying it on a few examples but to make it more robust you have to test it on a test dataset that matches the production distribution. This is an evolutionary process and something you will be doing throughout the lifecycle of your application but let&#x27;s see how Ragas and LangSmith can help you here.

This article is going to be specifically about QA systems (or [RAG systems](https://arxiv.org/abs/2005.11401?ref=blog.langchain.com)). Every QA pipeline has 2 components

- Retriever - which retrieves the most relevant information needed to answer the query
- Generator - which generates the answer with the retrieved information.

When evaluating a QA pipeline you have to evaluate both of these separately and together to get an overall score as well as the individual scores to pinpoint the aspects you want to improve. For example, using a better chunking strategy or embedding model can improve the retriever while using a different model or prompt can bring about changes to the generation step. You might want to measure the tendency for hallucinations in the generation step or the recall for the retrieval step.

But what metrics and datasets can you use to measure and benchmark these components? There are many conventional metrics and benchmarks for evaluating QA systems like [ROUGE](https://aclanthology.org/W04-1013/?ref=blog.langchain.com) and [BLUE](https://dl.acm.org/doi/10.3115/1073083.1073135?ref=blog.langchain.com) but they have [poor correlation with human judgment](https://arxiv.org/abs/2008.12009?ref=blog.langchain.com). Furthermore, the correlation between the performance of your pipeline over a standard benchmark (like [Beir](https://github.com/beir-cellar/beir?ref=blog.langchain.com)) and production data can vary depending on the distribution shift between both of them. Moreover, building such a golden test set is an expensive and time-consuming task.

## Leveraging LLMs for evaluations

Leveraging a strong LLM for reference-free evaluation is an upcoming solution that has shown a lot of promise. They correlate better with human judgment than traditional metrics and also require less human annotation. Papers like [G-Eval](https://arxiv.org/abs/2303.16634?ref=blog.langchain.com) have experimented with this and given promising results but there are certain shortcomings too.

LLM prefers outputs their own outputs and when asked to compare between different outputs the relative position of those outputs matters more. LLMs can also have a bias toward a value when asked to score given a range and they also prefer longer responses. Refer to the [Large Language Models are not Fair Evaluators pape](https://arxiv.org/abs/2305.17926?ref=blog.langchain.com)r for more. Ragas aims to work around these limitations of using LLMs to evaluate your QA pipelines while also providing actionable metrics using as little annotated data as possible, cheaper, and faster.

## Introducing Ragas

Ragas is a framework that helps you evaluate your QA pipelines across these different aspects. It provides you with a few metrics to evaluate the different aspects of your QA systems namely

- metrics to evaluate retrieval: offers `context_relevancy` and `context_recall` which give you the measure of the performance of your retrieval system.
- metrics to evaluate generation: offers `faithfulness` which measures hallucinations and `answer_relevancy` which measures how to the point the answers are to the question.

The harmonic mean of these 4 aspects gives you the **ragas score** which is a single measure of the performance of your QA system across all the important aspects.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb19844d72d975256f174_image-21.png)

Most of the measurements do not require any labeled data, making it easier for users to run it without worrying about building a human-annotated test dataset first. In order to run ragas all you need is a few questions and if your using `context_recall`, a reference answer. (The option to cold start your test dataset is also in the roadmap)

Now let&#x27;s see Ragas in action and try this by evaluating a QA chain build with Langchain.

## Evaluating a QA chain

We’re going to build a QA chain over the NYC Wikipedia page and run our evaluations on top of it. This is a pretty standard QA chain but feel free to check out [the docs](https://python.langchain.com/docs/use_cases/question_answering?ref=blog.langchain.com).

`from langchain.document_loaders import WebBaseLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

# load the Wikipedia page and create index
loader = WebBaseLoader(&quot;https://en.wikipedia.org/wiki/New_York_City&quot;)
index = VectorstoreIndexCreator().from_loaders([loader])

# create the QA chain
llm = ChatOpenAI()
qa_chain = RetrievalQA.from_chain_type(
    llm, retriever=index.vectorstore.as_retriever(), return_source_documents=True
)

# testing it out
question = &quot;How did New York City get its name?&quot;
result = qa_chain({&quot;query&quot;: question})
result[&quot;result&quot;]

# output
# &#x27;New York City got its name in 1664 when it was renamed after the Duke of York, who later became King James II of England. The city was originally called New Amsterdam by Dutch colonists and was renamed New York when it came under British control.&#x27;`

in order to use Ragas with LangChain, first import all the metrics you want to use from ragas.metrics. Next import the RagasEvaluatorChain which is a langchain chain wrapper to convert a ragas metric into a langchain [EvaluationChain](https://python.langchain.com/docs/guides/evaluation/?ref=blog.langchain.com).

`from ragas.metrics import faithfulness, answer_relevancy, context_relevancy, context_recall
from ragas.langchain import RagasEvaluatorChain

# make eval chains
eval_chains = {
    m.name: RagasEvaluatorChain(metric=m)
    for m in [faithfulness, answer_relevancy, context_relevancy, context_recall]
}`

Once the evaluator chains are created you can call the chain via the __call__() method with the outputs from the QA chain to run the evaluations

`# evaluate
for name, eval_chain in eval_chains.items():
    score_name = f&quot;{name}_score&quot;
    print(f&quot;{score_name}: {eval_chain(result)[score_name]}&quot;)

# output
# faithfulness_score: 1.0
# answer_relevancy_score: 0.9193459596511587
# context_relevancy_score: 0.07480974380786602
# context_recall_score: 0.9193459596511587`

Ragas uses LLMs under the hood to do the evaluations but leverages them in different ways to get the measurements we care about while overcoming the biases they have. Let&#x27;s learn more about how they work under the hood to see how.

## Under the hood

> Optional, not required to follow the next steps but helps understand the inner workings of ragas.

All the metrics are documented here but in this section let&#x27;s try and understand how exactly each Ragas metric works.

- **Faithfulness**: measures the factual accuracy of the generated answer with the context provided. This is done in 2 steps. First, given a question and generated answer, Ragas uses an LLM to figure out the statements that the generated answer makes. This gives a list of statements whose validity we have we have to check. In step 2, given the list of statements and the context returned, Ragas uses an LLM to check if the statements provided are supported by the context. The number of correct statements is summed up and divided by the total number of statements in the generated answer to obtain the score for a given example.
- **Answer Relevancy**: measures how relevant and to the point the answer is to the question. For a given generated answer Ragas uses an LLM to find out the probable questions that the generated answer would be an answer to and computes similarity to the actual question asked.
- **Context Relevancy**: measures the signal-to-noise ratio in the retrieved contexts. Given a question, Ragas calls LLM to figure out sentences from the retrieved context that are needed to answer the question. A ratio between the sentences required and the total sentences in the context gives you the score
- **Context Recall**: measures the ability of the retriever to retrieve all the necessary information needed to answer the question. Ragas calculates this by using the provided ground_truth answer and using an LLM to check if each statement from it can be found in the retrieved context. If it is not found that means the retriever was not able to retrieve the information needed to support that statement.

Understanding how each Ragas metric works gives you clues as to how the evaluation was performed making these metrics reproducible and more understandable. One easy way to visualize the results from Ragas is to use the traces from LangSmith and LangSmith’s evaluation features. Let&#x27;s look more into that now

## Visualising the Evaluations with LangSmith

While Ragas provides you with a few insightful metrics, it does not help you in the process of continuously evaluation of your QA pipeline in production. But this is where LangSmith comes in.

[LangSmith](https://docs.smith.langchain.com/?ref=blog.langchain.com) is a platform that helps to debug, test, evaluate, and monitor chains and agents built on any LLM framework. LangSmith offers the following benefits

- a platform to create and store a test dataset and run evaluations.
- a platform to visualise and dig into the evaluation results. Makes Ragas metrics explainable and reproducible.
- The ability to continuously add test examples from production logs if your app is also monitored with LangSmith.

With `RagasEvaluatorChain` you can use the Ragas metrics for running LangSmith evaluations as well. To know more about LangSmith evaluations check out the [quickstart](https://docs.smith.langchain.com/evaluation/quickstart?ref=blog.langchain.com).

Let&#x27;s start with your need to create a dataset inside LangSmith to store the test examples. We’re going to start off with a small dataset with 5 questions and answers to those questions (used only for the `context_recall` metric).

`# test dataset
eval_questions = [
    &quot;What is the population of New York City as of 2020?&quot;,
    &quot;Which borough of New York City has the highest population?&quot;,
    &quot;What is the economic significance of New York City?&quot;,
    &quot;How did New York City get its name?&quot;,
    &quot;What is the significance of the Statue of Liberty in New York City?&quot;,
]

eval_answers = [
    &quot;8,804,000&quot;, # incorrect answer
    &quot;Queens&quot;,    # incorrect answer
    &quot;New York City&#x27;s economic significance is vast, as it serves as the global financial capital, housing Wall Street and major financial institutions. Its diverse economy spans technology, media, healthcare, education, and more, making it resilient to economic fluctuations. NYC is a hub for international business, attracting global companies, and boasts a large, skilled labor force. Its real estate market, tourism, cultural industries, and educational institutions further fuel its economic prowess. The city&#x27;s transportation network and global influence amplify its impact on the world stage, solidifying its status as a vital economic player and cultural epicenter.&quot;,
    &quot;New York City got its name when it came under British control in 1664. King Charles II of England granted the lands to his brother, the Duke of York, who named the city New York in his own honor.&quot;,
    &#x27;The Statue of Liberty in New York City holds great significance as a symbol of the United States and its ideals of liberty and peace. It greeted millions of immigrants who arrived in the U.S. by ship in the late 19th and early 20th centuries, representing hope and freedom for those seeking a better life. It has since become an iconic landmark and a global symbol of cultural diversity and freedom.&#x27;,
]

examples = [{&quot;query&quot;: q, &quot;ground_truths&quot;: [eval_answers[i]]}
           for i, q in enumerate(eval_questions)]# dataset creation
from langsmith import Client
from langsmith.utils import LangSmithError

client = Client()
dataset_name = &quot;NYC test&quot;

try:
    # check if dataset exists
    dataset = client.read_dataset(dataset_name=dataset_name)
    print(&quot;using existing dataset: &quot;, dataset.name)
except LangSmithError:
    # if not create a new one with the generated query examples
    dataset = client.create_dataset(
        dataset_name=dataset_name, description=&quot;NYC test dataset&quot;
    )
    for q in eval_questions:
        client.create_example(
            inputs={&quot;query&quot;: q},
            dataset_id=dataset.id,
        )

    print(&quot;Created a new dataset: &quot;, dataset.name)`

If you go to the LangSmith dashboard and check the datasets section you should be able to see the dataset we just created.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb19844d72d975256f16d_image-23.png)LangSmith dataset tab with the NYC dataset we created

To run the evaluations you have to call the run_on_dataset() function from the LangSmith SDK.  but before that, you have to create a chain factory that will return a new QA chain every time this is called. This is so that any states in the QA chain are not reused when evaluating with individual examples. Make sure the QA chains return the context if using metrics that check on context.

`# factory function that return a new qa chain
def create_qa_chain(return_context=True):
    qa_chain = RetrievalQA.from_chain_type(
        llm,
        retriever=index.vectorstore.as_retriever(),
        return_source_documents=return_context,
    )
    return qa_chain`

Now let&#x27;s configure and run the evaluation. You use RunEvalConfig to configure the evaluation with the metrics/evaluator chains that you want to run against and the prediction_key for the returned result. Now call run_on_dataset and LangSmith to use the dataset we uploaded and run it against the chain from the factory and evaluate with the custom_evaluators we provided and upload the results.

`from langchain.smith import RunEvalConfig, run_on_dataset

evaluation_config = RunEvalConfig(
    custom_evaluators=[eval_chains.values()],
    prediction_key=&quot;result&quot;,
)

result = run_on_dataset(
    client,
    dataset_name,
    create_qa_chain,
    evaluation=evaluation_config,
    input_mapper=lambda x: x,
)

# output
# View the evaluation results for project &#x27;2023-08-24-03-36-45-RetrievalQA&#x27; at:
# https://smith.langchain.com/projects/p/9fb78371-150e-49cc-a927-b1247fdb9e8d?eval=true`

Open up the results and you will see something like this

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb19844d72d975256f17d_image-24.png)

This shows the output for each example in the training dataset and the Feedback columns show the evaluation results. Now if you want to dive more into the reasons for the scores and how to improve them, click on any single example and open the Feedback tab.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb19844d72d975256f177_Untitled.png)

This will show you each score and if you open the pop-up icon it will point you to the evaluation run of the RagasEvaluatorChain.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb19844d72d975256f17a_image-26.png)

You can analyze each result to see why it was so and this will give you ideas on how to improve it.

Now if your QA pipeline also uses LangSmith for logging, tracing, and monitoring you can leverage the add-to-dataset feature to set up a continuous evaluation pipeline that keeps adding interesting data points (based on human feedback of other indirect methods) into the test to keep the test dataset up to date with a more comprehensive dataset with wider coverage.

## Conclusion

Ragas enhances QA system evaluation by addressing limitations in traditional metrics and leveraging Large Language Models. LangSmith provides a platform for running evaluations and visualizing results.

By using Ragas and LangSmith, you can ensure your QA systems are robust and ready for real-world applications, making the development process more efficient and reliable.

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc07193192cebc73980fd3_logo%20and%20title%20-%2020%20characters%20max%20(6).png)PartnerDeep Agents

#### Building a company due diligence agent with Deep Agents, LangSmith and Parallel

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01c6959ca5fd924ab432_MattHarris.jpg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01b812793b72539057d5_nick%20headshot.jpeg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd2d50cd0f84dacf92e7b_ProfilePic.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd29baf4c28709e2566a7_headshot.jpg)Matt HarrisNick MartitschSrimanth TangedipalliKaran SinghMay 8, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)9min[](/blog/building-a-company-due-diligence-agent-with-deep-agents-langsmith-and-parallel)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef96ff74c638e982ff68c6_86%20(1).png)Agent ArchitectureLangSmithOpen Source

#### How LangSmith and LangChain OSS Help You Meet EU AI Act Requirements

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0003a1af368dfae13c23c_jacob-talbot.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Jacob TalbotBecca WengApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/langsmith-langchain-oss-eu-ai-act)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e251cee3c69c0b64e26c79_case-study-16_9%20(1).png)Case StudiesLangSmith

#### How Credit Genie used Insights Agent to improve their AI financial assistant

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e251111d491175462a384c_david-li.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e25199461e789ce4b875a7_jeffrey-ngai.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e2518d5b449e720f9f295a_goyo-lozano-palacio.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e2515f9f57e45d15dbd331_charles-yuan.png)David LiJeffrey NgaiGoyo Lozano PalacioCharles YuanApril 20, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)5min[](/blog/credit-genie-insights-agent-financial-assistant)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)