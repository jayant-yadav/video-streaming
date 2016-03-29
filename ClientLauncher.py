import sys, signal
from Tkinter import Tk
from Client import Client

def signal_handler(signal, frame):
    print '\nGoodbye!'
    sys.exit(0)

if __name__ == "__main__":
	# setup terminator
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
	serverPort=5000
	rtpPort=30000
	fileName="out1.Mjpeg"
	# Create a new client
	app = Client(root, serverAddr, serverPort, rtpPort, fileName)
	app.master.title("RTPClient")	
	root.mainloop()
	
