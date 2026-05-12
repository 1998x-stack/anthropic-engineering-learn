---
title: "LLM Agent Tools: Best Practices and Tips | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/building-better-tools-for-llm-agents-f8c5a6714f11"
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







Over the past month I’ve been diving into the world of Large Language Model (LLM) Agents and building out LlamaIndex’s library of tools for use with agents. I helped to lead the LlamaHub Tools effort as part of broader [Data Agents launch](https://medium.com/llamaindex-blog/data-agents-eed797d7972f) last week.



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



In the process of building out LlamaHub Tools I’ve collected some techniques for creating effective and easy to use tools, and want to share some of my thoughts.

# Context on LlamaHub Tools

[LlamaHub Tools](https://llamahub.ai/) allow LLMs like ChatGPT to connect to APIs and act on a user’s behalf to create, read, update and delete data. Examples of tools that we’ve put together include [drafting and sending emails](https://llamahub.ai/l/tools-gmail), [reading and creating Google Calendar invite](https://llamahub.ai/l/tools-google_calendar)s, [searching Wikipedia](https://llamahub.ai/l/tools-wikipedia), and that’s just a few of the 15 tools we are releasing on launch.

## Overview of tool abstractions

So how exactly do LlamaHub Tools work? The LlamaHub tool abstractions allow you to easily write Python functions that can be understood and called by Agents. Instead of trying to make an Agent do complicated mathematics for example, we can provide the Agent with a Tool that calls Wolfram Alpha and provides the result to the Agent:

from llama_index.tools.base import BaseToolSpec

QUERY_URL_TMPL = "http://api.wolframalpha.com/v1/result?appid={app_id}&amp;amp;i={query}"

# Inherit from the LlamaIndex BaseToolSpec abstraction
class WolframAlphaToolSpec(BaseToolSpec):

  # Define the functions that we export to the LLM
    spec_functions = ["wolfram_alpha_query"]

  # Initialize with our wolfram alpha API key
    def __init__(self, app_id: Optional[str] = None) -&amp;gt; None:
        """Initialize with parameters."""
        self.token = app_id

  # Our function to be called by the Agent
  def wolfram_alpha_query(self, query: str):
          """
          Make a query to wolfram alpha about a mathematical or scientific problem.

          Example inputs:
              "(7 * 12 ^ 10) / 321"
              "How many calories are there in a pound of strawberries"

          Args:
              query (str): The query to be passed to wolfram alpha.

          """
          response = requests.get(QUERY_URL_TMPL.format(app_id=self.token, query=urllib.parse.quote_plus(query)))
          return response.textThe above code is enough to define a LlamaIndex Tool that allows the Agent to query to Wolfram Alpha. No more incorrect guesses at math problems! We can initialize an instance of the Tool Spec like this:

# Initialize an instance of the Tool
wolfram_spec = WolframAlphaToolSpec(app_id="your-key")
# Convert the Tool Spec to a list of tools. In this case we just have one tool.
tools = wolfram_spec.to_tool_list()
# Convert the tool to an OpenAI function and inspect
print(tools[0].metadata.to_openai_function())Here’s the cleaned up output of the print statement:

{
  'description': '
    Make a query to wolfram alpha about a mathematical or scientific problem.

          Example inputs:
              "(7 * 12 ^ 10) / 321"
              "How many calories are there in a pound of strawberries"

          Args:
              query (str): The query to be passed to wolfram alpha.',
  'name': 'wolfram_alpha_query',
  'parameters': {
    'properties': {'query': {'title': 'Query', 'type': 'string'}},
    'title': 'wolfram_alpha_query',
    'type': 'object'
  }
}We can see that the [docstring](https://en.wikipedia.org/wiki/Docstring) describing how to use the Tool get passed to the Agent. Additionally, the parameters, type info and function name are passed along to give the Agent a strong idea on how it can use this function. All of this information is essentially acting as the prompt for how the agent understands the tool.

Inheriting from the BaseToolSpec class means it’s very simple to write Tools for Agents to use. In fact, the above tool definition is only 9 lines of code, ignoring white space, imports and comments. We can easily get the function ready for Agents to use without any heavy boilerplate or modifications. Let’s look at loading the Tool into an OpenAI Agent:

agent = OpenAIAgent.from_tools(tools, verbose=True)
agent.chat('What is (7 * 12 ^ 10) / 321')
""" OUTPUT:
=== Calling Function ===
Calling function: wolfram_alpha_query with args: {
  "query": "(7 * 12 ^ 10) / 14"
}
Got output: 30958682112
========================
Response(response='The result of the expression (7 * 12 ^ 10) / 14 is 30,958,682,112.', source_nodes=[], metadata=None)
"""And we can test out passing this query to ChatGPT without the tools:

&amp;gt; 'What is (7 * 12 ^ 10) / 321'
"""
To calculate the expression (7 * 12^10) / 14, you need to follow the order of operations, which is parentheses, exponents, multiplication, and division (from left to right).

Step 1: Calculate the exponent 12^10.
12^10 = 619,173,642,24.

Step 2: Multiply 7 by the result from Step 1.
7 * 619,173,642,24 = 4,333,215,496,68.

Step 3: Divide the result from Step 2 by 14.
4,333,215,496,68 / 14 = 309,515,392,62.

Therefore, the result of the expression (7 * 12^10) / 14 is 309,515,392,62.
"""This example should show how easily you can write new Tools for use with Agents. For the rest of the blog post I’ll be talking about tips and tricks I’ve found to write more functional and effective tools. Hopefully by the end of the blog post you are excited to write and contribute some Tools of your own!

# Techniques for building better tools

Below are a variety of tactics for writing more usable and functional tools to minimize friction when interfacing with the Agent. Not all of the tactics apply to every tool, but usually at least a few of the techniques below will prove valuable.

## Writing useful tool prompts

Here’s an example of the function signature and docstring for a tool that an Agent can call to create a draft email.

def create_draft(
        self,
        to: List[str],
        subject: str,
        message: str
    ) -&amp;gt; str:
        """Create and insert a draft email.
           Print the returned draft's message and id.
           Returns: Draft object, including draft id and message meta data.

        Args:
            to (List[str]): The email addresses to send the message to, eg ['adam@example.com']
            subject (str): The subject for the event
            message (str): The message for the event
        """This prompt takes advantage of a few different patterns to ensure that the agent can use the tool effectively:

- Give a concise description of the function and its purpose
- Inform the Agent on what data will be returned from this function
- List the arguments that the function accepts, with descriptions and type information
- Give example values for arguments with a specific format, eg adam@example.com

Tool prompts should be concise as to not take up too much length in context, but also informative enough that the agent can use the tool without making mistakes.

## Making tools tolerant of partial inputs

One way to help Agents make fewer mistakes is to write tools that are more *tolerant* of their inputs, for example by making inputs optional when the value can be inferred from somewhere else. Take the example of drafting an email, but this time let’s consider a tool that updates a draft email:

def update_draft(
        self,
        draft_id: str,
        to: Optional[List[str]] = None,
        subject: Optional[str] = None,
        message: Optional[str] = None,
    ) -&amp;gt; str:
        """Update a draft email.
           Print the returned draft's message and id.
           This function is required to be passed a draft_id that is obtained when creating messages
           Returns: Draft object, including draft id and message meta data.

        Args:
            draft_id (str): the id of the draft to be updated
            to (Optional[str]): The email addresses to send the message to
            subject (Optional[str]): The subject for the event
            message (Optional[str]): The message for the event
        """The Gmail API **requires** all of the above values when updating a draft, however using just the `draft_id` we can fetch the current content of the draft and use the existing values as defaults if the Agent did not provide the values when updating the draft:

def update_draft(...):
  ...
  draft = self.get_draft(draft_id)
  headers = draft['message']['payload']['headers']
  for header in headers:
      if header['name'] == 'To' and not to:
          to = header['value']
      elif header['name'] == 'Subject' and not subject:
          subject = header['value']
    elif header['name'] == 'Message' and not message:
      message = header['values']
  ...By providing the above logic in the `update_draft` function, the Agent can invoke `update_draft` with only one of the fields (and the `draft_id`), and we can update the draft as the user expects. This means that in more circumstances the Agent can complete the task successfully, instead of returning an error or needing to ask for more information.

## Validating input and Agent error handling

Despite best efforts at prompting and tolerance, we can end up in circumstances where the Agent invokes a tool in a way that it can’t complete the task at hand. However, we can detect this and prompt the Agent to recover the error on its own.

For example, in the `update_draft` example above, what do we do if the agent calls the function without a `draft_id`? We could simply pass along the null value and return an error from the Gmail API library, but we could also detect that a null `draft_id` will invariably cause an error, and return a prompt for the agent instead:

def update_draft(...):
  if draft_id == None:
    return "You did not provide a draft id when calling this function. If you previously created or retrieved the draft, the id is available in context"Now, if the Agent invokes `update_draft` without a `draft_id` , it is made aware of the exact mistake it made and given instructions on how it can correct the issue.

In my experience working with this tool, the Agent will often immediately call the `update_draft` function in the correct way when receiving this prompt, or if there is no `draft_id` available, it will inform the user of the issue and ask the user for a `draft_id`. Either scenario is much better than crashing or returning an opaque error from a library to the user.

## Providing simple functions related to the tool

Agents can struggle at what would otherwise be simple functions for a computer to calculate. For example, when building a tool for creating events in Google Calendar, a user may prompt the Agent with something like this:

>

*Create an event on my Calendar to discuss the Tools PR with *[*adam@example.com*](mailto:adam@example.com)* tomorrow at 4pm*

Can you see the problem? If we try asking ChatGPT what day it is:

agent.chat('what day is it?')
# &gt; I apologize for the confusion. As an AI language model, I don't have real-time data or access to the current date. My responses are based on the information I was last trained on, which is up until September 2021. To find out the current day, I recommend checking your device's clock, referring to a calendar, or checking an online source for the current date.Agents won’t know what the current date is, and so the Agent would either call the function incorrectly, providing a string like `tomorrow` for the date, hallucinate a date sometime in the past based on when it was trained, or put the burden on the user to tell it the date. All of the above actions cause friction and frustration for the user.

Instead, in the Google Calendar Tool Spec we provide a simple deterministic function for the agent to call if it needs to fetch the date:

def get_date(self):
        """
        A function to return todays date.
        Call this before any other functions if you are unaware of the current date
        """
        return datetime.date.today()Now, when the Agent tries to handle the prompt above, it can first call the function to get the date and then create the event as the user requested, inferring the date for “tomorrow” or “a week from now”. No errors, no guesses and no need for further user interaction!

## Returning prompts from functions that perform mutations

Some functions perform mutations to data in a way that it isn’t clear what useful data can be returned from the function, back to the agent. For example, in the Google Calendar tool if an event is successfully created it doesn’t make sense to return the content of the event back to the Agent, as the agent just passed in all of the information and thus has it in context.

Generally with functions that are focused on mutations (create, update, delete) we can help the Agent understand its actions better by using the return value of these functions to further prompt the agent. For example, from the Google Calendar `create_event` tool we could do the following:

def create_event(...):
  ...
  return 'Event created succesfully! You can move onto the next step.'  This helps the agent register that the action succeeded and encourages it to complete the action it was prompted for, especially if creating the google calendar event is only a single step in a multiple step instruction. We can still return ids as part of these prompts as well:

def create_event(...):
  ...
  event = service.events().insert(...).execute()
  return 'Event created with id {event.id}! You can move onto the next step.'

## Storing large responses in indices for the Agent to read

One consideration when building tools that has been mentioned already is the size of the context window the Agent has. Currently, LLMs tend to have context windows from 4k-16k tokens, however it can certainly be larger or smaller. If the size of the data that a tool would return is larger than the context window, the Agent will be unable to process the data and error out.

One consideration when building tools that has been mentioned already is the size of the context window the Agent has. Currently, LLMs tend to have context windows from 4k-16k tokens, however it can certainly be larger or smaller. If the size of the data that a tool would return is larger than the context window, the Agent will be unable to process the data and error out.

The only consideration that needs to be made when creating tools that might need to be wrapped by the LoadAndSearchTool, is they need to return a list of LlamaIndex documents. For a tool that returns a string, the only modification you need to make to have it be compatible with the LoadAndSearchTool is wrapping it in a document and an array:

from llama_index.readers.schema.base import Document

# Not compatible
def large_text_response_function():
  ...
  return result

# LoadAndSearch compatible
def large_text_response_function():
  ...
  return [Document(text=result)]

## Verify how the Agent understands the tool

A useful technique for debugging tools in development is to **ask the Agent about its own tools**: the tools it has available, what arguments the tools accept, what those arguments represent, and what the tool is used for. The responses of the Agent are useful in determining where your prompts might be lacking or helping pinpoint why an Agent is failing to successfully use a tool that you are developing.

An example conversation debugging the Google Calendar Tool Spec, assuming you have setup an Agent similar to the example notebook:

agent.chat('what tools do you have available')
# I have the following tools available
#   1. `load_data`: This tool allows me to load data from your calendar. It can retrieve a specified number of events starting from a given date.
#   2. `create_event`: This tool allows me to create an event on your calendar. You can provide details such as the title, description, location, start datetime, end datetime, and attendees.
#   3. `get_date`: This tool returns today's date. It can be used to ensure that the correct date is used when working with other tools.
# Please let me know if you would like more information about any of these tools or if you have any specific requests.
agent.chat('what arguments does the load_data tool take')
# 'The `load_data` tool takes the following arguments:
#   1. `number_of_results` (optional, default: 100): Specifies the number of events to return from your calendar.
#   2. `start_date` (optional): Specifies the start date from which to retrieve events. It can be provided as a string in ISO format (e.g., "2023-07-05") or as a `datetime.date` object.
# You can use these arguments to customize the number of events and the start date for retrieving data from your calendar.

# Concluding thoughts

Building tools for Agents requires you to think critically about how users will interact with the Agent, and to try and anticipate any possible usage patterns. Building well thought out tools that can be resilient to errors and issues requires careful consideration and testing of possible use cases. I hope that these reflections and techniques assist you in creating new tools for Agents, and don’t forget to share your tools on [LlamaHub](https://llama-hub-ui.vercel.app/).