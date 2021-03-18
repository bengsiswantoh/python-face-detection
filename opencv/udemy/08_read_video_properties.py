import cv2 as cv

cap = cv.VideoCapture(0)
print(cap.isOpened())

while(cap.isOpened()):
    ret, frame = cap.read()

    print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

    cv.imshow("Frame", frame)

    if cv.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv.destroyAllWindows()
