f= open('out.Mjpeg','rb')
#leng=f.read(5)
q=open('out1.Mjpeg','wb')
q.write(f.read())
f.close()
q.close()


