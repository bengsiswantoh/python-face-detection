import cv2
import numpy as np

# initialize the HOG descriptor/person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

cap = cv2.VideoCapture(0)

process_this_frame = True

while True:
    # Grab a single frame of video
    ret, frame = cap.read()

    # Only process every other frame of video to save time
    if process_this_frame:
        # detect people in the image
        # returns the bounding boxes for the detected objects
        boxes, weights = hog.detectMultiScale(frame, winStride=(8, 8))

        boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])

        print(boxes)

        for (xA, yA, xB, yB) in boxes:
            # display the detected boxes in the colour picture
            cv2.rectangle(frame, (xA, yA), (xB, yB),
                          (0, 255, 0), 2)

    process_this_frame = not process_this_frame

    # Display the resulting image
    cv2.imshow("Frame", frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()
