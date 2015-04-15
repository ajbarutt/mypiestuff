import zlib
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

pub_key = """-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCeNVj2v/gT/eHZm1RSH1w5dkzc
MyhA/nbSrAV6KWiDCjKKXK1si5+0llK9eUcCf55F5swag1JYzxxVaJQyMFUAImsV
J+3OMysYLDZCN2tAeYzlSZptPs/JY0KaFRNXinDG9EyaTdpvrC4d72KT8qw5eDwS
gyR1XwJKoRUGYjki+wIDAQAB
-----END PUBLIC KEY-----"""

plaintext = "Hello World!"


print "Compressing %d bytes" % len(plaintext)

plaintext = zlib.compress(plaintext)

print "Encrypting %d bytes" % len(plaintext)

rsakey = RSA.importKey(pub_key)

rsakey = PKCS1_OAEP.new(rsakey)

encrypted = rsakey.encrypt(plaintext)

print encrypted

fp = open("Encrypted.txt", "w")

fp.write(encrypted)