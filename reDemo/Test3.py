# coding:utf-8
import re
if __name__ == '__main__':
    pattern = re.compile(r'\d+')
    result = re.split(pattern, 'A8BC884U3LKJSDFK889F9A890KNM')
    if (result):
        print(result)
    else:
        print('匹配失败')








