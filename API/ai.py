import tensorflow as tf
import tensorflow_hub as hub
import os
import numpy as np
import tensorflow_datasets as tfds
import warnings
warnings.filterwarnings('ignore')
import PIL
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential


# classes
stress_classes = ['healthy', 'water_stressed']
bean_classes = ['angular_leaf_spot', 'bean_rust', 'healthy']
def bean_model():
    return tf.keras.models.load_model('static/Models2/last_bean_model')

# Check its architecture
# bean_model().summary()

def water_stress():
    return tf.keras.models.load_model('static/STRESSED_Model/Irrigate_model')

# Check its architecture
# water_stress().summary()
def get_local(image):
    img = tf.keras.utils.load_img(image, target_size=(224, 224))
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0) # Create a batch
    return img_array

def predict2(image):
    image = get_local(image)  
    prediction = bean_model().predict(image)
    score = tf.nn.softmax(prediction[0])
    return {"prediction":bean_classes[np.argmax(score)],"score":np.max(score) * 100}

def predict(image):
    image = get_local(image)  
    predictions = water_stress().predict(image)
    prediction = bean_model().predict(image)
    score = tf.nn.softmax(predictions[0])
    score2 = tf.nn.softmax(prediction[0])
    data = {
            "stress":stress_classes[np.argmax(score)],
            "stress_score":np.max(score) * 100,
            "bean":bean_classes[np.argmax(score2)],
            "bean_score":np.max(score2) * 100
        }
    return data
# images = get_local('media/garden_pic/img_2022-11-28-221626.627744.jpg')
# predictions = bean_model().predict(images)
# score = tf.nn.softmax(predictions[0])
# print(np.max(score) * 100)
# print(bean_classes[np.argmax(score)])
# data = predict('media/garden_pic/img_2022-11-28-221626.627744.jpg')
# print(data)
