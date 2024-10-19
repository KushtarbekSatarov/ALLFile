import warnings

warnings.filterwarnings("ignore")  # Suppress warnings

import cv2
import numpy as np
import HandTrackingModule as htm
import time
import pyautogui  # Use pyautogui for mouse control

# Camera resolution
wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)  # Use 0 for the default camera
if not cap.isOpened():
    print("Error: Camera not opened.")
    exit()  # Exit if the camera fails to open

cap.set(3, wCam)
cap.set(4, hCam)

detector = htm.HandDetector(maxHands=1)  # Initialize the hand detector

# Define screen size for mapping
screen_width, screen_height = pyautogui.size()

while True:
    success, img = cap.read()
    if not success:
        print("Error: Could not read frame.")
        break  # Exit if frame capture fails

    img = detector.findHands(img)  # Find hands in the image
    lmList = detector.findPosition(img)  # Get hand landmarks position

    if len(lmList) != 0:
        # Get index finger tip position
        index_x, index_y = lmList[8][1], lmList[8][2]

        # Map the index finger position to the screen size
        x_screen = np.interp(index_x, [0, wCam], [0, screen_width])
        y_screen = np.interp(index_y, [0, hCam], [0, screen_height])

        # Invert the x-coordinate to match the hand movement
        x_screen = screen_width - x_screen  # Invert the x-coordinate

        # Move the mouse to the mapped position
        pyautogui.moveTo(x_screen, y_screen)

        # Check for click (using thumb and index finger distance)
        thumb_x, thumb_y = lmList[4][1], lmList[4][2]
        distance = np.sqrt((index_x - thumb_x) ** 2 + (index_y - thumb_y) ** 2)

        if distance < 50:  # Threshold distance for clicking
            pyautogui.click()  # Perform a click

    cv2.imshow("Image", img)
    cv2.waitKey(1)

cap.release()  # Release the camera when done
cv2.destroyAllWindows()  # Close all OpenCV windows
