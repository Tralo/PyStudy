# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib.request
def sechBodyUrl(path):
    text = BeautifulSoup(path, 'html.parser')
    urls = text.findAll('a')
    for u in urls:
        while True:
            if u['href'].startswith('//'):
                u['href'] = 'http://' + u['href'][2:]
            else:
                break
        print(u['href'])
    content = text.get_text().strip('\n')
    return content

with urllib.request.urlopen('http://www.baidu.com') as response:
    html = response.read()
sechBodyUrl(html)



