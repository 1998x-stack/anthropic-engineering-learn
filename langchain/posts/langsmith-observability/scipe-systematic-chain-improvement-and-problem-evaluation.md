---
title: "SCIPE - Systematic Chain Improvement and Problem Evaluation"
author: "LangChain Accounts"
date: "2024-11-07"
url: "https://www.langchain.com/blog/scipe-systematic-chain-improvement-and-problem-evaluation"
---

LangGraphDeployment

# SCIPE - Systematic Chain Improvement and Problem Evaluation

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamNovember 7, 2024![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)6min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbae4c1082f68faaec7a9f_unnamed--3-.png)***Editor&#x27;s Note: we&#x27;re EXTREMELY excited to highlight this research from Ankush Garg and Shreya Shankar from Berkeley. At LangChain, two of the biggest problems we think about are evals and agents, and this research sits right at the intersection. You can try it out today in their Python package.***

***TLDR: It helps you find underperforming nodes in LLM chains.***

## The problem it solves

Building LLM-powered applications is challenging, and the complexity multiplies with LLM chains that can have multiple LLM calls per query.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbae4d1082f68faaec7aa7_AD_4nXc7CiW2_1eGDZkhzhJ6HXLKZCz0YuRJuMZAVo5C7Snxwjm-HAl-B066F_-pz7o7xTUlozRwQ6EWP7WD8Td62lsoBKyZzrZ62Pta_Tdre8n9G99uYXwnKJk8obs8gmuEaCMxFFm86QNqhQ1oHgpuZP_HXPYd.png)

While assessing the final outputs is critical in ensuring AI applications are working as designed, assessing intermediate outputs is largely ignored. This is most likely due to resource constraints applications developers may have.

A single node in an LLM chain can cause the entire chain to malfunction, causing a ripple effect, making it difficult to debug and fix.

In this post, we introduce [SCIPE](https://github.com/garg-ankush/scipe/tree/main?ref=blog.langchain.com), a lightweight, yet powerful tool that conducts error analysis on LLM chains. This tool can benefit anyone creating applications that rely on LLMs for making decisions and carrying out tasks.

SCIPE works by analyzing inputs and outputs for each node in the LLM chain and identifying the most important node to fix–the node that, if accuracy is improved, will *most* improve the final or downstream output accuracy.

You can try out SCIPE in our [Colab Notebook](https://colab.research.google.com/drive/1INuL-6cQ-R9z4Clx9L8416ykv6XsRWwg?ref=blog.langchain.com#scrollTo=33z20rSze8CK).

## Technical Details - How it works

SCIPE works by analyzing the failure probabilities of nodes in your application graph to identify the most impactful source of failures. Importantly, it requires *no labeled data* or ground truth examples to perform this analysis. The core problem it addresses is:

**What node’s failures have the biggest impact on the most downstream node’s failures?**

For each node in the application graph, SCIPE models two distinct types of failures that can occur:

- **Independent Failures**: These occur when the node itself (or the LLM processing it) may be the primary cause of the failure (i.e., the node fails even though its upstream dependencies are correct).
- **Dependent Failures**: These happen when a node fails while one or more of its upstream dependencies have failed.

To detect these failures without requiring ground truth data, SCIPE uses an LLM as a judge to evaluate each node in the graph.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbae4d1082f68faaec7ab1_AD_4nXdhpc4RkPyUPqW_C63kvho-BAoBHiLXdY8baJgLt5JRtZW04jlTSVjh5Ca9S-Yt81zwI-ZOLBEAAA2ay8RWzCXZQaWlE34RSei_Hgv8n5WiVutyW68DlU0rEWbPTJ-BnsVw1gOtIiLZU8gV_iEE7jnObkEf.png)

This evaluation process creates a pass/fail score for each node, for each of its input and output pairs. The LLM judge then determines whether each node&#x27;s output is valid given its input, generating a comprehensive dataset of node evaluations across multiple samples. This dataset is used to calculate conditional and independent failure probabilities to find problematic nodes.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbae4d1082f68faaec7aab_AD_4nXfXCLvf4Lbz37c986AgXHFUA1Z77nr-_dzFflofFf_NWQ9ba932IsBsiFr4gw1R1lSHNfjD9EFrEkp1qOxe4U65qC3ZtVe6dTsCmWAR108uf64iPIsos5I9xwnPZ4fh6QMZ7T-16E9_T8rLBM0J6Q2RCE_-.png)

Starting from the most downstream node, SCIPE computes conditional failure probabilities to understand how each node&#x27;s failures relate to its dependencies&#x27; failures. Conditional failure probability is the node failure rate while its dependency (parent node) is also failing.

If a node has no dependencies or its independent failure probability is highest among its local neighborhood, it&#x27;s identified as a potential root cause, ending the analysis. Otherwise, the analysis continues recursively traversing upstream through the graph until the true root cause is identified–the node whose failures are most likely independent (originating from itself rather than being propagated from its dependencies).

To illustrate, here&#x27;s high-level pseudocode on how SCIPE finds problematic nodes.

`function find_root_cause(node, data, graph):
    calculate probabilities for node (overall, independent, and dependent)
    if node has no dependencies or independent failure probability is highest:
        mark node as root cause
        return node
    else:
        find dependency with highest conditional failure probability
        recursively call find_root_cause on that dependency

function find_problematic_node(data, graph):
    identify the most downstream node in the graph
    root_cause = find_root_cause(downstream_node, data, graph)
    calculate probabilities for all nodes in the graph
    construct debug trace from downstream node to root cause
    return EvaluationResult(root_cause, debug_path, node_results)
`

## Getting Started: Prerequisites

If you are using SCIPE on your own application, you’ll need the following:

### Graph

A compiled graph from [Langgraph](https://langchain-ai.github.io/langgraph/?ref=blog.langchain.com). We need to access the internal graph structure to run SCIPE.

### Application Responses

We need prompts and LLM responses for all the nodes in our application as a dataframe. We need this to run validations on and to identify nodes that fail at the highest rate.

Each row of the application responses dataframe is a single user query that cascades through the entire LLM Graph. Here are a couple of example rows of the applications&#x27; input/output responses dataframe.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbae4d1082f68faaec7aae_AD_4nXeYFItB3-zjNjfpeTjNEvP2snw0wHKUjYWDB3b9jshU1wxlVfuPa1BzF1mfBNLizS79FUZiYkDJKyW4pMn7QESCfV8XwbrI1WfJ6FwcMy-pWSEHtJaZTkOQEoWb74eWEJoStlhASv1TF3VELVKQ9MCDgkle.png)

In this example, we have two rows of the dataframe with 3 LLM calls, each responsible for a single step.

- Redact PII
- Extract useful information
- Summarize the chat

### Configs

- PATH_TO_SAVE_VALIDATIONS - Path for saving the LLM as a judge responses
- MODEL_NAME - Model to be used here. We support all the models supported by [LiteLLM](https://docs.litellm.ai/docs/providers?ref=blog.langchain.com)
- node_input_output_mappings - This creates the relationship between the application graph and the application responses.

Once we have application responses, a compiled graph, and have set up our configuration file, we’re ready to run validations and find the nodes with a high failure rate.

## Example: How to use SCIPE

SCIPE uses a compiled StateGraph from LangGraph , which we’ll convert into a lightweight format by using convert_edges_to_dag function.

`from scipe.middleware import convert_edges_to_dag

# Convert a compiled langgraph into a lightweight dag
converted_graph = convert_edges_to_dag(graph=graph)`

Define configs for the evaluator.

`config = {
 PATH_TO_SAVE_VALIDATIONS’: ‘validations.csv’,
 ‘MODEL_NAME’: ‘claude-3-5-sonnet-20240620’,
 # Input and Output mappings for SCIPE
 ‘node_input_output_mappings’: {
    ‘pii_agent’: [‘pii_agent_input’, ‘pii_agent_output’],
    ‘extractor’:[‘extractor_input’, ‘extractor_output’],
    ‘Summarizer’: [‘summarizer_input’, ‘summarizer_output’]
  }
}
`

We can then import LLMEvaluator from scipe and instantiate an object by passing in config, responses (application responses), and the graph we converted.

`from scipe import LLMEvaluator

evaluator = LLMEvaluator(
  config=config,
  responses=application_responses, # DataFrame input/output pairs
  graph=converted_graph # Converted Langgraph
)`

 LLMEvaluator simplifies managing/running LLM-based evaluations on the application responses, and then finding problematic nodes in the application graph. First, it constructs input and output pairs from application responses based on the node_input_output_mappings in configs. Then, it runs validations using an LLM as Judge and saves the validations to the PATH_TO_SAVE_VALIDATIONS in the config.

`results = evaluator.run_validation(
        special_instructions=None
).find_problematic_node()
`

Note: The run_validation method can take in special_instructions, that we might want to pass to the LLM judge. These instructions will be appended to the LLM judge prompt that SCIPE uses internally.

The find_problematic_node() method traverses through the graph to figure out which node has the highest failure rate. Once it finds the problematic node, the algorithm stops and returns the result.

The output is an EvaluationResult which contains the root cause, the debug path (from terminal node backwards), and the failure rate for each node.

You can look at the results of the algorithm by converting the results to JSON.

`results.to_json()Output:

{&#x27;root_cause&#x27;: &#x27;pii_agent&#x27;,
 &#x27;debug_path&#x27;: [&#x27;summarizer&#x27;, &#x27;extractor&#x27;, &#x27;pii_agent&#x27;],
 &#x27;node_results&#x27;: {&#x27;summarizer&#x27;: {&#x27;overall_failure_probability&#x27;: 1.0,
   &#x27;independent_failure_probability&#x27;: 0.0,
   &#x27;conditional_failure_probabilities&#x27;: {&#x27;extractor&#x27;: 1.0},
   &#x27;dependencies&#x27;: [&#x27;extractor&#x27;],
   &#x27;is_root_cause&#x27;: False},
  &#x27;extractor&#x27;: {&#x27;overall_failure_probability&#x27;: 1.0,
   &#x27;independent_failure_probability&#x27;: 0.0,
   &#x27;conditional_failure_probabilities&#x27;: {&#x27;pii_agent&#x27;: 1.0},
   &#x27;dependencies&#x27;: [&#x27;pii_agent&#x27;],
   &#x27;is_root_cause&#x27;: False},
  &#x27;pii_agent&#x27;: {&#x27;overall_failure_probability&#x27;: 1.0,
   &#x27;independent_failure_probability&#x27;: 1.0,
   &#x27;conditional_failure_probabilities&#x27;: {},
   &#x27;dependencies&#x27;: [],
   &#x27;is_root_cause&#x27;: True}}}
`

Application developers can use the failure probabilities of problematic nodes up the LLM chain to further explore what’s causing this node to fail and what can be done to fix it. The results output here tell us that the pii_agent node is the root cause, failing independently at a higher rate compared to other nodes and should be fixed/improved upon.

## Conclusion

In conclusion, SCIPE analyzes independent and dependent failure probabilities to identify the most impactful problematic node in the system. This helps developers pinpoint and fix issues in their LLM-based application graph, improving overall performance and reliability.

We&#x27;re actively developing SCIPE and would love to hear from you! If you&#x27;re interested in participating in our user study, have feedback on the tool, or want to stay updated on future developments, please email us at ankush-garg@berkeley.edu.

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cb92b0ec45aa6d7bc39a91_KEnsho.png)Case StudiesLangGraphObservability &amp; Evals

#### How Kensho built a multi-agent framework with LangGraph to solve trusted financial data retrieval

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamMarch 26, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/customers-kensho)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cb92b9f48cfd92b76f4795_Nullframe-Moda.png)Case StudiesDeep AgentsDeployment

#### How Moda Builds Production-Grade AI Design Agents with Deep Agents

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamMarch 24, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)6min[](/blog/how-moda-builds-production-grade-ai-design-agents-with-deep-agents)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cb92becc1b0764b5d200f1_agent-identity-banner.png)Harrison&#x27;s In the LoopDeploymentAgent Architecture

#### Two different types of agent authorization

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcedd2eda55edd2cc8a271_Harrison.png)Harrison ChaseMarch 23, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/two-different-types-of-agent-authorization)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)