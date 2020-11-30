import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
import matplotlib.cm as cm

data_path = '../Data/Sorted/Pneumonia/one'
model = keras.models.load_model('../model1.h5')
conv_layer = 'conv2d_2'


test_data = ImageDataGenerator(rescale=1. / 255)
test_generator = test_data.flow_from_directory(
    data_path,
    target_size=(512, 512),
    batch_size=1,
    class_mode='binary'
)

scores = model.predict()



def get_img_array(img_path, size):
    img = keras.preprocessing.image.load_img()

