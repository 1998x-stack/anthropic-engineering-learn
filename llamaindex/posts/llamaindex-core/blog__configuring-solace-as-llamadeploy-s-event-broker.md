---
title: "Solace Event Broker Setup for LlamaDeploy | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/configuring-solace-as-llamadeploy-s-event-broker"
category: "llamaindex-core"
---

Content



- [ LlamaDeploy’s Event-Driven Advantage  ](#llamadeploys-event-driven-advantage)
- [ Solace: proven in production  ](#solace-proven-in-production)
- [ Got 10 minutes? Get going with LlamaDeploy and Solace Event Mesh.  ](#got-10-minutes-get-going-with-llamadeploy-and-solace-event-mesh)



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







 Today’s AI is much more than proof of concepts and helpful GenAI tools that help developers code and writers write. Companies are implementing business-critical solutions in areas such as fraud detection, process automation, and front-line customer relationship management.



 But how do these valuable use cases make it into production in a way that’s reliable, secure, and integrates applications across your enterprise? One powerful way is combining Solace and LlamaDeploy:


-  Solace provides an industry-leading event-driven integration and streaming platform that connects your applications, devices and people with real-time information using an interconnected network of event brokers called an event mesh.
  -  LlamaDeploy (formerly llama-agents) is an async-first framework for deploying, scaling, and productionizing agentic multi-service systems based on workflows from LlamaIndex.



 As of today, the Solace platform is fully integrated with LlamaDeploy, [which means you can create an AI-ready event mesh in 10 minutes](https://github.com/run-llama/llama_deploy/tree/main/examples/message-queue-integrations).



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



##  LlamaDeploy’s Event-Driven Advantage



 As described in the [documentation](https://docs.llamaindex.ai/en/stable/module_guides/llama_deploy/), LlamaDeploy easily transitions something that you built in a notebook to a production-ready service—&quot;with the minimum amount of changes to the original code, possibly zero.” To pull off this transition, LlamaDeploy relies on an API server to expose the agents to end users. But more importantly, LlamaDeploy uses asynchronous events to move information between AI agents, which offers huge gains in reliability, speed and ease of deployment. For more information on LlamaDeploy’s architecture, [check out this introductory post](https://www.llamaindex.ai/blog/introducing-llama-deploy-a-microservice-based-way-to-deploy-llamaindex-workflows).



 Even better, LlamaDeploy lets you choose which event broker to use for its asynchronous event distribution amongst agents. Existing options include Kafka, Redis, Rocket MQ…and now the Solace platform.

  ![](https://cdn.sanity.io/images/7m9jw85w/production/287b4e2fac8eb0d69aaac84113da5674ff6b8db6-668x842.png)

##  Solace: proven in production



 So, given a choice between event brokers, why choose Solace? Over twenty years, we’ve honed our solution into a rock-solid real-time information platform that distributes data across diverse systems, environments and geographies more effectively and efficiently than any other broker by letting you build an event mesh.



 You create an event mesh with Solace by deploying our event brokers in any/all your environments (public/private clouds, on premises), and then connecting them, at which point all applications, microservices, cloud services, SaaS, iPaaS and legacy systems connected to any event broker in the mesh will be instantly and continuously connected with one another.



 PubSub+ features:


-  **Sophisticated, Automated Routing:** Smart topics, with support for hierarchy and wildcards, make it easy to make sure data gets exactly – and only – where it’s needed. The event mesh ensures that information gets where it needs to be, and only where it needs to be, across all brokers.
  -  **Enterprise-level scalability and reliability:** Solace is trusted for mission-critical applications by many of the world’s biggest banks, stock markets, telcos, and transportation companies including airlines and aviation agencies like the FAA. They trust our guaranteed message delivery, built-in disaster recovery and class-leading observability with OpenTelemetry to run their businesses.
  -  **Commitment to openness and flexibility:** Solace embraces open standards like AsyncAPI, AMQP, JMS, MQTT, OpenTelemetry, and REST. That means a wide variety of options for connectivity and observability. And being cloud agnostic means that you aren’t locked into a single cloud provider or AI model--your events can flow between cloud, edge and on-premises environments anywhere in the world.
  -  **Rock-solid security: **Every event is locked down by default for security, and the platform provides self-service access to developers, and automatically provisions necessary infrastructure on demand.



 For more information on the advantages of building an event mesh with Solace, check out [From Silos to Symphony](https://solace.com/solutions/initiative/event-mesh/).



##  Got 10 minutes? Get going with LlamaDeploy and Solace Event Mesh.



 Combining Solace’s platform and LlamaDeploy means having a broker that can run anywhere, connect to anything with a platform that manages the details. That means you can focus on solving real problems with LlamaDeploy and not on data movement and integration. Want to see how to do it? Get up and running in about 10 minutes with the [quick start guide](https://github.com/run-llama/llama_deploy/tree/main/examples/message-queue-integrations).