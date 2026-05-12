---
title: "Automate Online Tasks With MultiOn &amp; LlamaIndex Guide | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/automate-online-tasks-with-multion-and-llamaindex"
category: "llamaindex-core"
---

Content



- [ Introduction  ](#introduction)
- [ Technical walkthrough: Integrating MultiOn with LlamaIndex  ](#technical-walkthrough-integrating-multion-with-llamaindex)
- [ Next Steps  ](#next-steps)



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







##  **Introduction**



 MultiOn is an AI agents platform designed to facilitate the autonomous completion of tasks in any web environment. It empowers developers to build AI agents that can manage online activities from start to finish, handling everything from simple data retrieval to complex interactions.



 LlamaIndex complements this by providing an orchestration framework that bridges the gap between private and public data essential for building applications with Large Language Models. It facilitates data ingestion, indexing, and querying, making it indispensable for developers looking to leverage generative AI.



 In this article, we&#39;ll demonstrate how MultiOn&#39;s capabilities can be seamlessly integrated within the LlamaIndex framework, showcasing a practical application that leverages both technologies to automate and streamline web interactions.



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



##  **Technical walkthrough: Integrating MultiOn with LlamaIndex**



 Let’s explore a practical example where MultiOn and LlamaIndex work in tandem to manage email interactions and web browsing.



 **Step 1: Setting Up the Environment** We begin by setting up our AI agent with the necessary configurations and API keys:



python






```
import openai
from llama_index.agent.openai import OpenAIAgent
openai.api_key = "sk-your-key"

from llama_index.tools.multion import MultionToolSpec
multion_tool = MultionToolSpec(api_key="your-multion-key")
```
    **Step 2: Integrating Gmail Search Tool** Next, we integrate a Gmail search tool to help our agent fetch and analyze emails, providing the necessary context for further actions:



python






```
from llama_index.tools.google import GmailToolSpec
from llama_index.core.tools.ondemand_loader_tool import OnDemandLoaderTool

gmail_tool = GmailToolSpec()
gmail_loader_tool = OnDemandLoaderTool.from_tool(
    gmail_tool.to_tool_list()[1],
    name="gmail_search",
    description="""
         This tool allows you to search the users gmail inbox and give directions for how to summarize or process the emails

        You must always provide a query to filter the emails, as well as a query_str to process the retrieved emails.
        All parameters are required

        If you need to reply to an email, ask this tool to build the reply directly
        Examples:
            query='from:adam subject:dinner', max_results=5, query_str='Where are adams favourite places to eat'
            query='dentist appointment', max_results=1, query_str='When is the next dentist appointment'
            query='to:jerry', max_results=1, query_str='summarize and then create a response email to jerrys latest email'
            query='is:inbox', max_results=5, query_str='Summarize these emails'
    """
)
```
    **Step 3: Initialize agent**



 Initialise the agent with tools and a system prompt



python






```
agent = OpenAIAgent.from_tools(
    [*multion_tool.to_tool_list(), gmail_loader_tool],
    system_prompt="""
	    You are an AI agent that assists the user in crafting email responses based on previous conversations.

	    The gmail_search tool connects directly to an API to search and retrieve emails, and answer questions based on the content.
	    The browse tool allows you to control a web browser with natural language to complete arbitrary actions on the web.

	    Use these two tools together to gain context on past emails and respond to conversations for the user.
    """
)
```
    **Step 4: Agent Execution Flow** With our tools integrated, the agent is now equipped to perform a series of tasks:




 **1. Search and Summarize Emails**: The agent uses LlamaIndex&#39;s Gmail tool to fetch relevant emails and summarize the content, providing a basis for drafting a response.



python






```
print(agent.chat("browse to the latest email from Julian and open the email"))
```
     text






```
Added user message to memory: browse to the latest email from Julian and open the email
=== Calling Function ===
Calling function: gmail_search with args: {"query":"from:Julian","max_results":1,"query_str":"Browse to the latest email from Julian and open the email"}
Please visit this URL to authorize this application: https://accounts.google.com/o/oauth2/auth?response_type=code&#x26;client_id=1054044249014.apps.googleusercontent.com&#x26;redirect_uri=http%3A%2F%2Flocalhost%3A8080%2F&#x26;scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fgmail.compose+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fgmail.readonly&#x26;state=JSdsfdsi990sddsd&#x26;access_type=offline
Got output: Open the email from Julian to view the latest communication.
========================

I have opened the latest email from Julian for you to view. If you need any specific information or action to be taken, please let me know.
```
    **2. Generate Response**: Based on the summarized information, the agent crafts an appropriate response to the email chain.



python






```
print(agent.chat(
	"Summarize the email chain with julian and create a response to the last email that confirms all the details"
))
```
     text






```
Added user message to memory: Summarize the email chain with julian and create a response to the last email that confirms all the details
=== Calling Function ===
Calling function: gmail_search with args: {"query":"from:Julian","max_results":1,"query_str":"Summarize the email chain with Julian and create a response to the last email confirming all the details"}
Got output: The email chain with Julian involved a change in an event scheduled for Friday, August 6, 2021, from 15:30 to 16:00 United Kingdom Time on Google Meet. The instructions for joining were provided in the description. The email also included contact information for joining the meeting. Julian and Nassar were listed as attendees, with Julian being the organizer. The email was authenticated and passed SPF and DKIM checks.

In response to the last email, I would confirm all the details of the event change, reiterating the date, time, platform (Google Meet), and any specific instructions provided. I would express gratitude for the update and confirm attendance at the revised event timing.
========================

Based on the email chain with Julian, here is a summary:
- The event scheduled for Friday, August 6, 2021, has been changed from 15:30 to 16:00 United Kingdom Time on Google Meet.
- Instructions for joining the meeting were provided in the email.
- Attendees included Julian and Nassar, with Julian as the organizer.
- The email passed SPF and DKIM checks.

To respond and confirm all the details, you can mention the revised event date and time, the platform (Google Meet), and express gratitude for the update. Confirm your attendance at the new timing. Let me know if you would like me to draft the response email for you.
```
    **3. Send Email through MultiOn**: Finally, the generated response is passed to the MultiOn agent, which manages the action of sending the email through the web browser.



python






```
print(agent.chat(
	"pass the entire generated email to the browser and have it send the email as a reply to the chain"
))
```
     text






```
Added user message to memory: pass the entire generated email to the browser and have it send the email as a reply to the chain
=== Calling Function ===
Calling function: browse with args: {"cmd": "Compose a reply email to Julian confirming the event change to Fri 6 Aug 2021 from 15:30 to 16:00 UK Time on Google Meet. Express readiness to attend and thank Julian for the details."}
Got output: Email response sent to Julian
========================
```


##  Next Steps

  MultiOn is an officially supported tool on LlamaHub, the central page for all LlamaIndex integrations (from tools to LLMs to vector stores). Check out the [LlamaHub page](https://llamahub.ai/l/tools/llama-index-tools-multion?from=) here.



 If you’re interested in running through this tutorial on building a browser + Gmail-powered agent yourself, check out our [notebook](https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/tools/llama-index-tools-multion/examples/multion.ipynb).



 The integration of MultiOn and LlamaIndex offers a powerful toolkit for developers aiming to automate and streamline online tasks. As these technologies evolve, they will continue to unlock new potentials in AI application, significantly impacting how developers interact with digital environments and manage data.