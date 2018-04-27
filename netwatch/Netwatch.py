# -*- coding: utf-8 -*-
import requests
import urllib.request


if __name__ == '__main__':
    status = requests.get("http://www.baidu.com").status_code;
    print(status)

    codel = urllib.request.urlopen("https://www.baidu.com").code

    print(codel)







