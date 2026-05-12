---
title: "Cloud Configuration Automation Guide: RAGformation | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/automatically-generating-cloud-configurations-introducing-ragformation"
category: "rag"
---

Content



- [ Problem: Cloud Complexity Hinders Innovation  ](#problem-cloud-complexity-hinders-innovation)
- [ The Winning Solution: An AI-Powered Tool for Tailored Cloud Solutions  ](#the-winning-solution-an-ai-powered-tool-for-tailored-cloud-solutions)
- [ What is RAGformation?  ](#what-is-ragformation)
- [ Key Features and Benefits  ](#key-features-and-benefits)
- [ Impact: Empowering Businesses to Embrace the Cloud  ](#impact-empowering-businesses-to-embrace-the-cloud)
- [ Technology  ](#technology)
- [ How We Built It  ](#how-we-built-it)
- [ Extensions/ Future Work:  ](#extensions-future-work)
- [ A Step Towards Democratizing Cloud Adoption  ](#a-step-towards-democratizing-cloud-adoption)
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







 *This is a guest post from one of the winners of our [recent hackathon](https://www.llamaindex.ai/blog/agentic-rag-a-thon-2-winners-and-recap), [Steve Castellotti](https://www.linkedin.com/in/theprofessionalamateur/) and teammates [Supriya Ramarao Prasanna](https://www.linkedin.com/in/supriya-rp/), [Christen Jacquottet](https://www.linkedin.com/in/christenjacquottet/), [Kevin Tran](https://www.linkedin.com/in/kqtrans/), [Bharat Bhavnasi](https://www.linkedin.com/in/bharatsatya/), [Rushi Chaudhari](https://www.linkedin.com/in/rushichaudhari/), and [Anthony Avendano](https://www.linkedin.com/in/anthony-avendano/)*.







 In today&#39;s fast-paced business environment, companies rely heavily on cloud infrastructure for scalability and rapid innovation. However, the process of selecting appropriate cloud services, estimating costs, and designing architectures can be complex and time-consuming, often taking days or weeks to complete. This complexity poses a significant challenge for enterprises looking to leverage the cloud&#39;s full potential.



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



##  Problem: Cloud Complexity Hinders Innovation



 Businesses face significant challenges navigating the vast landscape of cloud services across providers like AWS, Azure, and Google Cloud. Selecting the right services for specific use cases, accurately estimating costs, and designing optimized architectures require considerable research and specialized knowledge. This complexity often results in deployment delays, slowing innovation and impacting a company’s ability to remain competitive in an evolving market.



##  The Winning Solution: An AI-Powered Tool for Tailored Cloud Solutions



 [**RAGformation**](https://devpost.com/software/ragformation) [1], an innovative project that won the &quot;Box Award&quot; at the [LlamaIndex RAG-a-thon](https://rag-a-thon-2.devpost.com) [2], addresses this challenge by automating the process of cloud service selection, pricing, and architecture design. This AI-powered tool leverages natural language processing and Retrieval Augmented Generation (RAG) to simplify cloud complexity and accelerate innovation.



##  What is RAGformation?



 ​​RAGformation simplifies the process of cloud architecture design by allowing users to describe their specific use case in natural language. Utilizing the robust capabilities of Llama Index Workflows—RAGformation interprets the input and generates a dynamic flow diagram, visually representing the recommended cloud services tailored to the user’s needs.



 In addition to architecture suggestions, the platform provides detailed pricing information for the proposed cloud setup, enabling users to make informed decisions. As users refine their requirements, RAGformation automatically adjusts the flow diagram, offering alternative services and configurations that align with updated preferences. Once the optimal setup is confirmed, RAGformation finalizes the pricing and generates a comprehensive report, providing users with a detailed blueprint of their cloud solution.



##  Key Features and Benefits


-  **Automated Cloud Service Selection:** RAGformation leverages RAG and a vectorized knowledge base stored in Pinecone to identify the most suitable cloud services based on the user&#39;s input. The knowledge base is first loaded into a Box storage repository, with new files being dynamically added to the vector store upon upload.
  -  **Visual Flow Diagram Generation:** The tool automatically creates a flow diagram that visually represents the proposed cloud architecture, making it easy for users to understand and evaluate the solution.
  -  **Detailed Pricing Estimation:** RAGformation provides accurate cost estimates for the entire cloud services setup, enabling users to make informed decisions about their cloud infrastructure.
  -  **Dynamic Recommendation Refinement:** Users can interact with the tool to refine recommendations based on their preferences or budget constraints, ensuring the solution aligns perfectly with their needs.
  -  **Comprehensive Report Generation:** RAGformation generates a detailed report that includes the optimized flow diagram, pricing information, and a summary of the selected cloud services.
  -  **Open Source**: RAGformation is an Open Source solution with code available on [GitHub](https://github.com/RAGformation/RAGformation) [3].



##  Impact: Empowering Businesses to Embrace the Cloud



 By automating and simplifying the cloud service selection process, RAGformation empowers businesses to:


-  **Accelerate Time-to-Deployment:** Eliminating manual research and design processes enables companies to deploy cloud solutions faster, reducing time-to-market and gaining a competitive edge.
  -  **Empower Leadership Decisions:** Providing clear visualizations and accurate cost estimates helps stakeholders make informed decisions about their cloud investments.
  -  **Optimize ROI:** Tailored cloud solutions ensure businesses utilize resources efficiently, avoiding over-provisioning and maximizing the return on their cloud spending.
  -  **Stay Agile and Competitive:** The ability to quickly adapt cloud architectures to changing needs allows companies to remain agile and responsive in a dynamic market.



##  Technology



 Some of the technologies employed by RAGformation include:


-  **LlamaIndex Agent Framework:** This framework, powered by LlamaIndex, enables prompt chaining, integration of various LLM models, and enhanced agentic workflows.
  -  **Box**: Designed to ingest and organize scraped AWS blog architectures, Box allows for the creation of a private, centralized repository of internal architectures used within your organization.
  -  **Toolhouse**: A hub for tools that enable automated code execution, streamlining workflows and reducing manual intervention



 **Standardized User Interface API:** The backend was designed to communicate with the UI through an implementation of the Open AI API for chat competitions endpoint, which means any frontend already designed to work with ChatGPT can be used to communicate with RAGformation. For example, [Urcuchillay Chat](https://github.com/castellotti/urcuchillay-chat) [4]:

  ![](https://cdn.sanity.io/images/7m9jw85w/production/8b019be8ac27ef4f9602625c692f4b4887705f00-1020x832.png)

##  How We Built It

  ![](https://cdn.sanity.io/images/7m9jw85w/production/b4d9037565b2f80a1cda4284955fa82aac5fa370-1024x632.png)

 **1. Data Collection:**


-  Sources for design best practices include blog posts, IEEE papers, and cloud services documentation.
  -  Design documentation is collected and uploaded to a Box repository for automated processing.
  -  A LlamaParse-hosted and Pinecone-backed RAG (Retrieval-Augmented Generation) solution for service suggestion and flow building is used to process the design documentation into the vector store.
  -  Costs are calculated on the fly by utilizing pricing APIs provided by AWS.
  -  Diagram functions are imported for building flow diagrams.



 **2. User Interaction:**


-  The user inputs a use case and confirms the suggested cloud services flow.
  -  Use case information and flow confirmation are collected.
  -  The chat-based system for the user interface allows free-form dialog which can continue prompting the user until all necessary information is complete.
  -  An (optional) Image-to-Text agent receives any diagram sketches from the user (via the concierge agent and orchestrator, see below) to form a more complete design specification.
  -  The user&#39;s budget is used to inform the overall project cost.



 **3. Agent Process:**


-  A LlamaIndex-based orchestrator works with agents to accomplish tasks.
  -  A concierge agent interfaces with the user to collect requirements and ask follow-up questions for clarification and completeness, handing off to the orchestrator.
  -  The orchestrator calls the RAG agent to retrieve cloud services information and diagram imports.
  -  Next, the diagram agent is called to interpret suggested services to build flow diagram(s) by generating the appropriate YAML file(s) in the format expected by the service.
  -  Iteration is performed by the check diagram agent for correctness.
  -  The pricing agent is next in the chain, estimating the price for the suggested cloud flow using the AWS Price List API.
  -  Finally, the reporter agent is called to generate a report of the confirmed flow with diagram(s) and pricing.



 **4. Output Generation:**


-  The output from the reporter agent passes back through the orchestrator to the user, via the concierge agent.
  -  An executive summary is provided, outlining and re-confirming the original requirements.
  -  A PDF version of the flow diagram is presented outlining the generated architecture design.
  -  Key business benefits are highlights based on the user’s requirements and budgetary restraints.
  -  Output is completed with a cost estimation summary that breaks down one-time and recurring costs on a per-component and service basis.







##  Extensions/ Future Work:



 We’re thrilled about the potential for RAGformation. Some ideas include:


-  Open-source models with improved prompts for function calling
  -  Integration with Azure and GCP
  -  Implementing a RAG database with multi-cloud architectures



##  A Step Towards Democratizing Cloud Adoption



 RAGformation represents a significant step towards democratizing cloud adoption by making it easier and faster for businesses of all sizes to leverage the power of the cloud. By automating complex processes, providing valuable insights, and empowering users to make informed decisions, RAGformation enables companies to focus on their core competencies and drive innovation, ultimately shaping the future of cloud infrastructure.

  ![](https://cdn.sanity.io/images/7m9jw85w/production/a5fbbc4db957d79dbe1d605e02aab8924427e31f-1240x768.png)

##  **References**


-  [https://devpost.com/software/ragformation](https://devpost.com/software/ragformation)
  -  [https://rag-a-thon-2.devpost.com](https://rag-a-thon-2.devpost.com)
  -  [https://github.com/RAGformation/RAGformation](https://github.com/RAGformation/RAGformation)
  -  [https://github.com/castellotti/urcuchillay-chat](https://github.com/castellotti/urcuchillay-chat)