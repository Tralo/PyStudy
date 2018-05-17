# coding:utf-8

import tensorflow as tf
if __name__ == '__main__':

    sess = tf.Session()

    a = tf.placeholder(tf.float32)
    b = tf.placeholder(tf.float32)
    adder_node = a + b
    print(sess.run(adder_node, {a:3, b:4.5}))
    print(sess.run(adder_node,{a:[3,8.5],b:[2,7.7]}))

    add_and_triple = adder_node * 3
    print(sess.run(add_and_triple,{a:[3,8.5],b:[2,7.7]}))
    print(sess.run(add_and_triple,{a:3, b:4.5}))


