---
title: "LlamaParse Update May 2025: New Models &amp; Skew Fixes | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/llamaparse-update-may-2025-new-models-skew-detection-and-more"
category: "document-processing"
---

Content



- [ New models  ](#new-models)
- [ Automatic orientation and skew detection  ](#automatic-orientation-and-skew-detection)
- [ Confidence Scores  ](#confidence-scores)
- [ Page Error Tolerance  ](#page-error-tolerance)
- [ Replace Failed Page Mode  ](#replace-failed-page-mode)
- [ Always improving  ](#always-improving)



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







 We’re always improving LlamaParse, our industry-leading parser of complex document formats. Here’s a grab-bag of recent new features and quality-of-life improvements that we’ve shipped.



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



##  New models



 We’re constantly expanding the selection of models available for our most advanced, agentic parsing modes. We now support OpenAI’s GPT 4.1 and Google’s Gemini 2.5 Pro. Both have delivered outstanding results in our tests, and can deliver state-of-the-art accuracy when parsing complex documents like PDFs, PowerPoints, and Word documents.

  ![](https://cdn.sanity.io/images/7m9jw85w/production/1ae2e6daeb20a0e3b3a195d6d655a3119c99c671-1323x1045.jpg)    ![](https://cdn.sanity.io/images/7m9jw85w/production/7b33ba2b059f3adb8994f368864860131155ce4f-1844x1263.jpg)

##  Automatic orientation and skew detection



 Parsing your documents can fail completely if the documents have been scanned upside-down or sideways. To avoid that failure mode, pages that are rotated 90º, 180º, or 270º are now automatically detected and parsed at the correct orientation.



 More subtly, slight skews — being off-level by anywhere between 1º and 12º — can also lead to poor parsing results, so we detect these and automatically vertically align them so they can be parsed with the greatest possible accuracy.



 And of course, if both are true — for instance, your document is sideways but also skewed, for a rotation of 93º — we correct both!



 The JSON output of your results contains a new property, `originalOrientationAngle` , that will let you know if this correction has taken place.



##  Confidence Scores



 We now include confidence scores with every parsed page. Here’s how they work:


-  **Text‑only pages:** We compare the original page and Markdown by averaging the character-count ratio, bag-of-letter overlap, and bag-of-words overlap.
  -  **Pages with images:** We run OCR, keep only high‑confidence text, and check how much of it appears in the Markdown to find missing content.



 Confidence Scores go from 0 to 1, where higher is better. Any score below ~0.2 is automatically flagged as low-confidence. You will find these scores in JSON results for all modes except Fast and LVM.



##  Page Error Tolerance



 You can now specify your preferred tolerance for errors in parsed pages, expressed as a number between 0 and 1 representing the error percentage. The `page_error_tolerance`  is the maximum number of pages that can be failed when converting to markdown before failing a job. To use it, set `pageErrorTolerance=&quot;$value&quot;`  when using the API.



##  Replace Failed Page Mode



 If LlamaParse fails to transform a page to Markdown, you now have greater control over how the API will handle this by setting `replace_failed_page_mode=&quot;$value&quot;`  in the API to one of three supported values:


-  `raw_text` : returns the raw text of the page instead of Markdown (this is the default)
  -  `blank_page` : returns a blank page.
  -  `error_message` : returns an error message explaining why page failed.



##  Always improving



 That’s it for our latest updates! LlamaParse is free for 10,000 pages per month, so it’s easy to [log in to LlamaParse](https://cloud.llamaindex.ai/) and get started with your parsing projects.