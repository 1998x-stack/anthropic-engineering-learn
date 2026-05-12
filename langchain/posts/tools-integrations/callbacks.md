---
title: "Callbacks Improvements"
author: "LangChain Accounts"
date: "2023-05-01"
url: "https://www.langchain.com/blog/callbacks"
---

Agent Architecture

# Callbacks Improvements

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamMay 1, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)3min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb23103935dbc92e0a720_photo-1520923642038-b4259acecbd7.jpeg)**TL;DR**: We&#x27;re announcing improvements to our callbacks system, which powers logging, tracing, [streaming output](https://python.langchain.com/docs/modules/model_io/models/llms/how_to/streaming_llm?ref=blog.langchain.com), and some awesome [third-party integrations](https://python.langchain.com/docs/ecosystem/integrations/?ref=blog.langchain.com). This will better support concurrent runs with independent callbacks, tracing of deeply nested trees of LangChain components, and callback handlers scoped to a single request (which is super useful for deploying LangChain on a server).

- [Python docs](https://python.langchain.com/docs/modules/callbacks/?ref=blog.langchain.com)
- [JS docs](https://js.langchain.com/docs/production/callbacks/?ref=blog.langchain.com)

### Context

Originally we designed the callbacks mechanism in LangChain to be used in non-async Python applications. Now that we have support for both `asyncio` Python usage as well LangChain in JavaScript/TypeScript, we needed some better abstractions native to this new world where many concurrent LangChain runs can be inflight in the same thread or in multiple threads. Additionally, it became clear that developers using LangChain in web environments often wanted to scope a callback to a single request (so they can pass it a specific handle to a websocket, for example).

## Changes

We&#x27;ve made some changes to our callbacks mechanism to address these issues:

- You can now declare which callbacks you want either in constructor args (which apply to all runs), or passing them directly to the `run` / `call` / `apply` methods that start a run. *Constructor callbacks* will be used for all calls made on that object, and will be scoped to that object only, i.e. if you pass a handler to the `LLMChain` constructor, it will not be used by the model attached to that chain.
- *Request callbacks* will be used for that specific request only, and all sub-requests that it contains (eg. a call to an LLMChain triggers a call to a Model, which uses the same handler passed in the `call()` method). These are explicitly passed through. An example to make this more concrete: when a handler is passed through to an `AgentExecutor` via `run`, it will be used for all callbacks related to the agent and all the objects involved in the agent’s execution, in this case, the `Tools`, `LLMChain`, and `LLM`. Previously, to use a callback scoped to particular agent run, that callback manager had to be attached to all nested objects – this was tedious, ugly, and made it hard to re-use objects. See the TypeScript example below:

`// What had to be done before for run-scoped custom callbacks. Very tedious!
const executors = [];
for (let i = 0; i &lt; 3; i += 1) {
  const callbackManager = new CallbackManager();
  callbackManager.addHandler(new ConsoleCallbackHandler());
  callbackManager.addHandler(new LangChainTracer());

  const model = new OpenAI({ temperature: 0, callbackManager });
  const tools = [new SerpAPI(), new Calculator()];
  for (const tool of tools) {
    tool.callbackManager = callbackManager;
  }
  const executor = await initializeAgentExecutor(
    tools,
    model,
    &quot;zero-shot-react-description&quot;,
    true,
    callbackManager
  );
  executor.agent.llmChain.callbackManager = callbackManager;
  executors.push(executor);
}

const results = await Promise.all(
  executors.map((executor) =&gt; executor.call({ input }))
);
for (const result of results) {
  console.log(`Got output ${result.output}`);
}`

- `_call`, `_generate`, `_run`, and equivalent async methods on Chains / LLMs / Chat Models / Agents / Tools now receive a 2nd argument called `runManager` which is bound to that run, and contains the logging methods that can be used by that object (i.e. `handleLLMNewToken`). This is useful when constructing custom chains, for example, and you can find [more info here](https://python.langchain.com/docs/modules/chains/how_to/custom_chain?ref=blog.langchain.com).
- The `verbose` argument now just serves as a shortcut to add a `ConsoleCallbackHandler` in JS and `StdOutCallbackHandler` in python that prints events to stdout. **It does not control other callbacks**.

Tracing and other callbacks now [*just work* with concurrency](https://python.langchain.com/docs/modules/callbacks/how_to/tracing?ref=blog.langchain.com). We&#x27;ve also added a context manager to make tracing specific runs even easier.

## Breaking Changes and Deprecations:

- Any code that relied on global callbacks or the global tracer (i.e. `SharedCallbackManager`, `SharedTracer`) outside of LangChain will break in versions &gt;0.0.153 of the python package.
- Attaching a `CallbackManager` to an object is now deprecated, use the `callbacks` argument to pass in a list of handlers.
- The `verbose` flag now only controls `stdout` and `console` callbacks, not other callbacks.

## Inspiration

When we were implementing these improvements to Callbacks we looked at a few existing solutions that ended up influencing the final API, worth calling out:

- The Python `logging` module (and others), which offers a `getChild` method that returns a new logger bound to a certain context. This inspired the new `runManager.getChild()` which you can use when implementing a custom Chain to ensure child runs are tracked correctly.
- Web server frameworks like `express` where all the context specific to each HTTP request is passed around explicitly as function arguments, rather than being available as some sort of global variable.

We also considered the alternative of using some form of async context variables, an implementation of which exists in [Python](https://docs.python.org/3/library/contextvars.html?ref=blog.langchain.com) and in [Node.js](https://nodejs.org/api/async_context.html?ref=blog.langchain.com) (but not in other JS environments). In the end we decided for the explicit function arguments approach because it is easier to debug, and more compatible cross-platform (function args work just about anywhere).

Please let us know if you run into any issues, as this was a large change!

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69f20536df00c0eb15eab1d3_blue-77%20characters%20max.png)Deep AgentsAgent ArchitectureOpen Source

#### Tuning Deep Agents to Work Well with Different Models

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcefac505b6b48827abf84_vivek-trivedy.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcf032ce65a32e276a4d0a_mason-daugherty.png)Vivek TrivedyMason DaughertyApril 29, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)5min[](/blog/tuning-deep-agents-different-models)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef96ff74c638e982ff68c6_86%20(1).png)Agent ArchitectureLangSmithOpen Source

#### How LangSmith and LangChain OSS Help You Meet EU AI Act Requirements

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0003a1af368dfae13c23c_jacob-talbot.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Jacob TalbotBecca WengApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/langsmith-langchain-oss-eu-ai-act)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e23754937c2f749d12bb0b_76%20(1).png)Agent ArchitecturePartner

#### Agentic Engineering: How Swarms of AI Agents Are Redefining Software Engineering

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e234176723e6111407b935_renuka-kumar.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e23427e77d2631610e5d62_Prashanth-Ramagopal.png)Renuka KumarPrashanth RamagopalApril 17, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)11min[](/blog/agentic-engineering-redefining-software-engineering)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)