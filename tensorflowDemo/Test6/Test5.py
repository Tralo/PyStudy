# coding:utf-8
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

if __name__ == '__main__':
    sess = tf.Session()
    # 数据集
    iris = datasets.load_iris()
    x_vals = np.array([x[3] for x in iris.data])
    y_vals = np.array([y[0] for y in iris.data])
    batch_size = 50
    # 模型
    x_data = tf.placeholder(shape=[None, 1], dtype=tf.float32)
    y_target = tf.placeholder(shape=[None, 1], dtype=tf.float32)
    A = tf.Variable(tf.random_normal(shape=[1, 1]))
    b = tf.Variable(tf.random_normal(shape=[1, 1]))
    model_output = tf.add(tf.matmul(x_data, A), b)
    demming_numerator = tf.abs(tf.subtract(y_target, tf.add(tf.matmul(x_data, A), b)))
    demming_denomiator = tf.sqrt(tf.add(tf.square(A), 1))
    loss = tf.reduce_mean(tf.truediv(demming_numerator, demming_denomiator))

    # 初始化变量(必须的!!!)
    init = tf.global_variables_initializer()
    sess.run(init)
    # 设置最低损值
    my_opt = tf.train.GradientDescentOptimizer(0.1)
    train_step = my_opt.minimize(loss)
    loss_vec = []
    # 开始训练
    for i in range(250):
        rand_index = np.random.choice(len(x_vals), size=batch_size)
        rand_x = np.transpose([x_vals[rand_index]])
        rand_y = np.transpose([y_vals[rand_index]])
        sess.run(train_step, feed_dict={x_data: rand_x, y_target: rand_y})
        temp_loss = sess.run(loss, feed_dict={x_data: rand_x, y_target: rand_y})
        loss_vec.append(temp_loss)
        if((i + 1) % 50 == 0):
            print('Step #' + str(i + 1) + ' A = ' + str(sess.run(A)) + ' b = ' + str(sess.run(b)))
            print('Loss = ' + str(temp_loss))
    [slope] = sess.run(A)
    [y_intercept] = sess.run(b)
    best_fit = []
    # 画图显示
    for i in x_vals:
        best_fit.append(slope * i + y_intercept)
    plt.plot(x_vals, y_vals, 'o', label='Data Points')
    plt.plot(x_vals, best_fit, 'r-', label='Best fit line', linewidth=3)
    plt.legend(loc='upper left')
    plt.title('Sepal Length vs Pedal Width')
    plt.xlabel('Pedal Width')
    plt.ylabel('Sepal Length')
    plt.show()


