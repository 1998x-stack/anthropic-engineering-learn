---
title: "Groq's Compound AI Systems Are Powered by E2B"
author: "Tereza Tizkova"
date: "2025-05-20"
url: "https://e2b.dev/blog/groqs-compound-ai-models-are-powered-by-e2b"
category: "integrations"
site: "e2b"
---

In April 2025, Groq [launched Compound Beta](https://groq.com/now-in-preview-groqs-first-compound-ai-system/), its first compound AI system that combines LLMs with the ability to search the web and execute code. Behind this advancement is E2B's AI infrastructure. It enables Groq to securely run code execution at scale while maintaining their renowned speed advantage.

Compound Beta represents a significant leap forward in AI systems that can take action beyond just generating text. By integrating E2B's secure code execution environment, Groq has built a system that combines the reasoning abilities of large language models with real-world interaction capabilities.

## **Building a Complex AI System**

For AI to solve real-world problems effectively, it needs to do more than predict the next token in a sequence. It needs to access up-to-date information, perform calculations, and interact with external data sources.

Compound Beta uses iterative, server-side tool execution to answer complex queries. The system can autonomously decide when and how to use tools such as web search and code execution, potentially running them multiple times before returning a response. This allows it to handle tasks that require both reasoning and real-time data processing:

- Searching the web for current information
- Running and validating code for computations and data analysis
- Returning grounded answers using live information or logical reasoning.

## **E2B: The Engine Behind Groq's Code Execution**

When Groq set out to build Compound, they needed a solution for code execution that would maintain their performance edge while ensuring security and reliability. E2B's sandbox environment proved to be the perfect fit.

> "We needed a fast, secure, and scalable way to let Compound Beta execute code. E2B was the obvious choice. E2B’s impressive API interface made their sandbox infrastructure require minimal effort to integrate, and their team has been incredibly responsive. They are truly invested in our success."

- Benjamin Klieger, Compound AI Lead at Groq 

‍

Under the hood, E2B uses Firecracker microVMs—lightweight virtual machines that provide complete isolation for running untrusted code. For Groq, this means:

- **Security**: Each piece of code runs in a fully isolated environment, preventing any potential security risks
- **Speed**: E2B sandboxes start up quickly maintaining Groq's performance advantage
- **Scalability**: The AI system scales seamlessly to handle thousands of concurrent requests
- **Reliability**: Consistent execution environment ensures predictable results

> "E2B was the only solution that could match our requirements for both security and speed. The fast sandbox startup time was a game-changer for us."

- Benjamin Klieger, Compound AI Lead at Groq 

‍

Groq's implementation of E2B for Compound Beta focused on three key aspects:

- **Seamless API Integration**: The team integrated E2B's code execution capabilities as a new module directly into their existing infrastructure, allowing developers to access LLMs with server-side code execution with just a simple model name change.
- **Advanced Orchestration**: Groq developed sophisticated orchestration systems that decide when and how to use code execution versus web search, with full control over tool selection.
- **Performance Optimization**: The team worked to ensure the entire pipeline, from initial request to final response, maintained Groq's industry-leading performance standards.

## **Why Groq Chose E2B Over Alternatives**

The Groq team evaluated several options for code execution before selecting E2B:

- **Docker containers** were too slow to spin up, adding significant latency to responses
- **Custom solutions** would have required months of engineering time and ongoing maintenance

E2B offered the right balance of security, performance, and developer experience. The solution's focus on AI-specific use cases made it particularly well-suited for Compound Beta's requirements.

## **Results and Future Plans**

Since launching in April 2025, Compound Beta has demonstrated impressive performance. On Groq's RealtimeEval benchmark, designed to measure search and computation capabilities on current events and live data, Compound Beta outperformed competing solutions from major providers.

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/68235870ad6094ae252cbc41_AD_4nXedT95Go7EyshDx1Ll5jkoP_RbynGSn4evGb1SuTt4VpOFYZ9GiHFj_RAjgr8XfLY5kihMCGg899kt-pdOhq2PuP0yFLNhGEq_0ZVa1yt7z4p3FK9qiC5P2k5RPpDwSTtS7Hd3lbQ.png)

Looking ahead, Groq plans to expand Compound's capabilities with additional tools and improved orchestration. The team is also exploring more advanced use cases that leverage E2B's sandbox technology:

- **Extended persistence**: Allowing users to maintain state across multiple interactions
- **Multi-language support**: Expanding beyond Python to additional programming languages
- **Filesystem interactions**: Supporting more complex workflows involving file manipulations

## **Learn more**

- [Groq Compound Beta launch post](https://groq.com/now-in-preview-groqs-first-compound-ai-system/)
- [Compound Beta documentation](https://console.groq.com/docs/agentic-tooling/compound-beta)
- [Groq's RealtimeEval benchmark](https://github.com/groq/realtime-eval)