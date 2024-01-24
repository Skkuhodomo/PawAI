import cv2
import matplotlib.pyplot as plt
import tensorflow_datasets as tfds
import tensorflow as tf
from keras.applications.resnet import ResNet50, decode_predictions, preprocess_input

data_train, ds_info = tfds.load('cats_vs_dogs', split=[tfds.Split.TRAIN], with_info=True)
images = [one['image'].numpy() for one in data_train[0].take(30)]
resnet50_pre = ResNet50(weights='imagenet', input_shape=(224, 224, 3))
resnet50_pre.summary()

def pred_img(img):
    img_resized = cv2.resize(img, (224, 224))
    img_resized = preprocess_input(img_resized)
    pred = resnet50_pre.predict(img_resized.reshape([1, 224, 224, 3]))
    decoded_pred = decode_predictions(pred)

    for i, instance in enumerate(decoded_pred[0]):
        print('{}위: {} ({:.2f}%)'.format(i + 1, instance[1], instance[2] * 100))

# 예시 이미지 중 하나를 선택하여 예측 수행
pred_img(images[0])
