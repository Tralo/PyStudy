# coding:utf-8

import tensorflow as tf
if __name__ == '__main__':
    linear_tsr = tf.linspace(start=0.0,stop=1.0, num=3)

    sess = tf.Session()
    print(sess.run(linear_tsr))

