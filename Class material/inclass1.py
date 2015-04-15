F = open("emails.txt", "r")

#for line in open("emails.txt", "r"):
#	print line

with open("emails.txt", "r") as f:
	data = f.readlines()
	
#print data

W = open("output.txt", "w")

for item in data:
	item = item.split("@")[1]
	W.write(item)