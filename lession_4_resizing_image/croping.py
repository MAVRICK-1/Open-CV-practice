import cv2

import os

img = cv2.imread(os.path.join('.','images','navamita.jpg')) # Read image from file

print(img.shape) # Display the shape of the image

# Crop the image

cropped_img = img[100:300, 200:400] # Crop the image from (100, 200) to (300, 400) pixels (height x width)

cv2.imshow('Original Image', img)
cv2.imshow('Cropped Image', cropped_img)

cv2.waitKey(0)