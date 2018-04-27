# -*- coding: utf-8 -*-
import requests
payload = {
    'Keywords':'blog:qiyeboy','pageindex':1
}
r = requests.get('http://zzk.cnblogs.com/s/blogpost',params=payload)
print(r.url)








