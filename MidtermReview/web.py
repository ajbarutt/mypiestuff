import urllib2 as urllib
import urlparse as U
import re

def main():
	P = "http://www.dsu.edu"
	Page = "http://www.dsu.edu"
	src = []

	Req = urllib.Request(Page)
	Req.add_header("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/600.5.9 (KHTML, like Gecko) Version/8.0.5 Safari/600.5.9")
	Page = urllib.urlopen(Req)
	HTML = Page.read()

	for item in HTML.split("\n"):
		if "src=\"" in item:
			item = item.split("src=\"")[1].split("\"")[0]

			if "http://" not in item:
				item = U.urljoin(P, item)
			print item

if __name__ == "__main__":
	main()