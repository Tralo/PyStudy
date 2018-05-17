# coding:utf-8

import tensorflow as tf

if __name__ == '__main__':
    sess = tf.Session()
    W = tf.Variable([2.], tf.float32)
    b = tf.Variable([-3.], tf.float32)
    x = tf.placeholder(tf.float32)
    linear_model = W * x + b


    '''
    前面已经提到在调用 tf.constant 时会初始化不可变更的常量。 
    而这里通过调用 tf.Variable 创建的变量不会被初始化，
    为了在TensorFlow运行之前（sess.run执行模型运算之前）初始化所有的变量，
    需要增加一步 init 操作：
    '''
    init = tf.global_variables_initializer()
    sess.run(init)


    print(sess.run(linear_model, {x:[1,2,3,4]}))


    # 定义占位符
    y = tf.placeholder(tf.float32)

    # 方差计算
    squared_deltas = tf.square(linear_model - y)

    # 定义损益模型
    loss = tf.reduce_sum(squared_deltas)
    # 输出损益计算结果
    print(sess.run(loss, {x:[1,2,3,4], y:[0,-1,-2,-3]}))


    fixW = tf.assign(W, [-1.])
    fixb = tf.assign(b,[1.])
    sess.run([fixW,fixb])
    print(sess.run(loss, {x:[1,2,3,4], y:[0,-1,-2,-3]}))


    # 设定优化器，这里的 0.01 表示训练时的步进值
    optimizer = tf.train.GradientDescentOptimizer(0.01)
    train = optimizer.minimize(loss)
    sess.run(init)
    for i in range(1000):
        sess.run(train, {x:[1,2,3,4], y:[0,-1,-2,-3]})
    print(sess.run([W,b]))







