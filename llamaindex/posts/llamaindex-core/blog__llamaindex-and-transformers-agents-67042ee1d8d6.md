---
title: "Transformers Agents With LlamaIndex: How-To Guide | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/llamaindex-and-transformers-agents-67042ee1d8d6"
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







# Summary

Agents are a popular use-case for Large Language Models (LLMs), typically provide a structure that enables LLMs to make decisions, use tools, and accomplish tasks. These agents can take many forms, like the fully-autonomous versions seen with [Auto-GPT](https://github.com/Significant-Gravitas/Auto-GPT), to more controlled implementations like [Langchain](https://python.langchain.com/en/latest/) Agents. With the recent release of [Transformers Agents](https://huggingface.co/docs/transformers/transformers_agents), we showcase how [LlamaIndex](https://www.llamaindex.ai/) continues to be a useful tool for agents, by augmenting their existing image-generator tool. Using an vector index created from 10K [DiffusionDB ](https://huggingface.co/datasets/poloclub/diffusiondb)prompts, the Text2Image Prompt Assistant tool we created can re-write prompts to generate more beautiful images. Full source code is available in the [Hugging Face Space for the tool](https://huggingface.co/spaces/llamaindex/text2image_prompt_assistant/tree/main), and a [colab notebook](https://colab.research.google.com/drive/1r0t423LTkCYi5fGLrSfTdtC0DzKuU-zq?usp=sharing) is available as a usage walkthrough.



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



# Creating the Tool

Transformers Agents come with a variety of per-configured tools that leverage the vast amounts of open-source models hosted on Hugging Face-Hub. Furthermore, additional tools can be created and shared by simply publishing a new Hugging Face Space with the proper tool setup.

To create a tool, your code simply needs a `tool_config.json` file that describes the tool, as well as a file containing the implementation of your tool. While the documentation was a little fuzzy for this part, we eventually were able to use [the implementation of existing custom tools](https://huggingface.co/huggingface-tools) as the framework for our own.

To enable LlamaIndex to write text-to-image prompts, we need a way to show the LLM what examples of good prompts look like. To do this, we indexed 10K random text-to-image prompts from DiffusionDB.

from datasets import load_dataset
from llama_index import VectorStoreIndex, Document

# downloads a LOT of data
dataset = load_dataset('poloclub/diffusiondb', '2m_random_10k')

documents = []
for sample in dataset['train']:
    documents.append(Document(sample['prompt']))

# create index
index = VectorStoreIndex.from_documents(documents)

# store index
index.storage_context.persist(persist_dir="./storage")To get LlamaIndex to write prompts using examples, we need to customize the prompt templates a bit. You can see the final prompt templates and how to use them below:

text_qa_template = Prompt(
    "Examples of text-to-image prompts are below: \n"
    "---------------------\n"
    "{context_str}"
    "\n---------------------\n"
    "Given the existing examples of text-to-image prompts, "
    "write a new text-to-image prompt in the style of the examples, "
    "by re-wording the following prompt to match the style of the above examples: {query_str}\n"
)

refine_template = Prompt(
    "The initial prompt is as follows: {query_str}\n"
    "We have provided an existing text-to-image prompt based on this query: {existing_answer}\n"
    "We have the opportunity to refine the existing prompt "
    "(only if needed) with some more relevant examples of text-to-image prompts below.\n"
    "------------\n"
    "{context_msg}\n"
    "------------\n"
    "Given the new examples of text-to-image prompts, refine the existing text-to-image prompt to better "
    "statisfy the required style. "
    "If the context isn't useful, or the existing prompt is good enough, return the existing prompt."
)

query_engine = index.as_query_engine(
    text_qa_template=text_qa_template,
    refine_template=refine_template
)

response = query_engine.query("Draw me a picture of a happy dog")

## Snag #1

One main drawback of Transformers Agents currently is that they will only pick one tool to solve each prompt. So if we want to augment the image-generator tool, we need to replace it! In our tool implementation, we actually load the original image-generator tool and call it after running LlamaIndex to generate a new text-to-image prompt.

## Snag #2

The next bump in our journey is how Hugging Face downloads tools from the space. Initially, it only downloading the `tool_config.json` file and the source code for the tool. But we also need to download the prompts we spent time indexing!

To get around this, during the `setup()` of the tool, we call `hf_hub_download()` to download the files we need to load the index.

## Back on Track

With the index created and the general processes figured out, the actual tool implementation is fairly straightforward.

class Text2ImagePromptAssistant(Tool):

    inputs = ['text']
    outputs = ['image']
    description = PROMPT_ASSISTANT_DESCRIPTION

    def __init__(self, *args, openai_api_key='', model_name='text-davinci-003', temperature=0.3, verbose=False, **hub_kwargs):
        super().__init__()
        os.environ['OPENAI_API_KEY'] = openai_api_key
        if model_name == 'text-davinci-003':
            llm = OpenAI(model_name=model_name, temperature=temperature)
        elif model_name in ('gpt-3.5-turbo', 'gpt-4'):
            llm = ChatOpenAI(model_name=model_name, temperature=temperature)
        else:
            raise ValueError(
                f"{model_name} is not supported, please choose one "
                "of 'text-davinci-003', 'gpt-3.5-turbo', or 'gpt-4'."
            )
        service_context = ServiceContext.from_defaults(llm_predictor=LLMPredictor(llm=llm))
        set_global_service_context(service_context)

        self.storage_path = os.path.dirname(__file__)
        self.verbose = verbose
        self.hub_kwargs = hub_kwargs

    def setup(self):
        hf_hub_download(repo_id="llamaindex/text2image_prompt_assistant", filename="storage/vector_store.json", repo_type="space", local_dir=self.storage_path)
        hf_hub_download(repo_id="llamaindex/text2image_prompt_assistant", filename="storage/index_store.json", repo_type="space", local_dir=self.storage_path)
        hf_hub_download(repo_id="llamaindex/text2image_prompt_assistant", filename="storage/docstore.json", repo_type="space", local_dir=self.storage_path)

        self.index = load_index_from_storage(StorageContext.from_defaults(persist_dir=os.path.join(self.storage_path, "storage")))
        self.query_engine = self.index.as_query_engine(similarity_top_k=5, text_qa_template=text_qa_template, refine_template=refine_template)

        # setup the text-to-image tool too
        self.text2image = load_tool('huggingface-tools/text-to-image')
        self.text2image.setup()

        self.initialized = True

    def __call__(self, prompt):
        if not self.is_initialized:
            self.setup()

        better_prompt = str(self.query_engine.query(prompt)).strip()

        if self.verbose:
            print('==New prompt generated by LlamaIndex==', flush=True)
            print(better_prompt, '\n', flush=True)

        return self.text2image(better_prompt)

# Running the Tool

With the tool setup, we can now test it with an actual agent! For testing, we used an `OpenAIAgent` with the `text-davinci-003` model. When asked to draw a picture of a mountain, this is what we got:

from transformers import OpenAiAgent
agent = OpenAiAgent(model="text-davinci-003", api_key="your_api_key")

agent.run("Draw me a picture a mountain.")![](/blog/images/1*qFmnkvn46OwynmJGJ2fKeQ.png)The initial picture of mountains that the agent created.As you can see, the picture looks alright. But, text-to-image prompts are somewhat of an art.

To use our new tool, we just need to replace the existing image-generator tool:

from transformers import load_tool
prompt_assistant = load_tool(
    "llamaindex/text2image_prompt_assistant",
    openai_api_key="your_api_key",
    model_name='text-davinci-003',
    temperature=0.3,  # increase or decrease this to control variation
    verbose=True
)

from transformers import OpenAiAgent
agent = OpenAiAgent(model="text-davinci-003", api_key="your_api_key")

# replace the existing tool
agent.toolbox['image_generator'] = prompt_assistant

agent.run("Draw me a picture a mountain.")Using Our new LlamaIndex Prompt Assistant tool, we get a much more stylized result. In the terminal, we see the prompt was re-written as “a majestic mountain peak, surrounded by lush greenery, with a stunning sunset in the background,” which resulted in the following image:

![](/blog/images/1*1YbUcsgYESVAccKpJzt2Wg.png)Image generated by our Text2Image Prompt Assistant tool.

Looks great! With the temperature variable, we can control how varied the generated prompts become. With a temperature above zero, each prompt generated by LlamaIndex with the same agent prompt will be brand new!

# Conclusion

In conclusion, we have demonstrated how LlamaIndex can be used to augment LLM agents, by implementing a Text2Image Prompt Assistant tool with a Transformers Agent. Using a vector database created from DiffusionDB, LlamaIndex can suggest better prompts when generating images.

Custom tools in Transformers Agents are easily distributed and shared using Hugging Face Spaces, and we are excited to see what other people build and share!