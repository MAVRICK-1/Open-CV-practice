import cv2

import os

# Load the image
image = cv2.imread(os.path.join('images','handwritten.png'));

adaptive_thresh = cv2.adaptiveThreshold(
    cv2.cvtColor(image, cv2.COLOR_BGR2GRAY), # Convert the image from BGR to grayscale
    255, # Maximum value to use if a pixel value meets the threshold condition (set to white)
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C, # Adaptive thresholding method: use Gaussian-weighted sum of neighborhood values
    cv2.THRESH_BINARY, # Type of thresholding: convert pixels above the threshold to max value (255), below to 0
    21, # Block size: size of the neighborhood area used for calculating the threshold for each pixel (must be odd)
    30 # Constant subtracted from the calculated mean (fine-tunes thresholding)
)

cv2.imshow('Original Image', image)
cv2.imshow('Adaptive Threshold', adaptive_thresh)   

cv2.waitKey(0)