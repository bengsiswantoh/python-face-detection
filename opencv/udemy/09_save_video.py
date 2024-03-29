import cv2 as cv

cap = cv.VideoCapture(0)
result = cv.VideoWriter(
    "videos/output.avi", cv.VideoWriter_fourcc(*'MJPG'), 20.0, (640, 480))

while(cap.isOpened()):
    ret, frame = cap.read()

    if ret == True:
        print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

        result.write(frame)

        cv.imshow("Frame", frame)

        if cv.waitKey(1) & 0xFF == ord("q"):
            break

cap.release()
result.release()
cv.destroyAllWindows()
