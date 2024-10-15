import cv2

import os

# Load the image
image = cv2.imread(os.path.join('images', 'navamita.jpg'))

# Convert the image to grayscale
#gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # Convert the image to grayscale
img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # Convert the image to RGB format for displaying with matplotlib library

img_hsb = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

cv2.imshow('HSB',img_hsb)
# Display the grayscale image
cv2.imshow('RGB Image', img_rgb)
cv2.imshow('Original Image', image)

cv2.waitKey(0)