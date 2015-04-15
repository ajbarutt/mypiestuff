import shelve
from datetime import datetime

F = shelve.open("Shelf")
N = datetime.now()


try:
	F["stuff"] = {'int': 10, 'string': 'String of things'}
	F['Date1'] = N
except Exception, as e:
	print "[!] Error - " + str(e)

print F
F.close()

FA = shelve.open("Shelf.db")
print FA["Date1"]
