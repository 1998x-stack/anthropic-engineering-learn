---
title: "About deployment, evaluation, and testing of agents with Sully Omar, the CEO of Cognosys AI"
author: "Tereza Tizkova"
date: "2023-08-28"
url: "https://e2b.dev/blog/about-deployment-evaluation-and-testing-of-agents-with-sully-omar-the-ceo-of-cognosys-ai"
category: "case-studies"
site: "e2b"
---

[Cognosys](https://www.cognosys.ai/) provides a closed-source UI for creating AI agents. Their vision is to develop an easy-to-use consumer-facing product to assist non-technical individuals in completing specific daily tasks.

We asked the founder of [Cognosys](https://www.cognosys.ai/), [Sully Omar](https://twitter.com/SullyOmarr), about his experience with building a product for no-code users in the Agents space.

### Users and Basic Architecture

[Cognosys](https://www.cognosys.ai/) is a web-based version of AutoGPT/babyAGI working in "loops" - a series of tasks. The agent generates output based on provided objectives and iterates until completion. It puts high-level tasks into smaller ones, calls an LLM, and iterates until the task is done. The whole process takes a few seconds and requires zero coding. 
Sully emphasizes that the crucial moment is the first trial of Cognosys. “The people that have **found value within first experience with the agents**, are the ones who become **returning users**.”

There are more options offered for the agent’s “specialization”.

“Currently, we are focusing on **narrowing down the use cases** to just a few,” explains Sully. “People find the biggest value in letting the agent **dig into the internet.**”

The agent for searching over the internet, similar to [**Perplexity AI**](https://www.perplexity.ai/)**,** is currently the most popular one. The research agent takes an objective, conducts internet research, synthetizes it, and provides links to relevant sources.

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6797a08ea98f7c2ff1b4f24f_6797a01ad3be664fdf6632bc_kJRkgXVM5qMWkmbXlU5U094CQA.avif)

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6797a08ea98f7c2ff1b4f252_6797a02f4b6706e68851f64b_yUWe52P49DFhlGoMDYUfIHhu7kw.webp)**Source**: [https://cognosys.ai/](https://cognosys.ai/)

### Overcoming Agents Challenges

Sully comments on the current problems of agent developers.

“Locally, **monitoring of LLM agent’s steps** is easy, but **tracking what is happening at scale on the aggregate level is the most important challenge** to solve, for any company using LLMs in general.”
For tracing agent runs, Cognosys uses mostly its own UI. 

An important concern is how much information users should receive about the agents. According to Sully, for example, **offering users a choice between GPT-3.5 and GPT-4 is useless **if they do not understand which models are suitable for their needs. He believes that the primary concern of users is whether the agent can perform the expected tasks.

## 1. Deployment

The [Cognosys](https://www.cognosys.ai/) team started by using the [**Vercel edge function**](https://vercel.com/features/edge-functions), which had **a limit of 60 seconds for a timeout**. However, this posed a problem for Cognosys, since occasionally, the agent needs more time to execute.

They have tried [**Cloud Functions**](https://cloud.google.com/functions), which didn’t yield optimal results. Now they use **an instance of **[**Cloud Run**](https://cloud.google.com/run) **that all main systems run on**. “The advantage is that **we get a unified API via an API Gateway **for agents and can easily spin up tens of agents for a single user,”

There are issues that are associated with LLM calls in general. **Serverless functions are meant to take 10-50 milliseconds**. With LLM calls taking much more time, it doesn't make sense for Cognosys to use serverless architecture. They do use serverless for minor things, e.g. updating users’ profiles.

## 2. Observability

The [Cognosys](https://www.cognosys.ai/) team is exploring a variety of tools, using different **infra plugins for observability**, which is a challenge due to multiple factors contributing to the success or failure of agents.

“We have tried [**Sentry**](https://sentry.io/welcome/)**, **[**Google Cloud**](https://cloud.google.com/)**, **[**Google Cloud Platform**](https://cloud.google.com/gcp?utm_source=google&utm_medium=cpc&utm_campaign=emea-emea-all-en-bkws-all-all-trial-e-gcp-1011340&utm_content=text-ad-none-any-DEV_c-CRE_500236788675-ADGP_Hybrid+%7C+BKWS+-+EXA+%7C+Txt+~+GCP+~+General%23v3-KWID_43700060393213451-aud-1641092902540:kwd-87853815-userloc_9048063&utm_term=KW_gcp-NET_g-PLAC_&&gad=1&gclid=Cj0KCQjwoeemBhCfARIsADR2QCunVw3Ik-GCi1d1E_3uLJSLKNP2vdpjV_KCneskLRfd49cfS7n6rVsaApsGEALw_wcB&gclsrc=aw.ds).” names Sully. “Another one we are starting to look at and that is agnostic to agents, but still in beta version, is [**Langsmith**](https://smith.langchain.com/).”

The key aspect of observability is understanding which tools the agent uses throughout the process and whether they are the right choice.

### 3. Testing and Evals

“**Evaluation is currently a big challenge** for autonomous agents in general, due to the LLMs nature,” says Sully. “How do you define good output, especially for the longer and more complex runs requiring many steps, where **we lack the simple input-output relation**?”

We discussed how the **subjectivity of good versus bad results** is one of the root causes of agents' evaluation struggles. 

“There are two parts to evaluate. The objective part to evaluate is the binary form, for example, whether the agent did, or didn’t order a meal or booked a flight. The other and more tricky part is to evaluate how well the agent wrote a text or how quality research it did.”

## 4. Debugging

Cognosys has **its own system of the retrial of the agents’ steps **when it fails. It notifies the end user by saying that the instance failed, and they can run the agent again.

## 5. Latency

In traditional SW engineering,** around 200 milliseconds is considered slow**. For AI agents in general, latency is a big issue, with **LLM calls taking more than 30 seconds**. Cognosys agents usually run anywhere from 60 seconds to even 5 minutes sometimes.

“Currently, the agent uses [GPT-4](https://openai.com/gpt-4), which takes quite a long time to take action,” says Sully. “But people expect results quickly, and waiting even a minute until an agent provides the result makes them unsatisfied.”

## Conclusion

Sully realizes that the whole agents' space is still in the **early phase**.

“There is not that much functionality yet, so a big use-case at the beginning was just that the agent is fun to play with and try what it can do,” says Sully.

“But we want to continue focusing on a **few valuable specializations** for the agent. It’s very easy to want to do everything with the agent, but with the current models, it is impossible to do all these things well. And once the users get frustrated, they leave and never return.”

The [Cognosys](https://www.cognosys.ai/) team is working on a **new version of their platform**. “We are excited about our next iteration that would solve some of the agents' issues, like latency”.

“Our plan for the future is to make the system more robust and easier to use, and have users more aware of capabilities.”