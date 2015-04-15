#!/usr/bin/python
# Second script
import re, argparse
import urllib2 as urllib
import urlparse as U

LinksParsed = []

def main():
	parser = argparse.ArgumentParser(prog="Url", 
									description="Url to check")
	parser.add_argument("Address", type=str, help="Url to use")
	parser.add_argument("Ofile", type=str, help="Output file to use")

	args = parser.parse_args()

	Address = args.Address
	Ofile = args.Ofile

	Req = urllib.Request(Address)
	Req.add_header("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/600.5.9 (KHTML, like Gecko) Version/8.0.5 Safari/600.5.9")
	Page = urllib.urlopen(Req)
	HTML = Page.read()

	L = re.findall('"((http)s?://.*?)"', HTML)

	for Item in L:
			if Item[0] not in LinksParsed:
				LinksParsed.append(Item[0])

	f = open(Ofile, "w")
	f.write(LinksParsed)
	f.close()




if __name__ == "__main__":
	main()