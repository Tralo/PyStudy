# coding:utf-8
import tensorflow as tf
import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt


if __name__ == '__main__':
    sess = tf.Session()
    iris = datasets.load_iris()



    init = tf.global_variables_initializer()
    sess.run(init)