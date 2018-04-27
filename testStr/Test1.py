# -*- coding: utf-8 -*-

str1 = "k:1|k2:2|k3:3|k4:4"
str_list = str1.split('|')
print(str_list)
d={}
for i in str_list:
    key,value=i.split(':')
    d[key]=value
print(d)