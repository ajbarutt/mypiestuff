#!/usr/bin/python
#Alex Barutt
#hangman.py

import argparse, string, random

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
		test = ' '.join(newguy)		
		#print ' '.join(newguy)
		print test
		self.startgame(cntlist, myline, newguy, guesses)
		
	def startgame(self, cntlist, myline, newguy, guesses):
		
		needed = 0
		for i in cntlist:
			needed = needed + 1

			
		orgguess = guesses	
		usedletters = []	
		progress = []
		correct = 0
		while guesses > 0:
				print 'You have %i guesses' % guesses
				print '\n\n'
				guess = raw_input("Guess a letter: ")
				guess = string.lower(guess)
									
				
				if guess in myline:
					if guess not in usedletters:
						for x in guess:
							progress.append(x)
							correct = correct + 1
							guesses = guesses - 1
						print "Correct Guess\n"
					else:
						print "Already guessed\n"
				elif guess not in myline:
					if guess not in usedletters:
						print "Incorrect\n"
						guesses = guesses - 1
					else:
						print "Already guessed\n"
				
				
				
				keeper = 0
				for j in myline:		#This changes _ to correct letter when guessed
					if j in progress:
						newguy[keeper] = j
					keeper = keeper + 1
				
				usedletters.append(guess)
				print ' '.join(newguy)
				if correct >= needed:
					break

		if correct >= needed:
			print "YOU WON"
		else:
			print "YOU.... LOST"	

def main():

	launch = game()

if __name__ == '__main__':
	main()