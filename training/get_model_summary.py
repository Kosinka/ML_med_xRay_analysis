from tensorflow.python.keras.models import Sequential
import keras

model = keras.models.load_model('../model1.h5')
model.summary()
