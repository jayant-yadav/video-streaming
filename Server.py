import socket
import sys, socket

from ServerWorker import ServerWorker
from threading import Thread
from SocketServer import ThreadingMixIn
from threading import Thread
from SocketServer import ThreadingMixIn


BUFFER_SIZE = 1024
SERVER_PORT=5001

            
class ClientThread(Thread):

    def __init__(self,ip,port,sock):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.sock = sock
        clientInfo={}
        
        try:
            SERVER_PORT = int(sys.argv[1])
        except:
            #print "[Usage: Server.py Server_port]\n"
        #threads=[]
        
        #while True:
            
            #print "hello baby"
            clientInfo['rtspSocket'] = (conn, (ip,port))
            #print clientInfo
            ServerWorker(clientInfo).run()    
            print " New thread started for "+ip+":"+str(port)
        

 

rtspSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
rtspSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
rtspSocket.bind(('localhost', SERVER_PORT))
threads = []

while True:
    rtspSocket.listen(5)
    print "Waiting for incoming connections..."
    #(conn, (ip,port)) = rtspSocket.accept()
    #clientInfo['rtspSocket'] = rtspSocket.accept()
    (conn, (ip,port))=rtspSocket.accept()

    print 'Got connection from ', (ip,port)
    newthread = ClientThread(ip,port,conn)
    print newthread
    newthread.start()
    threads.append(newthread)

for t in threads:
    t.join()