import sys, signal
from Tkinter import Tk
from Client import Client

def signal_handler(signal, frame):
    print '\nbyebye!'
    sys.exit(0)

if __name__ == "__main__":
	signal.signal(signal.SIGINT,signal_handler)
	try:
		serverAddr = sys.argv[1]
		serverPort = sys.argv[2]
		rtpPort = sys.argv[3]
		fileName = sys.argv[4]	
	except:
		print "[Usage: ClientLauncher.py Server_name Server_port RTP_port Video_file]\n"	
	
	root = Tk()
	serverAddr="localhost"
	#serverAddr="192.168.43.170"
	serverPort=5001
	rtpPort=30000
	fileName="out.Mjpeg"
	app = Client(root, serverAddr, serverPort, rtpPort, fileName)
	app.master.title("RTPClient")	
	root.mainloop()
	
