---
title: "LlamaSheets: Turn Messy Spreadsheets Into AI-Ready Data | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/announcing-llamasheets-turn-messy-spreadsheets-into-ai-ready-data-beta"
category: "general"
---

Content



- [ Introducing LlamaSheets  ](#introducing-llamasheets)
- [ Technical Approach  ](#technical-approach)
- [ Output Contents and Format  ](#output-contents-and-format)
- [ Use Cases  ](#use-cases)
- [ Example: Extract and Analyze in 5 Lines  ](#example-extract-and-analyze-in-5-lines)
- [ Available now in beta  ](#available-now-in-beta)
- [ What&#39;s Next  ](#whats-next)



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



   51



 Today, we are announcing the first of our dedicated API&#39;s for handling spreadsheets, available today in Beta for free!


-  [LlamaParse Sign-up/Sign-in](http://cloud.llamaindex.ai)
  -  [LlamaSheets Docs](https://developers.llamaindex.ai/python/cloud/llamasheets/getting_started/)



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



##  Introducing LlamaSheets



 Spreadsheets are everywhere. From financial models, product catalogs, and operational reports, spreadsheets exist across a wide range of formats and levels of organization.



 Unlike typical unstructured documents, spreadsheets contain highly structured numerical data, complex formatting, and visual hierarchies that traditional text parsing cannot capture. LLMs and agents need to understand not just the raw cell values, but the semantic relationships, formatting patterns, and hierarchical structure encoded in these documents.



 The challenge is that &quot;messy&quot; spreadsheets often use visual formatting (bold headers, colored cells, merged regions) to convey meaning rather than explicit data structures. Before any AI automation can happen, this normalization step,extracting structured data while preserving semantic context, is critical. That is why we’re so excited today to announce our newest product to LlamaParse, LlamaSheets!



 **LlamaSheets** is a new **LlamaParse API** that automatically structures complex spreadsheets into AI-ready data using semantic understanding. The input is any `.xlsx`  file, and the output is [parquet files](https://parquet.apache.org/) that can be used in any agent or downstream application.



###  **Technical Approach**



 Our processing algorithm implements a sophisticated multi-stage pipeline:


-  **Feature Extraction &amp; Clustering** - 40+ features per cell are extracted (position, formatting, etc.) and are then featurized for clustering
  -  **Intelligent Region Classification** - Clusters are then classified into specific types of regions are classified using a combination of traditional ML techniques and agent-based processing
  -  **Adaptive Table Segmentation** - A scoring system evaluates boundary quality between regions and iteratively refines boundaries
  -  **Hierarchical Structure Preservation** - ****Intelligent extraction within each table is applied that preserves multi-level headers and complex table structures and preserves types where possible (dates, numbers, booleans, text)



###  **Output Contents and Format**



 LlamaSheets produces multiple types of outputs, mostly as parquet files:


-  **Table data**: Clean, typed DataFrames with preserved data types (dates, numbers, strings, booleans). Column names are intelligently extracted from header rows.
  -  **Extra data**: Data in your spreadsheet that doesn&#39;t explicitly belong in a structured data table (notes, titles, etc.)
  -  **Cell metadata**: 40+ features per cell including formatting (`font_bold` , `background_color_rgb` ), position (`row_number` , `coordinate` ), data types (`is_date_like` , `is_percentage` ), and layout (`is_merged_cell` , `horizontal_alignment` )
  -  **Sheet context**: Optional LLM-generated titles and descriptions for each worksheet and extracted table region



###  **Use Cases**



 LlamaSheets enables AI automation across diverse spreadsheet workflows. Here&#39;s just a few examples:


-  [Financial Analysis](https://developers.llamaindex.ai/python/cloud/llamasheets/examples/coding_agent/#workflow-1-understanding-a-new-spreadsheet): Extract quarterly revenue tables from complex financial reports with merged headers and calculate KPIs automatically
  -  [Multi-Region Data Consolidation](https://developers.llamaindex.ai/python/cloud/llamasheets/examples/coding_agent/#workflow-2-generating-analysis-scripts): Parse and combine sales data from dozens of regional spreadsheets with inconsistent formatting
  -  [Budget Parsing with Metadata](https://developers.llamaindex.ai/python/cloud/llamasheets/examples/coding_agent/#workflow-3-using-cell-metadata-to-understand-structure): Use background colors and bold formatting to identify department groupings and category hierarchies in budget files
  -  [Automated Weekly Reports](https://developers.llamaindex.ai/python/cloud/llamasheets/examples/coding_agent/#workflow-4-building-complete-automation): Build end-to-end pipelines that extract, validate, analyze, and generate reports from recurring spreadsheet uploads
  -  [Custom Agent Integrations](https://developers.llamaindex.ai/python/cloud/llamasheets/examples/llama_index/): Load extracted Parquet files into AI Agent frameworks (like LlamaIndex) for interactive data exploration, script generation, and more

  ![](https://cdn.sanity.io/images/7m9jw85w/production/4fd5e1ee933d15cccdbffa75b713bccf5f061722-2922x1792.png)

###  **Example: Extract and Analyze in 5 Lines**



python






```
from llama_cloud_services.beta.sheets import LlamaSheets

client = LlamaSheets(api_key="llx-...")
results = await client.aextract_regions("budget.xlsx")

# Download as pandas DataFrame
df = await client.adownload_region_as_dataframe(
  results.job_id,
  results.regions[0].region_id,
  result_type=regions[0].region_type
)

# Access rich cell metadata
metadata = await client.adownload_region_as_dataframe(
  results.job_id,
  results.regions[0].region_id,
  result_type="cell_metadata"
)
```


##  **Available now in beta**

  LlamaSheets is available **today in beta** through multiple interfaces:


-  🧩 **Playground UI:** Experiment with sample spreadsheets directly in the browser at [cloud.llamaindex.ai](http://cloud.llamaindex.ai)
  -  💻 **Python SDK:** The [llama-cloud-services](https://github.com/run-llama/llama_cloud_services) package provides async/sync methods for uploading files, creating extraction jobs, polling for completion, and downloading Parquet results as pandas DataFrames or raw bytes
  -  🌐 **REST API:** [Four-step workflow](https://developers.llamaindex.ai/python/cloud/llamasheets/getting_started/#lower-level-usage) via `/api/v1/beta/sheets/`  endpoints: (1) Upload file → (2) Create job with parsing config → (3) Poll for completion → (4) Download Parquet files via presigned URLs
  -  📘 **Build Agents** Integrate with any agent framework (LlamaIndex, Claude Code, Cursor, etc.) by loading extracted Parquet files and cell metadata into your agent&#39;s context



##  **What&#39;s Next**



 During the beta period, we&#39;re focused on performance optimization, enhanced accuracy, additional output formats, and future API’s that build on the region and table extraction to provide more end-to-end experiences.



 We encourage users to try the API, provide feedback on extraction quality, and help us prioritize features for the full release!



 Let us know what you think:


-  [X](https://x.com/llama_index)
  -  [LinkedIn](https://www.notion.so/BYOC-Questions-for-Chris-from-DataStax-Christopher-Bradford-1d442e06306744dbbe8dc1feea07452e?pvs=21)
  -  [LlamaParse Sign-up/Sign-in](http://cloud.llamaindex.ai)
  -  [LlamaSheets Docs](https://developers.llamaindex.ai/python/cloud/llamasheets/getting_started/)