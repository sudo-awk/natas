
import requests
import re

user = 'natas2'
password = 'h4ubbcXrWqsTo7GGnnUMLppXbOogfBZ7'
url = 'http://%s.natas.labs.overthewire.org' %user
proxies = {"http": "socks5://127.0.0.1:9050"}
# directory = '' 


resp = requests.get(url,auth=(user,password), proxies=proxies)
content = resp.text
print(content)


# print(re.findall('password (.*)', content))

# g9D9cREhslqBKtcA2uocGHPfMZVzeFK6
# h4ubbcXrWqsTo7GGnnUMLppXbOogfBZ7
