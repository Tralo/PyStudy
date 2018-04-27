# coding:utf-8
from lxml import etree
import requests


if __name__ == '__main__':
    response = requests.get('http://www.baidu.com')
    html = response.text
    



