import tensorflow as tf
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from tensorflow import keras
from vis.visualization import visualize_cam, visualize_saliency, visualize_activation, overlay
from vis.utils import utils
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator

img_width, img_height = 512, 512
input_shape = (img_width, img_height, 3)
batch_size = 4

data_path = '../Data/Sorted/Pneumonia'
model = keras.models.load_model('../model1.h5')


test_data = ImageDataGenerator(rescale=1. / 255)
test_generator = test_data.flow_from_directory(
    data_path,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='binary'
)

test_shape = tf.data.Dataset.from_generator(lambda: test_generator,
                                            output_types=(tf.float32, tf.int32),
                                            output_shapes=([None, 512, 512, 1]))

images = next(iter(test_shape))

predictions = model.predict(images)


def visualize_cams(images, predictions):
    rows, cols = 3, 3
    fig, axes = plt.subplot(rows, cols)
    fig.set_size_inches(2*2*cols, 2.2*2*rows)
    fig.suptitle('cams')
    current_index = 0
    for i in range(rows):
        for j in range(cols):
            image = images[current_index]
            image_rgb = tf.image.grayscale_to_rgb(image)
            visualization = visualize_cam(model, -1, filter_indices=0, seed_input=image, penultimate_layer_idx=-4)
            axes[i, j].imshow(tf.image.grayscale_to_rgb(image))
            axes[i, j].imshow(visualization, interpolation='nearest', alpha=0.6)
            axes[i, j].set_xticks([])
            axes[i, j].set_yticks([])
    plt.show()

    visualize_cams(images, predictions)
