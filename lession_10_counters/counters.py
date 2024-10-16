import cv2
import os

# Load the image
image = cv2.imread(os.path.join('.','images', 'birds.jpg'))

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 

# Binary thresholding at 127 intensity level
ret, thresh = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY_INV) # arguments: source image, threshold value, max value, thresholding type (in this case cv2.THRESH_BINARY_INV) 

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # Find the contours in the image, arguments: source image, contour retrieval mode, contour approximation method
#define more
#contour retrieval mode: cv2.RETR_TREE retrieves all of the contours and reconstructs a full hierarchy of nested contours
#contour approximation method: cv2.CHAIN_APPROX_SIMPLE removes all redundant points and compresses the contour, thereby saving memory
#hierarchy is the relationship between the contours in the image
#it returns two values: contours and hierarchy
#contours is a list of all the contours in the image
print(len(contours)) # Print the number of contours in the image
# contour means the boundary of an object
for cnt in contours:
    if cv2.contourArea(cnt) > 200:
        #cv2.drawContours(image, cnt, -1, (0,255,0), 1) # Draw the contours on the image, arguments: source image, contours, contour index , color, thickness, we are using original image as source image because we want to draw the contours on the original image
        
        x1, y1, w, h = cv2.boundingRect(cnt) # Get the bounding rectangle of the contour, arguments: contour
        #it returns 4 values: x1, y1, width, height
        cv2.rectangle(image, (x1, y1), (x1+w, y1+h), (0,255,0), 2)
        #cv2.putText(image, 'Bird', (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)
# Display the original and binary threshold images
# counter index is the index of the contour to be drawn. If it is -1, all the contours are drawn
cv2.imshow('Original Image', image)
#cv2.imshow('Binary Threshold', thresh)

cv2.waitKey(0)
