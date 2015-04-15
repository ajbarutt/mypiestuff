#!/usr/bin/python
# duh server

import socket
import threading

servIP = "0.0.0.0"
servPort = 31337

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((servIP,servPort))
server.listen(5)

print "[* :) *] Listening on %s:%d" % (servIP,servPort)

# Client handling thread
def handle_client(client_socket):

	# Printing data sent by client
	request = client_socket.recv(1024)
	print "[* :) *] Recieved: %s" % request
	
	# Send back
	client_socket.send("ACK!")
	# Close
	client_socket.close()

while True:
	client,addr = server.accept()
	print "[* :) *] Accepted Connection from %s:%d" % (addr[0],addr[1])

	# Start client thread to handle incoming data
	client_handler = threading.Thread(target=handle_client,args=(client,))
	client_handler.start()