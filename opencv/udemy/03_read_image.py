import cv2 as cv

img = cv.imread("images/chara_16.png", -1)
print(img)

cv.imshow("image", img)

cv.waitKey(delay=0)
cv.destroyAllWindows()
