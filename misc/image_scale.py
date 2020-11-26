import os
import cv2
import matplotlib.pyplot as plt

IMAGE_TARGET_RESOLUTION_X = 512
IMAGE_TARGET_RESOLUTION_Y = 512
DIR = '../Data/Sorted/Pneumonia/'

for filename in os.listdir(DIR):
    pathsrt = str(DIR + filename)
    image = cv2.imread(pathsrt, cv2.IMREAD_GRAYSCALE)
    #plt.imshow(image)
    #cv2.imshow('image', image)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    #plt.show()
    image = cv2.resize(image, (IMAGE_TARGET_RESOLUTION_X, IMAGE_TARGET_RESOLUTION_Y), interpolation = cv2.INTER_AREA)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    image = clahe.apply(image)
    cv2.imwrite(str('../Data/Sorted/512/Pneumonia/' + filename), image)


