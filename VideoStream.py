import numpy as np
import cv2
import os
cap = cv2.VideoCapture('out2.Mjpeg')
class VideoStream:
	def __init__(self, filename):
		self.filename = filename
		
		try:
			self.file = open(filename, 'rb')
		except:
			raise IOError
		self.frameNum = 0
		
	def nextFrame(self):
		"""Get next frame."""
		ret,frame=cap.read()
		cv2.imwrite('temp.jpg',frame)
		#data = self.file.read(5) # Get the framelength from the first 5 bits
		#if data:
 		#	framelength = int(data)
		#	print framelength			
		# Read the current frame
		#f=open('temp261.Mjpeg','rb')

		#	data= self.file.read(framelength)
		#f.close()
	#		f.close()
		
		f= open('temp.jpg','rb')
#leng=f.read(5)
		q=open('temp.Mjpeg','wb')
		q.write(f.read())
		f.close()
		q.close()
		f=open('temp.Mjpeg','rb')
		data=f.read()
		f.close()
		if ret==False:
			cap.release()
		self.frameNum += 1
		return data
		
	def frameNbr(self):
		"""Get frame number."""
		return self.frameNum
	
	
