---
title: "AutoTranslateDoc: Translate GitHub Docs With LLMs | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/bridging-the-language-gap-in-programming-introducing-autotranslatedoc-ccc93fbcd3a8"
category: "general"
---

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







Author: [Pierre-Loic Doulcet](https://twitter.com/hexapode)

As programmers, we often find ourselves limited by language barriers. Documentation for various programming frameworks and tools is predominantly available in English, and increasingly in languages like Chinese, creating challenges for non-native speakers. I faced similar obstacles in my early programming days, and it was only through community efforts like [traduc.org](https://traduc.org/)’s translation of man pages that I could surmount them.



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



Today, we are excited to unveil a solution to this pervasive issue: [AutoTranslateDoc](https://www.npmjs.com/package/autotranslatedoc), a command-line tool designed to democratize access to technical documentation by breaking down language barriers.

**How AutoTranslateDoc Works**

![](/blog/images/1*-UGTd6bjRYIitb_077_uBw.png)
- Collect the Documentation: The tool connects to GitHub, identifying and downloading .md and .mdx files from any repository.
- Chunk and Prepare: The documentation is then chunked or split for translation.
- Translate Efficiently: Utilizing the power of LLMs like GPT-3.5 and GPT-4, each chunk of documentation is translated accurately.
- Verify and Enhance: The translation is automatically verified, with retranslation if needed, ensuring the highest quality.
- Consolidate: Finally, the chunks are amalgamated back into a cohesive document.

Our initial tests on translating the llamaIndexTS documentation have been highly promising. You can now read our docs in over a dozen languages including [Chinese](https://ts.llamaindex.ai/zh-Hans/), [French](https://ts.llamaindex.ai/fr/), and [Spanish](https://ts.llamaindex.ai/es/)!

**Getting Started**

Install AutoTranslateDoc easily via npm, or clone the repo ([https://github.com/run-llama/automatic-doc-translate](https://github.com/run-llama/automatic-doc-translate)) :

npm install -g autotranslatedocTry it out with run-lama/LlamaIndexTS or your favorite repo! You will need a [GitHub Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) and an [OpenAI API Key](https://platform.openai.com/api-keys) (the tool will prompt you to set these):

# Translate
autotranslatedoc translate run-llama LlamaIndexTS -d apps/docs -l fr#build
autotranslatedoc build run-llama LlamaIndexTS -d apps/docs -l frThis translates the directory `apps/docs` in the GitHub repo `run-llama/LlamaIndexTS`.

**Improving Accuracy and Consistency**

Our commitment to improving translation accuracy led us to innovate in both the translation process and verification methods.

**Strategic Document Splitting:**

We approach translation by dividing each page of the documentation into sections. To provide enhanced context and coherence, each section’s title hierarchy is appended to its respective chunk during translation. This technique ensures that the translated content maintains the original structure and thematic relevance.

**Rigorous Translation Verification:**

Our verification process is designed to rigorously assess the accuracy of translations. We employ several checks on the translated documentation:

- Translation Length Check: We compare the length of the translated text with the original to ensure consistency.
- Title Hierarchy Analysis: We verify that no new sections are inadvertently added in the translation.
- Link Count Validation: The number of hyperlinks is matched against the original to ensure none are missed or added unnecessarily.
- Code Block Accuracy: The presence and correctness of code blocks in the translation are checked against the original document.

These checks address common issues with LLMs, such as hallucination or omission, and prompt retranslation when necessary. This rigorous process significantly enhances the accuracy of our translations. Moreover, we incorporate a unique self-critique feature, where the LLM evaluates its own translation output, further refining the quality.

This dual approach of meticulous chunking and thorough verification ensures that our translations are not only accurate but also contextually relevant, maintaining the integrity and utility of the original documentation.

**Managing Documentation Updates: Keeping Translations Current**

Documentation, by its nature, is a dynamic entity that evolves over time. Recognizing this, we’ve integrated a robust system into AutoDocTranslate to manage documentation updates efficiently.

**Historical Tracking through JSON:**

When translating a repository using our tool, a .json file is generated, chronicling the history of translations. This file is crucial for tracking changes and versions in the documentation. It serves as a foundation for differential translation, a process that identifies and translates only the newly added or modified content. This feature can be accessed through the `autotranslatedoc update` command, streamlining the maintenance of up-to-date translations.

**Future Enhancements:**

We are actively working on enhancing this system with the following features:

**Manual Change Integration:** Recognizing that translations might undergo manual edits post-generation, we are developing functionality to account for these manual changes during updates. This will ensure that any human revisions are retained and only new or altered sections from the source documentation are translated in subsequent updates.

**GUI for Translation Management:** To further simplify the process of translation editing, tracking, and verification, we’re in the early stages of developing a graphical user interface (GUI). This interface will allow users to interact more intuitively with the translations. An experimental version of this feature can be accessed through the `autotranslatedoc serve` command. This GUI will enable users to visually navigate through the translations, make edits, and verify the accuracy of the content more efficiently.

By continually updating and refining these features, AutoDocTranslate aims to stay at the forefront of making technical documentation universally accessible and easy to maintain in multiple languages.

**The Future of Technical Documentation**

AutoDocTranslate is more than a tool; it’s a step towards an inclusive, barrier-free tech world where language is no longer an impediment to learning and growth. We’re excited to see how it empowers programmers across the globe.

Join us in this journey and contribute to a more accessible programming community!