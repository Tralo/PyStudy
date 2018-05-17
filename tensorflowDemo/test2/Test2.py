# coding:utf-8

import tensorflow as tf
if __name__ == '__main__':

    sess = tf.Session()
    my_var = tf.Variable(tf.zeros([2, 3]))
    initialize_op = tf.global_variables_initializer()
    sess.run(initialize_op)



