# coding:utf-8
import tensorflow as tf
import numpy as np

if __name__ == '__main__':
    sess = tf.Session()
    print(sess.run(tf.nn.relu([-3., 3., 10., -1, -5])))

    print(sess.run(tf.nn.relu6([-3., 5, 8, -2.])))


