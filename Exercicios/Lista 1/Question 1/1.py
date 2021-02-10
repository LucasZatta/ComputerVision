import cv2 as cv
import sys
img = cv.imread("landscape.png")
if img is None:
    sys.exit("Error reading image")

cv.imshow("Display image", img)

cv.waitKey(0)
cv.destroyAllWindows()