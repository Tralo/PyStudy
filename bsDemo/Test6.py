# coding:utf-8

import urllib.request
from lxml import etree
import requests
def Schedule(blocknum, blocksize, totalsize):
    per = 100.0 * blocknum * blocksize / totalsize
    if(per > 100):
        per = 100
    print('当前下载进度: %d' % per)

if __name__ == '__main__':
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3355.4 Safari/537.36'
    headers = {'User-Agent':user_agent}
    r = requests.get('http://www.ivsky.com/tupian/ziranfengguang/',headers=headers)
    html = etree.HTML(r.text)
    img_urls = html.xpath('.//img/@src')
    i = 0
    for img_url in img_urls:
        urllib.request.urlretrieve(img_url, 'img' + str(i) + '.jpg', Schedule)
        i+=1






