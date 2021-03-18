import cv2 as cv

# img = cv.imread("images/bill warren.jpeg", -1)
img = cv.imread("images/bill warren.jpeg", 0)
print(img)

cv.imshow("image", img)

cv.waitKey(delay=0)
cv.destroyAllWindows()
