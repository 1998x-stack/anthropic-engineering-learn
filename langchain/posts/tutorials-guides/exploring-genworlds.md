---
title: "Yeager.ai x LangChain: Exploring GenWorlds a Framework for Coordinating AI Agents"
author: "LangChain Accounts"
date: "2023-08-04"
url: "https://www.langchain.com/blog/exploring-genworlds"
---

Agent ArchitecturePartner

# Yeager.ai x LangChain: Exploring GenWorlds a Framework for Coordinating AI Agents

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamAugust 4, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)11min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1dca83bd2fbf5709207_5-social--16.png)***Editor&#x27;s Note: This is another edition of our series of guest posts highlighting the powerful applications of LangChain. We have been working with the ***[***Yeager.ai***](https://www.yeager.ai/?ref=blog.langchain.com)*** team for several months now, and they have built some really impressive applications of LangChain agents. We&#x27;re excited to highlight this guest blog on their GenWorlds framework for multi-agent systems.  We are especially excited to see their plan for making it seamless for the LangChain/GenWorlds community to monetize their projects.***

🧬🌍GenWorlds is an open-source development [framework](https://github.com/yeagerai/genworlds/tree/main?ref=blog.langchain.com) for multi-agent systems. Core to the framework are dedicated environments or &quot;[Worlds](https://genworlds.com/docs/genworlds-framework/worlds?ref=blog.langchain.com)&quot; with specialized AI [Agents ](https://genworlds.com/docs/genworlds-framework/agents/?ref=blog.langchain.com)and shared [Objects](https://genworlds.com/docs/genworlds-framework/objects?ref=blog.langchain.com). In these Worlds, Agents use shared Objects to coordinate to execute complex tasks and achieve common goals.

Our research has shown that Agents perform better with narrow focus, so Agent coordination is essential for GenAI systems to perform complex operations.

## Developers Can Easily Monetize

Yeager.ai is building a robust ecosystem for GenAI applications. The framework is designed with composability and interoperability in mind. In addition to the framework, GenWorlds will offer a platform for hosting GenAI applications with minimal maintenance and a marketplace where developers can easily monetize their builds.

## The Power of Modularity

Modularity is a cornerstone of the GenWorlds [framework](https://github.com/yeagerai/genworlds/tree/main?ref=blog.langchain.com). In software engineering, breaking things down into smaller self-contained components can improve reusability and reliability of systems. The same is true for systems using LLMs - the more specific and narrow each call to the language model, the higher the reliability of the output. The GenWorlds [framework](https://github.com/yeagerai/genworlds/tree/main?ref=blog.langchain.com) applies this principle at multiple levels:

- Instead of a single agent trying to do everything, GenWorlds allows you to create multiple agents, each with a much narrower mission, that can work together towards a common goal
- Furthermore, each Agent&#x27;s thought process is broken down into multiple Brains appropriate for the task at hand. Each brain needs only a fraction of the total context of the Agent and can therefore perform better
- Developers can configure each Brain to use advanced techniques such as &#x27;chain-of-thought&#x27;, &#x27;self-evaluation&#x27;, and &#x27;tree-of-thought&#x27;. The framework is built with the flexibility to accommodate any new technique that comes out.

The end result is focused and highly reliable Agents that fully harness the power of the underlying language models to achieve complex goals.

With this context set, now let’s dive into the 🧬🌍 GenWorlds [framework](https://github.com/yeagerai/genworlds/tree/main?ref=blog.langchain.com).

## World

The &#x27;[Worlds](https://genworlds.com/docs/genworlds-framework/world?ref=blog.langchain.com)&#x27; is the setting for all the action. It keeps track of all the Agents, Objects, and World properties such as Agent inventories. The World ensures every Agent is informed about the World state, entities nearby, and the events that are available to them to interact with the World.

### World Definition YAML

For convenience, the [RoundTable](https://github.com/yeagerai/genworlds/tree/0e2f5295a0bd74b229170dd28cb4f1d185feb5cb/use_cases/roundtable?ref=blog.langchain.com) example (a multi-agent podcast simulation, more on this below) comes with a loader which reads a world configuration from a YAML file. This allows everyone to quickly create and modify various worlds. Here is an example:

`world_definition:
  base_args:
    websocket_url: ws://localhost:7456/ws
  world:
    id: world
    class: genworlds.worlds.world_2d.world_2d.World2D
    name: All-In Podcast
    description: The four &quot;besties&quot; discuss any topic you want.
    locations:
    - roundtable
    objects:
    - id: mic1
      ...
    agents:
    - id: jason_calacanis
...`

## Simulation Socket

The “[Simulation Socket](https://github.com/yeagerai/genworlds/tree/0e2f5295a0bd74b229170dd28cb4f1d185feb5cb/genworlds/simulation?ref=blog.langchain.com)” is a websocket server which serves as the communication backbone. It enables parallel operation of the World, Agents, and Objects, and allows them to communicate by sending events. This architecture supports connecting frontends or other services to the World, running Agents on external servers, and much more.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1dca83bd2fbf57091fb_0z95rrt-_wdhojhiqxdjyq8sdlzotjgsjalubdwjbvr281sqjpmuumfttirf3te634ty97nrmacpsq7b5hfcfk387kz_bbkqrygifh60nvecma3gdxtu13movvkjnenit2imna1hhquhefdqqh3lpqi.png)

## Agents

[Agents](https://genworlds.com/docs/genworlds-framework/agents/?ref=blog.langchain.com) in GenWorlds are autonomous entities built on top of LangChain that perceive their surroundings and make decisions to achieve specific goals as set by the user. The Agents interact with their environment by sending events through the Simulation Socket server. They dynamically learn about the World and the Objects around them, figuring out how to utilize these Objects to achieve their goals.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1dca83bd2fbf57091fe_shmbxzbvgrqdp7sv5vr41zva626v6spnlkdv34m4uaya2uy0uisrpsdmvlzokzmkmro_bokzj5mhp-dnjacgawhfnftjt-522zmhvqizlxncxivtnsxpxbwuk_gv1xxyqgx9tedg2vznu4adny4hkro.png)

There can be many different types of Agents, as long as each one of them understands the event protocol used to communicate with the World.

## The Agent’s Mental Model

Agents follow a specific [mental mode](https://genworlds.com/docs/genworlds-framework/agents/?ref=blog.langchain.com#agent-mental-model)l at each step of their interaction with the World:

- **Review World state: **The Agent assesses the environment to understand the context before planning any actions.
- **Review new events:** The Agent evaluates any new occurrences in the World. These could be actions taken by other Agents or changes in the World state due to Object interactions.
- **Remember: **Using its stored [memories](https://genworlds.com/docs/genworlds-framework/agents/?ref=blog.langchain.com#custom-memories) and awareness of previous state changes, the Agent recalls past experiences and data that might affect its current decision-making process.
- **Create a plan:** The Agent creates and updates action plans based on World state changes. An Agent can execute multiple actions in one step, improving overall efficiency.
- **Execution: ** Agent implements its plan, influencing the World state and potentially triggering responses from other Agents.

This interactive process fosters the emergence of complex, autonomous behavior, making each Agent an active participant in the World.

## The Thinking Process

The think() method in the code is the central function where an Agent’s [thinking process](https://genworlds.com/docs/genworlds-framework/agents/thought_actions?ref=blog.langchain.com) is carried out. The function first acquires the initial state of the World and potential actions to be performed. It then enters a loop, where it processes events and evaluates entities in the Agent&#x27;s proximity to inform its decision-making.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1dca83bd2fbf5709204_irc2qajibtnybflwxxj5kx1egkifnjky6srvzsouqhcp4r7i950eylvl5pbcqgqlxs1gfunzszqj-vixzl-ftqcjxogr_qihpzxeed4-u1_zqso2mx8znsmcvang2pv-xb-9zoozata6hz1034ersfe.png)

Depending on the current state and goals of the Agent, the think() function may choose to wait, respond to user input, or interact with entities. If the Agent selects an action, it executes it and updates its memory accordingly. The think() function continually updates the Agent&#x27;s state in the World and repeats the process until it decides to exit.  See diagram below showing the Agent Loop in [RoundTable](https://genworlds.com/docs/example-usecases/roundtable?ref=blog.langchain.com), our podcast simulation application:

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1dca83bd2fbf570920c_ubqssevnp1miacowgfsmv4cozrwqlw08q78inbmrianucww_5-i5a6yxazcjwsoey4omkvtp568-ulscpgcoakijakwqgwngexedc0qyvvwxwsbnt1tm4y_ut0iftbech9ukuxg1_usc8k1y9n7epns.png)

## Components of an Agent

[**Brains**](https://genworlds.com/docs/genworlds-framework/agents/thought_actions/?ref=blog.langchain.com)**: **A Brain is a system that controls one step of an Agent&#x27;s thinking process. It manages the process of thought generation, evaluation, and selection. The Brain defines the functions necessary for these processes and uses a Large Language Model to generate and evaluate thoughts.** **All Brains take full advantage of OpenAI Functions to allow easy specification of the desired output format.

Most Agents have the following Brain types:

[**Navigation**](https://github.com/yeagerai/genworlds/blob/0e2f5295a0bd74b229170dd28cb4f1d185feb5cb/use_cases/roundtable/thoughts/navigation_thought.py?ref=blog.langchain.com#L9)** Brain: **The Navigation Brain is designed for selecting the next action of the agent which helps it achieve its goals. It generates a plan for the Agent&#x27;s next steps in the World. The inputs to this class include the Agent&#x27;s information (name, role, background, personality), goals, constraints, evaluation principles, and the number of thoughts to generate.  It generates a set of possible plans, each consisting of an action to take, whether the action is valid, any violated constraints, and an updated plan. The NavigationBrain then evaluates these plans and selects the one that best meets the evaluation principles and constraints.

Sometimes you want to constrain the sequence of actions and force the Agent to follow a certain action with another one - this can be done using the [Action-Brain map](https://genworlds.com/docs/genworlds-framework/agents/think?ref=blog.langchain.com#the-action-brain-map).

Here you can see the constructor of a NavigationBrain:

`NavigationBrain(
    openai_api_key=openai_api_key,
    name=name,
    role=role,
    background=background,
    personality=personality,
    topic_of_conversation=topic_of_conversation,
    constraints=constraints,
    evaluation_principles=evaluation_principles,
    n_of_thoughts=3,
),`

The n_of_thoughts=3 parameter specifies that the Brain will generate 3 possible next actions and pick the best one according to its evaluation_principles.

**Execution Brains:** [Execution Brains](https://genworlds.com/docs/genworlds-framework/agents/think?ref=blog.langchain.com#execution-brains) enable the execution of diverse tasks by Agents. These Brains accept Agent details, task attributes, constraints, and evaluation parameters. These brains can be configured to generate their output in a single call, or generate multiple potential outputs and select the best one using self-evaluation techniques.

The power of Execution Brains lies in their customizability. Developers can create Brains adapted for various tasks such as participating in a podcast, writing an essay, analyzing data, or scraping social media feeds. This flexibility allows the creation of uniquely skilled Agents capable of performing a wide array of tasks in their simulated environments.

The following is a constructor of an example execution brain - the PodcastBrain:

`PodcastBrain(
    openai_api_key=openai_api_key,
    name=name,
    role=role,
    background=background,
    personality=personality,
    communication_style=communication_style,
    topic_of_conversation=topic_of_conversation,
    constraints=constraints,
    evaluation_principles=evaluation_principles,
    n_of_thoughts=1,
),`

Here, the n_of_thoughts is set to 1, meaning the Podcast Brain will generate only one output message and skip the evaluation step.

**Event Filler Brain: **The [Event Filler ](https://github.com/yeagerai/genworlds/blob/0e2f5295a0bd74b229170dd28cb4f1d185feb5cb/use_cases/roundtable/thoughts/event_filler_thought.py?ref=blog.langchain.com#L9)Brain is used for generating the JSON parameters required for an action the Agent executes in a World. The inputs are similar to the Navigation Brain but also include the command the Agent has decided to execute, as well as the outputs of any previous brains in the execution flow.
You can see it takes fewer parameters than the other Brains, because it doesn&#x27;t need as much context to complete its task.

`EventFillerBrain(
    openai_api_key=openai_api_key,
    name=name,
    role=role,
    background=background,
    topic_of_conversation=topic_of_conversation,
    constraints=constraints,
    evaluation_principles=evaluation_principles,
    n_of_thoughts=1,
),
`

Different types of Brains can be created to handle different tasks, scenarios, or problems. An Agent can have multiple Brains each focused on a specific goal with its context tailored to that goal.  For instance, a podcaster Agent would have a “Content Brain” which would be its only Brain that possesses information about the Agent’s communication-style.

Using multiple Brains helps narrow the Agent’s focus and thus significantly enhances the quality and reliability of an Agent&#x27;s output.  Additionally, each Brain can use a different LLM, which allows you to further optimize the system.  For instance certain actions or decisions require more powerful LLMs (e.g. GPT-4) while other steps can be done with more simple, faster, and cheaper LLMs (e.g. GPT-3.5).

**Action-Brain Map: **The [Action-Brain Map](https://genworlds.com/docs/genworlds-framework/agents/think?ref=blog.langchain.com#the-action-brain-map) of an Agent defines a deterministic path through the various Brains. It&#x27;s the system that decides which Brain to use based on the Agent&#x27;s next action. The output of each brain is passed on to the consecutive brain in the execution brain path of that action. From our Podcaster Agent example above, it will engage the Content Brain when the Agent is about to speak, and pass the output to the Event Filler Brain to generate a valid World event with the generated response.

You can furthermore specify a deterministic follow-up for each action if you don&#x27;t want the agent to choose freely - for example, after speaking into the microphone, the Agent must pass it to someone else. This allows you to constrain the Agent to create more predictable execution paths and increase reliability.

Here&#x27;s what that looks like in code:

`action_brain_map = {
    &quot;Microphone:agent_speaks_into_microphone&quot;: {&quot;brains&quot;:[
        &quot;podcast_brain&quot;,
        &quot;event_filler_brain&quot;,
    ], &quot;next_actions&quot;: [&quot;World:agent_gives_object_to_agent_event&quot;]},
    &quot;World:agent_gives_object_to_agent_event&quot;:        {&quot;brains&quot;:[&quot;event_filler_brain&quot;], &quot;next_actions&quot;: []},
    &quot;default&quot;: {&quot;brains&quot;:[&quot;event_filler_brain&quot;], &quot;next_actions&quot;: []},
}`

**Agent Inventory**: The specific [Objects](https://genworlds.com/docs/genworlds-framework/objects?ref=blog.langchain.com) that an Agent currently holds. This state is maintained by the world, and allows Agents to pass items such as Tokens from one to another, and keep Objects with them as they move to different locations in the [World](https://genworlds.com/docs/genworlds-framework/world?ref=blog.langchain.com#world2d).

## Memories: Current and Pregenerated

Agents in GenWorlds have two types of [memories](https://genworlds.com/docs/genworlds-framework/agents/?ref=blog.langchain.com#baseagent), current and pregenerated memories:

- Current Memories:  Agents remember [number] of the most recent events, [number] of the most relevant events, and a running summary of the whole history.  The number of recent and relevant memories is configurable by the user.
- Pregenerated Memories: Generated from external content (e.g. youtube videos, books, etc.) and stored in vector dbs.   Pre-generated memories are injected in Agents’ prompts based on their relevance to the Agent&#x27;s current goals, allowing for more focused and reliable interactions.  These memories allow Agents to learn without fine-tuning the underlying model.

*Below is how you can easily configure custom pregenerated memories in a World definition YAML file, which are stored in a *[*Qdrant *](http://qdrant.tech/?ref=blog.langchain.com)*vector database:*

*To use the memories, you need to set the following values in the world_definition.yaml file *

`world_definition:
  world:
    path_to_to_external_memory: ./databases/summaries_qdrant`

*	For each Agent you need to specify the collection name*

`agents:
-  id: maria
   personality_db_collection_name: maria`

## Objects

[Objects](https://genworlds.com/docs/genworlds-framework/objects?ref=blog.langchain.com) play a crucial role in facilitating interaction between Agents. Every Object defines a unique set of events, enabling Agents to accomplish specific tasks and work together in a dynamic environment. Objects can be in an Agent&#x27;s vicinity or can be part of their inventory, expanding the scope of possible interactions.

Agents are designed to adapt dynamically, learning about nearby Objects, understanding the event definitions, and determining the best way to interact with them to achieve their goals.  Objects are the main way to give Agents new capabilities and organize them in a structure to achieve a collective broader goal.

## Agent Coordination

Since Agents are aware of the events in the World including those of the other Agents, Agents naturally react to each other.  In order to facilitate structure and organized behavior between the Agents we use shared Objects.  See three examples below:

**“Token Bearer”:** Agents use a Token in their inventory to communicate and to signal to the other Agents whose turn it is to perform an action. For example, in RoundTable (our podcast simulation app), Agents use a [microphone](https://github.com/yeagerai/genworlds/blob/0e2f5295a0bd74b229170dd28cb4f1d185feb5cb/use_cases/roundtable/objects/microphone.py?ref=blog.langchain.com#L8) as a token to speak to each other. Agents can only speak if they have the mic in their inventory. This ensures the Agents listen to each other and prevents them from interrupting each other, thus creating a dynamic discussion.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1dca83bd2fbf5709201_lpfzzy8ing1ibx2zhimg2r1aj08ajavcqiyzzuosfi_1g9ss7l0ndksdforkiomnjytdujbkl9mt8ebxy0o3bwhu9_ndp_-l2iawc7ze8ovreqq1dtxxjxl0azeyx3j6iff5jrbk_djba7qxgtldgra.png)

*This is how it looks in the code *

`world_definition:
  world:
    path_to_to_external_memory: ./databases/summaries_qdrant`

**Pipeline:** Each Agent is assigned a role in the pipeline and completes their role when it’s their turn. It’s like a factory line. For example, most sales processes go something like this:

Research &gt; obtain contact info &gt; create/send a compelling outreach message &gt; follow up &gt; schedule/conduct a call &gt; review call notes &gt; send/negotiate legal docs &gt; follow-ups/calls &gt; and on and on until the deal is won/lost.

To facilitate this sort of an operation, you would create a set of Objects such as boxes, where each agent can put their work output, and the next Agent in the pipeline can look to see when a new item has been passed to them, pick it up, process it according to the step of the pipeline they&#x27;re in, and put in in the next box.

Pipeline is best for sequential tasks like in the sales example.

**Project Management:** A project manager (human or Agent) uses a Blackboard, an Object for assigning roles to each Agent and keeping track of progress. The Project Manager and the Agents interact via the Blackboard, sharing files, updating assignments, tracking progress, etc.

**Tools:** Agents can use Tools to execute specific functions such as calling external APIs, running complex calculations, or triggering unique events in the World.

The framework provides the flexibility for anyone to create their own Objects and coordination methods.

## Use Case Highlight - RoundTable

In order to showcase the coordination capabilities of Agents in GenWorlds, we built [RoundTable](https://genworlds.com/docs/example-usecases/roundtable?ref=blog.langchain.com), a podcast simulation. Users can summon the brightest minds for a group discussion on any topic. It&#x27;s not another ChatGPT wrapper; it’s a team of AI Agents acting independently with specific personalities, memories, and expertise.

RoundTable uses Objects, Agent inventories, and pre-generated memories to create dynamic discussions between Agents who sound like the people they are emulating. See a demo here:

You can also try it for free on Replit

- Go to [Replit](https://replit.com/@yeagerai/GenWorlds?ref=blog.langchain.com)
- Fork the Replit (it’s completely free)
- Select which use case you want to use

## The GenAI Ecosystem - Our Northstar

We designed the GenWorlds framework with modularity, flexibility, and composability.  We envision GenAI developers using this modularity to plug and play or build each element of the framework (Worlds, Agents, Objects, Memories, Brains, etc.) to create their own useful applications.

We are not stopping there.  We are giving our developer community a [platform](https://genworlds.com/docs/platform/genworlds-marketplace?ref=blog.langchain.com) and the [tools](https://genworlds.com/docs/genworlds-framework/objects?ref=blog.langchain.com) for easy access to monetizing their applications in a Gen-AI marketplace.

## Learn More About 🧬🌍GenWorlds

Demo: [https://youtu.be/INsNTN4S680](https://youtu.be/INsNTN4S680?ref=blog.langchain.com)

GitHub: [https://github.com/yeagerai/genworlds](https://github.com/yeagerai/genworlds?ref=blog.langchain.com)

Docs: [https://genworlds.com/docs/intro](https://genworlds.com/docs/intro?ref=blog.langchain.com)

Discord: [https://discord.gg/wKds24jdAX](https://discord.gg/wKds24jdAX?ref=blog.langchain.com)

Blog: [https://medium.com/yeagerai](https://medium.com/yeagerai?ref=blog.langchain.com)

Replit: [https://replit.com/@yeagerai/GenWorlds](https://replit.com/@yeagerai/GenWorlds?ref=blog.langchain.com)

## About Yeager

At Yeager.ai, we are on a mission to enhance the quality of life through the power of Generative AI. Our goal is to eliminate the burdensome aspects of work by making GenAI reliable and easily accessible. By doing so, we foster a conducive environment for learning, innovation, and decision-making, propelling technological advancement.

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc07193192cebc73980fd3_logo%20and%20title%20-%2020%20characters%20max%20(6).png)PartnerDeep Agents

#### Building a company due diligence agent with Deep Agents, LangSmith and Parallel

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01c6959ca5fd924ab432_MattHarris.jpg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01b812793b72539057d5_nick%20headshot.jpeg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd2d50cd0f84dacf92e7b_ProfilePic.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd29baf4c28709e2566a7_headshot.jpg)Matt HarrisNick MartitschSrimanth TangedipalliKaran SinghMay 8, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)9min[](/blog/building-a-company-due-diligence-agent-with-deep-agents-langsmith-and-parallel)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69f20536df00c0eb15eab1d3_blue-77%20characters%20max.png)Deep AgentsAgent ArchitectureOpen Source

#### Tuning Deep Agents to Work Well with Different Models

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcefac505b6b48827abf84_vivek-trivedy.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcf032ce65a32e276a4d0a_mason-daugherty.png)Vivek TrivedyMason DaughertyApril 29, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)5min[](/blog/tuning-deep-agents-different-models)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef96ff74c638e982ff68c6_86%20(1).png)Agent ArchitectureLangSmithOpen Source

#### How LangSmith and LangChain OSS Help You Meet EU AI Act Requirements

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0003a1af368dfae13c23c_jacob-talbot.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Jacob TalbotBecca WengApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/langsmith-langchain-oss-eu-ai-act)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)