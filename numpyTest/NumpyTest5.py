# coding:utf-8
from numpy import *
if __name__ == '__main__':
    a = ones(3, dtype=int32)
    b = linspace(0,pi,3)
    print(a)
    print(b)
    print(a + b)
    print(b.dtype.name)
    c = random.random((2,3))
    print(c)
    print(c.sum())
    print(c.max())
    print(c.min())

