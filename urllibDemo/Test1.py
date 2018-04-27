# -*- coding: utf-8 -*-
import urllib.request

if __name__ == '__main__':
    response = urllib.request.urlopen('http://zhihu.com')
    html = response.read()
    print(html)





