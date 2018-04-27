# coding:utf-8
import requests
from lxml import html
import os
import time
from multiprocessing.dummy import Pool as ThreadPool
import re


index = 0

class NovelItem(object):
    def __init__(self,number,name,url):
        self.number = number
        self.name = name
        self.url = url

def header(referer):
    headers = {
        "Accept-Language":"zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3355.4 Safari/537.36",
        "Accept":"*/*",
        "Accept-Encoding":"gzip, deflate, br",

    }
    return headers

def getParentDirname():
    return u"D:/py小说/"

def getPrefixUrl():
    return 'https://www.xxbiquge.com'

def searchPageNovel(url):
    global index
    selector = html.fromstring(requests.get(url).content)
    results = list()
    try:

        allAs = selector.xpath('//div[@class="search-result-page-main"]/a')
        if allAs:   # 有分页
            ai = allAs[-1]
            pattern = re.compile(r'\d+')
            totalStr = re.search(pattern,ai.get('href'))
            # print(totalStr.group())


            for i in range(1,int(totalStr.group()) + 1):
                searchAllNovel(url + "&page="+ str(i), results)
            showData(results)


        else:       # 没分页
            searchAllNovel(url + "&page=1",results)
    except Exception as e:
        searchPageNovel(url)

def showData(list):
    for item in list:
        print('Number --> %d |||||||| Name --> %s |||||||| Url --> %s' % (item.number,item.name,item.url))
    print(list[-2])

def searchAllNovel(url,list):

    global index
    try:
        print(url)
        selector = html.fromstring(requests.get(url).content)
        allAs = selector.xpath('//div[@class="result-game-item-detail"]/h3[@class="result-item-title result-game-item-title"]/a')
        #print(allAs)
        for a in allAs:
            index+=1;
            url = a.get('href')
            #print(url)
            title = a.get('title')
            #print(title)
            item = NovelItem(number=index,name=title,url=url)
            list.append(item)



        # print(url)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    word = input('请输入你要搜索的小说:')
    url = getPrefixUrl() + "/search.php?keyword=" + word
    searchPageNovel(url)


