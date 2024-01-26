import streamlit as st
import openai
from langchain.chat_models import ChatOpenAI
from langchain.callbacks.base import BaseCallbackHandler
from langchain.schema import HumanMessage
import streamlit as st
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.vectorstores import FAISS
import tempfile
from openai import OpenAI
import os, base64, requests
import ui_classifier as cl
st.subheader("**GPT will analysis your pet image**")
openai_api_key = st.text_input(
        label="$\\hspace{0.25em}\\texttt{Your OpenAI API Key}$",
        type="password",
        placeholder="sk-",
        label_visibility="collapsed",
        )

def encode_image(image_file):
    return base64.b64encode(image_file.getvalue()).decode("utf-8")


# Initialize the OpenAI client with the API key
client = OpenAI(api_key=openai_api_key)


# File uploader allows user to add their own image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

# Toggle for showing additional details input
show_details = st.toggle("Add details about the image", value=False)

if show_details:
    # Text input for additional details about the image, shown only if toggle is True
    additional_details = st.text_area(
        "Add any additional details or context about your pet here:",
        disabled=not show_details
    )
  
# Button to trigger the analysis
analyze_button = st.button("Analyse the Pet Image", type="secondary")

# display uploaded images
if uploaded_file:
    # Display the uploaded image
    with st.expander("Image", expanded = True):
        st.image(uploaded_file, caption=uploaded_file.name, use_column_width=True)

# Check if an image has been uploaded, if the API key is available, and if the button has been pressed
if uploaded_file is not None and analyze_button:

    with st.spinner("Analysing the image ..."):
        # Encode the image
        base64_image = encode_image(uploaded_file)
    
        # Optimized prompt for additional clarity and detail
        prompt_text = (
            "You love animals. You have spent a long time as a veterinarian."
            "Your task is to identify the type of animal by looking at a picture and understand the behavior and mood of the animal."
            "but You should express image in a more descriptive manner."
        )
    
        if show_details and additional_details:
            prompt_text += (
                f"\n\nAdditional Context Provided by the User:\n{additional_details}"
            )
    
        # Create the payload for the completion request
        messages = [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt_text},
                    {
                        "type": "image_url",
                        "image_url": f"data:image/jpeg;base64,{base64_image}",
                    },
                ],
            }
        ]
    
        # Make the request to the OpenAI API
        try:
            # Without Stream
            
            # response = client.chat.completions.create(
            #     model="gpt-4-vision-preview", 
            #     messages=messages, 
            #     max_tokens=500, 
            #     stream=False
            # )
    
            # Stream the response
            full_response = ""
            message_placeholder = st.empty()
            for completion in client.chat.completions.create(
                model="gpt-4-vision-preview", 
                messages=messages, 
                max_tokens=500, 
                stream=True
            ):
                # Check if there is content to display
                if completion.choices[0].delta.content is not None:
                    full_response += completion.choices[0].delta.content
                    message_placeholder.markdown(full_response + "▌")
                    
            # Final update to placeholder after the stream ends
            message_placeholder.markdown(full_response)
    
            # Display the response in the app
            # st.write(response.choices[0].message.content)
        except Exception as e:
            st.error(f"An error occurred: {e}")
else:
    # Warnings for user action required
    if not uploaded_file and analyze_button:
        st.warning("Please upload an image.")
        