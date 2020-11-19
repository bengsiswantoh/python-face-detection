import cv2 as cv

face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv.imread("images/chara_16.png")
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
