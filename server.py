#!/usr/bin/python
#server.py

import argparse, socket, select

def broadcast(sock,message):
	
	for socket in sockets:
		if socket != s and socket != sock:
			try:
				socket.send(message)
			except:
				socket.close()
				sockets.remove(socket)

if __name__ == '__main__':

	parser = argparse.ArgumentParser(prog="Chat Server",
										description="Chat with me")
										
	parser.add_argument('port',
			type=int,
			help="Port number to bind")
			
	args = parser.parse_args()
	
	sockets = []
	
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
	s.bind(("0.0.0.0",args.port))
	s.listen(10)
	
	sockets.append(s)
	
	while 1:
		
		read_socks,write_socks,error_socks = select.select(sockets,[],[])
		
		for socket in read_socks:
			if socket == s:
				sockfd,addr = s.accept()
				sockets.append(sockfd)
				broadcast(socket, "[%s:%s] entered room\n" % addr)
				# Broadcast Join Message
			else:
				try:
					data = socket.recv(4096)
					if data:
						broadcast(socket,"\r" + "<" + str(socket.getpeername()) + ">" + data)
				except:
					broadcast(socket,"Client [%s:%s] if offline" % addr)
					socket.close()
					sockets.remove(socket)
					continue