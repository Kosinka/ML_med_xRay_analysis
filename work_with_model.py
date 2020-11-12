import os
import tensorflow
import keras
import cv2 as cv


from tensorflow.python.keras.preprocessing.image import ImageDataGenerator
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Conv2D, MaxPooling2D
from tensorflow.python.keras.layers import Activation, Dropout, Flatten, Dense

#data dir's
train_dir = os.curdir + '/Data/Sorted/'
val_dir = os.curdir + '/Data/Val/'
test_dir = os.curdir + '/Data/Test_2/'

img_width, img_height = 512, 512
input_shape = (img_width, img_height, 3)
epochs = 3
batch_size = 16
nb_train_samples = 40430
nb_val_samples = 7339
nb_test_samples = 14842

datagen = ImageDataGenerator(rescale=1. / 255)
test_generator = datagen.flow_from_directory(
    test_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='binary'
)


model = keras.models.load_model('model1.h5')
scores = model.evaluate_generator(test_generator, nb_test_samples)
print("Аккуратность на тестовых данных: %.2f%%" % (scores[1]*100))
