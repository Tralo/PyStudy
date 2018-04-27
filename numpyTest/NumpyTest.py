# coding:utf-8

from numpy import *


if __name__ == '__main__':
    a = arange(1000).reshape(5, 200)
    print(a)
    print(a.shape)
    print(a.ndim)
    print(a.dtype.name)
    print(a.itemsize)
    print(a.size)
    print(type(a))



    b = array([6,7,8])
    print(b)
    print(type(b))
    print(type(a) == type(b))


    c = arange(48).reshape(2,2,3,4)
    print(c)





