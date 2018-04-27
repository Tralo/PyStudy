# -*- coding: utf-8 -*-
import requests
import chardet
if __name__ == '__main__':
    r = requests.get('http://www.baidu.com')
    print (chardet.detect(r.content))
    r.encoding = chardet.detect(r.content)['encoding']

    print(r.text)



