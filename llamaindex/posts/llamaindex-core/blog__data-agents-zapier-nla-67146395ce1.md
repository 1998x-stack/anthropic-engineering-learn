---
title: "Data Agents With Zapier NLA: Quick Setup Guide | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/data-agents-zapier-nla-67146395ce1"
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







>

Joint blog by LlamaIndex team &amp; Zapier NLA team

Wouldn’t it be great to have a personal assistant that can **access your data** and **perform tasks for you**?



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



Introducing LlamaIndex data agents, now more powerful with Zapier NLA. **Within 5 lines of code**, you can access the 5,000+ third party apps and over 30,000 actions on Zapier.

from llama_hub.tools.zapier.base import ZapierToolSpec
from llama_index.agent import OpenAIAgent

zapier_spec = ZapierToolSpec(api_key="sk-ak-your-key")
agent = OpenAIAgent.from_tools(zapier_spec.to_tool_list(), verbose=True)

agent.chat('Can you summarize the unread emails and send it to me on Slack?')