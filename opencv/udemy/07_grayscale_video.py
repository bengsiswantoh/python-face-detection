import cv2 as cv

cap = cv.VideoCapture(0)

while(True):
    ret, frame = cap.read()

    gray_vid = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow("Frame", gray_vid)

    if cv.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv.destroyAllWindows()
