#!/usr/bin/python

import urllib2 as urllib
import re, sys, os, time

os.system('cls' if os.name == 'nt' else 'clear')

Links = []
LinksParsed = []
Emails = []
URLERR = 0
HTTPERR = 0

Address = "http://www.students.dsu.edu/dsu/tjflaagan"

Links.append(Address)

while Links:
	try:
		Current = Links.pop(0)
		Request = urllib.Request(Current)
		Request.add_header("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36")
		Page = urllib.urlopen(Request)

		HTML = Page.read()

		L = re.findall('"((http)s?://.*?)"', HTML)

		for Item in L:
			if Item[0] not in Links and Item[0] not in LinksParsed:
				Links.append(Item[0])

		for Item in HTML.split("\n"):
			if "mailto:" in Item:
				Mail = Item.split("mailto:")[1].split("\"")[0]
				if "?" in Mail:
					Mail = Mail.split("?")[0]
				
				if re.match("([^@]+@[^@]+\.[^@]+)", Mail):
					print "mail is valid"
					Emails.append(Mail)
					print Mail
	

		LinksParsed.append(Current)

	except urllib.HTTPerror, e:
		print e
		HTTPERR += 1
		continue

	except urllip.URLerror, e:
		URLERR += 1
		continue

	except Exception, e:
		print e
		continue

print "\n\n\n"
for Item in LinksParsed: print Item
print Emails