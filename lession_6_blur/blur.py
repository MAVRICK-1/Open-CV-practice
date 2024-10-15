import cv2
import os

img_path = os.path.join('.','images','navamita.jpg')
image = cv2.imread(img_path)

# Apply average blur
average_blurred = cv2.blur(image, (5,5)) # (5,5) is the kernel size
# Apply median blur
median_blurred = cv2.medianBlur(image, 5) # 5 is the kernel size (it must be an odd number) passed to the medianBlur function  (refer to the documentation for more details)
# Apply Bilateral filter (used for noise removal while keeping the edges sharp)
bilateral_blurred = cv2.bilateralFilter(image, 9, 75, 75) # 9 is the diameter of the pixel neighbourhood, 75 is the sigma color and 75 is the sigma space (refer to the documentation for more details) 

# Apply Gaussian blur
Gussina_blurred = cv2.GaussianBlur(image, (5,5), 0) # (5,5) is the kernel size and 0 is the standard deviation in X direction of the kernel (0 means that it is calculated using the kernel size) 
#kernel is a matrix that is used to blur the image. The bigger the kernel, the more the blur.

cv2.imshow('Original Image', image)
cv2.imshow('Average Blurred Image', average_blurred)
cv2.imshow('Median Blurred Image', median_blurred)
cv2.imshow('Bilateral Blurred Image', bilateral_blurred)
cv2.imshow('Gaussian Blurred Image', Gussina_blurred)

cv2.waitKey(0)