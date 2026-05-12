---
title: "Text-to-SQL: Fine-Tune Llama 2 Fast | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/easily-finetune-llama-2-for-your-text-to-sql-applications-ecd53640e10d"
category: "general"
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







[Llama 2](https://ai.meta.com/llama/) is a huge milestone in the advancement of open-source LLMs. The biggest model and its finetuned variants sit at the top of the [Hugging Face Open LLM Leaderboard](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard). Multiple benchmarks show that it is approaching GPT-3.5 (or in some cases even surpassing it) in terms of performance. All of this means that open-source LLMs are an increasingly viable and reliable option for use in complex LLM applications, from RAG systems to agents.



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



# Context: Llama-2–7B is Not Good at Text-to-SQL

A downside of the smallest Llama 2 model (7B parameters), however, is that it’s not very good at generating SQL, making it impractical for structured analytics use cases. As an example, we tried prompting Llama 2 to generate the correct SQL statement given the following prompt template:

You are a powerful text-to-SQL model. Your job is to answer questions about a database. You are given a question and context regarding one or more tables.

You must output the SQL query that answers the question.

### Input:
{input}

### Context:
{context}

### Response:Here we plugged in a sample entry from the [sql-create-context dataset](https://huggingface.co/datasets/b-mc2/sql-create-context).

input: In 1981 which team picked overall 148?
context: CREATE TABLE table_name_8 (team VARCHAR, year VARCHAR, overall_pick VARCHAR)Meanwhile, here is the generated output vs. correct output:

Generated output: SELECT * FROM `table_name_8` WHERE '1980' = YEAR AND TEAM = "Boston Celtics" ORDER BY OVERALL_PICK DESC LIMIT 1;

Correct output: SELECT team FROM table_name_8 WHERE year = 1981 AND overall_pick = "148"This is clearly not ideal. Unlike ChatGPT and GPT-4, Llama 2 does not reliably produce well-formatted and correct SQL outputs.

This is exactly where fine-tuning comes in — given a proper corpus of text-to-SQL data, we can teach Llama 2 to be better at generating SQL outputs from natural language. At a high-level, fine-tuning involves modifying the weights of the model in some capacity. There are different ways to finetune models, from updating all parameters of the network, to a subset of the parameters, to only finetuning additional parameters (e.g. [how LoRA works](https://arxiv.org/abs/2106.09685)).

Once the model is finetuned, it can still be plugged into a downstream LLM application. That is exactly what this tutorial aims to show. It is a step more involved than our existing tutorials which have primarily focused on “in-context learning” and “retrieval-augmentation” use cases — freezing the model itself but focusing on the orchestration of data into the input prompt. Finetuning can have a high learning curve and also require a lot of compute. This tutorial makes it as easy as possible to get started.

# Tutorial Overview

In this tutorial, we show you how you can finetune Llama 2 on a text-to-SQL dataset, and then use it for structured analytics against any SQL database using the capabilities of [LlamaIndex](https://github.com/jerryjliu/llama_index).

Here is the stack that we use:

- `[b-mc2/sql-create-context](https://huggingface.co/datasets/b-mc2/sql-create-context)`[ from Hugging Face datasets](https://huggingface.co/datasets/b-mc2/sql-create-context) as the training dataset
- [OpenLLaMa](https://github.com/openlm-research/open_llama) `open_llama_7b_v2` as the base model
- [PEFT for efficient finetuning](https://github.com/huggingface/peft)
- [Modal](https://modal.com/) for handling all cloud compute/orchestration for finetuning. And also for the excellent reference [doppel-bot repo](https://github.com/modal-labs/doppel-bot).
- [LlamaIndex](https://www.llamaindex.ai/) for text-to-SQL inference against any SQL database.

Special mention to the awesome [Llama 2 tutorial from Anyscale that helped to inspire this project](https://www.anyscale.com/blog/fine-tuning-llama-2-a-comprehensive-case-study-for-tailoring-models-to-unique-applications).

All of our materials can be found in our Github repo: [https://github.com/run-llama/modal_finetune_sql](https://github.com/run-llama/modal_finetune_sql) (again emphasizing that this is adapted from [doppel-bot](https://github.com/modal-labs/doppel-bot)). Also, the full tutorial can be found in our [Jupyter notebook guide](https://github.com/run-llama/modal_finetune_sql/blob/main/tutorial.ipynb). Make sure to check it out!

As mentioned above, performing finetuning does require quite a few steps. Our goal is to make this as straightforward as possible to follow and use out of the box. We don’t cover all the nitty gritty detailsof Modal, PEFT, the finetuning procedure itself, etc. but we do give a rough overview.

There are also certainly higher-level APIs that we could’ve used (e.g. OpenAI, Lamini) in order to achieve this task. There’s plenty of room for followup tutorials to cover these topics!

## Step 1: Loading Training Data for Finetuning LLaMa

The first step here is to open up the [Jupyter notebook](https://github.com/run-llama/modal_finetune_sql/blob/main/tutorial.ipynb). The notebook is organized into a series of runnable scripts that each perform the steps needed to load data.

Our code uses Modal for every step of the orchestration, and Modal is best used on top of the Python scripts themselves. That is why a lot of these cells don’t contain Python blocks of their own.

First we use Modal to load in the `b-mc2/sql-create-context` dataset. This is a simple task that just loads in the dataset and formats it into a `.jsonl` file.

modal run src.load_data_sql --data-dir "data_sql"As we can see, under the hood the task is quite straightforward:

# Modal stubs allow our function to run remotely
@stub.function(
    retries=Retries(
        max_retries=3,
        initial_delay=5.0,
        backoff_coefficient=2.0,
    ),
    timeout=60 * 60 * 2,
    network_file_systems={VOL_MOUNT_PATH.as_posix(): output_vol},
    cloud="gcp",
)
def load_data_sql(data_dir: str = "data_sql"):
    from datasets import load_dataset

    dataset = load_dataset("b-mc2/sql-create-context")

    dataset_splits = {"train": dataset["train"]}
    out_path = get_data_path(data_dir)

    out_path.parent.mkdir(parents=True, exist_ok=True)

    for key, ds in dataset_splits.items():
        with open(out_path, "w") as f:
            for item in ds:
                newitem = {
                    "input": item["question"],
                    "context": item["context"],
                    "output": item["answer"],
                }
                f.write(json.dumps(newitem) + "\n")

## Step 2: Run Finetuning Script

The next step is to run our finetuning script on the parsed dataset.

modal run src.finetune_sql --data-dir "data_sql" --model-dir "model_sql"The finetuning script performs the following steps.

**Splits the dataset into training and validation splits**

train_val = data["train"].train_test_split(test_size=val_set_size, shuffle=True, seed=42)
train_data = train_val["train"].shuffle().map(generate_and_tokenize_prompt)
val_data = train_val["test"].shuffle().map(generate_and_tokenize_prompt)**Formats each split into tuples of (input prompt, label): **The input query and context are formatted into the same input prompt. The input prompt is then tokenized, and the labels are set to the exact same as the input prompt — this allows the model to train on next-token prediction.

def generate_and_tokenize_prompt(data_point):
  full_prompt = generate_prompt_sql(
      data_point["input"],
      data_point["context"],
      data_point["output"],
  )
  tokenized_full_prompt = tokenize(full_prompt)
  if not train_on_inputs:
      raise NotImplementedError("not implemented yet")
  return tokenized_full_promptThe input prompt is the exact same as what was given at the top of this blog.

When the finetuning script is run, the model is saved in the remote cloud directory specified by model_dir (which is set to a default value if not specified).

## Step 3: Evaluation

The model has been finetuned and can be served from the cloud. We can run some basic evaluations using sample data from sql-create-context to compare the performance of the finetuned model vs. the baseline Llama 2 model.

modal run src.eval_sql::mainThe results demonstrate a massive improvement for the finetuned model:

Input 1: {'input': 'Which region (year) has Abigail at number 7, Sophia at number 1 and Aaliyah at number 5?', 'context': 'CREATE TABLE table_name_12 (region__year_ VARCHAR, no_5 VARCHAR, no_7 VARCHAR, no_1 VARCHAR)', 'output': 'SELECT region__year_ FROM table_name_12 WHERE no_7 = "abigail" AND no_1 = "sophia" AND
no_5 = "aaliyah"'}
Output 1 (finetuned model): SELECT region__year_ FROM table_name_12 WHERE no_7 = "abigail" AND no_1 = "aaliyah" AND no_5 = "sophia"
Output 1 (base model): SELECT * FROM table_name_12 WHERE region__year = '2018' AND no_5 = 'Abigail' AND no_7 = 'Sophia' AND no_1 = 'Aaliyah';

Input 2: {'input': 'Name the result/games for 54741', 'context': 'CREATE TABLE table_21436373_11 (result_games VARCHAR, attendance VARCHAR)', 'output': 'SELECT result_games FROM table_21436373_11 WHERE attendance = 54741'}
Output 2 (finetuned model): SELECT result_games FROM table_21436373_11 WHERE attendance = "54741"
Output 2 (base model): SELECT * FROM table_21436373_11 WHERE result_games = 'name' AND attendance &amp;gt; 0;Whereas the base model produces wrongly formatted outputs, or incorrect SQL statements,

the finetuned model is able to produce outputs that are much closer to that of the expected output.

## Step 4: Integrating the Finetuned Model with LlamaIndex

We can now use this model in LlamaIndex for text-to-SQL over any database.

We first define a test SQL database that we can then use to test the inference capabilities of the model.

We create a toy `city_stats` table that contains city name, population, and country information, and populate it with a few sample cities.

db_file = "cities.db"
engine = create_engine(f"sqlite:///{db_file}")
metadata_obj = MetaData()
# create city SQL table
table_name = "city_stats"
city_stats_table = Table(
    table_name,
    metadata_obj,
    Column("city_name", String(16), primary_key=True),
    Column("population", Integer),
    Column("country", String(16), nullable=False),
)
metadata_obj.create_all(engine)This is stored in a `cities.db` file.

We can then use Modal to load both the finetuned model and this database file into the `NLSQLTableQueryEngine` in LlamaIndex - this query engine allows users easily start performing text-to-SQL over a given database.

modal run src.inference_sql_llamaindex::main --query "Which city has the highest population?" --sqlite-file-path "nbs/cities.db" --model-dir "model_sql" --use-finetuned-model TrueWe get a response like the following:

SQL Query: SELECT MAX(population) FROM city_stats WHERE country = "United States"
Response: [(2679000,)]

# Conclusion

And that’s basically it! This tutorial provides a very high-level way for you to get started finetuning a Llama 2 model on generating SQL statements, and showcases end-to-end how you can plug it into your text-to-SQL workflows with LlamaIndex.

**Resources**

For the sake of completeness we’re linking all of our resources again here.

Tutorial repo: [https://github.com/run-llama/modal_finetune_sql](https://github.com/run-llama/modal_finetune_sql) (adapted from [doppel-bot](https://modal.com/)).

[Jupyter notebook guide](https://github.com/run-llama/modal_finetune_sql/blob/main/tutorial.ipynb).

Stack:

- `[b-mc2/sql-create-context` from Hugging Face datasets]([https://huggingface.co/datasets/b-mc2/sql-create-context](https://huggingface.co/datasets/b-mc2/sql-create-context))
- [OpenLLaMa](https://github.com/openlm-research/open_llama)
- [PEFT](https://github.com/huggingface/peft)
- [Modal](https://modal.com/) (+ [doppel-bot repo](https://github.com/modal-labs/doppel-bot)).
- [LlamaIndex](https://www.llamaindex.ai/)

Special mention: [Llama 2 tutorial from Anyscale](https://www.anyscale.com/blog/fine-tuning-llama-2-a-comprehensive-case-study-for-tailoring-models-to-unique-applications).