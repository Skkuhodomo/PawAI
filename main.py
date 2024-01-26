from st_pages import Page, Section, show_pages, add_page_title
import streamlit as st  
show_pages(
    [
        Page("main.py", "Home", "🏠"),
        Page("ui_classifier.py", "PawAI", ":paw_prints:"),
        Page("gpt-vision.py", "GPT-vision", ":robot_face:"),    
    ]
)
st.title("Welcome!")

col1, col2, col3= st.columns(3)
with col1:
    st.header(":paw_prints:")
    st.write("PawAI")
    st.write("Upload an image! PawAI will help identify the breed of your pet.")
    st.write("This app utilizes the TensorFlow and Keras frameworks to load the cats_vs_dogs dataset from TensorFlow Datasets. ")
with col2:
    st.header(":art:")
    st.write("GPT-vision")
    st.write("Share your pet's image. GPT Vision will analyze the personality and behavior of your pet based on the provided image.")
    
with col3:
    st.header(":dog:")
    st.image("home_dog.jpg")
    st.write("Notice: If your pet is a hybrid, PawAI will identify the breed of your pet")
    
st.write("")
st.write("")

st.image("home_image.jpg")

st.write("The motivation behind creating this app is evident. Many individuals are likely to adopt 'stray dogs.' However, as someone who has personally adopted and cared for a stray dog, I realize that we often lack information about their early experiences and family background. At times, we might not even know their specific breed. Through the app I developed, you can identify your pet!")