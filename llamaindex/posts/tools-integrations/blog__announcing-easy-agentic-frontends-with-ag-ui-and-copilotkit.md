---
title: "AG-UI Agentic Frontends: Quick Start Guide | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/announcing-easy-agentic-frontends-with-ag-ui-and-copilotkit"
category: "tools-integrations"
---

Content



- [ Get started today!  ](#get-started-today)



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







 It’s been a big month for CopilotKit’s AG-UI project since [it launched](https://www.copilotkit.ai/blog/introducing-ag-ui-the-protocol-where-agents-meet-users) a little over a month ago! They’ve seen a lot of adoption and are celebrating today with a raft of updates and new features. We’re joining in the celebration by launching the official [LlamaIndex integration to AG-UI](https://github.com/run-llama/llama_index/tree/main/llama-index-integrations/protocols/llama-index-protocols-ag-ui)!







 If you’re just tuning in, AG-UI is a protocol that makes it easy to bring agents out of the backend and into direct interaction with users. The protocol can work with any end-user facing UI – a web app, a desktop application, or any existing chat application. CopilotKit is a first-class client to the protocol, focusing on bringing agents into interaction with users through modern web frontends in React.







 Getting started is easy, just pip install the integration:



sh






```
pip install llama-index-protocols-ag-ui
```
    Then you can create an AG-UI compatible FastAPI router in one line of code! This creates an agent, and provides it with tools that it can use on the frontend or the backend to complete user tasks.



python






```
agentic_chat_router = get_ag_ui_workflow_router(
    llm=OpenAI(model="gpt-4.1"),
    frontend_tools=[change_background],
    backend_tools=[],
    system_prompt="You are a helpful assistant that can change the background color of the chat.",
    initial_state=None,  # Unused in this example
)
```
    (See the [full documentation](https://github.com/run-llama/llama_index/tree/main/llama-index-integrations/protocols/llama-index-protocols-ag-ui) or [starter example](https://github.com/CopilotKit/CopilotKit/tree/main/examples/llamaindex/starter) for how to define these tools.)



 On the frontend, this will allow you to include the CopilotChat React component:



javascript






```
import { CopilotChat } from "@copilotkit/react-ui";
```
    Which can then be instantiated to give you simple access to your agent:



javascript






```
return (
    &#x3C;div className="flex justify-center items-center h-full w-full" style={{ background }}>
      &#x3C;div className="w-8/10 h-8/10 rounded-lg">
        &#x3C;CopilotChat
          className="h-full rounded-2xl"
          labels={{ initial: "Hi, I'm an agent. Want to chat?" }}
        />
      &#x3C;/div>
    &#x3C;/div>
  );
```
    CopilotKit works seamlessly with the AG-UI protocol to route user requests to frontend or backend tools to achieve their goals. A lot of messy boilerplate is abstracted away, letting you focus on your business logic and user experience.



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



##  Get started today!



 We’re delighted to add to AG-UI’s already impressive momentum. If you want to build your own agentic frontend using LlamaIndex and CopilotKit, check out these resources:


-  [Official LlamaIndex integration](https://github.com/run-llama/llama_index/tree/main/llama-index-integrations/protocols/llama-index-protocols-ag-ui)
  -  [LlamaIndex CopilotKit documentation](https://docs.copilotkit.ai/llamaindex/)
  -  [LlamaIndex example in AG-UI documentation](https://github.com/ag-ui-protocol/ag-ui/tree/main/typescript-sdk/integrations/llamaindex)