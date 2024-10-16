import cv2
import os
import numpy as np
img = cv2.imread(os.path.join('images', 'whiteboard.png'))

#line 
cv2.line(img, (100,100), (250,250), (255,0,0), 5) # arguments: source image, starting point, ending point, color, thickness 

cv2.rectangle(img, (100,100), (250,250), (0,255,0), 5) # arguments: source image, top-left corner, bottom-right corner, color, thickness
'''
-1 thickness means that the rectangle is filled with the color
'''
cv2.circle(img, (175,175), 75, (0,0,255), 5) # arguments: source image, center, radius, color, thickness

cv2.polylines(img, [np.array([[100,100],[250,250],[300,150],[200,50]], np.int32)], True, (255,255,0), 5) # arguments: source image, points, isClosed, color, thickness
# [np.array([[100,100],[250,250],[300,150],[200,50]], np.int32)] is a list of points that form the polygon (in this case a quadrilateral) 

cv2.putText(img, 'Whiteboard', (100,400), cv2.FONT_HERSHEY_SIMPLEX, 4, (255,255,255), 2) # arguments: source image, text, bottom-left corner, font, font scale, color, thickness
cv2.imshow('image', img)
cv2.waitKey(0)