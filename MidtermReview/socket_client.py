import socket
import argparse
import sys

def main():
	parser = argparse.ArgumentParser(prog="Socket Client", 
									description="Chat with the server")
	parser.add_argument("port", type=int, help="Port to connect to")
	parser.add_argument("IP", type=str, help="IP to connect to")

	args = parser.parse_args()

	port = args.port
	IP = args.IP

	S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	S.settimeout(5)

	try:
		S.connect((IP, port))
		while 1:
			Input = raw_input("Input stuff here:").rstrip()
			if Input == "exit":
				sys.exit(1)
			S.send(Input)

	except Exception, e:
		print "Error: " + str(e)


if __name__ == "__main__":
	main()