#!/usr/bin/python3

import requests
import re

user = 'natas0'
password = 'natas0'
url = 'http://%s.natas.labs.overthewire.org' %user

resp = requests.get(url,auth=(user,password))
content = resp.text


print(re.findall('<!--The password for natas1 is (.*) -->', content))