import argparse
import socket
import select
import sys

def main():
	parser = argparse.ArgumentParser(prog="Socket Server", 
									description="A socket server")
	parser.add_argument("port", type=int, help="Port to bind server to")

	args = parser.parse_args()

	Sockets = []

	S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	S.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	S.bind(('localhost', args.port))
	S.listen(1)

	conn, addr = S.accept()

	Sockets.append(conn)

	while 1:

		print conn.recv(1024)

if __name__ == "__main__":
	main()