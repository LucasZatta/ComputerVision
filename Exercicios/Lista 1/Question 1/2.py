import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


img = cv.imread('landscape.png')
color = ('b','g','r')
plt.figure()
for index,col in enumerate(color):
    histogram = cv.calcHist([img],[index],None,[256],[0,256])
    plt.plot(histogram,color = col)
    plt.xlim([0,256])
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()