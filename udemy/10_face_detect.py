import cv2 as cv

face_cascade = cv.CascadeClassifier(
    "cascades/haarcascade_frontalface_default.xml")

img = cv.imread("images/chara_16.png")
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
face_detect = face_cascade.detectMultiScale(gray_img, 1.1, 4)

for(x, y, w, h) in face_detect:
    cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), thickness=2)

cv.imshow("image", img)
cv.waitKey(0)
