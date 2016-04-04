# video-streaming
Video Streaming using an existing video file of .Mjpeg format 
Convert the Video .Mjpeg file to the desired format using following ffmpeg commands: 1.scaling- ffmpeg -i input.avi -vf scale=320:240 output.avi (refer link https://trac.ffmpeg.org/wiki/Scaling%20%28resizing%29%20with%20ffmpeg) 2.convert pixel format to yuvj444p- ffmpeg -i R:\input.MOV -pix_fmt yuvj422p R:\ouput.MOV (refer link http://ffmpeg.gusari.org/viewtopic.php?f=16&t=1081)

Convert the Video .Mjpeg file to the desired format using following ffmpeg commands:
1.scaling-
ffmpeg -i input.avi -vf scale=320:240 output.avi
(refer link https://trac.ffmpeg.org/wiki/Scaling%20%28resizing%29%20with%20ffmpeg)
2.convert pixel format to yuvj444p-
ffmpeg -i R:\input.MOV -pix_fmt yuvj422p R:\ouput.MOV
(refer link http://ffmpeg.gusari.org/viewtopic.php?f=16&t=1081)
