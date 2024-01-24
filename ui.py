import streamlit as st
import classifier as cl

st.title("Dog vs Cat")

img_file = st.file_uploader('이미지를 업로드 하세요.', type=['png', 'jpg', 'jpeg'])

if img_file:
    st.image(img_file, caption='Uploaded Image.', use_column_width=True)
    cl.pred_img(img_file)

st.sidebar.title("About")
st.sidebar.info("This is a simple image classification web app to predict dog or cat using ResNet50.")  
st.sidebar.title("How it works?")   



