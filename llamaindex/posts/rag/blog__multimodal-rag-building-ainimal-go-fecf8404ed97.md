---
title: "Multimodal RAG Guide: Build AInimal Go App | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/multimodal-rag-building-ainimal-go-fecf8404ed97"
category: "rag"
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







In the current landscape where GPT-4 Vision (GPT-4V) use cases are everywhere, I wanted to explore an alternative approach: pairing deep learning vision models with large language models (LLMs). My latest project, ‘AInimal Go!’, is an attempt to showcase how a specialized vision model like ResNet18 can seamlessly integrate with an LLM, using LlamaIndex as the orchestration layer and Wikipedia articles as the knowledge base.



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



# Project Overview

‘AInimal Go!’ is an interactive app that allows users to either capture or upload images of animals. Upon uploading an image, the ResNet18 model swiftly classifies the animal. Following this, the Cohere LLM API, adeptly orchestrated by LlamaIndex, takes over. It roleplays as the identified animal, enabling users to engage in unique conversations about and with the animal. The dialogue is informed and enriched by a knowledge base of nearly 200 Wikipedia articles, providing accurate and relevant responses to user queries.

# Why Not GPT-4V?

Amidst the surge in GPT-4 Vision use cases, I wanted to explore an efficient yet powerful alternative. It is important to choose the right tool for the job — using GPT-4V for every multimodal task can be overkill, like using a sledgehammer to crack a nut. My approach was to harness the agility and precision of ResNet18 for animal identification. This method not only **curtails costs** but also underscores the adaptability of specialized models in multi-modal realms.

# Tools and Tech

- **ResNet for Animal Detection:** A blazing-fast implementation to identify animals in images, utilizing the ImageNet classification scheme.
- **Cohere LLM:** For generating engaging, informative conversations based on the identified animal.
- **LlamaIndex:** Seamlessly orchestrates the workflow, managing the retrieval of information from pre-indexed Wikipedia articles about animals.
- **Streamlit for UI**

![](/blog/images/1*FE3C63cROo8pLrKpsHjJGg.gif)Gif showing the demo in action

# Deep Dive into app.py

The heart of ‘AInimal Go!’ lies in the `app.py` script, where ResNet, Cohere LLM, and LlamaIndex seamlessly come together. Now, let’s delve into the key aspects of the code:

## 1. Image Capture/Upload

In ‘AInimal Go!’, the flow begins with the user uploading an image or capturing one using their device’s camera. This is a crucial step as it sets the stage for the subsequent interaction with the identified animal.

The code snippet below illustrates how Streamlit is used to create a UI for image upload and capture. It offers two options: a file uploader for selecting an image file and a camera input for real-time capture. Once an image is provided through either method, it’s converted into a byte stream (`BytesIO`) for processing. This streamlining ensures a seamless user experience, whether the image is uploaded from a gallery or captured on the spot.

# Image upload section.
    image_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"], key="uploaded_image", on_change=on_image_upload)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:  # Camera input will be in the middle column
        camera_image = st.camera_input("Take a picture", on_change=on_image_upload)


    # Determine the source of the image (upload or camera)
    if image_file is not None:
        image_data = BytesIO(image_file.getvalue())
    elif camera_image is not None:
        image_data = BytesIO(camera_image.getvalue())
    else:
        image_data = None

    if image_data:
        # Display the uploaded image at a standard width.
        st.session_state['assistant_avatar'] = image_data
        st.image(image_data, caption='Uploaded Image.', width=200)

## 2. Initializing ResNet for Image Classification

Once the user uploads or captures an image, the next critical step is identifying the animal within it. This is where ResNet18, a robust deep learning model for image classification, comes into play.

The function `load_model_and_labels` performs two key tasks:

- **Loading Animal Labels:** It starts by loading a subset of ImageNet labels specific to animals. These labels are stored in a dictionary, mapping class IDs to their corresponding animal names. This mapping is essential for interpreting the output of the ResNet model.
- **Initializing ResNet18:** The function then initializes the feature extractor and the ResNet18 model. The feature extractor preprocesses the images to the format required by ResNet18, while the model itself is responsible for the actual classification task.

def load_model_and_labels():
    # Load animal labels as a dictionary
    animal_labels_dict = {}
    with open('imagenet_animal_labels_subset.txt', 'r') as file:
        for line in file:
            parts = line.strip().split(':')
            class_id = int(parts[0].strip())
            label_name = parts[1].strip().strip("'")
            animal_labels_dict[class_id] = label_name

    # Initialize feature extractor and model
    feature_extractor = AutoFeatureExtractor.from_pretrained("microsoft/resnet-18")
    model = ResNetForImageClassification.from_pretrained("microsoft/resnet-18")

    return feature_extractor, model, animal_labels_dict

feature_extractor, model, animal_labels_dict = load_model_and_labels()By integrating ResNet18 in this manner, ‘AInimal Go!’ leverages its speed and accuracy for the crucial task of identifying the animal in the user’s image. This sets the foundation for the engaging and informative conversations that follow.

## 3. Animal Detection with ResNet18

After initializing ResNet18, the next step is to use it for detecting the animal in the uploaded image. The function `get_image_caption` handles this task.

- **Image Preprocessing: **The uploaded image is first opened and then preprocessed using the feature extractor initialized earlier. This preprocessing adapts the image to the format required by ResNet18.
- **Animal Detection:** The preprocessed image is then fed into ResNet18, which predicts the class of the image. The logits (the model’s raw output) are processed to find the class with the highest probability, which corresponds to the predicted animal.
- **Retrieving the Animal Name: **The predicted class ID is mapped to the corresponding animal name using the label dictionary created earlier. This name is then displayed to the user.

def get_image_caption(image_data):
    image = Image.open(image_data)
    inputs = feature_extractor(images=image, return_tensors="pt")

    with torch.no_grad():
        logits = model(**inputs).logits

    predicted_label_id = logits.argmax(-1).item()
    predicted_label_name = model.config.id2label[predicted_label_id]
    st.write(predicted_label_name)
    # Return the predicted animal name
    return predicted_label_name, predicted_label_id

## 4. Validating Animal Presence in Images

To ensure that the conversation in ‘AInimal Go!’ is relevant and engaging, it’s crucial to verify that the uploaded image indeed depicts an animal. This verification is handled by the `is_animal` function.

def is_animal(predicted_label_id):
    # Check if the predicted label ID is within the animal classes range
    return 0 &amp;lt;= predicted_label_id &amp;lt;= 398The function checks if the predicted label ID from ResNet18 falls within the range of animal classes (0 to 398 in ImageNet’s classification). This simple yet effective check is essential for maintaining the app’s focus on animal interactions.

Further in the script, this function is utilized to validate the detected object:

if not (is_animal(label_id)):
    st.error("Please upload image of an animal!")
    st.stop()If the uploaded image does not depict an animal, the app prompts the user to upload an appropriate image, ensuring that the conversation remains on track.

## 5. Initializing LLM

The `init_llm` function initializes the Cohere LLM along with the necessary contexts for storage and service (specify llm and embed_model). It also loads the pre-indexed Wikipedia articles for about 200 animals. The function sets up the environment in which the LLM operates, preparing it for generating responses.

def init_llm(api_key):
    llm = Cohere(model="command", api_key=st.secrets['COHERE_API_TOKEN'])

    service_context = ServiceContext.from_defaults(llm=llm, embed_model="local")
    storage_context = StorageContext.from_defaults(persist_dir="storage")
    index = load_index_from_storage(storage_context, index_id="index", service_context=service_context)

    return llm, service_context, storage_context, indexThis function is critical for setting up the LLM, ensuring that all necessary components are in place for the chat functionality.

## 6. Creating the Chat Engine

The `create_chat_engine` function takes the animal description and utilizes it to create a query engine. This engine is responsible for handling user queries and generating responses based on the identified animal.

def create_chat_engine(img_desc, api_key):
    doc = Document(text=img_desc)

    query_engine = CitationQueryEngine.from_args(
        index,
        similarity_top_k=3,
        citation_chunk_size=512,
        verbose=True
    )

    return query_enginesystem_prompt=f"""
              You are a chatbot, able to have normal interactions. Do not make up information.
              You always answer in great detail and are polite. Your job is to roleplay as an {img_desc}.
              Remember to make {img_desc} sounds while talking but dont overdo it.
              """

response = chat_engine.query(f"{system_prompt}. {user_input}")By creating a query engine specific to the identified animal, this function ensures that the conversations in the app are relevant, informative, and engaging. I have used the CitationQueryEngine to provide the future possibility of showing the sources as well, making the conversations not only engaging but also informative with credible references.

## 7. Bringing It All Together

With all the technical components in place, ‘AInimal Go!’ combines everything into a user-friendly chat interface. Here, users can interact directly with the AI, asking questions and receiving responses about the identified animal. This final interaction loop, skillfully managed by Streamlit, perfectly showcases the seamless integration of vision and language models in the app.

# Wrapping Up

‘AInimal Go!’ represents an exciting fusion of vision models, language models, and Wikipedia, with LlamaIndex serving as the orchestrator that seamlessly integrates ResNet for animal identification and Cohere’s LLM for engaging conversations. This app is a stepping stone to even more innovative visual-language applications. The possibilities are boundless, and your insights can shape its future. I encourage you to explore the demo, experiment with the code, and join me in pushing the boundaries of what AI can achieve in the realm of multimodal interactions.

[GitHub Repo](https://github.com/AI-ANK/AInimalGo-Chat-with-Animals)

[Connect with Me on LinkedIn](https://www.linkedin.com/in/harshadsuryawanshi/)

[LinkedIn Post](https://www.linkedin.com/posts/harshadsuryawanshi_llamaindex-ai-deeplearning-activity-7134632983495327744-M7yy?utm_source=share&amp;utm_medium=member_desktop)

[Live Demo](https://huggingface.co/spaces/AI-ANK/AInimal_Go)