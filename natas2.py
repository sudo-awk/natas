#!/usr/bin/python3

import requests
import re

user = 'natas2'
password = 'h4ubbcXrWqsTo7GGnnUMLppXbOogfBZ7'
url = 'http://%s.natas.labs.overthewire.org/files/users.txt' %user
# directory = '' 


resp = requests.get(url,auth=(user,password))
content = resp.text

print(content)

# print(re.findall('password (.*)', content))

# g9D9cREhslqBKtcA2uocGHPfMZVzeFK6
# h4ubbcXrWqsTo7GGnnUMLppXbOogfBZ7
# G6ctbMJ5Nb4cbFwhpMPSvxGHhQ7I6W8Q