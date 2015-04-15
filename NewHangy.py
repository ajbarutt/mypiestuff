#!/usr/bin/python
#Alex Barutt
#hangman.py

import argparse, string, random, socket, threading

class game():
	def __init__(self):

		def handle_client(client_socket):
		
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
				else:
					newguy.append(i)		
						
			tester = ' '.join(newguy)
			client_socket.send(tester)
			needed = 0
			for i in cntlist:
				needed = needed + 1

				
			orgguess = guesses	
			usedletters = []	
			progress = []
			correct = 0
			while guesses > 0:
					client_socket.send('\n')
					client_socket.send('You have %i guesses' % guesses)
					client_socket.send('\n\n')
					client_socket.send("Guess a Letter:")
					guess = client_socket.recv(1024)
					guess = guess.replace("\n", "")
					guess = string.lower(guess)
					client_socket.send("\n")
				
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
					test = ' '.join(newguy)
					client_socket.send(test)
					if correct >= needed:
						break

			if correct >= needed:
				client_socket.send("\n\nYOU WON\n\n")
			else:
				client_socket.send("\n\nYOU.... LOST\n\n")
			client_socket.close()


		servIP = "0.0.0.0"	# Listening on:
		servPort = 31358	# Port:

		server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server.bind((servIP,servPort))
		server.listen(5)
		print "[* :) *] Listening on %s:%d" % (servIP,servPort)

		while True:
			client,addr = server.accept()
			print "[* :) *] Accepted Connection from %s:%d" % (addr[0],addr[1])
			# Start client thread to handle incoming data
			client_handler = threading.Thread(target=handle_client,args=(client,))
			client_handler.start()
			

def main():

	launch = game()

if __name__ == '__main__':
	main()