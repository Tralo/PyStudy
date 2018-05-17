# coding:utf-8

import numpy as np
import tensorflow as tf
if __name__ == '__main__':
    sess = tf.Session()
    x = tf.placeholder(tf.float32, shape=[2, 2])
    y = tf.identity(x)
    x_vals = np.random.rand(2, 2)
    print(sess.run(y, feed_dict={x: x_vals}))



