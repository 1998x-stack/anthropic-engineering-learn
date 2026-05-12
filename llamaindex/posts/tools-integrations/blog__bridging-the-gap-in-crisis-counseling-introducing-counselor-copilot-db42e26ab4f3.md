---
title: "Crisis Counseling AI Copilot: How It Works | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/bridging-the-gap-in-crisis-counseling-introducing-counselor-copilot-db42e26ab4f3"
category: "tools-integrations"
---

Content



- [ Introduction  ](#introduction)
- [ Problem: The Dual Challenge Faced by Crisis Counselors  ](#problem-the-dual-challenge-faced-by-crisis-counselors)
- [ The Winning Solution: An AI Copilot for Crisis Counselors  ](#the-winning-solution-an-ai-copilot-for-crisis-counselors)
- [ How we built it  ](#how-we-built-it)
- [ Possible Extensions  ](#possible-extensions)
- [ Conclusion: A Step Toward Efficient and Effective Crisis Care  ](#conclusion-a-step-toward-efficient-and-effective-crisis-care)
- [ References  ](#references)



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







 *Co-authored by: [Riya Jagetia](https://medium.com/u/e84f937083e3?source=post_page-----db42e26ab4f3--------------------------------),* *[Tarun Malik](https://medium.com/u/7d279643046e?source=post_page-----db42e26ab4f3--------------------------------),* *[Divija N](https://medium.com/u/6fe4060f2a53?source=post_page-----db42e26ab4f3--------------------------------),* *[Sharon Tan](https://medium.com/u/361137e928c3?source=post_page-----db42e26ab4f3--------------------------------),* [*Zehra Rizvi*](https://medium.com/u/7bdf7b817eec?source=post_page-----db42e26ab4f3--------------------------------), [*Amanda Piyapanee*](https://medium.com/u/b75312a598d6?source=post_page-----db42e26ab4f3--------------------------------)



 At the recent LlamaIndex RAG-a-thon [1], our team’s **“Counselor Copilot”** won 2nd prize in the Traditional track and 1st prize in the Datastax/AstraDB category. More details can be found on our [DevPost](https://devpost.com/software/counselor-copilot) [2] writeup.



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



##  Introduction



 Against the backdrop of growing strain on mental health services [3, 4], non-profit organizations like The Trevor Project [5] are a critical part of the care ecosystem. Focusing on helping LGBTQ+ youth who are contemplating suicide, The Trevor Project provides accessible crisis services including via TrevorText, an online chat service with trained volunteer counselors.



##  Problem: The Dual Challenge Faced by Crisis Counselors



 However, TrevorText counselors face significant challenges. Not only is there high demand for counselors during busy times like holidays and night shifts, but also, counselors have to juggle a number of administrative tasks such as sifting through forms, responding to messages across multiple chats, and locating relevant local resources. This not only increases the risk of counselors burning out but also hampers their ability to provide timely and effective care.



 In light of these challenges, there’s a pressing need for innovative solutions to bridge the gap between the demand and supply of crisis services.



 While our hackathon project focused on augmenting TrevorText, our product can be easily extended to general crisis chat alternatives as well.



##  The Winning Solution: An AI Copilot for Crisis Counselors



 Counselor Copilot is a real-time assistant for crisis counselors that takes into account contact context and chat history to suggest replies so that counselors can focus on what they do best: providing care. **There is no prompting that is needed from counselors; the copilot works seamlessly in the background.**



 Further, the copilot never directly replies to contacts; instead, replies are suggested and can be edited.

  ![](https://cdn.sanity.io/images/7m9jw85w/production/99979b85638c80808db1a1d41ac3df549735b72f-1600x646.webp) Counselor copilot takes into account contact context and chat history to provide real-time reply suggestions to the counselors

 Specifically, the copilot automates counselor tasks that include but are not limited to:


-  Retrieving and synthesizing contact data from complex PDFs in real-time. This also provides counselors context on their contacts when conversations are initiated.
  -  Assessing from the chat context if emergency intervention is required. If so, suggesting escalation to a supervisor.
  -  Using existing resources and guidelines from the organization to suggest appropriate replies.

  ![](https://cdn.sanity.io/images/7m9jw85w/production/3eebd183751fe14cb81676a33f55803ff9ab8a0b-751x405.webp)

 4. Searching for location-specific resources for contacts, and quickly sharing those resources via email.

  ![](https://cdn.sanity.io/images/7m9jw85w/production/6eb187a5ba134f34d4275d8ae2a81197b2f0defd-1489x232.webp)

 5. Completing case forms in a CRM for contacts, including summarizing the interaction.

  ![](https://cdn.sanity.io/images/7m9jw85w/production/ff5a01b3be56bbff38170e42f2091c83c6254358-1600x803.webp)

 While these tasks are important and necessary, they pull attention away from conversations with youth in crisis and take up precious time.



 With Counselor copilot, these tasks are completed when they are required and without any prompting from counselors, providing more bandwidth for counselors and ultimately leading to higher-quality conversations with patients.



 Below is a demo of our solution:



##  How we built it



 When the chat is initiated, the Counselor Copilot gets the contact’s data from the CRM, which is stored in complex PDFs. We used LlamaParse to extract relevant contact data in real-time and then provide a summary of that data to counselors as context at the beginning of each conversation.

  ![](https://cdn.sanity.io/images/7m9jw85w/production/0d224551401600550e9a5cac36177616e4104dcb-1384x1038.webp)

 Further, we used a LlamaIndex ReAct Agent to monitor the conversation and — based on the chat history and contact context — deploy the right tool. Tools at the ReAct Agent’s disposal include:


-  Escalating the conversation to a supervisor
  -  Suggesting a response and related resources based on The Trevor Project’s guidelines
  -  Searching the web for location-specific resources and sending the resources to the contact



 For tool #2, we created a vector database that contains The Trevor Project’s documents, which highlight key guidelines for counselors based on different scenarios and situations that they may face. We used RAG to retrieve resources relevant to the conversation, and GPT4 to draft a response for the counselor based on those resources, both of which are essential due to the sensitive nature of the conversation.



 Lastly, we used the conversation content to fill out a form with key Salesforce fields (e.g. name, age, city, state), as well as to summarize the conversation.



##  Possible Extensions



 We’re excited by the potential for others to build on our work [6] and extend Counselor Copilot further. Some ideas include:


-  Reduce costs and improve quality of suggested responses: Fine-tune a state-of-the-art open-source LLM on extracts of chat conversations conducted by counselors
  -  More targeted conversation management: Add a tool for the agent to assess the stage of the conversation, given that there are recommended styles and questions for each stage (e.g. establishing rapport, risk assessment)
  -  Closed-loop feedback cycle: Allow counselors to thumbs-up or thumbs-down selected responses, as a natural way to collect human feedback which can be used for further model or agent training



##  Conclusion: A Step Toward Efficient and Effective Crisis Care



 Our AI copilot for crisis counselors represents a significant step toward more efficient and effective crisis care. By automating administrative tasks, it frees up counselors to focus on their core mission of providing youth in crisis a safe place to talk. This not only enhances the quality of care provided but also addresses the pressing issue of counselor shortage by maximizing the impact of existing resources. As we continue to refine and expand this technology, we envision a future where crisis counseling is more accessible, responsive, and impactful for all those in need​​.



##  References


-  [https://rag-a-thon.devpost.com/](https://rag-a-thon.devpost.com/)
  -  [https://devpost.com/software/counselor-copilot](https://devpost.com/software/counselor-copilot)
  -  [https://www.mhanational.org/issues/state-mental-health-america](https://www.mhanational.org/issues/state-mental-health-america)
  -  [https://www.aamc.org/news/growing-psychiatrist-shortage-enormous-demand-mental-health-services](https://www.aamc.org/news/growing-psychiatrist-shortage-enormous-demand-mental-health-services)
  -  [https://www.thetrevorproject.org/](https://www.thetrevorproject.org/)
  -  [https://github.com/zrizvi93/trevorhack](https://github.com/zrizvi93/trevorhack)