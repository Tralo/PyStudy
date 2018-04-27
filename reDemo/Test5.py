# coding:utf-8
import re
if __name__ == '__main__':
    p = re.compile(r'(?P<word1>\w+) (?P<word2>\w+)')
    s = 'i say, hello world!'
    print(p.sub(r'\g<word2> \g<word1>',s))

    p = re.compile(r'(\w+) (\w+)')
    print(p.sub(r'\2 \1',s))








