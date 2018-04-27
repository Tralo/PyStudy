# coding:utf-8
import re

if __name__ == '__main__':
    s = 'i say, hello world! John Marry'
    p = re.compile(r'(\w+) (\w+)')
    print(p.subn(r'\2 \1', s))
