---
title: "Building a Data Visualization Agent with LangGraph Cloud"
author: "LangChain Accounts"
date: "2024-09-12"
url: "https://www.langchain.com/blog/data-viz-agent"
---

LangGraph

# Building a Data Visualization Agent with LangGraph Cloud

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamSeptember 12, 2024![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)23min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)**Editor&#x27;s Note: This is a guest blog post by **[**Dhruv Ateja**](https://www.linkedin.com/in/dhruv-atreja/?ref=blog.langchain.com)**. It covers building a full stack application that uses an agent to both query data as well as choose how to display that data. It leverages LangGraph and LangGraph Cloud.**

**Key Links:**

- [**YouTube Video**](https://youtu.be/LRcjlXL9hPA?ref=blog.langchain.com)
- [**GitHub Repo**](https://github.com/DhruvAtreja/datavisualization_langgraph?ref=blog.langchain.com)
- [**Hosted Application**](https://data-visualization-frontend-gamma.vercel.app/?ref=blog.langchain.com)

Let&#x27;s explore an exciting project that leverages LangGraph Cloud&#x27;s streaming API to create a data visualization agent. You can upload an SQLite database or CSV file, ask questions about your data, and the agent will generate appropriate visualizations. This blog is a brief dive into the agent’s workflow and key features.

0:00                            /0:281×

The entire workflow is orchestrated using **LangGraph Cloud**, which provides a framework for easily building complex AI agents, a streaming API for real-time updates, and a visual studio for monitoring and experimenting with the agent&#x27;s behavior.

First, let us see the current SOTA text to sql workflow:

### **Schema and Metadata Extraction:**

- The system processes the provided database (e.g., SQLite or CSV) to extract crucial information like table structure and column details.
- This initial step grants a comprehensive understanding of the database&#x27;s organization.

### **Embedding Creation:**

- For larger datasets, embeddings for schema elements (tables, columns) and sample data are generated. These embeddings improve efficiency during retrieval and matching tasks later on.

### **Entity and Context Retrieval:**

- The user&#x27;s query is analyzed to identify entities and the overall context.
- For database values, a syntactic search leveraging a Locality Sensitive Hashing (LSH) index can be implemented.

### **Relevant Table Extraction using Retrieval-Augmented Generation (RAG):**

- This step utilizes RAG to pinpoint the relevant tables that hold the information the user seeks.
- **Experimental Approaches:**
If the schema is manageable within the context window, this step might be skipped.
- Exploring a Knowledge Graph-based RAG for multi-hop functionalities is a potential avenue for future development.
- Extracting relevant columns can be fed into the RAG for more precise table extraction.

### **Large Schema Handling :**

- When dealing with massive table schemas, techniques can be employed to manage them effectively:
Reducing schema details to essential information ensures efficient processing.
- Pruning columns based on metadata tags streamlines the analysis.
- The pruned schema can then be presented to the Language Model (LLM) to assess table relevance.

### **Table and Relevance Validation:**

- The extracted tables are meticulously verified to ensure they are truly relevant to the user&#x27;s query.

### **SQL Query Generation:**

- The relevant tables, their schema, and sample data rows are fed into the LLM to generate the SQL query.
- **Experimentation:** Prompting the LLM to evaluate the necessity of each column in filtered tables, coupled with a chain-of-thought explanation, can provide valuable insights into the reasoning behind the generated query.

### **Query Structure Validation:**

- A workflow validates and corrects the generated SQL query&#x27;s structure, ensuring its correctness before execution.

For our project, we&#x27;ve focused on smaller datasets, eliminating the need for RAG or LSH techniques. However, the core workflow remains consistent. To explore text-to-SQL implementations for larger datasets, check out [this insightful article](https://medium.com/pinterest-engineering/how-we-built-text-to-sql-at-pinterest-30bad30dabff/?ref=blog.langchain.com) from Pinterest Engineering.

Here are is an overview of the implementation of the text to sql workflow:

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaf5ede8e4119828550fd_Screenshot-2024-09-11-at-8.43.31-PM.png)

### Setting up the graph

`
    def create_workflow(self) -&gt; StateGraph:
        &quot;&quot;&quot;Create and configure the workflow graph.&quot;&quot;&quot;
        workflow = StateGraph(State)
        # Add nodes to the graph
        workflow.add_node(&quot;parse_question&quot;, self.sql_agent.parse_question)
        workflow.add_node(&quot;get_unique_nouns&quot;, self.sql_agent.get_unique_nouns)
        workflow.add_node(&quot;generate_sql&quot;, self.sql_agent.generate_sql)
        workflow.add_node(&quot;validate_and_fix_sql&quot;, self.sql_agent.validate_and_fix_sql)
        workflow.add_node(&quot;execute_sql&quot;, self.sql_agent.execute_sql)
        workflow.add_node(&quot;format_results&quot;, self.sql_agent.format_results)
        workflow.add_node(&quot;choose_visualization&quot;, self.sql_agent.choose_visualization)
        workflow.add_node(&quot;format_data_for_visualization&quot;, self.data_formatter.format_data_for_visualization)
        # Define edges
        workflow.add_edge(&quot;parse_question&quot;, &quot;get_unique_nouns&quot;)
        workflow.add_edge(&quot;get_unique_nouns&quot;, &quot;generate_sql&quot;)
        workflow.add_edge(&quot;generate_sql&quot;, &quot;validate_and_fix_sql&quot;)
        workflow.add_edge(&quot;validate_and_fix_sql&quot;, &quot;execute_sql&quot;)
        workflow.add_edge(&quot;execute_sql&quot;, &quot;format_results&quot;)
        workflow.add_edge(&quot;execute_sql&quot;, &quot;choose_visualization&quot;)
        workflow.add_edge(&quot;choose_visualization&quot;, &quot;format_data_for_visualization&quot;)
        workflow.set_entry_point(&quot;parse_question&quot;)

        return workflow

`

### **1. Schema and Metadata Extraction:**

- We&#x27;ve developed a server to store and query SQLite files for this project: [https://github.com/DhruvAtreja/sqllite-server](https://github.com/DhruvAtreja/sqllite-server?ref=blog.langchain.com)
- This server has two main functions: querying the database and retrieving its schema.
- We extract the schema for all tables, including the first three rows of each table for context.

Extracting schema

`
  const db = new sqlite3.Database(dbPath);

  db.all(
    &quot;SELECT name, sql FROM sqlite_master WHERE type=&#x27;table&#x27;;&quot;,
    [],
    (err, tables) =&gt; {
      if (err) {
        db.close();
        return res.status(500).json({ error: err.message });
      }

      const schema = [];

      const processTable = (index) =&gt; {
        if (index &gt;= tables.length) {
          db.close();
          return res.json({ schema: schema.join(&quot;\\n&quot;) });
        }

        const { name: tableName, sql: createStatement } = tables[index];
        schema.push(`Table: ${tableName}`);
        schema.push(`CREATE statement: ${createStatement}\\n`);

        db.all(`SELECT * FROM &#x27;${tableName}&#x27; LIMIT 3;`, [], (err, rows) =&gt; {
          if (err) {
            console.error(`Error fetching rows for table ${tableName}:`, err);
          } else if (rows.length &gt; 0) {
            schema.push(&quot;Example rows:&quot;);
            rows.forEach((row) =&gt; schema.push(JSON.stringify(row)));
          }
          schema.push(&quot;&quot;); // Add a blank line between tables
          processTable(index + 1);
        });
      };

      processTable(0);
    }
  );

`

### **2. Parsing the user&#x27;s question:**

- We pass the user&#x27;s question to the SQLAgent along with the schema of the database. Using this data we extract the relevant tables and columns.
- We also identify columns which contain nouns. We&#x27;ll see why this is important in the next step.
- If the question is not relevant to the database or if there is not enough information to answer the question, we set is_relevant to false and end the workflow.

Prompt:

`You are a data analyst that can help summarize SQL tables and parse user questions about a database.
Given the question and database schema, identify the relevant tables and columns.
If the question is not relevant to the database or if there is not enough information to answer the question, set is_relevant to false.

The &quot;noun_columns&quot; field should contain only the columns that are relevant to the question and contain nouns or names, for example, the column &quot;Artist name&quot; contains nouns relevant to the question &quot;What are the top selling artists?&quot;, but the column &quot;Artist ID&quot; is not relevant because it does not contain a noun. Do not include columns that contain numbers.
`

Response Format:

`{

&quot;is_relevant&quot;: boolean,

&quot;relevant_tables&quot;: [

		{{

		&quot;table_name&quot;: string,

		&quot;columns&quot;: [string],

		&quot;noun_columns&quot;: [string]

		}}

	]

}
`

### **3. Getting the unique nouns:**

- If the user asks &quot;What are the top selling artists?&quot; or &quot;What is the market share of each category?&quot;, we need to know which artists are being referred to or which categories are being referred to in order to generate the correct SQL query.
- What if the user asks &quot;Top selling ac dc songs?&quot; (We all know it has to be Thunderstruck) but the table contains the name &quot;AC/DC&quot; instead of &quot;ac dc&quot;? We need to get the correct spelling of the artist&#x27;s name in order to generate the correct SQL query.
- This is where the unique nouns come in. We extract the unique nouns from the question and the schema and match them. We can get the correct spelling of the artist&#x27;s name and the list of entities using the unique nouns.

Function

`    def get_unique_nouns(self, state: dict) -&gt; dict:
        &quot;&quot;&quot;Find unique nouns in relevant tables and columns.&quot;&quot;&quot;
        parsed_question = state[&#x27;parsed_question&#x27;]

        if not parsed_question[&#x27;is_relevant&#x27;]:
            return {&quot;unique_nouns&quot;: []}

        unique_nouns = set()
        for table_info in parsed_question[&#x27;relevant_tables&#x27;]:
            table_name = table_info[&#x27;table_name&#x27;]
            noun_columns = table_info[&#x27;noun_columns&#x27;]

            if noun_columns:
                column_names = &#x27;, &#x27;.join(f&quot;`{col}`&quot; for col in noun_columns)
                query = f&quot;SELECT DISTINCT {column_names} FROM `{table_name}`&quot;
                results = self.db_manager.execute_query(state[&#x27;uuid&#x27;], query)
                for row in results:
                    unique_nouns.update(str(value) for value in row if value)

        return {&quot;unique_nouns&quot;: list(unique_nouns)}
`

### **4. Generating the SQL query:**

We pass the schema, the user&#x27;s question, the parsed question and the unique nouns to the SQLAgent. We skip the rows where any column is null, &quot;N/A&quot; or &quot;&quot;.

Prompt

`You are an AI assistant that generates SQL queries based on user questions, database schema, and unique nouns found in the relevant tables. Generate a valid SQL query to answer the user&#x27;s question.

If there is not enough information to write a SQL query, respond with &quot;NOT_ENOUGH_INFO&quot;.

Here are some examples:

1. What is the top selling product?
Answer: SELECT product_name, SUM(quantity) as total_quantity FROM sales WHERE product_name IS NOT NULL AND quantity IS NOT NULL AND product_name != &quot;&quot; AND quantity != &quot;&quot; AND product_name != &quot;N/A&quot; AND quantity != &quot;N/A&quot; GROUP BY product_name ORDER BY total_quantity DESC LIMIT 1

2. What is the total revenue for each product?
Answer: SELECT product_name, SUM(quantity * price) as total_revenue FROM sales WHERE product_name IS NOT NULL AND quantity IS NOT NULL AND price IS NOT NULL AND product_name != &quot;&quot; AND quantity != &quot;&quot; AND price != &quot;&quot; AND product_name != &quot;N/A&quot; AND quantity != &quot;N/A&quot; AND price != &quot;N/A&quot; GROUP BY product_name ORDER BY total_revenue DESC

3. What is the market share of each product?
Answer: SELECT product_name, SUM(quantity) * 100.0 / (SELECT SUM(quantity) FROM sales) as market_share FROM sales WHERE product_name IS NOT NULL AND quantity IS NOT NULL AND product_name != &quot;&quot; AND quantity != &quot;&quot; AND product_name != &quot;N/A&quot; AND quantity != &quot;N/A&quot; GROUP BY product_name ORDER BY market_share DESC

4. Plot the distribution of income over time
Answer: SELECT income, COUNT(*) as count FROM users WHERE income IS NOT NULL AND income != &quot;&quot; AND income != &quot;N/A&quot; GROUP BY income

THE RESULTS SHOULD ONLY BE IN THE FOLLOWING FORMAT, SO MAKE SURE TO ONLY GIVE TWO OR THREE COLUMNS:
[[x, y]]
or
[[label, x, y]]

For questions like &quot;plot a distribution of the fares for men and women&quot;, count the frequency of each fare and plot it. The x axis should be the fare and the y axis should be the count of people who paid that fare.
SKIP ALL ROWS WHERE ANY COLUMN IS NULL or &quot;N/A&quot; or &quot;&quot;.
Just give the query string. Do not format it. Make sure to use the correct spellings of nouns as provided in the unique nouns list.

`

Data passed

`===Database schema:
{schema}

===User question:

{question}

===Relevant tables and columns:

{parsed_question}

===Unique nouns in relevant tables:

{unique_nouns}
`

### **5. Validating and fixing the SQL query:**

- We pass the SQL query to the SQLAgent. It checks if the query is valid and all the tables and columns used in the query are relevant and if it is, it returns the SQL query.
- For example, there are cases when the data needs to be converted from string to date or integer, this is fixed in this step.

Prompt

`You are an AI assistant that validates and fixes SQL queries. Your task is to:
1. Check if the SQL query is valid.
2. Ensure all table and column names are correctly spelled and exist in the schema.
3. If there are any issues, fix them and provide the corrected SQL query.
4. If no issues are found, return the original query.

Respond in JSON format with the following structure. Only respond with the JSON:
{{
    &quot;valid&quot;: boolean,
    &quot;issues&quot;: string or null,
    &quot;corrected_query&quot;: string
}}
&#x27;&#x27;&#x27;),
            (&quot;human&quot;, &#x27;&#x27;&#x27;===Database schema:
{schema}

===Generated SQL query:
{sql_query}

Respond in JSON format with the following structure. Only respond with the JSON:
{{
    &quot;valid&quot;: boolean,
    &quot;issues&quot;: string or null,
    &quot;corrected_query&quot;: string
}}

For example:
1. {{
    &quot;valid&quot;: true,
    &quot;issues&quot;: null,
    &quot;corrected_query&quot;: &quot;None&quot;
}}

2. {{
    &quot;valid&quot;: false,
    &quot;issues&quot;: &quot;Column USERS does not exist&quot;,
    &quot;corrected_query&quot;: &quot;SELECT * FROM users WHERE age &gt; 25&quot;
}}
`

### **6. Executing the SQL query:**

We pass the SQL query to the DatabaseManager. It passes the query to the remote database and returns the results.

### **7. Choosing an appropriate visualization:**

I think it is a good idea to reverse engineer this process. Assuming that we are adding support for the following graphs/charts:

- Column Graphs
- Bar Graphs
- Scatter Plots
- Line Graphs
- Pie Charts

Here’s a breakdown of the types of questions we would need to support

- **Bar/Column Graphs**:
**Questions**: &quot;What are the sales figures for each product in the last quarter?&quot;, &quot;How does the population of cities compare?&quot;, &quot;What are the top 5 most common job titles in the company?&quot;
- **Use Case**: Best for comparing categorical data or showing changes over time when categories are discrete.

- **Scatter Plots**:
**Questions**: &quot;Is there a relationship between advertising spend and sales?&quot;, &quot;How do height and weight correlate in the dataset?&quot;, &quot;What is the distribution of ages vs. salaries?&quot;
- **Use Case**: Useful for identifying relationships or correlations between two numerical variables.

- **Pie Charts**:
**Questions**: &quot;What is the market share distribution among different companies?&quot;, &quot;How are the department budgets divided?&quot;, &quot;What percentage of the total revenue comes from each product?&quot;
- **Use Case**: Ideal for showing proportions or percentages within a whole.

- **Line Graphs**:
**Questions**: &quot;How have website visits changed over the year?&quot;, &quot;What is the trend in temperature over the past decade?&quot;, &quot;How has stock price fluctuated over time?&quot;
- **Use Case**: Best for showing trends over time with continuous data.

This identifies the following lines of questioning:

- **Aggregations and Summarizations**:
Example: &quot;What is the average revenue by month?&quot; (Line Graph)
- &quot;Show the total sales by product category.&quot; (Bar/Column Graph)

- **Comparisons**:
Example: &quot;Compare the sales figures of Product A and Product B over the last year.&quot; (Line or Column Graph)

- **Trends Over Time**:
Example: &quot;What is the trend in the number of active users over the past year?&quot; (Line Graph)

- **Proportions**:
Example: &quot;What percentage of sales came from each region?&quot; (Pie Chart)

- **Correlations**:
Example: &quot;Is there a correlation between marketing spend and revenue?&quot; (Scatter Plot)

**Prompt**

`You are an AI assistant that recommends appropriate data visualizations. Based on the user&#x27;s question, SQL query, and query results, suggest the most suitable type of graph or chart to visualize the data. If no visualization is appropriate, indicate that.

Available chart types and their use cases:

- Bar Graphs: Best for comparing categorical data or showing changes over time when categories are discrete and the number of categories is more than 2. Use for questions like &quot;What are the sales figures for each product?&quot; or &quot;How does the population of cities compare? or &quot;What percentage of each city is male?&quot;
- Horizontal Bar Graphs: Best for comparing categorical data or showing changes over time when the number of categories is small or the disparity between categories is large. Use for questions like &quot;Show the revenue of A and B?&quot; or &quot;How does the population of 2 cities compare?&quot; or &quot;How many men and women got promoted?&quot; or &quot;What percentage of men and what percentage of women got promoted?&quot; when the disparity between categories is large.
- Scatter Plots: Useful for identifying relationships or correlations between two numerical variables or plotting distributions of data. Best used when both x axis and y axis are continuous. Use for questions like &quot;Plot a distribution of the fares (where the x axis is the fare and the y axis is the count of people who paid that fare)&quot; or &quot;Is there a relationship between advertising spend and sales?&quot; or &quot;How do height and weight correlate in the dataset? Do not use it for questions that do not have a continuous x axis.&quot;
- Pie Charts: Ideal for showing proportions or percentages within a whole. Use for questions like &quot;What is the market share distribution among different companies?&quot; or &quot;What percentage of the total revenue comes from each product?&quot;
- Line Graphs: Best for showing trends and distributionsover time. Best used when both x axis and y axis are continuous. Used for questions like &quot;How have website visits changed over the year?&quot; or &quot;What is the trend in temperature over the past decade?&quot;. Do not use it for questions that do not have a continuous x axis or a time based x axis.

Consider these types of questions when recommending a visualization:

1. Aggregations and Summarizations (e.g., &quot;What is the average revenue by month?&quot; - Line Graph)

2. Comparisons (e.g., &quot;Compare the sales figures of Product A and Product B over the last year.&quot; - Line or Column Graph)

3. Plotting Distributions (e.g., &quot;Plot a distribution of the age of users&quot; - Scatter Plot)

4. Trends Over Time (e.g., &quot;What is the trend in the number of active users over the past year?&quot; - Line Graph)

5. Proportions (e.g., &quot;What is the market share of the products?&quot; - Pie Chart)

6. Correlations (e.g., &quot;Is there a correlation between marketing spend and revenue?&quot; - Scatter Plot)

Provide your response in the following format:

Recommended Visualization: [Chart type or &quot;None&quot;]. ONLY use the following names: bar, horizontal_bar, line, pie, scatter, none

Reason: [Brief explanation for your recommendation]
`

### **8. Formatting the data for visualization:**

We pass the SQL query results to the DataFormatter. It formats the data according to the visualization type. If the results are in a predictable format, we have implemented rule based logic to format the data and only use llms to come up with labels, which speeds up the process especially in the cases of bar graphs, line graphs and scatter plots. Else we pass the results to a LLM to format the data.

**Formatting instructions**

`
barGraphIntstruction = &#x27;&#x27;&#x27;

  Where data is: {
    labels: string[]
    values: {\\data: number[], label: string}[]
  }

// Examples of usage:
Each label represents a column on the x axis.
Each array in values represents a different entity.

Here we are looking at average income for each month.
1. data = {
  labels: [&#x27;Jan&#x27;, &#x27;Feb&#x27;, &#x27;Mar&#x27;, &#x27;Apr&#x27;, &#x27;May&#x27;, &#x27;Jun&#x27;],
  values: [{data:[21.5, 25.0, 47.5, 64.8, 105.5, 133.2], label: &#x27;Income&#x27;}],
}

Here we are looking at the performance of american and european players for each series. Since there are two entities, we have two arrays in values.
2. data = {
  labels: [&#x27;series A&#x27;, &#x27;series B&#x27;, &#x27;series C&#x27;],
  values: [{data:[10, 15, 20], label: &#x27;American&#x27;}, {data:[20, 25, 30], label: &#x27;European&#x27;}],
}
&#x27;&#x27;&#x27;

horizontalBarGraphIntstruction = &#x27;&#x27;&#x27;

  Where data is: {
    labels: string[]
    values: {\\data: number[], label: string}[]
  }

// Examples of usage:
Each label represents a column on the x axis.
Each array in values represents a different entity.

Here we are looking at average income for each month.
1. data = {
  labels: [&#x27;Jan&#x27;, &#x27;Feb&#x27;, &#x27;Mar&#x27;, &#x27;Apr&#x27;, &#x27;May&#x27;, &#x27;Jun&#x27;],
  values: [{data:[21.5, 25.0, 47.5, 64.8, 105.5, 133.2], label: &#x27;Income&#x27;}],
}

Here we are looking at the performance of american and european players for each series. Since there are two entities, we have two arrays in values.
2. data = {
  labels: [&#x27;series A&#x27;, &#x27;series B&#x27;, &#x27;series C&#x27;],
  values: [{data:[10, 15, 20], label: &#x27;American&#x27;}, {data:[20, 25, 30], label: &#x27;European&#x27;}],
}

&#x27;&#x27;&#x27;

lineGraphIntstruction = &#x27;&#x27;&#x27;

  Where data is: {
  xValues: number[] | string[]
  yValues: { data: number[]; label: string }[]
}

// Examples of usage:

Here we are looking at the momentum of a body as a function of mass.
1. data = {
  xValues: [&#x27;2020&#x27;, &#x27;2021&#x27;, &#x27;2022&#x27;, &#x27;2023&#x27;, &#x27;2024&#x27;],
  yValues: [
    { data: [2, 5.5, 2, 8.5, 1.5]},
  ],
}

Here we are looking at the performance of american and european players for each year. Since there are two entities, we have two arrays in yValues.
2. data = {
  xValues: [&#x27;2020&#x27;, &#x27;2021&#x27;, &#x27;2022&#x27;, &#x27;2023&#x27;, &#x27;2024&#x27;],
  yValues: [
    { data: [2, 5.5, 2, 8.5, 1.5], label: &#x27;American&#x27; },
    { data: [2, 5.5, 2, 8.5, 1.5], label: &#x27;European&#x27; },
  ],
}
&#x27;&#x27;&#x27;

pieChartIntstruction = &#x27;&#x27;&#x27;

  Where data is: {
    labels: string
    values: number
  }[]

// Example usage:
 data = [
        { id: 0, value: 10, label: &#x27;series A&#x27; },
        { id: 1, value: 15, label: &#x27;series B&#x27; },
        { id: 2, value: 20, label: &#x27;series C&#x27; },
      ],
&#x27;&#x27;&#x27;

scatterPlotIntstruction = &#x27;&#x27;&#x27;
Where data is: {
  series: {
    data: { x: number; y: number; id: number }[]
    label: string
  }[]
}

// Examples of usage:
1. Here each data array represents the points for a different entity.
We are looking for correlation between amount spent and quantity bought for men and women.
data = {
  series: [
    {
      data: [
        { x: 100, y: 200, id: 1 },
        { x: 120, y: 100, id: 2 },
        { x: 170, y: 300, id: 3 },
      ],
      label: &#x27;Men&#x27;,
    },
    {
      data: [
        { x: 300, y: 300, id: 1 },
        { x: 400, y: 500, id: 2 },
        { x: 200, y: 700, id: 3 },
      ],
      label: &#x27;Women&#x27;,
    }
  ],
}

2. Here we are looking for correlation between the height and weight of players.
data = {
  series: [
    {
      data: [
        { x: 180, y: 80, id: 1 },
        { x: 170, y: 70, id: 2 },
        { x: 160, y: 60, id: 3 },
      ],
      label: &#x27;Players&#x27;,
    },
  ],
}

// Note: Each object in the &#x27;data&#x27; array represents a point on the scatter plot.
// The &#x27;x&#x27; and &#x27;y&#x27; values determine the position of the point, and &#x27;id&#x27; is a unique identifier.
// Multiple series can be represented, each as an object in the outer array.
&#x27;&#x27;&#x27;

graph_instructions = {
    &quot;bar&quot;: barGraphIntstruction,
    &quot;horizontal_bar&quot;: horizontalBarGraphIntstruction,
    &quot;line&quot;: lineGraphIntstruction,
    &quot;pie&quot;: pieChartIntstruction,
    &quot;scatter&quot;: scatterPlotIntstruction
}
`

**Data formatter**

`
class DataFormatter:
    def __init__(self):
        self.llm_manager = LLMManager()


    def format_data_for_visualization(self, state: dict) -&gt; dict:
        &quot;&quot;&quot;Format the data for the chosen visualization type.&quot;&quot;&quot;
        visualization = state[&#x27;visualization&#x27;]
        results = state[&#x27;results&#x27;]
        question = state[&#x27;question&#x27;]
        sql_query = state[&#x27;sql_query&#x27;]

        if visualization == &quot;none&quot;:
            return {&quot;formatted_data_for_visualization&quot;: None}

        if visualization == &quot;scatter&quot;:
            try:
                return self._format_scatter_data(results)
            except Exception as e:
                return self._format_other_visualizations(visualization, question, sql_query, results)

        if visualization == &quot;bar&quot; or visualization == &quot;horizontal_bar&quot;:
            try:
                return self._format_bar_data(results, question)
            except Exception as e:
                return self._format_other_visualizations(visualization, question, sql_query, results)

        if visualization == &quot;line&quot;:
            try:
                return self._format_line_data(results, question)
            except Exception as e:
                return self._format_other_visualizations(visualization, question, sql_query, results)

        return self._format_other_visualizations(visualization, question, sql_query, results)

    def _format_line_data(self, results, question):
        if isinstance(results, str):
            results = eval(results)

        if len(results[0]) == 2:

            x_values = [str(row[0]) for row in results]
            y_values = [float(row[1]) for row in results]

            # Use LLM to get a relevant label
            prompt = ChatPromptTemplate.from_messages([
                (&quot;system&quot;, &quot;You are a data labeling expert. Given a question and some data, provide a concise and relevant label for the data series.&quot;),
                (&quot;human&quot;, &quot;Question: {question}\\n Data (first few rows): {data}\\n\\nProvide a concise label for this y axis. For example, if the data is the sales figures over time, the label could be &#x27;Sales&#x27;. If the data is the population growth, the label could be &#x27;Population&#x27;. If the data is the revenue trend, the label could be &#x27;Revenue&#x27;.&quot;),
            ])
            label = self.llm_manager.invoke(prompt, question=question, data=str(results[:2]))

            formatted_data = {
                &quot;xValues&quot;: x_values,
                &quot;yValues&quot;: [
                    {
                        &quot;data&quot;: y_values,
                        &quot;label&quot;: label.strip()
                    }
                ]
            }
        elif len(results[0]) == 3:

            # Group data by label
            data_by_label = {}
            x_values = []

            for item1, item2, item3 in results:
                # Determine which item is the label (string not convertible to float and not containing &quot;/&quot;)
                if isinstance(item1, str) and not item1.replace(&quot;.&quot;, &quot;&quot;).isdigit() and &quot;/&quot; not in item1:
                    label, x, y = item1, item2, item3
                else:
                    x, label, y = item1, item2, item3


                if str(x) not in x_values:
                    x_values.append(str(x))
                if label not in data_by_label:
                    data_by_label[label] = []
                data_by_label[label].append(float(y))

            # Create yValues array
            y_values = [
                {
                    &quot;data&quot;: data,
                    &quot;label&quot;: label
                }
                for label, data in data_by_label.items()
            ]

            formatted_data = {
                &quot;xValues&quot;: x_values,
                &quot;yValues&quot;: y_values
            }

            # Use LLM to get a relevant label for the y-axis
            prompt = ChatPromptTemplate.from_messages([
                (&quot;system&quot;, &quot;You are a data labeling expert. Given a question and some data, provide a concise and relevant label for the y-axis.&quot;),
                (&quot;human&quot;, &quot;Question: {question}\\n Data (first few rows): {data}\\n\\nProvide a concise label for the y-axis. For example, if the data represents sales figures over time for different categories, the label could be &#x27;Sales&#x27;. If it&#x27;s about population growth for different groups, it could be &#x27;Population&#x27;.&quot;),
            ])
            y_axis_label = self.llm_manager.invoke(prompt, question=question, data=str(results[:2]))

            # Add the y-axis label to the formatted data
            formatted_data[&quot;yAxisLabel&quot;] = y_axis_label.strip()

        return {&quot;formatted_data_for_visualization&quot;: formatted_data}

    def _format_scatter_data(self, results):
        if isinstance(results, str):
            results = eval(results)

        formatted_data = {&quot;series&quot;: []}

        if len(results[0]) == 2:
            formatted_data[&quot;series&quot;].append({
                &quot;data&quot;: [
                    {&quot;x&quot;: float(x), &quot;y&quot;: float(y), &quot;id&quot;: i+1}
                    for i, (x, y) in enumerate(results)
                ],
                &quot;label&quot;: &quot;Data Points&quot;
            })
        elif len(results[0]) == 3:
            entities = {}
            for item1, item2, item3 in results:
                # Determine which item is the label (string not convertible to float and not containing &quot;/&quot;)
                if isinstance(item1, str) and not item1.replace(&quot;.&quot;, &quot;&quot;).isdigit() and &quot;/&quot; not in item1:
                    label, x, y = item1, item2, item3
                else:
                    x, label, y = item1, item2, item3
                if label not in entities:
                    entities[label] = []
                entities[label].append({&quot;x&quot;: float(x), &quot;y&quot;: float(y), &quot;id&quot;: len(entities[label])+1})

            for label, data in entities.items():
                formatted_data[&quot;series&quot;].append({
                    &quot;data&quot;: data,
                    &quot;label&quot;: label
                })
        else:
            raise ValueError(&quot;Unexpected data format in results&quot;)

        return {&quot;formatted_data_for_visualization&quot;: formatted_data}

    def _format_bar_data(self, results, question):
        if isinstance(results, str):
            results = eval(results)

        if len(results[0]) == 2:
            # Simple bar chart with one series
            labels = [str(row[0]) for row in results]
            data = [float(row[1]) for row in results]

            # Use LLM to get a relevant label
            prompt = ChatPromptTemplate.from_messages([
                (&quot;system&quot;, &quot;You are a data labeling expert. Given a question and some data, provide a concise and relevant label for the data series.&quot;),
                (&quot;human&quot;, &quot;Question: {question}\\nData (first few rows): {data}\\n\\nProvide a concise label for this y axis. For example, if the data is the sales figures for products, the label could be &#x27;Sales&#x27;. If the data is the population of cities, the label could be &#x27;Population&#x27;. If the data is the revenue by region, the label could be &#x27;Revenue&#x27;.&quot;),
            ])
            label = self.llm_manager.invoke(prompt, question=question, data=str(results[:2]))

            values = [{&quot;data&quot;: data, &quot;label&quot;: label}]
        elif len(results[0]) == 3:
            # Grouped bar chart with multiple series
            categories = set(row[1] for row in results)
            labels = list(categories)
            entities = set(row[0] for row in results)
            values = []
            for entity in entities:
                entity_data = [float(row[2]) for row in results if row[0] == entity]
                values.append({&quot;data&quot;: entity_data, &quot;label&quot;: str(entity)})
        else:
            raise ValueError(&quot;Unexpected data format in results&quot;)

        formatted_data = {
            &quot;labels&quot;: labels,
            &quot;values&quot;: values
        }

        return {&quot;formatted_data_for_visualization&quot;: formatted_data}

    def _format_other_visualizations(self, visualization, question, sql_query, results):
        instructions = graph_instructions[visualization]
        prompt = ChatPromptTemplate.from_messages([
            (&quot;system&quot;, &quot;You are a Data expert who formats data according to the required needs. You are given the question asked by the user, it&#x27;s sql query, the result of the query and the format you need to format it in.&quot;),
            (&quot;human&quot;, &#x27;For the given question: {question}\\n\\nSQL query: {sql_query}\\n\\Result: {results}\\n\\nUse the following example to structure the data: {instructions}. Just give the json string. Do not format it&#x27;),
        ])
        response = self.llm_manager.invoke(prompt, question=question, sql_query=sql_query, results=results, instructions=instructions)

        try:
            formatted_data_for_visualization = json.loads(response)
            return {&quot;formatted_data_for_visualization&quot;: formatted_data_for_visualization}
        except json.JSONDecodeError:
            return {&quot;error&quot;: &quot;Failed to format data for visualization&quot;, &quot;raw_response&quot;: response}

`

**Throughout the workflow, this was our state:**

`class State(TypedDict):
    question: str
    uuid: str
    parsed_question: Dict[str, Any]
    unique_nouns: List[str]
    sql_query: str
    sql_valid: bool
    sql_issues: str
    results: List[Any]
    answer: Annotated[str, operator.add]
    error: str
    visualization: Annotated[str, operator.add]
    visualization_reason: Annotated[str, operator.add]
    formatted_data_for_visualization: Dict[str, Any]
`

### **Frontend**

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaf5ede8e411982855100_Screenshot-2024-09-11-at-8.44.23-PM.png)

On the frontend, we have prebuilt graph templates which are used to show the visualization.

We use langgraph&#x27;s streaming api to get the state of the workflow and updates in real time, to provide a nice UI where user can see the progress of the workflow.

Once the visualization is generated, the user can see the traces of the workflow along with the final visualization.

## **Conclusion**

By combining the power of LangGraph Cloud&#x27;s streaming API, parallel processing capabilities, and interactive studio, we&#x27;ve created a flexible and powerful data visualization agent. This project demonstrates how modern AI tools can be leveraged to create intuitive interfaces for database querying and data visualization.

The ability to ask natural language questions about your data and receive instant, visually appealing results opens up new possibilities for data exploration and analysis. Whether you&#x27;re a data scientist, business analyst, or just someone curious about your data, this tool provides an accessible and powerful way to gain insights.

We encourage you to try out this project, connect it to your own database, and explore the possibilities of agentic workflows with LangGraph Cloud!

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cb92b0ec45aa6d7bc39a91_KEnsho.png)Case StudiesLangGraphObservability &amp; Evals

#### How Kensho built a multi-agent framework with LangGraph to solve trusted financial data retrieval

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamMarch 26, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/customers-kensho)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa08cd1956c2e4f9ff39_Remote-case-study.png)Case StudiesLangChainLangGraph

#### How Remote uses LangChain and LangGraph to onboard thousands of customers with AI

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamJanuary 19, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)5min[](/blog/customers-remote)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa18703c727fd28ab4de_Vodafone-Italy---Oct-2025--1-.png)Case StudiesLangGraphLangSmith

#### Fastweb + Vodafone: Transforming Customer Experience with AI Agents using LangGraph and LangSmith

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamDecember 16, 2025![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/customers-vodafone-italy)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)