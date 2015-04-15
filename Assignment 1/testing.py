#!/usr/bin/python
#Alex Barutt
import sys

def primecheck(val):
	for i in xrange(2, val):
		if (val % i) == 0:
			return False
	return True
			
usrval = int(raw_input("Pick an integer: "))
primelist = [];



for x in xrange(2, usrval):
	if primecheck(x):
		primelist.append(x)

num = 0
counter = 0

#	Using num to access each index of the primelist
#	Using counter to count everytime it finds a twin prime pair

for primey in primelist:
	if primelist[num] + 2 in primelist:
		counter = counter + 1
	num = num+1
	
print "Result: %i" % counter