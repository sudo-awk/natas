#!/usr/bin/python3

import requests
import re

name = 'natas8'
password = 'a6bZCNYwdKqN5cGP11ZdtPg0iImQQhAB'

url = 'http://natas8.natas.labs.overthewire.org/'

resp = requests.post(url, data= {"secret":"oubWYf2kBq", "submit":"submit"}, auth=(name,password))

content = resp.text
# print(content)
flag = re.findall('Access granted. The password for natas9 is (.*)', content)


# this will print only the actual password without brackets
print(str(flag)[2:-2])
# Sda6t0vkOPkM8YeOZkAGVhFoaplvlJFd