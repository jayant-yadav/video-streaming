import numpy as np
import cv2
#import base64

#f= open('movie.Mjpeg','wb')


cap = cv2.VideoCapture('out.Mjpeg')
#Define the codec and create VideoWriter object
#fourcc = cv2.VideoWriter_fourcc(*'MJPG')
fourcc = cv2.cv.CV_FOURCC('M','J','P','G')
#out = cv2.VideoWriter('out.Mjpeg',fourcc, 10, (320,240),True)
#out = cv2.VideoWriter('out1.Mjpeg',fourcc, 25, (640,480),True)
#out = cv2.VideoWriter('movie.Mjpeg',-1, 25, (640,480))
j=0;
while(cap.isOpened()):
    
    ret, frame = cap.read()
    	
    if ret==True:
	#ret1 = cap.set(3,int(320))
    	#ret2 = cap.set(4,int(240))
	#print ret1,ret2
	#cv2.imwrite('temp'+str(j)+'.jpg',frame)
	#i=open('temp'+str(j)+'.Mjpeg','wb')
	#j+=1
	k=open('out1.Mjpeg','wb')
	k.write(frame)
	#i.write(frame)
        #frame = cv2.flip(frame,0)
        # write the flipped frame
        #out.write(base64.b64decode(frame))
	#f.write(frame)
	#(thresh, im_bw) = cv2.threshold(frame, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
	#cv2.imwrite('movie.Mjpeg', im_bw)
	#out.write(frame)
	#print len(frame)
	#fwrite(gray.data, sizeof(unsigned char), 640*480,f);
        cv2.imshow('frame',frame)
	#s, jpeg=cv2.imencode('.jpg',frame)
	#if s is not None:
	#	out.write(jpeg.tostring())
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
#f.close()
