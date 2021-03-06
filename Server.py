import sys, socket

from ServerWorker import ServerWorker

class Server:	
	
	def main(self):
		try:
			SERVER_PORT = int(sys.argv[1])
		except:
			print "[Usage: Server.py Server_port]\n"
		rtspSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		SERVER_PORT=5001
		rtspSocket.bind(('', SERVER_PORT))
		rtspSocket.listen(5)        

		# Receive client info (address,port) through RTSP/TCP session
		while True:
			clientInfo = {}
			clientInfo['rtspSocket'] = rtspSocket.accept()
			ServerWorker(clientInfo).run()	
			#print clientInfo	

if __name__ == "__main__":
	(Server()).main()
	#print clientInfo


