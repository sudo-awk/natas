#!/usr/bin/python3

import requests
import re

user = 'natas1'
password = 'g9D9cREhslqBKtcA2uocGHPfMZVzeFK6'
url = 'http://%s.natas.labs.overthewire.org' %user

resp = requests.get(url,auth=(user,password))
content = resp.text

# print(content)

print(re.findall('password (.*)', content))

# g9D9cREhslqBKtcA2uocGHPfMZVzeFK6