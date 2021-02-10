import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

def nothing(x):
  pass

#Define constants
prev_u = 0
G_MAX = 256
H_MAX = 3600
N = 601
C = 300
first_run = True
#create window
img = np.zeros((N, N, 3), np.uint8)
img2 = np.zeros((N, N, 3), np.uint8)
cv.namedWindow('image')
cv.createTrackbar('u','image',0,G_MAX-1,nothing)

while(1):
    final_image = np.hstack((img,img2))
    cv.imshow('image',final_image)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
       break
    #create track bar for u value
    u = cv.getTrackbarPos('u','image')
    if first_run:
        cv.setTrackbarPos('u','image',131)
        first_run = False
    if u != prev_u: #if u is different to prev u create a black image
        img = np.zeros((N, N, 3), np.uint8)
        img2 = np.zeros((N, N, 3), np.uint8)
        for h in range(0, H_MAX):
            for s in range(0,G_MAX):

                #calculate x and y 
                x = int(s * (np.cos(np.deg2rad(h/10))))
                y = int(s * (np.sin(np.deg2rad(h/10))))
                
                #get nearby rgb values 
                r = u + x/np.sqrt(2) + y/np.sqrt(6)
                g = u - 2*y/np.sqrt(6)
                b = u - x/np.sqrt(2) + y/np.sqrt(6)

                #add value rgb to 
                if r > 0 and g > 0 and b > 0:
                    if r < G_MAX and g < G_MAX and b < G_MAX:        
                        img[x+C,y+C] = np.array([b,g,r], np.uint8)
                        img2[x+C,y+C] = np.array([s,s,s], np.uint8)
    prev_u = u

cv.destroyAllWindows()