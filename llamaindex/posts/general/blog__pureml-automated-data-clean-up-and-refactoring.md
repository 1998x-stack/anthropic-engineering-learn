---
title: "Automated Data Cleaning Guide: PureML Overview | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/pureml-automated-data-clean-up-and-refactoring"
category: "general"
---

Content



- [ Method of Operation  ](#method-of-operation)
- [ Under the Hood  ](#under-the-hood)
- [ Future Considerations  ](#future-considerations)



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







 *This is a guest post by the PureML team, one of the winners of [our recent hackathon](https://www.llamaindex.ai/blog/agentic-rag-a-thon-2-winners-and-recap).*



 **



 In the process of building machine learning models, ML engineers and their teams often face the tedious and costly task of data cleaning—a critical step that demands considerable time and resources. When interns who help with this effort head back to school in the fall, the need for efficient, scalable solutions becomes even more apparent. This challenge inspired the development of PureML, a proof of concept created at the Agentic RAG-A-THON, designed to deploy AI agents that can streamline and automate data cleaning tasks reducing cost and improving model accuracy.







 **Proof of Concept Use Cases**



 When the team first met, they recognized the unique nature of the challenge. However, as Johann West explained, this is a real-world problem with a clear opportunity for innovation. With a focus on automotive applications, where vast amounts of car data require cleaning, the team set out to address three key use cases within this proof of concept (POC):



 1) Context-Aware Null Handling



 We leveraged an agentic RAG (Retrieval-Augmented Generation) system to enhance accuracy and avoid the pitfalls of imputing missing data with averages. By integrating Generative AI, we aimed to streamline and elevate the AI development process. Here’s a simplified example:

  ![](https://cdn.sanity.io/images/7m9jw85w/production/dfa81e7659bf67c804ccf520e9f3fb798bd8c26d-1380x334.png)

 2) Intelligent Feature Creation



 Missing a feature in your data? PureML can work with your dataset as it is, intelligently generating new features from the row-level context. For example, in this case, PureML automatically adds the country where each vehicle was manufactured, enriching the dataset with valuable, contextual information.

  ![](https://cdn.sanity.io/images/7m9jw85w/production/ad55cc7092286fc3b874978ee83627ddca676333-446x332.png)

 3) Data Consolidation



 Clean data isn’t a guarantee, but PureML addresses this by consolidating synonymous categories, ensuring consistency across the dataset. After all, a ‘Chevy’ should be recognized as a ‘Chevrolet.

  ![](https://cdn.sanity.io/images/7m9jw85w/production/e9382548cd490a2b0d19540f55638fc3e07d9f6c-310x332.png)

##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



##  Method of Operation



 Here’s how it works: the ML Engineer begins by loading the PureML web application and selecting the dataset they wish to clean. Next, they choose the relevant supporting content to build the RAG (Retrieval-Augmented Generation) system, which will drive the data cleaning process.

  ![](https://cdn.sanity.io/images/7m9jw85w/production/189f8a54158a95fb5e039870a4a3ce994c252ea0-1999x1135.png)

 Once the data is ingested, the ML Engineer can choose from one of three operations and monitor the results in real time.

  ![](https://cdn.sanity.io/images/7m9jw85w/production/4b4dbe56cde4e76774d9d0e7a044843b3ed1d4d7-1999x1135.png)

 Upon completion, the ML Engineer can run AutoML to obtain quantitative insights into the effectiveness of the data cleaning process.

  ![](https://cdn.sanity.io/images/7m9jw85w/production/0d75451a7133954403d30c78c69bcf35f76b15f5-1999x1135.png)

##  Under the Hood



 Let’s take a look under the hood.

  ![](https://cdn.sanity.io/images/7m9jw85w/production/a9fe9a0d9dd312d9cc75917782c51ed664d2b282-1788x1090.png)

 Starting with the data, the ML Engineer has a dataset in need of cleaning—in this case, collected automotive data. The next step is selecting files to create the RAG (Retrieval-Augmented Generation) system. After researching available sources, the team gathered relevant automotive data by running a script to create PDFs from the Kaggle dataset Car Specification Dataset 1945-2020 and stored them in Box as the repository for these supporting files.







 Given the complexity of these PDF files, they are difficult to use directly. As part of the ETL (Extract, Transform, Load) process in PureML, the team utilized LlamaParse, a component of LlamaParse, to transform these files into markdown format. This was then saved in the Pinecone Vector Database, facilitating improved retrieval for the first two use cases. The RAG system relies on OpenAI’s GPT-4 as its foundational model.







 However, a basic RAG setup may fall short; single-shot RAG retrievals may not yield the ideal results, and there’s often a need for internet-based searches as well. This is where an agentic RAG system, equipped with multiple tools, becomes essential.







 Unlike a simple chatbot, this isn’t a question-and-answer interface. The agentic system is optimized for generating reports, though instead of producing a blog post, the resulting artifact here is a cleaned dataset.







 This solution requires more than one agent, as each use case is unique. Implemented through LlamaIndex Workflow, the framework offers an event-driven approach, where steps in the process are triggered by specific emitted events.







 The user experience was crafted using Reflex, a unique web application framework. Once mastered, Reflex enables the creation of effective, seamless flows tailored to these use cases. We quickly went from beginners to experts, and this skillful use of Reflex earned the award for ‘Best Use of Reflex” at the hackathon.




##  Future Considerations



 Hackathons are fast-paced, and sometimes planned features don’t make it into the demo. In this case, our experiment and evaluation phase with VESSL and Arize Phoenix had to be cut. We also didn’t have a chance to use Llama Deploy, where our agents will be operating as microservices.







 Clean data is essential beyond model development; RAG systems with supporting data have potential applications across various business processes, where they can significantly reduce the time spent on manual searches.







 In discussions with data scientists and researchers, there’s clear interest in our project. The team is committed to making continuous improvements, exploring additional use cases for model development, and seeking new applications. We welcome conversations with interested parties, especially those who may be interested in investing in our project. Please reach out if you’d like to learn more: you can find us on [X](https://x.com/pureml_io) and on [LinkedIn](https://www.linkedin.com/company/pureml-io/).