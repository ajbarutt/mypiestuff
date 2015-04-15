#!/usr/bin/python
#Server and Game
# Alex

import socket
import threading
import argparse, string, random
#	=================================== Server
#	servIP = "0.0.0.0"
#	servPort = 31337

#	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#	server.bind((servIP,servPort))
#	server.listen(5)

#	print "[* :) *] Listening on %s:%d" % (servIP,servPort)
	
	# Client handling thread
#def handle_client(client_socket):

# Printing data sent by client
#	request = client_socket.recv(1024)
	#print "[* :) *] Recieved: %s" % request
	
	# Send back
	#client_socket.send("ACK!")
	# Close
	#client_socket.close()

#	while True:
#		client,addr = server.accept()
#		print "[* :) *] Accepted Connection from %s:%d" % (addr[0],addr[1])
#
#		# Start client thread to handle incoming data
#		client_handler = threading.Thread(target=handle_client,args=(client,))
#		client_handler.start()

servIP = "0.0.0.0"
servPort = 31333
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((servIP,servPort))
server.listen(5)
print "[* :) *] Listening on %s:%d" % (servIP,servPort)
#def handle_client(client_socket:

	# Printing data sent by client
#request = client_socket.recv(1024)
#print "[* :) *] Recieved: %s" % request
		
# Send back
#client_socket.send("")
# Close
#client_socket.close()

client,addr = server.accept()
print "[* :) *] Accepted Connection from %s:%d" % (addr[0],addr[1])

	# Start client thread to handle incoming data
client_handler = threading.Thread(target=handle_client,args=(client,))
client_handler.start()
#		==========================================

class game():
	def __init__(self):
		
		p = argparse.ArgumentParser(prog='Hangman')

		p.add_argument('filename',
				action='store',
				type=str,
				help='Enter a filename with phrases')

		args = p.parse_args()
		if (args.filename):
			lines = open(args.filename).read().splitlines()
			myline = random.choice(lines)
	
		guesses = 0
		hold = 'abcdefghijklmnopqrstuvwxyz'
		myline = string.lower(myline)
		newguy = []
		cntlist = []
		for i in myline:
			if (i in hold):
				newguy.append("_")
				guesses = guesses + 1
				if (i not in cntlist):
					cntlist.append(i)
			elif (i == '-'):
				newguy.append("-")
			else:
				newguy.append(' ')		
				
		guy = ' '.join(newguy)
		client_socket.send(guy)
		self.startgame(cntlist, myline, newguy, guesses)
		
	def startgame(self, cntlist, myline, newguy, guesses):
			#=======================
		needed = 0
		for i in cntlist:
			needed = needed + 1

			
		orgguess = guesses	
		usedletters = []	
		progress = []
		correct = 0
		while guesses > 0:
				client_socket.send('You have %i guesses' % guesses)
				client_socket.send('\n\n')
				guess = client_socket.recv(1024)("Guess a letter: ")
				guess = string.lower(guess)
									
				
				if guess in myline:
					if guess not in usedletters:
						for x in guess:
							progress.append(x)
							correct = correct + 1
							guesses = guesses - 1
						client_socket.send("Correct Guess\n")
					else:
						client_socket.send("Already guessed\n")
				elif guess not in myline:
					if guess not in usedletters:
						client_socket.send("Incorrect\n")
						guesses = guesses - 1
					else:
						client_socket.send("Already guessed\n")
				
				
				
				keeper = 0
				for j in myline:		#This changes _ to correct letter when guessed
					if j in progress:
						newguy[keeper] = j
					keeper = keeper + 1
				
				usedletters.append(guess)
				client_socket.send(' '.join(newguy))
				if correct >= needed:
					break

		if correct >= needed:
			client_socket.send("YOU WON")
		else:
			client_socket.send("YOU.... LOST")	

def main():
	launch = game()
	client_socket.close()

if __name__ == '__main__':
	main()