---
title: "GenAI-Driven ADU Planning Guide For Homeowners | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/pioneering-the-future-of-housing-introducing-genai-driven-adu-planning-ea950be71e2f"
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





          ADU Planner in action![](/blog/images/1*hEwxAnZ6JUS_vYuBjh-wuA.png)

In the midst of a pressing housing shortage, the American dream of homeownership is being reimagined through the innovative concept of Accessory Dwelling Units (ADUs). These compact, efficient homes, nestled in the backyards of existing properties, are more than just a trend — they’re a revolution in modular and prefabricated living solutions. In 2022, the ADU market, combined with modular and prefabricated houses, soared to an impressive $150 billion globally, with projections indicating a leap to $300 billion by 2032 ([link](https://www.factmr.com/report/4227/prefabricated-homes-market)).



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



Yet, the journey to erecting an ADU has been far from simple. Traditionally, it involves extensive land surveys and numerous consultations with vendors to sift through an array of floor plans. Recognizing the need for a more efficient pathway, our team has crafted an innovative solution: a GenAI-powered ADU planning system. This cutting-edge tool deftly navigates through the maze of city building codes, effortlessly connecting users with local vendors and presenting viable floor plan options — all within our user-friendly app.

Our mission is to streamline your ADU creation process, making it less daunting and more accessible. Imagine the potential when the complexities of planning are reduced to a few clicks — this is the power of GenAI at your fingertips.

# **Award-Winning Innovation: ADU Planner Takes the Lead**

We’re thrilled to announce a milestone achievement: Our “ADU Planner” project clinched the **top honor** at the [**LlamaIndex RAG Hackathon**](https://rag-a-thon.devpost.com/), held in the first weekend of February 2024. This victory underscores our commitment to transforming the ADU space with our pioneering technology.

Discover the features that set our project apart and explore the full scope of our innovative planner through the following resources:

· **Dive into the Details**: Visit our [Devpost project page](https://devpost.com/software/adu-planner?ref_content=my-projects-tab&amp;ref_feature=my_projects) for an in-depth look.

· **Explore Our Code**: For the tech enthusiasts, our codebase is available on [GitHub](https://github.com/RJ-Heisenberg/ADU-Planner_rag-a-thon2024).

We’re just getting started, and this recognition only fuels our drive to innovate and deliver solutions that matter.

# Watch Our Demo

# **Technologies**

At the heart of our “ADU Planner” lies a synergy of cutting-edge technology and user-friendly design. The seamless interface is crafted with React, providing an intuitive frontend experience, while our robust Flask backend is the powerhouse of functionality, energized by the latest AI from GPT-3.5/4V and augmented by the precision of the LlamaIndex PDF parser and the versatility of Google Maps.

Here’s how our workflow unfolds:

1. **Start with Simplicity:** Users begin by entering their address into our frontend. This action triggers our Google geocoding-powered backend to spring into action, capturing a detailed satellite image of the property in question.

2. **Deciphering the Details:** Next, the journey bifurcates into a dual analysis mode. One path involves parsing through local building codes, a task adeptly handled by GPT-3.5, to unearth specific ADU regulations such as minimum and maximum floor area constraints. Concurrently, GPT-4V meticulously scans the satellite imagery to pinpoint any potential obstructions and delineate the areas ripe for ADU development.

3. **Bringing Plans to Life:** With the viable regions marked, our system embarks on a virtual quest, scouring local builders’ websites for ADU floor plans that not only fit the legal criteria but also the physical realities of your property. These plans are then vividly rendered within the identified buildable zones.

4. **A Click to the Future:** Engaging with a chosen floor plan is as simple as a click, transporting users to the builder’s domain where immersive 3D renderings, pricing details, and more await. To cap it off, our tool thoughtfully prepares data exports to facilitate those all-important initial discussions with ADU builders.

This is more than a tool — it’s a gateway to turning your backyard into a space of possibility.

# **Flowchart**

Flowchart![](/blog/images/1*oAJ5L5oaRj_W5vV8uMSgWw.jpeg)

# **Code Samples**

**Querying PDFs**

In the following example, we’ll query local ADU building codes for Saratoga, CA. Once you’ve setup your LlamaIndex and OpenAI API keys, you’ll be able to parse the PDFs as follows:

from llama_parse import LlamaParse
parser = LlamaParse(result_type='markdown')
docs = sum([
  parser.load_data(file) for file in [
    'Documents/ADU_FAQ.pdf',
    'Documents/ADU_Handbook.pdf',
    'Documents/SCC-ADU-Guidebook-FINAL-9.8.23.pdf']], [])Then, we can index the documents into an ephemeral, or in-memory, [Chroma DB](https://www.trychroma.com/) embeddings store.

chroma_client = chromadb.EphemeralClient()
chroma_collection = chroma_client.get_or_create_collection('embeddings')
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)
index = VectorStoreIndex.from_documents(docs, storage_context=storage_context)Next, we can integrate the documents into our agentic flow by creating a tool for our agent to query them.

tools = [
  QueryEngineTool(
       query_engine=index.as_query_engine(),
       metadata=ToolMetadata(
           name='saratoga_adu_codes',
           description=('Provides information about ADU building codes for the city of Saratoga, CA.'),
       ),
   )
]All together, our agent will be able to answer questions about the documents as follows:

from llama_index.agent import OpenAIAgent

agent = OpenAIAgent.from_tools(tools, verbose=True)
agent.chat("""\
Answer the following questions regarding Accessory Dwelling Unit (ADU) construction planning in Saratoga, California (CA):
- What are the typical side and rear setbacks for a detached ADU?
""")

&amp;gt;&amp;gt;&amp;gt; 'For detached ADUs in Saratoga, California, the typical side and rear setbacks are a minimum of four feet from the lot lines.'**Image analysis**

Firstly, we’ll prepare an image and plot it for visual recognization.

import os
from pathlib import Path
from PIL import Image
import matplotlib.pyplot as plt

input_image_path = Path("input_images")
if not input_image_path.exists():
    Path.mkdir(input_image_path)

image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']

# Filter out non-image files
image_paths = [str(input_image_path / img_path) for img_path in os.listdir(input_image_path)
               if any(img_path.lower().endswith(ext) for ext in image_extensions)]

def plot_images(image_paths):
    images_shown = 0
    plt.figure(figsize=(16, 9))
    for img_path in image_paths:
        if os.path.isfile(img_path):
            image = Image.open(img_path)

            plt.subplot(2, 3, images_shown + 1)
            plt.imshow(image)
            plt.xticks([])
            plt.yticks([])

            images_shown += 1
            if images_shown &amp;gt;= 6:  # Adjusted to match the subplot dimensions (2,3)
                break

plot_images(image_paths)Secondly, we can do a image analysis and recognize the property layout based on GPT-4V, using the following prompt sample as an example.

instruction = '''
You are an intelligent Accessory Dwelling Units (ADU) architect designer and contractor.
Please analyze the image, describle the layout, and then describe the pool, property, and driveways in the format of:
1. property: xxx
2. pool: xxx
...
'''from llama_index.multi_modal_llms.openai import OpenAIMultiModal
from llama_index import SimpleDirectoryReader

# put your local directore here
image_documents = SimpleDirectoryReader("./input_images").load_data()

openai_mm_llm = OpenAIMultiModal(
    model="gpt-4-vision-preview", api_key=OPENAI_API_TOKEN, max_new_tokens=1500, temperature = 0.0
)

response = openai_mm_llm.complete(
    prompt = instruction,
    image_documents=image_documents,
)

print(response)Based on the aerial image provided, here is an analysis of the layout:

1. Property: The property appears to be a residential lot with a single-family home. The house has a hipped roof with multiple sections, indicating a complex floor plan with possibly several rooms or wings. There is a landscaped area surrounding the house with various trees and shrubs, and the terrain seems to be sloped, as indicated by the terracing on the land.

2. Pool: There is a kidney-shaped pool located to the northwest of the main house. It is surrounded by a paved area, likely for lounging and poolside activities, and is accessible via a curved pathway that leads from the house to the pool area.

3. Driveways: It is not entirely clear from the image where the driveway is located, as the specific access point to the property is not visible. However, there seems to be a paved path leading from the bottom right of the image towards the house, which could be the driveway or a walkway. If it is the driveway, it would be located on the southeast side of the property, leading up to the house.

Please note that without a broader view or additional context, some details about the property, such as the exact location of the driveway or additional structures, may not be accurately determined.

# **Conclusions**

Our application markedly simplifies the ADU construction process for homeowners. It adeptly navigates complex tasks such as land surveying and identifying viable floor plans. While ADU vendors need to validate the chosen floor plan and cities must grant construction approval, our tool propels this progression by facilitating comprehensive at-home analysis. Looking ahead, we are poised to officially launch this application and forge partnerships with reputable ADU vendors, enhancing oversight in modular and prefabricated home construction. We are committed to personalizing our service further by adapting our recommendations to align with individual budget constraints and specific layout preferences, ensuring that our users’ visions for their homes are realized with precision and care.