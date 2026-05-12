---
title: "OpaquePrompts x LangChain: Enhance the privacy of your LangChain application with just one code change"
author: "LangChain Accounts"
date: "2023-09-12"
url: "https://www.langchain.com/blog/opaqueprompts-x-langchain-enhance-the-privacy-of-your-langchain-application-with-just-one-code-change"
---

PartnerLangChain

# OpaquePrompts x LangChain: Enhance the privacy of your LangChain application with just one code change

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamSeptember 12, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)4min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb16c90227306de7e3f8a_5-social--23-.png)*Editor&#x27;s Note: This blog post was written in collaboration with the *[*Opaque*](https://opaque.co/?ref=blog.langchain.com)* team. As more apps get into production, we&#x27;ve been hearing more teams talk about solutions for data privacy. Opaque&#x27;s seamless integration with LangChain ensures personal information in your users’ prompts will be hidden from the LLM provider with just a few lines of code.*

We’ve been hearing growing feedback from our users that they want to keep their data private from LLM providers, whether it be OpenAI, Anthropic, Cohere, or others, for a number of reasons:

- Concerns about data retention
- Concerns about the LLM provider seeing the input data
- Concerns about the provider using user inputs to continually train the LLM
- Concerns about the LLM leaking data the model was trained on

The same is true for LLM application builders at companies of all sizes—from enterprise to small startups—across a variety of verticals. One startup we talked to is building a knowledge management solution that summarizes stored documents, but a potential customer, a law firm, doesn’t trust third-party providers with their legal documents. Another is building an application to generate targeted advertisements based off user data, but must strictly control how personal user information is shared and used by third-party providers. A large bank wants to automate risk assessment, which, in its manual form, requires meticulous analysis of sensitive documents whose contents cannot be shared with third-party providers in its plaintext form.

All these use cases and more have one common theme: an LLM application developer wants to leverage an LLM to operate on sensitive data, but cannot do so because of concerns about or restrictions on the LLM provider’s ability to see, process, and store the sensitive data. This is where OpaquePrompts comes in.

# An introduction to OpaquePrompts

OpaquePrompts serves as a privacy layer around your LLM of choice. With OpaquePrompts, you can:

- **Automatically identify sensitive tokens** in your prompts with natural language processing (NLP)-based machine learning
- **Pre-process LLM inputs to hide sensitive inputs** in your prompts from LLM providers via a sanitization mechanism
- For example, in the prompt, every instance of the name `John Smith` will be deterministically replaced with `PERSON_1`.
- **Post-process LLM responses** to replace all sanitized instances with the original sensitive information
- For example, in the LLM response, all instances of `PERSON_1` will be replaced with `John Smith`.
- **Leverage the power of **[**confidential computing**](https://en.wikipedia.org/wiki/Confidential_computing?ref=blog.langchain.com) to ensure that not even the OpaquePrompts service sees the underlying prompt
- OpaquePrompts runs in an [attestable](https://www.redhat.com/en/blog/attestation-confidential-computing?ref=blog.langchain.com) [trusted execution environment](https://en.wikipedia.org/wiki/Trusted_execution_environment?ref=blog.langchain.com), meaning that you can cryptographically verify that not even Opaque can see any input to OpaquePrompts.
- More on OpaquePrompts architecture and security guarantees can be found in the [documentation](https://promptguard.readthedocs.io/en/latest/?ref=blog.langchain.com).
- **Make your application privacy-preserving** by modifying just one line of code in your LangChain application
- See an example [here](https://github.com/opaque-systems/opaqueprompts-chat-server/blob/dev/python-package/src/opchatserver/server.py?ref=blog.langchain.com).

An application built with OpaquePrompts works as follows:

- The OpaquePrompts service takes in a constructed prompt.
- Using a state-of-the-art model, OpaquePrompts identifies sensitive information in the prompt.
- OpaquePrompts sanitizes the prompt by encrypting all identified personal information before returning the sanitized prompt to the LLM application.
- The LLM application sends the sanitized prompt to its LLM provider of choice.
- The LLM application receives a response from the LLM provider, which contains the post-sanitization identifiers.
- The LLM application sends the response to OpaquePrompts, which de-sanitizes the response by decrypting previously encrypted personal information.
- The LLM application returns the de-sanitized response to the user. From the user’s perspective, the response appears as if the original prompt were sent directly to the LLM.

Using GIFs, we compare LLM application workflows with and without OpaquePrompts. Without OpaquePrompts, the prompt goes directly from LLM application to the model provider, all in the clear.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb16d90227306de7e3fbd_OpaquePrompts-dataflow----without-Opaque-v2.gif)

With OpaquePrompts, the prompt first gets securely sanitized by the OpaquePrompts service (and the service doesn’t see the contents of the prompt) before making its way to the LLM provider for a response.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb16d90227306de7e3fb1_OpaquePrompts-dataflow---with-Opaque-15fps-L-1.gif)

# Modifying a chatbot built with LangChain to incorporate OpaquePrompts

Below, we walk through how we modified an existing GPT-based chat application built with LangChain to hide sensitive information from prompts sent to OpenAI.

The server-side with a `/chat` endpoint of a vanilla chat application looks something like the following.

`
# Full source code can be found here: &lt;https://github.com/opaque-systems/opaqueprompts-chat-server&gt;

class ChatRequest(BaseModel):
    history: Optional[list[str]]
    prompt: str

class ChatResponse(BaseModel):
    response: str

async def chat(
    chat_request: ChatRequest,
) -&gt; ChatResponse:
	  &quot;&quot;&quot;
		Defines an endpoint that takes in a prompt and sends it to
		GPT

		Parameters
		----------
		chat_request : ChatRequest
        The request body, which contains the history of the conversation
        and the prompt to be completed.

		Returns
    -------
    ChatResponse
        The response body, which contains GPT&#x27;s response to the prompt.
    &quot;&quot;&quot;
    # Actual template and build_memory logic are omitted and can be found in the
		# repo linked below
    prompt = PromptTemplate.from_template(CHAT_TEMPLATE)
    memory = build_memory(chat_request.history)

    chain = LLMChain(
        prompt=prompt,
        llm=OpenAI(),
        memory=memory,
    )
    return ChatResponse(response=chain.run(chat_request.prompt))
`

To use OpaquePrompts, once we retrieve an API token from the OpaquePrompts website, all we have to do is wrap the `llm` passed into `LLMChain` with `OpaquePrompts`:

`chain = LLMChain(
	prompt=prompt,
	# llm=OpenAI(),
	llm=OpaquePrompts(base_llm=OpenAI()),
	memory=memory,
)
`

You can play with a working implementation of a chatbot built with LangChain and OpaquePrompts on the [OpaquePrompts website](https://opaqueprompts.opaque.co/?ref=blog.langchain.com), and find the full source code from which we derived the example above on [GitHub](https://github.com/opaque-systems/opaqueprompts-chat-server?ref=blog.langchain.com). Note that the source code also includes logic for authentication and for displaying intermediate (i.e., the sanitized prompt and sanitized response) steps.

# Conclusion

With OpaquePrompts, you can bootstrap your existing LangChain-based application to add privacy for your users. With your OpaquePrompts + LangChain application, any personal information in your users’ prompts will be hidden from the LLM provider, ensuring that you, as the LLM application developer, do not have to worry about the provider’s data retention or processing policies. Take a look at the [documentation](https://python.langchain.com/docs/integrations/llms/opaqueprompts?ref=blog.langchain.com) or [try out OpaquePrompts Chat](https://opaqueprompts.opaque.co/?ref=blog.langchain.com) today!

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