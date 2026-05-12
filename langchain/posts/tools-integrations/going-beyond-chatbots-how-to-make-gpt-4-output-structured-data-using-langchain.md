---
title: "Going Beyond Chatbots: How to Make GPT-4 Output Structured Data Using LangChain"
author: "LangChain Accounts"
date: "2023-05-22"
url: "https://www.langchain.com/blog/going-beyond-chatbots-how-to-make-gpt-4-output-structured-data-using-langchain"
---

Tutorials &amp; How-Tos

# Going Beyond Chatbots: How to Make GPT-4 Output Structured Data Using LangChain

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamMay 21, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)4min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb21cba9d0fc72378175c_screenshot-2023-05-21-at-8.20.41-pm.png)By [Jacob Lee](https://twitter.com/hacubu?lang=en&amp;ref=blog.langchain.com)

Over the past few months, I had the opportunity to do some cool exploratory work for a client that integrated LLMs like GPT-4 and Claude into their internal workflow, rather than exposing them through a chat interface. The general idea was to take some input data, analyze it using an LLM, enrich the LLM&#x27;s output using existing data sources, and then sanity check it using both traditional tools and LLMs. This process could repeat several times until finally storing a final result in a database. I&#x27;ve been thinking of it as a pipeline that mixes LLMs with more mundane APIs where the output of one step feeds directly into the next.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb21cba9d0fc723781768_d171ad3e-19b0-498f-923c-c268d0a7c98b.jpeg)

## **The Problem**

While building such pipelines, I quickly realized that while natural language is an excellent interface for a chatbot, it&#x27;s quite a difficult one to use with existing APIs.

To illustrate this, let&#x27;s say you wanted to generate and store a list of countries in Airtable. Naively asking an LLM `Give me a list of 5 countries` results in a numbered list of countries:

`&#x27;1. United States\n&#x27; +
&#x27;2. Canada\n&#x27; +
&#x27;3. United Kingdom\n&#x27; +
&#x27;4. Australia\n&#x27; +
&#x27;5. Japan&#x27;
`

There are a few problems here - while the above output happens to be a numbered list, there is no guarantee of that. Also, you would need to write some awkward custom string parsing logic to extract the data for use in the next step of the pipeline.

The solution is to prompt the LLM to output data in some structured format, but it&#x27;s not quite that simple. For example, asking, `Give me a list of 5 countries, formatted as Airtable records` might result in something like this:

`&#x27;Airtable records require a unique ID and field values in a JSON format. Here is a list of 5 countries formatted as Airtable records:\n&#x27; +
&#x27;\n&#x27; +
&#x27;1. {\n&#x27; +
&#x27;  &quot;id&quot;: &quot;rec1&quot;,\n&#x27; +
&#x27;  &quot;fields&quot;: {\n&#x27; +
&#x27;    &quot;Country&quot;: &quot;United States&quot;,\n&#x27; +
&#x27;    &quot;Continent&quot;: &quot;North America&quot;\n&#x27; +
&#x27;  }\n&#x27; +
&#x27;}\n&#x27; +
&#x27;2. {\n&#x27; +
&#x27;  &quot;id&quot;: &quot;rec2&quot;,\n&#x27; +
&#x27;  &quot;fields&quot;: {\n&#x27; +
&#x27;    &quot;Country&quot;: &quot;Canada&quot;,\n&#x27; +
&#x27;    &quot;Continent&quot;: &quot;North America&quot;\n&#x27; +
&#x27;  }\n&#x27; +
&#x27;}\n&#x27; +
...
`

Though the LLM (in this case GPT-4) impressively knows the general schema of an Airtable record, this is even worse than the original attempt. There is conversational text at the top that must be parsed out, and the output format is still a numbered list. Additionally, the LLM has assumed the field names of your Airtable schema, which likely do not match your internal definitions.

I experimented with a few custom prompting strategies like `Output only an array of JSON objects containing X, Y, and Z`, but adding such language to all my prompts quickly became tedious. Furthermore, this was somewhat unreliable due to the non-deterministic nature of LLMs, particularly with long, complex prompts and higher temperatures.

## **The Solution**

I had already been using [LangChainJS](https://github.com/hwchase17/langchainjs?ref=blog.langchain.com), an open-source framework that helps with building complex applications around LLMs, for various pieces of the project. After asking around their Discord community, I discovered an elegant, built-in solution: [output fixing parsers](https://js.langchain.com/docs/modules/prompts/output_parsers/?ref=blog.langchain.com#output-fixing-parser)!

Output fixing parsers contain two components:

- An easy, consistent way of generating output formatting instructions (using a popular TypeScript validation framework, [Zod](https://github.com/colinhacks/zod?ref=blog.langchain.com)).
- An LLM-powered recovery mechanism for handling badly formatted outputs using a more focused prompt.

You could use one to solve the earlier problem like this (note that you will need to run `yarn add langchain` and `yarn add zod` if they aren&#x27;t already in your dependencies):

`import { z } from &quot;zod&quot;;
import { ChatOpenAI } from &quot;langchain/chat_models/openai&quot;;
import { PromptTemplate } from &quot;langchain/prompts&quot;;
import { LLMChain } from &quot;langchain/chains&quot;;
import {
  StructuredOutputParser,
  OutputFixingParser
} from &quot;langchain/output_parsers&quot;;

const outputParser = StructuredOutputParser.fromZodSchema(
  z.array(
    z.object({
      fields: z.object({
        Name: z.string().describe(&quot;The name of the country&quot;),
        Capital: z.string().describe(&quot;The country&#x27;s capital&quot;)
      })
    })
  ).describe(&quot;An array of Airtable records, each representing a country&quot;)
);

const chatModel = new ChatOpenAI({
  modelName: &quot;gpt-4&quot;, // Or gpt-3.5-turbo
  temperature: 0 // For best results with the output fixing parser
});

const outputFixingParser = OutputFixingParser.fromLLM(
  chatModel,
  outputParser
);

const prompt = new PromptTemplate({
  template: `Answer the user&#x27;s question as best you can:\n{format_instructions}\n{query}`,
  inputVariables: [&#x27;query&#x27;],
  partialVariables: {
    format_instructions: outputFixingParser.getFormatInstructions()
  }
});

// For those unfamiliar with LangChain, a class used to call LLMs
const answerFormattingChain = new LLMChain({
  llm: chatModel,
  prompt: prompt,
  outputKey: &quot;records&quot;, // For readability - otherwise the chain output will default to a property named &quot;text&quot;
  outputParser: outputFixingParser
});

const result = await answerFormattingChain.call({
  query: &quot;List 5 countries.&quot;
});

console.log(JSON.stringify(result.records, null, 2));
`

Clean and readable! And here&#x27;s an example of what the results look like:

`[
  {
    &quot;fields&quot;: {
      &quot;Name&quot;: &quot;United States&quot;,
      &quot;Capital&quot;: &quot;Washington, D.C.&quot;
    }
  },
  {
    &quot;fields&quot;: {
      &quot;Name&quot;: &quot;Canada&quot;,
      &quot;Capital&quot;: &quot;Ottawa&quot;
    }
  },
  {
    &quot;fields&quot;: {
      &quot;Name&quot;: &quot;Germany&quot;,
      &quot;Capital&quot;: &quot;Berlin&quot;
    }
  },
  {
    &quot;fields&quot;: {
      &quot;Name&quot;: &quot;Japan&quot;,
      &quot;Capital&quot;: &quot;Tokyo&quot;
    }
  },
  {
    &quot;fields&quot;: {
      &quot;Name&quot;: &quot;Australia&quot;,
      &quot;Capital&quot;: &quot;Canberra&quot;
    }
  }
]
`

Success! The result will already be typed as an array of objects, so there&#x27;s no need for `JSON.parse()` calls or any further parsing.

Note that the output fixing parser will throw an error if, for whatever reason, it can&#x27;t generate an output matching the provided Zod schema. You could even pipe it directly into an Airtable API call!

## **Additional Tips**

Descriptions provided with `.describe()` are optional, but give the LLM helpful context when populating individual fields. The LLM will also use clues like the field name and the overall structure of the provided schema.

- If you&#x27;re struggling to generate output in the right format, adding descriptions or tweaking the language in these descriptions can help.
- You can use different model instances in the output fixing parser and whatever chain you&#x27;re using, allowing you to mix and match temperatures and even providers for best results.

## **Thanks for Reading!**

I hope this post helps you better use the power of LLMs in your projects!

I&#x27;ve actually enjoyed building with LLMs and specifically [LangChain](https://js.langchain.com/?ref=blog.langchain.com) so much that I recently joined their team, so expect to see more related content over the coming months! And if you have any questions or have ideas for what you&#x27;d like me to write about next, reach out to me on Twitter [@Hacubu](https://twitter.com/hacubu?lang=en&amp;ref=blog.langchain.com). I&#x27;ll be active in the JS channels of [LangChain&#x27;s community Discord server](https://discord.com/invite/6adMQxSpJS?ref=blog.langchain.com) as well.

Happy prompting!

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cba9b9e7ec0692a2d079af_gtm-agent-diagram-1--6-.png)Tutorials &amp; How-Tos

#### How we built LangChain’s GTM Agent

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamMarch 9, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)11min[](/blog/how-we-built-langchains-gtm-agent)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa2fcd1956c2e4fa1ff2_Evaluating-Deep-Agents.png)Deep AgentsAgent ArchitectureTutorials &amp; How-Tos

#### Evaluating Deep Agents: Our Learnings

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamDecember 3, 2025![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)9min[](/blog/evaluating-deep-agents-our-learnings)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa490b26292282bdb573_Rebuilding-Chat-LangChain.png)Company AnnouncementsTutorials &amp; How-Tos

#### Why We Rebuilt LangChain’s Chatbot and What We Learned

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamNovember 5, 2025![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)13min[](/blog/rebuilding-chat-langchain)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)