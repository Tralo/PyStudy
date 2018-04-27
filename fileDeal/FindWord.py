# -*- coding: utf-8 -*-

word_filter = set()

with open('D:/file.txt','r',encoding='UTF-8') as f:
    for w in f.readlines():
        print(w.strip())
        word_filter.add(w.strip())


while True:
    s = input("Please enter your key works:  ")
    if s == 'exit':
        break
    for w in word_filter:
        if w in s:
            s=s.replace(w,'*' * len(w))
    print(s)






    






