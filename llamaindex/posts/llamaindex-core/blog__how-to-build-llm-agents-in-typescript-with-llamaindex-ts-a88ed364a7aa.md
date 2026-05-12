---
title: "LLM Agents in TypeScript: Step-by-Step Guide | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/how-to-build-llm-agents-in-typescript-with-llamaindex-ts-a88ed364a7aa"
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







Agents are autonomous systems that can execute end-to-end tasks without much or fewer instructions. These agents are capable of solving tasks related to questions and answering, using tools to achieve a desired behavior, or even planning tasks.



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



In this article, we will explore a few capabilities of LlamaIndex.TS’s built-in agents to achieve a set of goals. We have two parts:

- [Building a simple agent for calculation.](#cb81)
- [Using agents with your personal/private data to answer questions.](#b49b)

All the full code examples will be at the end of the post.

# Setup

To start you need to have `llamaindex` package installed on your node environment setup and an OpenAI key.

To install the package:

npm install llamaindex To set up the OpenAI key you can set your environment variable:

export OPENAI_API_KEY=sk-***************

# Agent for calculations

The first agent will be responsible for getting a user input of numbers and based on this selecting the right tools to achieve the task

## Import the classes:

import { FunctionTool, OpenAIAgent } from "llamaindex";

## Function Tool

The first step will be creating tools that the agent will have access to, we will be creating an `add` function and a `multiply` function.

OpenAI provides us a function calling API which we can send our function arguments and get back a response

We start by creating two functions:

// Define a function to sum two numbers
function sum({ a, b }: { a: number; b: number }): number {
  return a + b;
}

// Define a function to multiply two numbers
function multiply({ a, b }: { a: number; b: number }): number {
  return a * b;
}Now we can set up the `FunctionTool` class which will be given to the agent, this class requires the properties of the function and metadata for the tool, helping the Large Language Models (LLMs) to identify which tool the LLM should use and the parameters.

// Sum properties to give to the LLM
const sumJSON = {
  type: "object",
  properties: {
    a: {
      type: "number",
      description: "The first number",
    },
    b: {
      type: "number",
      description: "The second number",
    },
  },
  required: ["a", "b"],
};

// Multiply properties to give to the LLM
const multiplyJSON = {
  type: "object",
  properties: {
    a: {
      type: "number",
      description: "The number to multiply",
    },
    b: {
      type: "number",
      description: "The multiplier",
    },
  },
  required: ["a", "b"],
};

// Create sum function tool
const sumFunctionTool = new FunctionTool(sum, {
  name: "sum",
  description: "Use this function to sum two numbers",
  parameters: sumJSON,
});

// Creat multiply function tool
const multiplyFunctionTool = new FunctionTool(multiply, {
  name: "multiply",
  description: "Use this function to multiply two numbers",
  parameters: multiplyJSON,
});

## Chat with Agent

Now we have the tools to give to the agent, we can set up the agent:

// Setup the agent with the respective tools
const agent = new OpenAIAgent({
  tools: [sumFunctionTool, multiplyFunctionTool],
  verbose: true,
});And then ask a question:

// Chat with LLM
const response = await agent.chat({
  message: "How much is 5 + 5? then multiply by 2",
});

// Agent output
console.log(String(response));Now the agent will choose the right tools to achieve the desired task using the functions provided by you. Then you should see an output as:

=== Calling Function ===
Calling function: sum with args: {
  "a": 5,
  "b": 5
}
Got output 10
==========================
=== Calling Function ===
Calling function: multiply with args: {
  "a": 10,
  "b": 2
}
Got output 20
==========================
The result of adding 5 and 5 is 10. When you multiply 10 by 2, the result is 20.

# Using Agents with your documents

The second agent will be responsible for going through a set of Dan Abramov essays and answering questions based on the available data.

Firstly, we will import the necessary classes and functions

## Import the classes and functions

import {
  OpenAIAgent,
  SimpleDirectoryReader,
  VectorStoreIndex,
  SummaryIndex,
  QueryEngineTool,
} from "llamaindex";

## Loading Documents

Now we will load the documents and insert them into a local vector store index which will be responsible for storing the documents and allowing the agent to query the most relevant data for the task and a summarize vector index which can better help on tasks summary related.

// Load the documents
const documents = await new SimpleDirectoryReader().loadData({
  directoryPath: "node_modules/llamaindex/examples",
});

// Create a vector index from the documents
const vectorIndex = await VectorStoreIndex.fromDocuments(documents);
const summaryIndex = await SummaryIndex.fromDocuments(documents)

## Creating the Query Engine Tool

Now we will create the tooling that allows the Agents to access the Vector Index:

// Create a query engine from the vector index
const abramovQueryEngine = vectorIndex.asQueryEngine();
const abramovSummaryEngine = summaryIndex.asQueryEngine();

// Create a QueryEngineTool with the vector engine
const vectorEngineTool = new QueryEngineTool({
  queryEngine: abramovQueryEngine,
  metadata: {
    name: "abramov_query_engine",
    description: "Use this engine to answer specific questions about Abramov",
  },
});

// Create a QueryEngineTool with the summary engine
const summaryEngineTool = new QueryEngineTool({
  queryEngine: abramovSummaryEngine,
  metadata: {
    name: "abramov_summary_engine",
    description: "Use this engine to generate summaries about Abramov",
  },
});

## Creating the OpenAI Agent

Now we can create and provide the necessary tools for the agent

// Setup the agent
const agent = new OpenAIAgent({
  tools: [vectorEngineTool, summaryEngineTool],
  verbose: true,
});

## Chat with Agent

Now you can chat with the agent about Dan Abramov and it will select the right tools to achieve the goal.

// Chat with Agent
const response = await agent.chat({
  message: "Where he worked in his 20s?",
});

// Log output
console.log(String(response));The tool output

=== Calling Function ===
Calling function: abramov_query_engine with args: {
  "query": "work experience in 20s"
}
Got output The individual had their first job as a software developer in their 20s. They worked for a Russian-American outsourcing company and their salary was $18k/year.
==========================
In his 20s, Abramov worked as a software developer for a Russian-American outsourcing company. His salary during that time was $18,000 per year.

# Conclusion

Autonomous agents are powerful when talking about creating workflows and automation that can take your business to the next level or make your life easier.

There is still a long way to go before they are fully autonomous but the arrival of LLMs is allowing the first steps of these reasoning and decision-making engines

Do you already use agents in your day-to-day? and wanna discuss agents or help with agents? Reach me on [Twitter](https://twitter.com/manelferreira_)

# References

Code example: [https://github.com/EmanuelCampos/agents-typescript-example](https://github.com/EmanuelCampos/agents-typescript-example)

LLamaIndexTS Documentation: [https://ts.llamaindex.ai/modules/agent/openai](https://ts.llamaindex.ai/modules/agent/openai)

[https://www.llamaindex.ai/](https://www.llamaindex.ai/)