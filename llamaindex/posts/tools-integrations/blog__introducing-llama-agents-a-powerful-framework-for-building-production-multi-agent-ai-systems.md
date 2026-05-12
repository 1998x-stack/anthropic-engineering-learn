---
title: "Llama-Agents Framework: Production Multi-Agent Guide | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/introducing-llama-agents-a-powerful-framework-for-building-production-multi-agent-ai-systems"
category: "tools-integrations"
---

Content



- [ Key Features of llama-agents  ](#key-features-of-llama-agents)
- [ Getting Started with llama-agents  ](#getting-started-with-llama-agents)
- [ Basic System Setup  ](#basic-system-setup)
- [ Deploying Your Multi-Agent System  ](#deploying-your-multi-agent-system)
- [ Real-time monitoring  ](#real-time-monitoring)
- [ Building a Query Rewriting RAG System  ](#building-a-query-rewriting-rag-system)
- [ Public roadmap  ](#public-roadmap)
- [ Dive in!  ](#dive-in)



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



   11



 We&#39;re excited to announce the alpha release of `llama-agents` , a new open-source framework designed to simplify the process of building, iterating, and deploying multi-agent AI systems and turn your agents into production microservices. Whether you&#39;re working on complex question-answering systems, collaborative AI assistants, or distributed AI workflows, llama-agents provides the tools and structure you need to bring your ideas to life.



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



##  Key Features of llama-agents


-  **Distributed Service Oriented Architecture:** every agent in LlamaIndex can be its own independently running microservice, orchestrated by a fully customizable LLM-powered control plane that routes and distributes tasks.
  -  **Communication via standardized API interfaces:** interface between agents using a central control plane orchestrator. Pass messages between agents using a message queue.
  -  **Define agentic and explicit orchestration flows:** developers have the flexibility to directly define the sequence of interactions between agents, or leave it up to an “agentic orchestrator” that decides which agents are relevant to the task.
  -  **Ease of deployment:** launch, scale and monitor each agent and your control plane independently.
  -  **Scalability and resource management:** use our built-in observability tools to monitor the quality and performance of the system and each individual agent service



 Let&#39;s dive into how you can start using llama-agents to build your own multi-agent systems.



##  Getting Started with llama-agents



 First, install the framework using pip:



sh






```
pip install llama-agents llama-index-agent-openai
```


###  Basic System Setup

  Here&#39;s a simple example of how to set up a basic multi-agent system using llama-agents. First we’ll bring in our dependencies and set up our control plane, which contains our LLM-powered orchestrator



python






```
import dotenv
dotenv.load_dotenv() # our .env file defines OPENAI_API_KEY
from llama_agents import (
    AgentService,
    ControlPlaneServer,
    SimpleMessageQueue,
    AgentOrchestrator,
)
from llama_index.core.agent import FunctionCallingAgentWorker
from llama_index.core.tools import FunctionTool
from llama_index.llms.openai import OpenAI
import logging

# turn on logging so we can see the system working
logging.getLogger("llama_agents").setLevel(logging.INFO)

# Set up the message queue and control plane
message_queue = SimpleMessageQueue()
control_plane = ControlPlaneServer(
    message_queue=message_queue,
    orchestrator=AgentOrchestrator(llm=OpenAI()),
)
```
    Next we create our tools using LlamaIndex’s existing abstractions, provide those tools to an agent, and turn that agent into an independent microservice:



python






```
# create a tool
def get_the_secret_fact() -> str:
    """Returns the secret fact."""
    return "The secret fact is: A baby llama is called a 'Cria'."

tool = FunctionTool.from_defaults(fn=get_the_secret_fact)

# Define an agent
worker = FunctionCallingAgentWorker.from_tools([tool], llm=OpenAI())
agent = worker.as_agent()

# Create an agent service
agent_service = AgentService(
    agent=agent,
    message_queue=message_queue,
    description="General purpose assistant",
    service_name="assistant",
)
```
    Finally we launch the service and the control plane. Note that here we’re using a helper function to run a single query through the system and then exit; next we’ll show how to deploy this to production.



python






```
# Set up the launcher for local testing
from llama_agents import LocalLauncher

launcher = LocalLauncher(
    [agent_service],
    control_plane,
    message_queue,
)

# Run a single query through the system
result = launcher.launch_single("What's the secret fact?")
print(result)
```


##  Deploying Your Multi-Agent System

  Once you&#39;ve tested your system locally, you can deploy it as a set of services for real production use. Here&#39;s how you might set that up. This is similar to the previous example, but we’ve added a second agent service and we’re using a different launcher. Let’s bring in our dependencies and set up our control plane again:



python






```
import dotenv
dotenv.load_dotenv()
from llama_agents import (
    AgentService,
    AgentOrchestrator,
    ControlPlaneServer,
    SimpleMessageQueue,
)

from llama_index.core.agent import FunctionCallingAgentWorker
from llama_index.core.tools import FunctionTool
from llama_index.llms.openai import OpenAI
import logging

# change logging level to enable or disable more verbose logging
logging.getLogger("llama_agents").setLevel(logging.INFO)

# create our multi-agent framework components
message_queue = SimpleMessageQueue()
control_plane = ControlPlaneServer(
    message_queue=message_queue,
    orchestrator=AgentOrchestrator(llm=OpenAI()),
)
```
    Then as before we create a tool and an agent, though this time we’ll add a second agent:



python






```
# create a tool
def get_the_secret_fact() -> str:
    """Returns the secret fact."""
    return "The secret fact is: A baby llama is called a 'Cria'."

tool = FunctionTool.from_defaults(fn=get_the_secret_fact)

# create our agents
worker1 = FunctionCallingAgentWorker.from_tools([tool], llm=OpenAI())
worker2 = FunctionCallingAgentWorker.from_tools([], llm=OpenAI())
agent1 = worker1.as_agent()
agent2 = worker2.as_agent()
```
    We turn those agents into services:



python






```
agent_server_1 = AgentService(
    agent=agent1,
    message_queue=message_queue,
    description="Useful for getting the secret fact.",
    service_name="secret_fact_agent",
    host="localhost",
    port=8003
)
agent_server_2 = AgentService(
    agent=agent2,
    message_queue=message_queue,
    description="Useful for getting random dumb facts.",
    service_name="dumb_fact_agent",
    host="localhost",
    port=8004
)
```
    And finally we launch each service as an independent agent. Here we’re doing them all from a single script, but each of these could be a totally separate service, launched and scaled independently:



python






```
from llama_agents import ServerLauncher, CallableMessageConsumer

# Additional human consumer
def handle_result(message) -> None:
    print(f"Got result:", message.data)

# the final result is published to a "human" consumer
# so we define one to handle it!
human_consumer = CallableMessageConsumer(
    handler=handle_result, message_type="human"
)

# Define Launcher
launcher = ServerLauncher(
    [agent_server_1, agent_server_2],
    control_plane,
    message_queue,
    additional_consumers=[human_consumer]
)

launcher.launch_servers()
```


##  Real-time monitoring

  One of the coolest debugging features of our multi-agent system is our agent monitor, which is built right in. You launch it like this:



sh






```
llama-agents monitor --control-plane-url http://127.0.0.1:8000
```
    Once launched, you get an intuitive, point-and-click terminal application. You can see both of the agents running, and at the bottom you can inject a task like the query “What is the secret fact?” You’ll get a job ID which you can then click on to see your results:

  ![](https://cdn.sanity.io/images/7m9jw85w/production/077894fcf1dc8b2cd0ee5999ed58e252479783c4-1098x615.png)

##  Building a Query Rewriting RAG System



 Let&#39;s look at a more complex example: a Query Rewriting RAG system. This system will rewrite user queries to improve retrieval, then use the rewritten query to perform RAG over a document.



 This example demonstrates how to create a more sophisticated system that combines query rewriting with RAG to improve question-answering capabilities. See [this notebook](https://github.com/run-llama/llama-agents/blob/main/examples/query_rewrite_rag.ipynb) for a fuller explanation of what’s going on.



python






```
import dotenv
dotenv.load_dotenv() # our .env defines OPENAI_API_KEY
from llama_index.core import VectorStoreIndex, Document
from llama_index.core.agent import FnAgentWorker
from llama_index.core import PromptTemplate
from llama_index.core.query_pipeline import QueryPipeline
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_agents import (
    AgentService,
    ControlPlaneServer,
    SimpleMessageQueue,
    PipelineOrchestrator,
    ServiceComponent,
)
from llama_agents.launchers import LocalLauncher
from llama_index.llms.openai import OpenAI
import logging

# change logging level to enable or disable more verbose logging
logging.getLogger("llama_agents").setLevel(logging.INFO)

# Load and index your document
docs = [Document(text="The rabbit is a small mammal with long ears and a fluffy tail. His name is Peter.")]
index = VectorStoreIndex.from_documents(docs)

# Define a query rewrite agent
HYDE_PROMPT_STR = (
    "Please rewrite the following query to include more detail:\n{query_str}\n"
)
HYDE_PROMPT_TMPL = PromptTemplate(HYDE_PROMPT_STR)

def run_hyde_fn(state):
    prompt_tmpl, llm, input_str = (
        state["prompt_tmpl"],
        state["llm"],
        state["__task__"].input,
    )
    qp = QueryPipeline(chain=[prompt_tmpl, llm])
    output = qp.run(query_str=input_str)
    state["__output__"] = str(output)
    return state, True

hyde_agent = FnAgentWorker(
    fn=run_hyde_fn,
    initial_state={"prompt_tmpl": HYDE_PROMPT_TMPL, "llm": OpenAI()}
).as_agent()

# Define a RAG agent
def run_rag_fn(state):
    retriever, llm, input_str = (
        state["retriever"],
        state["llm"],
        state["__task__"].input,
    )
    query_engine = RetrieverQueryEngine.from_args(retriever, llm=llm)
    response = query_engine.query(input_str)
    state["__output__"] = str(response)
    return state, True

rag_agent = FnAgentWorker(
    fn=run_rag_fn,
    initial_state={"retriever": index.as_retriever(), "llm": OpenAI()}
).as_agent()

# Set up the multi-agent system
message_queue = SimpleMessageQueue()

query_rewrite_service = AgentService(
    agent=hyde_agent,
    message_queue=message_queue,
    description="Query rewriting service",
    service_name="query_rewrite",
)

rag_service = AgentService(
    agent=rag_agent,
    message_queue=message_queue,
    description="RAG service",
    service_name="rag",
)

# Create the pipeline
pipeline = QueryPipeline(chain=[
    ServiceComponent.from_service_definition(query_rewrite_service),
    ServiceComponent.from_service_definition(rag_service),
])
orchestrator = PipelineOrchestrator(pipeline)

control_plane = ControlPlaneServer(
    message_queue=message_queue,
    orchestrator=orchestrator,
)

# Set up the launcher
launcher = LocalLauncher(
    [query_rewrite_service, rag_service],
    control_plane,
    message_queue,
)

# Run a query
result = launcher.launch_single("Tell me about rabbits")
print(result)
```


##  Public roadmap

  This is an alpha release, meaning that we’d love your feedback on features to better help you build multi-agent systems in production! We’ve created a [public roadmap](https://github.com/run-llama/llama-agents/discussions/49) showing where we plan to go from here. We’re actively seeking public feedback on what works for you and what doesn’t.



##  Dive in!



 `llama-agents`  provides a powerful, flexible framework for building complex multi-agent AI systems. Whether you&#39;re prototyping a new idea or scaling to production, `llama-agents`  offers the tools you need to bring your AI vision to life. Check out [the repo](https://github.com/run-llama/llama-agents) to learn more, especially our library of [examples](https://github.com/run-llama/llama-agents/tree/main/examples).



 We&#39;re excited to see what the community builds with `llama-agents` . Happy coding!