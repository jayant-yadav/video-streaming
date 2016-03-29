import cv2
import numpy as np
#f=open('temp10.Mjpeg','rb')

#print f.read()
#f.close()
#print len(f.read())
cap = cv2.VideoCapture('temp10.Mjpeg')

while(cap.isOpened()):
    ret, frame = cap.read()	
    if ret==True:
	cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    else:
        break

#f.close()

f=open('temp10.Mjpeg','rb')

#print f.read()
#f.close()
#print len(f.read())
f.close()
cap.release()
#out.release()
cv2.destroyAllWindows()
