import zlib
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

import socket
import select
import sys

def main():
	port = 60005

	private_key = """-----BEGIN RSA PRIVATE KEY-----
	MIICXwIBAAKBgQCeNVj2v/gT/eHZm1RSH1w5dkzcMyhA/nbSrAV6KWiDCjKKXK1s
	i5+0llK9eUcCf55F5swag1JYzxxVaJQyMFUAImsVJ+3OMysYLDZCN2tAeYzlSZpt
	Ps/JY0KaFRNXinDG9EyaTdpvrC4d72KT8qw5eDwSgyR1XwJKoRUGYjki+wIDAQAB
	AoGBAICogaConOYlIPYGC5x9RFK2kerA74trZNYObqXZ5tQqBs/ebmpHYalKVh8f
	8U9m2R+fgXxOLzlptHEAiwQFqhkajreHrGHqLJ56Lu8M5f+xpjgRG6nITGDmAh0/
	y648jJiXe5cBvsNst1tPwdnRgJ+vaaGj6gJID93zgMXwLaMBAkEAx7wgupZWoSeD
	L37lFo8xZIHMaxckmSGUTLfiyaiRu0rU2NyoR/jM+ksWkaW9BfZuyl6iPPngvbST
	HHa9tgx5iQJBAMrGifQzh8FJPy+HcIP6DFsHXIrNFoT88DcwtF1vUQdaaYS096Vm
	87hxyNmQEIyED8VCuhDGGliDQUz7dlGzS2MCQQCaclHIlnn0ca5SashQ0nc6Jdhh
	Musc8kdPr53Rm+Tcs/e0naQOy0gNf0S7aTKqSq3PFLBVgE+Vwe1DxFncTPcpAkEA
	hVtvTPA63u5qJLsBT3q6d39u6EYbAllLLjDU3gIgmyJl9QYDPH9p2CrU+eiaSZ9s
	s8G/ltqCZyXjY1qZpP+ymwJBAMa9l2UCzDWah301zLF0VUmoqfE4U6mIX4WZ6xD5
	XKOsKpjktLf/HFexDELvO5RT5HL+75sdpu4aZoOLbz09F4Q=
	-----END RSA PRIVATE KEY-----"""

	Sockets = []
	S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	S.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	S.bind(('localhost', port))
	S.listen(1)


	conn, addr = S.accept()
	Sockets.append(conn)
	plaintext = 'GarbageTruck'

	while plaintext != 'exit':
		encrypted = conn.recv(1024)

		rsakey = RSA.importKey(private_key)
		rsakey = PKCS1_OAEP.new(rsakey)
		plaintext = rsakey.decrypt(encrypted)
		plaintext = zlib.decompress(plaintext)
		print plaintext

	S.close()

if __name__ == "__main__":
	main()