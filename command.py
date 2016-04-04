import os
import subprocess
os.system("rm out.Mjpeg")
os.system("rm out1.Mjpeg")
os.system("rm out2.Mjpeg")
os.system("python camera.py")
#os.system(sleep(10))
os.system("ffmpeg -i out.Mjpeg -vf scale=384:288 out1.Mjpeg")
#os.system(sleep(10))
os.system("ffmpeg -i out1.Mjpeg -pix_fmt yuvj444p out2.Mjpeg")
#os.system(sleep(10))
os.system("python ClientLauncher.py")
subprocess.call(['ffprobe','-v','error','-show_entries','format=size','-of','default=noprint_wrappers=1:nokey=1','tempframe.Mjpeg'])

