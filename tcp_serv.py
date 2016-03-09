import socket
import threading

class MyTh(threading.Thread):
	def __init__(self, channel, details, number):
		self.channel = channel
		self.details = details
		self.thrID = number
		threading.Thread.__init__(self)

	def run ( self ):
		#print('starting thread', self.thrID)
		while True:
			data = self.channel.recv(1024)
			#if not data: break
			if data == 'close': break	
			self.channel.send(data)
		#print('after close', self.thrID)
		self.channel.close()

        
        
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(10)

num = 1

while True:
	conn, addr = s.accept()
	MyTh(conn, addr, num).start()			
	num = num + 1
