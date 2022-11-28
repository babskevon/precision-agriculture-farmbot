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

def bean_model():
    return tf.keras.models.load_model('Models2/last_bean_model')

# Check its architecture
# bean_model.summary()

def water_stress():
    return tf.keras.models.load_model('STRESSED_Model/Irrigate_model')

# Check its architecture
# stress_model.summary()