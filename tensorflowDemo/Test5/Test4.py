# coding:utf-8
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

if __name__ == '__main__':
    sess = tf.Session()
    x_vals = np.random.normal(1, 0.1, 100)
    y_vals = np.repeat(10., 100)
    x_data = tf.placeholder(shape=[None, 1], dtype=tf.float32)
    y_target = tf.placeholder(shape=[None, 1], dtype=tf.float32)
    batch_size = 25
    train_indices = np.random.choice(len(x_vals), round(len(x_vals) * 0.8), replace=False)
    test_indices = np.array(list(set(range(len(x_vals)))))
    x_vals_train = x_vals[train_indices]
    x_vals_test = x_vals[test_indices]
    y_vals_train = y_vals[train_indices]
    y_vals_test = y_vals[test_indices]
    A = tf.Variable(tf.random_normal(shape=[1, 1]))


    my_output = tf.matmul(x_data, A)
    loss = tf.reduce_mean(tf.square(my_output - y_target))
    init = tf.initialize_all_variables()
    sess.run(init)
    my_opt = tf.train.GradientDescentOptimizer(0.02)
    train_step = my_opt.minimize(loss)

    for i in range(100):
        rand_index = np.random.choice(len(x_vals_train), size=batch_size)
        rand_x = np.transpose([x_vals_train[rand_index]])
        rand_y = np.transpose([y_vals_train[rand_index]])
        sess.run(train_step, feed_dict={x_data: rand_x, y_target:rand_y})
        if((i + 1) % 25 == 0):
            print('Step #' + str(i + 1) + ' A = ' + str(sess.run(A)))
            print('Loss = ' + str(sess.run(loss, feed_dict={x_data: rand_x, y_target: rand_y})))











