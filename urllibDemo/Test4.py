# -*- coding: utf-8 -*-
import requests
r = requests.get('http://www.baidu.com')
print('content --> %s'% r.content)
print('text    --> %s' % r.text.encode('utf-8'))
print('encoding--> %s' %r.encoding)




