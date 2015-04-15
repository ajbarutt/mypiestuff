#!/usr/bin/python
# First script
import json, socket, argparse, string

def main():
	parser = argparse.ArgumentParser(prog="Socket Client", 
									description="Send data to the server")
	parser.add_argument("port", type=int, help="Port to connect to")
	parser.add_argument("IP", type=str, help="IP to connect to")

	args = parser.parse_args()

	port = args.port
	IP = args.IP
	#print "port: %s ip: %s" % (port, IP)

	info = ()
	fname = raw_input("First name: ")
	lname = raw_input("Last name: ")
	year = raw_input("Year: ")
	home = raw_input("Hometown: ")
	school = raw_input("Highschool: ")


	obj = {u"Firstname": fname, u"Lastname": lname, u"Year": year, u"Hometown": home, u"School": school}
	jdata = json.dumps(obj)

	S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	S.settimeout(5)

	try:
		S.connect((IP, port))
		while 1:
			S.send(jdata)

	except Exception, e:
		print "Error: " + str(e)

if __name__ == "__main__":
	main()