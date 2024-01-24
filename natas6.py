#!/usr/bin/python3

import requests
import re

user = 'natas6'
password = 'fOIvE0MDtPTgRhqmmvvAOt2EfXR6uQgR'
url = 'http://%s.natas.labs.overthewire.org' %user

# headers = {"referer":"http://natas5.natas.labs.overthewire.org/"}

# resp = requests.get(url,auth=(user,password), headers = headers)

# jar = {"loggedin" : "1"}

session = requests.Session()
# resp = session.get(url, auth=(user,password), cookies = jar)
resp = session.get(url + '/index-source.html', auth=(user,password))

print(resp.text)



# content = resp.text

# print(content)

# print(re.findall('password (.*)', content))

