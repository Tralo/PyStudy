# coding:utf-8
import json
from bs4 import BeautifulSoup
import requests
if __name__ == '__main__':
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3355.4 Safari/537.36'
    headers = {'User-Agent':user_agent}
    r=requests.get('http://seputu.com/',headers=headers)
    soup=BeautifulSoup(r.text,'html.parser')
    content = []
    for mulu in soup.find_all(class_='mulu')[1:]:
        h2=mulu.find('h2')
        if(h2!=None):
            h2_title=h2.string
        list=[]
        for a in mulu.find(class_='box').find_all('a'):
            href=a.get('href')
            box_title=a.get('title')
            list.append({'href':href,'box_title':box_title})
            content.append({'title':h2_title,'content':list})
    with open('qiye.json','w') as fp:
        json.dump(content,fp=fp, indent=4)



