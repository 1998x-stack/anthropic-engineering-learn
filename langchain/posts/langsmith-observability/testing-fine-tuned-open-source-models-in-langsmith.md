---
title: "Testing Fine Tuned Open Source Models in LangSmith"
author: "LangChain Accounts"
date: "2023-10-16"
url: "https://www.langchain.com/blog/testing-fine-tuned-open-source-models-in-langsmith"
---

Tutorials &amp; How-TosLangSmithOpen Source

# Testing Fine Tuned Open Source Models in LangSmith

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamOctober 16, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)5min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb125a2e6df4d389adc01_Twitter-post---15--3-.png)*Editor&#x27;s Note. This blog post was written by *[*Ryan Brandt*](https://twitter.com/dexter_brandt?ref=blog.langchain.com)*, the CTO and Cofounder of ChatOpenSource, a business specializing in enterprise AI chat that runs entirely within an orgs network, no third party needed. He covers how he uses LangSmith,* *LangChain&#x27;s platform for getting LLM applications to production. Sign up for access *[*here*](https://smith.langchain.com/?ref=blog.langchain.com)*.*

Open source models are increasingly capable for use in applications. The trend is only accelerating with recent releases like **Mistral 7b** and the **Llama2** family. The future seems to be in the ability to quickly swap better models in and out of your application like cartridges in an old game console. Fine tuning different versions of a model only increases the number of possible cartridges a developer will need to compare.

So that begs the question, how can we productionize the evaluation of our models so we can can choose the best tool for the job? **LangSmith** offers us a way out of python script hell with a handy UI and API for creating evaluation datasets. With these datasets we can run tests on multiple models and directly compare their performance on multiple axis’.

It’s easy to upload data to **LangSmith** via python or the user interface. For our example notebook scroll to the end.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb126a2e6df4d389adc50_Untitled--14-.png)uploading our dataset in csv format. In this case, we chose a Key/Value type as it&#x27;s most suited to our data.![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb126a2e6df4d389adc59_Untitled--15-.png)Our dataset for validating correct structured SQL output once uploaded.

## **The Process**

Here’s the way we organized the study:

- **Initiation**: The task began with a goal to fine-tune the Llama2-7b and Llama2-13b model using the [sql-create-context](https://huggingface.co/datasets/arviii/sql-create-context?ref=blog.langchain.com) dataset on Hugging Face.
- **Data Conversion**: The dataset from Hugging Face, originally in JSON, was transformed to .jsonl for chat fine-tuning.
- **Data Sampling with GPT-4**: GPT-4&#x27;s Code Interpreter was used to select 10,000 rows from the dataset.
- **Validation Set Creation**: 1000 unique sql rows were chosen as a validation set, ensuring no overlap with the training data. We uploaded those testing rows to **LangSmith** so we could automate our evaluations.

`from langsmith import Client
def create_dataset(dataset_name=None):
    &quot;&quot;&quot;adds an example run with inputs and outputs to an existing dataset&quot;&quot;&quot;
    client = Client()

    dataset_name = dataset_name
    client.create_dataset(dataset_name=dataset_name)
    return dataset_name

def add_to_dataset(dataset_name, validation_file_path):
    client = Client()

    dataset = client.read_dataset(dataset_name=dataset_name)

    # Open and process the validation file
    with open(validation_file_path, &#x27;r&#x27;) as f:
        for line in f:
            data = json.loads(line)
            example = data[&#x27;prompt&#x27;]
            assistant_content = data[&#x27;completion&#x27;]

            # Add to dataset using client API
            client.create_chat_example(
                messages=[
                    {&quot;type&quot;: &quot;system&quot;, &quot;data&quot;: {&quot;content&quot;: &quot;You are a helpful assistant that is knowledgeable about sql. Only output the SQL.&quot;}},
                    {&quot;type&quot;: &quot;human&quot;, &quot;data&quot;: {&quot;content&quot;: example}}
                ],
                generations={&quot;type&quot;: &quot;ai&quot;, &quot;data&quot;: {&quot;content&quot;: assistant_content}},
                dataset_id=dataset.id
            )`

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb126a2e6df4d389adc62_Untitled--16-.png)The result of running the code block above

**5. Fine-tuning and Assessment: **The main goal was to improve Llama2-7b-chat and Llama2-13b-chat for specific SQL output. We fine tuned Llama2-7b-chat with 78k rows of sql data, and Llama2-13b-chat with 10k rows to control for cost. Both fine tuning and inference were done on an 8xA40 cluster. We did full parameter tuning, not LoRA. To do this we used Replicate, a platform for model hosting and fine tuning. You can learn more about them [here](https://replicate.com/docs/guides/fine-tune-a-language-model?ref=blog.langchain.com).

`import replicate

training = replicate.trainings.create(
  version=&quot;meta/llama-2-13b-chat:f4e2de70d66816a838a89eeeb621910adffb0dd0baba3976c96980970978018d&quot;,
  input={
    &quot;train_data&quot;: &quot;https://storage.googleapis.com/chatopensource-replicate-demo/selected_sql_create_context_v4.jsonl&quot;,
    &quot;num_train_epochs&quot;: 3
  },
  destination=&quot;papermoose/test&quot;
)`

**6. LangSmith Evaluation: **We used LangSmith to test the 1000 prompts on each model. We compared their result to the known correct answer to determine whether the model’s output was correct or not. We used GPT-4 to do the evals itself. LangSmith made the process extremely simple, as shown below.

`import replicate

async def evaluate_dataset(dataset_name=None, num_repetitions=1, model=&quot;gpt-4-0613&quot;, project_name=None):
    &quot;&quot;&quot;runs the model you want to evaluate against the assumed to be correct examples in your dataset, grading the evaluated model output correct or incorrect.&quot;&quot;&quot;

    from langchain.smith import run_on_dataset, RunEvalConfig, arun_on_dataset
    from langchain.chat_models import ChatOpenAI

    # The chat model you want to test, in our case replicate
    model_to_test = Replicate(
    model=model,
    model_kwargs={&quot;temperature&quot;: 0.75, &quot;max_length&quot;: 500, &quot;top_p&quot;: 1},
)

    client = Client()

    &quot;&quot;&quot;runs a question/answer evaluation, where the eval llm (gpt-4) will determine
    if model_to_test&#x27;s outputs are correct based on the example_dataset we uploaded in the previous set.
    the example_dataset is treated by the eval as a correct answer for the given input.&quot;&quot;&quot;

    eval_config = RunEvalConfig(
        evaluators=[
            &quot;cot_qa&quot;
        ],
    )
    chain_results = await arun_on_dataset(
        client,
        dataset_name=dataset_name,
        llm_or_chain_factory=model_to_test,
        evaluation=eval_config,
        num_repetitions=num_repetitions,
        project_name=project_name
    )`

The LangSmith platform itself allows you to view the results of our eval, in this case the chain of thought question answer builtin eval. You can also write your own if desired as shown [here](https://docs.smith.langchain.com/evaluation/custom-evaluators?ref=blog.langchain.com)!

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb126a2e6df4d389adc56_Untitled--17-.png)A correct answer![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb126a2e6df4d389adc65_Untitled--18-.png)An incorrect answer.

[View the dataset here](https://huggingface.co/datasets/b-mc2/sql-create-context?ref=blog.langchain.com)

## Our **Findings in LangSmith**

Here are our results, with our dataset names randomly generated. There’s still no easy way to change the name of the dataset in the UI, so I’ve also charted it out below in a more understandable way.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb126a2e6df4d389adc5c_Untitled--19-.png)LangSmith UI showing the results of our tests.![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb126a2e6df4d389adc68_Untitled--20-.png)graphing out our LangSmith results to better visualize the outcome

You can see how we generated this using chatgpt [here](https://chat.openai.com/share/8ca38826-b042-45e6-baf0-76e5c0d35b3c?ref=blog.langchain.com)!

## **Observations on the outcome**

- **Parameters vs. Data**: The data shows a relationship between the model parameters and training data volume. While `llama2-7b-chat-ft-78k`, with fewer parameters, performed well, it was outperformed by `llama2-13b-chat-ft-10k` with more parameters. This leads to the question: How might the 13b model have fared with the larger 78k dataset? It&#x27;s likely that accuracy would correlate with training set size and quality.
- **Response Times**: Beyond just accuracy, response times, particularly p50 and p99, are important for assessing model efficiency. Here, the `llama2-7b-chat-ft-78k` model showed both good accuracy and efficient response times. It’s worth baring in mind that these llama models have response times based on **Replicate,** and could change depending on the hardware used to run them.
- **Comparison to GPT-3.5T**: The data highlights how these models compare to `GPT-3.5-turbo-base`. Notably, `llama2-13b-chat-ft-10k`&#x27;s accuracy was close to that of `GPT-3.5T`, suggesting the potential of optimized open-source models to match or even exceed established models.

## To Recap

- We’ve seen how **LangSmith** works with any model, open or closed source.
- We’ve seen both code snippets detailing the process of interacting with **LangSmith**, and the screenshotted results in the UI.
- We’ve graphed out the results using ChatGPT advanced data analysis.
- We’ve seen how for some domains open source models are competitive with OpenAI
- for a more interactive example of using **LangSmith**, [check out our python notebook here](https://github.com/chatopensource/ai-cookbooks/blob/main/openai-fine-tuning-langsmith-cookbook.ipynb?ref=blog.langchain.com).

We also run **ChatOpenSource,** a fully data private and auditable chat replacement for ChatGPT for enterprises. Companies can easily configure documents and data so only the right team can ask about them, and no data ever leaves the company environment. [Book a quick call with us to learn more](https://calendly.com/chatopensource/30min?ref=blog.langchain.com)!

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69f20536df00c0eb15eab1d3_blue-77%20characters%20max.png)Deep AgentsAgent ArchitectureOpen Source

#### Tuning Deep Agents to Work Well with Different Models

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcefac505b6b48827abf84_vivek-trivedy.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcf032ce65a32e276a4d0a_mason-daugherty.png)Vivek TrivedyMason DaughertyApril 29, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)5min[](/blog/tuning-deep-agents-different-models)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef96ff74c638e982ff68c6_86%20(1).png)Agent ArchitectureLangSmithOpen Source

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