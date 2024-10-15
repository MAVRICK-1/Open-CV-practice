import cv2
import os

img = cv2.imread(os.path.join('.','images','navamita.jpg')) # Read image from file
print(img.shape) # Display the shape of the image

# Resize the image
resized_img = cv2.resize(img, (300, 300)) # Resize the image to 300x300 pixels (width x height) arguments are (image, (width, height))  it doesn't follow the same order as the shape of the image
print(resized_img.shape) # Display the shape of the resized image

cv2.imshow('Original Image', img)
cv2.imshow('Resized Image', resized_img)
cv2.waitKey(0)