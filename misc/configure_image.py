import os
import cv2

image_path = 'D:/Users/kosin/PycharmProjects/Neuro_1/Data/misc_data/00000001_000.png'
cv2image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
print(cv2image.shape)
cv2image2 = cv2.resize(cv2image, (512, 512))
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
cv2image3 = clahe.apply(cv2image2)

print('0')
cv2.imshow('image2', cv2image3)
cv2.imshow('image1', cv2image2)
cv2.waitKey(0)
cv2.imwrite(str('/Data/misc_data/cv2image.png'), cv2image2)


