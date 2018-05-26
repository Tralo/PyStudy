# coding:utf-8

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn import datasets
if __name__ == '__main__':
    sess = tf.Session()
    iris = datasets.load_iris()
    binary_target = np.array([1. if x== 0 else 0. for x in iris.target])
    iris_2d = np.array([[x[2], x[3]] for x in iris.data])

    batch_size = 20
    x1_data = tf.placeholder(shape=[None, 1], dtype=tf.float32)
    x2_data = tf.placeholder(shape=[None, 1], dtype=tf.float32)
    y_target = tf.placeholder(shape=[None, 1], dtype=tf.float32)
    A = tf.Variable(tf.random_normal(shape=[1, 1]))
    b = tf.Variable(tf.random_normal(shape=[1, 1]))
    my_mult = tf.matmul(x2_data, A)
    my_add = tf.add(my_mult, b)
    my_output = tf.subtract(x1_data, my_add)

    xentropy = tf.nn.sigmoid_cross_entropy_with_logits(labels=my_output, logits=y_target)
    my_opt = tf.train.GradientDescentOptimizer(0.05)
    train_step = my_opt.minimize(xentropy)


    init = tf.initialize_all_variables()
    sess.run(init)


    for i in range(1000):
        rand_index = np.random.choice(len(iris_2d),size=batch_size)
        rand_x = iris_2d[rand_index]
        rand_x1 = np.array([[x[0]] for x in rand_x])
        rand_x2 = np.array([[x[1]] for x in rand_x])
        rand_y = np.array([[y] for y in binary_target[rand_index]])
        sess.run(train_step, feed_dict={x1_data:rand_x1, x2_data: rand_x2, y_target:rand_y})
        if( (i + 1 )% 200 == 0):
            print('Step #' + str(i + 1) + ' A = ' + str(sess.run(A)) + ', b = ' + str(sess.run(b)))




