import cv2

# Read video from webcam
video = cv2.VideoCapture(0)  # 0 is the index of the webcam

while True:
    ret, frame = video.read() # ret is a boolean value that indicates if the frame is read correctly, frame is the image frame
    if ret:
        cv2.imshow('frame', frame) # Display the frame
        if cv2.waitKey(40) & 0xFF == ord('q'):  # Delay 40ms and check if 'q' is pressed
            break

# Release the video capture object
video.release()
cv2.destroyAllWindows()  # Close all windows