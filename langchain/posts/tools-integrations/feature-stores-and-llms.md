---
title: "Feature Stores and LLMs"
author: "LangChain Accounts"
date: "2023-05-09"
url: "https://www.langchain.com/blog/feature-stores-and-llms"
---

Agent Architecture

# Feature Stores and LLMs

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamMay 9, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)5min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb22444d72d9752573164_photo-1600137175990-437ff58e6729.jpeg)**Editor&#x27;s note: big thank you to **[**Willem Pienaar**](https://twitter.com/willpienaar?ref=blog.langchain.com)** (**[**Feast**](https://github.com/feast-dev/feast?ref=blog.langchain.com)**), **[**Mike Del Balso**](https://twitter.com/mikedelbalso?ref=blog.langchain.com)** (**[**Tecton**](https://www.tecton.ai/?ref=blog.langchain.com)**), and **[**Simba Khadder**](https://twitter.com/simba_khadder?ref=blog.langchain.com)** (**[**FeatureForm**](https://www.featureform.com/?ref=blog.langchain.com)**) for their comments and help on this post.**

LLMs represent a new paradigm of AI. There is a big open question of how many of the tools and services that were useful for traditional machine learning are still relevant here. On one hand, there are very real new use cases and requirements for this new paradigm. On the other hand, existing tools and services have years of experience, development, and feature hardening. Are these tools still useful in this new paradigm?

### Feature stores overview

One particularly interesting case study is feature stores. In traditional machine learning, the input to models is not raw text or an image, but rather a series of engineered “features” related to the datapoint at hand. A feature store is a A feature store is a system meant to centralize and serve ML features to models. There are usually two benefits:

- A way of keeping track of what features are present at a particular point in time to use in model training
- A real-time pipeline of features to use when doing inference

How might these apply to LLM applications?

The first point seems not as relevant. Most folks are using pre-trained LLMs from OpenAI, Anthropic, etc and not training their own models from scratch.

On the other hand, we believe that the second benefit (a real-time pipeline of features to use when doing inference) is still extremely relevant. We believe that a real-time pipeline of features (enabled by a feature store) can be used to achieve real-time personalization of LLM applications. Although we do not see a lot of this at the moment, we believe that this will become more popular as applications become more advanced.

An LLM is a &quot;reasoning engine,&quot; just like a person. There are a whole set of tasks that would be much easier to reason for if you also had ready access to fresh data about your user or business. E.g. if you are asking a person to estimate how long will take to drive from a to b, they&#x27;d probably make a way better decision if they also knew which road segments there were between a and b and how much traffic is on those segments right now.

This kind of added context or data enrichment has been widely used in traditional ML for a long time. Some models have 1000s of features. Although LLMs make it possible to solve some ML tasks with only user prompts, a large set of tasks can only be completed at competitive accuracy with a lot of context data.

### Prompting overview

Language model applications are largely defined by how their prompts are constructed. Therefore, before trying to think about how feature stores could impact language model applications, we should try to understand different ways of constructing prompts, and then think about how feature stores could impact prompt construction. Below are probably the three most common types of prompt construction, ordered from least complex to most complex.

**#1: Hard coded prompt string**

This is when the entire prompt that is passed into the language model is hard coded by the application. There is no customization done to the prompt, and therefore all the variation in output comes from the language model. This is an incredibly simple prompting strategy that honestly is likely so simple it’s rarely used.

**#2: Incorporating user input**

The next step is incorporating user input into the prompt string. This means having a prompt template, and filling in the variables with user input that they put in at run time. An example of an application like this could be a poem-generating application. This application could ask the user for a `subject` input, and then format a prompt like `Write me a poem about {subject}` before passing that to the language model. This can be done with multiple variables, but the important part is it is taking in user input at runtime and formatting a string with those variables.

**#3: Incorporating basic real-time system data**

It can often be helpful to include basic, real time system data into the prompt. The most common example of this is incorporating the current date and time. This is not something that you would want to hard code (because it changes constantly). This can be helpful in order to give the language a sense of the current state of the system/world.

**#4: Incorporating external data fetched based on user input**

Another step up is using the user provided input to fetch even more information to put into a prompt. A good example of this is all the question-answering applications. Those applications generally use a prompt template like:

`Answer the following question: {question}
Only use the following information to answer:
{context}
Answer:
`

There are two variables this prompt expects: `question` and `context`. Question is usually provided at run-time by the user, and context is data that is fetched (usually via a retrieval system) that is relevant to the user input.

This already allows for a certain type of “personalization” - depending on the retriever that is used, that context can be used to “personalize” an application so that it can respond about a specific type of data.

### Feature stores &lt;&gt; Prompting

Those are the four main prompt construction strategies that we see today. We think feature stores can supercharge prompt construction - by allowing for inclusion of real-time, complex, and often user-based, information.

This is combining key ideas from existing prompt construction methods. When we insert things like the current date and time, we are injecting knowledge of the current state of the world into the prompt - but it is very simple and general knowledge. When we insert external data fetched based on user input, we are incorporating more personalized data - but it is largely based solely on user input.

To see this in play, we can head over to the [feast GitHub repository](https://github.com/feast-dev/feast?ref=blog.langchain.com) - one of the more popular open source feature stores. Let’s look at the example on the README.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb22444d72d975257316c_3bf8ee2d.png)

In this example we are fetching realtime, user specific information. In traditional ML models this information would be fed in as feature values into a model, but now we can feed it into the prompt!

To see how this can be done, we’ve set up an example notebook showing how to connect a feature store to a prompt template. Putting it inside a prompt template allows us to nicely package up that logic and pass it through the chain. When we then call that chain, real-time information can be fetched via feast and used to construct a prompt which is then passed into the language model.

See the example notebook for this [here](https://python.langchain.com/docs/modules/model_io/prompts/prompt_templates/connecting_to_a_feature_store?ref=blog.langchain.com). We do this for a variety of feature stores: feast, [Tecton](https://www.tecton.ai/?ref=blog.langchain.com), [FeatureForm](https://www.featureform.com/?ref=blog.langchain.com). Here’s an example of the code for doing it with Tecton - as you can see - it’s really quite simple!

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb22444d72d975257316f_2b5c27f0.png)

This is obviously a simple example, but we believe it highlights the power of this approach and hints at a future where this is more common. Many language model applications are still struggling to get off the ground, but as time progresses we believe real-time, user-level information will be used to construct prompts and provide a superior, personalized end-user experience. Examples of potential applications include chatbots with real-time context, marketing content with personalized context, and recommendations given recent user session history. As we move toward this world, we believe existing feature stores are well-positioned to help do so.

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