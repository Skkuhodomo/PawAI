import streamlit as st
import classifier as cl

st.title("Who are you?")

img_file = st.file_uploader('Upload', type=['png', 'jpg', 'jpeg'])

if img_file:
    st.image(img_file, caption='Uploaded Image.', use_column_width=True)
    cl.pred_img(img_file)






