import cv2
import os

# Load the image
image = cv2.imread(os.path.join('images', 'navamita.jpg'))

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # Convert the image to grayscale

thresh = cv2.blur(gray_image, (3,3)) # Apply a blur filter to the image, arguments: source image, kernel size where (5,5) is the kernel size
ret, thresh1 = cv2.threshold(thresh, 50, 255, cv2.THRESH_BINARY) # Binary thresholding at 127 intensity level , arguments: source image, threshold value, max value, thresholding type, threshold value defined by user
ret, thresh2 = cv2.threshold(thresh, 50, 255, cv2.THRESH_BINARY_INV) # Binary thresholding at 127 intensity level , arguments: source image, threshold value, max value, thresholding type, threshold value defined by user


cv2.imshow('Original Image', image)
cv2.imshow('Binary Threshold', thresh1)
cv2.imshow('Binary Threshold Inverse', thresh2)


cv2.waitKey(0)