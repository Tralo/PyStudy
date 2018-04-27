# -*- coding: utf-8 -*-
from collections import OrderedDict
import xlwt,json

with open('D:\student.txt','r',encoding="utf-8") as f:
    data = json.load(f, object_pairs_hook=OrderedDict)
    workbook = xlwt.Workbook()
    sheet1 = workbook.add_sheet('student',cell_overwrite_ok=True)
    for index, (key,values) in enumerate(data.items()):
        sheet1.write(index,0,key)# (row,col,value)
        for i,value in enumerate(values):
            sheet1.write(index,i+1,value)
    workbook.save('D:\students.xls')


