import cv2

path='Jorel.mp4'
cap = cv2.VideoCapture(path)

i=0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    if(i%24 == 0):
        cv2.imwrite('Frames/Jorel'+str(int(i/24))+'.jpg',frame)
    i+=1
 
cap.release()
cv2.destroyAllWindows()
