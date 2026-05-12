---
title: "Multi-Page Table Parsing &amp; Excel Output Guide | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/new-in-llamaparse-multi-page-tables-beta-and-excel-spreadsheet-output"
category: "document-processing"
---

Content



- [ Continuous Mode (Beta)  ](#continuous-mode-beta)
- [ Excel spreadsheet output  ](#excel-spreadsheet-output)
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







 At LlamaIndex we’re constantly improving LlamaParse, our world-class document parser for complex document formats like PDFs, Word files, Excel spreadsheets, and PowerPoint presentations. We’re always listening to user feedback and looking for new pain points we can resolve. Today we’re excited to launch two new features: Excel file output, and Continuous Mode for multi-page tables.



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



##  Continuous Mode (Beta)



 Our latest innovation addresses the problem of multi-page tables: as Sacha demonstrates in this video, parsing a single table that spans multiple pages used to result in several troublesome issues:


-  The two halves of the table appear as separate tables in the output
  -  Headers present in the table on the first page are not necessarily persisted or correct on subsequent pages
  -  This inconsistency is repeated in the raw JSON output of LlamaParse




 With new Continuous Mode we address this limitation with a single click: just turn it on and tables spanning even dozens of pages can be quickly consolidated into a single easily parsed and manipulated table.



 This feature is in **beta:** we’ve primarily tested on small documents (&lt; 10 pages), with relatively simple formatted tables. It will run a bit slower than our other parsing modes, and may take ~30 minutes to parse a full 80-page 10K report.



##  Excel spreadsheet output



 Another common use-case we’ve observed is parsing tabular data directly into spreadsheet format for manipulation in programs like Microsoft Excel. This is now also just a click away in LlamaParse!



 To access Excel Sheet output, parse your documents in Accurate, Premium, or Continuous Mode. When your document is ready, select the new “XLSX” output format and click the Export button and your Excel file will be automatically downloaded.

  ![](https://cdn.sanity.io/images/7m9jw85w/production/24a02998c474f5e2e035b26fa52aab880bac55c2-2567x1251.png)

 And yes, these two features combine seamlessly! If you parse a giant table in Continuous Mode you can get it as Excel Sheet output.



##  Always improving



 Love these features? [Sign up today](https://cloud.llamaindex.ai/) and start parsing! Want to learn more? [Get in touch](https://www.llamaindex.ai/contact) with us, we’re always listening!