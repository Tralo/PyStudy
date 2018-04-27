# coding:utf-8
from numpy import *
if __name__ == '__main__':
    a = ones((2,3), dtype=int) * 4
    b = random.random((2,3)) * 4
    print(a)
    print(b)
    b += a
    print(b)



