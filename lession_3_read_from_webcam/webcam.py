import cv2

# Read video from webcam
video = cv2.VideoCapture(0)  # 0 is the index of the webcam

while True:
    ret, frame = video.read()
    if ret:
        cv2.imshow('frame', frame)
        if cv2.waitKey(40) & 0xFF == ord('q'):  # Delay 40ms and check if 'q' is pressed
            break

# Release the video capture object
video.release()
cv2.destroyAllWindows()  # Close all windows