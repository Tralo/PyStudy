# coding:utf-8
import re


if __name__ == '__main__':
    pattern = re.compile(r'\d+')
    result1 = re.search(pattern, 'abc192def89432897fkjlasdsfjklajkl')
    if (result1):
        print(result1.group())
    else:
        print('匹配失败')





