# coding:utf-8

from sklearn import datasets

if __name__ == '__main__':
    iris = datasets.load_iris()
    print(len(iris.data))
    print(len(iris.target))
    print(iris.data[0])
    print(set(iris.data[0]))




