# coding:utf-8

import tensorflow as tf
import numpy as np

if __name__ == '__main__':
    sess = tf.Session()
    print(sess.run(tf.div(3, 4)))
    print(sess.run(tf.truediv(3,4)))
    print(sess.run(tf.floordiv(3, 4)))
    print(sess.run(tf.mod(22, 6)))
    print(sess.run(tf.cross([1.0, 0, 0],[0, 1.0, 0])))




