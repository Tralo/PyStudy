# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup # html 解析包
import requests # url 请求
import shutil #文件操作包
import os

def gethtml(url):
    r=requests.get(url)
    return r.content

def analysehtml(html):
    soup = BeautifulSoup(html,'html.parser')
    body=soup.body
    #formatted stop

    ul=body.find('ul',attrs={"class":"gallery-thumbs"})
    for fig in ul.find_all('li'):
        src=fig.img.get('data-src')
        src=src.replace('thumb_jpg','large_jpg')
        saveimg(src)

def saveimg(photo_url):
    photo_name=photo_url.split("?")[0]
    photo_name=photo_name.rsplit("/",1)[-1]
    print(photo_name)
    photo_name=path+"//"+photo_name
    r=requests.get(photo_url)
# here we need to set stream=True parameter for streamingly reading

#save image
    with open(photo_name, 'wb') as f:
        f.write(r.content)
        f.close
#save image finished

URL = 'https://www.archdaily.com/883967/fabricated-scenery-hohai-beijing-tsuo-wonder-architects'
#项目页
html = gethtml(URL)
path=URL.rsplit("/",1)[-1]
os.mkdir(path) #创建一个目录
analysehtml(html)