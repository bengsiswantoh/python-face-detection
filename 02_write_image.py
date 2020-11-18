import cv2 as cv

img = cv.imread("images/chara_16.png", 1)

# cv.imshow("image", img)

cv.imwrite("images/test.png", img)

# cv.waitKey(0)
