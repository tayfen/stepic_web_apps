import socket
import threading

class MyTh(threading.Thread):
	def __init__(self, channel, details):
		self.channel = channel
		self.details = details
		threading.Thread.__init__(self)

	def run ( self ):
		#while True:
		#	data = conn.recv(1024)
		#	if not data: break
		print('waiting for a connection')
		#	if data == 'close': break
		#	conn.send(data)
		#conn.close()

        
        
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.bind(('0.0.0.0', 2222))
#s.listen(10)

#while True:
for x in range(10):
#	conn, addr = s.accept()
	MyTh(1, 2).start()			
