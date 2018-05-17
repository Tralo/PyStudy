# coding:utf-8
import tensorflow as tf


if __name__ == '__main__':
    node1 = tf.constant(3.0, tf.float32)
    node2 = tf.constant(4.0)
    print(node1, node2)

    sess = tf.Session()
    print(sess.run([node1,node2]))

    node3 = tf.add(node1,node2)
    print("sess.run(node3):  ", sess.run(node3))





