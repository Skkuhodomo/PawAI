import cv2
import tensorflow_datasets as tfds
import tensorflow as tf
from keras.applications.resnet import ResNet50, decode_predictions, preprocess_input
from PIL import Image
import numpy as np
import streamlit as st
data_train, ds_info = tfds.load('cats_vs_dogs', split=[tfds.Split.TRAIN], with_info=True)
images = [one['image'].numpy() for one in data_train[0].take(30)]
resnet50_pre = ResNet50(weights='imagenet', input_shape=(224, 224, 3))
resnet50_pre.summary()

def pred_img(img_bytes):
    # Convert BytesIO to NumPy array
    img = Image.open(img_bytes).convert('RGB')
    img = np.array(img)
    
    img_resized = cv2.resize(img, (224, 224))
    img_resized = preprocess_input(img_resized)
    img_resized = img_resized.reshape((1, 224, 224, 3))  # Reshape the input
    pred = resnet50_pre.predict(img_resized)
    decoded_pred = decode_predictions(pred)

    if decoded_pred is not None and len(decoded_pred[0]) > 0:
        for i, instance in enumerate(decoded_pred[0]):
            st.write('{}: {} ({:.2f}%)'.format(i + 1, instance[1], instance[2] * 100))
        st.header('I think your pet is a {}'.format(decoded_pred[0][0][1]))
    else:
        print("Unable to decode predictions.")

