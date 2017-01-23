import numpy as np
import cv2
import os
import subprocess

cap = cv2.VideoCapture(0)		

class VideoStream:
	def __init__(self, filename):
		self.filename = filename
		
		'''try:
			self.file = open(filename, 'rb')
		except:
			raise IOError'''
		self.frameNum = 0
		
	def nextFrame(self):
		"""Get next frame."""
		ret,frame=cap.read()
		if ret==True:
			cv2.imwrite('temp.jpg',frame)
			#cv2.imwrite('out2.jpg',frame)
			os.system("ffmpeg -i temp.jpg -vf scale=384:288 out1.jpg")
			#os.system("ffmpeg -i temp.jpg -vf scale=420:300 out1.jpg")
			#os.system("ffmpeg -i temp.jpg -vf scale=620:460 out1.jpg")
			#os.system("ffmpeg -i out1.jpg -pix_fmt yuvj444p out2.jpg")
			#os.system("ffmpeg -i temp.jpg -pix_fmt yuvj444p out1.jpg")

		data=1
		if data:
 	
			f= open('out1.jpg','rb')
			#f= open('temp.jpg','rb')
			q=open('temp1.Mjpeg','wb')
			q.write(f.read())
			f.close()
			q.close()
			f=open('temp1.Mjpeg','rb')
			data=f.read()
			f.close()
			os.system("rm out1.jpg")
			#os.system("rm out2.jpg")
		if ret==False:
			cap.release()
		self.frameNum += 1
		return data
		
	def frameNbr(self):
		"""Get frame number."""
		return self.frameNum
	
	
