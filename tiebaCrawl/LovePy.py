# -*- coding: utf-8 -*-
import os
import requests
from bs4 import BeautifulSoup
url = 'http://tieba.baidu.com/p/2166231880'
html = requests.get(url)
soup = BeautifulSoup(html.text,'html.parser')
img_urls = soup.findAll('img',pic_type="0")
count = 1
for img_url in img_urls:
    img_src = img_url['src']
    with open('D:/source/'+('%s.jpg'% count),'wb') as f:
        f.write(requests.get(img_src).content)
        count += 1


