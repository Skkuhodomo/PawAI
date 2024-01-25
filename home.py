import streamlit as st
st.title("Welcome!")

col1, col2, col3= st.columns(3)
with col1:
    st.header(":paw_prints:")
    st.write("PawAI")
    st.write("Upload an image! PawAI will help identify the breed of your pet.")
    st.write("This app utilizes the TensorFlow and Keras frameworks to load the cats_vs_dogs dataset from TensorFlow Datasets. ")
with col2:
    st.header(":robot_face:")
    st.write("Chat with GPT")
    st.write("Engage in a conversation about your pets with GPT. Anything goes! However, refrain from using it for information related to 'what to eat' or 'how to make treats,' as incorrect information may be provided. Please avoid using it for such purposes")
    
with col3:
    st.header(":art:")
    st.write("DALL-E Image generator")
    st.write("Share your pet's unique traits, from behavior to personality. Introducing the DALL-E app that paints a picture of their family.")
st.write("")
st.write("")

st.image("home_image.jpg")

st.write("The motivation behind creating this app is evident. Many individuals are likely to adopt 'stray dogs.' However, as someone who has personally adopted and cared for a stray dog, I realize that we often lack information about their early experiences and family background. At times, we might not even know their specific breed. Through the app I developed, you can identify your pet, engage in meaningful conversations, and capture beautiful family moments!")