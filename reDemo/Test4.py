# coding:utf-8
import re


if __name__ == '__main__':
    pattern = re.compile(r'\d+')
    result = re.findall(pattern, 'fi48377vfjkjifd874312juhivsd8953j8v')
    if (result):
        print(result)
    else:
        print("匹配失败")




