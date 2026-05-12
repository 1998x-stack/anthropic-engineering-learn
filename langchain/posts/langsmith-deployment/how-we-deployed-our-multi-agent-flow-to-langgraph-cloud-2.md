---
title: "How We Deployed our Multi-Agent Flow to LangGraph Cloud"
author: "LangChain Accounts"
date: "2024-07-15"
url: "https://www.langchain.com/blog/how-we-deployed-our-multi-agent-flow-to-langgraph-cloud-2"
---

LangGraphAgent Architecture

# How We Deployed our Multi-Agent Flow to LangGraph Cloud

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamJuly 15, 2024![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)6min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaf8c57c432b84a7381bc_assafe_a_team_of_friendly_and_cute_robot_agents_doing_academic__cea21689-2919-4e80-8bdb-45bd6be131ea.png)*Note: This is a guest blog post by Elisha Kramer, Tech Lead at Fiverr. He is also one of the top contributors of the leading `gpt-researcher` Github project by Assaf Elovic.*

After experimenting with the new LangGraph Cloud feature, we were so excited that we had to write about it. Below, we’ll show of how we deployed our LangGraph Cloud Host &amp; queried it from the [GPT Researcher](https://github.com/assafelovic/gpt-researcher?ref=blog.langchain.com) frontend (NextJS).

## **What is GPT Researcher?**

[GPT Researcher](https://github.com/assafelovic/gpt-researcher?ref=blog.langchain.com) is an open-source autonomous agent designed for comprehensive online research on a variety of tasks. The open source has grown in popularity over the past year, with over 13K stars and a community of 4K+ developers.

GPT Researcher has also been evolved over time, starting as a successful RAG implementation and now using multi-agents with the popular LangGraph framework.

But there was still a missing piece. GPT Researcher didn&#x27;t yet have a top-standard front-end application and was still built on simple HTML and CSS. We’re excited to introduce our latest client built with NextJS, designed to provide an optimal research experience! [Check out a demo here](https://www.youtube.com/watch?v=hIZqA6lPusk&amp;ref=blog.langchain.com).

## **How does LangGraph tie into the picture?**

As we started trying to build context-aware AI agents capable of reasoning through problems, we discovered the LangChain library and LangGraph.

Specifically, we were hooked on the concept of LangGraph: a framework that could enable us to build out complex multi-agent flows where AI agents coordinate with other agents, bringing their unique perspectives and reviewing each other&#x27;s work.

LangGraph turned out to be a great fit for that! And the ability to easily connect our new frontend to a cloud-based version of GPT Researcher sounded too good to be true.

## **What is LangGraph Cloud?**

The concept behind the LangGraph Cloud Host is very similar to the concept behind a GraphQL API Server.

A GraphQL API Server:

- Can help abstract away access to a database
- Can leverage any library of the Server Language

So too, a LangGraph API Server can:

- Abstract away access to a LangGraph
- Leverage any pip package used within your LangGraph

Essentially, you’re deploying a Python server with your LangGraph baked into it. And while you’re at it, you get a bunch of stuff for free; here are the [API endpoints automatically exposed on your LangGraph Cloud Host](https://langchain-ai.github.io/langgraph-example/?ref=blog.langchain.com) to enable easy job-triggering &amp; graph edits.

## **What did we deploy?**

In our case, the brunt of the work was done by Assaf, founder of  [GPT-Researcher](https://github.com/assafelovic/gpt-researcher?ref=blog.langchain.com), when he built a multi-agent workflow leveraging LangGraph. (Feel free to read up on that adventure in this earlier post: [How to Build the Ultimate AI Automation with Multi-Agent Collaboration](https://blog.langchain.com/how-to-build-the-ultimate-ai-automation-with-multi-agent-collaboration/).)

Once that multi-agent flow was built with LangGraph, it set the stage for some easy wins down the road. Several weeks later, Harrison (CEO of LangChain) stepped in &amp; created a pull request to enable us to easily deploy Assaf’s pre-built LangGraph: [Here’s the GPT Researcher PR](https://github.com/assafelovic/gpt-researcher/pull/537/files?ref=blog.langchain.com).

The beauty of that PR was that it made our GPT-Researcher LangGraph easily available to deploy, edit &amp; trigger with custom parameters via an API Call. Wow! Only 4 changed files to go from our dev environment to a scalable production-ready service!

## **Querying the LangGraph API Server**

It took me a while to fully appreciate the simplicity of the previous 2 steps. It couldn’t be that easy to trigger a multi-agent LLM workflow... could it?

Turns out, it was.

Building on top of Assaf &amp; Harrison’s code, all we needed to do was the following.

### Step 1: Watch [Harrison’s deployment tutorial](https://youtu.be/l4sMKF1dTDM?si=L2HdcZMg_UM1QGKZ&amp;t=254&amp;ref=blog.langchain.com)

### Step 2: Deploy our custom LangGraph [via the LangSmith GUI](https://smith.langchain.com/?ref=blog.langchain.com)’s “Deployments” tab.

In our case, I selected my fork of the GPT Researcher Project &amp; pointing to my langgraph.json config file within GPT Researcher’s multi_agents directory (see below)

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaf8d57c432b84a7381f5_AD_4nXedaZCT6HLcCvFp6xyG-r4F7-jOz-sNHT8cANqjWN--_Z7PSNOebxb3ON6pa6BWTZjL9ubsxITZEAkPuhaGNrPcJkfvm7V8jHMkEAwd76TFZWOapTtFwp6sYApOChYmJTKMD98XQhAJ2m60Gc0hx3Rlod0.png)

### **Step 3: **Add my environment variables to my LangGraph Cloud deployment.

These should suffice:

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaf8d57c432b84a7381f8_AD_4nXdvFlBYnmIqaaAO_xQSzqBihV0HFk_5R-lRSCxtqYXd0GzShUfzitAA8QDpUffsttkh6pHY2w8C1N3CYarQhY0krV3sn2W81DmJk_1SY09AvZQIlGQHPE8dMOtxjVSpOntGWJCUi0PdEhHLDX8yjL_5XUFa.png)

Notice in the screenshot above that LangGraph Cloud will automatically create a “Tracing Project” for me.

That means we get the same LangSmith tracing benefits that we got with our MVP multi-agents flow. Here’s what it looks like:

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaf8e57c432b84a7381ff_AD_4nXfb4dwrSbJrf6wZOXNRbcjZqanUO5WdsmE7E5NBOWcKqVc8fWqIpSpoUX78MlSzAa6X7OzRscshpldLpdwXIOGH09Mj3-1QTviXMjL1piOPIUprUUZhnNqE0V36MaaiC85mPbnA-HYM-i5vR_WHbZaL4RY.png)

And here’s what you get — a powerful tool for:

- Enabling users to visualize and inspect the backend data flow
- Quality assurance debugging - i.e. where can the input or output of our AI flows use improvement

### **Step 4:** Query the newly deployed LangGraph.

Here’s a sample of the React Code:

`
import { getHost } from &#x27;../../helpers/getHost&#x27;;
import { Client } from &quot;@langchain/langgraph-sdk&quot;;
import { task } from &#x27;../../config/task&#x27;;

export async function startLanggraphResearch(newQuestion, report_source) {
   // Update the task query with the new question
   task.task.query = newQuestion;
   task.task.source = report_source;
   const host = getHost({purpose: &#x27;langgraph-gui&#x27;});
   const client = new Client({apiUrl: host});
    // List all assistants
   const assistants = await client.assistants.search({
     metadata: null,
     offset: 0,
     limit: 10,
   });

   const agent = assistants[0];
    // Start a new thread
   const thread = await client.threads.create();
    // Start a streaming run
   const input = task;
    const streamResponse = client.runs.stream(
     thread[&quot;thread_id&quot;],
     agent[&quot;assistant_id&quot;],
     {
       input,
     },
   );

   return {streamResponse, host, thread_id: thread[&quot;thread_id&quot;]};
}
`

The task object imported at the top of the file can be thought of as our API Request object. It’s practically identical to the [task.json file leveraged by Assaf’s LangGraph.](https://blog.langchain.com/how-to-build-the-ultimate-ai-automation-with-multi-agent-collaboration#running-the-research-assistant)

The getHost function either returns localhost:8123 (for the langgraph-cli service) or the domain of the LangGraph Cloud Server we deployed on.

And that’s pretty much all there is to it. The above code enables us to trigger a run on the LangGraph server - which is fully observable on the LangSmith User Interface! Here’s the continuation of the above code which displays to the user the status of our LangGraph State (per task) as our multi-agent flow runs through its paces:

`     const langsmithGuiLink = `https://smith.langchain.com/studio/thread/${thread_id}?baseUrl=${host}`;

     let previousChunk = null;

     for await (const chunk of streamResponse) {
       console.log(chunk);
       if (chunk.data.report != null &amp;&amp; chunk.data.report != &quot;Full report content here&quot;) {
         setOrderedData((prevOrder) =&gt; [...prevOrder, { ...chunk.data, output: chunk.data.report, type: &#x27;report&#x27; }]);
         setLoading(false);
       } else if (previousChunk) {
         const differences = findDifferences(previousChunk, chunk);
         setOrderedData((prevOrder) =&gt; [...prevOrder, { type: &#x27;differences&#x27;, content: &#x27;differences&#x27;, output: JSON.stringify(differences) }]);
       }
       previousChunk = chunk;
     }
   }
`

Notice in an earlier code snippet that we leveraged the `client.runs.stream` method.

That means that the LangGraph API Server will feed us back updates in chunks. Those chunks can contain: the updated state of the Job currently running or any custom errors our python scripts encountered on our deployed LangGraph server.

In our case, we wanted to show our users a custom play-by-play of the LangGraph API Job - therefore, we also added a `findDifferences` function whose role is to calculate the difference between two JavaScript objects.

If the Graph completes the report, that report is displayed to the user.

If the Graph had some field edits in real-time, those differences in the Graph are displayed to the user.

## **Summary**

In this blog post, we show how we triggered our LangGraph multi-agent flows via React &amp; LangGraph Cloud. These flows mimic human reasoning, making them quite complex. However, as demonstrated in the walkthrough above, an elegant API simplifies the process and makes everything fall into place effortlessly.

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69f20536df00c0eb15eab1d3_blue-77%20characters%20max.png)Deep AgentsAgent ArchitectureOpen Source

#### Tuning Deep Agents to Work Well with Different Models

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcefac505b6b48827abf84_vivek-trivedy.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcf032ce65a32e276a4d0a_mason-daugherty.png)Vivek TrivedyMason DaughertyApril 29, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)5min[](/blog/tuning-deep-agents-different-models)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef96ff74c638e982ff68c6_86%20(1).png)Agent ArchitectureLangSmithOpen Source

#### How LangSmith and LangChain OSS Help You Meet EU AI Act Requirements

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0003a1af368dfae13c23c_jacob-talbot.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Jacob TalbotBecca WengApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/langsmith-langchain-oss-eu-ai-act)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e23754937c2f749d12bb0b_76%20(1).png)Agent ArchitecturePartner

#### Agentic Engineering: How Swarms of AI Agents Are Redefining Software Engineering

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e234176723e6111407b935_renuka-kumar.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e23427e77d2631610e5d62_Prashanth-Ramagopal.png)Renuka KumarPrashanth RamagopalApril 17, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)11min[](/blog/agentic-engineering-redefining-software-engineering)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)