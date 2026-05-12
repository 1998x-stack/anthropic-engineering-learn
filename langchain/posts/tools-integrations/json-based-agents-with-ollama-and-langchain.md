---
title: "JSON agents with Ollama &amp; LangChain"
author: "LangChain Accounts"
date: "2024-02-20"
url: "https://www.langchain.com/blog/json-based-agents-with-ollama-and-langchain"
---

Tutorials &amp; How-TosPartner

# JSON agents with Ollama &amp; LangChain

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamFebruary 20, 2024![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)7min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb019e51c6ccf7873853a_symbol-1.webp)

## Learn to implement an open-source Mixtral agent that interacts with a graph database Neo4j through a semantic layer

**Editor&#x27;s note: This post is written by **[**Tomaz Bratanic**](https://twitter.com/tb_tomaz?ref=blog.langchain.dev)** from Neo4j**

By now, we all have probably recognized that we can significantly enhance the capabilities of LLMs by providing them with additional tools. For example, even ChatGPT can use Bing Search and Python interpreter out of the box in the paid version. OpenAI is a step ahead and provides fine-tuned LLM models for tool usage, where you can pass the available tools along with the prompt to the API endpoint. The LLM then decides if it can directly provide a response or if it should use any of the available tools first. Note that the tools don’t have to be only for retrieving additional information; they can be anything, even allowing LLMs to book a dinner reservation. I have previously implemented a project [allowing an LLM to interact with a graph database through a set of predefined tools](https://towardsdatascience.com/enhancing-interaction-between-language-models-and-graph-databases-via-a-semantic-layer-0a78ad3eba49?ref=blog.langchain.com), which I called a semantic layer.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb01ae51c6ccf7873856d_1*gheQBa_1fWFeHzp4gQXekQ.png)An agentic LLM interacting with a graph database. Image by author.

In essence, these tools augment a LLM like GPT-4 by providing dynamic, real-time access to information, personalization through memory, and a sophisticated understanding of relationships through the knowledge graph. Together, they enable the LLM to offer more accurate recommendations, understand user preferences over time, and access a broader range of up-to-date information, resulting in a more interactive and adaptive user experience. As mentioned, besides the ability to retrieve additional information at query time, they also give the LLM an option to influence their environment by, for example, booking a meeting in the calendar.

While OpenAI has spoiled us with its fine-tuned models for tool usage, the reality is that most other LLMs aren’t at the level of OpenAI when it comes to function calling and tool usage. I have tried most of the models available in Ollama, and most struggle with consistently generating predefined structured output that could be used to power an agent. On the other hand, there are some models that are fine-tuned for function-calling. However, those models have a custom prompt engineering schema for function-calling they follow, which is not well documented, or they can’t be used for anything other than function-calling.

Ultimately, I decided to follow the existing LangChain implementation of a JSON-based agent using the Mixtral 8x7b LLM. I used the Mixtral 8x7b as a movie agent to interact with Neo4j, a native graph database, through a semantic layer. The [code is available as a Langchain template](https://github.com/langchain-ai/langchain/tree/master/templates/neo4j-semantic-ollama?ref=blog.langchain.com) and as a [Jupyter notebook](https://github.com/tomasonjo/blogs/blob/master/llm/ollama_semantic_layer.ipynb?ref=blog.langchain.com). If you are interested in how the tools are implemented, you can look at my [previous blog post](https://towardsdatascience.com/enhancing-interaction-between-language-models-and-graph-databases-via-a-semantic-layer-0a78ad3eba49?ref=blog.langchain.com). Here, we will discuss how to implement a JSON-based LLM agent.

## Tools in the semantic layer

The examples in LangChain documentation ([JSON agent](https://python.langchain.com/docs/modules/agents/agent_types/json_agent?ref=blog.langchain.com), [HuggingFace example](https://huggingface.co/blog/open-source-llms-as-agents?ref=blog.langchain.com)) use tools with a single string input. Since the tools in the semantic layer use slightly more complex inputs, I had to dig a little deeper. Here is an example input for a recommender tool.

`all_genres = [
    &quot;Action&quot;,
    &quot;Adventure&quot;,
    &quot;Animation&quot;,
    &quot;Children&quot;,
    &quot;Comedy&quot;,
    &quot;Crime&quot;,
    &quot;Documentary&quot;,
    &quot;Drama&quot;,
    &quot;Fantasy&quot;,
    &quot;Film-Noir&quot;,
    &quot;Horror&quot;,
    &quot;IMAX&quot;,
    &quot;Musical&quot;,
    &quot;Mystery&quot;,
    &quot;Romance&quot;,
    &quot;Sci-Fi&quot;,
    &quot;Thriller&quot;,
    &quot;War&quot;,
    &quot;Western&quot;,
]

class RecommenderInput(BaseModel):
    movie: Optional[str] = Field(description=&quot;movie used for recommendation&quot;)
    genre: Optional[str] = Field(
        description=(
            &quot;genre used for recommendation. Available options are:&quot; f&quot;{all_genres}&quot;
        )
    )
`

The recommender tools has two optional inputs, movie and genre. Additionally, we use an enumeration of available values for the genre parameter. While the inputs are not highly complex, they are still more advanced than a single string input, so the implementation has to be slightly different.

## JSON-based prompt for an LLM agent

In my implementation, I took heavy inspiration from the existing `hwchase17/react-json` prompt available in [LangChain hub](https://smith.langchain.com/hub/hwchase17/react-json?ref=blog.langchain.com). The prompt uses the following system message.

`Answer the following questions as best you can. You have access to the following tools:

{tools}

The way you use the tools is by specifying a json blob.
Specifically, this json should have a `action` key (with the name of the tool to use) and a `action_input` key (with the input to the tool going here).

The only values that should be in the &quot;action&quot; field are: {tool_names}

The $JSON_BLOB should only contain a SINGLE action, do NOT return a list of multiple actions. Here is an example of a valid $JSON_BLOB:

```
{{
  &quot;action&quot;: $TOOL_NAME,
  &quot;action_input&quot;: $INPUT
}}
```

ALWAYS use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action:
```
$JSON_BLOB
```
Observation: the result of the action
... (this Thought/Action/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin! Reminder to always use the exact characters `Final Answer` when responding.
`

The prompt starts by defining the available tools, which we will get to a bit later. The most important part of the prompt is instructing the LLM on what the output should look like. When the LLM needs to call a function, it should use the following JSON structure:

`{{
  &quot;action&quot;: $TOOL_NAME,
  &quot;action_input&quot;: $INPUT
}}
`

That’s why it is called a JSON-based agent: we instruct the LLM to produce a JSON when it wants to use any available tools. However, that is only a part of the output definition. The full output should have the following structure:

`Thought: you should always think about what to do
Action:
```
$JSON_BLOB
```
Observation: the result of the action
... (this Thought/Action/Observation can repeat N times)
Final Answer: the final answer to the original input question
`

The LLM should always expain what is it doing in the thought part of the output. When it wants to use any of the available tools, it should provide the action input as a JSON blob. The observation part is reserved for tool outputs, and when the agent decides it can return an answer to the user, it should use the final answer key. Here is an example from the movie agent using this structure.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb01ae51c6ccf78738574_1*5DxR7F0iExxB4nhim4Twpw.png)

In this example, we asked the agent to recommend a good comedy. Since one of the available tools of the agent is a recommender tool, it decided to utilize the recommender tool by providing the JSON syntax to define its input. Luckily, LangChain has a [built-in output parser of the JSON agent](https://api.python.langchain.com/en/latest/agents/langchain.agents.output_parsers.react_json_single_input.ReActJsonSingleInputOutputParser.html?ref=blog.langchain.com), so we don’t have to worry about implementing it. Next, the LLM gets a response from the tool and uses it as an observation in the prompt. Since the tool provided all the required information, the LLM decided that it had enough information to construct a final answer, which could be returned to the user.

I noticed that it’s hard to prompt engineer Mixtral in a way so that it only uses the JSON syntax when it needs to use a tool. In my experiments, when it didn’t want to use any tools, it sometimes used the following JSON action input.

`{{
  &quot;action&quot;: Null,
  &quot;action_input&quot;: &quot;&quot;
}}
`

The output parsing function in LangChain doesn’t ignore the action if it is null or similar, but returns an error that the null tool is not defined. I tried to prompt engineer a solution for this problem, but couldn’t do it in a consistent manner. Therefore, I decided to add a dummy smalltalk tool that the agent can call when the user wants to smalltalk.

`response = (
    &quot;Create a final answer that says if they &quot;
    &quot;have any questions about movies or actors&quot;
)

class SmalltalkInput(BaseModel):
    query: Optional[str] = Field(description=&quot;user query&quot;)

class SmalltalkTool(BaseTool):
    name = &quot;Smalltalk&quot;
    description = &quot;useful for when user greets you or wants to smalltalk&quot;
    args_schema: Type[BaseModel] = SmalltalkInput

    def _run(
        self,
        query: Optional[str] = None,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -&gt; str:
        &quot;&quot;&quot;Use the tool.&quot;&quot;&quot;
        return response
`

This way, the agent can decide to use a dummy Smalltalk tool when the user greets it, and we no longer have problems with parsing null or missing tool names.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb01ae51c6ccf78738570_1*zWpSjeMEuVZqSr-yQ4LwSw.png)

This workaround works quite well, so I decided to keep it. As mentioned, most models aren’t trained to produce action inputs or text if no action is required, so we have to work with what is currently available. However, sometimes the model successfully doesn’t call any tools on the first iteration as well, it depends. But giving it an escape option like the smalltalk tool seems to prevent exceptions.

## Defining tool inputs in system prompt

As mentioned, I had to figure out how to define slightly more complex tool inputs so that the LLM could correctly interpret them. Funnily enough, after implementing a custom function, I found an existing LangChain function that transforms the custom Pydantic tool input definition into a JSON object that the Mixtral recognizes.

`from langchain.tools.render import render_text_description_and_args

tools = [RecommenderTool(), InformationTool(), Smalltalk()]

tool_input = render_text_description_and_args(tools)
print(tool_input)
`

Produces the following string description:

`&quot;Recommender&quot;:&quot;useful for when you need to recommend a movie&quot;,
&quot;args&quot;:{
   {
      &quot;movie&quot;:{
         {
            &quot;title&quot;:&quot;Movie&quot;,
            &quot;description&quot;:&quot;movie used for recommendation&quot;,
            &quot;type&quot;:&quot;string&quot;
         }
      },
      &quot;genre&quot;:{
         {
            &quot;title&quot;:&quot;Genre&quot;,
            &quot;description&quot;:&quot;genre used for recommendation. Available options are:[&#x27;Action&#x27;, &#x27;Adventure&#x27;, &#x27;Animation&#x27;, &#x27;Children&#x27;, &#x27;Comedy&#x27;, &#x27;Crime&#x27;, &#x27;Documentary&#x27;, &#x27;Drama&#x27;, &#x27;Fantasy&#x27;, &#x27;Film-Noir&#x27;, &#x27;Horror&#x27;, &#x27;IMAX&#x27;, &#x27;Musical&#x27;, &#x27;Mystery&#x27;, &#x27;Romance&#x27;, &#x27;Sci-Fi&#x27;, &#x27;Thriller&#x27;, &#x27;War&#x27;, &#x27;Western&#x27;]&quot;,
            &quot;type&quot;:&quot;string&quot;
         }
      }
   }
},
&quot;Information&quot;:&quot;useful for when you need to answer questions about various actors or movies&quot;,
&quot;args&quot;:{
   {
      &quot;entity&quot;:{
         {
            &quot;title&quot;:&quot;Entity&quot;,
            &quot;description&quot;:&quot;movie or a person mentioned in the question&quot;,
            &quot;type&quot;:&quot;string&quot;
         }
      },
      &quot;entity_type&quot;:{
         {
            &quot;title&quot;:&quot;Entity Type&quot;,
            &quot;description&quot;:&quot;type of the entity. Available options are &#x27;movie&#x27; or &#x27;person&#x27;&quot;,
            &quot;type&quot;:&quot;string&quot;
         }
      }
   }
},
&quot;Smalltalk&quot;:&quot;useful for when user greets you or wants to smalltalk&quot;,
&quot;args&quot;:{
   {
      &quot;query&quot;:{
         {
            &quot;title&quot;:&quot;Query&quot;,
            &quot;description&quot;:&quot;user query&quot;,
            &quot;type&quot;:&quot;string&quot;
         }
      }
   }
}
`

We can simply copy this tool description in the system prompt and Mixtral will be able to use the defined tools, which is quite cool.

## Conclusion

Most of the work to implement the JSON-based agent was done by Harrison Chase and the LangChain team, for which I am grateful. All I had to do was find the puzzle pieces and put them together. As mentioned, don’t expect the same level of agent performance as with GPT-4. However, I think the more powerful OSS LLMs like Mixtral could be used as agents today (with a bit more exception handling than GPT-4). I am looking forward to more open source LLMs being fine-tuned as agents.

The [code is available as a Langchain template](https://github.com/langchain-ai/langchain/tree/master/templates/neo4j-semantic-ollama?ref=blog.langchain.com) and as a [Jupyter notebook](https://github.com/tomasonjo/blogs/blob/master/llm/ollama_semantic_layer.ipynb?ref=blog.langchain.com).

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc07193192cebc73980fd3_logo%20and%20title%20-%2020%20characters%20max%20(6).png)PartnerDeep Agents

#### Building a company due diligence agent with Deep Agents, LangSmith and Parallel

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01c6959ca5fd924ab432_MattHarris.jpg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01b812793b72539057d5_nick%20headshot.jpeg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd2d50cd0f84dacf92e7b_ProfilePic.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd29baf4c28709e2566a7_headshot.jpg)Matt HarrisNick MartitschSrimanth TangedipalliKaran SinghMay 8, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)9min[](/blog/building-a-company-due-diligence-agent-with-deep-agents-langsmith-and-parallel)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e23754937c2f749d12bb0b_76%20(1).png)Agent ArchitecturePartner

#### Agentic Engineering: How Swarms of AI Agents Are Redefining Software Engineering

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e234176723e6111407b935_renuka-kumar.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e23427e77d2631610e5d62_Prashanth-Ramagopal.png)Renuka KumarPrashanth RamagopalApril 17, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)11min[](/blog/agentic-engineering-redefining-software-engineering)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e122306b7173e8fad25030_81%20(1).png)LangChainPartner

#### A Developer’s First 10 Minutes: Secure LangChain Agents with Cisco AI Defense

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0e375654393ca0c125e00_siddhant-dash.png)Siddhant DashApril 16, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/secure-agents-cisco-ai-defense)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)