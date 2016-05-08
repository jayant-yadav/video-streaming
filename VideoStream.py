import numpy as np
import cv2
import subprocess
#self.cap = cv2.Videoself.capture('out.Mjpeg')
class VideoStream:
	def __init__(self, filename):
		self.filename = filename
		self.cap = cv2.VideoCapture(self.filename+'.Mjpeg')
		
		'''try:
			#self.cap = cv2.video.capture(self.filename+'.Mjpeg')
			#self.file = open(self.filename, 'rb')
		except:
			raise IOError'''
		self.frameNum = 0
		
	def nextFrame(self):
		"""Get next frame."""
		ret,frame=self.cap.read()
		cv2.imwrite(self.filename+'temp.jpg',frame)
		data=1
		if data:
			print "manish chutiya"
 	
			f= open(self.filename+'temp.jpg','rb')
			q=open(self.filename+'temp.Mjpeg','wb')
			q.write(f.read())
			f.close()
			q.close()
			f=open(self.filename+'temp.Mjpeg','rb')
			data=f.read()
			f.close()
		if ret==False:
			self.cap.release()
		self.frameNum += 1
		return data
		
	def frameNbr(self):
		"""Get frame number."""
		return self.frameNum
	
	
