import cv2
from fer import FER

# Initialize the emotion detector
detector = FER()

# Open a video capture (webcam)
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    success, frame = cap.read()
    if not success:
        print("Error: Could not read frame.")
        break  # Exit if frame capture fails

    # Detect emotions in the frame
    emotions = detector.detect_emotions(frame)

    # Draw rectangles around detected faces and display emotions
    for emotion in emotions:
        # Get the bounding box and the dominant emotion
        box = emotion["box"]
        dominant_emotion = emotion["emotions"]
        dominant_emotion_name = max(dominant_emotion, key=dominant_emotion.get)

        # Draw a rectangle around the face
        cv2.rectangle(frame,
                      (int(box[0]), int(box[1])),
                      (int(box[0] + box[2]), int(box[1] + box[3])),
                      (0, 255, 0), 2)  # Green rectangle

        # Display the emotion label
        cv2.putText(frame, dominant_emotion_name,
                    (int(box[0]), int(box[1] - 10)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9,
                    (36, 255, 12), 2)  # Emotion text above the face

    # Display the resulting frame
    cv2.imshow("Face Emotion Recognition", frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()
