import socket
import threading

class MyTh(threading.Thread):
	def __init__(self, channel, details):
		self.channel = channel
		self.details = details
		threading.Thread.__init__(self)

	def run ( self ):		
		client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		client.connect(('127.0.0.1', 1249))		
		client.send("close")
		#while True:
		data = client.recv(1024)
		#	if not data: break
		print(data)
		#	if data == 'close': break
		#	conn.send(data)
		client.close()

#s.listen(10)
#while True:
#for x in range(10):
#	conn, addr = s.accept()
MyTh(1, 2).start()			
