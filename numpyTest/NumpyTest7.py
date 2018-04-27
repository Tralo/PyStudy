# coding:utf-8
from numpy import *
if __name__ == '__main__':
    a = floor(10 * random.random((2,2)))
    b = floor(10 * random.random((2,2)))

    print(a)
    print(b)
    print(vstack((a,b)))

    print(hstack((a,b)))



