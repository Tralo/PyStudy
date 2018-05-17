# coding:utf-8
from tensorflow.examples.tutorials.mnist import input_data

if __name__ == '__main__':
    mnist = input_data.read_data_sets('MNIST_data/', one_hot=True)
    print(len(mnist.train.images))
    print(len(mnist.test.images))
    print(len(mnist.validation.images))
    print(mnist.train.labels[1,:])




