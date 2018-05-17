# coding:utf-8
import tensorflow as tf
import numpy as np
import matplotlib as plt

if __name__ == '__main__':
    sess = tf.Session()
    x_vals = tf.linspace(-1., 1., 500)
    target = tf.constant(0.)

    l2_y_vals = tf.square(target - x_vals)
    l2_y_out = sess.run(l2_y_vals)

    l1_y_vals = tf.abs(target - x_vals)
    l1_y_out = sess.run(l1_y_vals)

    delta1 = tf.constant(0.25)
    phuber1_y_value = tf.multiply(tf.square(delta1), tf.sqrt(1. +
                                                             tf.square((target - x_vals) /delta1)) - 1.)

    phuber1_y_out = sess.run(phuber1_y_value)
    delta2 = tf.constant(5.)
    phuber2_y_value = tf.multiply(tf.square(delta2), tf.sqrt(1. +
                                                             tf.square((target - x_vals) / delta2)) - 1.)

    phuber2_y_out = sess.run(phuber2_y_value)

    x_vals = tf.linspace(-3., 5., 500)
    target = tf.constant(1.)
    targets = tf.fill([500,], 1.)






