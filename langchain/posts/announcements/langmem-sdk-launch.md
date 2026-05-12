---
title: "LangMem SDK for agent long-term memory"
author: "LangChain Accounts"
date: "2025-02-18"
url: "https://www.langchain.com/blog/langmem-sdk-launch"
---

Observability &amp; Evals

# LangMem SDK for agent long-term memory

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamFebruary 18, 2025![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)6min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbadeef72d73b2dc00d80c_langmem_launch-2.png)Today we&#x27;re releasing the LangMem SDK, a library that helps your agents learn and improve through long-term memory.

It provides tooling to extract information from conversations, optimize agent behavior through prompt updates, and maintain long-term memory about behaviors, facts, and events.

You can use its core API with any storage system and within any Agent framework, and it integrates natively with LangGraph&#x27;s long-term memory layer. We are also launching a managed service that provides additional long-term memory results for free - sign up [here](https://forms.gle/KY8ja6F24nJFRF2e9?ref=blog.langchain.com) if you are interested in using it in production.

Our goal is to make it easier for **anyone** to build AI experiences that become smarter and more personalized over time. This work builds on our previous work of the hosted LangMem [alpha service](https://blog.langchain.com/langfriend/) and LangGraph&#x27;s persistent [long-term memory layer](https://blog.langchain.com/launching-long-term-memory-support-in-langgraph/).

To install, just run:

`pip install -U langmem`

## Quick links

- Documentation: [[link](https://langchain-ai.github.io/langmem/?ref=blog.langchain.com)]
- Managed Service Signup: [[link](https://forms.gle/KY8ja6F24nJFRF2e9?ref=blog.langchain.com)]
- Video Tutorials:
Concepts: [[link](https://youtu.be/snZI5ojuMRc?ref=blog.langchain.com)]
- Semantic Memory in LangMem: [[link](https://youtu.be/3Yp-hIEcWXk?ref=blog.langchain.com)]
- Procedural Memory in LangMem: [[link](https://youtu.be/WW-v5mO2P7w?ref=blog.langchain.com)]

## On memory and adaptive agents

Agents use memory to learn, but the way their memories are formed, stored, updated, and retrieved impacts types of things your agent can learn to know or do. At LangChain, we’ve found it useful to **first** identify the capabilities your agent needs to be able to learn, map these to specific memory types or approaches, and only then implement them in your agent. Before adding memory, we think you should consider:

- **What behavior should be learned (user-informed) vs. pre-defined?**
- **What types of knowledge or facts should be tracked?**
- **What conditions should trigger a memory to be recalled?**

While there may be some overlap, each memory type serves distinct functions when building adaptive agents:

Memory TypePurposeAgent ExampleHuman ExampleTypical Storage PatternSemanticFacts &amp; KnowledgeUser preferences; knowledge tripletsKnowing Python is a programming languageProfile or CollectionEpisodicPast ExperiencesFew-shot examples; Summaries of past conversationsRemembering your first day at workCollectionProceduralSystem BehaviorCore personality and response patternsKnowing how to ride a bicyclePrompt rules or Collection

So then revisiting our questions above:

- **What behavior should be learned vs. fixed?** Some aspects of your agent&#x27;s behavior may need to adapt based on feedback and experience, while others should remain consistent. This will guide whether you need **procedural memory **to evolve behavior patterns, or if fixed prompt rules are sufficient. This is similar in spirit to the concept of the &quot;chain of command&quot; in OpenAI&#x27;s model spec  since learned behaviors are shaped by user interactions.
- **What types of knowledge or facts should be tracked?**
Different use cases require different types of knowledge persistence. You might need **semantic memory** to maintain facts about users or domains, **episodic memory** to learn from successful interactions, or both working together.
- **What conditions should trigger a memory to be recalled?**
Some memories (core procedural memory) may be **data-independent** - they are always present in the prompt. Some are **data-dependent** and may be recalled based on semantic similarity. Others may be recalled based on a combination of application context, similarity, time, etc.

A related concern is memory privacy. In LangMem, all memories are given a **namespace**. The most common namespaces would include a use_id in order to prevent cross-over of user memories. In general, memories can be scoped to particular app routes, to individual users, shared across teams, or the agent could learn core procedures across all users. The extent of memory sharing is determined both by privacy and performance needs.

All of these memory types are meant to address recall **beyond individual conversations**. Memory within a given conversation, or thread, is already handled reasonably well using checkpointing in LangGraph (so long as it doesn’t extend beyond the model’s effective context window), which serves as the “short-term” or “working” memory system for your agent.

Note that this also differs from standard RAG in a couple ways. One is the way the information is gained: through interaction rather than offline data ingestion. The other is in the type of information that’s prioritized. Below, we will share more about the memory types in more detail.

### Semantic memory: facts

[Semantic memory](https://langchain-ai.github.io/langgraph/concepts/memory/?ref=blog.langchain.com#semantic-memory) stores key facts (and their relationships) and other information that ground an agent&#x27;s responses. It lets your agent remember important details that wouldn’t be “pre-trained” into the model itself and that isn’t accessible from a web search or generic retriever.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbadeff72d73b2dc00d826_image.png)

Code`
from langmem import create_memory_manager

manager = create_memory_manager(
    &quot;anthropic:claude-3-5-sonnet-latest&quot;,
    instructions=&quot;Extract user preferences and facts&quot;,
    enable_inserts=True
)

# Process conversation to extract facts
conversation = [
    {&quot;role&quot;: &quot;user&quot;, &quot;content&quot;: &quot;Alice manages the ML team and mentors Bob, who is also on the team.&quot;}
]
memories = manager.invoke({&quot;messages&quot;: conversation})

# Extract and store new knowledge
conversation2 = [
    {&quot;role&quot;: &quot;user&quot;, &quot;content&quot;: &quot;Bob now leads the ML team and the NLP project.&quot;}
]
update = manager.invoke({&quot;messages&quot;: conversation2, &quot;existing&quot;: memories})
 `

`memories = [
    ExtractedMemory(
        id=&quot;27e96a9d-8e53-4031-865e-5ec50c1f7ad5&quot;,
        content=Memory(
            content=&quot;Alice manages the ML team and mentors Bob, who is also on the team.&quot;
        ),
    ),
    ExtractedMemory(
        id=&quot;e2f6b646-cdf1-4be1-bb40-0fd91d25d00f&quot;,
        content=Memory(
            content=&quot;Bob now leads the ML team and the NLP project.&quot;
        ),
    ),
]
`

In our experience, semantic memory is the most common form of “memory” that engineers ask for and imagine (after, perhaps, short-term “conversation history” memory) when they first seek to add a memory layer.

It also (debatably) has the most overlap with traditional RAG systems. If the knowledge is available from another store (docs site, codebase, etc.), and if that store is the source of truth (rather than the interactions themselves), then your agent may work fine simply retrieving over that knowledge corpus directly. Or you can periodically ingest that knowledge to integrate that in the semantic memory system. If the knowledge is regarding personalization (about the user) or conceptual relationships not found in the raw materials, then semantic memory is perfect for you.

### Procedural memory: evolving behavior

Procedural memory represents internalized knowledge of **how to** perform tasks. It is distinct from episodic memory in that it focuses on generalized skills, rules, and behaviors. For AI agents, procedural memory is saved across a combination of model weights, agent code, and agent&#x27;s prompt that collectively determine the agent&#x27;s functionality. In LangMem, we focus on saving learned procedures as updated instructions in the agent&#x27;s prompt.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbadeff72d73b2dc00d82b_image-1.png)

Code`
from langmem import create_prompt_optimizer

trajectories = [
    (
        [
            {&quot;role&quot;: &quot;user&quot;, &quot;content&quot;: &quot;Tell me about Mars&quot;},
            {&quot;role&quot;: &quot;assistant&quot;, &quot;content&quot;: &quot;Mars is the fourth planet...&quot;},
            {&quot;role&quot;: &quot;user&quot;, &quot;content&quot;: &quot;I wanted more about its moons&quot;},
        ],
        {&quot;score&quot;: 0.5, &quot;comment&quot;: &quot;Missed key information about moons&quot;}
    )
]

optimizer = create_prompt_optimizer(
    &quot;anthropic:claude-3-5-sonnet-latest&quot;,
    kind=&quot;metaprompt&quot;,
    config={&quot;max_reflection_steps&quot;: 3}
)

improved_prompt = optimizer.invoke({
    &quot;trajectories&quot;: trajectories,
    &quot;prompt&quot;: &quot;You are a planetary science expert&quot;
})

 `

`&quot;&quot;&quot;
You are a helpful assistant..
    If the user asks about astronomy, explain topics clearly using real-world examples and current scientific data.
    Use visual references when helpful and adapt to the user&#x27;s knowledge level.
    Balance practical observational astronomy with theoretical concepts, providing either viewing advice or technical explanations based on user needs.
&quot;&quot;&quot;`

The optimizer is prompted with identifying patterns in successful and unsuccessful interactions, then updating the system prompt to reinforce effective behaviors. This creates a feedback loop where the agent&#x27;s core instructions evolve based on observed performance.

Informed by our [work on prompt optimization](https://blog.langchain.com/exploring-prompt-optimization/), LangMem provides multiple algorithms for generating prompt update proposals, including: `metaprompt` uses reflection &amp; additional “thinking” time to study the conversations and then use a meta-prompt to propose the update; `gradient` explicitly divides the work into separate steps of critique and prompt proposals to further simplify the task at each step; and a simple `prompt_memory` algorithm that attempts to do the above in a single step.

### Episodic memory: events and experiences

Episodic memory stores memories of past interactions. It is distinct from procedural memory in its focus on recalling *specific* experiences. It is distinguished from semantic memory in its focus on past events rather than general knowledge, answering “how” the agent solved a particular problem rather than just “what” the answer was. It often takes the form of few-shot examples, with each example distilled from a longer raw interaction. LangMem doesn&#x27;t yet support opinionated utilities for episodic memory.

### Try it today

Check out the [docs](https://langchain-ai.github.io/langmem/?ref=blog.langchain.com) for more examples on how to implement custom memory systems using LangMem, including guides on how to:

- Create an agent that actively manage its own memory
- Share memories between agents
- Namespace memories to organize information by user or team.
- Integrate LangMem in your custom framework

If your team wants to add personalization or life-long learning to your agents, fill out our [interest form](https://forms.gle/KY8ja6F24nJFRF2e9?ref=blog.langchain.com).

### Join our team

We&#x27;re recruiting engineers to build the world&#x27;s best runtime for adaptive agents. If you&#x27;re interested in designing and building with us, check out our [open positions](https://www.langchain.com/careers?ref=blog.langchain.com).

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e113adb98acef39fe4aa32_Reusable-evaluators.png)Observability &amp; EvalsLangSmith

#### Reusable Evaluators and Evaluator Templates in LangSmith

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0006d57fa417eb9caf388_catherine-qiao.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0003a1af368dfae13c23c_jacob-talbot.png)Catherine QiaoJacob TalbotApril 16, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/reusable-langsmith-evaluator-templates)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dce8a01c18c14b60cd4372_76.webp)LangSmithObservability &amp; Evals

#### Human judgment in the agent improvement loop

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2d3bf32d4fc06a289383_rahul-verma.png)Rahul VermaApril 9, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)11min[](/blog/human-judgment-in-the-agent-improvement-loop)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dce9138b145f1419b6b38b_74--2-.webp)Observability &amp; Evals

#### Better Harness: A Recipe for Harness Hill-Climbing with Evals

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcefac505b6b48827abf84_vivek-trivedy.png)Vivek TrivedyApril 8, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)8min[](/blog/better-harness-a-recipe-for-harness-hill-climbing-with-evals)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)