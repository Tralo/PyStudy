import tensorflow as tf
import numpy as np
if __name__ == '__main__':
    x = np.asarray([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
    x_p = tf.placeholder(tf.int32, [2, 2, 3])
    y = tf.reduce_sum(x_p, 0)  # 修改这里
    with tf.Session() as sess:
        y = sess.run(y, feed_dict={x_p: x})
        print(y)
