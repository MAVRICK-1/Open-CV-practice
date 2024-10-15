import cv2
import os

video_path = os.path.join('.','video','killmonger.mp4')

# Read video from file

video = cv2.VideoCapture(video_path) # Read video from file

#visulize video

ret = True
while ret:
    ret, frame = video.read() # ret is a boolean variable that returns True if the frame is read correctly and False otherwise, frame is the image frame
    if ret: #we used if statement to ret is True to avoid error when ret is False 
        cv2.imshow('frame', frame)
        cv2.waitKey(40) # Delay 40ms to show the next frame
        
video.release() # Release the video
cv2.destroyAllWindows() # Close all windows