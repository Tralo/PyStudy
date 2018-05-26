# coding:utf-8
import matplotlib.pyplot as plt
import numpy as np
import requests
import tensorflow as tf
from sklearn import datasets
from sklearn.preprocessing import normalize
from tensorflow.python.framework import ops

if __name__ == '__main__':
    ops.reset_default_graph()
    sess = tf.Session()
    birthdata_url = 'https://www.umass.edu/statdata/statdata/data/'