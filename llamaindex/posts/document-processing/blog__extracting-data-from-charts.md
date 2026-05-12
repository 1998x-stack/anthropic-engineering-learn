---
title: "Extracting Data From Charts: A Step-by-Step Guide"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/extracting-data-from-charts"
category: "document-processing"
---

Content



- [ Why Charts Are a Data Trap  ](#why-charts-are-a-data-trap)
- [ How to Extract Data From Charts: Step by Step  ](#how-to-extract-data-from-charts-step-by-step)
- [ What Makes a Chart Easy or Hard to Extract  ](#what-makes-a-chart-easy-or-hard-to-extract)
- [ Validating the Data You Extract  ](#validating-the-data-you-extract)
- [ Manual, OCR, and AI: Choosing the Right Approach  ](#manual-ocr-and-ai-choosing-the-right-approach)
- [ Where Traditional OCR Hits Its Limit on Charts  ](#where-traditional-ocr-hits-its-limit-on-charts)
- [ When Scale Changes Everything  ](#when-scale-changes-everything)
- [ Stop Recreating Charts by Hand  ](#stop-recreating-charts-by-hand)



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



   20



 You&#39;ve found the exact numbers you need, right there in a bar chart on page 42 of a 200-page PDF. Getting them out is a different problem.



 For years, the answer was to squint at axis lines and type into a spreadsheet. AI has changed what&#39;s possible, but the right approach still depends on what you&#39;re working with, what volume you&#39;re processing, and how much accuracy you need.



 **Chart data extraction** is the process of converting visual data encoded in charts, graphs, and plots into structured, usable numbers, typically rows and columns in a spreadsheet or JSON format. On the surface, it sounds simple, but the extraction method matters.



 This guide walks through each method, why charts are harder to extract than they appear, and where agentic OCR fits in.



##  Why Charts Are a Data Trap



 Charts look simple. A bar reaches a certain height, a line crosses a grid. The data feels obvious. The problem is that charts encode **numerical data** as visual relationships, not as text or structured values. A bar chart doesn&#39;t store the number 47. It stores a rectangle whose height corresponds to 47 on a scale defined by the y-axis.



 Traditional OCR (optical character recognition) reads pixels and recognizes text. It can pull the label &quot;Q3 Revenue&quot; off a chart axis without any trouble, but it can&#39;t connect that label to the height of the adjacent bar, read the scale, and conclude that Q3 Revenue was $142M. That interpretation requires understanding the coordinate system embedded in the **graph image**.



 Manual extraction works fine for a single or a few charts at best. At any real volume, say 50 charts across a quarterly earnings report pack, the math gets ugly fast. Manual chart digitization typically runs 15 to 30 minutes per chart, with error rates that compound when axes are compressed, legends overlap, or resolution is poor. A 3D bar chart introduces perspective distortion that makes visual height estimation unreliable. A pie chart with twelve slices, several under 5% of the total, is nearly impossible to read accurately without access to the underlying data. These are common cases in scanned industry reports and exported PDFs.



 The core challenge is that extracting data from charts is a geometry problem wrapped in a visual interpretation problem, and traditional text-reading tools solve neither.



##  How to Extract Data From Charts: Step by Step



 Understanding this process matters whether you&#39;re doing it manually, evaluating a tool, or debugging why an extraction went wrong. Here is what accurate chart data extraction actually requires:


-  **Identify the graph type.** Whether you’re dealing with a bar, line, pie, scatter, stacked bar, or area chart, each has different extraction logic. A pie chart requires reading arc angles and converting them to percentages. A scatter plot requires mapping individual points to coordinate pairs. Knowing the **graph type** determines every step that follows.
  -  **Parse the axes.** Read the x-axis labels, the y-axis scale and units, and any secondary axes. Note whether the scale is linear or logarithmic, and note where zero is.
  -  **Read the legend.** Map each series, color, or pattern to its label. A stacked bar chart with five series and ambiguous color coding is one of the harder extraction cases you&#39;ll encounter.
  -  **Locate and record each data point.** Map each visual mark (bar height, point position, line vertex) to its coordinate value on the axes. This is where most of the work happens, and where most of the error occurs.
  -  **Export to a structured format.** CSV, JSON, or a table. The goal is **data points** in rows and columns, not a screenshot with annotations.



 This is the same process AI systems replicate, which is why understanding it helps when evaluating how well a given tool actually performs.



###  What Makes a Chart Easy or Hard to Extract



 Not all charts are equal. A clean 2D bar chart with labeled axes, high-resolution source, and a single data series is about as easy as it gets. The hard cases are where most real-world data lives:


-  Low-resolution scans or compressed PDFs
  -  Overlapping data series with similar colors
  -  3D effects that distort bar heights and pie angles
  -  Compressed or unlabeled axes
  -  Small-slice pie charts where angles are nearly indistinguishable
  -  Stacked bars requiring cumulative value calculation



 The graph type matters significantly here**.** Line charts with multiple series require tracking each series independently across the x-axis. Scatter plots may have hundreds of individual points. Stacked bar charts require subtracting values to recover per-series data.



###  Validating the Data You Extract



 Spot-checking extracted data is not optional, especially if downstream decisions depend on it. A few verification steps that catch the most common errors:


-  Do totals add up? A stacked bar chart&#39;s segments should sum to the bar&#39;s total height.
  -  Do extracted values match any numbers mentioned in the surrounding text?
  -  Does the trend make sense relative to adjacent charts in the same report?
  -  Keep a reference back to the source **graph image** for each extracted value so discrepancies can be traced.



 At scale, this validation step is where manual methods fail. Checking 500 data points against 50 source charts is its own full-time job.



##  Manual, OCR, and AI: Choosing the Right Approach



 Three methods exist, each with real trade-offs:




      Method
      Accuracy
      Speed
      Scale
      Output Format
      Validation




      Manual
      High (single chart)
      15-30 min/chart
      Fails at volume
      Whatever you type
      Human judgment only


      Traditional OCR
      Text labels only
      Fast
      Scales for text
      Structured text
      Cannot validate missing values


      AI/VLM (e.g., LlamaParse)
      High across chart types
      Fast
      Scales
      CSV, JSON, Markdown
      Confidence scores, citations



 **Manual extraction** makes sense when you have one chart, you need to verify something quickly, or the chart is unusual enough that automation would require significant custom work. It doesn&#39;t scale.



 **Traditional OCR** can read axis labels, titles, and any text embedded in a chart. It can tell you the chart says &quot;Revenue ($M)&quot; and that the x-axis labels say &quot;Q1, Q2, Q3, Q4.&quot; It can&#39;t *automatically extract* the underlying values, because those are encoded as visual geometry, not text. This is a fundamental limit of character-recognition tools applied to image-based data.



 **AI and vision-language model (VLM) approaches** read the entire graph image as a whole. They understand spatial encoding: the relationship between bar height and axis scale, the meaning of color coding in a legend, the approximate value of each point in a scatter plot. This is where actual automation becomes possible at volume.



 Cost matters too. Manual extraction eats analyst time and scales badly. Traditional OCR is cheap per document but leaves the actual data extraction to a human, which erases the savings. VLM-based tools cost more per document than simple character recognition but avoid the downstream labor of manual correction and the risk of missing data entirely.



 The right choice depends on what you&#39;re actually dealing with. One chart: manual is fine. Simple, text-heavy charts in bulk: OCR handles the text layer, but you still need a human for the values. Complex charts at any volume: AI.



##  Where Traditional OCR Hits Its Limit on Charts



 Traditional OCR was designed to recognize characters. Tools like Tesseract and AWS Textract do this well. The problem is that a bar chart&#39;s data isn&#39;t stored as characters. The number 142 doesn&#39;t appear anywhere in the image file. It exists only as the height of a rectangle relative to a scale defined by the y-axis. Better character recognition doesn&#39;t close that gap, because text recognition and visual data interpretation are solving different problems.



 [LlamaParse](https://www.llamaindex.ai/llamaparse)&#39;s agentic approach handles this differently. Rather than treating a document as a text extraction problem, it processes text, tables, images, and charts through the same multi-modal pipeline. For charts, this means reconstructing actual data values from visual reasoning, not just pulling axis labels.



 The result is that when you run a financial report through [LlamaParse](https://www.llamaindex.ai/llamaparse), you get the chart data out as structured values alongside the surrounding text, in Markdown, JSON, or HTML, without needing a separate chart-extraction tool bolted onto your pipeline. LlamaParse handles the document as a whole. It also applies self-correction loops as part of its agentic pipeline, checking extracted values for internal consistency and flagging outputs that fall outside the range defined by the axis. That verification step is what makes the results auditable and fast.



 Where traditional OCR stops at axis labels, [LlamaParse](https://www.llamaindex.ai/llamaparse) reconstructs the actual data values through visual reasoning, outputting the numbers behind the bars and lines as structured data. That difference matters for any workflow where charts are a meaningful source of information.



##  When Scale Changes Everything



 Processing one chart manually is fine. Processing 50 charts across a quarterly earnings report pack, or pulling data from a hundred competitor filings each containing fifteen or more charts, requires automation that most document pipelines don&#39;t currently have.



 The scenarios where scale forces the issue:


-  **Financial analysts** building market models from industry reports, pulling revenue, margin, and volume data across dozens of company filings where the underlying numbers live in charts, not tables
  -  **Insurance assessors** processing claim documents where embedded charts document loss history or actuarial projections
  -  **Researchers** aggregating competitor data across analyst reports and trade publications
  -  **Legal teams** reviewing exhibits that include charts as evidence, where each extracted value needs to be traceable back to a specific page and source image



 At this scale, the requirements change. You need bulk processing across entire document sets, consistent structured output across every chart regardless of type, the ability to **extract data** from every chart without manually identifying each one, and an audit trail linking extracted values back to source pages.



 Manual methods fail on item one. Traditional OCR fails on items two and three. The volume of data locked in charts across PDFs, scanned reports, and presentation decks is large and keeps growing, and most document pipelines have no good answer for it.



##  Stop Recreating Charts by Hand



 More reports, more PDFs, more dashboards screenshotted and embedded in decks: the volume of data locked in chart images is increasing, not shrinking. The question for any team processing documents at scale is whether their pipeline handles charts as part of normal document processing or routes them to a manual step that bottlenecks everything downstream.



 [LlamaParse](https://www.llamaindex.ai/llamaparse) handles charts as part of full document parsing. Multi-modal from the start, not a chart-specific add-on. When a PDF comes in with tables, text, and bar charts, all of it goes through the same pipeline and comes out as structured, AI-ready data in Markdown, JSON, or HTML, with each chart&#39;s extracted values mapped to their source page. No separate workflow for visual data, no stitching three tools together for one document type, and no manual cleanup before the data is usable downstream.



 If you&#39;re processing documents that include charts and currently handling the visual data manually or skipping it entirely, [LlamaParse](https://www.llamaindex.ai/llamaparse) handles charts as part of full document parsing. LlamaCloud is free to try with 10,000 credits on [signup](https://cloud.llamaindex.ai/signup).