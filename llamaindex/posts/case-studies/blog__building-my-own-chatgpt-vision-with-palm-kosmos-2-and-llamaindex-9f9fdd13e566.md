---
title: "ChatGPT Vision App: How To Build With PaLM | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/building-my-own-chatgpt-vision-with-palm-kosmos-2-and-llamaindex-9f9fdd13e566"
category: "case-studies"
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







In the ever-evolving landscape of AI, OpenAI’s ChatGPT with vision capabilities has opened a new chapter. It’s an exciting time for developers and creators as we explore the fusion of visual understanding with conversational AI. Inspired by this innovation, I set out to build my own multi-modal prototype, not just as a replica but as a launchpad for more advanced and tailored visual-language applications.



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



The tools at our disposal are nothing short of extraordinary. **KOSMOS-2** a true powerhouse in painting vivid narratives from mere pixels, making image captioning seem almost magical. Then there’s the Google **PaLM API**, bringing a level of conversational depth that truly understands and responds with relevance. And of course, there’s **LlamaIndex **- the brains of the operation, orchestrating these elements with such finesse that the interaction flows as naturally as a conversation between old friends.

# Features Overview

The outcome of my curiosity and coding is a Streamlit app — a prototype that stands as an homage and alternative to ChatGPT’s vision capabilities. Here’s what it brings to the table:

- **Real-Time Image Interaction:** Upload your images and instantly dive into a dialogue about them.
- **Automatic Captioning with KOSMOS-2: **Microsoft’s AI model offers a descriptive base for the conversation.
- **Conversational Depth with PaLM:** Google’s language model ensures the chat is as rich and nuanced as the images themselves.
- **User-Friendly Interface: **Streamlit powers an intuitive and clean UI, making it easy for anyone to navigate and interact.

# Deep Dive into the Tech Stack

The project is a symphony of technologies, each playing a crucial role:

- Microsoft AI **KOSMOS-2** via Replicate breathes life into images by providing them a narrative.
- Google **PaLM API** adds the layer of linguistic intelligence, making the conversation about the images insightful and engaging.
- **LlamaIndex **acts as the maestro, coordinating the models to work in harmony.

# Unveiling `app.py`: The Core of the Application

The `app.py` script is the heart of the app, where we bring together KOSMOS-2 and PaLM with Llamaindex to create a seamless multimodal experience. Let’s walk through it, from start to finish.

**1. Initial Setup**

We start by importing the necessary libraries and setting up our Streamlit page. Here, we lay the groundwork for image processing and conversation management.

import streamlit as st
import extra_streamlit_components as stx
import requests
from PIL import Image
from transformers import AutoProcessor, AutoModelForVision2Seq
from io import BytesIO
import replicate
from llama_index.llms.palm import PaLM
from llama_index import ServiceContext, VectorStoreIndex, Document
from llama_index.memory import ChatMemoryBuffer
import os
import datetime

st.set_page_config(layout="wide")
st.write("My version of ChatGPT vision. You can upload an image and start chatting with the LLM about the image")**2. User Interface**

Next, we craft the sidebar and the main area, ensuring that the user knows who created the app and has access to other projects, enhancing credibility and engagement.

# Sidebar
st.sidebar.markdown('## Created By')
st.sidebar.markdown("[Harshad Suryawanshi](https://www.linkedin.com/in/harshadsuryawanshi/)")
st.sidebar.markdown('## Other Projects')
# ...sidebar content continues**3. Image Upload and Processing**

Upon uploading an image, the app not only displays it but also invokes the `get_image_caption` function to generate a relevant caption. This function, decorated with `@st.cache`for caching, uses the KOSMOS-2 model through Replicate to provide a brief description of the uploaded image. The description is then used as the basis for the initial conversation with the user.

@st.cache
def get_image_caption(image_data):
    input_data = {
        "image": image_data,
        "description_type": "Brief"
    }
    output = replicate.run(
        "lucataco/kosmos-2:3e7b211c29c092f4bcc8853922cc986baa52efe255876b80cac2c2fbb4aff805",
        input=input_data
    )
    # Split the output string on the newline character and take the first item
    text_description = output.split('\n\n')[0]
    return text_description**4. Conversational Flow with PaLM and Llamaindex**

With the image caption in hand, the `create_chat_engine` function is called to set up the chat engine. This function is crucial as it establishes the context for the conversation and initializes the PaLM API for interaction.

@st.cache_resource
def create_chat_engine(img_desc, api_key):
    llm = PaLM(api_key=api_key)
    service_context = ServiceContext.from_defaults(llm=llm)
    doc = Document(text=img_desc)
    index = VectorStoreIndex.from_documents([doc], service_context=service_context)
    chatmemory = ChatMemoryBuffer.from_defaults(token_limit=1500)

    chat_engine = index.as_chat_engine(
        chat_mode="context",
        system_prompt=(
            f"You are a chatbot, able to have normal interactions, as well as talk. "
            "You always answer in great detail and are polite. Your responses always descriptive. "
            "Your job is to talk about an image the user has uploaded. Image description: {img_desc}."
        ),
        verbose=True,
        memory=chatmemory
    )
    return chat_engineThe `create_chat_engine` function builds the infrastructure for our app's conversation capabilities. It starts by instantiating a PaLM object with the provided API key, setting up the service context, and creating a document with the image description. This document is then indexed to prepare it for Llamaindex’s context chat engine. Finally, the chat engine is configured with a prompt that instructs the AI on how to engage in the conversation, referencing the image description and defining the chatbot's behavior.

**5. User Interaction and Message Handling**

The application ensures an engaging and controlled user experience by limiting the number of messages to 20 per session in the demo version. If this limit is reached, it gracefully notifies the user and disables further input to manage resources effectively.

if message_count &amp;gt;= 20:
    st.error("Notice: The maximum message limit for this demo version has been reached.")
    # Disabling the uploader and input by not displaying them
    image_uploader_placeholder = st.empty()  # Placeholder for the uploader
    chat_input_placeholder = st.empty()      # Placeholder for the chat inputHowever, when the message count is within the limit, the application provides a clear chat option and handles the image upload process. Upon uploading, it immediately processes the image to get a caption, sets up the chat engine, and updates the user interface to reflect the successful upload.

else:
    # Add a clear chat button
    if st.button("Clear Chat"):
        clear_chat()

    # Image upload section
    image_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"], key="uploaded_image", on_change=on_image_upload)
    # ...code for image upload and displayFor each user input, the message is added to the chat history, and the chat engine is queried for a response. The app ensures that each message — whether from the user or the assistant — is displayed in the chat interface, maintaining a coherent conversation flow.

# ...code for handling user input and displaying chat history

# Call the chat engine to get the response if an image has been uploaded
if image_file and user_input:
    try:
        with st.spinner('Waiting for the chat engine to respond...'):
            # Get the response from your chat engine
            response = chat_engine.chat(user_input)
        # ...code for appending and displaying the assistant's response
    except Exception as e:
        st.error(f'An error occurred.')
        # ...exception handling code

# Wrapping Up

This app is the foundation, a springboard for more complex visual-language applications. The potential is limitless, and your insights can shape its future. I invite you to dive into the demo, tinker with the code, and join me in pushing the envelope of what AI can do.

[Link to GitHub Repo](https://github.com/AI-ANK/PaLM-Kosmos-Vision)

[Connect with Me on LinkedIn](https://www.linkedin.com/in/harshadsuryawanshi/)

[LinkedIn Post](https://www.linkedin.com/posts/harshadsuryawanshi_ai-computervision-streamlit-activity-7126698614541680640-y5kB):