# coding:utf-8
import tensorflow as tf
import numpy as np


if __name__ == '__main__':
    sess = tf.Session()
    identity_matrix = tf.diag([1.0, 1.0, 1.0])
    A = tf.truncated_normal([2, 3])
    B = tf.fill([2, 3], 5.0)
    C = tf.random_uniform([2, 3])
    D = tf.convert_to_tensor(np.array([[1., 2., 3.], [-3., -7., -1.],
                                       [0., 5., -2.]]))
    print(sess.run(identity_matrix))
    print(sess.run(A))
    print(sess.run(B))
    print(sess.run(C))
    print(sess.run(D))



    print(sess.run(A + B))
    print(sess.run(B - B))
    print(sess.run(tf.matmul(B, identity_matrix)))
