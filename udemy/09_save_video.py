import cv2 as cv

cap = cv.VideoCapture(0)
FourCC = cv.VideoWriter_fourcc(*"VXID")
result = cv.VideoWriter("videos/test.avi", FourCC, 20.0, (640, 480))

while(cap.isOpened()):
    ret, frame = cap.read()

    if ret == True:
        print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

        result.write(frame)

        cv.imshow("Frame", frame)

        if cv.waitKey(1) & 0xFF == ord("e"):
            break

cap.release()
result.release()
cv.destroyAllWindows()
