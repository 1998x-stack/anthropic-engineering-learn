---
title: "Lindy Powers AI Workflows With E2B Code Action"
author: "Tereza Tizkova"
date: "2025-05-19"
url: "https://e2b.dev/blog/lindy-powers-ai-workflows-with-e2b-code-action"
category: "integrations"
site: "e2b"
---

Lindy AI, the workflow automation platform, recently launched their highly requested power-user feature: custom Python and JavaScript code execution directly within workflows. Behind this new capability is E2B's secure code execution infrastructure, allowing Lindy users to run custom code safely without leaving their automation environment.

This integration represents a significant advancement in no-code/low-code platforms, bridging the gap between visual workflow builders and the flexibility of custom code. By partnering with E2B, Lindy has empowered its users to tackle more complex automation challenges while maintaining the platform's user-friendly approach.

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6825f10fd225a6c213813ff2_AD_4nXfGvYAvvC8wpEfuPuy_YwTwKjTph3UEOGhDYF2ubg7PyKHpUwbVUEYJL0AEwCDa9PK__HJlH3VnDwGI074xJWB3nJjyYBr-HUSRUG0YWTIQ2b8WFF2NC76NVgwfh2UPsU33C-l3.png)

## **Adding Code Power to No-Code**

While Lindy's visual workflow builder has enabled thousands of users to automate their work, there was a persistent demand for the ability to execute custom code for more advanced use cases.

> "Before integrating E2B, our users kept hitting the limits of what they could do with purely visual workflows. They needed to manipulate data in specific ways, connect to niche APIs, or implement complex conditional logic that wasn't practical to build into our visual interface."

- Luiz Scheidegger, Head of Engineering at Lindy 

‍

The new Code action feature enables Lindy users to:

- Perform advanced data manipulation and analysis
- Create custom API integrations
- Implement complex conditional logic
- Execute everyday calculations within their workflows

This bridges a critical gap in the platform's capabilities. Now, when users encounter a task that's difficult to achieve with standard actions, they can seamlessly insert custom code without leaving the Lindy environment.

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6825f10ecaff9a4fe8f91b0e_AD_4nXf85cHdRFKyuTQyrnCIHCPGfuEZyXN8MZHWAHWM7fM5s-EsZB4lOe-sRTvvFGioB4XX1zQEAH3OMl7aPIUXF02itayUmFHHVSkOSPlTU05A18oFydhtDWK3zeKL2FizB3kB5_Eo.png)

## **The Security Challenge of User-Generated Code**

Implementing code execution in a production SaaS platform presents significant technical and security challenges. Lindy needed a solution that would:

- Speed of implementation compared to building in-house
- Securely isolate user code to prevent security vulnerabilities
- Scale efficiently to handle thousands of workflow runs
- Start quickly to maintain the responsiveness users expect
- Support both Python and JavaScript, the most requested languages
- Integrate seamlessly with their existing infrastructure

> "We had implemented E2B in a week, needing just a single engineer working on that in spare cycles. Building this in-house would take us a few weeks and require multiple people."

- Luiz Scheidegger, Head of Engineering at Lindy 

‍

## **Integrating E2B for Secure Code Execution**

After evaluating building code support in-house, Lindy chose E2B as the foundation for their Code action feature. In particular, the security and isolation posture of E2B code environments were a very attractive proposition for Lindy. E2B's architecture offers several benefits that were critical for Lindy's implementation:

- **Isolation**: Each code execution runs in its own Firecracker microVM, providing complete isolation from other users and the host system.
- **Fast startup**: E2B sandboxes initialize in approximately 150ms, ensuring that adding code to workflows doesn't introduce noticeable delays.
- **Language support**: Native support for both Python and JavaScript, the two languages most requested by Lindy users.
- **Simple integration**: E2B's API made it straightforward to integrate code execution capabilities into Lindy's existing platform.

Lindy's implementation of the Code action feature focused on maintaining the platform's user-friendly approach while adding powerful new capabilities.

The team designed a simple interface that allows users to:

- Select their preferred programming language (Python or JavaScript)
- Write or paste their code in a syntax-highlighted editor
- Define input variables that connect to other parts of their workflow
- Specify output variables to use the code's results in subsequent steps

> "We spent significant time refining the user experience to make code actions approachable for users with varying levels of programming experience. E2B's reliability allowed us to focus on the UX rather than worrying about the underlying execution environment."

- Luiz Scheidegger, Head of Engineering at Lindy 

‍

Behind the scenes, when a workflow with a Code action runs:

- Lindy prepares the code execution environment using E2B's SDK
- Input variables from previous workflow steps are passed to the sandbox
- The user's code executes in an isolated E2B environment
- Results are captured and passed back to the Lindy workflow engine
- The workflow continues with subsequent actions, potentially using the code's output

## **Customer Impact and Future Plans**

The Code action feature has been in beta for several weeks and is now rolling out to all Lindy users. Initial feedback has been overwhelmingly positive. @ Lindy team: Any user feedback on the Code Action.

The new capability has also expanded Lindy's market appeal:

- Technical users who previously felt limited by no-code tools now have the flexibility they need
- Teams can create more sophisticated workflows without involving developers
- Companies can standardize on Lindy for a wider range of automation needs

Looking ahead, Lindy plans to expand the Code action feature with additional capabilities:

- Allowing AI to help end users write code
- UI optimizations - syntax highlighting and line numbers in the code editor
- The ability for users to install packages

For Lindy's users, this new capability represents a significant expansion of what's possible within the platform. Tasks that previously required custom integrations or external services can now be handled directly within Lindy workflows.

## **Learn more**

- [Lindy ](https://www.lindy.ai/)website
- [E2B integration](https://www.lindy.ai/integrations/e2b)
- [LinkedIn launch post](https://www.linkedin.com/feed/update/urn:li:activity:7323774203596296192/)