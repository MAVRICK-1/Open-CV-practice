import cv2
import mediapipe as mp
import pyautogui
import time
import math

# Initialize Mediapipe hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

# Capture video from webcam
cap = cv2.VideoCapture(0)

# Screen dimensions for cursor scaling
screen_width, screen_height = pyautogui.size()

# Variables for double-tap detection
last_tap_time = 0
tap_timeout = 0.3  # 300 milliseconds for detecting a double-tap
last_tap_position = None

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame horizontally for a mirror effect
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape

    # Convert the frame to RGB (Mediapipe requires RGB input)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame to find hand landmarks
    result = hands.process(rgb_frame)

    # If landmarks are detected, process them
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            # Get the tip of the index finger (landmark 8)
            index_finger_tip = hand_landmarks.landmark[8]

            # Convert the landmark to screen coordinates
            cursor_x = int(index_finger_tip.x * screen_width)
            cursor_y = int(index_finger_tip.y * screen_height)

            # Move the mouse cursor
            pyautogui.moveTo(cursor_x, cursor_y)

            # Double-tap detection
            current_time = time.time()
            if last_tap_position:
                # Calculate the distance between the current and last tap position
                distance = math.sqrt(
                    (cursor_x - last_tap_position[0]) ** 2 +
                    (cursor_y - last_tap_position[1]) ** 2
                )

                # If the distance is small and within the timeout, perform a click
                if distance < 20 and (current_time - last_tap_time) < tap_timeout:
                    pyautogui.click()
                    last_tap_time = 0  # Reset to avoid multiple clicks
                    last_tap_position = None
                else:
                    # Update tap position and time
                    last_tap_position = (cursor_x, cursor_y)
                    last_tap_time = current_time
            else:
                # Set the first tap position and time
                last_tap_position = (cursor_x, cursor_y)
                last_tap_time = current_time

            # Draw hand landmarks on the frame
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Display the frame
    cv2.imshow("Hand Cursor Control", frame)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the OpenCV window
cap.release()
cv2.destroyAllWindows()
