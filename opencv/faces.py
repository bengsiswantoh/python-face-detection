import cv2 as cv
import pickle

face_cascade = cv.CascadeClassifier(
    "cascades/haarcascade_frontalface_default.xml")
recognizer = cv.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")

labels = {}
with open("label.pickle", "rb") as f:
    og_labels = pickle.load(f)
    labels = {v: k for k, v in og_labels.items()}

cap = cv.VideoCapture(0)

while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    face_detect = face_cascade.detectMultiScale(
        gray, scaleFactor=1.5, minNeighbors=5)

    for(x, y, w, h) in face_detect:
        # print(x, y, w, h)
        roi_gray = gray[y:y+h, x:x+w]  # (ycord_start, ycord_end)
        roi_color = frame[y:y+h, x:x+w]

        # recognize? deep learning model predict (keras, tensorflow, pytorch, scikit learn)
        id, conf = recognizer.predict(roi_gray)
        if conf >= 45:
            print(id)
            print(labels[id])
            font = cv.FONT_HERSHEY_SIMPLEX
            name = labels[id]
            color = (255, 255, 255)
            stroke = 2
            cv.putText(frame, name, (x, y), font, 1, color, stroke, cv.LINE_AA)

        img_item = "images/my-image.png"
        cv.imwrite(img_item, roi_gray)

        color = (255, 0, 0)  # BGR 0 -255
        stroke = 2
        end_cord_x = x+w
        end_cord_y = y+h
        cv.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)

    # display frame
    cv.imshow("Frame", frame)

    if cv.waitKey(20) & 0xFF == ord("q"):
        break

cap.release()
cv.destroyAllWindows()
