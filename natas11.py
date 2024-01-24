#!/usr/bin/python3

# -*- coding: utf-8 -*-


import requests
import re
import urllib.parse
import base64

# This is the request instructions
name = 'natas11'
password = '1KFqoJXi6hRaPluAmk8ESDW4fSysRoIg'
url = 'http://%s.natas.labs.overthewire.org/' %name
# 

# this is the proxy
proxies = {'http': "socks5://127.0.0.1:9050"}
#,cookies = cookies

# this is for the cookies
cookies = {"data":"AAAAAAAAAAAAAAAAAAAAAAAXClEODkAFBAwDAx1QGBgBRQAAAAAARF8G"}
unproc_cookie = 'MGw7JCQ5OC04PT8jOSpqdmkgJ25nbCorKCEkIzlscm5oKC4qLSgubjY%3D'
proc_cookie = 'MGw7JCQ5OC04PT8jOSpqdmkgJ25nbCorKCEkIzlscm5oKC4qLSgubjY='

# this is the actual request
s = requests.Session()
response = s.get(url, data={"needle":"","submit":"submit"}, auth=(name,password) , proxies = proxies)

# print(response.cookies)
# print(urllib.parse.unquote(response.cookies['data']))
# print(base64.b64decode(urllib.parse.unquote_plus(response.cookies['data'])))

print(urllib.parse.unquote(orig_cookie))

# print(okay)


# print(b)
# print(base64.b64decode(cookies))
# print(a

# 





# content= response.text

# print(re.findall("<pre>(.*)</pre>",content))
# 1KFqoJXi6hRaPluAmk8ESDW4fSysRoIg