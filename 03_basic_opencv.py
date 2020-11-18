import cv2 as cv

img = cv.imread("images/chara_16.png", 1)

cv.imshow("image", img)

e = cv.waitKey()

if e == 27:
    cv.destroyAllWindows()
elif e == "s":
    cv.imwrite("images/test.png", img)
    cv.destroyAllWindows()
