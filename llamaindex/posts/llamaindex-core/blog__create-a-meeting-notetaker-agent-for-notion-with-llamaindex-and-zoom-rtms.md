---
title: "Meeting Notetaker Agent for Notion Guide | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/create-a-meeting-notetaker-agent-for-notion-with-llamaindex-and-zoom-rtms"
category: "llamaindex-core"
---

Content



- [ Combining Zoom RTMS and Custom LlamaIndex Events  ](#combining-zoom-rtms-and-custom-llamaindex-events)
- [ The Final Meeting Notes Assistant for Notion  ](#the-final-meeting-notes-assistant-for-notion)
- [ Points of Improvement  ](#points-of-improvement)
- [ In Summary  ](#in-summary)



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







 Zoom released their new RTMS functionality, specifically designed to bring live meeting data to AI agents. We’ve partnered with them for this release, and in this blog, I’ll walk through an example note taking agent that you can also find open-sourced [here](https://github.com/TuanaCelik/llama_index_zoom_assistant/tree/main).



 Before we get started, here are some basics to know about Zoom RTMS:



 When enabled, Zoom RTMS allows you to stream meeting data such as attendees who joined, transcripts from each attendee as the call is ongoing, attendees leaving the call, the call ending and so on.



 We can make use of this data during or after the call to enable a number of AI applications and agents. We’re also lucky that LlamaIndex’s event driven agent workflow approach ties in pretty well to this setup.



 So, in this blog, I’ll walk you through a small example built with Zoom RTMS, LlamaIndex agent Workflows, and the addition of the Notion API (because why not), to build an agent that works during an ongoing Zoom call to do the following:


-  Create a new ‘Meeting Notes’ page in a Notion Database when we receive the first “RTMS started” event (indicating that an attendee has joined a call)
  -  As the conversation is ongoing, write down ‘to-dos’ in the newly created Meeting Notes page
  -  When we get an event from Zoom RTMS indicating that the call has ended, we use an LLM to read the entire transcript and create a meeting summary at the end of the page

  ![](https://cdn.sanity.io/images/7m9jw85w/production/86db63fb211698e5a4c9d2264fb47631f95c56a9-1356x1278.png)

##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



##  Combining Zoom RTMS and Custom LlamaIndex Events



 For this project, I’ve created a completely custom [LlamaIndex Agent Workflow](https://docs.llamaindex.ai/en/stable/module_guides/workflow/). These workflows have 2 very important features: Events, and steps!



 Each step, can be triggered by an event, as well as emit events.



 This gave us the opportunity to translate some Zoom RTMS events to LlamaIndex Agent Workflow events. Let’s look at some of our custom events, when they’re triggered and what `step`  they result in:


-  `CreateNotionPage` : An event that we emit when we get the first `“meeting.rtms_started&quot;`  event from Zoom. It triggers a step called `create_notion_page`  that uses the Notion API to create a new page in a given database.
  -  `CheckForActions` : Throughout an ongoing RTMS stream, Zoom will send us various payloads. We can check the payload `msg_tye`  for a `MEDIA_DATA_TRANSCRIPT`  message - indicating that someone said something. This event is emitted once we’ve received a certain number of transcripts (that makes up a transcript chunk). This event then triggers a `evaluate_actions`  step which uses an LLM to check the transcript chunk for any action items or to-dos that should be added to our meeting notes in Notion.
  -  `ActionItems`  : This event is emitted by the previous step, *if* there are any action items to be extracted from the transcript chunk. It ten triggers a `add_action_items`  step to actually add them to our meeting notes.
  -  `SummarizeMeeting` : And finally, this is the last event that is triggered when we get the first `&quot;meeting.rtms_stopped&quot;`  event from Zoom. It triggers the last step, which is `meeting_end_summary` , before we stop the workflow.



##  The Final Meeting Notes Assistant for Notion



 The final result of our custom workflow is a Zoom Meeting Notes assistant that sits alongside your meeting, taking notes in Notion as you go along. You can watch a perfectly scripted fake call that I had with my colleague Clelia about a dream team get together we’d like to have in Italy below:




##  Points of Improvement



 A few things that I have not done, which are as always open to contributions:


-  The database I created in Notion for this demo also has a property called “Attendees”. And Zoom RTMS does a great job of delivering that information too. An extra step can be added to add the names of the attendees to this property.
  -  We don’t wait for the last person to leave the call to consider it ‘finished’ in this first implementation. The first “rtms_stopped” event we get is when we consider the call finished. We could do a better job of checking that all attendees have left before triggering the event that adds the meeting summary to the Notion page!



##  In Summary



 Zoom’s new RTMS feature opens up a powerful real-time interface to meeting data, and combining it with LlamaIndex&#39;s event-driven agent workflows makes it possible to build intelligent, responsive applications that evolve with the flow of conversation. In this example, we explored how to connect RTMS events to a multi-step agent that writes action items and summaries directly into Notion, effectively creating a live meeting assistant.



 This setup is just a starting point—there’s plenty of room to enhance the workflow further, from attendee tracking to smarter call-end logic. If you&#39;re interested in experimenting with this yourself or building something similar, here are some helpful resources to get started:


-  Get started with Zoom RTMS [here](https://developers.zoom.us/docs/rtms/).
  -  Check out the open-source demo [here](https://github.com/TuanaCelik/llama_index_zoom_assistant/tree/main).
  -  LlamaIndex Worflows [documentation](https://docs.llamaindex.ai/en/stable/module_guides/workflow/).