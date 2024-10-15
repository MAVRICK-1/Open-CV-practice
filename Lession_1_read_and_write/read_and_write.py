import cv2 #importing opencv library
import os #os module provides a way of using operating system dependent functionality

image_path=os.path.join('.','images','navamita.jpg') #os.path.join('.','images','navamita.jpg') where '.' is the current directory, 'images' is the folder where the image is stored and 'navamita.jpg' is the name of the image

#read image

img = cv2.imread(image_path)

#write image

cv2.imwrite(os.path.join('.','images_out','navamita_out.jpg'),img) #first argument is the path where the image is to be saved and second argument is the image to be saved ,
#os.path.join('.','images_out','navamita_out.jpg') where '.' is the current directory, 'images_out' is the folder where the image is to be saved and 'navamita_out.jpg' is the name of the image to be saved


#visualize image

cv2.imshow('image',img) #image is the window name and img is the image to be displayed
cv2.waitKey(5000) #waits for any key to be pressed , here 5000 is 5000 milisec and 0 it will open for ever