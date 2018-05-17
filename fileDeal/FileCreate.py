# -*- coding: utf-8 -*-
postfix='.txt'
with open('D:/codes.txt','r',encoding='UTF-8') as f:
    while True:
        lines = f.readlines()
        if not lines: break
        for line in lines:
            file_out=str('_'.join(line.split()[:])) + postfix
            open(file_out,'w').write(line)




