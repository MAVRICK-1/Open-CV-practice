import cv2
import os

import numpy as np

# Load the image
image = cv2.imread(os.path.join('images', 'navamita.jpg'))

# edge detection
img_edge  =cv2.Canny(image,40,200) # Canny edge detection, arguments: source image, threshold1, threshold2 , threshold1 and threshold2 are the minimum and maximum intensity gradient values respectively 
#threshold is the minimum intensity gradient value. If the intensity gradient is below this value, it is considered not an edge. If the intensity gradient is above this value, it is considered an edge.

img_edge_d = cv2.dilate(img_edge, np.ones((3,3), np.uint8)) # Dilate the edges, arguments: source image, kernel, number of iterations , kernel is the matrix used for dilation, number of iterations is the number of times dilation is applied to the image
# np.ones is a matrix of ones with the size (3,3) and data type np.uint8

img_edge_er = cv2.erode(img_edge_d, np.ones((3,3), np.uint8)) # Erode the edges, arguments: source image, kernel, number of iterations , kernel is the matrix used for erosion, number of iterations is the number of times erosion is applied to the image

cv2.imshow('img_edge',img_edge);
cv2.imshow('img_edge_d',img_edge_d);
cv2.imshow('img_edge_er',img_edge_er);
cv2.waitKey(0)