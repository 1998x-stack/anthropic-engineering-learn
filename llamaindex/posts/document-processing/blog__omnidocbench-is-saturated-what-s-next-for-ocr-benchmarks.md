---
title: "OmniDocBench is Saturated, What’s Next for OCR Benchmarks?"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/omnidocbench-is-saturated-what-s-next-for-ocr-benchmarks"
category: "document-processing"
---

Content



- [ Quick Overview  ](#quick-overview)
- [ OmniDocBench is getting saturated  ](#omnidocbench-is-getting-saturated)
- [ OmniDocBench is too rigid in its evaluation metrics  ](#omnidocbench-is-too-rigid-in-its-evaluation-metrics)
- [ What’s Next  ](#whats-next)



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



   9



 We’ve seen a whirlwind of advancements in document OCR VLMs in the past month, from [Deepseek-OCR2](https://github.com/deepseek-ai/DeepSeek-OCR-2) to [PaddleOCR-VL-1.5](https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.5) to [GLM-OCR](https://huggingface.co/zai-org/GLM-OCR). The latest model, GLM-OCR, set a new SOTA benchmark on OmniDocBench v1.5 with 94.6% accuracy, beating not only OSS models but also recent frontier models like Gemini 3 Pro and GPT-5.2.



 [OmniDocBench](https://arxiv.org/abs/2412.07626) has emerged as one of the default benchmarks for evaluating any model on document understanding. Besides the models above, it’s also used in the latest [Gemini](https://blog.google/products-and-platforms/products/gemini/gemini-3/#gemini-3-deep-think) and [Kimi 2.5](https://www.kimi.com/blog/kimi-k2-5.html) releases.



 Yet document parsing is far from a solved problem. Even though the latest models like GLM-OCR are getting very high accuracy scores on OmniDocBench, there is a massive long tail of document edge cases where even the best visual understanding models still fail. The ‘unicorn’ document parsing benchmark metric should challenge the best models and push them to 100% parsing accuracy over any complex document type.



 There are two issues with OmniDocBench:


-  It is getting saturated and the dataset types are a bit too limited/easy
  -  It is too rigid in its evaluation metrics, penalizing innovation in much better, general parsers



 To be clear, I think OmniDocBench has provided significant value as a document benchmark. Before its release, there really wasn’t a good parsing benchmark at all. Even though there has also been [OlmOCR-Bench](https://huggingface.co/datasets/allenai/olmOCR-bench) (which uses binary tests) and [OCR-Bench v2](https://99franklin.github.io/ocrbench_v2/), OmniDocBench remains as one of the only “reference” benchmarks for document understanding.



##  Quick Overview



 [OmniDocBench](https://arxiv.org/abs/2412.07626) (CVPR 2025) is a benchmark published by Ouyang et al. at OpenDataLab back in 2025. Its document dataset spans nine different document sources, ranging from academic papers to textbooks to handwritten notes. Each document contains top-level annotations like layout bounding boxes and reading order, to fine-grained annotations on titles, text paragraphs, and tables. The original curation process has 981 samples, and v1.5 later expanded and adjusted the distribution.



 Its evaluation pipeline consists of a set of continuous heuristics used to evaluate different elements. It uses Normalized Edit Distance for text, Tree-Edit-Distance-based similarity (TEDS) for tables, and Character Detection Matching (CDM) for formulas.



 The overall score is computed as:

  ![](https://cdn.sanity.io/images/7m9jw85w/production/b44fbc59320a9f57a3e21eafbec6c301c8e31f81-1258x158.png)

##  OmniDocBench is getting saturated



 This is self-evident from the extremely high top-line scores from recent models. Both GLM-OCR and PaddleOCR-VL-1.5 have surpassed 94% in accuracy. For comparison, the latest SOTA result from frontier labs is Gemini 3 Pro at 90.3%. From a pure quantitative perspective, additional increases in OmniDocBench could reduce to “edge case fixing” and doesn’t represent “true” improvements in doc parsing accuracy.

  ![](https://cdn.sanity.io/images/7m9jw85w/production/9788b47bf6e86ea3e804634da69ef73e659299cf-3972x2352.jpg) Latest results from GLM-OCR ([tweet](https://x.com/Zai_org/status/2018520052941656385?s=20))

 The biggest reason for this is that the benchmark size is still small relative to the space of real-world documents. Even at [1355 pages](https://www.notion.so/OmniDocBench-is-Saturated-What-s-Next-for-OCR-Benchmarks-2fcdb4b7d41a8000b42bfeacbd838baa?pvs=21), the benchmark covers 9 doc types and misses a lot more complex documents, particularly those relevant to specific domains. This includes complex financial presentations, market research reports, complex legal filings, insurance claims, and intake forms. The benchmark itself heavily weights towards data types like academic papers. It also heavily weights elements like text/tables/formulas, but it ignores other relevant elements like visuals, handwriting, and form fields.



##  OmniDocBench is too rigid in its evaluation metrics



 OmniDocBench uses continuous metrics like BLEU and edit distance to measure similarity between parsed outputs and its ground-truth annotations. The issue with the benchmark evaluation methodology is it tends to punish small, harmless differences like punctuation, spacing, and line breaks. This is both due to the nature of continuous heuristic metrics, and also the fact that there is a “single fixed ground-truth”.

  ![](https://cdn.sanity.io/images/7m9jw85w/production/35ea8850eae40f3279a8005210ab7bf7f9f051ee-1456x1140.png) In this example, LlamaParse outputs the formula table without merged cells. It also outputs the scientific notation in HTML rather than LaTeX format. These are still semantically correct. However the scores are penalized (0.6344 on TEDS, 0.5581 on edit distance)

 This is especially evident in tables. Exact table match failures can occur when the output is functionally equivalent - for instance, the parsed table representation is in HTML and not markdown, or the parsed table representation adds some stylistic tags that the annotations don’t have. Any failure in formatting directly penalizes edit distance metrics.



 Even ignoring the metric itself, the document inputs can oftentimes have “ambiguous” ground-truth representations. For instance, outputting 3 bullet points could be as equally valid as outputting them without bullet points. When two tables are side by side and semantically related, the tables could be joined together or separated. Unfortunately within OmniDocBench there is only one single ground-truth representation. If the document parser outputs any semantically correct representation that’s different than the ground-truth, it is penalized.

  ![](https://cdn.sanity.io/images/7m9jw85w/production/ef9810d7b576ef0c8b350b1e41dffbe067313947-4066x1640.png) Example of a ‘false flag’ from exact match table matching. LlamaParse (right) outputs the source table (left) into two tables. It (correctly) separates the top-left bolded heading into a separate cell. The OmniDocBench outputs a merged table, and joins the top-level heading. Due to the matching algorithm, only one LlamaParse table is matched with the ground-truth; also the table representation are different. This leads LlamaParse outputs having a low TEDS (0.3825) and text edit distance (0.5998).





 Exact match evaluation is *especially* bad for document intelligence in the AI-native era. In a world where agents or humans are processing unstructured text tokens, what matters the most is that the representation is *semantically correct*, not that it has to conform to an exact formatting specification. AI agents don’t care if the parsed output is in HTML or markdown; they don’t care if the text is in bullet points or emdashes. They *will* care if the table rows/columns are misaligned, if diagrams and charts are interpreted incorrectly, and if content is dropped.



 There are many parsers capable of handling much more complex documents in a semantically correct manner than the documents within the OmniDocBench dataset, but they are parsed in an incorrect manner.



##  What’s Next



 We need a good document benchmark that is not only more complex and comprehensive, but also contains an evaluation methodology that rewards general semantic correctness beyond exact match.



 This will lead to models that aren’t hillclimbing edge cases for exact text/table matching, but are encouraged to have better one-shot visual reasoning across any type of document.



 This is a hard problem and we welcome discussion and feedback in this space. If you come across benchmarks or have ideas on document edge cases, we’d love to chat.



 We’re also working on both fast/cheap and accurate parsing models that output semantically correct, easy-to-interpret markdown from even the most complex visual documents, without paying as much attention to exact matching. If you’re looking to scale up your OCR workload in production, come check out [LlamaParse](https://cloud.llamaindex.ai/)!