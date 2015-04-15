import zlib
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import socket
import argparse
import sys


def main():
	port = 60005
	IP = '127.0.0.1'

	pub_key = """-----BEGIN PUBLIC KEY-----
	MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCeNVj2v/gT/eHZm1RSH1w5dkzc
	MyhA/nbSrAV6KWiDCjKKXK1si5+0llK9eUcCf55F5swag1JYzxxVaJQyMFUAImsV
	J+3OMysYLDZCN2tAeYzlSZptPs/JY0KaFRNXinDG9EyaTdpvrC4d72KT8qw5eDwS
	gyR1XwJKoRUGYjki+wIDAQAB
	-----END PUBLIC KEY-----"""


	S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	S.settimeout(5)

	try:
		S.connect((IP, port))
		while 1:
			plaintext = raw_input("What message should we encrypt?: ").rstrip()
			if plaintext == "stop":
				S.close()
				sys.exit(1)
				
			print "Compressing %d bytes" % len(plaintext)
			plaintext = zlib.compress(plaintext)
			print "Encrypting %d bytes" % len(plaintext)
			rsakey = RSA.importKey(pub_key)
			rsakey = PKCS1_OAEP.new(rsakey)
			encrypted = rsakey.encrypt(plaintext)
			S.send(encrypted)

	except Exception, e:
		print "Error: " + str(e)


if __name__ == "__main__":
	main()