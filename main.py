import cv2 as cv

cap = cv.VideoCapture(0)

while(cap.isOpened()):
    ret, frame = cap.read()

    cv.imshow("Frame", frame)

    if cv.waitKey(20) & 0xFF == ord("q"):
        break

cap.release()
cv.destroyAllWindows()
